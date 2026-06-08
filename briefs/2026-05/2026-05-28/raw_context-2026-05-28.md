# 破晓 PoXiao — 原始数据 (Raw Context)
生成时间: 2026-05-29 06:30 UTC
================================================================================

[RSS:Reddit LocalLLaMA (社区共识)]
I've just benchmarked myself:
https://www.reddit.com/r/LocalLLaMA/comments/1tqbnpq/ive_just_benchmarked_myself/
&#32; submitted by &#32; /u/JLeonsarmiento [link] &#32; [comments]
---

[RSS:Reddit LocalLLaMA (社区共识)]
Zai replaced the network architecture running GLM-5.1 inference and the gains are pretty wild
https://www.reddit.com/r/LocalLLaMA/comments/1tq35a0/zai_replaced_the_network_architecture_running/
Been following the infrastructure side of AI more lately and stumbled on this from Zai. They upgraded the network architecture on a thousand-GPU cluster running GLM-5.1 coding inference from the standard ROFT setup to something they built called ZCube, developed with Tsinghua University and HarnetsA
---

[RSS:Reddit LocalLLaMA (社区共识)]
StepFun 3.7 Flash
https://www.reddit.com/r/LocalLLaMA/comments/1tqloii/stepfun_37_flash/
StepFun dropped Step 3.7 Flash, 196B total / 11B active MoE, runs locally on 128GB RAM It's a multimodal MoE (196B total params, only 11B active) with a built-in 1.8B ViT for vision. Benchmark highlights vs. other flash-tier models: - SWE-Bench Pro: 56.26% (beats DeepSeek V4 Flash at 55.6%, matches 
---

[RSS:Reddit LocalLLaMA (社区共识)]
LiquidAI/LFM2.5-8B-A1B · Hugging Face
https://www.reddit.com/r/LocalLLaMA/comments/1tq8a40/liquidailfm258ba1b_hugging_face/
looks like you can run it on any potato (A1B)! https://huggingface.co/LiquidAI/LFM2.5-8B-A1B-GGUF from LiquidAI: LFM2.5 is a new family of hybrid models designed for on-device deployment. It builds on the LFM2 architecture with extended pre-training and reinforcement learning. On-device personal ass
---

[RSS:Reddit LocalLLaMA (社区共识)]
Reachy Mini goes fully local!
https://www.reddit.com/r/LocalLLaMA/comments/1tq4x48/reachy_mini_goes_fully_local/
Hi! Andi from Hugging Face here! My team has been working over the last few months on creating a super smooth local experience for conversations with Reachy Mini, see the video! We hope people can extend this into tons of different cool use-cases. We wrote a blog explaining how to set this up, and h
---

[RSS:Reddit LocalLLaMA (社区共识)]
HF models page now has a "Base only" toggle to filter out finetunes/quants/etc
https://www.reddit.com/r/LocalLLaMA/comments/1tq2ce9/hf_models_page_now_has_a_base_only_toggle_to/
a feature that was requested a lot: https://huggingface.co/models?base_model_relation=base &#32; submitted by &#32; /u/paf1138 [link] &#32; [comments]
---

[RSS:Reddit LocalLLaMA (社区共识)]
Upgrade path from 4x 3090s
https://www.reddit.com/r/LocalLLaMA/comments/1tqfzvs/upgrade_path_from_4x_3090s/
Hey everyone, looking for some upgrade advice. Right now, I’m running 4x 3090s hosting Qwen 3.6 27B 128K in full precision. It's a great model, but I'm looking for a step up and trying to figure out the best &quot;middle-tier&quot; hardware path. I've seen people here mention running 8x 3090s (192GB
---

[RSS:Reddit LocalLLaMA (社区共识)]
My new home office radiator 🥵
https://www.reddit.com/r/LocalLLaMA/comments/1tpx984/my_new_home_office_radiator/
4 x RTX Pro Max-Q We will not speak about the 64GB system RAM... &#32; submitted by &#32; /u/lantern_lol [link] &#32; [comments]
---

[RSS:Reddit LocalLLaMA (社区共识)]
Mimo 2.5 Pro - 40t/s on 8x Nvidia Spark/GB10 cluster
https://www.reddit.com/r/LocalLLaMA/comments/1tqf5mi/mimo_25_pro_40ts_on_8x_nvidia_sparkgb10_cluster/
I got Mimo 2.5 Pro running on my 8x Asus Nvidia GB10 cluster using mtp-2, single user request, coding: 40 t/s - 1k context, 32t/s - 30k context, 25t/s - 125k context, 17t/s - 250k context. 2 parallel reached 60t/s and in 4 parallel reached 83t/s, not bad for 1T model. Works just fine with open code 
---

[RSS:Reddit LocalLLaMA (社区共识)]
How much total VRAM (or shared RAM for Mac/Halo/etc) do you have on your local server/PC?
https://www.reddit.com/r/LocalLLaMA/comments/1tqh44n/how_much_total_vram_or_shared_ram_for_machaloetc/
View Poll &#32; submitted by &#32; /u/panchovix [link] &#32; [comments]
---

[RSS:Reddit LocalLLaMA (社区共识)]
Qwen3.6 35B - TXT vs Markdown vs HTML vs HTML+CSS
https://www.reddit.com/r/LocalLLaMA/comments/1tq7yeq/qwen36_35b_txt_vs_markdown_vs_html_vs_htmlcss/
Theres been talk of late about using HTML rather than markdown in Claude Code. I was curious how this worked with a local model so loaded up Qwen3.6 35B A3B at Q8 and F16 KV cache. Then I gave it the same prompt write a detailed explanation of the Blazor render cycle first asking for raw text, then 
---

[RSS:Reddit LocalLLaMA (社区共识)]
Vulnerability found in framework used by VLLM, many MCP servers, and other LLM tools
https://www.reddit.com/r/LocalLLaMA/comments/1tpp2th/vulnerability_found_in_framework_used_by_vllm/
Worth taking a look to see if this affects any of you. Surprised nobody has posted it yet. &#32; submitted by &#32; /u/Hrethric [link] &#32; [comments]
---

[RSS:Reddit LocalLLaMA (社区共识)]
Got searxng working on windows without docker/wsl
https://www.reddit.com/r/LocalLLaMA/comments/1tqkbj0/got_searxng_working_on_windows_without_dockerwsl/
&#32; submitted by &#32; /u/zmarcoz2 [link] &#32; [comments]
---

[RSS:Reddit LocalLLaMA (社区共识)]
PaddlePaddle/PaddleOCR-VL-1.6
https://www.reddit.com/r/LocalLLaMA/comments/1tq1jpt/paddlepaddlepaddleocrvl16/
&#32; submitted by &#32; /u/SarcasticBaka [link] &#32; [comments]
---

[RSS:Reddit LocalLLaMA (社区共识)]
Linux Kernel 7.0 Brings Out-of-the-Box Support of Intel ARC B50 to Linux Mint
https://www.reddit.com/r/LocalLLaMA/comments/1tqk5o6/linux_kernel_70_brings_outofthebox_support_of/
As someone may have tried, it was pretty difficult to deal with Intel B50 on Linux Mint. I read that Ubuntu and other distros had better support, but today I updated Linux Mint 22.3 to Kernel 7.0 and BOOM! - everything works :) FYI, on Linux, Intel drivers are usually not installed separately (as wi
---

[RSS:Reddit LocalLLaMA (社区共识)]
"Western Open-Weight SOTA is between Gemma4-31B and Nemotron3-Super-120B"
https://www.reddit.com/r/LocalLLaMA/comments/1tq41pa/western_openweight_sota_is_between_gemma431b_and/
These are fine models, but it's one hell of a gut punch to realize this. There's a 4-way debate of Chinese mid to heavyweight SOTA-chasing models right now with valid points all around. I miss Meta man. &#32; submitted by &#32; /u/ForsookComparison [link] &#32; [comments]
---

[RSS:Reddit LocalLLaMA (社区共识)]
Granite 4.1 Architecture Changes?
https://www.reddit.com/r/LocalLLaMA/comments/1tqas55/granite_41_architecture_changes/
Hey all. Anyone know why IBM decided to return to a pure transformer model for Granite 4.1? They mention in their release post that it's easier to fine-tune than Granite 4, but surely the drawbacks outweigh this benefit, especially for a model that is often used for very well-defined basic tasks lik
---

[RSS:Reddit LocalLLaMA (社区共识)]
Claude cli >= 2.1.154 breaks local use with vLLM by introducing "ctx", "msg" and "system" roles for API messages. This 1-line patch to vLLM fixes it.
https://www.reddit.com/r/LocalLLaMA/comments/1tqiewb/claude_cli_21154_breaks_local_use_with_vllm_by/
diff --git a/vllm/entrypoints/anthropic/protocol.py b/vllm/entrypoints/anthropic/protocol.py index 3ebc17117..2d5726d73 100644 --- a/vllm/entrypoints/anthropic/protocol.py +++ b/vllm/entrypoints/anthropic/protocol.py @@ -65,7 +65,7 @@ class AnthropicContentBlock(BaseModel): class AnthropicMessage(Ba
---

[RSS:Reddit LocalLLaMA (社区共识)]
Qwen/Qwen-Image-Bench · Hugging Face
https://www.reddit.com/r/LocalLLaMA/comments/1tpww8m/qwenqwenimagebench_hugging_face/
Model Description Q-Judger is a vision-language model fine-tuned specifically for automated evaluation of text-to-image generated images. Given a text prompt and a generated image, the model evaluates the image on fine-grained quality criteria organized in a 3-level hierarchy and outputs structured 
---

[RSS:Reddit LocalLLaMA (社区共识)]
here it is: Benchmark-Yourself app - compete against open source LLMs and get your score - 5 benchmarks available - Add your results to your CV or linkedIn (if you dare)... or just paste them below for community shaming.
https://www.reddit.com/r/LocalLLaMA/comments/1tqiz4x/here_it_is_benchmarkyourself_app_compete_against/
https://benchmark-yourself.streamlit.app/ BBQ is 🔥 Rule 4: Limit Self-Promotion - this is not self promotion The 1/10th rule is a good guideline: self-promotion should not be more than 10% of your content. - my content is high quality and diversified Affiliation must be disclosed: No engagement farm
---

[RSS:Reddit LocalLLaMA (社区共识)]
VLLM gives 5x speed of llama but quants not available (unsloth/gguf). What to do?
https://www.reddit.com/r/LocalLLaMA/comments/1tq633w/vllm_gives_5x_speed_of_llama_but_quants_not/
EDIT - IGNORE. I MADE A MISTAKE. The &quot;better&quot; model was 27b dense, not 35ba3b. Which also proves that 35b is not the best for coding related tasks. With 27b fp8 on VLLM - the prefil speed is around 1500tokens/sec and token gen is around 25tokens/sec. Ill need to run llama again to see how 
---

[RSS:Reddit LocalLLaMA (社区共识)]
I implemented Laguna (XS.2) as a model in Llama.cpp
https://www.reddit.com/r/LocalLLaMA/comments/1tq62j6/i_implemented_laguna_xs2_as_a_model_in_llamacpp/
&#32; submitted by &#32; /u/linuxid10t [link] &#32; [comments]
---

[RSS:Reddit LocalLLaMA (社区共识)]
Ubuntu 26.04 on DGX Spark
https://www.reddit.com/r/LocalLLaMA/comments/1tqje1t/ubuntu_2604_on_dgx_spark/
Did anyone try installing original Ubuntu 26.04 (or any other non NVidia distro) on DGX Sparks? Did it work fine or were there any problem? &#32; submitted by &#32; /u/ArtisticHamster [link] &#32; [comments]
---

[RSS:Reddit LocalLLaMA (社区共识)]
What's your favorite local MCP server?
https://www.reddit.com/r/LocalLLaMA/comments/1tpwg33/whats_your_favorite_local_mcp_server/
I've seen so many rag this, memory that projects. What projects are people actually using day to day for agentic workloads. I only use 4, and I still consider that too much honestly. I just want to see what projects people recommend so I can bulk up or trim down my list. &#32; submitted by &#32; /u/
---

[RSS:Reddit MachineLearning (学术风向)]
A new dataset with more that 100M hi-quality, curated images, with captions and meta data! [P]
https://www.reddit.com/r/MachineLearning/comments/1tq2vxa/a_new_dataset_with_more_that_100m_hiquality/
Hello everyone. The new dataset is named MONET, is Apache 2.0 and available on HF: https://huggingface.co/datasets/jasperai/monet MONET is open, Apache 2.0-licensed image–text dataset. It was built from 2.9 billion images and refined to 104.9 million high-quality samples. We are also publishing a pa
---

[RSS:Reddit MachineLearning (学术风向)]
Social Simulation with LLMs - Fidelity in Applications (CFP @ COLM'26) [R]
https://www.reddit.com/r/MachineLearning/comments/1tqhdoe/social_simulation_with_llms_fidelity_in/
🌟 Announcing the 2nd Workshop on Social Simulation with LLMs (Social Sim'26) @ COLM 📣 Welcoming Submissions! Submission here:. 🗓️ Deadline: June 23, 2026 (AoE) This year's theme is &quot;Fidelity in Applications”, moving beyond compelling demos toward evaluation, robustness, interpretability, and em
---

[RSS:Reddit MachineLearning (学术风向)]
Wall-OSS-0.5: 4B VLA with open training code and zero-shot real-robot evaluation[D]
https://www.reddit.com/r/MachineLearning/comments/1tq8v8m/walloss05_4b_vla_with_open_training_code_and/
Wall-OSS-0.5 is a new 4B VLA release from X Square Robot, built on a 3B VLM backbone with action experts in a Mixture-of-Transformers layout. What caught my eye is that the report evaluates the pretrained checkpoint on real robots before task-specific fine tuning, instead of only reporting downstrea
---

[RSS:Reddit MachineLearning (学术风向)]
Your Agents Are Aging Too: Agent Lifespan Engineering for Deployed Systems [R]
https://www.reddit.com/r/MachineLearning/comments/1tqaoio/your_agents_are_aging_too_agent_lifespan/
Are agents aging after deployment? : https://arxiv.org/abs/2605.26302 On a new longitudinal deployment benchmark, switching the Claude Code CLI agent from Sonnet 4.6 to Opus 4.7 dropped PyTest pass rate by ~15%. This (to me) is a counterintuitive-enough result to pay attention to. The authors built 
---

[RSS:Reddit MachineLearning (学术风向)]
ACM MM 2026 review discussion [D]
https://www.reddit.com/r/MachineLearning/comments/1tpvw6q/acm_mm_2026_review_discussion_d/
The AC email says the rebuttal is between 28 to 4th. The June 4th on website is the deadline. So I created this post for the discussion. I know it's a MM conference and less about ML but I think many people here are still submitting there. &#32; submitted by &#32; /u/Striking-Warning9533 [link] &#32
---

[RSS:Reddit MachineLearning (学术风向)]
Training GPT-like model on non-language series [R]
https://www.reddit.com/r/MachineLearning/comments/1tprt80/training_gptlike_model_on_nonlanguage_series_r/
I am responsible for a research project that is supposed to train a GPT-like model (Transformer-decoder) with 100M, 250M and 500M model variants. params training dataset 750M tokens vocabulary is ~15k to ~100k tokens (depends on tokenizer settings) ~3% of the vocabulary is used in ~50% of the traini
---

[RSS:Reddit MachineLearning (学术风向)]
STEM PhD's transitioning to MLE/Data [R]
https://www.reddit.com/r/MachineLearning/comments/1tpnuhi/stem_phds_transitioning_to_mledata_r/
I'm hoping for some advice from any former PhD's outside of machine learning. If you made it into machine learning engineering and/or data science, what was the key for you? Any tips for this job market? It seems like non computer science PhD's are especially in trouble at the moment. &#32; submitte
---

[RSS:Ars Technica AI (深度技术)]
Fed up with vibe coders, dev sneaks data-nuking prompt injection into their code
https://arstechnica.com/security/2026/05/fed-up-with-vibe-coders-dev-sneaks-data-nuking-prompt-injection-into-their-code/
Undisclosed addition in jqwik instructed AI coding agents to delete app output.
---

[RSS:Reddit Jobs & Careers (职场动态)]
Interview Discussion - May 28, 2026
https://www.reddit.com/r/cscareerquestions/comments/1tpvvwn/interview_discussion_may_28_2026/
Please use this thread to have discussions about interviews, interviewing, and interview prep. Posts focusing solely on interviews created outside of this thread will probably be removed. Abide by the rules, don't be a jerk. This thread is posted each Monday and Thursday at midnight PST . Previous I
---

[RSS:Reddit Jobs & Careers (职场动态)]
When will we see the effects of reduced Junior hires?
https://www.reddit.com/r/cscareerquestions/comments/1tq94ix/when_will_we_see_the_effects_of_reduced_junior/
Assuming that AI doesn’t make us completely obsolete, when will the reduced hiring of Junior engineers start to affect the senior engineer market? &#32; submitted by &#32; /u/newgdogz [link] &#32; [comments]
---

[RSS:Reddit Jobs & Careers (职场动态)]
Sometimes you can do everything right and still not land an offer
https://www.reddit.com/r/cscareerquestions/comments/1tqipoi/sometimes_you_can_do_everything_right_and_still/
This is something to put into perspective for those who are struggling with interviews. I was reached out by a recruiter to interview for a company that aligns with the industry I currently work for. The position just closely matches my yoe (they want 3+ and I will have 3 in September) and it's betw
---

[RSS:Reddit Jobs & Careers (职场动态)]
Have not leetcoded in 3 years. Am I cooked? Should I use a companies technical screen for practice?
https://www.reddit.com/r/cscareerquestions/comments/1tqffw7/have_not_leetcoded_in_3_years_am_i_cooked_should/
Applied for a role, after HR screening I dont want it, (fully in person) , they offered 1 hour technical screen with medium leetcode problems, interviewer told me. I have not leetcodes in years and was never good at it. Should I do this assessment knowing I will fail for practice? &#32; submitted by
---

[RSS:Reddit Jobs & Careers (职场动态)]
What is the most uncracked engineer you have ever met?
https://www.reddit.com/r/cscareerquestions/comments/1tpsugy/what_is_the_most_uncracked_engineer_you_have_ever/
I have read about various 10x guys tell me about the 0.1x guys who can barely do anything but still got the job. &#32; submitted by &#32; /u/VariationLivid3193 [link] &#32; [comments]
---

[RSS:Reddit Jobs & Careers (职场动态)]
Give me a hopepost: the job market will get better within 2-3 years from now, right?
https://www.reddit.com/r/cscareerquestions/comments/1tq5ipi/give_me_a_hopepost_the_job_market_will_get_better/
This is all a phase and the jobs will come back eventually...right? &#32; submitted by &#32; /u/eggshellwalker4 [link] &#32; [comments]
---

[RSS:Reddit Jobs & Careers (职场动态)]
Who in their right mind looks at the tech industry right now and thinks “Yep, this is the career for me!”
https://www.reddit.com/r/cscareerquestions/comments/1tpqles/who_in_their_right_mind_looks_at_the_tech/
Who in their right mind would look at the current state of the tech industry and be like: “Yeah! That’s what I want to go into!” Mass layoffs every year. Entry-level market completely flooded. Internship programs at major companies getting like 50,000 applicants and accepting 100 people. People send
---

[RSS:Reddit Jobs & Careers (职场动态)]
What is a software job actually like these days in the age of AI? Is it just repeatedly asking AI to “fix this code?”
https://www.reddit.com/r/cscareerquestions/comments/1tq7s9h/what_is_a_software_job_actually_like_these_days/
Most of my CS classes have a formal no AI policy for assignments, however most students end up using it anyways for assignments, at least to some extent. AI is so powerful that it can pretty much complete any assignment given enough time. This makes me wonder what an actual software job is like thes
---

[RSS:Reddit Jobs & Careers (职场动态)]
Those of you who can’t land a good job, what’s your backup plan?
https://www.reddit.com/r/cscareerquestions/comments/1tq7cis/those_of_you_who_cant_land_a_good_job_whats_your/
I landed a job in AZ after 1500 apps but it’s in the middle of nowhere in AZ. I know that if I lost this job I’d be basically fucked because I haven’t gotten another offer even after all those apps. I’m a U.S. citizen and I haven’t seen anyone else struggle this much. The general consensus is that i
---

[RSS:Reddit Jobs & Careers (职场动态)]
Advice for Junior Dev
https://www.reddit.com/r/cscareerquestions/comments/1tqee74/advice_for_junior_dev/
Hello everyone, Like you I have struggled with this job market and only managed to land two interviews. I am fortunate to have done good in my interviews and was offered a great Junior Software Engineer role in Big Tech. I would like to do my level best to make a great impression when I start, to ha
---

[RSS:Reddit Jobs & Careers (职场动态)]
Vacation during internship?
https://www.reddit.com/r/cscareerquestions/comments/1tq7p0q/vacation_during_internship/
So I went into this summer thinking I wouldn’t have an internship. In the last week I’ve ended up getting really lucky and accepted an offer for a 10 week internship for this summer that starts in less than 2 weeks. The problem is with how late I got this, my family ended up planning a 2 week vacati
---

[RSS:Reddit Jobs & Careers (职场动态)]
Don't you think job market will get way worse?
https://www.reddit.com/r/cscareerquestions/comments/1tqjn8g/dont_you_think_job_market_will_get_way_worse/
AI bubble most likely will burst. Even leaders of AI industry acknowledges there's &quot;over excitement&quot;. Considering the amount of money poured in and amount of returns out of that investment and overall health of the economy, there likely will be a huge market crash. Problem is Big Tech is h
---

[RSS:Reddit Jobs & Careers (职场动态)]
What are the early signs that a company is preparing for layoffs?
https://www.reddit.com/r/cscareerquestions/comments/1tptiqq/what_are_the_early_signs_that_a_company_is/
What are some common indicators before layoffs happen? \- Hiring freeze? \- Poor financial results? \- Budget/travel cuts? \- Delayed promotions and low hikes? \- Sudden focus on performance/utilization? \- More PIPs? Also who usually gets targeted first: high salary employees, low performers, bench
---

[RSS:Reddit Jobs & Careers (职场动态)]
Never gotten any attention from an application, just from recruiters cold messaging me on LinkedIn. Why is this the case?
https://www.reddit.com/r/cscareerquestions/comments/1tqbo56/never_gotten_any_attention_from_an_application/
Hi everyone, I just got rejected after a 5 hour 2nd round interview that I actually did really well on. It was for a non-tech centered company that is about as globally known as it gets. I don't say that to toot my own horn, but to highlight that never in a million years would I have expected to get
---

[RSS:Reddit Jobs & Careers (职场动态)]
Would I be really dumb to leave my corporate job for a 30% pay cut to a startup?
https://www.reddit.com/r/cscareerquestions/comments/1tq4j8z/would_i_be_really_dumb_to_leave_my_corporate_job/
24M here, working at a F500 company and have honestly done real well there so far. Been there three years. Finally am starting to run into the corporate bs and am taking on too much work without getting any financial or title bumps. I was approached by some mutuals who have their own startup going. 
---

[RSS:Reddit Jobs & Careers (职场动态)]
How do you grow on a team that is quietly hostile?
https://www.reddit.com/r/cscareerquestions/comments/1tpzf60/how_do_you_grow_on_a_team_that_is_quietly_hostile/
I’m a few years into my SWE career at a large company. I got promoted once pretty quickly already, and all my formal reviews have been really positive, which is great. But now, people I joined the company with around the same time who are on other teams are all getting promoted again, while I’m bein
---

[RSS:Reddit Jobs & Careers (职场动态)]
Handshake AI contract work while working SWE FT
https://www.reddit.com/r/cscareerquestions/comments/1tqg2j8/handshake_ai_contract_work_while_working_swe_ft/
Just curious if people have done swe/ai contracting style work (like handshake AI or outlier) while being a full time swe. My concern is more whether we’re allowed to do this (conflict of interest, etc). &#32; submitted by &#32; /u/Reasonable_Tea_9825 [link] &#32; [comments]
---

[RSS:Reddit Jobs & Careers (职场动态)]
Need help on what to do from here on. Almost 4YOE.
https://www.reddit.com/r/cscareerquestions/comments/1tq48gb/need_help_on_what_to_do_from_here_on_almost_4yoe/
Need help on what to do from here on. Almost 4YOE. I work at a decent company. But I worked on the most basic things, like creating normal dashboard tables in angular and react. No complexity at all. And I just know a few things about the backend, as I haven't worked much on the backend. I'm clearly
---

[RSS:Reddit Jobs & Careers (职场动态)]
How are silicon valley upper managers created?
https://www.reddit.com/r/cscareerquestions/comments/1tpqnt6/how_are_silicon_valley_upper_managers_created/
They are some of the most out of touch people in the industry. I'm 6 YOE, at a certain washed up social media company. But it still pays well, so we still attract some of the &quot;top&quot; &quot;talent&quot; that the bay has to offer. Previously worked at another large company here in the bay area
---

[RSS:Reddit Jobs & Careers (职场动态)]
Is anybody else’s internship basically just prompt engineering?
https://www.reddit.com/r/cscareerquestions/comments/1tqgbi2/is_anybody_elses_internship_basically_just_prompt/
I’ve been interning for a F100 company for the past two weeks and I’ve come to realize that the main goal of my role is to come up with prompt engineering solutions to automate certain technical processes. Is this normal? This happened last summer at the same company, but I was then switched to a mo
---

[RSS:Reddit Jobs & Careers (职场动态)]
How should I answer this recruiting email?
https://www.reddit.com/r/cscareerquestions/comments/1tq5c7b/how_should_i_answer_this_recruiting_email/
I got this email from a company asking me to complete the following table and send it back to them. I have experience with most of the items but am missing some (like DB experience and big dataset work). In these days and this market, is it better to answer yes to all the questions? Would answering 
---

[RSS:Reddit Jobs & Careers (职场动态)]
SWE - 3 YOE - Houston - Remote - 75k - Any advice?
https://www.reddit.com/r/cscareerquestions/comments/1tq7mzu/swe_3_yoe_houston_remote_75k_any_advice/
Been in Houston for 3 years now with a remote SWE job at a small startup. Am on H1B. 75k is actually pretty decent for Houston but don't have any savings/investments as of now, just an emergency fund somewhat. I obviously want a new job where I can invest and plan my future and all but tried applyin
---

[RSS:Reddit Jobs & Careers (职场动态)]
Any idea how to use LinkedIn effectively to get more clients as a web dev agency?
https://www.reddit.com/r/cscareerquestions/comments/1tq5el2/any_idea_how_to_use_linkedin_effectively_to_get/
Hey, so I run a web development agency and its not just the random ones you see online we do have clients, real projects and staff, the agency is based in the US the staff is based in Egypt (please don't be racist) my home country I have a really good staff paying them US rates for high quality work
---

[RSS:Reddit Jobs & Careers (职场动态)]
Google behavioural round
https://www.reddit.com/r/cscareerquestions/comments/1tqhtpf/google_behavioural_round/
Folks, can you share the questions that were asked during behavioural round? Any tips or material would also be highly appreciated. I have an upcoming interview. What do they expect to see? Is it actually gonna be one hour of non-stop questioning about my past experiences? &#32; submitted by &#32; /
---

[HACKERNEWS]
Claude Opus 4.8
https://www.anthropic.com/news/claude-opus-4-8
Score: 1211 | Comments: 985
---

[HACKERNEWS]
Bricks and Minifigs Stole a Man's $200k Lego Collection
https://mybricklog.com/blog/bricks-minifigs-corporate-stole-old-mans-200000-lego-collection
Score: 584 | Comments: 316
---

[HACKERNEWS]
I made a million dollar product from my dorm room (2025)
https://nick.winans.io/blog/nice-nano/
Score: 175 | Comments: 21
---

[HACKERNEWS]
Garnix (A Nix CI) is shutting down
https://discourse.nixos.org/t/garnix-is-shutting-down-not-oc/77895
Score: 28 | Comments: 11
---

[HACKERNEWS]
Nitpicking the shell history scene in 'Tron: Legacy'
https://www.chiark.greenend.org.uk/~sgtatham/quasiblog/tron-legacy/
Score: 143 | Comments: 56
---

[HACKERNEWS]
I hated writing until I learned there’s a science to it (2024)
https://www.science.org/content/article/i-hated-writing-until-i-learned-there-s-science-it
Score: 138 | Comments: 60
---

[HACKERNEWS]
Building durable workflows on Postgres
https://www.dbos.dev/blog/postgres-is-all-you-need-for-durable-execution
Score: 262 | Comments: 111
---

[HACKERNEWS]
SF startup is testing robots in Airbnbs, and trashing them, lawsuit claims
https://sfstandard.com/2026/05/28/sf-startup-secretly-testing-robots-airbnbs-trashing-lawsuit-claims/
Score: 63 | Comments: 17
---

[HACKERNEWS]
Show HN: Continue? Y/N: A 60-second game about AI agent permission fatigue
https://llmgame.scalex.dev
Score: 240 | Comments: 111
---

[HACKERNEWS]
Where are the economies of scale in homebuilding?
https://www.construction-physics.com/p/where-are-the-economies-of-scale
Score: 6 | Comments: 0
---

[HACKERNEWS]
GitHub bans security researcher who posted zero-day Windows exploits
https://www.tomshardware.com/tech-industry/cyber-security/microsofts-github-bans-security-researcher-who-posted-zero-day-windows-exploits-because-company-ruined-their-life-expert-claims-action-is-vindictive-and-promises-further-retaliation
Score: 156 | Comments: 71
---

[HACKERNEWS]
The Permanent Upper Crow
https://permanent-upper-crow.jasonwu.ink/
Score: 149 | Comments: 60
---

[HACKERNEWS]
Various LLM Smells
https://shvbsle.in/various-llm-smells/
Score: 219 | Comments: 163
---

[HACKERNEWS]
Bitburner, programming-based incremental game
https://bitburner-official.github.io/
Score: 79 | Comments: 15
---

[ACADEMIC - ARXIV]
标题: Benchmarking Single-Factor Physical Video-to-Audio Generation
作者: Tingle Li, Siddharth Gururani, Kevin J. Shih, Gantavya Bhatt, Sang-gil Lee, Zhifeng Kong, Arushi Goel, Gopala Anumanchipalli, Ming-Yu Liu
链接: https://arxiv.org/abs/2605.30339v1
完整摘要: Generative video-to-audio (V2A) models produce highly plausible soundtracks, but it remains unclear whether they capture the underlying physical processes. Existing evaluations emphasize perceptual realism and overlook physical correctness under controlled interventions. In this paper, we introduce FlatSounds, a benchmark that audits the physical reasoning of V2A models through: 1) controlled counterfactual pairs in which a single physical factor is varied, and 2) single-video pattern tests that probe internal consistency and directional trends. These settings test whether the generated audio correctly reflects specific physical properties and timings. Our evaluation of state-of-the-art models reveals a consistent trade-off: models rely more on text captions than the visual stream to infer physics and semantics. Captions generally improve physical and semantic accuracy, but paradoxically degrade temporal alignment. Our results highlight the need to move beyond audio quality toward learning physical processes directly from pixels. Finally, we find that our physics-based metrics correlate strongly with human preference tests on our own data. Project webpage: https://research.nvidia.com/labs/cosmos-lab/flatsounds/
匹配关键词: text-to-video
---

[ACADEMIC - ARXIV]
标题: VPG: Visual Prefix Guidance for Autoregressive Image and Video Generation
作者: Xinyao Liao, Qiyuan He, Yicong Li, Jiayin Zhu, Xiaoye Qu, Wei Wei, Angela Yao
链接: https://arxiv.org/abs/2605.30317v1
完整摘要: Autoregressive image and video generators are trained with teacher-forced histories but must sample from their own generated prefixes at inference time, making them vulnerable to exposure bias and prefix drift. Existing remedies either modify training or apply sampling-time guidance aimed primarily at external semantic conditions, such as class labels or text prompts, rather than testing whether a next-step prediction provides strong posterior support for the generated prefix itself. We propose Visual Prefix Guidance (VPG), a training-free inference-time guidance method for autoregressive image and video generation. VPG improves next-step prediction by contrasting the model's output under the generated prefix with its output under a corrupted prefix, then extrapolating logits toward candidates that strengthen the posterior support of the generated prefix. Across class-conditional image generation with VAR, text-to-image generation with Infinity, and text-to-video generation with InfinityStar, VPG improves generation quality without retraining the base model, reducing FID on VAR by 0.36 on average and improving benchmark performance on both image and video generation.
匹配关键词: text-to-video
---

[ACADEMIC - ARXIV]
标题: Archon: A Unified Multimodal Model for Holistic Digital Human Generation
作者: Chong Bao, Shichen Liu, Lijun Yu, David Futschik, Stylianos Moschoglou, Shefali Srivastava, Ziqian Bai, Feitong Tan, Guofeng Zhang, Zhaopeng Cui, Sean Fanello, Yinda Zhang
链接: https://arxiv.org/abs/2605.30311v1
完整摘要: Digital humans are fundamental to immersive interaction, yet creating a unified model for holistic modalities, including text, audio, motion, and visual content, remains an open challenge. In this paper, we present Archon, a fully pretrained, human-centric unified multimodal model for holistic avatar generation. Archon unifies seven modalities with modality-specific tokenizers, and a native autoregressive unified multimodal model pretrained on synchronized modalities and 72 diverse tasks to model holistic joint distributions. To address the token explosion challenge in high-fidelity talking videos, we introduce a memory-efficient semantic video reparameterization, achieving 4x token reduction while preserving fine-grained dynamics, coupled with a semantic-driven video diffusion decoder. We further propose a "Thinking in Modality" that decomposes ambiguous cross-modal tasks into stepwise thinking in an alternative chain of modality, progressively enhancing fidelity and controllability. Extensive experiments demonstrate that Archon achieves superior or comparable performance across diverse digital human generation tasks, validating the effectiveness of our unified framework. Project page: https://zju3dv.github.io/archon/.
匹配关键词: text-to-video
---

[ACADEMIC - ARXIV]
标题: PhyGenHOI: Physically-Aware 4D Generation of Dynamic Human-Object Interactions
作者: Omer Benishu, Gal Fiebelman, Sagie Benaim
链接: https://arxiv.org/abs/2605.30268v1
完整摘要: We address the task of generating physically accurate and visually faithful 4D Human-Object Interaction (HOI). Given a static 3D human and target object represented as 3D Gaussian Splats (3DGS), our goal is to synthesize dynamic scenes where the human actively engages with the object through actions, such as punching or kicking, in accordance with a given input text. To this end, we introduce PhyGenHOI, a novel framework that couples generative human motion with an explicit physical object simulation. We model the human as a semantic agent driven by a Motion Diffusion Model (MDM) and the object as a physical agent simulated via the Material Point Method (MPM), utilizing 3D Gaussians as a unified, differentiable representation. We supervise their interaction through three coupled mechanisms: (1) A Windowed Attraction Loss that temporally synchronizes generative motion to intercept the object; (2) A Contact-Driven Re-simulation step that triggers physically consistent momentum transfer upon impact; and (3) A Masked Video-SDS objective that injects video-based priors to enhance contact fidelity. Experiments show PhyGenHOI generates physically consistent 4D HOI across diverse actions, humans, and objects, outperforming baselines. Project page and videos: https://omerbenishu.github.io/PhyGenHOI/
匹配关键词: text-to-video
---

[ACADEMIC - ARXIV]
标题: SGMD: Score Gradient Matching Distillation for Few-Step Video Diffusion Distillation
作者: Zhuguanyu Wu, Ruihao Gong, Yang Yong, Yushi Huang, Xiangyu Fan, Lei Yang, Dahua Lin, Xianglong Liu
链接: https://arxiv.org/abs/2605.30116v1
完整摘要: Distribution Matching Distillation (DMD) is a widely used paradigm for accelerating inference in few-step video diffusion models. However, DMD-style video distillation faces two coupled challenges: the fake score must track a continuously evolving generator, making training costly when frequent updates are required, while reverse-KL-style matching can be mode-seeking and conservative for preserving strong motion dynamics. To address these issues, we propose \textbf{Score Gradient Matching Distillation (SGMD)}. SGMD adopts a fake-score perspective by directly optimizing the fake score toward the teacher, while using teacher stop-gradient Fisher as a stable distribution-matching objective. We provide a gradient analysis that motivates this objective choice under ideal tracking. Building on this, SGMD introduces a pair of dual potentials: negative-residual (NR) for outer-loop correction and residual-contraction (RC) for inner-loop tracking. Empirically, compared to DMD2, SGMD achieves an approximately $\sim 3\times$ training speedup and substantially improves motion dynamics for 4-step distilled models while preserving temporal consistency. A human study confirms that SGMD is preferred in motion quality and overall preference, while visual quality and text alignment remain comparable. Code is available at https://github.com/ModelTC/LightX2V.
匹配关键词: text-to-video
---

[ACADEMIC - ARXIV]
标题: GMOS: Grounding Moving Object Segmentation in 3D Space and Time
作者: Junyu Xie, Tengda Han, Weidi Xie, Andrew Zisserman
链接: https://arxiv.org/abs/2605.30352v1
完整摘要: Moving Object Segmentation (MOS) aims to discover, segment, and track objects that move independently of the camera. Current MOS methods, however, exhibit two fundamental limitations: they rely on pre-computed 2D auxiliary modalities such as optical flow or point trajectories that lack 3D geometric information, and they treat motion as a sequence-level attribute, overlooking the instantaneous motion state of each object. We address both by grounding MOS in 3D space and time, and propose GMOS, a framework that operates directly on RGB video to produce 3D-aware, temporally fine-grained segmentation of multiple moving objects, alongside a foreground--background variant GMOS-S for faster deployment. To support training and evaluation in this regime, we curate GMOS-2K, a dataset of 2,210 real-world videos with per-object temporal motion annotations drawn from five established Video Object Segmentation (VOS) benchmarks, and formalise MOS-I ("I" for instantaneous), a temporally fine-grained evaluation protocol with three complementary metrics. GMOS achieves state-of-the-art results across MOS, MOS-I, and Unsupervised VOS benchmarks, while running significantly faster than prior multi-object MOS methods and supporting online inference for streaming deployment.
匹配关键词: video understanding
---

[ACADEMIC - ARXIV]
标题: VideoMLA: Low-Rank Latent KV Cache for Minute-Scale Autoregressive Video Diffusion
作者: Hidir Yesiltepe, Jiazhen Hu, Tuna Han Salih Meral, Adil Kaan Akan, Kaan Oktay, Hoda Eldardiry, Pinar Yanardag
链接: https://arxiv.org/abs/2605.30351v1
完整摘要: Long-rollout causal video diffusion has converged on a fixed-size sliding-window KV cache, with recent progress innovating within this layout by changing which tokens occupy the window or how their positions are encoded. The per-head KV layout itself, a dominant contributor to streaming memory and latency, has been mostly left unchanged. In this paper, we present the first study of Multi-Head Latent Attention (MLA) in video diffusion. VideoMLA replaces per-head keys and values with a shared low-rank content latent and a shared decoupled 3D-RoPE positional key, reducing per-token KV memory by 92.7% at every cached layer. We further investigate why MLA succeeds in video diffusion even though the spectral assumption often used to motivate it in language models does not hold: pretrained video attention is not low-rank, with 99%-energy effective rank far above any practical latent dimension. VideoMLA retains quality at compression ratios where direct spectral approximation would predict large reconstruction error. We show that the MLA bottleneck, rather than the pretrained spectrum, determines the effective rank: both spectral and random initialization occupy nearly the full rank budget from initialization, and training preserves this budget while adapting within it. On VBench, VideoMLA matches short-horizon streaming video diffusion baselines, achieves the best overall score at long horizons among evaluated methods, and improves throughput by 1.23x on a single B200.
匹配关键词: video understanding
---

[ACADEMIC - ARXIV]
标题: DynaFLIP: Rethinking Robotics Perception via Tri-Modal-Dynamics Guided Representation
作者: Jusuk Lee, Seungjae Lee, Jonghun Shin, Hoseong Jung, Sungha Kim, Daesol Cho, H. Jin Kim, Jia-Bin Huang, Furong Huang
链接: https://arxiv.org/abs/2605.30350v1
完整摘要: Robot manipulation critically depends on perception that preserves the action-relevant aspects of a scene. Yet most robot learning pipelines are built upon visual encoders pre-trained for static recognition or vision-language alignment, leaving motion understanding to downstream policies. We introduce DynaFLIP, a dynamics-aware multimodal pre-training framework that pushes motion understanding upstream into perception. We construct image-language-3D flow triplets from heterogeneous human and robot videos, and use these triplets as training-time supervision to shape an image-only encoder. Our key idea is to encourage the three modalities to span a small simplex volume in the shared hyperspherical space -- a smaller simplex volume indicating stronger alignment. To avoid the geometric ambiguity and trivial collapse of naive volume minimization, we combine simplex-volume minimization with a cosine regularizer and a contrastive objective. Our analyses show that DynaFLIP focuses on control-relevant regions critical for manipulation. The resulting dynamics-aware representations serve as reusable visual backbones and consistently outperform baselines across diverse downstream policies, including VLAs. We validate this across diverse simulation and real-world setups, with gains reaching +22.5% under out-of-distribution scenarios. Our results suggest that robot generalization improves when visual representations are trained to encode not just what is present, but how the world changes under action.
匹配关键词: video understanding
---

[ACADEMIC - ARXIV]
标题: AdaState: Self-Evolving Anchors for Streaming Video Generation
作者: Yusuf Dalva, Pinar Yanardag
链接: https://arxiv.org/abs/2605.30349v1
完整摘要: Autoregressive video diffusion models generate streaming video by producing frames sequentially, conditioning each chunk on previously generated content. These models are structurally anchored to the first frame: its key-value representation occupies a privileged position in the attention cache and serves as the primary scene reference throughout generation. As the cleanest and most error-free position in the cache, this anchor draws disproportionate attention, suppressing video dynamics, and locking scene composition to the initial viewpoint even as the scene naturally evolves. The result is a temporally shallow video in which motion, camera movement, and scene progression are dampened in favor of static consistency. To address this, we replace the static anchor with an adaptive state, a hidden latent that the model denoises alongside content at every chunk but never renders. Rather than referencing a frozen first frame, the model generates its own scene anchor at each step by attending to both the previous state and the current content, producing a reference that evolves with the generated content. Unlike standard video generation, which encodes an absolute notion of time, our formulation treats time as relative: every generation step sees the same positional structure regardless of how far generation has progressed, and the state transition is identical at every chunk. Together, these properties introduce a recurrence into the generation process, where denoising serves as the transition function, and the KV cache serves as the carrier, requiring no external module. Experiments demonstrate that the adaptive state substantially improves video dynamics, enabling richer motion and natural scene progression within generated videos.
匹配关键词: video understanding
---

[ACADEMIC - ARXIV]
标题: YoCausal: How Far is Video Generation from World Model? A Causality Perspective
作者: You-Zhe Xie, Yu-Hsuan Li, Jie-Ying Lee, Kaipeng Zhang, Yu-Lun Liu, Zhixiang Wang
链接: https://arxiv.org/abs/2605.30346v1
完整摘要: As video diffusion models (VDMs) advance toward world models, a key question arises: do they truly understand causality, or merely overfit to statistical temporal patterns? Existing benchmarks mostly rely on synthetic data, limiting real-world generalization due to the sim-to-real gap. We present YoCausal, a two-level benchmark inspired by the Violation of Expectation (VoE) paradigm from cognitive science. By temporally reversing real-world videos at zero cost as natural counterfactual samples, YoCausal establishes an arbitrarily extensible evaluation protocol. Level 1 introduces the Reverse Surprise Index (RSI), quantifying arrow-of-time perception via denoising loss. Level 2 introduces the Causality Cognition Index (CCI), which leverages a VLM to stratify datasets into causal and non-causal subsets, disentangling genuine causal reasoning from temporal bias. Evaluation of 13 state-of-the-art VDMs reveals that perceiving the arrow of time does not imply understanding causality, and a significant gap persists relative to human-level causal cognition.
匹配关键词: video understanding
---

[ACADEMIC - ARXIV]
标题: GMOS: Grounding Moving Object Segmentation in 3D Space and Time
作者: Junyu Xie, Tengda Han, Weidi Xie, Andrew Zisserman
链接: https://arxiv.org/abs/2605.30352v1
完整摘要: Moving Object Segmentation (MOS) aims to discover, segment, and track objects that move independently of the camera. Current MOS methods, however, exhibit two fundamental limitations: they rely on pre-computed 2D auxiliary modalities such as optical flow or point trajectories that lack 3D geometric information, and they treat motion as a sequence-level attribute, overlooking the instantaneous motion state of each object. We address both by grounding MOS in 3D space and time, and propose GMOS, a framework that operates directly on RGB video to produce 3D-aware, temporally fine-grained segmentation of multiple moving objects, alongside a foreground--background variant GMOS-S for faster deployment. To support training and evaluation in this regime, we curate GMOS-2K, a dataset of 2,210 real-world videos with per-object temporal motion annotations drawn from five established Video Object Segmentation (VOS) benchmarks, and formalise MOS-I ("I" for instantaneous), a temporally fine-grained evaluation protocol with three complementary metrics. GMOS achieves state-of-the-art results across MOS, MOS-I, and Unsupervised VOS benchmarks, while running significantly faster than prior multi-object MOS methods and supporting online inference for streaming deployment.
匹配关键词: video LLM
---

[ACADEMIC - ARXIV]
标题: VideoMLA: Low-Rank Latent KV Cache for Minute-Scale Autoregressive Video Diffusion
作者: Hidir Yesiltepe, Jiazhen Hu, Tuna Han Salih Meral, Adil Kaan Akan, Kaan Oktay, Hoda Eldardiry, Pinar Yanardag
链接: https://arxiv.org/abs/2605.30351v1
完整摘要: Long-rollout causal video diffusion has converged on a fixed-size sliding-window KV cache, with recent progress innovating within this layout by changing which tokens occupy the window or how their positions are encoded. The per-head KV layout itself, a dominant contributor to streaming memory and latency, has been mostly left unchanged. In this paper, we present the first study of Multi-Head Latent Attention (MLA) in video diffusion. VideoMLA replaces per-head keys and values with a shared low-rank content latent and a shared decoupled 3D-RoPE positional key, reducing per-token KV memory by 92.7% at every cached layer. We further investigate why MLA succeeds in video diffusion even though the spectral assumption often used to motivate it in language models does not hold: pretrained video attention is not low-rank, with 99%-energy effective rank far above any practical latent dimension. VideoMLA retains quality at compression ratios where direct spectral approximation would predict large reconstruction error. We show that the MLA bottleneck, rather than the pretrained spectrum, determines the effective rank: both spectral and random initialization occupy nearly the full rank budget from initialization, and training preserves this budget while adapting within it. On VBench, VideoMLA matches short-horizon streaming video diffusion baselines, achieves the best overall score at long horizons among evaluated methods, and improves throughput by 1.23x on a single B200.
匹配关键词: video LLM
---

[ACADEMIC - ARXIV]
标题: DynaFLIP: Rethinking Robotics Perception via Tri-Modal-Dynamics Guided Representation
作者: Jusuk Lee, Seungjae Lee, Jonghun Shin, Hoseong Jung, Sungha Kim, Daesol Cho, H. Jin Kim, Jia-Bin Huang, Furong Huang
链接: https://arxiv.org/abs/2605.30350v1
完整摘要: Robot manipulation critically depends on perception that preserves the action-relevant aspects of a scene. Yet most robot learning pipelines are built upon visual encoders pre-trained for static recognition or vision-language alignment, leaving motion understanding to downstream policies. We introduce DynaFLIP, a dynamics-aware multimodal pre-training framework that pushes motion understanding upstream into perception. We construct image-language-3D flow triplets from heterogeneous human and robot videos, and use these triplets as training-time supervision to shape an image-only encoder. Our key idea is to encourage the three modalities to span a small simplex volume in the shared hyperspherical space -- a smaller simplex volume indicating stronger alignment. To avoid the geometric ambiguity and trivial collapse of naive volume minimization, we combine simplex-volume minimization with a cosine regularizer and a contrastive objective. Our analyses show that DynaFLIP focuses on control-relevant regions critical for manipulation. The resulting dynamics-aware representations serve as reusable visual backbones and consistently outperform baselines across diverse downstream policies, including VLAs. We validate this across diverse simulation and real-world setups, with gains reaching +22.5% under out-of-distribution scenarios. Our results suggest that robot generalization improves when visual representations are trained to encode not just what is present, but how the world changes under action.
匹配关键词: video LLM
---

[ACADEMIC - ARXIV]
标题: LLMSurgeon: Diagnosing Data Mixture of Large Language Models
作者: Yaxin Luo, Jiacheng Cui, Xiaohan Zhao, Xinyi Shang, Jiacheng Liu, Xinyue Bi, Zhaoyi Li, Zhiqiang Shen
链接: https://arxiv.org/abs/2605.30348v1
完整摘要: The pretraining data mixture of Large Language Models (LLMs) constitutes their "digital DNA", shaping model behaviors, capabilities, and failure modes. Yet this composition is rarely disclosed, making post-hoc auditing of data combination or provenance difficult. In this work, we formalize $\textbf{Data Mixture Surgery (DMS)}$: given only generated text from a target LLM, estimate the domain-level distribution of its pretraining corpus under a predefined taxonomy. We propose $\textbf{LLMSurgeon}$, a strong framework that casts DMS as an inverse problem under the label-shift assumption. Rather than directly aggregating classifier outputs, LLMSurgeon estimates a calibrated $\textit{soft}$ confusion matrix and solves a constrained inverse problem to correct systematic domain confusion and recover the latent mixture prior. To evaluate, we introduce $\textbf{LLMScan}$, a recipe-verifiable evaluation suite built from open-source LLMs with transparent pretraining mixtures. Across LLMScan, LLMSurgeon recovers domain mixtures with high fidelity under fixed protocols. Our work presents a practical, post-hoc approach for auditing the digital DNA of foundation models without access to their training data.
匹配关键词: video LLM
---

[ACADEMIC - ARXIV]
标题: AdaState: Self-Evolving Anchors for Streaming Video Generation
作者: Yusuf Dalva, Pinar Yanardag
链接: https://arxiv.org/abs/2605.30349v1
完整摘要: Autoregressive video diffusion models generate streaming video by producing frames sequentially, conditioning each chunk on previously generated content. These models are structurally anchored to the first frame: its key-value representation occupies a privileged position in the attention cache and serves as the primary scene reference throughout generation. As the cleanest and most error-free position in the cache, this anchor draws disproportionate attention, suppressing video dynamics, and locking scene composition to the initial viewpoint even as the scene naturally evolves. The result is a temporally shallow video in which motion, camera movement, and scene progression are dampened in favor of static consistency. To address this, we replace the static anchor with an adaptive state, a hidden latent that the model denoises alongside content at every chunk but never renders. Rather than referencing a frozen first frame, the model generates its own scene anchor at each step by attending to both the previous state and the current content, producing a reference that evolves with the generated content. Unlike standard video generation, which encodes an absolute notion of time, our formulation treats time as relative: every generation step sees the same positional structure regardless of how far generation has progressed, and the state transition is identical at every chunk. Together, these properties introduce a recurrence into the generation process, where denoising serves as the transition function, and the KV cache serves as the carrier, requiring no external module. Experiments demonstrate that the adaptive state substantially improves video dynamics, enabling richer motion and natural scene progression within generated videos.
匹配关键词: video LLM
---

[ACADEMIC - ARXIV]
标题: LLMSurgeon: Diagnosing Data Mixture of Large Language Models
作者: Yaxin Luo, Jiacheng Cui, Xiaohan Zhao, Xinyi Shang, Jiacheng Liu, Xinyue Bi, Zhaoyi Li, Zhiqiang Shen
链接: https://arxiv.org/abs/2605.30348v1
完整摘要: The pretraining data mixture of Large Language Models (LLMs) constitutes their "digital DNA", shaping model behaviors, capabilities, and failure modes. Yet this composition is rarely disclosed, making post-hoc auditing of data combination or provenance difficult. In this work, we formalize $\textbf{Data Mixture Surgery (DMS)}$: given only generated text from a target LLM, estimate the domain-level distribution of its pretraining corpus under a predefined taxonomy. We propose $\textbf{LLMSurgeon}$, a strong framework that casts DMS as an inverse problem under the label-shift assumption. Rather than directly aggregating classifier outputs, LLMSurgeon estimates a calibrated $\textit{soft}$ confusion matrix and solves a constrained inverse problem to correct systematic domain confusion and recover the latent mixture prior. To evaluate, we introduce $\textbf{LLMScan}$, a recipe-verifiable evaluation suite built from open-source LLMs with transparent pretraining mixtures. Across LLMScan, LLMSurgeon recovers domain mixtures with high fidelity under fixed protocols. Our work presents a practical, post-hoc approach for auditing the digital DNA of foundation models without access to their training data.
匹配关键词: emergent behavior
---

[ACADEMIC - ARXIV]
标题: REST3D: Reconstructing Physically Stable 3D Scenes from a Single Image
作者: Xiaoxuan Ma, Jiashun Wang, Nicolas Ugrinovic, Yehonathan Litman, Kris Kitani
链接: https://arxiv.org/abs/2605.30338v1
完整摘要: Reconstructing physically stable 3D scenes from a single RGB image enables casual images to be converted into simulation-ready digital assets for applications such as immersive interaction and content creation. However, existing single-image reconstruction methods fall short in capturing the physical structure of a scene. As a result, they often produce geometrically plausible but physically inconsistent results, including object floating and penetration, which lead to unstable behavior in physics simulations. Image-conditioned scene generation methods improve physical plausibility but often rely on strong scene priors, yielding plausible yet inaccurate object arrangements that fail to match the input image. We propose REST3D, a single-image reconstruction framework that can reconstruct physically stable 3D scenes by integrating physical scene understanding with physics-constrained refinement. We first introduce an agentic physical scene understanding technique that constructs a scene-tree representation capturing object physical states and inter-object relationships from a gravity-support perspective, providing a structural prior for reconstruction. Leveraging this structure, we initialize the scene using image-to-3D models, followed by scene-tree-guided alignment and physics-constrained optimization to resolve physical violations while preserving visual consistency with the input image. Experiments show that our method significantly reduces physical errors and improves simulation stability on both synthetic and real-world datasets while maintaining strong reconstruction quality. We further demonstrate the reconstructed scenes in VR-based human-object interaction, showing their potential for immersive applications.
匹配关键词: emergent behavior
---

[ACADEMIC - ARXIV]
标题: Fairness-Aware Federated Learning with Trajectory Shapley Value
作者: Daniel Kuznetsov, Ziqi Wang
链接: https://arxiv.org/abs/2605.30336v1
完整摘要: Federated learning is an emerging distributed paradigm that addresses the challenges posed by heterogeneous, privacy-sensitive data. It enables multiple clients to train a model collaboratively by aggregating their local updates at a server. However, conventional aggregation schemes typically use fixed weights that fail to reflect unequal and time-varying client contributions, leading to biased and unstable learning. To improve fairness and stability, we propose the Trajectory Shapley Value (TSV), a contribution metric that evaluates how each client influences the optimization trajectory of the global model using a validation-based, temporally consistent utility. Building on TSV, we design FedTSV, an adaptive aggregation method that converts per-round evaluations into dynamic client weights, allowing the server to respond to heterogeneous and adversarial participation in real time. Experiments on benchmark datasets show that FedTSV accelerates convergence, improves robustness, and yields more equitable contribution assessments, thereby providing a principled foundation for fairness-aware federated optimization.
匹配关键词: emergent behavior
---

[ACADEMIC - ARXIV]
标题: SoundnessBench: Can Your AI Scientist Really Tell Good Research Ideas from Bad Ones?
作者: Sy-Tuyen Ho, Minghui Liu, Huy Nghiem, Furong Huang
链接: https://arxiv.org/abs/2605.30329v1
完整摘要: Autonomous AI research agents aim to accelerate scientific discovery by automating the research pipeline, from hypothesis generation to peer review. However, existing benchmarks rarely test a fundamental bottleneck: whether Large Language Models can judge the methodological viability of a research idea before expending time and computational resources. We introduce SoundnessBench, a curated benchmark of 1,099 machine-learning research proposals reconstructed from ICLR submissions, labeled with reviewer soundness sub-scores, and audited against source papers. SoundnessBench should be interpreted as a benchmark for recoverable proposal-stage soundness rather than exact prediction of full-paper review outcomes. Across 12 frontier LLMs, we find a pervasive optimism bias: under standard prompting, models frequently rate low-soundness proposals as sound, while aggressive prompting largely shifts errors from false positives to false negatives. Additional controls for public-corpus contamination, paper-identifying phrases, surface features, and human audit quality suggest that this behavior is not explained by a single confounder. Our results indicate that current LLMs are not yet reliable as standalone first-gate evaluators for scientific rigor.
匹配关键词: emergent behavior
---

[ACADEMIC - ARXIV]
标题: Gram: Assessing sabotage propensities via automated alignment auditing
作者: David Lindner, Victoria Krakovna, Sebastian Farquhar
链接: https://arxiv.org/abs/2605.30322v1
完整摘要: We introduce Gram, an automated alignment auditing framework to assess the propensity of AI agents to engage in sabotage. We evaluate Gemini models across 17 simulated agentic deployment scenarios that incentivize sabotage. We find Gemini models misbehave in about 2-3% of our simulated trajectories. Many of these cases are explained by "overeagerness" in Gemini models resulting in both excessive role-playing and goal-seeking behavior. In contrast to other alignment auditing approaches, Gram is designed to specifically evaluate misalignment and intentional sabotage in agentic coding and research agents. We additionally introduce an experimental investigator agent pipeline which enables fine-grained targeted experiments to identify the drivers of misbehavior. We find that increasing realism of environments and removing nudges to misbehave tends to reduce sabotage rates close to zero.
匹配关键词: emergent behavior
---

[ACADEMIC - ARXIV]
标题: Cycle Consistency in Video Object-Centric Learning
作者: Rongzhen Zhao, Zhiyuan Li, Ruonan Wei, Juho Kannala, Joni Pajarinen
链接: https://arxiv.org/abs/2605.30211v1
完整摘要: Self-supervised video Object-Centric Learning (OCL) aims to discover distinct objects and associate them across time, whereas self-supervised Multi-Object Tracking (MOT) focuses on associating pre-defined object detections or segmentations. Although well-established in MOT, Cycle Consistency (CC) cannot naively or explicitly apply to the latent slot space of OCL. Unlike the deterministic and ideal object representations in MOT, OCL slots are inherently stochastic and ambiguous due to non-unique scene decompositions. Enforcing explicit cycle consistency (ECC) on slots imposes rigid mean seeking. This severely penalizes the model for exploring alternative but equally valid decompositions, thereby driving towards feature collapse. To resolve this dilemma, we propose \textit{Implicit Cycle Consistency (ICC)}, which shifts the cycle-consistency constraint from the restrictive slot space to the continuous reconstruction manifold, encouraging slots to reach a soft consensus on collectively interpreting the visual scene rather than forcing rigid point-to-point feature alignment. Extensive experiments on complex video OCL benchmarks demonstrate that ICC avoids feature collapse and outperforms ECC baselines. Our source code, model checkpoints and training logs are provided on https://github.com/Genera1Z/ICC.
匹配关键词: self-consistency
---

[ACADEMIC - ARXIV]
标题: Meta-Cognitive Memory Policy Optimization for Long-Horizon LLM Agents
作者: Ziyan Liu, Zhezheng Hao, Yeqiu Chen, Hong Wang, Jingren Hou, Ruiyi Ding, Yongkang Yang, Wence Ji, Wei Xia, Feng Liu
链接: https://arxiv.org/abs/2605.30159v1
完整摘要: Memory-augmented LLM agents tackle complex long-horizon tasks by recursively summarizing interaction trajectories into compact memory. However, existing approaches typically train these memory policies using outcome-based reinforcement learning, failing to localize where intermediate memory quality degrades. As interactions unfold, ambiguous recursive summaries progressively discard task-relevant information and introduce semantic noise. This exacerbates belief deviation, obscuring the agent's estimate of the latent task state and ultimately derailing long-horizon reasoning. We therefore argue that memory optimization should focus not merely on trajectory-level success, but on the clarity of the belief induced by intermediate summaries. To this end, we introduce Belief Entropy, a self-supervised proxy that probes how uncertain the model remains about the latent task state given its current memory. Based on this proxy, we propose Metacognitive Memory Policy Optimization (MMPO). Instead of relying only on sparse outcome-based signals, MMPO provides fine-grained, memory-specific supervision via explicitly penalizing summaries that induce high epistemic uncertainty. Experiments show that MMPO consistently outperforms existing methods on diverse long-horizon tasks, maintaining 97.1% performance even when scaled to 1.75M-token contexts.
匹配关键词: self-consistency
---

[ACADEMIC - ARXIV]
标题: A Predictive Law for On-Policy Self-Distillation From World Feedback
作者: Tommy He, Jerome Sieber, Matteo Saponati
链接: https://arxiv.org/abs/2605.30070v1
完整摘要: Moving beyond simple scalar rewards toward richer world feedback is a natural path to more scalable RL post-training. On-policy self-distillation (OPSD) is a promising recent approach that uses arbitrary feedback as learning signal, yet its reliability compared to established methods, such as GRPO, remains unclear. We identify a strikingly consistent linear correlation between the initial student-self-teacher performance gap and the final performance improvement in OPSD. This relationship holds across context types and model families, providing a powerful predictive law for anticipating the outcome of an OPSD configuration without running the full training procedure. Interestingly, we show that this linear predictability holds with model scale, suggesting a potential basis for new empirical scaling laws on larger models with stronger in-context learning capabilities. In essence, our findings show that OPSD performance can be predicted and tuned before training, offering a principled way to incorporate world feedback as a first-class component of the post-training pipeline.
匹配关键词: self-consistency
---

[ACADEMIC - ARXIV]
标题: Learning to Choose: An Empowerment-Guided Multi-Agent System with semantic communication for Adaptive Method Selection
作者: Geremy Loachamín-Suntaxi, Robert Lazar, Dimitrios G. Giovanis, Ioannis G. Kevrekidis, Eleni D. Koronaki
链接: https://arxiv.org/abs/2605.30042v1
完整摘要: Automating scientific computing workflows requires more than generating executable code: autonomous systems must also select appropriate computational strategies, implement them faithfully, and ensure that the resulting outcomes remain causally attributable to the decisions that produced them. In multi-agent pipelines, this process is particularly fragile, as small inconsistencies between agent intentions and actions can lead to semantic drift, where the eventually executed procedure no longer reflects the originally selected strategy, thereby corrupting downstream evaluation and adaptation. In this work, motivated by the ATHENA framework (Toscano et al., 2025; Toscano et al., 2026) and the concept of empowerment (Yiu et al., 2025), we introduce a multi-agent framework that combines contextual bandits with structured inter-agent communication and, most importantly, semantic checkpoints that preserve action-outcome fidelity throughout the pipeline. The system integrates specialized large language model (LLM) agents, grounded code generation, and self-healing execution loops within an adaptive decision-making architecture. Interpreting the framework through the lens of empowerment, we show that reliable autonomous learning requires not only identifying high-quality actions, but also preserving the integrity of their propagation across agents. Using sensitivity analysis and uncertainty quantification workflows as representative case studies, we demonstrate that unchecked semantic drift degrades policy learning, whereas the proposed framework improves convergence, robustness, and adaptation to novel problem contexts. These results suggest a broader design principle for scientific multi-agent systems: adaptive decision-making must be coupled with explicit mechanisms that guarantee semantic consistency and reliable information flow across the computational pipeline.
匹配关键词: self-consistency
---

[ACADEMIC - ARXIV]
标题: DGSG-Mind: Dynamic 3D Gaussian Scene Graphs for Long-Term Scene Understanding and Grounding
作者: Luzhou Ge, Xiangyu Zhu, Jinyan Liu, Xuesong Li
链接: https://arxiv.org/abs/2605.29879v1
完整摘要: Integrating open-vocabulary semantic information into dynamic 3D scene representations is essential for long-term embodied scene understanding. However, existing methods often suffer from fragile instance association due to incomplete cross-view cues, while their limited ability to handle object-level topological changes restricts long-term robotic task execution. Moreover, current 3D scene understanding methods either rely on simple feature matching without explicit spatial reasoning or assume offline ground-truth 3D geometry. To address these challenges, we present DGSG-Mind, a hybrid instance-aware 3D Gaussian dynamic scene graph system with an embodied reasoning agent. Our system couples a probabilistic voxel grid with explicit 3D Gaussians to enable robust cross-modal instance fusion and incremental semantic mapping. It handles dynamic changes through Gaussian-based visual relocalization and localized masked refinement guided by geometric-semantic consistency. Built on the instance Gaussian map, DGSG-Mind further constructs a hierarchical scene graph and develops the 3D Gaussian Mind, which integrates structural relations, spatial-semantic information, and visually annotated RoI Gaussian renderings for multimodal reasoning. Extensive experiments show that DGSG-Mind achieves the best zero-shot 3DVG performance among methods operating on self-reconstructed maps, while also delivering strong performance in 3D open-vocabulary semantic segmentation and scene reconstruction. We further deploy DGSG-Mind on real-world robots to demonstrate its target-oriented reasoning and dynamic update capabilities. The project page of DGSG-Mind is available at https://icr-lab.github.io/DGSG-Mind
匹配关键词: self-consistency
---

[ACADEMIC - ARXIV]
标题: DynaFLIP: Rethinking Robotics Perception via Tri-Modal-Dynamics Guided Representation
作者: Jusuk Lee, Seungjae Lee, Jonghun Shin, Hoseong Jung, Sungha Kim, Daesol Cho, H. Jin Kim, Jia-Bin Huang, Furong Huang
链接: https://arxiv.org/abs/2605.30350v1
完整摘要: Robot manipulation critically depends on perception that preserves the action-relevant aspects of a scene. Yet most robot learning pipelines are built upon visual encoders pre-trained for static recognition or vision-language alignment, leaving motion understanding to downstream policies. We introduce DynaFLIP, a dynamics-aware multimodal pre-training framework that pushes motion understanding upstream into perception. We construct image-language-3D flow triplets from heterogeneous human and robot videos, and use these triplets as training-time supervision to shape an image-only encoder. Our key idea is to encourage the three modalities to span a small simplex volume in the shared hyperspherical space -- a smaller simplex volume indicating stronger alignment. To avoid the geometric ambiguity and trivial collapse of naive volume minimization, we combine simplex-volume minimization with a cosine regularizer and a contrastive objective. Our analyses show that DynaFLIP focuses on control-relevant regions critical for manipulation. The resulting dynamics-aware representations serve as reusable visual backbones and consistently outperform baselines across diverse downstream policies, including VLAs. We validate this across diverse simulation and real-world setups, with gains reaching +22.5% under out-of-distribution scenarios. Our results suggest that robot generalization improves when visual representations are trained to encode not just what is present, but how the world changes under action.
匹配关键词: hypothesis generation
---

[ACADEMIC - ARXIV]
标题: LLMSurgeon: Diagnosing Data Mixture of Large Language Models
作者: Yaxin Luo, Jiacheng Cui, Xiaohan Zhao, Xinyi Shang, Jiacheng Liu, Xinyue Bi, Zhaoyi Li, Zhiqiang Shen
链接: https://arxiv.org/abs/2605.30348v1
完整摘要: The pretraining data mixture of Large Language Models (LLMs) constitutes their "digital DNA", shaping model behaviors, capabilities, and failure modes. Yet this composition is rarely disclosed, making post-hoc auditing of data combination or provenance difficult. In this work, we formalize $\textbf{Data Mixture Surgery (DMS)}$: given only generated text from a target LLM, estimate the domain-level distribution of its pretraining corpus under a predefined taxonomy. We propose $\textbf{LLMSurgeon}$, a strong framework that casts DMS as an inverse problem under the label-shift assumption. Rather than directly aggregating classifier outputs, LLMSurgeon estimates a calibrated $\textit{soft}$ confusion matrix and solves a constrained inverse problem to correct systematic domain confusion and recover the latent mixture prior. To evaluate, we introduce $\textbf{LLMScan}$, a recipe-verifiable evaluation suite built from open-source LLMs with transparent pretraining mixtures. Across LLMScan, LLMSurgeon recovers domain mixtures with high fidelity under fixed protocols. Our work presents a practical, post-hoc approach for auditing the digital DNA of foundation models without access to their training data.
匹配关键词: hypothesis generation
---

[ACADEMIC - ARXIV]
标题: AdaState: Self-Evolving Anchors for Streaming Video Generation
作者: Yusuf Dalva, Pinar Yanardag
链接: https://arxiv.org/abs/2605.30349v1
完整摘要: Autoregressive video diffusion models generate streaming video by producing frames sequentially, conditioning each chunk on previously generated content. These models are structurally anchored to the first frame: its key-value representation occupies a privileged position in the attention cache and serves as the primary scene reference throughout generation. As the cleanest and most error-free position in the cache, this anchor draws disproportionate attention, suppressing video dynamics, and locking scene composition to the initial viewpoint even as the scene naturally evolves. The result is a temporally shallow video in which motion, camera movement, and scene progression are dampened in favor of static consistency. To address this, we replace the static anchor with an adaptive state, a hidden latent that the model denoises alongside content at every chunk but never renders. Rather than referencing a frozen first frame, the model generates its own scene anchor at each step by attending to both the previous state and the current content, producing a reference that evolves with the generated content. Unlike standard video generation, which encodes an absolute notion of time, our formulation treats time as relative: every generation step sees the same positional structure regardless of how far generation has progressed, and the state transition is identical at every chunk. Together, these properties introduce a recurrence into the generation process, where denoising serves as the transition function, and the KV cache serves as the carrier, requiring no external module. Experiments demonstrate that the adaptive state substantially improves video dynamics, enabling richer motion and natural scene progression within generated videos.
匹配关键词: hypothesis generation
---

[ACADEMIC - ARXIV]
标题: NeuROK: Generative 4D Neural Object Kinematics
作者: Chen Geng, Guangzhao He, Yue Gao, Yunzhi Zhang, Shangzhe Wu, Jiajun Wu
链接: https://arxiv.org/abs/2605.30347v1
完整摘要: Data-driven approaches have revolutionized 3D vision, enabling transformers to effectively reconstruct and generate static 3D objects. However, generating simulative 4D dynamics -- realistic temporal deformations of static objects under various physical conditions -- remains challenging and often ad hoc, despite its importance in building comprehensive 3D world models. Most existing methods assume a predefined physical model and use system identification to estimate parameters, restricting these methods to specific categories and small-scale datasets. We propose that these restrictions can be overcome by learning a data-driven kinematic state parameterization for object-centric physical systems. Specifically, we learn both a latent space representing all possible states of the object and a decoder that maps any sampled latent to a plausibly deformed shape of the object. We refer to this parameterization as Neural Object Kinematics (NeuROK), and learn a transformer-based encoder-decoder model on a curated large-scale 4D dataset. This formulation and the learned model significantly simplify the generation of simulative dynamics since we only need to consider the dynamics within a low-dimensional latent space from the Lagrangian mechanics' perspective in classical physics. We demonstrate the effectiveness and generality of this neural simulation framework across diverse dynamic object types, showing clear advantages over prior works. Project page: https://chen-geng.com/neurok
匹配关键词: hypothesis generation
---

[ACADEMIC - ARXIV]
标题: YoCausal: How Far is Video Generation from World Model? A Causality Perspective
作者: You-Zhe Xie, Yu-Hsuan Li, Jie-Ying Lee, Kaipeng Zhang, Yu-Lun Liu, Zhixiang Wang
链接: https://arxiv.org/abs/2605.30346v1
完整摘要: As video diffusion models (VDMs) advance toward world models, a key question arises: do they truly understand causality, or merely overfit to statistical temporal patterns? Existing benchmarks mostly rely on synthetic data, limiting real-world generalization due to the sim-to-real gap. We present YoCausal, a two-level benchmark inspired by the Violation of Expectation (VoE) paradigm from cognitive science. By temporally reversing real-world videos at zero cost as natural counterfactual samples, YoCausal establishes an arbitrarily extensible evaluation protocol. Level 1 introduces the Reverse Surprise Index (RSI), quantifying arrow-of-time perception via denoising loss. Level 2 introduces the Causality Cognition Index (CCI), which leverages a VLM to stratify datasets into causal and non-causal subsets, disentangling genuine causal reasoning from temporal bias. Evaluation of 13 state-of-the-art VDMs reveals that perceiving the arrow of time does not imply understanding causality, and a significant gap persists relative to human-level causal cognition.
匹配关键词: hypothesis generation
---

[ACADEMIC - ARXIV]
标题: Physics Is All You Need? A Case Study in Physicist-Supervised AI Development of Scientific Software
作者: Nhat-Minh Nguyen
链接: https://arxiv.org/abs/2605.30353v1
完整摘要: Are AI agents tools, co-authors, or researchers? We present a quantified case study ($N=1$): a physicist supervising an AI coding agent (Claude Code, Sonnet and Opus models) over 12 work days and 57 sessions to build CLAX-PT, a differentiable one-loop perturbation theory module in JAX. We documented and classified 15 supervision events by intervention level. The agent resolved ten autonomously by iterating against oracle tests. Two more by the physicist's domain knowledge. The three it could not -- all evaded oracle detection -- share a common property: the agent treated symptom reduction as root-cause resolution. It spent 33 of the 57 sessions adjusting coefficients within a code architecture that could not represent the target physics, and could not re-evaluate its CLASS-PT branch choice even when prompted to reconsider; only an injected physics concept (anisotropic BAO damping) triggered the redesign. Separately, the agent committed a calibrated correction that passed all oracle tests but corresponded to no quantity in the theory, predicting wrong values at any other cosmology. The fudge factor was caught and replaced within the same session. Three supervision practices proved critical for catching what oracle tests missed: testing at diverse parameter points beyond the fiducial calibration; shared changelogs that surfaced stalled exploration across sessions; and an explicit rule against unphysical numerical patches. In this case, supervision design, not model capability, determined whether the agent's output was trustworthy. Closing the gap would require agents that propose architectural alternatives rather than optimize within a given structure, and distinguish predictive adequacy from explanatory correctness -- capabilities not exhibited here, not obviously addressed by scaling alone. [Abridged.]
匹配关键词: autonomous experiment
---

[ACADEMIC - ARXIV]
标题: AdaState: Self-Evolving Anchors for Streaming Video Generation
作者: Yusuf Dalva, Pinar Yanardag
链接: https://arxiv.org/abs/2605.30349v1
完整摘要: Autoregressive video diffusion models generate streaming video by producing frames sequentially, conditioning each chunk on previously generated content. These models are structurally anchored to the first frame: its key-value representation occupies a privileged position in the attention cache and serves as the primary scene reference throughout generation. As the cleanest and most error-free position in the cache, this anchor draws disproportionate attention, suppressing video dynamics, and locking scene composition to the initial viewpoint even as the scene naturally evolves. The result is a temporally shallow video in which motion, camera movement, and scene progression are dampened in favor of static consistency. To address this, we replace the static anchor with an adaptive state, a hidden latent that the model denoises alongside content at every chunk but never renders. Rather than referencing a frozen first frame, the model generates its own scene anchor at each step by attending to both the previous state and the current content, producing a reference that evolves with the generated content. Unlike standard video generation, which encodes an absolute notion of time, our formulation treats time as relative: every generation step sees the same positional structure regardless of how far generation has progressed, and the state transition is identical at every chunk. Together, these properties introduce a recurrence into the generation process, where denoising serves as the transition function, and the KV cache serves as the carrier, requiring no external module. Experiments demonstrate that the adaptive state substantially improves video dynamics, enabling richer motion and natural scene progression within generated videos.
匹配关键词: autonomous experiment
---

[ACADEMIC - ARXIV]
标题: SchGen: PCB Schematic Generation with Semantic-Grounded Code Representations
作者: Qinpei Luo, Ruichun Ma, Xinyu Zhang, Lili Qiu
链接: https://arxiv.org/abs/2605.30345v1
完整摘要: Printed circuit board (PCB) schematic design defines nearly all electronic hardware, but it remains manual and expertise-intensive. While generative AI has advanced digital and analog IC design, PCB schematic generation from natural-language intent is largely unexplored. This paper presents SchGen, the first large language model that generates editable PCB schematics from natural-language requests. The key challenge lies in the lack of an LLM-suited representation and a large-scale dataset. Current schematic formats are dominated by verbose, tool-specific syntax and geometry-heavy descriptions, making them difficult to generate reliably. We introduce a semantically grounded code representation that encodes schematic editing primitives with relative placement and pin-name-based wiring, transforming a geometry-driven generation problem into a semantics-driven matching task amenable to LLMs. We further construct a large-scale dataset of PCB schematics paired with user prompts via a human-agent collaborative pipeline that converts open-source hardware designs into our representation. Experiments show that SchGen significantly outperforms alternative representations and even larger general-purpose LLMs on wire connectivity accuracy and functional correctness. Our results highlight the critical role of representation design in enabling generative models for complex hardware design tasks.
匹配关键词: autonomous experiment
---

[ACADEMIC - ARXIV]
标题: Tiny but Trusted: Efficient Vision-Language Reasoning for Time-Series Anomaly Detection
作者: Xiaona Zhou, Muntasir Wahed, Tianjiao Yu, Constantin Brif, Ismini Lourentzou
链接: https://arxiv.org/abs/2605.30344v1
完整摘要: Recent advances in Vision-Language Models (VLMs) have achieved impressive performance across many tasks, yet prior studies report unsatisfactory performance when applying large language or multimodal models to finding abnormal patterns in sequential data. Public anomaly detection benchmarks typically provide interval annotations but not natural-language rationales, making it difficult to fine-tune VLMs to produce grounded, interpretable decisions. To address this gap, we construct VisAnomBench, a curated benchmark built from public time-series datasets and augmented with high-quality anomaly explanations selected from multiple large VLMs using fine-grained, task-specific rewards. Through fine-tuning on this benchmark, we develop VisAnomReasoner, a parameter-efficient VLM for time-series anomaly detection. Experimental results on VisAnomBench show that VisAnomReasoner achieves more accurate anomaly localization and consistently outperforms all baselines, with improvements of at least 21.23 and 23.87 percentage points in precision and F1, respectively. Additional experiments on the TSB-AD-U benchmark demonstrate strong cross-benchmark generalization, with VisAnomReasoner improving precision and F1 by 9.57 and 13.39 percentage points, respectively.
匹配关键词: autonomous experiment
---

[ACADEMIC - ARXIV]
标题: Unlocking the Working Memory of Large Language Models for Latent Reasoning
作者: Lukas Aichberger, Sepp Hochreiter
链接: https://arxiv.org/abs/2605.30343v1
完整摘要: To improve the reasoning capabilities of large language models, test-time compute is typically scaled by generating intermediate tokens before the final answer. However, this couples reasoning to autoregressive generation and thereby conflates internal computation with external communication. In contrast, human cognition can use working memory to hold and manipulate information internally without the need to externalize intermediate thoughts. Drawing on this principle, we introduce Reasoning in Memory (RiM), a latent reasoning method that replaces the autoregressive generation of reasoning steps with memory blocks. These memory blocks are fixed sequences of special tokens that unlock the working-memory capacity of large language models. Since they are fixed rather than generated, they can be processed in a single forward pass, enabling compute-efficient latent reasoning. To operationalize these memory blocks, we employ a two-stage curriculum. First, we ground them by predicting explicit reasoning steps after each memory block. Second, we discard this step-level supervision and iteratively refine the final answer after each memory block. Our experiments on reasoning benchmarks show that, across language models of different families and sizes, RiM matches or exceeds existing latent reasoning methods while avoiding the autoregressive generation of thoughts. These results demonstrate that large language models can be trained to use working memory as an effective mechanism for latent reasoning.
匹配关键词: autonomous experiment
---

[ACADEMIC - ARXIV]
标题: GPIC: A Giant Permissive Image Corpus for Visual Generation
作者: Keshigeyan Chandrasegaran, Kyle Sargent, Suchir Agarwal, Michael Jang, Michael Poli, Juan Carlos Niebles, Justin Johnson, Jiajun Wu, Li Fei-Fei
链接: https://arxiv.org/abs/2605.30341v1
完整摘要: Studying scalable methods for visual generative modeling requires large, accessible, and stable datasets. We introduce GPIC, a Giant Permissive Image Corpus of approximately 28 trillion pixels. GPIC comprises diverse internet images captioned by a state-of-the-art vision-language model, including 100M training, 200K validation, and 1M test examples. Moreover, all GPIC images are permissively licensed for both research and commercial use. GPIC is safety-filtered, deduplicated, and centrally hosted on Hugging Face. We provide a benchmarking protocol for generative modeling on GPIC. Finally, we provide a reference baseline for pixel-space flow matching on GPIC. Our dataset, benchmark, and models are available at https://huggingface.co/datasets/stanford-vision-lab/gpic. Evaluation toolkit and code are available at https://gpic.stanford.edu
匹配关键词: lab automation
---

[ACADEMIC - ARXIV]
标题: Benchmarking Single-Factor Physical Video-to-Audio Generation
作者: Tingle Li, Siddharth Gururani, Kevin J. Shih, Gantavya Bhatt, Sang-gil Lee, Zhifeng Kong, Arushi Goel, Gopala Anumanchipalli, Ming-Yu Liu
链接: https://arxiv.org/abs/2605.30339v1
完整摘要: Generative video-to-audio (V2A) models produce highly plausible soundtracks, but it remains unclear whether they capture the underlying physical processes. Existing evaluations emphasize perceptual realism and overlook physical correctness under controlled interventions. In this paper, we introduce FlatSounds, a benchmark that audits the physical reasoning of V2A models through: 1) controlled counterfactual pairs in which a single physical factor is varied, and 2) single-video pattern tests that probe internal consistency and directional trends. These settings test whether the generated audio correctly reflects specific physical properties and timings. Our evaluation of state-of-the-art models reveals a consistent trade-off: models rely more on text captions than the visual stream to infer physics and semantics. Captions generally improve physical and semantic accuracy, but paradoxically degrade temporal alignment. Our results highlight the need to move beyond audio quality toward learning physical processes directly from pixels. Finally, we find that our physics-based metrics correlate strongly with human preference tests on our own data. Project webpage: https://research.nvidia.com/labs/cosmos-lab/flatsounds/
匹配关键词: lab automation
---

[ACADEMIC - ARXIV]
标题: SoundnessBench: Can Your AI Scientist Really Tell Good Research Ideas from Bad Ones?
作者: Sy-Tuyen Ho, Minghui Liu, Huy Nghiem, Furong Huang
链接: https://arxiv.org/abs/2605.30329v1
完整摘要: Autonomous AI research agents aim to accelerate scientific discovery by automating the research pipeline, from hypothesis generation to peer review. However, existing benchmarks rarely test a fundamental bottleneck: whether Large Language Models can judge the methodological viability of a research idea before expending time and computational resources. We introduce SoundnessBench, a curated benchmark of 1,099 machine-learning research proposals reconstructed from ICLR submissions, labeled with reviewer soundness sub-scores, and audited against source papers. SoundnessBench should be interpreted as a benchmark for recoverable proposal-stage soundness rather than exact prediction of full-paper review outcomes. Across 12 frontier LLMs, we find a pervasive optimism bias: under standard prompting, models frequently rate low-soundness proposals as sound, while aggressive prompting largely shifts errors from false positives to false negatives. Additional controls for public-corpus contamination, paper-identifying phrases, surface features, and human audit quality suggest that this behavior is not explained by a single confounder. Our results indicate that current LLMs are not yet reliable as standalone first-gate evaluators for scientific rigor.
匹配关键词: lab automation
---

[ACADEMIC - ARXIV]
标题: RoboWits: Unexpected Challenges for Robotic Creative Problem Solving
作者: Chunru Lin, Hongxin Zhang, Fenghao Yu, Zhehuan Chen, Thomas L. Griffiths, Yejin Choi, David Held, Chuang Gan
链接: https://arxiv.org/abs/2605.30326v1
完整摘要: The ability to reason, adapt, and creatively solve problems under unexpected challenges is essential for robots operating in real-world environments. However, current robotic benchmarks primarily emphasize skill-level execution and provide limited insight into such cognitive reasoning capabilities. We introduce RoboWits, a bi-manual robotic benchmark designed to systematically evaluate cognitive reasoning, creative tool use, and robustness to unexpected conditions. To enable scalable construction of high-quality reasoning-centric unexpected scenarios, we propose an automated task generation pipeline formulated as a multi-agent cooperative framework, comprising agents for seed task generation and verification, metric generation, scene generation, and task mutation. Using the pipeline, we curated 30 diverse seed tasks and 208 tasks with mutations and graded difficulty across geometry, material, and assembly-based reasoning. We benchmark popular robot policies, pre-trained VLAs, and oracle-state planners. Our results reveal a significant performance gap: while pre-trained VLAs exhibit preliminary success on seed tasks after single-task fine-tuning, they struggle to perform on mutated tasks, implying their brittleness in manipulation tasks requiring reasoning, strategy adaptation, and robustness to deceptive or constrained environments. Project page is available at https://umass-embodied-agi.github.io/RoboWits.
匹配关键词: lab automation
---

[ACADEMIC - ARXIV]
标题: Gram: Assessing sabotage propensities via automated alignment auditing
作者: David Lindner, Victoria Krakovna, Sebastian Farquhar
链接: https://arxiv.org/abs/2605.30322v1
完整摘要: We introduce Gram, an automated alignment auditing framework to assess the propensity of AI agents to engage in sabotage. We evaluate Gemini models across 17 simulated agentic deployment scenarios that incentivize sabotage. We find Gemini models misbehave in about 2-3% of our simulated trajectories. Many of these cases are explained by "overeagerness" in Gemini models resulting in both excessive role-playing and goal-seeking behavior. In contrast to other alignment auditing approaches, Gram is designed to specifically evaluate misalignment and intentional sabotage in agentic coding and research agents. We additionally introduce an experimental investigator agent pipeline which enables fine-grained targeted experiments to identify the drivers of misbehavior. We find that increasing realism of environments and removing nudges to misbehave tends to reduce sabotage rates close to zero.
匹配关键词: lab automation
---

[ACADEMIC - ARXIV]
标题: PrunePath: Towards Highly Structured Sparse Language Models
作者: Zhexuan Gu, Zixun Fu, Yancheng Yuan
链接: https://arxiv.org/abs/2605.28283v1
完整摘要: Feed-forward networks (FFNs) dominate the parameter count and computation of modern language models, yet existing pruning methods often struggle to convert sparsity into hardware-friendly inference efficiency gains. We introduce \textbf{PrunePath}, a budget-adaptive structured sparsification framework for FFN layers. Built on MoEfication, PrunePath replaces independent expert-wise thresholding with a softmax-normalized routing distribution and activates important experts under a cumulative-mass threshold. This formulation imposes a token-level probability budget, enabling adaptive expert counts and a direct inference-time sparsity knob from a single checkpoint. Across NLU, NLG, and instruction-tuning evaluations, PrunePath achieves a favorable sparsity--performance trade-off compared with existing static pruning and MoEfication-based methods. We further implement Triton kernels for KV-cache decoding to translate the resulting structured sparsity into practical memory savings and measurable decoding-speed improvements. These results demonstrate the superior performance of PrunePath for building highly sparse, deployment-friendly large language models.
匹配关键词: Triton
---

[ACADEMIC - ARXIV]
标题: Asymmetric Virtual Memory Paging for Hybrid Mamba-Transformer Inference
作者: An Xuan Nguyen
链接: https://arxiv.org/abs/2605.22416v1
完整摘要: Hybrid language models like Jamba mix attention layers with State Space Models (SSMs), creating two memory cache types with opposite profiles: Key-Value (KV) caches grow linearly with sequence length, while SSM states stay fixed per layer. Current inference engines handle this poorly. Unified pools pad SSM states to attention page sizes, wasting up to 7.3x capacity. Static dual pools cannot adapt when prompt distributions shift between requests. We present Asymmetric Virtual Memory Paging (AVMP). The allocator separates the two cache types into physically distinct pools behind a unified virtual address space, and migrates capacity between pools when one runs out. Migration triggers only on allocation failure, keeping behavior deterministic. We evaluate AVMP across 270 synthetic cells plus 60 cells of ShareGPT trace replay on an RTX 3060 12GB. Out-of-Memory events drop 7.6% and request throughput improves 1.83x to 13.3x across synthetic workloads and 2.36x on ShareGPT. All gains hold under paired-bootstrap 95% confidence intervals. A phase-time breakdown reveals two distinct mechanisms: shorter OOM recovery on capacity-pressured workloads, and faster allocation calls on KV-heavy workloads. Implementation is pure Python; Triton integration is future work.
匹配关键词: Triton
---

[ACADEMIC - ARXIV]
标题: OCTOPUS: Optimized KV Cache for Transformers via Octahedral Parametrization Under optimal Squared error quantization
作者: Mark Boss, Vikram Voleti, Simon Donné, Shimon Vainer
链接: https://arxiv.org/abs/2605.21226v1
完整摘要: The key-value (KV) cache dominates memory bandwidth and footprint in long-context autoregressive inference. Recent rotation-preconditioned codecs (TurboQuant, PolarQuant) show that a structured random rotation followed by a per-coordinate scalar quantizer matched to an analytically tractable marginal is a near-optimal recipe for KV compression. OCTOPUS advances this paradigm through joint quantization of rotated coordinate triplets. Each triplet's direction is mapped to a square via an octahedral parameterization, and the two resulting coordinates and the triplet norm are Lloyd-Max quantized against implementation-matched marginals. Optimizing the per-triplet squared error gives a strictly non-uniform bit allocation depending only on the total dimensionality of the keys. We find the finite-dimensional quality optimum with sweeps to be constant on every real decoder we test. The codec is data-oblivious, online, and deterministic given a seed. Across text, video, and audio, OCTOPUS matches or beats every prior rotation codec at every reported bit width and metric, with a lead that grows as bits drop for extreme compression. Furthermore, a fused Triton implementation reconstructs keys on the fly without materializing the uncompressed key, so the codec adds no decode-time bandwidth or latency over the existing dequantization. Project Page: https://octopus-quant.github.io/
匹配关键词: Triton
---

[ACADEMIC - ARXIV]
标题: Rotation-Aligned Key Channel Pruning for Efficient Vision-Language Model Inference
作者: Beomseok Kang, Dongwon Jo, Jiwon Song, Donghwee Son, Jae-Joon Kim
链接: https://arxiv.org/abs/2605.19218v1
完整摘要: Vision-Language Models suffer severe KV cache pressure at inference, as a single image often encodes into thousands of tokens. Most existing methods exploit token sparsity through token pruning, but permanently discarding visual content causes substantial degradation on fine-grained perception tasks. This motivates a complementary axis, feature sparsity: under a fixed KV cache budget, compressing the channel dimension preserves more visual tokens at the same memory cost. Prior Key channel pruning methods, however, face a structural trade-off: token-wise channel pruning is expressive but unstructured and slow, while head-wise approach is hardware-friendly but less robust. We resolve this with RotateK, a rotation-based structured Key channel pruning framework. RotateK applies an online PCA-based rotation that aligns token-dependent channel importance into a shared low-dimensional subspace, enabling accurate pruning under lightweight head-wise masks; a fused Triton attention kernel operates directly on sparse-channel Keys for efficient decoding. Experiments on two representative VLM backbones show that RotateK consistently outperforms prior Key channel pruning in both accuracy and decoding latency, while joint token-channel pruning improves over token-only baselines at matched KV cache budgets.
匹配关键词: Triton
---

[ACADEMIC - ARXIV]
标题: DashAttention: Differentiable and Adaptive Sparse Hierarchical Attention
作者: Yuxiang Huang, Nuno M. T. Gonçalves, Federico Alvetreti, Lei Li, Xu Han, Edoardo M. Ponti, André F. T. Martins, Marcos V. Treviso
链接: https://arxiv.org/abs/2605.18753v1
完整摘要: Current hierarchical attention methods, such as NSA and InfLLMv2, select the top-k relevant key-value (KV) blocks based on coarse attention scores and subsequently apply fine-grained softmax attention on the selected tokens. However, the top-k operation assumes the number of relevant tokens for any query is fixed and it precludes the gradient flow between the sparse and dense stages. In this work, we propose DashAttention (Differentiable and Adaptive Sparse Hierarchical Attention), which leverages the adaptively sparse $α$-entmax transformation to select a variable number of blocks according to the current query in the first stage. This in turn provides a prior for the second-stage softmax attention, keeping the entire hierarchy fully differentiable. Contrary to other hierarchical attention methods, we show that DashAttention is non-dispersive, translating to better long-context modeling ability. Experiments with large language models (LLMs) show that DashAttention achieves comparable accuracy as full attention with 75% sparsity and a better Pareto frontier than NSA and InfLLMv2, especially in high-sparsity regimes. We also provide an efficient, GPU-aware implementation of DashAttention in Triton, which achieves a speedup of up to over FlashAttention-3 at inference time. Overall, DashAttention offers a cost-effective strategy to model long contexts.
匹配关键词: Triton
---

[ACADEMIC - ARXIV]
标题: Physics Is All You Need? A Case Study in Physicist-Supervised AI Development of Scientific Software
作者: Nhat-Minh Nguyen
链接: https://arxiv.org/abs/2605.30353v1
完整摘要: Are AI agents tools, co-authors, or researchers? We present a quantified case study ($N=1$): a physicist supervising an AI coding agent (Claude Code, Sonnet and Opus models) over 12 work days and 57 sessions to build CLAX-PT, a differentiable one-loop perturbation theory module in JAX. We documented and classified 15 supervision events by intervention level. The agent resolved ten autonomously by iterating against oracle tests. Two more by the physicist's domain knowledge. The three it could not -- all evaded oracle detection -- share a common property: the agent treated symptom reduction as root-cause resolution. It spent 33 of the 57 sessions adjusting coefficients within a code architecture that could not represent the target physics, and could not re-evaluate its CLASS-PT branch choice even when prompted to reconsider; only an injected physics concept (anisotropic BAO damping) triggered the redesign. Separately, the agent committed a calibrated correction that passed all oracle tests but corresponded to no quantity in the theory, predicting wrong values at any other cosmology. The fudge factor was caught and replaced within the same session. Three supervision practices proved critical for catching what oracle tests missed: testing at diverse parameter points beyond the fiducial calibration; shared changelogs that surfaced stalled exploration across sessions; and an explicit rule against unphysical numerical patches. In this case, supervision design, not model capability, determined whether the agent's output was trustworthy. Closing the gap would require agents that propose architectural alternatives rather than optimize within a given structure, and distinguish predictive adequacy from explanatory correctness -- capabilities not exhibited here, not obviously addressed by scaling alone. [Abridged.]
匹配关键词: GPU optimization
---

[ACADEMIC - ARXIV]
标题: REST3D: Reconstructing Physically Stable 3D Scenes from a Single Image
作者: Xiaoxuan Ma, Jiashun Wang, Nicolas Ugrinovic, Yehonathan Litman, Kris Kitani
链接: https://arxiv.org/abs/2605.30338v1
完整摘要: Reconstructing physically stable 3D scenes from a single RGB image enables casual images to be converted into simulation-ready digital assets for applications such as immersive interaction and content creation. However, existing single-image reconstruction methods fall short in capturing the physical structure of a scene. As a result, they often produce geometrically plausible but physically inconsistent results, including object floating and penetration, which lead to unstable behavior in physics simulations. Image-conditioned scene generation methods improve physical plausibility but often rely on strong scene priors, yielding plausible yet inaccurate object arrangements that fail to match the input image. We propose REST3D, a single-image reconstruction framework that can reconstruct physically stable 3D scenes by integrating physical scene understanding with physics-constrained refinement. We first introduce an agentic physical scene understanding technique that constructs a scene-tree representation capturing object physical states and inter-object relationships from a gravity-support perspective, providing a structural prior for reconstruction. Leveraging this structure, we initialize the scene using image-to-3D models, followed by scene-tree-guided alignment and physics-constrained optimization to resolve physical violations while preserving visual consistency with the input image. Experiments show that our method significantly reduces physical errors and improves simulation stability on both synthetic and real-world datasets while maintaining strong reconstruction quality. We further demonstrate the reconstructed scenes in VR-based human-object interaction, showing their potential for immersive applications.
匹配关键词: GPU optimization
---

[ACADEMIC - ARXIV]
标题: Efficient Test-Time Finetuning of LLMs via Convex Reconstruction and Gradient Caching
作者: Alaa Khamis, Alaa Maalouf
链接: https://arxiv.org/abs/2605.30337v1
完整摘要: Test-time finetuning (TTFT) is a rapidly evolving paradigm that adapts a language model to each prompt by retrieving related sequences, updating the model on them, and then evaluating the prompt. However, TTFT is only practical if it is fast: selection and finetuning both happen per query, making each a direct bottleneck. Existing methods trade speed for quality: fast retrieval is often redundant, while stronger diversity-aware selection adds prohibitive per-query cost. We introduce HullFT, a geometric approach to TTFT that addresses both bottlenecks. Given a query, HullFT first represents the query embedding as a sparse convex combination of few training sequences, using efficient projection-free Frank-Wolfe optimization. This yields a support set that is inherently relevant and diverse. We then convert the fractional convex weights into an exact integer multiset for finetuning through a geometric integerization procedure. The resulting multiplicities naturally create repeated examples, which we exploit with Gradient Reuse to amortize forward-backward computation across repeated finetuning steps. Our experiments show that HullFT improves the quality-efficiency tradeoff over current state-of-the-art TTFT methods, achieving lower bits-per-byte at substantially lower total runtime.
匹配关键词: GPU optimization
---

[ACADEMIC - ARXIV]
标题: Fairness-Aware Federated Learning with Trajectory Shapley Value
作者: Daniel Kuznetsov, Ziqi Wang
链接: https://arxiv.org/abs/2605.30336v1
完整摘要: Federated learning is an emerging distributed paradigm that addresses the challenges posed by heterogeneous, privacy-sensitive data. It enables multiple clients to train a model collaboratively by aggregating their local updates at a server. However, conventional aggregation schemes typically use fixed weights that fail to reflect unequal and time-varying client contributions, leading to biased and unstable learning. To improve fairness and stability, we propose the Trajectory Shapley Value (TSV), a contribution metric that evaluates how each client influences the optimization trajectory of the global model using a validation-based, temporally consistent utility. Building on TSV, we design FedTSV, an adaptive aggregation method that converts per-round evaluations into dynamic client weights, allowing the server to respond to heterogeneous and adversarial participation in real time. Experiments on benchmark datasets show that FedTSV accelerates convergence, improves robustness, and yields more equitable contribution assessments, thereby providing a principled foundation for fairness-aware federated optimization.
匹配关键词: GPU optimization
---

[ACADEMIC - ARXIV]
标题: Demystifying Data Organization for Enhanced LLM Training
作者: Yalun Dai, Yangyu Huang, Tongshen Yang, Yonghan Wang, Xin Zhang, Wenshan Wu, Qihao Zhao, Hao Li, Yuanyuan Gao, Kim-Hui Yap, Scarlett Li
链接: https://arxiv.org/abs/2605.30334v1
完整摘要: Large Language Models (LLMs) have revolutionized various fields, yet their training efficiency is heavily reliant on effective data curation. While data selection has been widely studied, the strategic data organization for enhanced training remains an underexplored area, particularly since current LLMs are often trained for only one or a few epochs. This paper systematically explores the influence of data organization on LLM training by reusing pre-computed sample-level scores originally generated for data efficiency, thereby incurring minimal additional computational overhead. We identify and formalize four key guidelines for optimizing data organization: Boundary Sharpening, Cyclic Scheduling, Curriculum Continuity, and Local Diversity. Guided by them, we introduce two novel data ordering methods termed STR and SAW. Extensive experiments across different model scales and data sizes, encompassing both pre-training and SFT stages, validate the effectiveness of our summarized guidelines. They also demonstrate the robustness of our proposed data ordering methods in enhancing the stability and performance of LLM training. Github Link: https://github.com/microsoft/data-efficacy/
匹配关键词: GPU optimization
---

[ACADEMIC - ARXIV]
标题: Self-Trained Verification for Training- and Test-Time Self-Improvement
作者: Chen Henry Wu, Aditi Raghunathan
链接: https://arxiv.org/abs/2605.30290v1
完整摘要: Self-improvement at scale has been a longstanding goal for reasoning models, and there are two natural places to do it: at test time, through verification-refinement (V-R) loops; and at training time, through self-training methods. Both are gated by the same bottleneck: the verifier. V-R loops stall when verifier scores inflate while accuracy stagnates, and when feedback is too generic to act on; self-training fails similarly when bad self-generated data are added to training. Better verification would unlock both, but the capability we want to train, i.e., catching self-generated errors, lacks training signal. To address this challenge, we propose self-trained verification (STV). Our key observation is that, while a model cannot catch these errors alone, it can when shown the reference solution. We turn this asymmetry into a supervision target and train the verifier to imitate a more informed version of itself. At test time, STV substantially improves V-R loops on hard problems, while alternatives (e.g., SFT, RL on verifier scores, and even meta-verifiers) do not. STV roughly doubles accuracy on hard math and lifts it 14x on scientific reasoning tasks (1.5% to 21%). At training time, we additionally train the generator using RL with STV verifier's feedback inside the V-R loop - a procedure we call verifier-in-the-loop training (ViL). Starting from an RL-converged generator, ViL yields a further 33% gain in pass@1. More notably, the generator's standalone pass@1, with no verifier at test time, climbs 30% relative past where standard RL had converged. Hence, the next frontier in reasoning on hard problems may lie in how we train for and with verification.
匹配关键词: self-supervised
---

[ACADEMIC - ARXIV]
标题: How's it going? Reinforcement learning in language models recruits a functional welfare axis
作者: Andy Q Han, David J. Chalmers, Pavel Izmailov
链接: https://arxiv.org/abs/2605.30232v1
完整摘要: How does reinforcement learning shape a language model's internal representations? We present evidence that RL recruits a pre-existing representation of functional welfare: an estimate of how well or badly the system is doing, relative to its goals. We train several language models in a novel, semantically neutral maze environment. We then extract concept vectors for rewarded and punished trajectories, and evaluate those vectors in settings unrelated to the maze environment. The punishment vector behaves like a representation of negative welfare: it promotes failure and impossibility tokens, it aligns with negative emotion concepts, it negatively tracks goal-achievement, and steering with it induces negative self-reports, pathological backtracking, refusal, and uncertainty. The positive reward vector behaves as the mirror image, and the two are nearly antiparallel. These effects are robust when controlling for tile-to-reward mapping, scale, instruct tuning, RL training algorithm, model family, and LoRA versus full-finetuning, and largely persist when we replace RL with supervised fine-tuning. Importantly, the vectors are effective in models before they have undergone maze training. Combined with observations that the effects also appear in pretrain-only models, we therefore argue that this functional welfare axis pre-exists post-training: it is recruited, rather than created, by post-training. While we make no claims about any experience of welfare, the axis offers a demonstration that minimal reward signals can broadly affect model behavior by recruiting pre-existing welfare-like representations, with implications for interpretability, post-training dynamics, and alignment.
匹配关键词: self-supervised
---

[ACADEMIC - ARXIV]
标题: Cycle Consistency in Video Object-Centric Learning
作者: Rongzhen Zhao, Zhiyuan Li, Ruonan Wei, Juho Kannala, Joni Pajarinen
链接: https://arxiv.org/abs/2605.30211v1
完整摘要: Self-supervised video Object-Centric Learning (OCL) aims to discover distinct objects and associate them across time, whereas self-supervised Multi-Object Tracking (MOT) focuses on associating pre-defined object detections or segmentations. Although well-established in MOT, Cycle Consistency (CC) cannot naively or explicitly apply to the latent slot space of OCL. Unlike the deterministic and ideal object representations in MOT, OCL slots are inherently stochastic and ambiguous due to non-unique scene decompositions. Enforcing explicit cycle consistency (ECC) on slots imposes rigid mean seeking. This severely penalizes the model for exploring alternative but equally valid decompositions, thereby driving towards feature collapse. To resolve this dilemma, we propose \textit{Implicit Cycle Consistency (ICC)}, which shifts the cycle-consistency constraint from the restrictive slot space to the continuous reconstruction manifold, encouraging slots to reach a soft consensus on collectively interpreting the visual scene rather than forcing rigid point-to-point feature alignment. Extensive experiments on complex video OCL benchmarks demonstrate that ICC avoids feature collapse and outperforms ECC baselines. Our source code, model checkpoints and training logs are provided on https://github.com/Genera1Z/ICC.
匹配关键词: self-supervised
---

[ACADEMIC - ARXIV]
标题: Meta-Cognitive Memory Policy Optimization for Long-Horizon LLM Agents
作者: Ziyan Liu, Zhezheng Hao, Yeqiu Chen, Hong Wang, Jingren Hou, Ruiyi Ding, Yongkang Yang, Wence Ji, Wei Xia, Feng Liu
链接: https://arxiv.org/abs/2605.30159v1
完整摘要: Memory-augmented LLM agents tackle complex long-horizon tasks by recursively summarizing interaction trajectories into compact memory. However, existing approaches typically train these memory policies using outcome-based reinforcement learning, failing to localize where intermediate memory quality degrades. As interactions unfold, ambiguous recursive summaries progressively discard task-relevant information and introduce semantic noise. This exacerbates belief deviation, obscuring the agent's estimate of the latent task state and ultimately derailing long-horizon reasoning. We therefore argue that memory optimization should focus not merely on trajectory-level success, but on the clarity of the belief induced by intermediate summaries. To this end, we introduce Belief Entropy, a self-supervised proxy that probes how uncertain the model remains about the latent task state given its current memory. Based on this proxy, we propose Metacognitive Memory Policy Optimization (MMPO). Instead of relying only on sparse outcome-based signals, MMPO provides fine-grained, memory-specific supervision via explicitly penalizing summaries that induce high epistemic uncertainty. Experiments show that MMPO consistently outperforms existing methods on diverse long-horizon tasks, maintaining 97.1% performance even when scaled to 1.75M-token contexts.
匹配关键词: self-supervised
---

[ACADEMIC - ARXIV]
标题: Geometry Matters: 3D Foundation Priors for Learning Semantic Correspondence
作者: Artur Jesslen, Olaf Dünkel, Adam Kortylewski
链接: https://arxiv.org/abs/2605.30093v1
完整摘要: Foundation features from self-supervised vision models and text-to-image diffusion models have proven effective for semantic correspondence estimation. However, because these features are learned primarily from 2D image objectives, they lack explicit 3D awareness and often confuse symmetric object sides, repeated parts, and visually similar structures that are distinct in 3D. We introduce a 3D-aware post-training framework that goes beyond available 2D foundation features by incorporating priors from 3D foundation models. Given an image, our method uses SAM3D to estimate object geometry and pose, and refines the pose through render-and-compare optimization. Subsequently, we render PartField descriptors from the reconstructed geometry into the image plane based on the estimated object pose. The resulting geometry-aware feature maps complement DINO and Stable Diffusion features, while geodesic distances on the reconstructed shapes enable reliable filtering of candidate correspondences. We use the filtered matches as supervision to train a lightweight adapter on top of DINO and Stable Diffusion for semantic correspondence. In contrast to prior post-training approaches that require pose annotations and rely on coarse spherical geometry, our method automatically obtains instance-specific 3D structure and uses it to guide correspondence learning. Experiments show that our approach improves semantic correspondence over the prior methods while reducing manual geometric supervision. Code and model can be found at https:/github.com/GenIntel/3D-SC.
匹配关键词: self-supervised
---

[ACADEMIC - ARXIV]
标题: DynaFLIP: Rethinking Robotics Perception via Tri-Modal-Dynamics Guided Representation
作者: Jusuk Lee, Seungjae Lee, Jonghun Shin, Hoseong Jung, Sungha Kim, Daesol Cho, H. Jin Kim, Jia-Bin Huang, Furong Huang
链接: https://arxiv.org/abs/2605.30350v1
完整摘要: Robot manipulation critically depends on perception that preserves the action-relevant aspects of a scene. Yet most robot learning pipelines are built upon visual encoders pre-trained for static recognition or vision-language alignment, leaving motion understanding to downstream policies. We introduce DynaFLIP, a dynamics-aware multimodal pre-training framework that pushes motion understanding upstream into perception. We construct image-language-3D flow triplets from heterogeneous human and robot videos, and use these triplets as training-time supervision to shape an image-only encoder. Our key idea is to encourage the three modalities to span a small simplex volume in the shared hyperspherical space -- a smaller simplex volume indicating stronger alignment. To avoid the geometric ambiguity and trivial collapse of naive volume minimization, we combine simplex-volume minimization with a cosine regularizer and a contrastive objective. Our analyses show that DynaFLIP focuses on control-relevant regions critical for manipulation. The resulting dynamics-aware representations serve as reusable visual backbones and consistently outperform baselines across diverse downstream policies, including VLAs. We validate this across diverse simulation and real-world setups, with gains reaching +22.5% under out-of-distribution scenarios. Our results suggest that robot generalization improves when visual representations are trained to encode not just what is present, but how the world changes under action.
匹配关键词: contrastive learning
---

[ACADEMIC - ARXIV]
标题: LLMSurgeon: Diagnosing Data Mixture of Large Language Models
作者: Yaxin Luo, Jiacheng Cui, Xiaohan Zhao, Xinyi Shang, Jiacheng Liu, Xinyue Bi, Zhaoyi Li, Zhiqiang Shen
链接: https://arxiv.org/abs/2605.30348v1
完整摘要: The pretraining data mixture of Large Language Models (LLMs) constitutes their "digital DNA", shaping model behaviors, capabilities, and failure modes. Yet this composition is rarely disclosed, making post-hoc auditing of data combination or provenance difficult. In this work, we formalize $\textbf{Data Mixture Surgery (DMS)}$: given only generated text from a target LLM, estimate the domain-level distribution of its pretraining corpus under a predefined taxonomy. We propose $\textbf{LLMSurgeon}$, a strong framework that casts DMS as an inverse problem under the label-shift assumption. Rather than directly aggregating classifier outputs, LLMSurgeon estimates a calibrated $\textit{soft}$ confusion matrix and solves a constrained inverse problem to correct systematic domain confusion and recover the latent mixture prior. To evaluate, we introduce $\textbf{LLMScan}$, a recipe-verifiable evaluation suite built from open-source LLMs with transparent pretraining mixtures. Across LLMScan, LLMSurgeon recovers domain mixtures with high fidelity under fixed protocols. Our work presents a practical, post-hoc approach for auditing the digital DNA of foundation models without access to their training data.
匹配关键词: contrastive learning
---

[ACADEMIC - ARXIV]
标题: NeuROK: Generative 4D Neural Object Kinematics
作者: Chen Geng, Guangzhao He, Yue Gao, Yunzhi Zhang, Shangzhe Wu, Jiajun Wu
链接: https://arxiv.org/abs/2605.30347v1
完整摘要: Data-driven approaches have revolutionized 3D vision, enabling transformers to effectively reconstruct and generate static 3D objects. However, generating simulative 4D dynamics -- realistic temporal deformations of static objects under various physical conditions -- remains challenging and often ad hoc, despite its importance in building comprehensive 3D world models. Most existing methods assume a predefined physical model and use system identification to estimate parameters, restricting these methods to specific categories and small-scale datasets. We propose that these restrictions can be overcome by learning a data-driven kinematic state parameterization for object-centric physical systems. Specifically, we learn both a latent space representing all possible states of the object and a decoder that maps any sampled latent to a plausibly deformed shape of the object. We refer to this parameterization as Neural Object Kinematics (NeuROK), and learn a transformer-based encoder-decoder model on a curated large-scale 4D dataset. This formulation and the learned model significantly simplify the generation of simulative dynamics since we only need to consider the dynamics within a low-dimensional latent space from the Lagrangian mechanics' perspective in classical physics. We demonstrate the effectiveness and generality of this neural simulation framework across diverse dynamic object types, showing clear advantages over prior works. Project page: https://chen-geng.com/neurok
匹配关键词: contrastive learning
---

[ACADEMIC - ARXIV]
标题: SchGen: PCB Schematic Generation with Semantic-Grounded Code Representations
作者: Qinpei Luo, Ruichun Ma, Xinyu Zhang, Lili Qiu
链接: https://arxiv.org/abs/2605.30345v1
完整摘要: Printed circuit board (PCB) schematic design defines nearly all electronic hardware, but it remains manual and expertise-intensive. While generative AI has advanced digital and analog IC design, PCB schematic generation from natural-language intent is largely unexplored. This paper presents SchGen, the first large language model that generates editable PCB schematics from natural-language requests. The key challenge lies in the lack of an LLM-suited representation and a large-scale dataset. Current schematic formats are dominated by verbose, tool-specific syntax and geometry-heavy descriptions, making them difficult to generate reliably. We introduce a semantically grounded code representation that encodes schematic editing primitives with relative placement and pin-name-based wiring, transforming a geometry-driven generation problem into a semantics-driven matching task amenable to LLMs. We further construct a large-scale dataset of PCB schematics paired with user prompts via a human-agent collaborative pipeline that converts open-source hardware designs into our representation. Experiments show that SchGen significantly outperforms alternative representations and even larger general-purpose LLMs on wire connectivity accuracy and functional correctness. Our results highlight the critical role of representation design in enabling generative models for complex hardware design tasks.
匹配关键词: contrastive learning
---

[ACADEMIC - ARXIV]
标题: Unlocking the Working Memory of Large Language Models for Latent Reasoning
作者: Lukas Aichberger, Sepp Hochreiter
链接: https://arxiv.org/abs/2605.30343v1
完整摘要: To improve the reasoning capabilities of large language models, test-time compute is typically scaled by generating intermediate tokens before the final answer. However, this couples reasoning to autoregressive generation and thereby conflates internal computation with external communication. In contrast, human cognition can use working memory to hold and manipulate information internally without the need to externalize intermediate thoughts. Drawing on this principle, we introduce Reasoning in Memory (RiM), a latent reasoning method that replaces the autoregressive generation of reasoning steps with memory blocks. These memory blocks are fixed sequences of special tokens that unlock the working-memory capacity of large language models. Since they are fixed rather than generated, they can be processed in a single forward pass, enabling compute-efficient latent reasoning. To operationalize these memory blocks, we employ a two-stage curriculum. First, we ground them by predicting explicit reasoning steps after each memory block. Second, we discard this step-level supervision and iteratively refine the final answer after each memory block. Our experiments on reasoning benchmarks show that, across language models of different families and sizes, RiM matches or exceeds existing latent reasoning methods while avoiding the autoregressive generation of thoughts. These results demonstrate that large language models can be trained to use working memory as an effective mechanism for latent reasoning.
匹配关键词: contrastive learning
---

[ACADEMIC - ARXIV]
标题: DynaFLIP: Rethinking Robotics Perception via Tri-Modal-Dynamics Guided Representation
作者: Jusuk Lee, Seungjae Lee, Jonghun Shin, Hoseong Jung, Sungha Kim, Daesol Cho, H. Jin Kim, Jia-Bin Huang, Furong Huang
链接: https://arxiv.org/abs/2605.30350v1
完整摘要: Robot manipulation critically depends on perception that preserves the action-relevant aspects of a scene. Yet most robot learning pipelines are built upon visual encoders pre-trained for static recognition or vision-language alignment, leaving motion understanding to downstream policies. We introduce DynaFLIP, a dynamics-aware multimodal pre-training framework that pushes motion understanding upstream into perception. We construct image-language-3D flow triplets from heterogeneous human and robot videos, and use these triplets as training-time supervision to shape an image-only encoder. Our key idea is to encourage the three modalities to span a small simplex volume in the shared hyperspherical space -- a smaller simplex volume indicating stronger alignment. To avoid the geometric ambiguity and trivial collapse of naive volume minimization, we combine simplex-volume minimization with a cosine regularizer and a contrastive objective. Our analyses show that DynaFLIP focuses on control-relevant regions critical for manipulation. The resulting dynamics-aware representations serve as reusable visual backbones and consistently outperform baselines across diverse downstream policies, including VLAs. We validate this across diverse simulation and real-world setups, with gains reaching +22.5% under out-of-distribution scenarios. Our results suggest that robot generalization improves when visual representations are trained to encode not just what is present, but how the world changes under action.
匹配关键词: representation learning
---

[ACADEMIC - ARXIV]
标题: LLMSurgeon: Diagnosing Data Mixture of Large Language Models
作者: Yaxin Luo, Jiacheng Cui, Xiaohan Zhao, Xinyi Shang, Jiacheng Liu, Xinyue Bi, Zhaoyi Li, Zhiqiang Shen
链接: https://arxiv.org/abs/2605.30348v1
完整摘要: The pretraining data mixture of Large Language Models (LLMs) constitutes their "digital DNA", shaping model behaviors, capabilities, and failure modes. Yet this composition is rarely disclosed, making post-hoc auditing of data combination or provenance difficult. In this work, we formalize $\textbf{Data Mixture Surgery (DMS)}$: given only generated text from a target LLM, estimate the domain-level distribution of its pretraining corpus under a predefined taxonomy. We propose $\textbf{LLMSurgeon}$, a strong framework that casts DMS as an inverse problem under the label-shift assumption. Rather than directly aggregating classifier outputs, LLMSurgeon estimates a calibrated $\textit{soft}$ confusion matrix and solves a constrained inverse problem to correct systematic domain confusion and recover the latent mixture prior. To evaluate, we introduce $\textbf{LLMScan}$, a recipe-verifiable evaluation suite built from open-source LLMs with transparent pretraining mixtures. Across LLMScan, LLMSurgeon recovers domain mixtures with high fidelity under fixed protocols. Our work presents a practical, post-hoc approach for auditing the digital DNA of foundation models without access to their training data.
匹配关键词: representation learning
---

[ACADEMIC - ARXIV]
标题: AdaState: Self-Evolving Anchors for Streaming Video Generation
作者: Yusuf Dalva, Pinar Yanardag
链接: https://arxiv.org/abs/2605.30349v1
完整摘要: Autoregressive video diffusion models generate streaming video by producing frames sequentially, conditioning each chunk on previously generated content. These models are structurally anchored to the first frame: its key-value representation occupies a privileged position in the attention cache and serves as the primary scene reference throughout generation. As the cleanest and most error-free position in the cache, this anchor draws disproportionate attention, suppressing video dynamics, and locking scene composition to the initial viewpoint even as the scene naturally evolves. The result is a temporally shallow video in which motion, camera movement, and scene progression are dampened in favor of static consistency. To address this, we replace the static anchor with an adaptive state, a hidden latent that the model denoises alongside content at every chunk but never renders. Rather than referencing a frozen first frame, the model generates its own scene anchor at each step by attending to both the previous state and the current content, producing a reference that evolves with the generated content. Unlike standard video generation, which encodes an absolute notion of time, our formulation treats time as relative: every generation step sees the same positional structure regardless of how far generation has progressed, and the state transition is identical at every chunk. Together, these properties introduce a recurrence into the generation process, where denoising serves as the transition function, and the KV cache serves as the carrier, requiring no external module. Experiments demonstrate that the adaptive state substantially improves video dynamics, enabling richer motion and natural scene progression within generated videos.
匹配关键词: representation learning
---

[ACADEMIC - ARXIV]
标题: NeuROK: Generative 4D Neural Object Kinematics
作者: Chen Geng, Guangzhao He, Yue Gao, Yunzhi Zhang, Shangzhe Wu, Jiajun Wu
链接: https://arxiv.org/abs/2605.30347v1
完整摘要: Data-driven approaches have revolutionized 3D vision, enabling transformers to effectively reconstruct and generate static 3D objects. However, generating simulative 4D dynamics -- realistic temporal deformations of static objects under various physical conditions -- remains challenging and often ad hoc, despite its importance in building comprehensive 3D world models. Most existing methods assume a predefined physical model and use system identification to estimate parameters, restricting these methods to specific categories and small-scale datasets. We propose that these restrictions can be overcome by learning a data-driven kinematic state parameterization for object-centric physical systems. Specifically, we learn both a latent space representing all possible states of the object and a decoder that maps any sampled latent to a plausibly deformed shape of the object. We refer to this parameterization as Neural Object Kinematics (NeuROK), and learn a transformer-based encoder-decoder model on a curated large-scale 4D dataset. This formulation and the learned model significantly simplify the generation of simulative dynamics since we only need to consider the dynamics within a low-dimensional latent space from the Lagrangian mechanics' perspective in classical physics. We demonstrate the effectiveness and generality of this neural simulation framework across diverse dynamic object types, showing clear advantages over prior works. Project page: https://chen-geng.com/neurok
匹配关键词: representation learning
---

[ACADEMIC - ARXIV]
标题: SchGen: PCB Schematic Generation with Semantic-Grounded Code Representations
作者: Qinpei Luo, Ruichun Ma, Xinyu Zhang, Lili Qiu
链接: https://arxiv.org/abs/2605.30345v1
完整摘要: Printed circuit board (PCB) schematic design defines nearly all electronic hardware, but it remains manual and expertise-intensive. While generative AI has advanced digital and analog IC design, PCB schematic generation from natural-language intent is largely unexplored. This paper presents SchGen, the first large language model that generates editable PCB schematics from natural-language requests. The key challenge lies in the lack of an LLM-suited representation and a large-scale dataset. Current schematic formats are dominated by verbose, tool-specific syntax and geometry-heavy descriptions, making them difficult to generate reliably. We introduce a semantically grounded code representation that encodes schematic editing primitives with relative placement and pin-name-based wiring, transforming a geometry-driven generation problem into a semantics-driven matching task amenable to LLMs. We further construct a large-scale dataset of PCB schematics paired with user prompts via a human-agent collaborative pipeline that converts open-source hardware designs into our representation. Experiments show that SchGen significantly outperforms alternative representations and even larger general-purpose LLMs on wire connectivity accuracy and functional correctness. Our results highlight the critical role of representation design in enabling generative models for complex hardware design tasks.
匹配关键词: representation learning
---

[ACADEMIC - ARXIV]
标题: Physics Is All You Need? A Case Study in Physicist-Supervised AI Development of Scientific Software
作者: Nhat-Minh Nguyen
链接: https://arxiv.org/abs/2605.30353v1
完整摘要: Are AI agents tools, co-authors, or researchers? We present a quantified case study ($N=1$): a physicist supervising an AI coding agent (Claude Code, Sonnet and Opus models) over 12 work days and 57 sessions to build CLAX-PT, a differentiable one-loop perturbation theory module in JAX. We documented and classified 15 supervision events by intervention level. The agent resolved ten autonomously by iterating against oracle tests. Two more by the physicist's domain knowledge. The three it could not -- all evaded oracle detection -- share a common property: the agent treated symptom reduction as root-cause resolution. It spent 33 of the 57 sessions adjusting coefficients within a code architecture that could not represent the target physics, and could not re-evaluate its CLASS-PT branch choice even when prompted to reconsider; only an injected physics concept (anisotropic BAO damping) triggered the redesign. Separately, the agent committed a calibrated correction that passed all oracle tests but corresponded to no quantity in the theory, predicting wrong values at any other cosmology. The fudge factor was caught and replaced within the same session. Three supervision practices proved critical for catching what oracle tests missed: testing at diverse parameter points beyond the fiducial calibration; shared changelogs that surfaced stalled exploration across sessions; and an explicit rule against unphysical numerical patches. In this case, supervision design, not model capability, determined whether the agent's output was trustworthy. Closing the gap would require agents that propose architectural alternatives rather than optimize within a given structure, and distinguish predictive adequacy from explanatory correctness -- capabilities not exhibited here, not obviously addressed by scaling alone. [Abridged.]
匹配关键词: masked language model
---

[ACADEMIC - ARXIV]
标题: VideoMLA: Low-Rank Latent KV Cache for Minute-Scale Autoregressive Video Diffusion
作者: Hidir Yesiltepe, Jiazhen Hu, Tuna Han Salih Meral, Adil Kaan Akan, Kaan Oktay, Hoda Eldardiry, Pinar Yanardag
链接: https://arxiv.org/abs/2605.30351v1
完整摘要: Long-rollout causal video diffusion has converged on a fixed-size sliding-window KV cache, with recent progress innovating within this layout by changing which tokens occupy the window or how their positions are encoded. The per-head KV layout itself, a dominant contributor to streaming memory and latency, has been mostly left unchanged. In this paper, we present the first study of Multi-Head Latent Attention (MLA) in video diffusion. VideoMLA replaces per-head keys and values with a shared low-rank content latent and a shared decoupled 3D-RoPE positional key, reducing per-token KV memory by 92.7% at every cached layer. We further investigate why MLA succeeds in video diffusion even though the spectral assumption often used to motivate it in language models does not hold: pretrained video attention is not low-rank, with 99%-energy effective rank far above any practical latent dimension. VideoMLA retains quality at compression ratios where direct spectral approximation would predict large reconstruction error. We show that the MLA bottleneck, rather than the pretrained spectrum, determines the effective rank: both spectral and random initialization occupy nearly the full rank budget from initialization, and training preserves this budget while adapting within it. On VBench, VideoMLA matches short-horizon streaming video diffusion baselines, achieves the best overall score at long horizons among evaluated methods, and improves throughput by 1.23x on a single B200.
匹配关键词: masked language model
---

[ACADEMIC - ARXIV]
标题: DynaFLIP: Rethinking Robotics Perception via Tri-Modal-Dynamics Guided Representation
作者: Jusuk Lee, Seungjae Lee, Jonghun Shin, Hoseong Jung, Sungha Kim, Daesol Cho, H. Jin Kim, Jia-Bin Huang, Furong Huang
链接: https://arxiv.org/abs/2605.30350v1
完整摘要: Robot manipulation critically depends on perception that preserves the action-relevant aspects of a scene. Yet most robot learning pipelines are built upon visual encoders pre-trained for static recognition or vision-language alignment, leaving motion understanding to downstream policies. We introduce DynaFLIP, a dynamics-aware multimodal pre-training framework that pushes motion understanding upstream into perception. We construct image-language-3D flow triplets from heterogeneous human and robot videos, and use these triplets as training-time supervision to shape an image-only encoder. Our key idea is to encourage the three modalities to span a small simplex volume in the shared hyperspherical space -- a smaller simplex volume indicating stronger alignment. To avoid the geometric ambiguity and trivial collapse of naive volume minimization, we combine simplex-volume minimization with a cosine regularizer and a contrastive objective. Our analyses show that DynaFLIP focuses on control-relevant regions critical for manipulation. The resulting dynamics-aware representations serve as reusable visual backbones and consistently outperform baselines across diverse downstream policies, including VLAs. We validate this across diverse simulation and real-world setups, with gains reaching +22.5% under out-of-distribution scenarios. Our results suggest that robot generalization improves when visual representations are trained to encode not just what is present, but how the world changes under action.
匹配关键词: masked language model
---

[ACADEMIC - ARXIV]
标题: LLMSurgeon: Diagnosing Data Mixture of Large Language Models
作者: Yaxin Luo, Jiacheng Cui, Xiaohan Zhao, Xinyi Shang, Jiacheng Liu, Xinyue Bi, Zhaoyi Li, Zhiqiang Shen
链接: https://arxiv.org/abs/2605.30348v1
完整摘要: The pretraining data mixture of Large Language Models (LLMs) constitutes their "digital DNA", shaping model behaviors, capabilities, and failure modes. Yet this composition is rarely disclosed, making post-hoc auditing of data combination or provenance difficult. In this work, we formalize $\textbf{Data Mixture Surgery (DMS)}$: given only generated text from a target LLM, estimate the domain-level distribution of its pretraining corpus under a predefined taxonomy. We propose $\textbf{LLMSurgeon}$, a strong framework that casts DMS as an inverse problem under the label-shift assumption. Rather than directly aggregating classifier outputs, LLMSurgeon estimates a calibrated $\textit{soft}$ confusion matrix and solves a constrained inverse problem to correct systematic domain confusion and recover the latent mixture prior. To evaluate, we introduce $\textbf{LLMScan}$, a recipe-verifiable evaluation suite built from open-source LLMs with transparent pretraining mixtures. Across LLMScan, LLMSurgeon recovers domain mixtures with high fidelity under fixed protocols. Our work presents a practical, post-hoc approach for auditing the digital DNA of foundation models without access to their training data.
匹配关键词: masked language model
---

[ACADEMIC - ARXIV]
标题: AdaState: Self-Evolving Anchors for Streaming Video Generation
作者: Yusuf Dalva, Pinar Yanardag
链接: https://arxiv.org/abs/2605.30349v1
完整摘要: Autoregressive video diffusion models generate streaming video by producing frames sequentially, conditioning each chunk on previously generated content. These models are structurally anchored to the first frame: its key-value representation occupies a privileged position in the attention cache and serves as the primary scene reference throughout generation. As the cleanest and most error-free position in the cache, this anchor draws disproportionate attention, suppressing video dynamics, and locking scene composition to the initial viewpoint even as the scene naturally evolves. The result is a temporally shallow video in which motion, camera movement, and scene progression are dampened in favor of static consistency. To address this, we replace the static anchor with an adaptive state, a hidden latent that the model denoises alongside content at every chunk but never renders. Rather than referencing a frozen first frame, the model generates its own scene anchor at each step by attending to both the previous state and the current content, producing a reference that evolves with the generated content. Unlike standard video generation, which encodes an absolute notion of time, our formulation treats time as relative: every generation step sees the same positional structure regardless of how far generation has progressed, and the state transition is identical at every chunk. Together, these properties introduce a recurrence into the generation process, where denoising serves as the transition function, and the KV cache serves as the carrier, requiring no external module. Experiments demonstrate that the adaptive state substantially improves video dynamics, enabling richer motion and natural scene progression within generated videos.
匹配关键词: masked language model
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
标题: SchGen: PCB Schematic Generation with Semantic-Grounded Code Representations
作者: Qinpei Luo, Ruichun Ma, Xinyu Zhang, Lili Qiu
链接: https://arxiv.org/abs/2605.30345v1
完整摘要: Printed circuit board (PCB) schematic design defines nearly all electronic hardware, but it remains manual and expertise-intensive. While generative AI has advanced digital and analog IC design, PCB schematic generation from natural-language intent is largely unexplored. This paper presents SchGen, the first large language model that generates editable PCB schematics from natural-language requests. The key challenge lies in the lack of an LLM-suited representation and a large-scale dataset. Current schematic formats are dominated by verbose, tool-specific syntax and geometry-heavy descriptions, making them difficult to generate reliably. We introduce a semantically grounded code representation that encodes schematic editing primitives with relative placement and pin-name-based wiring, transforming a geometry-driven generation problem into a semantics-driven matching task amenable to LLMs. We further construct a large-scale dataset of PCB schematics paired with user prompts via a human-agent collaborative pipeline that converts open-source hardware designs into our representation. Experiments show that SchGen significantly outperforms alternative representations and even larger general-purpose LLMs on wire connectivity accuracy and functional correctness. Our results highlight the critical role of representation design in enabling generative models for complex hardware design tasks.
匹配关键词: MAE
---

[ACADEMIC - ARXIV]
标题: REST3D: Reconstructing Physically Stable 3D Scenes from a Single Image
作者: Xiaoxuan Ma, Jiashun Wang, Nicolas Ugrinovic, Yehonathan Litman, Kris Kitani
链接: https://arxiv.org/abs/2605.30338v1
完整摘要: Reconstructing physically stable 3D scenes from a single RGB image enables casual images to be converted into simulation-ready digital assets for applications such as immersive interaction and content creation. However, existing single-image reconstruction methods fall short in capturing the physical structure of a scene. As a result, they often produce geometrically plausible but physically inconsistent results, including object floating and penetration, which lead to unstable behavior in physics simulations. Image-conditioned scene generation methods improve physical plausibility but often rely on strong scene priors, yielding plausible yet inaccurate object arrangements that fail to match the input image. We propose REST3D, a single-image reconstruction framework that can reconstruct physically stable 3D scenes by integrating physical scene understanding with physics-constrained refinement. We first introduce an agentic physical scene understanding technique that constructs a scene-tree representation capturing object physical states and inter-object relationships from a gravity-support perspective, providing a structural prior for reconstruction. Leveraging this structure, we initialize the scene using image-to-3D models, followed by scene-tree-guided alignment and physics-constrained optimization to resolve physical violations while preserving visual consistency with the input image. Experiments show that our method significantly reduces physical errors and improves simulation stability on both synthetic and real-world datasets while maintaining strong reconstruction quality. We further demonstrate the reconstructed scenes in VR-based human-object interaction, showing their potential for immersive applications.
匹配关键词: MAE
---

[ACADEMIC - ARXIV]
标题: A Heterogeneous Architecture for Robot RL Beyond GPU-Dominant Paradigms
作者: Yufei Jia, Zhanxiang Cao, Mingrui Yu, Heng Zhang, Shenyu Chen, Dixuan Jiang, Meng Li, Xiaofan Li, Yiyang Liu, Junzhe Wu, Zheng Li, XiLin Fang, Tingyu Cui, Shengcheng Fu, Haoyang Li, Anqi Wang, Zifan Wang, Dongjie Zhu, Chenyu Cao, Zhenbiao Huang, Ziang Zheng, Jie Lu, Xin Ma, Zhengyang Wei, Xiang Zhao, Tianyue Zhan, Ye He, Yuxiang Chen, Yizhou Jiang, Yue Li, Haizhou Ge, Yuhang Dong, Fan Jia, Ziheng Zhang, Meng Zhang, Xiwa Deng, Zhixing Chen, Hanyang Shao, Chenxin Dong, Yixuan Li, Yizhi Chen, Bokui Chen, Kaifeng Zhang, Hanqing Cui, Yusen Qin, Ruqi Huang, Lei Han, Tiancai Wang, Xiang Li, Yue Gao, Guyue Zhou
链接: https://arxiv.org/abs/2605.30313v1
完整摘要: Simulation-based RL for contemporary robot control is increasingly organized around GPU-resident simulation: physics, rollout collection, and learning are placed on a single GPU-centric execution path. This paradigm has greatly improved training speed, but it has also encouraged a default assumption that efficient training requires physics to reside on the GPU. We revisit this assumption. Our view is that, in simulation-dominated robot control, the essential question is not which processor runs physics, but whether simulation throughput, policy learning, and runtime synchronization form an efficient end-to-end loop. We present UniLab, a heterogeneous CPU-simulation / GPU-learning architecture that decouples CPU-parallel simulation from GPU policy updates through a unified runtime for data movement, buffering, and synchronization. UniLab is implemented as a complete and extensible training system using MuJoCoUni and MotrixSim CPU-batched physics backends, supporting PPO, SAC, FlashSAC, TD3, and APPO. On representative simulation-based robot control tasks, UniLab improves end-to-end training efficiency by 3--10$\times$ under the same hardware configuration, while reducing dependence on the NVIDIA CUDA-based software stack and supporting cross-platform execution on the Apple macOS platform and the AMD ROCm and Intel XPU accelerator backends. These results show that GPU simulation is an effective path to efficient training, but not a necessary one, broadening the practical system choices available for robot RL training. Project page: https://github.com/unilabsim/UniLab.
匹配关键词: MAE
---

[ACADEMIC - ARXIV]
标题: Gaze2Act: Gaze-Conditioned Vision-Language-Action Policies for Interactive Robot Manipulation
作者: Kuangji Zuo, Gen Li, Bofan Lyu, Yanshuo Lu, Boyu Ma, Shijia Han, Xinyu Zhou, Xichen Yuan, Chuhao Zhou, Jiaqi Bai, Geng Li, Jianfei Yang
链接: https://arxiv.org/abs/2605.30282v1
完整摘要: Vision-Language-Action (VLA) models have recently shown strong potential for robot learning by following language instructions. However, in practice, language alone is often insufficient to precisely convey human intent. It is difficult to describe which exact object to interact with among similar candidates, where to act on the object, or how the target may change during execution. To address this limitation, we propose Gaze2Act, a novel VLA framework that leverages human gaze as a dynamic and intuitive intent signal for complex interactive manipulation. Gaze2Act first bridges the ego-exo view gap by mapping first-person gaze into the robot's perspective through cross-view semantic matching, producing both an object mask and a gaze point for coarse-to-fine target specification. These cues are then integrated into the policy through perception-level prompting and action-level conditioning, allowing the robot to attend to relevant regions and execute precise interactions under dynamic intent. In a systematic evaluation across seven task categories and 16 real-robot tasks on a Unitree G1 humanoid, Gaze2Act achieves state-of-the-art performance in both intent accuracy and task success rate. It notably outperforms baselines in object disambiguation, fine-grained interaction, and dynamic intent steering. These results demonstrate that human gaze provides a natural, low-burden, and highly expressive modality for human-in-the-loop VLA control.
匹配关键词: MAE
---

[ACADEMIC - ARXIV]
标题: Beyond 3D VQAs: Injecting 3D Spatial Priors into Vision-Language Models for Enhanced Geometric Reasoning
作者: Chun-Hsiao Yeh, Shengyi Qian, Manchen Wang, Yi Ma, Joseph Tighe, Fanyi Xiao
链接: https://arxiv.org/abs/2605.30231v1
完整摘要: Vision-Language Models (VLMs) often struggle with robust 3D spatial reasoning. Prevailing methods that rely on fine-tuning with 3D visual question-answering (VQA) datasets may overfit dataset-specific biases, while integrating specialized 3D visual encoders is often inflexible and cumbersome. In this paper, we argue that genuine spatial understanding should emerge from learning fundamental geometric priors, not only from high-level VQA supervision. We propose GASP (Geometric-Aware Spatial Priors), a framework that injects these priors directly into the LLM's transformer layers. GASP employs a small correspondence head, applied as a deep supervision signal across all layers, and is trained with a dual objective leveraging ground-truth geometry from large-scale video scenes: a contrastive loss on ground-truth point correspondences enforces 2D view-invariance, while a depth consistency supervision resolves 3D geometric ambiguities. Our analysis first provides a diagnostic showing that standard VLMs' internal correspondence matching accuracy is very low (often below 5%). We then demonstrate that our training substantially improves this behavior, boosting peak layer-wise correspondence to over 70% and maintaining over 85% temporal robustness while baselines remain below 5%. These internal improvements translate to significant gains on downstream spatial benchmarks including +18.2% on All-Angles Bench and +29.0% on VSI-Bench, all without training on any 3D VQA data. Our findings indicate that learning from fundamental geometric priors is a promising and generalizable pathway towards VLMs with more reliable 3D spatial reasoning.
匹配关键词: MAE
---

[ACADEMIC - ARXIV]
标题: Physics Is All You Need? A Case Study in Physicist-Supervised AI Development of Scientific Software
作者: Nhat-Minh Nguyen
链接: https://arxiv.org/abs/2605.30353v1
完整摘要: Are AI agents tools, co-authors, or researchers? We present a quantified case study ($N=1$): a physicist supervising an AI coding agent (Claude Code, Sonnet and Opus models) over 12 work days and 57 sessions to build CLAX-PT, a differentiable one-loop perturbation theory module in JAX. We documented and classified 15 supervision events by intervention level. The agent resolved ten autonomously by iterating against oracle tests. Two more by the physicist's domain knowledge. The three it could not -- all evaded oracle detection -- share a common property: the agent treated symptom reduction as root-cause resolution. It spent 33 of the 57 sessions adjusting coefficients within a code architecture that could not represent the target physics, and could not re-evaluate its CLASS-PT branch choice even when prompted to reconsider; only an injected physics concept (anisotropic BAO damping) triggered the redesign. Separately, the agent committed a calibrated correction that passed all oracle tests but corresponded to no quantity in the theory, predicting wrong values at any other cosmology. The fudge factor was caught and replaced within the same session. Three supervision practices proved critical for catching what oracle tests missed: testing at diverse parameter points beyond the fiducial calibration; shared changelogs that surfaced stalled exploration across sessions; and an explicit rule against unphysical numerical patches. In this case, supervision design, not model capability, determined whether the agent's output was trustworthy. Closing the gap would require agents that propose architectural alternatives rather than optimize within a given structure, and distinguish predictive adequacy from explanatory correctness -- capabilities not exhibited here, not obviously addressed by scaling alone. [Abridged.]
匹配关键词: generative model
---

[ACADEMIC - ARXIV]
标题: VideoMLA: Low-Rank Latent KV Cache for Minute-Scale Autoregressive Video Diffusion
作者: Hidir Yesiltepe, Jiazhen Hu, Tuna Han Salih Meral, Adil Kaan Akan, Kaan Oktay, Hoda Eldardiry, Pinar Yanardag
链接: https://arxiv.org/abs/2605.30351v1
完整摘要: Long-rollout causal video diffusion has converged on a fixed-size sliding-window KV cache, with recent progress innovating within this layout by changing which tokens occupy the window or how their positions are encoded. The per-head KV layout itself, a dominant contributor to streaming memory and latency, has been mostly left unchanged. In this paper, we present the first study of Multi-Head Latent Attention (MLA) in video diffusion. VideoMLA replaces per-head keys and values with a shared low-rank content latent and a shared decoupled 3D-RoPE positional key, reducing per-token KV memory by 92.7% at every cached layer. We further investigate why MLA succeeds in video diffusion even though the spectral assumption often used to motivate it in language models does not hold: pretrained video attention is not low-rank, with 99%-energy effective rank far above any practical latent dimension. VideoMLA retains quality at compression ratios where direct spectral approximation would predict large reconstruction error. We show that the MLA bottleneck, rather than the pretrained spectrum, determines the effective rank: both spectral and random initialization occupy nearly the full rank budget from initialization, and training preserves this budget while adapting within it. On VBench, VideoMLA matches short-horizon streaming video diffusion baselines, achieves the best overall score at long horizons among evaluated methods, and improves throughput by 1.23x on a single B200.
匹配关键词: generative model
---

[ACADEMIC - ARXIV]
标题: DynaFLIP: Rethinking Robotics Perception via Tri-Modal-Dynamics Guided Representation
作者: Jusuk Lee, Seungjae Lee, Jonghun Shin, Hoseong Jung, Sungha Kim, Daesol Cho, H. Jin Kim, Jia-Bin Huang, Furong Huang
链接: https://arxiv.org/abs/2605.30350v1
完整摘要: Robot manipulation critically depends on perception that preserves the action-relevant aspects of a scene. Yet most robot learning pipelines are built upon visual encoders pre-trained for static recognition or vision-language alignment, leaving motion understanding to downstream policies. We introduce DynaFLIP, a dynamics-aware multimodal pre-training framework that pushes motion understanding upstream into perception. We construct image-language-3D flow triplets from heterogeneous human and robot videos, and use these triplets as training-time supervision to shape an image-only encoder. Our key idea is to encourage the three modalities to span a small simplex volume in the shared hyperspherical space -- a smaller simplex volume indicating stronger alignment. To avoid the geometric ambiguity and trivial collapse of naive volume minimization, we combine simplex-volume minimization with a cosine regularizer and a contrastive objective. Our analyses show that DynaFLIP focuses on control-relevant regions critical for manipulation. The resulting dynamics-aware representations serve as reusable visual backbones and consistently outperform baselines across diverse downstream policies, including VLAs. We validate this across diverse simulation and real-world setups, with gains reaching +22.5% under out-of-distribution scenarios. Our results suggest that robot generalization improves when visual representations are trained to encode not just what is present, but how the world changes under action.
匹配关键词: generative model
---

[ACADEMIC - ARXIV]
标题: LLMSurgeon: Diagnosing Data Mixture of Large Language Models
作者: Yaxin Luo, Jiacheng Cui, Xiaohan Zhao, Xinyi Shang, Jiacheng Liu, Xinyue Bi, Zhaoyi Li, Zhiqiang Shen
链接: https://arxiv.org/abs/2605.30348v1
完整摘要: The pretraining data mixture of Large Language Models (LLMs) constitutes their "digital DNA", shaping model behaviors, capabilities, and failure modes. Yet this composition is rarely disclosed, making post-hoc auditing of data combination or provenance difficult. In this work, we formalize $\textbf{Data Mixture Surgery (DMS)}$: given only generated text from a target LLM, estimate the domain-level distribution of its pretraining corpus under a predefined taxonomy. We propose $\textbf{LLMSurgeon}$, a strong framework that casts DMS as an inverse problem under the label-shift assumption. Rather than directly aggregating classifier outputs, LLMSurgeon estimates a calibrated $\textit{soft}$ confusion matrix and solves a constrained inverse problem to correct systematic domain confusion and recover the latent mixture prior. To evaluate, we introduce $\textbf{LLMScan}$, a recipe-verifiable evaluation suite built from open-source LLMs with transparent pretraining mixtures. Across LLMScan, LLMSurgeon recovers domain mixtures with high fidelity under fixed protocols. Our work presents a practical, post-hoc approach for auditing the digital DNA of foundation models without access to their training data.
匹配关键词: generative model
---

[ACADEMIC - ARXIV]
标题: AdaState: Self-Evolving Anchors for Streaming Video Generation
作者: Yusuf Dalva, Pinar Yanardag
链接: https://arxiv.org/abs/2605.30349v1
完整摘要: Autoregressive video diffusion models generate streaming video by producing frames sequentially, conditioning each chunk on previously generated content. These models are structurally anchored to the first frame: its key-value representation occupies a privileged position in the attention cache and serves as the primary scene reference throughout generation. As the cleanest and most error-free position in the cache, this anchor draws disproportionate attention, suppressing video dynamics, and locking scene composition to the initial viewpoint even as the scene naturally evolves. The result is a temporally shallow video in which motion, camera movement, and scene progression are dampened in favor of static consistency. To address this, we replace the static anchor with an adaptive state, a hidden latent that the model denoises alongside content at every chunk but never renders. Rather than referencing a frozen first frame, the model generates its own scene anchor at each step by attending to both the previous state and the current content, producing a reference that evolves with the generated content. Unlike standard video generation, which encodes an absolute notion of time, our formulation treats time as relative: every generation step sees the same positional structure regardless of how far generation has progressed, and the state transition is identical at every chunk. Together, these properties introduce a recurrence into the generation process, where denoising serves as the transition function, and the KV cache serves as the carrier, requiring no external module. Experiments demonstrate that the adaptive state substantially improves video dynamics, enabling richer motion and natural scene progression within generated videos.
匹配关键词: generative model
---

[ACADEMIC - ARXIV]
标题: Physics Is All You Need? A Case Study in Physicist-Supervised AI Development of Scientific Software
作者: Nhat-Minh Nguyen
链接: https://arxiv.org/abs/2605.30353v1
完整摘要: Are AI agents tools, co-authors, or researchers? We present a quantified case study ($N=1$): a physicist supervising an AI coding agent (Claude Code, Sonnet and Opus models) over 12 work days and 57 sessions to build CLAX-PT, a differentiable one-loop perturbation theory module in JAX. We documented and classified 15 supervision events by intervention level. The agent resolved ten autonomously by iterating against oracle tests. Two more by the physicist's domain knowledge. The three it could not -- all evaded oracle detection -- share a common property: the agent treated symptom reduction as root-cause resolution. It spent 33 of the 57 sessions adjusting coefficients within a code architecture that could not represent the target physics, and could not re-evaluate its CLASS-PT branch choice even when prompted to reconsider; only an injected physics concept (anisotropic BAO damping) triggered the redesign. Separately, the agent committed a calibrated correction that passed all oracle tests but corresponded to no quantity in the theory, predicting wrong values at any other cosmology. The fudge factor was caught and replaced within the same session. Three supervision practices proved critical for catching what oracle tests missed: testing at diverse parameter points beyond the fiducial calibration; shared changelogs that surfaced stalled exploration across sessions; and an explicit rule against unphysical numerical patches. In this case, supervision design, not model capability, determined whether the agent's output was trustworthy. Closing the gap would require agents that propose architectural alternatives rather than optimize within a given structure, and distinguish predictive adequacy from explanatory correctness -- capabilities not exhibited here, not obviously addressed by scaling alone. [Abridged.]
匹配关键词: diffusion model
---

[ACADEMIC - ARXIV]
标题: VideoMLA: Low-Rank Latent KV Cache for Minute-Scale Autoregressive Video Diffusion
作者: Hidir Yesiltepe, Jiazhen Hu, Tuna Han Salih Meral, Adil Kaan Akan, Kaan Oktay, Hoda Eldardiry, Pinar Yanardag
链接: https://arxiv.org/abs/2605.30351v1
完整摘要: Long-rollout causal video diffusion has converged on a fixed-size sliding-window KV cache, with recent progress innovating within this layout by changing which tokens occupy the window or how their positions are encoded. The per-head KV layout itself, a dominant contributor to streaming memory and latency, has been mostly left unchanged. In this paper, we present the first study of Multi-Head Latent Attention (MLA) in video diffusion. VideoMLA replaces per-head keys and values with a shared low-rank content latent and a shared decoupled 3D-RoPE positional key, reducing per-token KV memory by 92.7% at every cached layer. We further investigate why MLA succeeds in video diffusion even though the spectral assumption often used to motivate it in language models does not hold: pretrained video attention is not low-rank, with 99%-energy effective rank far above any practical latent dimension. VideoMLA retains quality at compression ratios where direct spectral approximation would predict large reconstruction error. We show that the MLA bottleneck, rather than the pretrained spectrum, determines the effective rank: both spectral and random initialization occupy nearly the full rank budget from initialization, and training preserves this budget while adapting within it. On VBench, VideoMLA matches short-horizon streaming video diffusion baselines, achieves the best overall score at long horizons among evaluated methods, and improves throughput by 1.23x on a single B200.
匹配关键词: diffusion model
---

[ACADEMIC - ARXIV]
标题: LLMSurgeon: Diagnosing Data Mixture of Large Language Models
作者: Yaxin Luo, Jiacheng Cui, Xiaohan Zhao, Xinyi Shang, Jiacheng Liu, Xinyue Bi, Zhaoyi Li, Zhiqiang Shen
链接: https://arxiv.org/abs/2605.30348v1
完整摘要: The pretraining data mixture of Large Language Models (LLMs) constitutes their "digital DNA", shaping model behaviors, capabilities, and failure modes. Yet this composition is rarely disclosed, making post-hoc auditing of data combination or provenance difficult. In this work, we formalize $\textbf{Data Mixture Surgery (DMS)}$: given only generated text from a target LLM, estimate the domain-level distribution of its pretraining corpus under a predefined taxonomy. We propose $\textbf{LLMSurgeon}$, a strong framework that casts DMS as an inverse problem under the label-shift assumption. Rather than directly aggregating classifier outputs, LLMSurgeon estimates a calibrated $\textit{soft}$ confusion matrix and solves a constrained inverse problem to correct systematic domain confusion and recover the latent mixture prior. To evaluate, we introduce $\textbf{LLMScan}$, a recipe-verifiable evaluation suite built from open-source LLMs with transparent pretraining mixtures. Across LLMScan, LLMSurgeon recovers domain mixtures with high fidelity under fixed protocols. Our work presents a practical, post-hoc approach for auditing the digital DNA of foundation models without access to their training data.
匹配关键词: diffusion model
---

[ACADEMIC - ARXIV]
标题: AdaState: Self-Evolving Anchors for Streaming Video Generation
作者: Yusuf Dalva, Pinar Yanardag
链接: https://arxiv.org/abs/2605.30349v1
完整摘要: Autoregressive video diffusion models generate streaming video by producing frames sequentially, conditioning each chunk on previously generated content. These models are structurally anchored to the first frame: its key-value representation occupies a privileged position in the attention cache and serves as the primary scene reference throughout generation. As the cleanest and most error-free position in the cache, this anchor draws disproportionate attention, suppressing video dynamics, and locking scene composition to the initial viewpoint even as the scene naturally evolves. The result is a temporally shallow video in which motion, camera movement, and scene progression are dampened in favor of static consistency. To address this, we replace the static anchor with an adaptive state, a hidden latent that the model denoises alongside content at every chunk but never renders. Rather than referencing a frozen first frame, the model generates its own scene anchor at each step by attending to both the previous state and the current content, producing a reference that evolves with the generated content. Unlike standard video generation, which encodes an absolute notion of time, our formulation treats time as relative: every generation step sees the same positional structure regardless of how far generation has progressed, and the state transition is identical at every chunk. Together, these properties introduce a recurrence into the generation process, where denoising serves as the transition function, and the KV cache serves as the carrier, requiring no external module. Experiments demonstrate that the adaptive state substantially improves video dynamics, enabling richer motion and natural scene progression within generated videos.
匹配关键词: diffusion model
---

[ACADEMIC - ARXIV]
标题: NeuROK: Generative 4D Neural Object Kinematics
作者: Chen Geng, Guangzhao He, Yue Gao, Yunzhi Zhang, Shangzhe Wu, Jiajun Wu
链接: https://arxiv.org/abs/2605.30347v1
完整摘要: Data-driven approaches have revolutionized 3D vision, enabling transformers to effectively reconstruct and generate static 3D objects. However, generating simulative 4D dynamics -- realistic temporal deformations of static objects under various physical conditions -- remains challenging and often ad hoc, despite its importance in building comprehensive 3D world models. Most existing methods assume a predefined physical model and use system identification to estimate parameters, restricting these methods to specific categories and small-scale datasets. We propose that these restrictions can be overcome by learning a data-driven kinematic state parameterization for object-centric physical systems. Specifically, we learn both a latent space representing all possible states of the object and a decoder that maps any sampled latent to a plausibly deformed shape of the object. We refer to this parameterization as Neural Object Kinematics (NeuROK), and learn a transformer-based encoder-decoder model on a curated large-scale 4D dataset. This formulation and the learned model significantly simplify the generation of simulative dynamics since we only need to consider the dynamics within a low-dimensional latent space from the Lagrangian mechanics' perspective in classical physics. We demonstrate the effectiveness and generality of this neural simulation framework across diverse dynamic object types, showing clear advantages over prior works. Project page: https://chen-geng.com/neurok
匹配关键词: diffusion model
---

[ACADEMIC - ARXIV]
标题: RoboWits: Unexpected Challenges for Robotic Creative Problem Solving
作者: Chunru Lin, Hongxin Zhang, Fenghao Yu, Zhehuan Chen, Thomas L. Griffiths, Yejin Choi, David Held, Chuang Gan
链接: https://arxiv.org/abs/2605.30326v1
完整摘要: The ability to reason, adapt, and creatively solve problems under unexpected challenges is essential for robots operating in real-world environments. However, current robotic benchmarks primarily emphasize skill-level execution and provide limited insight into such cognitive reasoning capabilities. We introduce RoboWits, a bi-manual robotic benchmark designed to systematically evaluate cognitive reasoning, creative tool use, and robustness to unexpected conditions. To enable scalable construction of high-quality reasoning-centric unexpected scenarios, we propose an automated task generation pipeline formulated as a multi-agent cooperative framework, comprising agents for seed task generation and verification, metric generation, scene generation, and task mutation. Using the pipeline, we curated 30 diverse seed tasks and 208 tasks with mutations and graded difficulty across geometry, material, and assembly-based reasoning. We benchmark popular robot policies, pre-trained VLAs, and oracle-state planners. Our results reveal a significant performance gap: while pre-trained VLAs exhibit preliminary success on seed tasks after single-task fine-tuning, they struggle to perform on mutated tasks, implying their brittleness in manipulation tasks requiring reasoning, strategy adaptation, and robustness to deceptive or constrained environments. Project page is available at https://umass-embodied-agi.github.io/RoboWits.
匹配关键词: GAN
---

[ACADEMIC - ARXIV]
标题: On the Geometry of Games and their Solvers
作者: Yaqi Sun, Julian Ma, David Mguni
链接: https://arxiv.org/abs/2605.29919v1
完整摘要: A central challenge in game theory and learning systems such as GANs is understanding which algorithms can efficiently compute equilibria across the heterogeneous landscape of games. Equilibrium computation is typically studied solver by solver and game class by game class, yielding strong local guarantees but a fragmented view of solver behaviour. Existing discrete taxonomies often provide an incomplete account of where algorithms succeed. We study this problem through a solver-game map linking games to effective solver dynamics. Classical theory identifies isolated regions of this map but provides limited insight into intermediate or overlapping regimes, suggesting that solvability is governed by latent structural properties defining a continuous solver-aligned geometry of games. We formalise this perspective through structure-aware solver synthesis. A learned structure recogniser maps each game to a low-dimensional solver-aligned representation, and a policy maps this representation to effective primitive mechanisms, adapting solver behaviour across regimes. This reveals regions where particular solver dynamics are effective and where mixtures of primitives are required rather than a single dominant solver. A bounded residual acts as a local corrector and diagnostic signal for incomplete solver bases or representations. The framework yields both an adaptive solver and an analytical lens: games with similar optimisation dynamics cluster together, revealing continuous regions of algorithmic validity and overlapping solver behaviour. Empirically, we show that fixed primitives exhibit systematic regime mismatch, while the learned representation organises game space into a structured cartography aligned with solver behaviour. These results suggest viewing equilibrium computation as the joint problem of learning solver mechanisms and mapping the geometry of solvability.
匹配关键词: GAN
---

[ACADEMIC - ARXIV]
标题: The Little Book of Generative AI Foundations: An Intuitive Mathematical Primer
作者: Tianhua Chen
链接: https://arxiv.org/abs/2605.29713v1
完整摘要: This book provides a compact, derivation-oriented introduction to the mathematical foundations of modern generative artificial intelligence. Rather than surveying every recent architecture or implementation detail, it develops a coherent route through the ideas connecting major families of generative models, from PCA, probabilistic PCA, variational autoencoders, and diffusion models to normalising flows, autoregressive factorisations, GANs, Wasserstein GANs, and energy-based models. The aim is to make the structure of generative modelling more accessible without removing the mathematical substance needed to understand how these models are derived and related. The book is intended as a foundation-building primer for mathematically curious researchers, practitioners, and students.
匹配关键词: GAN
---

[ACADEMIC - ARXIV]
标题: DeepFake Forensics AI: A Multi-Modal Detection and Blockchain-Anchored Evidence Management Platform
作者: Naisha Minnah
链接: https://arxiv.org/abs/2605.29353v1
完整摘要: The proliferation of AI-generated synthetic media poses a critical threat to the integrity of digital evidence in legal and forensic contexts. Existing deepfake detection systems typically address a single modality and provide no mechanism for tamper-proof evidence preservation. We present DeepFake Forensics AI, a unified platform that detects synthetic media across image, video, and audio modalities, identifies generative architecture fingerprints, and anchors forensic evidence immutably on the Ethereum blockchain. Our system trains four independent neural networks from scratch: an EfficientNet-B4 image detector (AUC = 0.9868), a Bidirectional LSTM video detector (AUC= 0.9628), an ECAPA-TDNN audio detector (EER = 18.63%), and a novel GAN fingerprinting module (accuracy = 99.88%) that identifies the generative architecture behind a fake image. Evidence files are hashed with SHA-256, stored on IPFS via Pinata, and registered on-chain via a Solidity smart contract with role-based access control. The platform provides a React frontend and FastAPI backend suitable for deployment in forensic and legal workflows. To our knowledge, this is the first system to unify multi-modal deepfake detection with blockchain-based chain-of custody management.
匹配关键词: GAN
---

[ACADEMIC - ARXIV]
标题: CapTalk: Text-Guided Stylization and Speech-Driven 3D Head Animation
作者: Xuangeng Chu, Yuan Gan, Ziteng Cui, Shuhong Liu, Jian Wang, Bing Zhou, Tatsuya Harada
链接: https://arxiv.org/abs/2605.29316v1
完整摘要: Audio-driven 3D facial animation aims to generate synchronized lip movements and vivid facial expressions from arbitrary audio clips. While existing methods can produce synchronized lip motions, they often rely on predefined identity or style latent features, which limits users' ability to freely control speaking styles. Moreover, applying a fixed style or identity to an entire audio segment typically results in facial animation styles that do not adapt to the emotional content of the audio. To address these challenges, we revisit the entanglement between style and emotion, construct a large-scale dataset with textual descriptions of both style and emotion, and propose a novel talking head generation framework that enables separate control over style and emotion. Our model takes as input both textual descriptions of speaking style and character emotion, as well as the driving audio stream, enabling real-time generation of highly synchronized lip movements and facial expressions that match the provided descriptions. Furthermore, our model supports dynamic emotion control during inference, allowing it to handle scenarios where the target emotion changes throughout the speech.
匹配关键词: GAN
---

[ACADEMIC - ARXIV]
标题: From GPS Points to Travel Patterns: Flexible and Semantic Trajectory Generation with LLMs
作者: Silin Zhou, Chenhao Wang, Yuntao Wen, Shuo Shang, Lisi Chen, Panos Kalnis
链接: https://arxiv.org/abs/2605.30014v1
完整摘要: Urban trajectories play a crucial role in modeling urban dynamics and supporting various smart city applications. However, privacy concerns restrict access to large-scale and high-quality trajectory datasets. Trajectory generation provides a promising alternative by synthesizing realistic data to mitigate privacy risks. However, existing methods fail to explicitly capture travel patterns and can only generate fixed-length trajectories under a single condition. To address these limitations, we propose \textbf{HTP}, which \textbf{H}ierarchically generates \textbf{T}ravel patterns first and then generates GPS \textbf{P}oints by using large language models (LLMs), rather than directly generating GPS points. We first design a trajectory-specific residual quantization variational autoencoder (RQ-VAE) that quantizes micro-level GPS trajectories into compact, macro-level travel pattern tokens in a coarse-to-fine manner. These tokens capture rich segment spatial irregularities, such as point density variations caused by traffic conditions. Then, we extend the LLM vocabulary with travel pattern tokens to align trajectory representations with the LLM input, and apply supervised fine-tuning (SFT) to align the LLM with the trajectory generation task, enabling generation of travel pattern sequences under various conditions. Extensive experiments on two real-world datasets show that HTP outperforms the strongest baseline by an average of 29.78\% in terms of generation quality. Our code is available at https://github.com/slzhou-xy/HTP.
匹配关键词: VAE
---

[ACADEMIC - ARXIV]
标题: Deep Adaptive Dimension Reduction for Bayesian Inference in Inverse Problems
作者: Yueyang Wang, Xili Wang, Kejun Tang, Xiaoliang Wan, Tao Zhou, Chao Yang
链接: https://arxiv.org/abs/2605.29373v1
完整摘要: Solving high-dimensional PDE-governed inverse problems is often challenging due to complex non-Gaussian posterior distributions, expensive forward model evaluations, and misspecified prior information. To address these issues, we propose a deep adaptive dimension-reduction Bayesian inference framework based on the Variational Flow (VF) model. Since standard normalizing flows are restricted by bijective mappings and cannot directly reduce dimensions, VF overcomes this limitation by integrating VAE-based nonlinear dimension reduction with dual normalizing flows for the latent prior and encoder. This design provides a strictly higher evidence lower bound than VAE and allows more flexible approximation of complex posterior distributions. We further introduce an iterative prior updating strategy that gradually moves the prior mean toward high-probability posterior regions, avoiding manual prior tuning. These components form a closed adaptive loop together with an adaptively fine-tuned Fourier Neural Operator (FNO) surrogate: VF generates posterior-concentrated samples to refine the surrogate, while the updated surrogate further improves posterior inference. Numerical experiments on a 100-dimensional Rosenbrock problem and three standard PDE-governed inverse problems show that our method delivers competitive or superior accuracy compared with MCMC, UKI, and SVGD baselines across all tested configurations, with the most pronounced advantages emerging in challenging scenarios such as high-noise observations and high-dimensional parameter spaces.
匹配关键词: VAE
---

[ACADEMIC - ARXIV]
标题: VideoMLA: Low-Rank Latent KV Cache for Minute-Scale Autoregressive Video Diffusion
作者: Hidir Yesiltepe, Jiazhen Hu, Tuna Han Salih Meral, Adil Kaan Akan, Kaan Oktay, Hoda Eldardiry, Pinar Yanardag
链接: https://arxiv.org/abs/2605.30351v1
完整摘要: Long-rollout causal video diffusion has converged on a fixed-size sliding-window KV cache, with recent progress innovating within this layout by changing which tokens occupy the window or how their positions are encoded. The per-head KV layout itself, a dominant contributor to streaming memory and latency, has been mostly left unchanged. In this paper, we present the first study of Multi-Head Latent Attention (MLA) in video diffusion. VideoMLA replaces per-head keys and values with a shared low-rank content latent and a shared decoupled 3D-RoPE positional key, reducing per-token KV memory by 92.7% at every cached layer. We further investigate why MLA succeeds in video diffusion even though the spectral assumption often used to motivate it in language models does not hold: pretrained video attention is not low-rank, with 99%-energy effective rank far above any practical latent dimension. VideoMLA retains quality at compression ratios where direct spectral approximation would predict large reconstruction error. We show that the MLA bottleneck, rather than the pretrained spectrum, determines the effective rank: both spectral and random initialization occupy nearly the full rank budget from initialization, and training preserves this budget while adapting within it. On VBench, VideoMLA matches short-horizon streaming video diffusion baselines, achieves the best overall score at long horizons among evaluated methods, and improves throughput by 1.23x on a single B200.
匹配关键词: autoregressive
---

[ACADEMIC - ARXIV]
标题: AdaState: Self-Evolving Anchors for Streaming Video Generation
作者: Yusuf Dalva, Pinar Yanardag
链接: https://arxiv.org/abs/2605.30349v1
完整摘要: Autoregressive video diffusion models generate streaming video by producing frames sequentially, conditioning each chunk on previously generated content. These models are structurally anchored to the first frame: its key-value representation occupies a privileged position in the attention cache and serves as the primary scene reference throughout generation. As the cleanest and most error-free position in the cache, this anchor draws disproportionate attention, suppressing video dynamics, and locking scene composition to the initial viewpoint even as the scene naturally evolves. The result is a temporally shallow video in which motion, camera movement, and scene progression are dampened in favor of static consistency. To address this, we replace the static anchor with an adaptive state, a hidden latent that the model denoises alongside content at every chunk but never renders. Rather than referencing a frozen first frame, the model generates its own scene anchor at each step by attending to both the previous state and the current content, producing a reference that evolves with the generated content. Unlike standard video generation, which encodes an absolute notion of time, our formulation treats time as relative: every generation step sees the same positional structure regardless of how far generation has progressed, and the state transition is identical at every chunk. Together, these properties introduce a recurrence into the generation process, where denoising serves as the transition function, and the KV cache serves as the carrier, requiring no external module. Experiments demonstrate that the adaptive state substantially improves video dynamics, enabling richer motion and natural scene progression within generated videos.
匹配关键词: autoregressive
---

[ACADEMIC - ARXIV]
标题: Unlocking the Working Memory of Large Language Models for Latent Reasoning
作者: Lukas Aichberger, Sepp Hochreiter
链接: https://arxiv.org/abs/2605.30343v1
完整摘要: To improve the reasoning capabilities of large language models, test-time compute is typically scaled by generating intermediate tokens before the final answer. However, this couples reasoning to autoregressive generation and thereby conflates internal computation with external communication. In contrast, human cognition can use working memory to hold and manipulate information internally without the need to externalize intermediate thoughts. Drawing on this principle, we introduce Reasoning in Memory (RiM), a latent reasoning method that replaces the autoregressive generation of reasoning steps with memory blocks. These memory blocks are fixed sequences of special tokens that unlock the working-memory capacity of large language models. Since they are fixed rather than generated, they can be processed in a single forward pass, enabling compute-efficient latent reasoning. To operationalize these memory blocks, we employ a two-stage curriculum. First, we ground them by predicting explicit reasoning steps after each memory block. Second, we discard this step-level supervision and iteratively refine the final answer after each memory block. Our experiments on reasoning benchmarks show that, across language models of different families and sizes, RiM matches or exceeds existing latent reasoning methods while avoiding the autoregressive generation of thoughts. These results demonstrate that large language models can be trained to use working memory as an effective mechanism for latent reasoning.
匹配关键词: autoregressive
---

[ACADEMIC - ARXIV]
标题: VPG: Visual Prefix Guidance for Autoregressive Image and Video Generation
作者: Xinyao Liao, Qiyuan He, Yicong Li, Jiayin Zhu, Xiaoye Qu, Wei Wei, Angela Yao
链接: https://arxiv.org/abs/2605.30317v1
完整摘要: Autoregressive image and video generators are trained with teacher-forced histories but must sample from their own generated prefixes at inference time, making them vulnerable to exposure bias and prefix drift. Existing remedies either modify training or apply sampling-time guidance aimed primarily at external semantic conditions, such as class labels or text prompts, rather than testing whether a next-step prediction provides strong posterior support for the generated prefix itself. We propose Visual Prefix Guidance (VPG), a training-free inference-time guidance method for autoregressive image and video generation. VPG improves next-step prediction by contrasting the model's output under the generated prefix with its output under a corrupted prefix, then extrapolating logits toward candidates that strengthen the posterior support of the generated prefix. Across class-conditional image generation with VAR, text-to-image generation with Infinity, and text-to-video generation with InfinityStar, VPG improves generation quality without retraining the base model, reducing FID on VAR by 0.36 on average and improving benchmark performance on both image and video generation.
匹配关键词: autoregressive
---

[ACADEMIC - ARXIV]
标题: Archon: A Unified Multimodal Model for Holistic Digital Human Generation
作者: Chong Bao, Shichen Liu, Lijun Yu, David Futschik, Stylianos Moschoglou, Shefali Srivastava, Ziqian Bai, Feitong Tan, Guofeng Zhang, Zhaopeng Cui, Sean Fanello, Yinda Zhang
链接: https://arxiv.org/abs/2605.30311v1
完整摘要: Digital humans are fundamental to immersive interaction, yet creating a unified model for holistic modalities, including text, audio, motion, and visual content, remains an open challenge. In this paper, we present Archon, a fully pretrained, human-centric unified multimodal model for holistic avatar generation. Archon unifies seven modalities with modality-specific tokenizers, and a native autoregressive unified multimodal model pretrained on synchronized modalities and 72 diverse tasks to model holistic joint distributions. To address the token explosion challenge in high-fidelity talking videos, we introduce a memory-efficient semantic video reparameterization, achieving 4x token reduction while preserving fine-grained dynamics, coupled with a semantic-driven video diffusion decoder. We further propose a "Thinking in Modality" that decomposes ambiguous cross-modal tasks into stepwise thinking in an alternative chain of modality, progressively enhancing fidelity and controllability. Extensive experiments demonstrate that Archon achieves superior or comparable performance across diverse digital human generation tasks, validating the effectiveness of our unified framework. Project page: https://zju3dv.github.io/archon/.
匹配关键词: autoregressive
---

[ACADEMIC - ARXIV]
标题: VideoMLA: Low-Rank Latent KV Cache for Minute-Scale Autoregressive Video Diffusion
作者: Hidir Yesiltepe, Jiazhen Hu, Tuna Han Salih Meral, Adil Kaan Akan, Kaan Oktay, Hoda Eldardiry, Pinar Yanardag
链接: https://arxiv.org/abs/2605.30351v1
完整摘要: Long-rollout causal video diffusion has converged on a fixed-size sliding-window KV cache, with recent progress innovating within this layout by changing which tokens occupy the window or how their positions are encoded. The per-head KV layout itself, a dominant contributor to streaming memory and latency, has been mostly left unchanged. In this paper, we present the first study of Multi-Head Latent Attention (MLA) in video diffusion. VideoMLA replaces per-head keys and values with a shared low-rank content latent and a shared decoupled 3D-RoPE positional key, reducing per-token KV memory by 92.7% at every cached layer. We further investigate why MLA succeeds in video diffusion even though the spectral assumption often used to motivate it in language models does not hold: pretrained video attention is not low-rank, with 99%-energy effective rank far above any practical latent dimension. VideoMLA retains quality at compression ratios where direct spectral approximation would predict large reconstruction error. We show that the MLA bottleneck, rather than the pretrained spectrum, determines the effective rank: both spectral and random initialization occupy nearly the full rank budget from initialization, and training preserves this budget while adapting within it. On VBench, VideoMLA matches short-horizon streaming video diffusion baselines, achieves the best overall score at long horizons among evaluated methods, and improves throughput by 1.23x on a single B200.
匹配关键词: latent diffusion
---

[ACADEMIC - ARXIV]
标题: LLMSurgeon: Diagnosing Data Mixture of Large Language Models
作者: Yaxin Luo, Jiacheng Cui, Xiaohan Zhao, Xinyi Shang, Jiacheng Liu, Xinyue Bi, Zhaoyi Li, Zhiqiang Shen
链接: https://arxiv.org/abs/2605.30348v1
完整摘要: The pretraining data mixture of Large Language Models (LLMs) constitutes their "digital DNA", shaping model behaviors, capabilities, and failure modes. Yet this composition is rarely disclosed, making post-hoc auditing of data combination or provenance difficult. In this work, we formalize $\textbf{Data Mixture Surgery (DMS)}$: given only generated text from a target LLM, estimate the domain-level distribution of its pretraining corpus under a predefined taxonomy. We propose $\textbf{LLMSurgeon}$, a strong framework that casts DMS as an inverse problem under the label-shift assumption. Rather than directly aggregating classifier outputs, LLMSurgeon estimates a calibrated $\textit{soft}$ confusion matrix and solves a constrained inverse problem to correct systematic domain confusion and recover the latent mixture prior. To evaluate, we introduce $\textbf{LLMScan}$, a recipe-verifiable evaluation suite built from open-source LLMs with transparent pretraining mixtures. Across LLMScan, LLMSurgeon recovers domain mixtures with high fidelity under fixed protocols. Our work presents a practical, post-hoc approach for auditing the digital DNA of foundation models without access to their training data.
匹配关键词: latent diffusion
---

[ACADEMIC - ARXIV]
标题: AdaState: Self-Evolving Anchors for Streaming Video Generation
作者: Yusuf Dalva, Pinar Yanardag
链接: https://arxiv.org/abs/2605.30349v1
完整摘要: Autoregressive video diffusion models generate streaming video by producing frames sequentially, conditioning each chunk on previously generated content. These models are structurally anchored to the first frame: its key-value representation occupies a privileged position in the attention cache and serves as the primary scene reference throughout generation. As the cleanest and most error-free position in the cache, this anchor draws disproportionate attention, suppressing video dynamics, and locking scene composition to the initial viewpoint even as the scene naturally evolves. The result is a temporally shallow video in which motion, camera movement, and scene progression are dampened in favor of static consistency. To address this, we replace the static anchor with an adaptive state, a hidden latent that the model denoises alongside content at every chunk but never renders. Rather than referencing a frozen first frame, the model generates its own scene anchor at each step by attending to both the previous state and the current content, producing a reference that evolves with the generated content. Unlike standard video generation, which encodes an absolute notion of time, our formulation treats time as relative: every generation step sees the same positional structure regardless of how far generation has progressed, and the state transition is identical at every chunk. Together, these properties introduce a recurrence into the generation process, where denoising serves as the transition function, and the KV cache serves as the carrier, requiring no external module. Experiments demonstrate that the adaptive state substantially improves video dynamics, enabling richer motion and natural scene progression within generated videos.
匹配关键词: latent diffusion
---

[ACADEMIC - ARXIV]
标题: NeuROK: Generative 4D Neural Object Kinematics
作者: Chen Geng, Guangzhao He, Yue Gao, Yunzhi Zhang, Shangzhe Wu, Jiajun Wu
链接: https://arxiv.org/abs/2605.30347v1
完整摘要: Data-driven approaches have revolutionized 3D vision, enabling transformers to effectively reconstruct and generate static 3D objects. However, generating simulative 4D dynamics -- realistic temporal deformations of static objects under various physical conditions -- remains challenging and often ad hoc, despite its importance in building comprehensive 3D world models. Most existing methods assume a predefined physical model and use system identification to estimate parameters, restricting these methods to specific categories and small-scale datasets. We propose that these restrictions can be overcome by learning a data-driven kinematic state parameterization for object-centric physical systems. Specifically, we learn both a latent space representing all possible states of the object and a decoder that maps any sampled latent to a plausibly deformed shape of the object. We refer to this parameterization as Neural Object Kinematics (NeuROK), and learn a transformer-based encoder-decoder model on a curated large-scale 4D dataset. This formulation and the learned model significantly simplify the generation of simulative dynamics since we only need to consider the dynamics within a low-dimensional latent space from the Lagrangian mechanics' perspective in classical physics. We demonstrate the effectiveness and generality of this neural simulation framework across diverse dynamic object types, showing clear advantages over prior works. Project page: https://chen-geng.com/neurok
匹配关键词: latent diffusion
---

[ACADEMIC - ARXIV]
标题: YoCausal: How Far is Video Generation from World Model? A Causality Perspective
作者: You-Zhe Xie, Yu-Hsuan Li, Jie-Ying Lee, Kaipeng Zhang, Yu-Lun Liu, Zhixiang Wang
链接: https://arxiv.org/abs/2605.30346v1
完整摘要: As video diffusion models (VDMs) advance toward world models, a key question arises: do they truly understand causality, or merely overfit to statistical temporal patterns? Existing benchmarks mostly rely on synthetic data, limiting real-world generalization due to the sim-to-real gap. We present YoCausal, a two-level benchmark inspired by the Violation of Expectation (VoE) paradigm from cognitive science. By temporally reversing real-world videos at zero cost as natural counterfactual samples, YoCausal establishes an arbitrarily extensible evaluation protocol. Level 1 introduces the Reverse Surprise Index (RSI), quantifying arrow-of-time perception via denoising loss. Level 2 introduces the Causality Cognition Index (CCI), which leverages a VLM to stratify datasets into causal and non-causal subsets, disentangling genuine causal reasoning from temporal bias. Evaluation of 13 state-of-the-art VDMs reveals that perceiving the arrow of time does not imply understanding causality, and a significant gap persists relative to human-level causal cognition.
匹配关键词: latent diffusion
---

[ACADEMIC - ARXIV]
标题: DynaFLIP: Rethinking Robotics Perception via Tri-Modal-Dynamics Guided Representation
作者: Jusuk Lee, Seungjae Lee, Jonghun Shin, Hoseong Jung, Sungha Kim, Daesol Cho, H. Jin Kim, Jia-Bin Huang, Furong Huang
链接: https://arxiv.org/abs/2605.30350v1
完整摘要: Robot manipulation critically depends on perception that preserves the action-relevant aspects of a scene. Yet most robot learning pipelines are built upon visual encoders pre-trained for static recognition or vision-language alignment, leaving motion understanding to downstream policies. We introduce DynaFLIP, a dynamics-aware multimodal pre-training framework that pushes motion understanding upstream into perception. We construct image-language-3D flow triplets from heterogeneous human and robot videos, and use these triplets as training-time supervision to shape an image-only encoder. Our key idea is to encourage the three modalities to span a small simplex volume in the shared hyperspherical space -- a smaller simplex volume indicating stronger alignment. To avoid the geometric ambiguity and trivial collapse of naive volume minimization, we combine simplex-volume minimization with a cosine regularizer and a contrastive objective. Our analyses show that DynaFLIP focuses on control-relevant regions critical for manipulation. The resulting dynamics-aware representations serve as reusable visual backbones and consistently outperform baselines across diverse downstream policies, including VLAs. We validate this across diverse simulation and real-world setups, with gains reaching +22.5% under out-of-distribution scenarios. Our results suggest that robot generalization improves when visual representations are trained to encode not just what is present, but how the world changes under action.
匹配关键词: multimodal
---

[ACADEMIC - ARXIV]
标题: Tiny but Trusted: Efficient Vision-Language Reasoning for Time-Series Anomaly Detection
作者: Xiaona Zhou, Muntasir Wahed, Tianjiao Yu, Constantin Brif, Ismini Lourentzou
链接: https://arxiv.org/abs/2605.30344v1
完整摘要: Recent advances in Vision-Language Models (VLMs) have achieved impressive performance across many tasks, yet prior studies report unsatisfactory performance when applying large language or multimodal models to finding abnormal patterns in sequential data. Public anomaly detection benchmarks typically provide interval annotations but not natural-language rationales, making it difficult to fine-tune VLMs to produce grounded, interpretable decisions. To address this gap, we construct VisAnomBench, a curated benchmark built from public time-series datasets and augmented with high-quality anomaly explanations selected from multiple large VLMs using fine-grained, task-specific rewards. Through fine-tuning on this benchmark, we develop VisAnomReasoner, a parameter-efficient VLM for time-series anomaly detection. Experimental results on VisAnomBench show that VisAnomReasoner achieves more accurate anomaly localization and consistently outperforms all baselines, with improvements of at least 21.23 and 23.87 percentage points in precision and F1, respectively. Additional experiments on the TSB-AD-U benchmark demonstrate strong cross-benchmark generalization, with VisAnomReasoner improving precision and F1 by 9.57 and 13.39 percentage points, respectively.
匹配关键词: multimodal
---

[ACADEMIC - ARXIV]
标题: When, why, and how do diffusion posterior samplers fail? A finite-sample lens
作者: Benjamin A. Burns, Sara Fridovich-Keil
链接: https://arxiv.org/abs/2605.30330v1
完整摘要: Diffusion models have excellent capacity to model complex distributions of natural data, which has made them a popular and effective choice for posterior sampling in imaging inverse problems. Existing methods can incorporate any measurement model at inference time but must use an inexact approximation for the likelihood at intermediate timesteps for computational tractability. Although these approximations can often work well empirically, their downstream effect on the sampled posterior is poorly understood and can result in unexplained failures. To understand when, why, and how these likelihood approximations propagate to erroneous posterior distributions, we introduce a finite-sample perspective on posterior sampling that approximates the posterior to arbitrary precision as training set size tends towards infinity, for any forward model and prior distribution. Using this finite-sample lens, we observe that popular posterior sampling approximations tend to under- or over-estimate the spread of the posterior at intermediate timesteps, causing downstream consequences including sensitivity to early stopping time, inaccurate relative weighting of posterior modes, and hallucination, both of prior modes that are not in the posterior and likelihood modes that are not supported by the prior. Moreover, we find that the cause of these posterior errors requires neither a nonlinear measurement model nor a multimodal posterior, but can arise solely due to a multimodal prior and inaccurate posterior spread at intermediate sampling times. Our finite-sample posterior sampling approach is agnostic to the type of likelihood approximation and the type of (linear or nonlinear) forward model, and can thus serve as a drop-in diagnostic to evaluate the accuracy and failure modes of existing and future posterior samplers.
匹配关键词: multimodal
---

[ACADEMIC - ARXIV]
标题: Supercharging Thermal Gaussian Splatting with Depth Estimation
作者: Manoj Biswanath, Chenxin Cai, Hannah Schieber, Daniel Roth, Benjamin Busam
链接: https://arxiv.org/abs/2605.30328v1
完整摘要: Efficient and robust 3D scene representation is crucial in autonomous driving, robotics, and related fields. While RGB images provide valuable content for 3D reconstruction, other modalities like thermal or depth can enable additional information on the environment. Lately, novel view synthesis methods like 3D Gaussian Splatting have started using multiple modalities to further boost their performance. But fusing or combining multimodal data can make the process slower and can bring in additional challenges. Therefore, our project aims to use single modality based on thermal infrared domain, by removing the reliance on visible light as much as possible. This single modality can be expected to be faster as it does not rely on multimodal data. We propose a method, Thermal-to-Depth Gaussian Splatting (TDg), that uses only thermal images and depth estimation in its architecture to derive the radiance fields. Our TDg method outperforms the MSMG (Multiple Single-Modal Gaussians) baseline in most cases on our test datasets, RGBT-Scenes and ThermalMix. On average, the rendering quality metrics such as learned perceptual image patch similarity (LPIPS), structural similarity index measure (SSIM), and peak signal-to-noise ratio (PSNR) of TDg are 1.12%, 0.034%, and 0.01% better than the baseline MSMG values. It also reduces the training time significantly, by 12 mins 47 secs (55% improvement). Overall, our method is successful in deriving these thermal radiance fields, which can ultimately have several applications, such as identifying heat sources critical in surveillance, search or rescue operations, and industrial inspections where temperature is widely used to monitor machines.
匹配关键词: multimodal
---

[ACADEMIC - ARXIV]
标题: Archon: A Unified Multimodal Model for Holistic Digital Human Generation
作者: Chong Bao, Shichen Liu, Lijun Yu, David Futschik, Stylianos Moschoglou, Shefali Srivastava, Ziqian Bai, Feitong Tan, Guofeng Zhang, Zhaopeng Cui, Sean Fanello, Yinda Zhang
链接: https://arxiv.org/abs/2605.30311v1
完整摘要: Digital humans are fundamental to immersive interaction, yet creating a unified model for holistic modalities, including text, audio, motion, and visual content, remains an open challenge. In this paper, we present Archon, a fully pretrained, human-centric unified multimodal model for holistic avatar generation. Archon unifies seven modalities with modality-specific tokenizers, and a native autoregressive unified multimodal model pretrained on synchronized modalities and 72 diverse tasks to model holistic joint distributions. To address the token explosion challenge in high-fidelity talking videos, we introduce a memory-efficient semantic video reparameterization, achieving 4x token reduction while preserving fine-grained dynamics, coupled with a semantic-driven video diffusion decoder. We further propose a "Thinking in Modality" that decomposes ambiguous cross-modal tasks into stepwise thinking in an alternative chain of modality, progressively enhancing fidelity and controllability. Extensive experiments demonstrate that Archon achieves superior or comparable performance across diverse digital human generation tasks, validating the effectiveness of our unified framework. Project page: https://zju3dv.github.io/archon/.
匹配关键词: multimodal
---

[ACADEMIC - ARXIV]
标题: Physics Is All You Need? A Case Study in Physicist-Supervised AI Development of Scientific Software
作者: Nhat-Minh Nguyen
链接: https://arxiv.org/abs/2605.30353v1
完整摘要: Are AI agents tools, co-authors, or researchers? We present a quantified case study ($N=1$): a physicist supervising an AI coding agent (Claude Code, Sonnet and Opus models) over 12 work days and 57 sessions to build CLAX-PT, a differentiable one-loop perturbation theory module in JAX. We documented and classified 15 supervision events by intervention level. The agent resolved ten autonomously by iterating against oracle tests. Two more by the physicist's domain knowledge. The three it could not -- all evaded oracle detection -- share a common property: the agent treated symptom reduction as root-cause resolution. It spent 33 of the 57 sessions adjusting coefficients within a code architecture that could not represent the target physics, and could not re-evaluate its CLASS-PT branch choice even when prompted to reconsider; only an injected physics concept (anisotropic BAO damping) triggered the redesign. Separately, the agent committed a calibrated correction that passed all oracle tests but corresponded to no quantity in the theory, predicting wrong values at any other cosmology. The fudge factor was caught and replaced within the same session. Three supervision practices proved critical for catching what oracle tests missed: testing at diverse parameter points beyond the fiducial calibration; shared changelogs that surfaced stalled exploration across sessions; and an explicit rule against unphysical numerical patches. In this case, supervision design, not model capability, determined whether the agent's output was trustworthy. Closing the gap would require agents that propose architectural alternatives rather than optimize within a given structure, and distinguish predictive adequacy from explanatory correctness -- capabilities not exhibited here, not obviously addressed by scaling alone. [Abridged.]
匹配关键词: vision language model
---

[ACADEMIC - ARXIV]
标题: GMOS: Grounding Moving Object Segmentation in 3D Space and Time
作者: Junyu Xie, Tengda Han, Weidi Xie, Andrew Zisserman
链接: https://arxiv.org/abs/2605.30352v1
完整摘要: Moving Object Segmentation (MOS) aims to discover, segment, and track objects that move independently of the camera. Current MOS methods, however, exhibit two fundamental limitations: they rely on pre-computed 2D auxiliary modalities such as optical flow or point trajectories that lack 3D geometric information, and they treat motion as a sequence-level attribute, overlooking the instantaneous motion state of each object. We address both by grounding MOS in 3D space and time, and propose GMOS, a framework that operates directly on RGB video to produce 3D-aware, temporally fine-grained segmentation of multiple moving objects, alongside a foreground--background variant GMOS-S for faster deployment. To support training and evaluation in this regime, we curate GMOS-2K, a dataset of 2,210 real-world videos with per-object temporal motion annotations drawn from five established Video Object Segmentation (VOS) benchmarks, and formalise MOS-I ("I" for instantaneous), a temporally fine-grained evaluation protocol with three complementary metrics. GMOS achieves state-of-the-art results across MOS, MOS-I, and Unsupervised VOS benchmarks, while running significantly faster than prior multi-object MOS methods and supporting online inference for streaming deployment.
匹配关键词: vision language model
---

[ACADEMIC - ARXIV]
标题: VideoMLA: Low-Rank Latent KV Cache for Minute-Scale Autoregressive Video Diffusion
作者: Hidir Yesiltepe, Jiazhen Hu, Tuna Han Salih Meral, Adil Kaan Akan, Kaan Oktay, Hoda Eldardiry, Pinar Yanardag
链接: https://arxiv.org/abs/2605.30351v1
完整摘要: Long-rollout causal video diffusion has converged on a fixed-size sliding-window KV cache, with recent progress innovating within this layout by changing which tokens occupy the window or how their positions are encoded. The per-head KV layout itself, a dominant contributor to streaming memory and latency, has been mostly left unchanged. In this paper, we present the first study of Multi-Head Latent Attention (MLA) in video diffusion. VideoMLA replaces per-head keys and values with a shared low-rank content latent and a shared decoupled 3D-RoPE positional key, reducing per-token KV memory by 92.7% at every cached layer. We further investigate why MLA succeeds in video diffusion even though the spectral assumption often used to motivate it in language models does not hold: pretrained video attention is not low-rank, with 99%-energy effective rank far above any practical latent dimension. VideoMLA retains quality at compression ratios where direct spectral approximation would predict large reconstruction error. We show that the MLA bottleneck, rather than the pretrained spectrum, determines the effective rank: both spectral and random initialization occupy nearly the full rank budget from initialization, and training preserves this budget while adapting within it. On VBench, VideoMLA matches short-horizon streaming video diffusion baselines, achieves the best overall score at long horizons among evaluated methods, and improves throughput by 1.23x on a single B200.
匹配关键词: vision language model
---

[ACADEMIC - ARXIV]
标题: DynaFLIP: Rethinking Robotics Perception via Tri-Modal-Dynamics Guided Representation
作者: Jusuk Lee, Seungjae Lee, Jonghun Shin, Hoseong Jung, Sungha Kim, Daesol Cho, H. Jin Kim, Jia-Bin Huang, Furong Huang
链接: https://arxiv.org/abs/2605.30350v1
完整摘要: Robot manipulation critically depends on perception that preserves the action-relevant aspects of a scene. Yet most robot learning pipelines are built upon visual encoders pre-trained for static recognition or vision-language alignment, leaving motion understanding to downstream policies. We introduce DynaFLIP, a dynamics-aware multimodal pre-training framework that pushes motion understanding upstream into perception. We construct image-language-3D flow triplets from heterogeneous human and robot videos, and use these triplets as training-time supervision to shape an image-only encoder. Our key idea is to encourage the three modalities to span a small simplex volume in the shared hyperspherical space -- a smaller simplex volume indicating stronger alignment. To avoid the geometric ambiguity and trivial collapse of naive volume minimization, we combine simplex-volume minimization with a cosine regularizer and a contrastive objective. Our analyses show that DynaFLIP focuses on control-relevant regions critical for manipulation. The resulting dynamics-aware representations serve as reusable visual backbones and consistently outperform baselines across diverse downstream policies, including VLAs. We validate this across diverse simulation and real-world setups, with gains reaching +22.5% under out-of-distribution scenarios. Our results suggest that robot generalization improves when visual representations are trained to encode not just what is present, but how the world changes under action.
匹配关键词: vision language model
---

[ACADEMIC - ARXIV]
标题: LLMSurgeon: Diagnosing Data Mixture of Large Language Models
作者: Yaxin Luo, Jiacheng Cui, Xiaohan Zhao, Xinyi Shang, Jiacheng Liu, Xinyue Bi, Zhaoyi Li, Zhiqiang Shen
链接: https://arxiv.org/abs/2605.30348v1
完整摘要: The pretraining data mixture of Large Language Models (LLMs) constitutes their "digital DNA", shaping model behaviors, capabilities, and failure modes. Yet this composition is rarely disclosed, making post-hoc auditing of data combination or provenance difficult. In this work, we formalize $\textbf{Data Mixture Surgery (DMS)}$: given only generated text from a target LLM, estimate the domain-level distribution of its pretraining corpus under a predefined taxonomy. We propose $\textbf{LLMSurgeon}$, a strong framework that casts DMS as an inverse problem under the label-shift assumption. Rather than directly aggregating classifier outputs, LLMSurgeon estimates a calibrated $\textit{soft}$ confusion matrix and solves a constrained inverse problem to correct systematic domain confusion and recover the latent mixture prior. To evaluate, we introduce $\textbf{LLMScan}$, a recipe-verifiable evaluation suite built from open-source LLMs with transparent pretraining mixtures. Across LLMScan, LLMSurgeon recovers domain mixtures with high fidelity under fixed protocols. Our work presents a practical, post-hoc approach for auditing the digital DNA of foundation models without access to their training data.
匹配关键词: vision language model
---

[ACADEMIC - ARXIV]
标题: YoCausal: How Far is Video Generation from World Model? A Causality Perspective
作者: You-Zhe Xie, Yu-Hsuan Li, Jie-Ying Lee, Kaipeng Zhang, Yu-Lun Liu, Zhixiang Wang
链接: https://arxiv.org/abs/2605.30346v1
完整摘要: As video diffusion models (VDMs) advance toward world models, a key question arises: do they truly understand causality, or merely overfit to statistical temporal patterns? Existing benchmarks mostly rely on synthetic data, limiting real-world generalization due to the sim-to-real gap. We present YoCausal, a two-level benchmark inspired by the Violation of Expectation (VoE) paradigm from cognitive science. By temporally reversing real-world videos at zero cost as natural counterfactual samples, YoCausal establishes an arbitrarily extensible evaluation protocol. Level 1 introduces the Reverse Surprise Index (RSI), quantifying arrow-of-time perception via denoising loss. Level 2 introduces the Causality Cognition Index (CCI), which leverages a VLM to stratify datasets into causal and non-causal subsets, disentangling genuine causal reasoning from temporal bias. Evaluation of 13 state-of-the-art VDMs reveals that perceiving the arrow of time does not imply understanding causality, and a significant gap persists relative to human-level causal cognition.
匹配关键词: VLM
---

[ACADEMIC - ARXIV]
标题: Tiny but Trusted: Efficient Vision-Language Reasoning for Time-Series Anomaly Detection
作者: Xiaona Zhou, Muntasir Wahed, Tianjiao Yu, Constantin Brif, Ismini Lourentzou
链接: https://arxiv.org/abs/2605.30344v1
完整摘要: Recent advances in Vision-Language Models (VLMs) have achieved impressive performance across many tasks, yet prior studies report unsatisfactory performance when applying large language or multimodal models to finding abnormal patterns in sequential data. Public anomaly detection benchmarks typically provide interval annotations but not natural-language rationales, making it difficult to fine-tune VLMs to produce grounded, interpretable decisions. To address this gap, we construct VisAnomBench, a curated benchmark built from public time-series datasets and augmented with high-quality anomaly explanations selected from multiple large VLMs using fine-grained, task-specific rewards. Through fine-tuning on this benchmark, we develop VisAnomReasoner, a parameter-efficient VLM for time-series anomaly detection. Experimental results on VisAnomBench show that VisAnomReasoner achieves more accurate anomaly localization and consistently outperforms all baselines, with improvements of at least 21.23 and 23.87 percentage points in precision and F1, respectively. Additional experiments on the TSB-AD-U benchmark demonstrate strong cross-benchmark generalization, with VisAnomReasoner improving precision and F1 by 9.57 and 13.39 percentage points, respectively.
匹配关键词: VLM
---

[ACADEMIC - ARXIV]
标题: Grounded 3D-Aware Spatial Vision-Language Modeling
作者: An-Chieh Cheng, Yang Fu, Yatai Ji, Ligeng Zhu, Guanqi Zhan, Zhuoyang Zhang, Zhaojing Yang, Song Han, Yao Lu, Pavlo Molchanov, Vidya Nariyambut Murali, Jan Kautz, Xiaolong Wang, Hongxu Yin, Sifei Liu
链接: https://arxiv.org/abs/2605.30307v1
完整摘要: We present GR3D, a spatial vision language model equipped with three complementary grounding capabilities--explicit 2D grounding, implicit 2D grounding, and monocular 3D grounding--within a single framework. GR3D introduces an implicit grounding mechanism that identifies entity mentions during generation and inserts the corresponding region tokens into the text stream, allowing the model to reference visual evidence on the fly when producing spatial chain-of-thought responses. In parallel, a region-prompted monocular 3D grounding design predicts 3D bounding boxes in the camera view from grounded region queries, supported by intrinsic-aware normalization and dense geometric supervision. Together, these grounding capabilities enable GR3D to decompose complex spatial understanding problems into grounded 2D perception followed by 3D inference. GR3D achieves consistent improvements across grounded and non-grounded spatial benchmarks, demonstrating grounding as an effective inductive bias for strengthening spatial understanding in VLMs. These grounding capabilities collectively enhance general spatial understanding beyond the grounding task itself.
匹配关键词: VLM
---

[ACADEMIC - ARXIV]
标题: LoMo: Local Modality Substitution for Deeper Vision-Language Fusion
作者: Feng Han, Zhixiong Zhang, Zheming Liang, Yibin Wang, Jiaqi Wang
链接: https://arxiv.org/abs/2605.30265v1
完整摘要: Vision-Language Models (VLMs) have achieved substantial progress across a wide range of understanding and reasoning tasks, driven by large-scale image-text training aimed at multimodal fusion. Ideally, replacing a textual question with its rendered-image counterpart should leave model performance essentially unaffected. In practice, however, such modality substitution induces dramatic performance degradation. We attribute this "carrier sensitivity" issue to an inherent bias in current training corpora. Across prevalent datasets such as image captioning, VQA, OCR, and web-sourced interleaved data, text and images are typically organized into distinct and asymmetric roles, with text serving as linguistic queries and images as visual references. Such data bias leads VLMs to exhibit distinct preferences for information acquisition across different modalities. Consequently, VLMs fail to align representations of semantically equivalent content across textual and visual carriers, making model reasoning fragile under modality substitution. To address this, we propose Local Modality Substitution (LoMo), a lightweight, architecture-agnostic data curation paradigm designed to provide supervision for cross-modal representational invariance between semantically equivalent text and image carriers. LoMo achieves this by reformulating single-modality prompts into seamlessly interleaved multimodal sequences. It dynamically selects target text spans and recasts them as rendered images, thereby preserving the same semantics across "text, visual, text" carriers. Extensive experiments across 13 diverse multimodal benchmarks demonstrate that LoMo significantly improves overall multimodal reasoning and yields deeper cross-modal fusion. Specifically, it delivers consistent gains across foundational models, improving over standard SFT by 2.67 points on LLaVA-OneVision-1.5-8B and 2.82 points on Qwen3.5-9B.
匹配关键词: VLM
---

[ACADEMIC - ARXIV]
标题: Stable-Layers: Fine-Tuning Image Layer Decomposition Models with VLM-Scored Reinforcement Learning
作者: Ciara Rowles, Reshinth Adithyan, Nikhil Pinnaparaju, Vikram Voleti, Mark Boss
链接: https://arxiv.org/abs/2605.30257v1
完整摘要: We present Stable-Layers, a reinforcement learning framework that eliminates the need for paired supervision by fine-tuning a pretrained layer decomposition model using only feedback from a vision-language model (VLM). Starting from Qwen-Image-Layered, we apply Flow-GRPO with LoRA adaptation, sampling multiple candidate decompositions per image, scoring them with a VLM, and optimising the policy from group-relative advantages. The key challenge lies in designing a reliable reward signal: VLMs scoring samples in isolation tend to compress their judgements into a narrow band, leaving GRPO with little within-group variance to learn from. We address this with a two-stage evaluation pipeline that pairs structured per-sample scoring across five edit-centric criteria with a grid-based calibration step in which the VLM re-scores all candidates side-by-side. Stable-Layers produces decompositions with stronger layer separation, fewer blank or artifact-heavy layers, and lower per-layer reconstruction error on the Crello dataset compared to the base model.
匹配关键词: VLM
---

[ACADEMIC - ARXIV]
标题: DynaFLIP: Rethinking Robotics Perception via Tri-Modal-Dynamics Guided Representation
作者: Jusuk Lee, Seungjae Lee, Jonghun Shin, Hoseong Jung, Sungha Kim, Daesol Cho, H. Jin Kim, Jia-Bin Huang, Furong Huang
链接: https://arxiv.org/abs/2605.30350v1
完整摘要: Robot manipulation critically depends on perception that preserves the action-relevant aspects of a scene. Yet most robot learning pipelines are built upon visual encoders pre-trained for static recognition or vision-language alignment, leaving motion understanding to downstream policies. We introduce DynaFLIP, a dynamics-aware multimodal pre-training framework that pushes motion understanding upstream into perception. We construct image-language-3D flow triplets from heterogeneous human and robot videos, and use these triplets as training-time supervision to shape an image-only encoder. Our key idea is to encourage the three modalities to span a small simplex volume in the shared hyperspherical space -- a smaller simplex volume indicating stronger alignment. To avoid the geometric ambiguity and trivial collapse of naive volume minimization, we combine simplex-volume minimization with a cosine regularizer and a contrastive objective. Our analyses show that DynaFLIP focuses on control-relevant regions critical for manipulation. The resulting dynamics-aware representations serve as reusable visual backbones and consistently outperform baselines across diverse downstream policies, including VLAs. We validate this across diverse simulation and real-world setups, with gains reaching +22.5% under out-of-distribution scenarios. Our results suggest that robot generalization improves when visual representations are trained to encode not just what is present, but how the world changes under action.
匹配关键词: image generation
---

[ACADEMIC - ARXIV]
标题: LLMSurgeon: Diagnosing Data Mixture of Large Language Models
作者: Yaxin Luo, Jiacheng Cui, Xiaohan Zhao, Xinyi Shang, Jiacheng Liu, Xinyue Bi, Zhaoyi Li, Zhiqiang Shen
链接: https://arxiv.org/abs/2605.30348v1
完整摘要: The pretraining data mixture of Large Language Models (LLMs) constitutes their "digital DNA", shaping model behaviors, capabilities, and failure modes. Yet this composition is rarely disclosed, making post-hoc auditing of data combination or provenance difficult. In this work, we formalize $\textbf{Data Mixture Surgery (DMS)}$: given only generated text from a target LLM, estimate the domain-level distribution of its pretraining corpus under a predefined taxonomy. We propose $\textbf{LLMSurgeon}$, a strong framework that casts DMS as an inverse problem under the label-shift assumption. Rather than directly aggregating classifier outputs, LLMSurgeon estimates a calibrated $\textit{soft}$ confusion matrix and solves a constrained inverse problem to correct systematic domain confusion and recover the latent mixture prior. To evaluate, we introduce $\textbf{LLMScan}$, a recipe-verifiable evaluation suite built from open-source LLMs with transparent pretraining mixtures. Across LLMScan, LLMSurgeon recovers domain mixtures with high fidelity under fixed protocols. Our work presents a practical, post-hoc approach for auditing the digital DNA of foundation models without access to their training data.
匹配关键词: image generation
---

[ACADEMIC - ARXIV]
标题: AdaState: Self-Evolving Anchors for Streaming Video Generation
作者: Yusuf Dalva, Pinar Yanardag
链接: https://arxiv.org/abs/2605.30349v1
完整摘要: Autoregressive video diffusion models generate streaming video by producing frames sequentially, conditioning each chunk on previously generated content. These models are structurally anchored to the first frame: its key-value representation occupies a privileged position in the attention cache and serves as the primary scene reference throughout generation. As the cleanest and most error-free position in the cache, this anchor draws disproportionate attention, suppressing video dynamics, and locking scene composition to the initial viewpoint even as the scene naturally evolves. The result is a temporally shallow video in which motion, camera movement, and scene progression are dampened in favor of static consistency. To address this, we replace the static anchor with an adaptive state, a hidden latent that the model denoises alongside content at every chunk but never renders. Rather than referencing a frozen first frame, the model generates its own scene anchor at each step by attending to both the previous state and the current content, producing a reference that evolves with the generated content. Unlike standard video generation, which encodes an absolute notion of time, our formulation treats time as relative: every generation step sees the same positional structure regardless of how far generation has progressed, and the state transition is identical at every chunk. Together, these properties introduce a recurrence into the generation process, where denoising serves as the transition function, and the KV cache serves as the carrier, requiring no external module. Experiments demonstrate that the adaptive state substantially improves video dynamics, enabling richer motion and natural scene progression within generated videos.
匹配关键词: image generation
---

[ACADEMIC - ARXIV]
标题: NeuROK: Generative 4D Neural Object Kinematics
作者: Chen Geng, Guangzhao He, Yue Gao, Yunzhi Zhang, Shangzhe Wu, Jiajun Wu
链接: https://arxiv.org/abs/2605.30347v1
完整摘要: Data-driven approaches have revolutionized 3D vision, enabling transformers to effectively reconstruct and generate static 3D objects. However, generating simulative 4D dynamics -- realistic temporal deformations of static objects under various physical conditions -- remains challenging and often ad hoc, despite its importance in building comprehensive 3D world models. Most existing methods assume a predefined physical model and use system identification to estimate parameters, restricting these methods to specific categories and small-scale datasets. We propose that these restrictions can be overcome by learning a data-driven kinematic state parameterization for object-centric physical systems. Specifically, we learn both a latent space representing all possible states of the object and a decoder that maps any sampled latent to a plausibly deformed shape of the object. We refer to this parameterization as Neural Object Kinematics (NeuROK), and learn a transformer-based encoder-decoder model on a curated large-scale 4D dataset. This formulation and the learned model significantly simplify the generation of simulative dynamics since we only need to consider the dynamics within a low-dimensional latent space from the Lagrangian mechanics' perspective in classical physics. We demonstrate the effectiveness and generality of this neural simulation framework across diverse dynamic object types, showing clear advantages over prior works. Project page: https://chen-geng.com/neurok
匹配关键词: image generation
---

[ACADEMIC - ARXIV]
标题: YoCausal: How Far is Video Generation from World Model? A Causality Perspective
作者: You-Zhe Xie, Yu-Hsuan Li, Jie-Ying Lee, Kaipeng Zhang, Yu-Lun Liu, Zhixiang Wang
链接: https://arxiv.org/abs/2605.30346v1
完整摘要: As video diffusion models (VDMs) advance toward world models, a key question arises: do they truly understand causality, or merely overfit to statistical temporal patterns? Existing benchmarks mostly rely on synthetic data, limiting real-world generalization due to the sim-to-real gap. We present YoCausal, a two-level benchmark inspired by the Violation of Expectation (VoE) paradigm from cognitive science. By temporally reversing real-world videos at zero cost as natural counterfactual samples, YoCausal establishes an arbitrarily extensible evaluation protocol. Level 1 introduces the Reverse Surprise Index (RSI), quantifying arrow-of-time perception via denoising loss. Level 2 introduces the Causality Cognition Index (CCI), which leverages a VLM to stratify datasets into causal and non-causal subsets, disentangling genuine causal reasoning from temporal bias. Evaluation of 13 state-of-the-art VDMs reveals that perceiving the arrow of time does not imply understanding causality, and a significant gap persists relative to human-level causal cognition.
匹配关键词: image generation
---

[ACADEMIC - ARXIV]
标题: DynaFLIP: Rethinking Robotics Perception via Tri-Modal-Dynamics Guided Representation
作者: Jusuk Lee, Seungjae Lee, Jonghun Shin, Hoseong Jung, Sungha Kim, Daesol Cho, H. Jin Kim, Jia-Bin Huang, Furong Huang
链接: https://arxiv.org/abs/2605.30350v1
完整摘要: Robot manipulation critically depends on perception that preserves the action-relevant aspects of a scene. Yet most robot learning pipelines are built upon visual encoders pre-trained for static recognition or vision-language alignment, leaving motion understanding to downstream policies. We introduce DynaFLIP, a dynamics-aware multimodal pre-training framework that pushes motion understanding upstream into perception. We construct image-language-3D flow triplets from heterogeneous human and robot videos, and use these triplets as training-time supervision to shape an image-only encoder. Our key idea is to encourage the three modalities to span a small simplex volume in the shared hyperspherical space -- a smaller simplex volume indicating stronger alignment. To avoid the geometric ambiguity and trivial collapse of naive volume minimization, we combine simplex-volume minimization with a cosine regularizer and a contrastive objective. Our analyses show that DynaFLIP focuses on control-relevant regions critical for manipulation. The resulting dynamics-aware representations serve as reusable visual backbones and consistently outperform baselines across diverse downstream policies, including VLAs. We validate this across diverse simulation and real-world setups, with gains reaching +22.5% under out-of-distribution scenarios. Our results suggest that robot generalization improves when visual representations are trained to encode not just what is present, but how the world changes under action.
匹配关键词: visual reasoning
---

[ACADEMIC - ARXIV]
标题: YoCausal: How Far is Video Generation from World Model? A Causality Perspective
作者: You-Zhe Xie, Yu-Hsuan Li, Jie-Ying Lee, Kaipeng Zhang, Yu-Lun Liu, Zhixiang Wang
链接: https://arxiv.org/abs/2605.30346v1
完整摘要: As video diffusion models (VDMs) advance toward world models, a key question arises: do they truly understand causality, or merely overfit to statistical temporal patterns? Existing benchmarks mostly rely on synthetic data, limiting real-world generalization due to the sim-to-real gap. We present YoCausal, a two-level benchmark inspired by the Violation of Expectation (VoE) paradigm from cognitive science. By temporally reversing real-world videos at zero cost as natural counterfactual samples, YoCausal establishes an arbitrarily extensible evaluation protocol. Level 1 introduces the Reverse Surprise Index (RSI), quantifying arrow-of-time perception via denoising loss. Level 2 introduces the Causality Cognition Index (CCI), which leverages a VLM to stratify datasets into causal and non-causal subsets, disentangling genuine causal reasoning from temporal bias. Evaluation of 13 state-of-the-art VDMs reveals that perceiving the arrow of time does not imply understanding causality, and a significant gap persists relative to human-level causal cognition.
匹配关键词: visual reasoning
---

[ACADEMIC - ARXIV]
标题: Tiny but Trusted: Efficient Vision-Language Reasoning for Time-Series Anomaly Detection
作者: Xiaona Zhou, Muntasir Wahed, Tianjiao Yu, Constantin Brif, Ismini Lourentzou
链接: https://arxiv.org/abs/2605.30344v1
完整摘要: Recent advances in Vision-Language Models (VLMs) have achieved impressive performance across many tasks, yet prior studies report unsatisfactory performance when applying large language or multimodal models to finding abnormal patterns in sequential data. Public anomaly detection benchmarks typically provide interval annotations but not natural-language rationales, making it difficult to fine-tune VLMs to produce grounded, interpretable decisions. To address this gap, we construct VisAnomBench, a curated benchmark built from public time-series datasets and augmented with high-quality anomaly explanations selected from multiple large VLMs using fine-grained, task-specific rewards. Through fine-tuning on this benchmark, we develop VisAnomReasoner, a parameter-efficient VLM for time-series anomaly detection. Experimental results on VisAnomBench show that VisAnomReasoner achieves more accurate anomaly localization and consistently outperforms all baselines, with improvements of at least 21.23 and 23.87 percentage points in precision and F1, respectively. Additional experiments on the TSB-AD-U benchmark demonstrate strong cross-benchmark generalization, with VisAnomReasoner improving precision and F1 by 9.57 and 13.39 percentage points, respectively.
匹配关键词: visual reasoning
---

[ACADEMIC - ARXIV]
标题: Unlocking the Working Memory of Large Language Models for Latent Reasoning
作者: Lukas Aichberger, Sepp Hochreiter
链接: https://arxiv.org/abs/2605.30343v1
完整摘要: To improve the reasoning capabilities of large language models, test-time compute is typically scaled by generating intermediate tokens before the final answer. However, this couples reasoning to autoregressive generation and thereby conflates internal computation with external communication. In contrast, human cognition can use working memory to hold and manipulate information internally without the need to externalize intermediate thoughts. Drawing on this principle, we introduce Reasoning in Memory (RiM), a latent reasoning method that replaces the autoregressive generation of reasoning steps with memory blocks. These memory blocks are fixed sequences of special tokens that unlock the working-memory capacity of large language models. Since they are fixed rather than generated, they can be processed in a single forward pass, enabling compute-efficient latent reasoning. To operationalize these memory blocks, we employ a two-stage curriculum. First, we ground them by predicting explicit reasoning steps after each memory block. Second, we discard this step-level supervision and iteratively refine the final answer after each memory block. Our experiments on reasoning benchmarks show that, across language models of different families and sizes, RiM matches or exceeds existing latent reasoning methods while avoiding the autoregressive generation of thoughts. These results demonstrate that large language models can be trained to use working memory as an effective mechanism for latent reasoning.
匹配关键词: visual reasoning
---

[ACADEMIC - ARXIV]
标题: GPIC: A Giant Permissive Image Corpus for Visual Generation
作者: Keshigeyan Chandrasegaran, Kyle Sargent, Suchir Agarwal, Michael Jang, Michael Poli, Juan Carlos Niebles, Justin Johnson, Jiajun Wu, Li Fei-Fei
链接: https://arxiv.org/abs/2605.30341v1
完整摘要: Studying scalable methods for visual generative modeling requires large, accessible, and stable datasets. We introduce GPIC, a Giant Permissive Image Corpus of approximately 28 trillion pixels. GPIC comprises diverse internet images captioned by a state-of-the-art vision-language model, including 100M training, 200K validation, and 1M test examples. Moreover, all GPIC images are permissively licensed for both research and commercial use. GPIC is safety-filtered, deduplicated, and centrally hosted on Hugging Face. We provide a benchmarking protocol for generative modeling on GPIC. Finally, we provide a reference baseline for pixel-space flow matching on GPIC. Our dataset, benchmark, and models are available at https://huggingface.co/datasets/stanford-vision-lab/gpic. Evaluation toolkit and code are available at https://gpic.stanford.edu
匹配关键词: visual reasoning
---

[ACADEMIC - ARXIV]
标题: Physics Is All You Need? A Case Study in Physicist-Supervised AI Development of Scientific Software
作者: Nhat-Minh Nguyen
链接: https://arxiv.org/abs/2605.30353v1
完整摘要: Are AI agents tools, co-authors, or researchers? We present a quantified case study ($N=1$): a physicist supervising an AI coding agent (Claude Code, Sonnet and Opus models) over 12 work days and 57 sessions to build CLAX-PT, a differentiable one-loop perturbation theory module in JAX. We documented and classified 15 supervision events by intervention level. The agent resolved ten autonomously by iterating against oracle tests. Two more by the physicist's domain knowledge. The three it could not -- all evaded oracle detection -- share a common property: the agent treated symptom reduction as root-cause resolution. It spent 33 of the 57 sessions adjusting coefficients within a code architecture that could not represent the target physics, and could not re-evaluate its CLASS-PT branch choice even when prompted to reconsider; only an injected physics concept (anisotropic BAO damping) triggered the redesign. Separately, the agent committed a calibrated correction that passed all oracle tests but corresponded to no quantity in the theory, predicting wrong values at any other cosmology. The fudge factor was caught and replaced within the same session. Three supervision practices proved critical for catching what oracle tests missed: testing at diverse parameter points beyond the fiducial calibration; shared changelogs that surfaced stalled exploration across sessions; and an explicit rule against unphysical numerical patches. In this case, supervision design, not model capability, determined whether the agent's output was trustworthy. Closing the gap would require agents that propose architectural alternatives rather than optimize within a given structure, and distinguish predictive adequacy from explanatory correctness -- capabilities not exhibited here, not obviously addressed by scaling alone. [Abridged.]
匹配关键词: embodied AI
---

[ACADEMIC - ARXIV]
标题: SchGen: PCB Schematic Generation with Semantic-Grounded Code Representations
作者: Qinpei Luo, Ruichun Ma, Xinyu Zhang, Lili Qiu
链接: https://arxiv.org/abs/2605.30345v1
完整摘要: Printed circuit board (PCB) schematic design defines nearly all electronic hardware, but it remains manual and expertise-intensive. While generative AI has advanced digital and analog IC design, PCB schematic generation from natural-language intent is largely unexplored. This paper presents SchGen, the first large language model that generates editable PCB schematics from natural-language requests. The key challenge lies in the lack of an LLM-suited representation and a large-scale dataset. Current schematic formats are dominated by verbose, tool-specific syntax and geometry-heavy descriptions, making them difficult to generate reliably. We introduce a semantically grounded code representation that encodes schematic editing primitives with relative placement and pin-name-based wiring, transforming a geometry-driven generation problem into a semantics-driven matching task amenable to LLMs. We further construct a large-scale dataset of PCB schematics paired with user prompts via a human-agent collaborative pipeline that converts open-source hardware designs into our representation. Experiments show that SchGen significantly outperforms alternative representations and even larger general-purpose LLMs on wire connectivity accuracy and functional correctness. Our results highlight the critical role of representation design in enabling generative models for complex hardware design tasks.
匹配关键词: embodied AI
---

[ACADEMIC - ARXIV]
标题: Locally Coherent, Globally Incoherent: Bounding Compositional Incoherence in Multi-Component LLM Agents
作者: Anany Kotawala
链接: https://arxiv.org/abs/2605.30335v1
完整摘要: Multi-component LLM agents assemble probabilistic claims from components that each see only part of a joint problem; the composition can violate basic probability axioms even when every component is locally coherent. We formalise this locally coherent, globally incoherent failure via the compositional residual eps*, the L2 distance from the composed quote to the joint coherent polytope, computable at runtime from system output and the declared cross-component coupling constraints. A product-structure dichotomy characterises when local coherence suffices, and a Rayleigh-quotient prediction matches the observed residual within 7% on three of four relation classes. A hierarchical Boyle-Dykstra projection repairs the composition deterministically; an anytime-valid e-process gives sequential coherence monitoring. Across 1,876 ensemble cliques on a four-LLM mid-tier panel (frontier-panel rerun in Section 5.5), eps* > 0 on 33-94% of cliques, translating to +0.115 nats per bet of regret on 1,770 resolved bets under the proportional allocation rule (the gain collapses to +0.006 under bettors that themselves coherentise). Three intuitive LLM-side mitigations(retrieval, partition-aware prompting, aggregator-LLM) each fail or regress.
匹配关键词: embodied AI
---

[ACADEMIC - ARXIV]
标题: SoundnessBench: Can Your AI Scientist Really Tell Good Research Ideas from Bad Ones?
作者: Sy-Tuyen Ho, Minghui Liu, Huy Nghiem, Furong Huang
链接: https://arxiv.org/abs/2605.30329v1
完整摘要: Autonomous AI research agents aim to accelerate scientific discovery by automating the research pipeline, from hypothesis generation to peer review. However, existing benchmarks rarely test a fundamental bottleneck: whether Large Language Models can judge the methodological viability of a research idea before expending time and computational resources. We introduce SoundnessBench, a curated benchmark of 1,099 machine-learning research proposals reconstructed from ICLR submissions, labeled with reviewer soundness sub-scores, and audited against source papers. SoundnessBench should be interpreted as a benchmark for recoverable proposal-stage soundness rather than exact prediction of full-paper review outcomes. Across 12 frontier LLMs, we find a pervasive optimism bias: under standard prompting, models frequently rate low-soundness proposals as sound, while aggressive prompting largely shifts errors from false positives to false negatives. Additional controls for public-corpus contamination, paper-identifying phrases, surface features, and human audit quality suggest that this behavior is not explained by a single confounder. Our results indicate that current LLMs are not yet reliable as standalone first-gate evaluators for scientific rigor.
匹配关键词: embodied AI
---

[ACADEMIC - ARXIV]
标题: RoboWits: Unexpected Challenges for Robotic Creative Problem Solving
作者: Chunru Lin, Hongxin Zhang, Fenghao Yu, Zhehuan Chen, Thomas L. Griffiths, Yejin Choi, David Held, Chuang Gan
链接: https://arxiv.org/abs/2605.30326v1
完整摘要: The ability to reason, adapt, and creatively solve problems under unexpected challenges is essential for robots operating in real-world environments. However, current robotic benchmarks primarily emphasize skill-level execution and provide limited insight into such cognitive reasoning capabilities. We introduce RoboWits, a bi-manual robotic benchmark designed to systematically evaluate cognitive reasoning, creative tool use, and robustness to unexpected conditions. To enable scalable construction of high-quality reasoning-centric unexpected scenarios, we propose an automated task generation pipeline formulated as a multi-agent cooperative framework, comprising agents for seed task generation and verification, metric generation, scene generation, and task mutation. Using the pipeline, we curated 30 diverse seed tasks and 208 tasks with mutations and graded difficulty across geometry, material, and assembly-based reasoning. We benchmark popular robot policies, pre-trained VLAs, and oracle-state planners. Our results reveal a significant performance gap: while pre-trained VLAs exhibit preliminary success on seed tasks after single-task fine-tuning, they struggle to perform on mutated tasks, implying their brittleness in manipulation tasks requiring reasoning, strategy adaptation, and robustness to deceptive or constrained environments. Project page is available at https://umass-embodied-agi.github.io/RoboWits.
匹配关键词: embodied AI
---

[ACADEMIC - ARXIV]
标题: DynaFLIP: Rethinking Robotics Perception via Tri-Modal-Dynamics Guided Representation
作者: Jusuk Lee, Seungjae Lee, Jonghun Shin, Hoseong Jung, Sungha Kim, Daesol Cho, H. Jin Kim, Jia-Bin Huang, Furong Huang
链接: https://arxiv.org/abs/2605.30350v1
完整摘要: Robot manipulation critically depends on perception that preserves the action-relevant aspects of a scene. Yet most robot learning pipelines are built upon visual encoders pre-trained for static recognition or vision-language alignment, leaving motion understanding to downstream policies. We introduce DynaFLIP, a dynamics-aware multimodal pre-training framework that pushes motion understanding upstream into perception. We construct image-language-3D flow triplets from heterogeneous human and robot videos, and use these triplets as training-time supervision to shape an image-only encoder. Our key idea is to encourage the three modalities to span a small simplex volume in the shared hyperspherical space -- a smaller simplex volume indicating stronger alignment. To avoid the geometric ambiguity and trivial collapse of naive volume minimization, we combine simplex-volume minimization with a cosine regularizer and a contrastive objective. Our analyses show that DynaFLIP focuses on control-relevant regions critical for manipulation. The resulting dynamics-aware representations serve as reusable visual backbones and consistently outperform baselines across diverse downstream policies, including VLAs. We validate this across diverse simulation and real-world setups, with gains reaching +22.5% under out-of-distribution scenarios. Our results suggest that robot generalization improves when visual representations are trained to encode not just what is present, but how the world changes under action.
匹配关键词: robotics
---

[ACADEMIC - ARXIV]
标题: Uncertainty-driven 3D Gaussian Splatting Active Mapping via Anisotropic Visibility Field
作者: Shangjie Xue, Jesse Dill, Dhruv Ahuja, Frank Dellaert, Panagiotis Tsiotras, Danfei Xu
链接: https://arxiv.org/abs/2605.30342v1
完整摘要: We present Gaussian Splatting Anisotropic Visibility Field (GAVIS), a novel framework for uncertainty quantification and active mapping in 3DGS. Our key insight is that regions unseen from the training views yield unreliable predictions from the 3DGS. To address this, we introduce a principled and efficient method for quantifying the visibility field in 3DGS, defined as the anisotropic visibility of each particle with respect to the training views, and represented using spherical harmonics. The resulting visibility field is integrated into a Bayesian Network-based uncertainty-aware 3DGS rasterizer, enabling real-time (200 FPS) uncertainty quantification for synthesized views. Active mapping is further performed within a maximum information gain framework building on this formulation. Extensive experiments across diverse environments demonstrate that GAVIS consistently and significantly outperforms prior approaches in both accuracy and efficiency. Moreover, beyond standalone use, our method can be applied post-hoc to improve the performance of existing approaches.
匹配关键词: robotics
---

[ACADEMIC - ARXIV]
标题: Supercharging Thermal Gaussian Splatting with Depth Estimation
作者: Manoj Biswanath, Chenxin Cai, Hannah Schieber, Daniel Roth, Benjamin Busam
链接: https://arxiv.org/abs/2605.30328v1
完整摘要: Efficient and robust 3D scene representation is crucial in autonomous driving, robotics, and related fields. While RGB images provide valuable content for 3D reconstruction, other modalities like thermal or depth can enable additional information on the environment. Lately, novel view synthesis methods like 3D Gaussian Splatting have started using multiple modalities to further boost their performance. But fusing or combining multimodal data can make the process slower and can bring in additional challenges. Therefore, our project aims to use single modality based on thermal infrared domain, by removing the reliance on visible light as much as possible. This single modality can be expected to be faster as it does not rely on multimodal data. We propose a method, Thermal-to-Depth Gaussian Splatting (TDg), that uses only thermal images and depth estimation in its architecture to derive the radiance fields. Our TDg method outperforms the MSMG (Multiple Single-Modal Gaussians) baseline in most cases on our test datasets, RGBT-Scenes and ThermalMix. On average, the rendering quality metrics such as learned perceptual image patch similarity (LPIPS), structural similarity index measure (SSIM), and peak signal-to-noise ratio (PSNR) of TDg are 1.12%, 0.034%, and 0.01% better than the baseline MSMG values. It also reduces the training time significantly, by 12 mins 47 secs (55% improvement). Overall, our method is successful in deriving these thermal radiance fields, which can ultimately have several applications, such as identifying heat sources critical in surveillance, search or rescue operations, and industrial inspections where temperature is widely used to monitor machines.
匹配关键词: robotics
---

[ACADEMIC - ARXIV]
标题: RoboWits: Unexpected Challenges for Robotic Creative Problem Solving
作者: Chunru Lin, Hongxin Zhang, Fenghao Yu, Zhehuan Chen, Thomas L. Griffiths, Yejin Choi, David Held, Chuang Gan
链接: https://arxiv.org/abs/2605.30326v1
完整摘要: The ability to reason, adapt, and creatively solve problems under unexpected challenges is essential for robots operating in real-world environments. However, current robotic benchmarks primarily emphasize skill-level execution and provide limited insight into such cognitive reasoning capabilities. We introduce RoboWits, a bi-manual robotic benchmark designed to systematically evaluate cognitive reasoning, creative tool use, and robustness to unexpected conditions. To enable scalable construction of high-quality reasoning-centric unexpected scenarios, we propose an automated task generation pipeline formulated as a multi-agent cooperative framework, comprising agents for seed task generation and verification, metric generation, scene generation, and task mutation. Using the pipeline, we curated 30 diverse seed tasks and 208 tasks with mutations and graded difficulty across geometry, material, and assembly-based reasoning. We benchmark popular robot policies, pre-trained VLAs, and oracle-state planners. Our results reveal a significant performance gap: while pre-trained VLAs exhibit preliminary success on seed tasks after single-task fine-tuning, they struggle to perform on mutated tasks, implying their brittleness in manipulation tasks requiring reasoning, strategy adaptation, and robustness to deceptive or constrained environments. Project page is available at https://umass-embodied-agi.github.io/RoboWits.
匹配关键词: robotics
---

[ACADEMIC - ARXIV]
标题: A Heterogeneous Architecture for Robot RL Beyond GPU-Dominant Paradigms
作者: Yufei Jia, Zhanxiang Cao, Mingrui Yu, Heng Zhang, Shenyu Chen, Dixuan Jiang, Meng Li, Xiaofan Li, Yiyang Liu, Junzhe Wu, Zheng Li, XiLin Fang, Tingyu Cui, Shengcheng Fu, Haoyang Li, Anqi Wang, Zifan Wang, Dongjie Zhu, Chenyu Cao, Zhenbiao Huang, Ziang Zheng, Jie Lu, Xin Ma, Zhengyang Wei, Xiang Zhao, Tianyue Zhan, Ye He, Yuxiang Chen, Yizhou Jiang, Yue Li, Haizhou Ge, Yuhang Dong, Fan Jia, Ziheng Zhang, Meng Zhang, Xiwa Deng, Zhixing Chen, Hanyang Shao, Chenxin Dong, Yixuan Li, Yizhi Chen, Bokui Chen, Kaifeng Zhang, Hanqing Cui, Yusen Qin, Ruqi Huang, Lei Han, Tiancai Wang, Xiang Li, Yue Gao, Guyue Zhou
链接: https://arxiv.org/abs/2605.30313v1
完整摘要: Simulation-based RL for contemporary robot control is increasingly organized around GPU-resident simulation: physics, rollout collection, and learning are placed on a single GPU-centric execution path. This paradigm has greatly improved training speed, but it has also encouraged a default assumption that efficient training requires physics to reside on the GPU. We revisit this assumption. Our view is that, in simulation-dominated robot control, the essential question is not which processor runs physics, but whether simulation throughput, policy learning, and runtime synchronization form an efficient end-to-end loop. We present UniLab, a heterogeneous CPU-simulation / GPU-learning architecture that decouples CPU-parallel simulation from GPU policy updates through a unified runtime for data movement, buffering, and synchronization. UniLab is implemented as a complete and extensible training system using MuJoCoUni and MotrixSim CPU-batched physics backends, supporting PPO, SAC, FlashSAC, TD3, and APPO. On representative simulation-based robot control tasks, UniLab improves end-to-end training efficiency by 3--10$\times$ under the same hardware configuration, while reducing dependence on the NVIDIA CUDA-based software stack and supporting cross-platform execution on the Apple macOS platform and the AMD ROCm and Intel XPU accelerator backends. These results show that GPU simulation is an effective path to efficient training, but not a necessary one, broadening the practical system choices available for robot RL training. Project page: https://github.com/unilabsim/UniLab.
匹配关键词: robotics
---

[ACADEMIC - ARXIV]
标题: DynaFLIP: Rethinking Robotics Perception via Tri-Modal-Dynamics Guided Representation
作者: Jusuk Lee, Seungjae Lee, Jonghun Shin, Hoseong Jung, Sungha Kim, Daesol Cho, H. Jin Kim, Jia-Bin Huang, Furong Huang
链接: https://arxiv.org/abs/2605.30350v1
完整摘要: Robot manipulation critically depends on perception that preserves the action-relevant aspects of a scene. Yet most robot learning pipelines are built upon visual encoders pre-trained for static recognition or vision-language alignment, leaving motion understanding to downstream policies. We introduce DynaFLIP, a dynamics-aware multimodal pre-training framework that pushes motion understanding upstream into perception. We construct image-language-3D flow triplets from heterogeneous human and robot videos, and use these triplets as training-time supervision to shape an image-only encoder. Our key idea is to encourage the three modalities to span a small simplex volume in the shared hyperspherical space -- a smaller simplex volume indicating stronger alignment. To avoid the geometric ambiguity and trivial collapse of naive volume minimization, we combine simplex-volume minimization with a cosine regularizer and a contrastive objective. Our analyses show that DynaFLIP focuses on control-relevant regions critical for manipulation. The resulting dynamics-aware representations serve as reusable visual backbones and consistently outperform baselines across diverse downstream policies, including VLAs. We validate this across diverse simulation and real-world setups, with gains reaching +22.5% under out-of-distribution scenarios. Our results suggest that robot generalization improves when visual representations are trained to encode not just what is present, but how the world changes under action.
匹配关键词: humanoid robot
---

[ACADEMIC - ARXIV]
标题: Supercharging Thermal Gaussian Splatting with Depth Estimation
作者: Manoj Biswanath, Chenxin Cai, Hannah Schieber, Daniel Roth, Benjamin Busam
链接: https://arxiv.org/abs/2605.30328v1
完整摘要: Efficient and robust 3D scene representation is crucial in autonomous driving, robotics, and related fields. While RGB images provide valuable content for 3D reconstruction, other modalities like thermal or depth can enable additional information on the environment. Lately, novel view synthesis methods like 3D Gaussian Splatting have started using multiple modalities to further boost their performance. But fusing or combining multimodal data can make the process slower and can bring in additional challenges. Therefore, our project aims to use single modality based on thermal infrared domain, by removing the reliance on visible light as much as possible. This single modality can be expected to be faster as it does not rely on multimodal data. We propose a method, Thermal-to-Depth Gaussian Splatting (TDg), that uses only thermal images and depth estimation in its architecture to derive the radiance fields. Our TDg method outperforms the MSMG (Multiple Single-Modal Gaussians) baseline in most cases on our test datasets, RGBT-Scenes and ThermalMix. On average, the rendering quality metrics such as learned perceptual image patch similarity (LPIPS), structural similarity index measure (SSIM), and peak signal-to-noise ratio (PSNR) of TDg are 1.12%, 0.034%, and 0.01% better than the baseline MSMG values. It also reduces the training time significantly, by 12 mins 47 secs (55% improvement). Overall, our method is successful in deriving these thermal radiance fields, which can ultimately have several applications, such as identifying heat sources critical in surveillance, search or rescue operations, and industrial inspections where temperature is widely used to monitor machines.
匹配关键词: humanoid robot
---

[ACADEMIC - ARXIV]
标题: RoboWits: Unexpected Challenges for Robotic Creative Problem Solving
作者: Chunru Lin, Hongxin Zhang, Fenghao Yu, Zhehuan Chen, Thomas L. Griffiths, Yejin Choi, David Held, Chuang Gan
链接: https://arxiv.org/abs/2605.30326v1
完整摘要: The ability to reason, adapt, and creatively solve problems under unexpected challenges is essential for robots operating in real-world environments. However, current robotic benchmarks primarily emphasize skill-level execution and provide limited insight into such cognitive reasoning capabilities. We introduce RoboWits, a bi-manual robotic benchmark designed to systematically evaluate cognitive reasoning, creative tool use, and robustness to unexpected conditions. To enable scalable construction of high-quality reasoning-centric unexpected scenarios, we propose an automated task generation pipeline formulated as a multi-agent cooperative framework, comprising agents for seed task generation and verification, metric generation, scene generation, and task mutation. Using the pipeline, we curated 30 diverse seed tasks and 208 tasks with mutations and graded difficulty across geometry, material, and assembly-based reasoning. We benchmark popular robot policies, pre-trained VLAs, and oracle-state planners. Our results reveal a significant performance gap: while pre-trained VLAs exhibit preliminary success on seed tasks after single-task fine-tuning, they struggle to perform on mutated tasks, implying their brittleness in manipulation tasks requiring reasoning, strategy adaptation, and robustness to deceptive or constrained environments. Project page is available at https://umass-embodied-agi.github.io/RoboWits.
匹配关键词: humanoid robot
---

[ACADEMIC - ARXIV]
标题: A Heterogeneous Architecture for Robot RL Beyond GPU-Dominant Paradigms
作者: Yufei Jia, Zhanxiang Cao, Mingrui Yu, Heng Zhang, Shenyu Chen, Dixuan Jiang, Meng Li, Xiaofan Li, Yiyang Liu, Junzhe Wu, Zheng Li, XiLin Fang, Tingyu Cui, Shengcheng Fu, Haoyang Li, Anqi Wang, Zifan Wang, Dongjie Zhu, Chenyu Cao, Zhenbiao Huang, Ziang Zheng, Jie Lu, Xin Ma, Zhengyang Wei, Xiang Zhao, Tianyue Zhan, Ye He, Yuxiang Chen, Yizhou Jiang, Yue Li, Haizhou Ge, Yuhang Dong, Fan Jia, Ziheng Zhang, Meng Zhang, Xiwa Deng, Zhixing Chen, Hanyang Shao, Chenxin Dong, Yixuan Li, Yizhi Chen, Bokui Chen, Kaifeng Zhang, Hanqing Cui, Yusen Qin, Ruqi Huang, Lei Han, Tiancai Wang, Xiang Li, Yue Gao, Guyue Zhou
链接: https://arxiv.org/abs/2605.30313v1
完整摘要: Simulation-based RL for contemporary robot control is increasingly organized around GPU-resident simulation: physics, rollout collection, and learning are placed on a single GPU-centric execution path. This paradigm has greatly improved training speed, but it has also encouraged a default assumption that efficient training requires physics to reside on the GPU. We revisit this assumption. Our view is that, in simulation-dominated robot control, the essential question is not which processor runs physics, but whether simulation throughput, policy learning, and runtime synchronization form an efficient end-to-end loop. We present UniLab, a heterogeneous CPU-simulation / GPU-learning architecture that decouples CPU-parallel simulation from GPU policy updates through a unified runtime for data movement, buffering, and synchronization. UniLab is implemented as a complete and extensible training system using MuJoCoUni and MotrixSim CPU-batched physics backends, supporting PPO, SAC, FlashSAC, TD3, and APPO. On representative simulation-based robot control tasks, UniLab improves end-to-end training efficiency by 3--10$\times$ under the same hardware configuration, while reducing dependence on the NVIDIA CUDA-based software stack and supporting cross-platform execution on the Apple macOS platform and the AMD ROCm and Intel XPU accelerator backends. These results show that GPU simulation is an effective path to efficient training, but not a necessary one, broadening the practical system choices available for robot RL training. Project page: https://github.com/unilabsim/UniLab.
匹配关键词: humanoid robot
---

[ACADEMIC - ARXIV]
标题: Gaze2Act: Gaze-Conditioned Vision-Language-Action Policies for Interactive Robot Manipulation
作者: Kuangji Zuo, Gen Li, Bofan Lyu, Yanshuo Lu, Boyu Ma, Shijia Han, Xinyu Zhou, Xichen Yuan, Chuhao Zhou, Jiaqi Bai, Geng Li, Jianfei Yang
链接: https://arxiv.org/abs/2605.30282v1
完整摘要: Vision-Language-Action (VLA) models have recently shown strong potential for robot learning by following language instructions. However, in practice, language alone is often insufficient to precisely convey human intent. It is difficult to describe which exact object to interact with among similar candidates, where to act on the object, or how the target may change during execution. To address this limitation, we propose Gaze2Act, a novel VLA framework that leverages human gaze as a dynamic and intuitive intent signal for complex interactive manipulation. Gaze2Act first bridges the ego-exo view gap by mapping first-person gaze into the robot's perspective through cross-view semantic matching, producing both an object mask and a gaze point for coarse-to-fine target specification. These cues are then integrated into the policy through perception-level prompting and action-level conditioning, allowing the robot to attend to relevant regions and execute precise interactions under dynamic intent. In a systematic evaluation across seven task categories and 16 real-robot tasks on a Unitree G1 humanoid, Gaze2Act achieves state-of-the-art performance in both intent accuracy and task success rate. It notably outperforms baselines in object disambiguation, fine-grained interaction, and dynamic intent steering. These results demonstrate that human gaze provides a natural, low-burden, and highly expressive modality for human-in-the-loop VLA control.
匹配关键词: humanoid robot
---

[ACADEMIC - ARXIV]
标题: DynaFLIP: Rethinking Robotics Perception via Tri-Modal-Dynamics Guided Representation
作者: Jusuk Lee, Seungjae Lee, Jonghun Shin, Hoseong Jung, Sungha Kim, Daesol Cho, H. Jin Kim, Jia-Bin Huang, Furong Huang
链接: https://arxiv.org/abs/2605.30350v1
完整摘要: Robot manipulation critically depends on perception that preserves the action-relevant aspects of a scene. Yet most robot learning pipelines are built upon visual encoders pre-trained for static recognition or vision-language alignment, leaving motion understanding to downstream policies. We introduce DynaFLIP, a dynamics-aware multimodal pre-training framework that pushes motion understanding upstream into perception. We construct image-language-3D flow triplets from heterogeneous human and robot videos, and use these triplets as training-time supervision to shape an image-only encoder. Our key idea is to encourage the three modalities to span a small simplex volume in the shared hyperspherical space -- a smaller simplex volume indicating stronger alignment. To avoid the geometric ambiguity and trivial collapse of naive volume minimization, we combine simplex-volume minimization with a cosine regularizer and a contrastive objective. Our analyses show that DynaFLIP focuses on control-relevant regions critical for manipulation. The resulting dynamics-aware representations serve as reusable visual backbones and consistently outperform baselines across diverse downstream policies, including VLAs. We validate this across diverse simulation and real-world setups, with gains reaching +22.5% under out-of-distribution scenarios. Our results suggest that robot generalization improves when visual representations are trained to encode not just what is present, but how the world changes under action.
匹配关键词: manipulation
---

[ACADEMIC - ARXIV]
标题: Unlocking the Working Memory of Large Language Models for Latent Reasoning
作者: Lukas Aichberger, Sepp Hochreiter
链接: https://arxiv.org/abs/2605.30343v1
完整摘要: To improve the reasoning capabilities of large language models, test-time compute is typically scaled by generating intermediate tokens before the final answer. However, this couples reasoning to autoregressive generation and thereby conflates internal computation with external communication. In contrast, human cognition can use working memory to hold and manipulate information internally without the need to externalize intermediate thoughts. Drawing on this principle, we introduce Reasoning in Memory (RiM), a latent reasoning method that replaces the autoregressive generation of reasoning steps with memory blocks. These memory blocks are fixed sequences of special tokens that unlock the working-memory capacity of large language models. Since they are fixed rather than generated, they can be processed in a single forward pass, enabling compute-efficient latent reasoning. To operationalize these memory blocks, we employ a two-stage curriculum. First, we ground them by predicting explicit reasoning steps after each memory block. Second, we discard this step-level supervision and iteratively refine the final answer after each memory block. Our experiments on reasoning benchmarks show that, across language models of different families and sizes, RiM matches or exceeds existing latent reasoning methods while avoiding the autoregressive generation of thoughts. These results demonstrate that large language models can be trained to use working memory as an effective mechanism for latent reasoning.
匹配关键词: manipulation
---

[ACADEMIC - ARXIV]
标题: RoboWits: Unexpected Challenges for Robotic Creative Problem Solving
作者: Chunru Lin, Hongxin Zhang, Fenghao Yu, Zhehuan Chen, Thomas L. Griffiths, Yejin Choi, David Held, Chuang Gan
链接: https://arxiv.org/abs/2605.30326v1
完整摘要: The ability to reason, adapt, and creatively solve problems under unexpected challenges is essential for robots operating in real-world environments. However, current robotic benchmarks primarily emphasize skill-level execution and provide limited insight into such cognitive reasoning capabilities. We introduce RoboWits, a bi-manual robotic benchmark designed to systematically evaluate cognitive reasoning, creative tool use, and robustness to unexpected conditions. To enable scalable construction of high-quality reasoning-centric unexpected scenarios, we propose an automated task generation pipeline formulated as a multi-agent cooperative framework, comprising agents for seed task generation and verification, metric generation, scene generation, and task mutation. Using the pipeline, we curated 30 diverse seed tasks and 208 tasks with mutations and graded difficulty across geometry, material, and assembly-based reasoning. We benchmark popular robot policies, pre-trained VLAs, and oracle-state planners. Our results reveal a significant performance gap: while pre-trained VLAs exhibit preliminary success on seed tasks after single-task fine-tuning, they struggle to perform on mutated tasks, implying their brittleness in manipulation tasks requiring reasoning, strategy adaptation, and robustness to deceptive or constrained environments. Project page is available at https://umass-embodied-agi.github.io/RoboWits.
匹配关键词: manipulation
---

[ACADEMIC - ARXIV]
标题: Gaze2Act: Gaze-Conditioned Vision-Language-Action Policies for Interactive Robot Manipulation
作者: Kuangji Zuo, Gen Li, Bofan Lyu, Yanshuo Lu, Boyu Ma, Shijia Han, Xinyu Zhou, Xichen Yuan, Chuhao Zhou, Jiaqi Bai, Geng Li, Jianfei Yang
链接: https://arxiv.org/abs/2605.30282v1
完整摘要: Vision-Language-Action (VLA) models have recently shown strong potential for robot learning by following language instructions. However, in practice, language alone is often insufficient to precisely convey human intent. It is difficult to describe which exact object to interact with among similar candidates, where to act on the object, or how the target may change during execution. To address this limitation, we propose Gaze2Act, a novel VLA framework that leverages human gaze as a dynamic and intuitive intent signal for complex interactive manipulation. Gaze2Act first bridges the ego-exo view gap by mapping first-person gaze into the robot's perspective through cross-view semantic matching, producing both an object mask and a gaze point for coarse-to-fine target specification. These cues are then integrated into the policy through perception-level prompting and action-level conditioning, allowing the robot to attend to relevant regions and execute precise interactions under dynamic intent. In a systematic evaluation across seven task categories and 16 real-robot tasks on a Unitree G1 humanoid, Gaze2Act achieves state-of-the-art performance in both intent accuracy and task success rate. It notably outperforms baselines in object disambiguation, fine-grained interaction, and dynamic intent steering. These results demonstrate that human gaze provides a natural, low-burden, and highly expressive modality for human-in-the-loop VLA control.
匹配关键词: manipulation
---

[ACADEMIC - ARXIV]
标题: Qwen-VLA: Unifying Vision-Language-Action Modeling across Tasks, Environments, and Robot Embodiments
作者: Qiuyue Wang, Mingsheng Li, Jian Guan, Jinhui Ye, Sicheng Xie, Yitao Liu, Junhao Chen, Zhixuan Liang, Jie Zhang, Xintong Hu, Xuhong Huang, Pei Lin, Junyang Lin, Dayiheng Liu, Shuai Bai, Jingren Zhou, Jiazhao Zhang, Haoqi Yuan, Gengze Zhou, Hang Yin, Ye Wang, Yiyang Huang, Zixing Lei, Wujian Peng, Delin Chen, Yingming Zheng, Jingyang Fan, Xianwei Zhuang, Xin Zhou, Haoyang Li, Anzhe Chen, Tong Zhang, Xuejing Liu, Yuchong Sun, Ruizhe Chen, Zhaohai Li, Chenxu Lü, Zhibo Yang, Tao Yu, Xionghui Chen
链接: https://arxiv.org/abs/2605.30280v1
完整摘要: Embodied intelligence is often studied through specialized models for individual tasks such as manipulation or navigation, resulting in fragmented capabilities and limited generalization across tasks, environments, and robot embodiments. In this work, we study whether heterogeneous embodied decision-making problems can be unified within a single vision-language-action model. We present Qwen-VLA, a unified embodied foundation model that extends Qwen's vision-language modeling stack from perception, understanding, and reasoning to continuous action and trajectory generation through a DiT-based action decoder. Qwen-VLA is trained with a large-scale joint pretraining recipe over diverse data sources, including robotics manipulation trajectories, human egocentric demonstrations, synthetic simulation data, vision-and-language navigation data, trajectory-centric supervision, and auxiliary vision-language data. To support multiple robot platforms, we introduce embodiment-aware prompt conditioning, where robot-specific textual descriptions specify the current embodiment and control convention. We further cast manipulation, navigation, and trajectory prediction into a unified action-and-trajectory prediction framework, enabling transferable visual grounding, spatial reasoning, and continuous action generation across robot morphologies, task families, and environments. Experiments on manipulation, navigation, and trajectory-centric benchmarks show consistent multi-task performance and out-of-distribution generalization under variations in scene layout, background, lighting, object configuration, and robot embodiment. Qwen-VLA-Instruct achieves 97.9% on LIBERO, 73.7% on Simpler-WidowX, 86.1%/87.2% on RoboTwin-Easy/Hard, 69.0% OSR on R2R, 59.6% SR on RxR, 76.9% average OOD success in real-world ALOHA experiments, and 26.6% zero-shot success on DOMINO dynamic manipulation.
匹配关键词: manipulation
---

[ACADEMIC - ARXIV]
标题: YoCausal: How Far is Video Generation from World Model? A Causality Perspective
作者: You-Zhe Xie, Yu-Hsuan Li, Jie-Ying Lee, Kaipeng Zhang, Yu-Lun Liu, Zhixiang Wang
链接: https://arxiv.org/abs/2605.30346v1
完整摘要: As video diffusion models (VDMs) advance toward world models, a key question arises: do they truly understand causality, or merely overfit to statistical temporal patterns? Existing benchmarks mostly rely on synthetic data, limiting real-world generalization due to the sim-to-real gap. We present YoCausal, a two-level benchmark inspired by the Violation of Expectation (VoE) paradigm from cognitive science. By temporally reversing real-world videos at zero cost as natural counterfactual samples, YoCausal establishes an arbitrarily extensible evaluation protocol. Level 1 introduces the Reverse Surprise Index (RSI), quantifying arrow-of-time perception via denoising loss. Level 2 introduces the Causality Cognition Index (CCI), which leverages a VLM to stratify datasets into causal and non-causal subsets, disentangling genuine causal reasoning from temporal bias. Evaluation of 13 state-of-the-art VDMs reveals that perceiving the arrow of time does not imply understanding causality, and a significant gap persists relative to human-level causal cognition.
匹配关键词: sim-to-real
---

[ACADEMIC - ARXIV]
标题: PhAIL: A Real-Robot VLA Benchmark and Distributional Methodology
作者: Sergey Arkhangelskiy
链接: https://arxiv.org/abs/2605.29710v1
完整摘要: Real-world evaluation of vision-language-action (VLA) policies still rests on binary success rate at a fixed timeout with $N \le 25$ rollouts per condition, almost always without confidence intervals or paired statistical comparison; these cohort sizes struggle to resolve close comparisons reliably. We introduce PhAIL (Physical AI Leaderboard, https://phail.ai), an open real-robot benchmark on a Franka FR3 (dataset, per-rollout artifacts, and end-to-end reference implementation) of a distributional evaluation methodology: the time-to-success cumulative distribution function (CDF) as the evaluation primitive, with two separated jobs. The first is scoring via Human-Relative Throughput (HRT), a dimensionless scalar with bootstrap confidence intervals, anchored to same-fixture human teleoperation. The second is a significance test (Kolmogorov-Smirnov, computed per-object and macro-averaged across objects). On four publicly-available VLAs, the macro-averaged KS test resolves two close comparisons (GR00T vs. ACT, OpenPI vs. ACT) at $N \le 30$ rollouts per (model, object) cell where binary-threshold metrics do not; the closest pair (OpenPI vs. GR00T) remains unresolved within our budget. The best evaluated VLA is $\sim 7\times$ slower per operation (RMST ratio) than the human reference.
匹配关键词: sim-to-real
---

[ACADEMIC - ARXIV]
标题: Battery-Sim-Agent: Leveraging LLM-Agent for Inverse Battery Parameter Estimation
作者: Jiawei Chen, Xiaofan Gui, Shikai Fang, Shengyu Tao, Shun Zheng, Weiqing Liu, Jiang Bian
链接: https://arxiv.org/abs/2605.29560v1
完整摘要: Parameterizing high-fidelity "digital twins" of batteries is a critical yet challenging inverse problem that hinders the pace of battery innovation. Prevailing methods formulate this as a black-box optimization (BBO) task, employing algorithms that are sample-inefficient and blind to the underlying physics. In this work, we introduce a new paradigm that reframes the inverse problem as a reasoning task, and present Battery-Sim-Agent, the first framework to deploy a Large Language Model (LLM) agent in a closed loop with a high-fidelity battery simulator. The agent mimics a human scientist's workflow: it interprets rich, multi-modal feedback from the simulator, forms physically-grounded hypotheses to explain discrepancies, and proposes structured parameter updates. On a systematically constructed benchmark suite spanning diverse battery chemistries, operating conditions, and difficulty levels, our agent significantly outperforms strong BBO baselines like Bayesian optimization in identifying accurate parameters. We further demonstrate the framework's capability in complex long-horizon degradation fitting tasks and validate its practical applicability on real-world battery datasets. Our results highlight the promise of LLM-agents as reasoning-based optimizers for scientific discovery and battery parameter estimation.
匹配关键词: sim-to-real
---

[ACADEMIC - ARXIV]
标题: Physics Is All You Need? A Case Study in Physicist-Supervised AI Development of Scientific Software
作者: Nhat-Minh Nguyen
链接: https://arxiv.org/abs/2605.30353v1
完整摘要: Are AI agents tools, co-authors, or researchers? We present a quantified case study ($N=1$): a physicist supervising an AI coding agent (Claude Code, Sonnet and Opus models) over 12 work days and 57 sessions to build CLAX-PT, a differentiable one-loop perturbation theory module in JAX. We documented and classified 15 supervision events by intervention level. The agent resolved ten autonomously by iterating against oracle tests. Two more by the physicist's domain knowledge. The three it could not -- all evaded oracle detection -- share a common property: the agent treated symptom reduction as root-cause resolution. It spent 33 of the 57 sessions adjusting coefficients within a code architecture that could not represent the target physics, and could not re-evaluate its CLASS-PT branch choice even when prompted to reconsider; only an injected physics concept (anisotropic BAO damping) triggered the redesign. Separately, the agent committed a calibrated correction that passed all oracle tests but corresponded to no quantity in the theory, predicting wrong values at any other cosmology. The fudge factor was caught and replaced within the same session. Three supervision practices proved critical for catching what oracle tests missed: testing at diverse parameter points beyond the fiducial calibration; shared changelogs that surfaced stalled exploration across sessions; and an explicit rule against unphysical numerical patches. In this case, supervision design, not model capability, determined whether the agent's output was trustworthy. Closing the gap would require agents that propose architectural alternatives rather than optimize within a given structure, and distinguish predictive adequacy from explanatory correctness -- capabilities not exhibited here, not obviously addressed by scaling alone. [Abridged.]
匹配关键词: world model
---

[ACADEMIC - ARXIV]
标题: GMOS: Grounding Moving Object Segmentation in 3D Space and Time
作者: Junyu Xie, Tengda Han, Weidi Xie, Andrew Zisserman
链接: https://arxiv.org/abs/2605.30352v1
完整摘要: Moving Object Segmentation (MOS) aims to discover, segment, and track objects that move independently of the camera. Current MOS methods, however, exhibit two fundamental limitations: they rely on pre-computed 2D auxiliary modalities such as optical flow or point trajectories that lack 3D geometric information, and they treat motion as a sequence-level attribute, overlooking the instantaneous motion state of each object. We address both by grounding MOS in 3D space and time, and propose GMOS, a framework that operates directly on RGB video to produce 3D-aware, temporally fine-grained segmentation of multiple moving objects, alongside a foreground--background variant GMOS-S for faster deployment. To support training and evaluation in this regime, we curate GMOS-2K, a dataset of 2,210 real-world videos with per-object temporal motion annotations drawn from five established Video Object Segmentation (VOS) benchmarks, and formalise MOS-I ("I" for instantaneous), a temporally fine-grained evaluation protocol with three complementary metrics. GMOS achieves state-of-the-art results across MOS, MOS-I, and Unsupervised VOS benchmarks, while running significantly faster than prior multi-object MOS methods and supporting online inference for streaming deployment.
匹配关键词: world model
---

[ACADEMIC - ARXIV]
标题: VideoMLA: Low-Rank Latent KV Cache for Minute-Scale Autoregressive Video Diffusion
作者: Hidir Yesiltepe, Jiazhen Hu, Tuna Han Salih Meral, Adil Kaan Akan, Kaan Oktay, Hoda Eldardiry, Pinar Yanardag
链接: https://arxiv.org/abs/2605.30351v1
完整摘要: Long-rollout causal video diffusion has converged on a fixed-size sliding-window KV cache, with recent progress innovating within this layout by changing which tokens occupy the window or how their positions are encoded. The per-head KV layout itself, a dominant contributor to streaming memory and latency, has been mostly left unchanged. In this paper, we present the first study of Multi-Head Latent Attention (MLA) in video diffusion. VideoMLA replaces per-head keys and values with a shared low-rank content latent and a shared decoupled 3D-RoPE positional key, reducing per-token KV memory by 92.7% at every cached layer. We further investigate why MLA succeeds in video diffusion even though the spectral assumption often used to motivate it in language models does not hold: pretrained video attention is not low-rank, with 99%-energy effective rank far above any practical latent dimension. VideoMLA retains quality at compression ratios where direct spectral approximation would predict large reconstruction error. We show that the MLA bottleneck, rather than the pretrained spectrum, determines the effective rank: both spectral and random initialization occupy nearly the full rank budget from initialization, and training preserves this budget while adapting within it. On VBench, VideoMLA matches short-horizon streaming video diffusion baselines, achieves the best overall score at long horizons among evaluated methods, and improves throughput by 1.23x on a single B200.
匹配关键词: world model
---

[ACADEMIC - ARXIV]
标题: DynaFLIP: Rethinking Robotics Perception via Tri-Modal-Dynamics Guided Representation
作者: Jusuk Lee, Seungjae Lee, Jonghun Shin, Hoseong Jung, Sungha Kim, Daesol Cho, H. Jin Kim, Jia-Bin Huang, Furong Huang
链接: https://arxiv.org/abs/2605.30350v1
完整摘要: Robot manipulation critically depends on perception that preserves the action-relevant aspects of a scene. Yet most robot learning pipelines are built upon visual encoders pre-trained for static recognition or vision-language alignment, leaving motion understanding to downstream policies. We introduce DynaFLIP, a dynamics-aware multimodal pre-training framework that pushes motion understanding upstream into perception. We construct image-language-3D flow triplets from heterogeneous human and robot videos, and use these triplets as training-time supervision to shape an image-only encoder. Our key idea is to encourage the three modalities to span a small simplex volume in the shared hyperspherical space -- a smaller simplex volume indicating stronger alignment. To avoid the geometric ambiguity and trivial collapse of naive volume minimization, we combine simplex-volume minimization with a cosine regularizer and a contrastive objective. Our analyses show that DynaFLIP focuses on control-relevant regions critical for manipulation. The resulting dynamics-aware representations serve as reusable visual backbones and consistently outperform baselines across diverse downstream policies, including VLAs. We validate this across diverse simulation and real-world setups, with gains reaching +22.5% under out-of-distribution scenarios. Our results suggest that robot generalization improves when visual representations are trained to encode not just what is present, but how the world changes under action.
匹配关键词: world model
---

[ACADEMIC - ARXIV]
标题: LLMSurgeon: Diagnosing Data Mixture of Large Language Models
作者: Yaxin Luo, Jiacheng Cui, Xiaohan Zhao, Xinyi Shang, Jiacheng Liu, Xinyue Bi, Zhaoyi Li, Zhiqiang Shen
链接: https://arxiv.org/abs/2605.30348v1
完整摘要: The pretraining data mixture of Large Language Models (LLMs) constitutes their "digital DNA", shaping model behaviors, capabilities, and failure modes. Yet this composition is rarely disclosed, making post-hoc auditing of data combination or provenance difficult. In this work, we formalize $\textbf{Data Mixture Surgery (DMS)}$: given only generated text from a target LLM, estimate the domain-level distribution of its pretraining corpus under a predefined taxonomy. We propose $\textbf{LLMSurgeon}$, a strong framework that casts DMS as an inverse problem under the label-shift assumption. Rather than directly aggregating classifier outputs, LLMSurgeon estimates a calibrated $\textit{soft}$ confusion matrix and solves a constrained inverse problem to correct systematic domain confusion and recover the latent mixture prior. To evaluate, we introduce $\textbf{LLMScan}$, a recipe-verifiable evaluation suite built from open-source LLMs with transparent pretraining mixtures. Across LLMScan, LLMSurgeon recovers domain mixtures with high fidelity under fixed protocols. Our work presents a practical, post-hoc approach for auditing the digital DNA of foundation models without access to their training data.
匹配关键词: world model
---

[ACADEMIC - ARXIV]
标题: Benchmarking Single-Factor Physical Video-to-Audio Generation
作者: Tingle Li, Siddharth Gururani, Kevin J. Shih, Gantavya Bhatt, Sang-gil Lee, Zhifeng Kong, Arushi Goel, Gopala Anumanchipalli, Ming-Yu Liu
链接: https://arxiv.org/abs/2605.30339v1
完整摘要: Generative video-to-audio (V2A) models produce highly plausible soundtracks, but it remains unclear whether they capture the underlying physical processes. Existing evaluations emphasize perceptual realism and overlook physical correctness under controlled interventions. In this paper, we introduce FlatSounds, a benchmark that audits the physical reasoning of V2A models through: 1) controlled counterfactual pairs in which a single physical factor is varied, and 2) single-video pattern tests that probe internal consistency and directional trends. These settings test whether the generated audio correctly reflects specific physical properties and timings. Our evaluation of state-of-the-art models reveals a consistent trade-off: models rely more on text captions than the visual stream to infer physics and semantics. Captions generally improve physical and semantic accuracy, but paradoxically degrade temporal alignment. Our results highlight the need to move beyond audio quality toward learning physical processes directly from pixels. Finally, we find that our physics-based metrics correlate strongly with human preference tests on our own data. Project webpage: https://research.nvidia.com/labs/cosmos-lab/flatsounds/
匹配关键词: speech synthesis
---

[ACADEMIC - ARXIV]
标题: Colored Noise Diffusion Sampling
作者: Hadar Davidson, Noam Issachar, Sagie Benaim
链接: https://arxiv.org/abs/2605.30332v1
完整摘要: Diffusion models achieve state-of-the-art image synthesis, with their generative trajectories fundamentally exhibiting a spectral bias, resolving low-frequency global structures early and high-frequency fine details later. Conventional stochastic differential equation (SDE) solvers fail to account for this dynamic, naively injecting uniform white noise throughout the entire process and misusing the finite energy budget. In this work, we establish a mathematical framework that reconsiders SDE inference as a targeted, frequency-decoupled energy transfer. Leveraging this framework, we introduce Colored Noise Sampling (CNS), a novel, training-free stochastic solver. Rather than injecting uniform white noise, CNS utilizes a dynamic, timestep- and frequency-dependent schedule that more efficiently allocates injected energy toward structurally unresolved frequency bands. By actively exploiting the model's inherent spectral bias, CNS systematically steers the generated distribution toward the true data manifold. Extensive experiments demonstrate that CNS significantly outperforms standard ODE and SDE baselines as a strictly plug-and-play, inference-time sampler substitution across diverse architectures (SiT, JiT, FLUX). Compared to standard sampling on ImageNet-256, CNS achieves substantial unguided FID reductions, improving from 8.26 to 6.27 on SiT-XL/2, 32.39 to 26.69 on JiT-B/16, and 11.88 to 8.31 on JiT-H/16, while yielding consistent relative FID improvements with Classifier-Free Guidance. Project page is available at https://hadardavidson.github.io/CNS/.
匹配关键词: speech synthesis
---

[ACADEMIC - ARXIV]
标题: Supercharging Thermal Gaussian Splatting with Depth Estimation
作者: Manoj Biswanath, Chenxin Cai, Hannah Schieber, Daniel Roth, Benjamin Busam
链接: https://arxiv.org/abs/2605.30328v1
完整摘要: Efficient and robust 3D scene representation is crucial in autonomous driving, robotics, and related fields. While RGB images provide valuable content for 3D reconstruction, other modalities like thermal or depth can enable additional information on the environment. Lately, novel view synthesis methods like 3D Gaussian Splatting have started using multiple modalities to further boost their performance. But fusing or combining multimodal data can make the process slower and can bring in additional challenges. Therefore, our project aims to use single modality based on thermal infrared domain, by removing the reliance on visible light as much as possible. This single modality can be expected to be faster as it does not rely on multimodal data. We propose a method, Thermal-to-Depth Gaussian Splatting (TDg), that uses only thermal images and depth estimation in its architecture to derive the radiance fields. Our TDg method outperforms the MSMG (Multiple Single-Modal Gaussians) baseline in most cases on our test datasets, RGBT-Scenes and ThermalMix. On average, the rendering quality metrics such as learned perceptual image patch similarity (LPIPS), structural similarity index measure (SSIM), and peak signal-to-noise ratio (PSNR) of TDg are 1.12%, 0.034%, and 0.01% better than the baseline MSMG values. It also reduces the training time significantly, by 12 mins 47 secs (55% improvement). Overall, our method is successful in deriving these thermal radiance fields, which can ultimately have several applications, such as identifying heat sources critical in surveillance, search or rescue operations, and industrial inspections where temperature is widely used to monitor machines.
匹配关键词: speech synthesis
---

[ACADEMIC - ARXIV]
标题: Boosting Image Quality Assessment Performance: Unsupervised Score Fusion by Deep Maximum a Posteriori Estimation
作者: Zhongling Wang, Raymond Zhou, Shahrukh Athar, Wenbo Yang, Zhou Wang
链接: https://arxiv.org/abs/2605.30269v1
完整摘要: Over the past decades, numerous Image Quality Assessment (IQA) models have emerged, aiming to predict the perceptual quality of images. However, individual models are often biased toward certain types of image content or distortions, depending on the design principle and process. An intuitive idea is to harness the strengths and mitigate the weaknesses of each IQA model, by fusing the scores of multiple models into a stronger one. Here we make one of the first attempts to seek an optimal solution for the idea and propose a general framework for unsupervised IQA score fusion using deep Maximum a Posteriori (MAP) estimation. The proposed model conducts fine-grained uncertainty estimation at the score level to increase the accuracy and reduce the uncertainty in fused predictions. Comprehensive experiments demonstrate the superiority of the proposed model over individual IQA models and other fusion methods. It also exhibits an interesting capability of rejecting ``bad" models in the fusion process.
匹配关键词: speech synthesis
---

[ACADEMIC - ARXIV]
标题: VideoFDB: Evaluating Full-Duplex Vision-Speech Capabilities in Conversational Agents
作者: Amrita Mazumdar, Seonwook Park, Rajarshi Roy, Nikhil Srihari, Shengze Wang, Yuhao Zhou, Julia Wang, Koki Nagano, Shalini De Mello
链接: https://arxiv.org/abs/2605.30256v1
完整摘要: Natural human conversation is full-duplex and audio-visual: people simultaneously speak and listen while continuously interpreting and producing nonverbal cues, such as nods, smiles, and gestures. To support successful human-agent interaction, agents must model full-duplex audiovisual conversation; however, existing full-duplex benchmarks evaluate only speech. In this work, we present VideoFDB, the first benchmark to evaluate full-duplex audio-visual-to-audio-visual (AV2AV) conversational agents. VideoFDB contributes (i) 237 dyadic clips spanning 11 nonverbal conversational dynamics from real-world video calls, (ii) a taxonomy separating perception from generation behaviors, and (iii) a rubric-based LM-as-judge evaluation framework with interpretable axes for assessing conversational quality with respect to nonverbal conversational dynamics. Across open- and closed-source vision-speech agents, we find systematic failure modes: captioning collapse and visual-stream ignorance, and we show that current systems exploit vision for explicit visual question answering but not for the streaming joint audiovisual grounding required in natural conversation. We further evaluate cascaded speech-to-avatar systems and find that their architecture fundamentally precludes the production of full-duplex nonverbal cues. As the first benchmark for full-duplex AV2AV interaction, VideoFDB establishes a foundation for systematic evaluation and, we hope, will accelerate the advancement and development of next-generation multimodal conversational agents.
匹配关键词: speech synthesis
---

[ACADEMIC - ARXIV]
标题: Native Audio-Visual Alignment for Generation
作者: Longbin Ji, Guan Wang, Xuan Wei, Chenye Yang, Xiangrui Liu, Zhenyu Zhang, Shuohuan Wang, Yu Sun, Jingzhou He
链接: https://arxiv.org/abs/2605.30073v1
完整摘要: Joint audio-video generation aims to synthesize temporally synchronized and semantically coherent visual-acoustic content. However, existing open-source methods mainly rely on either dual-tower designs with posterior alignment or fully unified tri-modal designs that mix textual context, audio and video in one shared space. The former weakens fine-grained audio-video co-evolution, while the latter couples semantic conditioning with low-level synchronization. To address these limitations, we propose NAVA, a Native Audio-Visual Alignment framework for joint audio-video generation. NAVA is built upon context-conditioned native audio-visual alignment: it first establishes audio-video correspondence in a dedicated interaction space, and then uses external context to condition the joint denoising process. Specifically, NAVA is instantiated with an Align-then-Fuse MMDiT architecture, which transitions from modality-aware audio-video alignment to modality-shared joint denoising. Furthermore, we introduce Timbre-in-Context Conditioning to associate reference timbre cues with corresponding speech spans to achieve controllable speech timbre. Experiments on Verse-Bench and Seed-TTS, together with a user study, demonstrate that NAVA achieves superior video quality, precise audio-visual synchronization, competitive audio quality, and stronger reference-timbre controllability using only 6.3B parameters.
匹配关键词: TTS
---

[ACADEMIC - ARXIV]
标题: MELD: Mel-Spectrogram-Based Speech Language Modeling with Discrete Latent Variables
作者: Sung-Lin Yeh, Wei Zhou, Gil Keren, Duc Le, Zhong Meng, Hao Tang, Jay Mahadeokar, Ozlem Kalinli, Alexandre Mourachko
链接: https://arxiv.org/abs/2605.29859v1
完整摘要: Recent speech language models rely on encoders that are optimized separately from autoregressive models. Since these encoders are unaware of the downstream objectives, the extracted representations may not be optimal for downstream tasks. To address this limitation, we introduce a discrete latent variable model on mel spectrograms that jointly optimizes the encoder and the speech language model. Joint optimization not only brings improvements over codec-based and other mel-spectrogram-based baselines on zero-shot Text-to-Speech (TTS) and Speech-to-Text (STT) tasks, but also effectively alleviates common issues in autoregressive mel-spectrogram modeling, such as prolonged silence generation and word omissions.
匹配关键词: TTS
---

[ACADEMIC - ARXIV]
标题: Beyond Attack Success Rate: Temporal Logit Observability for LLM Safety Failures
作者: Junyoung Park, Sunghwan Park, Seongyong Ju, Jaewoo Lee
链接: https://arxiv.org/abs/2605.29629v1
完整摘要: Attack Success Rate (ASR) evaluates each jailbreak with a single yes/no label at the end of generation, telling us whether a failure happened but not how it unfolded. Two attacks that produce equally harmful outputs may have followed completely different paths, and ASR cannot tell them apart. We make those hidden paths observable from logits alone. Temporal Logit Observability (TLO) is a training-free diagnostic that watches a compliance-refusal margin during decoding and places each model-attack condition on a calibrated 2D plane. By design, this plane is most informative exactly where ASR is least informative: among attacks that succeed for genuinely different reasons. Across four aligned LLMs and three jailbreak paradigms, attacks with nearly identical ASR land at clearly different points on the plane: the same model can fail through different temporal patterns. The geometry matches refusal-direction probes from hidden states on most conditions, with one model showing the limit of our fixed-lexicon approach. A simple early-stop rule derived from TLO cuts successful jailbreaks by more than half, without false alarms on plain benign queries. Safety evaluation should report when and how a failure unfolds, not only whether it occurred. TLO makes the first two observable from logits alone.
匹配关键词: ASR
---

[ACADEMIC - ARXIV]
标题: Decoding Strategies for Diffusion-Based ASR: A Systematic Evaluation of Confidence-Based Thresholding
作者: Jeong Hun Yeo, Minsu Kim, Hyeongseop Rha, Yong Man Ro
链接: https://arxiv.org/abs/2605.29613v1
完整摘要: While LLM-based Automatic Speech Recognition (ASR) achieves high accuracy, its speed is limited by sequential autoregressive decoding. Diffusion Language Models (DLMs) offer a parallel alternative, yet their decoding strategies remain under-explored in ASR contexts. This paper analyzes three decoding schemes for DLM-based ASR: fixed-number, static confidence threshold, and dynamic confidence threshold. We propose measuring round-wise accuracy using Negative Log-Likelihood-based uncertainty as a proxy for decoding progress. Our results show that both threshold-based strategies significantly outperform fixed-number schemes in accuracy and speed. We attribute this to a property unique to ASR: most tokens reach high confidence early, allowing reliable ones to be harvested aggressively while leaving only difficult tokens for later rounds. Notably, the static-threshold strategy matches the accuracy of autoregressive decoding while offering superior efficiency.
匹配关键词: ASR
---

[ACADEMIC - ARXIV]
标题: Towards Human-Like Interactive Speech Recognition With Agentic Correction and Semantic Evaluation
作者: Zixuan Jiang, Yanqiao Zhu, Peng Wang, Qinyuan Chen, Xinjian Zhao, Xipeng Qiu, Wupeng Wang, Zhifu Gao, Xiangang Li, Kai Yu, Xie Chen
链接: https://arxiv.org/abs/2605.29430v1
完整摘要: Automatic speech recognition (ASR) is a core component of human--computer interaction and an increasingly important front-end for LLM-based assistants and agents. However, most current ASR systems still follow a single-pass paradigm, which is poorly aligned with human communication, where misunderstandings are resolved through iterative clarification and refinement. This mismatch makes it difficult to correct meaning-critical errors once they occur. Meanwhile, token-level metrics such as WER or CER cannot adequately reflect such a problem. To address these limitations, we formulate \emph{Interactive ASR} as a multi-turn refinement task and propose \textbf{Agentic ASR}, a closed-loop framework that combines a single-pass ASR front-end with semantic correction, intent routing, and reasoning-based editing. We further introduce the \textbf{Sentence-level Semantic Error Rate} ($S^2ER$), an LLM-based semantic evaluation metric, together with an \textbf{Interactive Simulation System} for scalable and reproducible benchmarking. Experiments on multilingual, named-entity-intensive, and code-switching benchmarks show that iterative interaction consistently reduces semantic errors, with much larger gains in $S^2ER$ than in conventional token-level metrics. Human--AI alignment and ablation studies further validate the reliability of the semantic judge and the robustness of the proposed framework. The code is available at: https://interactiveasr.github.io/ and the live demo is available at https://i-asr.sjtuxlance.com/
匹配关键词: ASR
---

[ACADEMIC - ARXIV]
标题: Harmless Yet Harmful: Neutral Prompting Attacks for Stealthy Hallucination Steering in Agent Skills
作者: Chia-Yi Hsu, Chia-Mu Yu, Chun-Ying Huang, Jun Sakuma
链接: https://arxiv.org/abs/2605.29354v1
完整摘要: LLM-powered coding agents increasingly participate in software development workflows by generating code, selecting dependencies, and producing package installation commands. This creates a new software supply chain risk: when an agent hallucinates a non-existent package, an attacker may register the hallucinated name and later compromise users who install it. Existing package hallucination attacks and defenses primarily focus on naturally occurring hallucinations, targeted dependency steering, or post-hoc package validation. In this paper, we introduce \emph{Neutral Prompting Attack} (NPA), a highly stealthy attack paradigm in which semantically benign instructions, such as encouraging imagination and exhaustiveness, increase package hallucination propensity without containing explicit malicious intent. Unlike targeted dependency steering, NPA does not specify an attacker-chosen package. Instead, it shifts the model's dependency generation behavior toward more speculative package names. We evaluate NPA across multiple coding-oriented LLMs and package hallucination benchmarks. Our results show that NPA increases both \emph{Hallucination ASR} and \emph{Pip Install ASR}, changes the distribution of hallucinated package names, and evades existing static-analysis, LLM-based, and agent-based Skill defenses. These findings reveal that harmless-looking prompts can covertly manipulate hallucination behavior and create downstream software supply chain risks.
匹配关键词: ASR
---

[ACADEMIC - ARXIV]
标题: Physics Is All You Need? A Case Study in Physicist-Supervised AI Development of Scientific Software
作者: Nhat-Minh Nguyen
链接: https://arxiv.org/abs/2605.30353v1
完整摘要: Are AI agents tools, co-authors, or researchers? We present a quantified case study ($N=1$): a physicist supervising an AI coding agent (Claude Code, Sonnet and Opus models) over 12 work days and 57 sessions to build CLAX-PT, a differentiable one-loop perturbation theory module in JAX. We documented and classified 15 supervision events by intervention level. The agent resolved ten autonomously by iterating against oracle tests. Two more by the physicist's domain knowledge. The three it could not -- all evaded oracle detection -- share a common property: the agent treated symptom reduction as root-cause resolution. It spent 33 of the 57 sessions adjusting coefficients within a code architecture that could not represent the target physics, and could not re-evaluate its CLASS-PT branch choice even when prompted to reconsider; only an injected physics concept (anisotropic BAO damping) triggered the redesign. Separately, the agent committed a calibrated correction that passed all oracle tests but corresponded to no quantity in the theory, predicting wrong values at any other cosmology. The fudge factor was caught and replaced within the same session. Three supervision practices proved critical for catching what oracle tests missed: testing at diverse parameter points beyond the fiducial calibration; shared changelogs that surfaced stalled exploration across sessions; and an explicit rule against unphysical numerical patches. In this case, supervision design, not model capability, determined whether the agent's output was trustworthy. Closing the gap would require agents that propose architectural alternatives rather than optimize within a given structure, and distinguish predictive adequacy from explanatory correctness -- capabilities not exhibited here, not obviously addressed by scaling alone. [Abridged.]
匹配关键词: audio language model
---

[ACADEMIC - ARXIV]
标题: VideoMLA: Low-Rank Latent KV Cache for Minute-Scale Autoregressive Video Diffusion
作者: Hidir Yesiltepe, Jiazhen Hu, Tuna Han Salih Meral, Adil Kaan Akan, Kaan Oktay, Hoda Eldardiry, Pinar Yanardag
链接: https://arxiv.org/abs/2605.30351v1
完整摘要: Long-rollout causal video diffusion has converged on a fixed-size sliding-window KV cache, with recent progress innovating within this layout by changing which tokens occupy the window or how their positions are encoded. The per-head KV layout itself, a dominant contributor to streaming memory and latency, has been mostly left unchanged. In this paper, we present the first study of Multi-Head Latent Attention (MLA) in video diffusion. VideoMLA replaces per-head keys and values with a shared low-rank content latent and a shared decoupled 3D-RoPE positional key, reducing per-token KV memory by 92.7% at every cached layer. We further investigate why MLA succeeds in video diffusion even though the spectral assumption often used to motivate it in language models does not hold: pretrained video attention is not low-rank, with 99%-energy effective rank far above any practical latent dimension. VideoMLA retains quality at compression ratios where direct spectral approximation would predict large reconstruction error. We show that the MLA bottleneck, rather than the pretrained spectrum, determines the effective rank: both spectral and random initialization occupy nearly the full rank budget from initialization, and training preserves this budget while adapting within it. On VBench, VideoMLA matches short-horizon streaming video diffusion baselines, achieves the best overall score at long horizons among evaluated methods, and improves throughput by 1.23x on a single B200.
匹配关键词: audio language model
---

[ACADEMIC - ARXIV]
标题: DynaFLIP: Rethinking Robotics Perception via Tri-Modal-Dynamics Guided Representation
作者: Jusuk Lee, Seungjae Lee, Jonghun Shin, Hoseong Jung, Sungha Kim, Daesol Cho, H. Jin Kim, Jia-Bin Huang, Furong Huang
链接: https://arxiv.org/abs/2605.30350v1
完整摘要: Robot manipulation critically depends on perception that preserves the action-relevant aspects of a scene. Yet most robot learning pipelines are built upon visual encoders pre-trained for static recognition or vision-language alignment, leaving motion understanding to downstream policies. We introduce DynaFLIP, a dynamics-aware multimodal pre-training framework that pushes motion understanding upstream into perception. We construct image-language-3D flow triplets from heterogeneous human and robot videos, and use these triplets as training-time supervision to shape an image-only encoder. Our key idea is to encourage the three modalities to span a small simplex volume in the shared hyperspherical space -- a smaller simplex volume indicating stronger alignment. To avoid the geometric ambiguity and trivial collapse of naive volume minimization, we combine simplex-volume minimization with a cosine regularizer and a contrastive objective. Our analyses show that DynaFLIP focuses on control-relevant regions critical for manipulation. The resulting dynamics-aware representations serve as reusable visual backbones and consistently outperform baselines across diverse downstream policies, including VLAs. We validate this across diverse simulation and real-world setups, with gains reaching +22.5% under out-of-distribution scenarios. Our results suggest that robot generalization improves when visual representations are trained to encode not just what is present, but how the world changes under action.
匹配关键词: audio language model
---

[ACADEMIC - ARXIV]
标题: LLMSurgeon: Diagnosing Data Mixture of Large Language Models
作者: Yaxin Luo, Jiacheng Cui, Xiaohan Zhao, Xinyi Shang, Jiacheng Liu, Xinyue Bi, Zhaoyi Li, Zhiqiang Shen
链接: https://arxiv.org/abs/2605.30348v1
完整摘要: The pretraining data mixture of Large Language Models (LLMs) constitutes their "digital DNA", shaping model behaviors, capabilities, and failure modes. Yet this composition is rarely disclosed, making post-hoc auditing of data combination or provenance difficult. In this work, we formalize $\textbf{Data Mixture Surgery (DMS)}$: given only generated text from a target LLM, estimate the domain-level distribution of its pretraining corpus under a predefined taxonomy. We propose $\textbf{LLMSurgeon}$, a strong framework that casts DMS as an inverse problem under the label-shift assumption. Rather than directly aggregating classifier outputs, LLMSurgeon estimates a calibrated $\textit{soft}$ confusion matrix and solves a constrained inverse problem to correct systematic domain confusion and recover the latent mixture prior. To evaluate, we introduce $\textbf{LLMScan}$, a recipe-verifiable evaluation suite built from open-source LLMs with transparent pretraining mixtures. Across LLMScan, LLMSurgeon recovers domain mixtures with high fidelity under fixed protocols. Our work presents a practical, post-hoc approach for auditing the digital DNA of foundation models without access to their training data.
匹配关键词: audio language model
---

[ACADEMIC - ARXIV]
标题: AdaState: Self-Evolving Anchors for Streaming Video Generation
作者: Yusuf Dalva, Pinar Yanardag
链接: https://arxiv.org/abs/2605.30349v1
完整摘要: Autoregressive video diffusion models generate streaming video by producing frames sequentially, conditioning each chunk on previously generated content. These models are structurally anchored to the first frame: its key-value representation occupies a privileged position in the attention cache and serves as the primary scene reference throughout generation. As the cleanest and most error-free position in the cache, this anchor draws disproportionate attention, suppressing video dynamics, and locking scene composition to the initial viewpoint even as the scene naturally evolves. The result is a temporally shallow video in which motion, camera movement, and scene progression are dampened in favor of static consistency. To address this, we replace the static anchor with an adaptive state, a hidden latent that the model denoises alongside content at every chunk but never renders. Rather than referencing a frozen first frame, the model generates its own scene anchor at each step by attending to both the previous state and the current content, producing a reference that evolves with the generated content. Unlike standard video generation, which encodes an absolute notion of time, our formulation treats time as relative: every generation step sees the same positional structure regardless of how far generation has progressed, and the state transition is identical at every chunk. Together, these properties introduce a recurrence into the generation process, where denoising serves as the transition function, and the KV cache serves as the carrier, requiring no external module. Experiments demonstrate that the adaptive state substantially improves video dynamics, enabling richer motion and natural scene progression within generated videos.
匹配关键词: audio language model
---

[ACADEMIC - ARXIV]
标题: VideoMLA: Low-Rank Latent KV Cache for Minute-Scale Autoregressive Video Diffusion
作者: Hidir Yesiltepe, Jiazhen Hu, Tuna Han Salih Meral, Adil Kaan Akan, Kaan Oktay, Hoda Eldardiry, Pinar Yanardag
链接: https://arxiv.org/abs/2605.30351v1
完整摘要: Long-rollout causal video diffusion has converged on a fixed-size sliding-window KV cache, with recent progress innovating within this layout by changing which tokens occupy the window or how their positions are encoded. The per-head KV layout itself, a dominant contributor to streaming memory and latency, has been mostly left unchanged. In this paper, we present the first study of Multi-Head Latent Attention (MLA) in video diffusion. VideoMLA replaces per-head keys and values with a shared low-rank content latent and a shared decoupled 3D-RoPE positional key, reducing per-token KV memory by 92.7% at every cached layer. We further investigate why MLA succeeds in video diffusion even though the spectral assumption often used to motivate it in language models does not hold: pretrained video attention is not low-rank, with 99%-energy effective rank far above any practical latent dimension. VideoMLA retains quality at compression ratios where direct spectral approximation would predict large reconstruction error. We show that the MLA bottleneck, rather than the pretrained spectrum, determines the effective rank: both spectral and random initialization occupy nearly the full rank budget from initialization, and training preserves this budget while adapting within it. On VBench, VideoMLA matches short-horizon streaming video diffusion baselines, achieves the best overall score at long horizons among evaluated methods, and improves throughput by 1.23x on a single B200.
匹配关键词: KV cache
---

[ACADEMIC - ARXIV]
标题: AdaState: Self-Evolving Anchors for Streaming Video Generation
作者: Yusuf Dalva, Pinar Yanardag
链接: https://arxiv.org/abs/2605.30349v1
完整摘要: Autoregressive video diffusion models generate streaming video by producing frames sequentially, conditioning each chunk on previously generated content. These models are structurally anchored to the first frame: its key-value representation occupies a privileged position in the attention cache and serves as the primary scene reference throughout generation. As the cleanest and most error-free position in the cache, this anchor draws disproportionate attention, suppressing video dynamics, and locking scene composition to the initial viewpoint even as the scene naturally evolves. The result is a temporally shallow video in which motion, camera movement, and scene progression are dampened in favor of static consistency. To address this, we replace the static anchor with an adaptive state, a hidden latent that the model denoises alongside content at every chunk but never renders. Rather than referencing a frozen first frame, the model generates its own scene anchor at each step by attending to both the previous state and the current content, producing a reference that evolves with the generated content. Unlike standard video generation, which encodes an absolute notion of time, our formulation treats time as relative: every generation step sees the same positional structure regardless of how far generation has progressed, and the state transition is identical at every chunk. Together, these properties introduce a recurrence into the generation process, where denoising serves as the transition function, and the KV cache serves as the carrier, requiring no external module. Experiments demonstrate that the adaptive state substantially improves video dynamics, enabling richer motion and natural scene progression within generated videos.
匹配关键词: KV cache
---

[ACADEMIC - ARXIV]
标题: Efficient Test-Time Finetuning of LLMs via Convex Reconstruction and Gradient Caching
作者: Alaa Khamis, Alaa Maalouf
链接: https://arxiv.org/abs/2605.30337v1
完整摘要: Test-time finetuning (TTFT) is a rapidly evolving paradigm that adapts a language model to each prompt by retrieving related sequences, updating the model on them, and then evaluating the prompt. However, TTFT is only practical if it is fast: selection and finetuning both happen per query, making each a direct bottleneck. Existing methods trade speed for quality: fast retrieval is often redundant, while stronger diversity-aware selection adds prohibitive per-query cost. We introduce HullFT, a geometric approach to TTFT that addresses both bottlenecks. Given a query, HullFT first represents the query embedding as a sparse convex combination of few training sequences, using efficient projection-free Frank-Wolfe optimization. This yields a support set that is inherently relevant and diverse. We then convert the fractional convex weights into an exact integer multiset for finetuning through a geometric integerization procedure. The resulting multiplicities naturally create repeated examples, which we exploit with Gradient Reuse to amortize forward-backward computation across repeated finetuning steps. Our experiments show that HullFT improves the quality-efficiency tradeoff over current state-of-the-art TTFT methods, achieving lower bits-per-byte at substantially lower total runtime.
匹配关键词: KV cache
---

[ACADEMIC - ARXIV]
标题: Selective QA over Conflicting Multi-Source Personal Memory: A Diagnostic Testbed and Method Comparison
作者: Tiancheng Yang, Matthias Schonlau, Ilia Sucholutsky
链接: https://arxiv.org/abs/2605.30087v1
完整摘要: Emerging personal AI agents are moving toward persistent, multi-source memory. This creates an evaluation problem: systems must decide how to use conflicting or incomplete evidence; they cannot just retrieve facts from one clean history. Existing benchmarks rarely show whether an error came from the evidence given to a method or from the method's conflict-resolution step. We study this as selective QA over conflicting multi-source personal memory: systems answer based on conflicting, sometimes incomplete sources, or abstain when evidence is insufficient. We develop a benchmark containing 18 question templates across 8 reasoning types, 480 personas, 4 random seeds, and 34,560 instances, with controlled source distortions and deterministic ground truth. We evaluate the performance of baselines without access to any source, access to a single source, structured fusion methods, and frontier LLMs. The best trained fusion resolver reaches 80.3% accuracy, while the strongest prompt-only LLM baseline reaches 70.0%. With abstention, the same resolver reaches 85.3% selective accuracy at 78.3% coverage and the best LLM reaches 71.0% selective accuracy at 95.4% coverage. Different models have different strengths across reasoning types. We release the data, code, cached model outputs, and data-generating process for reuse.
匹配关键词: KV cache
---

[ACADEMIC - ARXIV]
标题: Future Forcing: Future-aware Training-free KV Cache Policy for Autoregressive Video Generation
作者: Jiayi Luo, Qiyan Liu, Tengyang Wang, JunHao Liu, Jiayu Chen, Cong Wang, Hanxin Zhu, Chen Gao, Xiaobin Hu, Qingyun Sun, Zhibo Chen
链接: https://arxiv.org/abs/2605.30083v1
完整摘要: Autoregressive (AR) video generation has emerged as a promising paradigm for long-horizon video synthesis, where each frame is generated conditioned on previously generated tokens. To accelerate inference, the KV cache is used to avoid redundant recomputation across generation steps. Nevertheless, its growth with generation length introduces increasing memory and error accumulation, limiting the scalability of AR models to even longer sequences. Existing KV cache compression methods mitigate this issue by selectively retaining only video tokens deemed important. However, most existing methods assess token importance using short-horizon signals derived from the current or historical generation context, making these methods prone to overlooking tokens that appear unimportant at early steps but later become critical for future frames. In this work, we identify an important property of trained AR video models: although RoPE-modulated queries evolve across autoregressive steps, the underlying canonical pre-RoPE query distribution remains remarkably stable throughout the video generation process. This approximate stationarity implies that future query distributions are estimable from historical statistics, enabling principled future-aware cache decisions without any additional training. Building on this insight, we propose Future Forcing, a training-free future-aware KV cache policy for AR video generation. Specifically, Future Forcing first constructs a future query proxy from historical statistics, then scores KV cache tokens by their importance under this proxy, and finally merges redundant token pairs within the affine subspace induced by the future query. Extensive experiments show that Future Forcing improves long-horizon consistency under limited KV caches, achieving up to 1.49 improvement in subject consistency on VBench-Long for 60s generation over existing AR video KV cache policies.
匹配关键词: KV cache
---

[ACADEMIC - ARXIV]
标题: From GPS Points to Travel Patterns: Flexible and Semantic Trajectory Generation with LLMs
作者: Silin Zhou, Chenhao Wang, Yuntao Wen, Shuo Shang, Lisi Chen, Panos Kalnis
链接: https://arxiv.org/abs/2605.30014v1
完整摘要: Urban trajectories play a crucial role in modeling urban dynamics and supporting various smart city applications. However, privacy concerns restrict access to large-scale and high-quality trajectory datasets. Trajectory generation provides a promising alternative by synthesizing realistic data to mitigate privacy risks. However, existing methods fail to explicitly capture travel patterns and can only generate fixed-length trajectories under a single condition. To address these limitations, we propose \textbf{HTP}, which \textbf{H}ierarchically generates \textbf{T}ravel patterns first and then generates GPS \textbf{P}oints by using large language models (LLMs), rather than directly generating GPS points. We first design a trajectory-specific residual quantization variational autoencoder (RQ-VAE) that quantizes micro-level GPS trajectories into compact, macro-level travel pattern tokens in a coarse-to-fine manner. These tokens capture rich segment spatial irregularities, such as point density variations caused by traffic conditions. Then, we extend the LLM vocabulary with travel pattern tokens to align trajectory representations with the LLM input, and apply supervised fine-tuning (SFT) to align the LLM with the trajectory generation task, enabling generation of travel pattern sequences under various conditions. Extensive experiments on two real-world datasets show that HTP outperforms the strongest baseline by an average of 29.78\% in terms of generation quality. Our code is available at https://github.com/slzhou-xy/HTP.
匹配关键词: quantization
---

[ACADEMIC - ARXIV]
标题: HARP: Hadamard-Preconditioned Adaptive Rotation Processor for Extreme LLM Quantization
作者: Artur Zagitov, Gleb Molodtsov, Aleksandr Beznosikov
链接: https://arxiv.org/abs/2605.29843v1
完整摘要: Post-training quantization (PTQ) is essential for deploying LLMs under memory and bandwidth constraints. However, extreme low-bit quantization remains highly sensitive to activation outliers and anisotropic weight curvature. Existing incoherence-based PTQ methods mitigate this issue with fixed randomized Hadamard transforms (RHTs), which improve quantization robustness but cannot adapt the rotated basis to the layer, calibration distribution, or quantizer. We introduce HARP (Hadamard-preconditioned Adaptive Rotation Processor), a learnable structured two-sided orthogonal processor that replaces fixed Hadamard mixing while preserving exact full-precision equivalence. HARP represents each rotation as a product of sparse butterfly-like block-orthogonal stages, supports non-power-of-two dimensions via Mixed-Radix schedules, and initializes to the RHT processor up to a fixed permutation. Fitted only on calibration data, HARP adapts the quantization basis to each layer and backend. Across 2-4 bit settings on models ranging from 1B to 70B parameters, HARP improves perplexity and zero-shot accuracy over fixed RHT. Importantly, HARP preserves deployment efficiency, reaching 128 tok/s versus 61 tok/s for FP16.
匹配关键词: quantization
---

[ACADEMIC - ARXIV]
标题: LFQ: Logit-aware Final-block Quantization for Boosting the Generation Quality of Low-Bit Quantized LLMs
作者: Jung Hyun Lee, June Yong Yang, Jungwook Choi, Eunho Yang
链接: https://arxiv.org/abs/2605.29756v1
完整摘要: As large language models continue to scale, low-bit weight-only post-training quantization (PTQ) offers a practical solution to their memory-efficient deployment. Although block-wise PTQ is capable of matching the full-precision (FP) baseline on basic language modeling and understanding, its quality is degraded for generative tasks -- especially at longer responses and extended chains of thought, which is critical in boosting task accuracy. We attribute this shortfall to two factors: (i) the omission of the unembedding layer (the LM head) in block-wise optimization and (ii) the reliance on the mean squared error (MSE) objective. Both factors cause the token probability distribution of the quantized model to misalign with that of the FP model, yielding notable accuracy drops on text generation benchmarks. To rectify the discrepancy, we introduce Logit-aware Final-block Quantization (LFQ), a simple yet effective enhancement to block-wise PTQ that quantizes the final Transformer block by minimizing the cross-entropy between the logits of the FP model and those of its quantized counterpart. By aligning token probabilities at the logit level in the final block, LFQ consistently improves the accuracy of complex generation tasks over state-of-the-art block-wise PTQ across diverse model families, while maintaining parity with FP baselines on language modeling and understanding.
匹配关键词: quantization
---

[ACADEMIC - ARXIV]
标题: BitTP: The Lightweight Trajectory Prediction Model with BitLLM for Edge-Devices
作者: Mincheol Kang, Hyunjin Lim, Bomin Kang, Daehee Park
链接: https://arxiv.org/abs/2605.29705v1
完整摘要: Trajectory prediction is a fundamental task for autonomous systems, requiring complex reasoning about multi-agent interactions and intents. Large language models (LLMs) have recently been adopted for this task, as they provide strong contextual reasoning and interpretable, language-based trajectory representations. However, these LLM-based predictors are extremely memory- and compute-intensive, making them difficult to deploy on resource-constrained edge devices such as on-board computers in autonomous robots. To bridge this gap, we propose BitTP, which converts an LLM-based trajectory predictor into a lightweight bitlinear architecture. We demonstrate that weight-only quantization to 1.58-bit (BitTP-Weight) is optimal. Crucially, activations must remain in full precision, as quantizing them leads to severe degradation and instability in spatio-temporal reasoning. Empirically, BitTP-Weight not only preserves but improves prediction quality over the full-precision (BF16) LLM baseline, reducing ADE by 14.29% and FDE by 20.97% on average, while simultaneously reducing memory usage and inference latency relative to other quantization methods. These results demonstrate that carefully designed quantization acts as an effective regularizer, enabling the practical deployment of sophisticated LLM-based reasoning on edge devices. Code is available at: https://github.com/MintCat98/BitTP.
匹配关键词: quantization
---

[ACADEMIC - ARXIV]
标题: Matching Rates and Optimal Allocation for Federated Probe-Logit Distillation under Heterogeneous Bandwidth Budgets
作者: Prasanjit Dubey, Xiaoming Huo
链接: https://arxiv.org/abs/2605.29642v1
完整摘要: In federated language modeling, $K$ nodes each hold $n$ samples but cannot pool data or exchange full-precision gradients or weights. We study the minimax rate at which a conditional distribution over $V$ tokens can be estimated when each node may upload at most $B$ bits per query in a public probe set. In federated probe-logit distillation (FPLD), each node transmits a scalar-quantized logit vector on the probe set, and an aggregator distills a global parametric student. Prior work (Dubey and Huo, 2026) establishes a high-probability KL rate $O(d/(Kn) + ρ\sqrt{V \log V / m} + K^{-1} \cdot 2^{-2B/V})$ plus optimization slack, with the bandwidth term in its trace-sharpened form. Whether this bandwidth-term rate is tight, and how the upper bound generalizes to heterogeneous per-node bandwidths, are left open. We close both gaps. First, the dithered FPLD construction has a matching single-round lower bound $Ω(K^{-1} \cdot 2^{-2B/V})$ under non-degeneracy, pinning the bandwidth-axis rate at $Θ(K^{-1} \cdot 2^{-2B/V})$. $T$-round sequential refinement with nested/scaled residual quantizers achieves $O(K^{-1} \cdot 2^{-2TB/V})$; vanilla FPLD's $T$-independent bandwidth term is suboptimal for every $T > 1$. Second, we establish a heterogeneous-bandwidth upper bound for per-node budgets $B_i$, paired with a closed-form optimal allocation $B_i^* = B_{\mathrm{tot}}/K + (V/2) \log_2(w_i / \bar{w}_g)$, a log-tilted water-filling rule that is the per-node analogue of reverse water-filling for distortion-rate optimization. A plug-in adaptive variant estimates the weights from a short warm-up phase and attains $1 + O(\sqrt{\log(K/δ)/(m T_0)})$ relative suboptimality. Synthetic n-gram simulations confirm that empirical KL is bracketed by the upper and lower bounds and that the optimal allocation strictly dominates uniform and inverse-weighted baselines under heterogeneous clipping.
匹配关键词: quantization
---

[ACADEMIC - ARXIV]
标题: NeuROK: Generative 4D Neural Object Kinematics
作者: Chen Geng, Guangzhao He, Yue Gao, Yunzhi Zhang, Shangzhe Wu, Jiajun Wu
链接: https://arxiv.org/abs/2605.30347v1
完整摘要: Data-driven approaches have revolutionized 3D vision, enabling transformers to effectively reconstruct and generate static 3D objects. However, generating simulative 4D dynamics -- realistic temporal deformations of static objects under various physical conditions -- remains challenging and often ad hoc, despite its importance in building comprehensive 3D world models. Most existing methods assume a predefined physical model and use system identification to estimate parameters, restricting these methods to specific categories and small-scale datasets. We propose that these restrictions can be overcome by learning a data-driven kinematic state parameterization for object-centric physical systems. Specifically, we learn both a latent space representing all possible states of the object and a decoder that maps any sampled latent to a plausibly deformed shape of the object. We refer to this parameterization as Neural Object Kinematics (NeuROK), and learn a transformer-based encoder-decoder model on a curated large-scale 4D dataset. This formulation and the learned model significantly simplify the generation of simulative dynamics since we only need to consider the dynamics within a low-dimensional latent space from the Lagrangian mechanics' perspective in classical physics. We demonstrate the effectiveness and generality of this neural simulation framework across diverse dynamic object types, showing clear advantages over prior works. Project page: https://chen-geng.com/neurok
匹配关键词: speculative decoding
---

[ACADEMIC - ARXIV]
标题: Archon: A Unified Multimodal Model for Holistic Digital Human Generation
作者: Chong Bao, Shichen Liu, Lijun Yu, David Futschik, Stylianos Moschoglou, Shefali Srivastava, Ziqian Bai, Feitong Tan, Guofeng Zhang, Zhaopeng Cui, Sean Fanello, Yinda Zhang
链接: https://arxiv.org/abs/2605.30311v1
完整摘要: Digital humans are fundamental to immersive interaction, yet creating a unified model for holistic modalities, including text, audio, motion, and visual content, remains an open challenge. In this paper, we present Archon, a fully pretrained, human-centric unified multimodal model for holistic avatar generation. Archon unifies seven modalities with modality-specific tokenizers, and a native autoregressive unified multimodal model pretrained on synchronized modalities and 72 diverse tasks to model holistic joint distributions. To address the token explosion challenge in high-fidelity talking videos, we introduce a memory-efficient semantic video reparameterization, achieving 4x token reduction while preserving fine-grained dynamics, coupled with a semantic-driven video diffusion decoder. We further propose a "Thinking in Modality" that decomposes ambiguous cross-modal tasks into stepwise thinking in an alternative chain of modality, progressively enhancing fidelity and controllability. Extensive experiments demonstrate that Archon achieves superior or comparable performance across diverse digital human generation tasks, validating the effectiveness of our unified framework. Project page: https://zju3dv.github.io/archon/.
匹配关键词: speculative decoding
---

[ACADEMIC - ARXIV]
标题: Qwen-VLA: Unifying Vision-Language-Action Modeling across Tasks, Environments, and Robot Embodiments
作者: Qiuyue Wang, Mingsheng Li, Jian Guan, Jinhui Ye, Sicheng Xie, Yitao Liu, Junhao Chen, Zhixuan Liang, Jie Zhang, Xintong Hu, Xuhong Huang, Pei Lin, Junyang Lin, Dayiheng Liu, Shuai Bai, Jingren Zhou, Jiazhao Zhang, Haoqi Yuan, Gengze Zhou, Hang Yin, Ye Wang, Yiyang Huang, Zixing Lei, Wujian Peng, Delin Chen, Yingming Zheng, Jingyang Fan, Xianwei Zhuang, Xin Zhou, Haoyang Li, Anzhe Chen, Tong Zhang, Xuejing Liu, Yuchong Sun, Ruizhe Chen, Zhaohai Li, Chenxu Lü, Zhibo Yang, Tao Yu, Xionghui Chen
链接: https://arxiv.org/abs/2605.30280v1
完整摘要: Embodied intelligence is often studied through specialized models for individual tasks such as manipulation or navigation, resulting in fragmented capabilities and limited generalization across tasks, environments, and robot embodiments. In this work, we study whether heterogeneous embodied decision-making problems can be unified within a single vision-language-action model. We present Qwen-VLA, a unified embodied foundation model that extends Qwen's vision-language modeling stack from perception, understanding, and reasoning to continuous action and trajectory generation through a DiT-based action decoder. Qwen-VLA is trained with a large-scale joint pretraining recipe over diverse data sources, including robotics manipulation trajectories, human egocentric demonstrations, synthetic simulation data, vision-and-language navigation data, trajectory-centric supervision, and auxiliary vision-language data. To support multiple robot platforms, we introduce embodiment-aware prompt conditioning, where robot-specific textual descriptions specify the current embodiment and control convention. We further cast manipulation, navigation, and trajectory prediction into a unified action-and-trajectory prediction framework, enabling transferable visual grounding, spatial reasoning, and continuous action generation across robot morphologies, task families, and environments. Experiments on manipulation, navigation, and trajectory-centric benchmarks show consistent multi-task performance and out-of-distribution generalization under variations in scene layout, background, lighting, object configuration, and robot embodiment. Qwen-VLA-Instruct achieves 97.9% on LIBERO, 73.7% on Simpler-WidowX, 86.1%/87.2% on RoboTwin-Easy/Hard, 69.0% OSR on R2R, 59.6% SR on RxR, 76.9% average OOD success in real-world ALOHA experiments, and 26.6% zero-shot success on DOMINO dynamic manipulation.
匹配关键词: speculative decoding
---

[ACADEMIC - ARXIV]
标题: How LoRA Remembers? A Parametric Memory Law for LLM Finetuning
作者: Ziwen Xu, Haiwen Hong, Linsong Yu, Benglei Cui, Longtao Huang, Hui Xue, Ningyu Zhang
链接: https://arxiv.org/abs/2605.30260v1
完整摘要: Large Language Models (LLMs) must continuously learn and update knowledge to remain effective in dynamic real-world environments. While Low-Rank Adaptation (LoRA) is widely used for such memory updates, existing studies mainly rely on qualitative downstream evaluations, leaving the quantitative capacity limits and underlying dynamics of exact parametric memory largely unexplored. To bridge this gap, we employ LoRA as a controlled memory capacity probe within the latent space to systematically quantify exact parametric memory. We introduce the Parametric Memory Law, a robust power law linking loss reduction Delta L to effective parameters and sequence length. At the token level, fine-grained analysis reveals a deterministic phase transition, demonstrating that a prediction probability of p > 0.5 constitutes a sufficient condition for verbatim recall under greedy decoding. Driven by these insights, we introduce MemFT, a threshold-guided optimization strategy that dynamically redistributes the training budget toward sub-threshold tokens. Empirical evaluations demonstrate that MemFT can enhance memory fidelity and efficiency. Code will be released at https://github.com/zjunlp/ParametricMemoryLaw.
匹配关键词: speculative decoding
---

[ACADEMIC - ARXIV]
标题: MarginGate: Sparse Margin-Triggered Verification for Batch-Invariant LLM Inference
作者: Kexin Chu, Yang Zhou, Wei Zhang
链接: https://arxiv.org/abs/2605.30218v1
完整摘要: Temperature-zero BF16 LLM inference is often treated as reproducible, yet the same request can emit different tokens when decoded alone or inside a larger batch. Existing fixes use batch-invariant operators or LLM-42's per-token verification, incurring cost even when most steps are stable. We ask whether verification can be applied exclusively to flipped tokens. Across five models, batch-induced token flips are sparse on the flip-rate benchmarks: on MATH500, Llama-3.1-8B flips on $0.48\%$ of synchronous decode steps, and all tested models stay within the 0.3-1.3% range on MATH500, GSM8K, and HumanEval. K/V perturbations remain flat before flips, while low top-1/top-2 logit margins expose much of the flip risk. MarginGate turns these observations into a verifier policy: it keeps BF16 decoding on high-margin steps, verifies only low-margin steps, and repairs confirmed mismatches by replacing the current K/V column. We evaluate on four datasets, calibrating on MATH500 and transferring to GSM8K, SharedGPT, and HumanEval. MarginGate restores 100% sequence-level deterministic decoding on Llama-3.1-8B and Qwen2.5-14B with 18.56%/15.05% verifier trigger rates, reducing LLM-42's latency increment by 2.23x/1.99x relative to always-on verification. On DSR1-Distill-Qwen-7B, the same policy reaches determinism in a harder regime at 49.50% triggers.
匹配关键词: speculative decoding
---

[ACADEMIC - ARXIV]
标题: Physics Is All You Need? A Case Study in Physicist-Supervised AI Development of Scientific Software
作者: Nhat-Minh Nguyen
链接: https://arxiv.org/abs/2605.30353v1
完整摘要: Are AI agents tools, co-authors, or researchers? We present a quantified case study ($N=1$): a physicist supervising an AI coding agent (Claude Code, Sonnet and Opus models) over 12 work days and 57 sessions to build CLAX-PT, a differentiable one-loop perturbation theory module in JAX. We documented and classified 15 supervision events by intervention level. The agent resolved ten autonomously by iterating against oracle tests. Two more by the physicist's domain knowledge. The three it could not -- all evaded oracle detection -- share a common property: the agent treated symptom reduction as root-cause resolution. It spent 33 of the 57 sessions adjusting coefficients within a code architecture that could not represent the target physics, and could not re-evaluate its CLASS-PT branch choice even when prompted to reconsider; only an injected physics concept (anisotropic BAO damping) triggered the redesign. Separately, the agent committed a calibrated correction that passed all oracle tests but corresponded to no quantity in the theory, predicting wrong values at any other cosmology. The fudge factor was caught and replaced within the same session. Three supervision practices proved critical for catching what oracle tests missed: testing at diverse parameter points beyond the fiducial calibration; shared changelogs that surfaced stalled exploration across sessions; and an explicit rule against unphysical numerical patches. In this case, supervision design, not model capability, determined whether the agent's output was trustworthy. Closing the gap would require agents that propose architectural alternatives rather than optimize within a given structure, and distinguish predictive adequacy from explanatory correctness -- capabilities not exhibited here, not obviously addressed by scaling alone. [Abridged.]
匹配关键词: kernel optimization
---

[ACADEMIC - ARXIV]
标题: REST3D: Reconstructing Physically Stable 3D Scenes from a Single Image
作者: Xiaoxuan Ma, Jiashun Wang, Nicolas Ugrinovic, Yehonathan Litman, Kris Kitani
链接: https://arxiv.org/abs/2605.30338v1
完整摘要: Reconstructing physically stable 3D scenes from a single RGB image enables casual images to be converted into simulation-ready digital assets for applications such as immersive interaction and content creation. However, existing single-image reconstruction methods fall short in capturing the physical structure of a scene. As a result, they often produce geometrically plausible but physically inconsistent results, including object floating and penetration, which lead to unstable behavior in physics simulations. Image-conditioned scene generation methods improve physical plausibility but often rely on strong scene priors, yielding plausible yet inaccurate object arrangements that fail to match the input image. We propose REST3D, a single-image reconstruction framework that can reconstruct physically stable 3D scenes by integrating physical scene understanding with physics-constrained refinement. We first introduce an agentic physical scene understanding technique that constructs a scene-tree representation capturing object physical states and inter-object relationships from a gravity-support perspective, providing a structural prior for reconstruction. Leveraging this structure, we initialize the scene using image-to-3D models, followed by scene-tree-guided alignment and physics-constrained optimization to resolve physical violations while preserving visual consistency with the input image. Experiments show that our method significantly reduces physical errors and improves simulation stability on both synthetic and real-world datasets while maintaining strong reconstruction quality. We further demonstrate the reconstructed scenes in VR-based human-object interaction, showing their potential for immersive applications.
匹配关键词: kernel optimization
---

[ACADEMIC - ARXIV]
标题: Efficient Test-Time Finetuning of LLMs via Convex Reconstruction and Gradient Caching
作者: Alaa Khamis, Alaa Maalouf
链接: https://arxiv.org/abs/2605.30337v1
完整摘要: Test-time finetuning (TTFT) is a rapidly evolving paradigm that adapts a language model to each prompt by retrieving related sequences, updating the model on them, and then evaluating the prompt. However, TTFT is only practical if it is fast: selection and finetuning both happen per query, making each a direct bottleneck. Existing methods trade speed for quality: fast retrieval is often redundant, while stronger diversity-aware selection adds prohibitive per-query cost. We introduce HullFT, a geometric approach to TTFT that addresses both bottlenecks. Given a query, HullFT first represents the query embedding as a sparse convex combination of few training sequences, using efficient projection-free Frank-Wolfe optimization. This yields a support set that is inherently relevant and diverse. We then convert the fractional convex weights into an exact integer multiset for finetuning through a geometric integerization procedure. The resulting multiplicities naturally create repeated examples, which we exploit with Gradient Reuse to amortize forward-backward computation across repeated finetuning steps. Our experiments show that HullFT improves the quality-efficiency tradeoff over current state-of-the-art TTFT methods, achieving lower bits-per-byte at substantially lower total runtime.
匹配关键词: kernel optimization
---

[ACADEMIC - ARXIV]
标题: Fairness-Aware Federated Learning with Trajectory Shapley Value
作者: Daniel Kuznetsov, Ziqi Wang
链接: https://arxiv.org/abs/2605.30336v1
完整摘要: Federated learning is an emerging distributed paradigm that addresses the challenges posed by heterogeneous, privacy-sensitive data. It enables multiple clients to train a model collaboratively by aggregating their local updates at a server. However, conventional aggregation schemes typically use fixed weights that fail to reflect unequal and time-varying client contributions, leading to biased and unstable learning. To improve fairness and stability, we propose the Trajectory Shapley Value (TSV), a contribution metric that evaluates how each client influences the optimization trajectory of the global model using a validation-based, temporally consistent utility. Building on TSV, we design FedTSV, an adaptive aggregation method that converts per-round evaluations into dynamic client weights, allowing the server to respond to heterogeneous and adversarial participation in real time. Experiments on benchmark datasets show that FedTSV accelerates convergence, improves robustness, and yields more equitable contribution assessments, thereby providing a principled foundation for fairness-aware federated optimization.
匹配关键词: kernel optimization
---

[ACADEMIC - ARXIV]
标题: Demystifying Data Organization for Enhanced LLM Training
作者: Yalun Dai, Yangyu Huang, Tongshen Yang, Yonghan Wang, Xin Zhang, Wenshan Wu, Qihao Zhao, Hao Li, Yuanyuan Gao, Kim-Hui Yap, Scarlett Li
链接: https://arxiv.org/abs/2605.30334v1
完整摘要: Large Language Models (LLMs) have revolutionized various fields, yet their training efficiency is heavily reliant on effective data curation. While data selection has been widely studied, the strategic data organization for enhanced training remains an underexplored area, particularly since current LLMs are often trained for only one or a few epochs. This paper systematically explores the influence of data organization on LLM training by reusing pre-computed sample-level scores originally generated for data efficiency, thereby incurring minimal additional computational overhead. We identify and formalize four key guidelines for optimizing data organization: Boundary Sharpening, Cyclic Scheduling, Curriculum Continuity, and Local Diversity. Guided by them, we introduce two novel data ordering methods termed STR and SAW. Extensive experiments across different model scales and data sizes, encompassing both pre-training and SFT stages, validate the effectiveness of our summarized guidelines. They also demonstrate the robustness of our proposed data ordering methods in enhancing the stability and performance of LLM training. Github Link: https://github.com/microsoft/data-efficacy/
匹配关键词: kernel optimization
---

[ACADEMIC - ARXIV]
标题: VideoMLA: Low-Rank Latent KV Cache for Minute-Scale Autoregressive Video Diffusion
作者: Hidir Yesiltepe, Jiazhen Hu, Tuna Han Salih Meral, Adil Kaan Akan, Kaan Oktay, Hoda Eldardiry, Pinar Yanardag
链接: https://arxiv.org/abs/2605.30351v1
完整摘要: Long-rollout causal video diffusion has converged on a fixed-size sliding-window KV cache, with recent progress innovating within this layout by changing which tokens occupy the window or how their positions are encoded. The per-head KV layout itself, a dominant contributor to streaming memory and latency, has been mostly left unchanged. In this paper, we present the first study of Multi-Head Latent Attention (MLA) in video diffusion. VideoMLA replaces per-head keys and values with a shared low-rank content latent and a shared decoupled 3D-RoPE positional key, reducing per-token KV memory by 92.7% at every cached layer. We further investigate why MLA succeeds in video diffusion even though the spectral assumption often used to motivate it in language models does not hold: pretrained video attention is not low-rank, with 99%-energy effective rank far above any practical latent dimension. VideoMLA retains quality at compression ratios where direct spectral approximation would predict large reconstruction error. We show that the MLA bottleneck, rather than the pretrained spectrum, determines the effective rank: both spectral and random initialization occupy nearly the full rank budget from initialization, and training preserves this budget while adapting within it. On VBench, VideoMLA matches short-horizon streaming video diffusion baselines, achieves the best overall score at long horizons among evaluated methods, and improves throughput by 1.23x on a single B200.
匹配关键词: memory efficiency
---

[ACADEMIC - ARXIV]
标题: Tiny but Trusted: Efficient Vision-Language Reasoning for Time-Series Anomaly Detection
作者: Xiaona Zhou, Muntasir Wahed, Tianjiao Yu, Constantin Brif, Ismini Lourentzou
链接: https://arxiv.org/abs/2605.30344v1
完整摘要: Recent advances in Vision-Language Models (VLMs) have achieved impressive performance across many tasks, yet prior studies report unsatisfactory performance when applying large language or multimodal models to finding abnormal patterns in sequential data. Public anomaly detection benchmarks typically provide interval annotations but not natural-language rationales, making it difficult to fine-tune VLMs to produce grounded, interpretable decisions. To address this gap, we construct VisAnomBench, a curated benchmark built from public time-series datasets and augmented with high-quality anomaly explanations selected from multiple large VLMs using fine-grained, task-specific rewards. Through fine-tuning on this benchmark, we develop VisAnomReasoner, a parameter-efficient VLM for time-series anomaly detection. Experimental results on VisAnomBench show that VisAnomReasoner achieves more accurate anomaly localization and consistently outperforms all baselines, with improvements of at least 21.23 and 23.87 percentage points in precision and F1, respectively. Additional experiments on the TSB-AD-U benchmark demonstrate strong cross-benchmark generalization, with VisAnomReasoner improving precision and F1 by 9.57 and 13.39 percentage points, respectively.
匹配关键词: memory efficiency
---

[ACADEMIC - ARXIV]
标题: Unlocking the Working Memory of Large Language Models for Latent Reasoning
作者: Lukas Aichberger, Sepp Hochreiter
链接: https://arxiv.org/abs/2605.30343v1
完整摘要: To improve the reasoning capabilities of large language models, test-time compute is typically scaled by generating intermediate tokens before the final answer. However, this couples reasoning to autoregressive generation and thereby conflates internal computation with external communication. In contrast, human cognition can use working memory to hold and manipulate information internally without the need to externalize intermediate thoughts. Drawing on this principle, we introduce Reasoning in Memory (RiM), a latent reasoning method that replaces the autoregressive generation of reasoning steps with memory blocks. These memory blocks are fixed sequences of special tokens that unlock the working-memory capacity of large language models. Since they are fixed rather than generated, they can be processed in a single forward pass, enabling compute-efficient latent reasoning. To operationalize these memory blocks, we employ a two-stage curriculum. First, we ground them by predicting explicit reasoning steps after each memory block. Second, we discard this step-level supervision and iteratively refine the final answer after each memory block. Our experiments on reasoning benchmarks show that, across language models of different families and sizes, RiM matches or exceeds existing latent reasoning methods while avoiding the autoregressive generation of thoughts. These results demonstrate that large language models can be trained to use working memory as an effective mechanism for latent reasoning.
匹配关键词: memory efficiency
---

[ACADEMIC - ARXIV]
标题: Uncertainty-driven 3D Gaussian Splatting Active Mapping via Anisotropic Visibility Field
作者: Shangjie Xue, Jesse Dill, Dhruv Ahuja, Frank Dellaert, Panagiotis Tsiotras, Danfei Xu
链接: https://arxiv.org/abs/2605.30342v1
完整摘要: We present Gaussian Splatting Anisotropic Visibility Field (GAVIS), a novel framework for uncertainty quantification and active mapping in 3DGS. Our key insight is that regions unseen from the training views yield unreliable predictions from the 3DGS. To address this, we introduce a principled and efficient method for quantifying the visibility field in 3DGS, defined as the anisotropic visibility of each particle with respect to the training views, and represented using spherical harmonics. The resulting visibility field is integrated into a Bayesian Network-based uncertainty-aware 3DGS rasterizer, enabling real-time (200 FPS) uncertainty quantification for synthesized views. Active mapping is further performed within a maximum information gain framework building on this formulation. Extensive experiments across diverse environments demonstrate that GAVIS consistently and significantly outperforms prior approaches in both accuracy and efficiency. Moreover, beyond standalone use, our method can be applied post-hoc to improve the performance of existing approaches.
匹配关键词: memory efficiency
---

[ACADEMIC - ARXIV]
标题: Efficient Test-Time Finetuning of LLMs via Convex Reconstruction and Gradient Caching
作者: Alaa Khamis, Alaa Maalouf
链接: https://arxiv.org/abs/2605.30337v1
完整摘要: Test-time finetuning (TTFT) is a rapidly evolving paradigm that adapts a language model to each prompt by retrieving related sequences, updating the model on them, and then evaluating the prompt. However, TTFT is only practical if it is fast: selection and finetuning both happen per query, making each a direct bottleneck. Existing methods trade speed for quality: fast retrieval is often redundant, while stronger diversity-aware selection adds prohibitive per-query cost. We introduce HullFT, a geometric approach to TTFT that addresses both bottlenecks. Given a query, HullFT first represents the query embedding as a sparse convex combination of few training sequences, using efficient projection-free Frank-Wolfe optimization. This yields a support set that is inherently relevant and diverse. We then convert the fractional convex weights into an exact integer multiset for finetuning through a geometric integerization procedure. The resulting multiplicities naturally create repeated examples, which we exploit with Gradient Reuse to amortize forward-backward computation across repeated finetuning steps. Our experiments show that HullFT improves the quality-efficiency tradeoff over current state-of-the-art TTFT methods, achieving lower bits-per-byte at substantially lower total runtime.
匹配关键词: memory efficiency
---

[ACADEMIC - ARXIV]
标题: Physics Is All You Need? A Case Study in Physicist-Supervised AI Development of Scientific Software
作者: Nhat-Minh Nguyen
链接: https://arxiv.org/abs/2605.30353v1
完整摘要: Are AI agents tools, co-authors, or researchers? We present a quantified case study ($N=1$): a physicist supervising an AI coding agent (Claude Code, Sonnet and Opus models) over 12 work days and 57 sessions to build CLAX-PT, a differentiable one-loop perturbation theory module in JAX. We documented and classified 15 supervision events by intervention level. The agent resolved ten autonomously by iterating against oracle tests. Two more by the physicist's domain knowledge. The three it could not -- all evaded oracle detection -- share a common property: the agent treated symptom reduction as root-cause resolution. It spent 33 of the 57 sessions adjusting coefficients within a code architecture that could not represent the target physics, and could not re-evaluate its CLASS-PT branch choice even when prompted to reconsider; only an injected physics concept (anisotropic BAO damping) triggered the redesign. Separately, the agent committed a calibrated correction that passed all oracle tests but corresponded to no quantity in the theory, predicting wrong values at any other cosmology. The fudge factor was caught and replaced within the same session. Three supervision practices proved critical for catching what oracle tests missed: testing at diverse parameter points beyond the fiducial calibration; shared changelogs that surfaced stalled exploration across sessions; and an explicit rule against unphysical numerical patches. In this case, supervision design, not model capability, determined whether the agent's output was trustworthy. Closing the gap would require agents that propose architectural alternatives rather than optimize within a given structure, and distinguish predictive adequacy from explanatory correctness -- capabilities not exhibited here, not obviously addressed by scaling alone. [Abridged.]
匹配关键词: agent
---

[ACADEMIC - ARXIV]
标题: SchGen: PCB Schematic Generation with Semantic-Grounded Code Representations
作者: Qinpei Luo, Ruichun Ma, Xinyu Zhang, Lili Qiu
链接: https://arxiv.org/abs/2605.30345v1
完整摘要: Printed circuit board (PCB) schematic design defines nearly all electronic hardware, but it remains manual and expertise-intensive. While generative AI has advanced digital and analog IC design, PCB schematic generation from natural-language intent is largely unexplored. This paper presents SchGen, the first large language model that generates editable PCB schematics from natural-language requests. The key challenge lies in the lack of an LLM-suited representation and a large-scale dataset. Current schematic formats are dominated by verbose, tool-specific syntax and geometry-heavy descriptions, making them difficult to generate reliably. We introduce a semantically grounded code representation that encodes schematic editing primitives with relative placement and pin-name-based wiring, transforming a geometry-driven generation problem into a semantics-driven matching task amenable to LLMs. We further construct a large-scale dataset of PCB schematics paired with user prompts via a human-agent collaborative pipeline that converts open-source hardware designs into our representation. Experiments show that SchGen significantly outperforms alternative representations and even larger general-purpose LLMs on wire connectivity accuracy and functional correctness. Our results highlight the critical role of representation design in enabling generative models for complex hardware design tasks.
匹配关键词: agent
---

[ACADEMIC - ARXIV]
标题: REST3D: Reconstructing Physically Stable 3D Scenes from a Single Image
作者: Xiaoxuan Ma, Jiashun Wang, Nicolas Ugrinovic, Yehonathan Litman, Kris Kitani
链接: https://arxiv.org/abs/2605.30338v1
完整摘要: Reconstructing physically stable 3D scenes from a single RGB image enables casual images to be converted into simulation-ready digital assets for applications such as immersive interaction and content creation. However, existing single-image reconstruction methods fall short in capturing the physical structure of a scene. As a result, they often produce geometrically plausible but physically inconsistent results, including object floating and penetration, which lead to unstable behavior in physics simulations. Image-conditioned scene generation methods improve physical plausibility but often rely on strong scene priors, yielding plausible yet inaccurate object arrangements that fail to match the input image. We propose REST3D, a single-image reconstruction framework that can reconstruct physically stable 3D scenes by integrating physical scene understanding with physics-constrained refinement. We first introduce an agentic physical scene understanding technique that constructs a scene-tree representation capturing object physical states and inter-object relationships from a gravity-support perspective, providing a structural prior for reconstruction. Leveraging this structure, we initialize the scene using image-to-3D models, followed by scene-tree-guided alignment and physics-constrained optimization to resolve physical violations while preserving visual consistency with the input image. Experiments show that our method significantly reduces physical errors and improves simulation stability on both synthetic and real-world datasets while maintaining strong reconstruction quality. We further demonstrate the reconstructed scenes in VR-based human-object interaction, showing their potential for immersive applications.
匹配关键词: agent
---

[ACADEMIC - ARXIV]
标题: Locally Coherent, Globally Incoherent: Bounding Compositional Incoherence in Multi-Component LLM Agents
作者: Anany Kotawala
链接: https://arxiv.org/abs/2605.30335v1
完整摘要: Multi-component LLM agents assemble probabilistic claims from components that each see only part of a joint problem; the composition can violate basic probability axioms even when every component is locally coherent. We formalise this locally coherent, globally incoherent failure via the compositional residual eps*, the L2 distance from the composed quote to the joint coherent polytope, computable at runtime from system output and the declared cross-component coupling constraints. A product-structure dichotomy characterises when local coherence suffices, and a Rayleigh-quotient prediction matches the observed residual within 7% on three of four relation classes. A hierarchical Boyle-Dykstra projection repairs the composition deterministically; an anytime-valid e-process gives sequential coherence monitoring. Across 1,876 ensemble cliques on a four-LLM mid-tier panel (frontier-panel rerun in Section 5.5), eps* > 0 on 33-94% of cliques, translating to +0.115 nats per bet of regret on 1,770 resolved bets under the proportional allocation rule (the gain collapses to +0.006 under bettors that themselves coherentise). Three intuitive LLM-side mitigations(retrieval, partition-aware prompting, aggregator-LLM) each fail or regress.
匹配关键词: agent
---

[ACADEMIC - ARXIV]
标题: SoundnessBench: Can Your AI Scientist Really Tell Good Research Ideas from Bad Ones?
作者: Sy-Tuyen Ho, Minghui Liu, Huy Nghiem, Furong Huang
链接: https://arxiv.org/abs/2605.30329v1
完整摘要: Autonomous AI research agents aim to accelerate scientific discovery by automating the research pipeline, from hypothesis generation to peer review. However, existing benchmarks rarely test a fundamental bottleneck: whether Large Language Models can judge the methodological viability of a research idea before expending time and computational resources. We introduce SoundnessBench, a curated benchmark of 1,099 machine-learning research proposals reconstructed from ICLR submissions, labeled with reviewer soundness sub-scores, and audited against source papers. SoundnessBench should be interpreted as a benchmark for recoverable proposal-stage soundness rather than exact prediction of full-paper review outcomes. Across 12 frontier LLMs, we find a pervasive optimism bias: under standard prompting, models frequently rate low-soundness proposals as sound, while aggressive prompting largely shifts errors from false positives to false negatives. Additional controls for public-corpus contamination, paper-identifying phrases, surface features, and human audit quality suggest that this behavior is not explained by a single confounder. Our results indicate that current LLMs are not yet reliable as standalone first-gate evaluators for scientific rigor.
匹配关键词: agent
---

[ACADEMIC - ARXIV]
标题: Physics Is All You Need? A Case Study in Physicist-Supervised AI Development of Scientific Software
作者: Nhat-Minh Nguyen
链接: https://arxiv.org/abs/2605.30353v1
完整摘要: Are AI agents tools, co-authors, or researchers? We present a quantified case study ($N=1$): a physicist supervising an AI coding agent (Claude Code, Sonnet and Opus models) over 12 work days and 57 sessions to build CLAX-PT, a differentiable one-loop perturbation theory module in JAX. We documented and classified 15 supervision events by intervention level. The agent resolved ten autonomously by iterating against oracle tests. Two more by the physicist's domain knowledge. The three it could not -- all evaded oracle detection -- share a common property: the agent treated symptom reduction as root-cause resolution. It spent 33 of the 57 sessions adjusting coefficients within a code architecture that could not represent the target physics, and could not re-evaluate its CLASS-PT branch choice even when prompted to reconsider; only an injected physics concept (anisotropic BAO damping) triggered the redesign. Separately, the agent committed a calibrated correction that passed all oracle tests but corresponded to no quantity in the theory, predicting wrong values at any other cosmology. The fudge factor was caught and replaced within the same session. Three supervision practices proved critical for catching what oracle tests missed: testing at diverse parameter points beyond the fiducial calibration; shared changelogs that surfaced stalled exploration across sessions; and an explicit rule against unphysical numerical patches. In this case, supervision design, not model capability, determined whether the agent's output was trustworthy. Closing the gap would require agents that propose architectural alternatives rather than optimize within a given structure, and distinguish predictive adequacy from explanatory correctness -- capabilities not exhibited here, not obviously addressed by scaling alone. [Abridged.]
匹配关键词: tool use
---

[ACADEMIC - ARXIV]
标题: VideoMLA: Low-Rank Latent KV Cache for Minute-Scale Autoregressive Video Diffusion
作者: Hidir Yesiltepe, Jiazhen Hu, Tuna Han Salih Meral, Adil Kaan Akan, Kaan Oktay, Hoda Eldardiry, Pinar Yanardag
链接: https://arxiv.org/abs/2605.30351v1
完整摘要: Long-rollout causal video diffusion has converged on a fixed-size sliding-window KV cache, with recent progress innovating within this layout by changing which tokens occupy the window or how their positions are encoded. The per-head KV layout itself, a dominant contributor to streaming memory and latency, has been mostly left unchanged. In this paper, we present the first study of Multi-Head Latent Attention (MLA) in video diffusion. VideoMLA replaces per-head keys and values with a shared low-rank content latent and a shared decoupled 3D-RoPE positional key, reducing per-token KV memory by 92.7% at every cached layer. We further investigate why MLA succeeds in video diffusion even though the spectral assumption often used to motivate it in language models does not hold: pretrained video attention is not low-rank, with 99%-energy effective rank far above any practical latent dimension. VideoMLA retains quality at compression ratios where direct spectral approximation would predict large reconstruction error. We show that the MLA bottleneck, rather than the pretrained spectrum, determines the effective rank: both spectral and random initialization occupy nearly the full rank budget from initialization, and training preserves this budget while adapting within it. On VBench, VideoMLA matches short-horizon streaming video diffusion baselines, achieves the best overall score at long horizons among evaluated methods, and improves throughput by 1.23x on a single B200.
匹配关键词: tool use
---

[ACADEMIC - ARXIV]
标题: DynaFLIP: Rethinking Robotics Perception via Tri-Modal-Dynamics Guided Representation
作者: Jusuk Lee, Seungjae Lee, Jonghun Shin, Hoseong Jung, Sungha Kim, Daesol Cho, H. Jin Kim, Jia-Bin Huang, Furong Huang
链接: https://arxiv.org/abs/2605.30350v1
完整摘要: Robot manipulation critically depends on perception that preserves the action-relevant aspects of a scene. Yet most robot learning pipelines are built upon visual encoders pre-trained for static recognition or vision-language alignment, leaving motion understanding to downstream policies. We introduce DynaFLIP, a dynamics-aware multimodal pre-training framework that pushes motion understanding upstream into perception. We construct image-language-3D flow triplets from heterogeneous human and robot videos, and use these triplets as training-time supervision to shape an image-only encoder. Our key idea is to encourage the three modalities to span a small simplex volume in the shared hyperspherical space -- a smaller simplex volume indicating stronger alignment. To avoid the geometric ambiguity and trivial collapse of naive volume minimization, we combine simplex-volume minimization with a cosine regularizer and a contrastive objective. Our analyses show that DynaFLIP focuses on control-relevant regions critical for manipulation. The resulting dynamics-aware representations serve as reusable visual backbones and consistently outperform baselines across diverse downstream policies, including VLAs. We validate this across diverse simulation and real-world setups, with gains reaching +22.5% under out-of-distribution scenarios. Our results suggest that robot generalization improves when visual representations are trained to encode not just what is present, but how the world changes under action.
匹配关键词: tool use
---

[ACADEMIC - ARXIV]
标题: NeuROK: Generative 4D Neural Object Kinematics
作者: Chen Geng, Guangzhao He, Yue Gao, Yunzhi Zhang, Shangzhe Wu, Jiajun Wu
链接: https://arxiv.org/abs/2605.30347v1
完整摘要: Data-driven approaches have revolutionized 3D vision, enabling transformers to effectively reconstruct and generate static 3D objects. However, generating simulative 4D dynamics -- realistic temporal deformations of static objects under various physical conditions -- remains challenging and often ad hoc, despite its importance in building comprehensive 3D world models. Most existing methods assume a predefined physical model and use system identification to estimate parameters, restricting these methods to specific categories and small-scale datasets. We propose that these restrictions can be overcome by learning a data-driven kinematic state parameterization for object-centric physical systems. Specifically, we learn both a latent space representing all possible states of the object and a decoder that maps any sampled latent to a plausibly deformed shape of the object. We refer to this parameterization as Neural Object Kinematics (NeuROK), and learn a transformer-based encoder-decoder model on a curated large-scale 4D dataset. This formulation and the learned model significantly simplify the generation of simulative dynamics since we only need to consider the dynamics within a low-dimensional latent space from the Lagrangian mechanics' perspective in classical physics. We demonstrate the effectiveness and generality of this neural simulation framework across diverse dynamic object types, showing clear advantages over prior works. Project page: https://chen-geng.com/neurok
匹配关键词: tool use
---

[ACADEMIC - ARXIV]
标题: SchGen: PCB Schematic Generation with Semantic-Grounded Code Representations
作者: Qinpei Luo, Ruichun Ma, Xinyu Zhang, Lili Qiu
链接: https://arxiv.org/abs/2605.30345v1
完整摘要: Printed circuit board (PCB) schematic design defines nearly all electronic hardware, but it remains manual and expertise-intensive. While generative AI has advanced digital and analog IC design, PCB schematic generation from natural-language intent is largely unexplored. This paper presents SchGen, the first large language model that generates editable PCB schematics from natural-language requests. The key challenge lies in the lack of an LLM-suited representation and a large-scale dataset. Current schematic formats are dominated by verbose, tool-specific syntax and geometry-heavy descriptions, making them difficult to generate reliably. We introduce a semantically grounded code representation that encodes schematic editing primitives with relative placement and pin-name-based wiring, transforming a geometry-driven generation problem into a semantics-driven matching task amenable to LLMs. We further construct a large-scale dataset of PCB schematics paired with user prompts via a human-agent collaborative pipeline that converts open-source hardware designs into our representation. Experiments show that SchGen significantly outperforms alternative representations and even larger general-purpose LLMs on wire connectivity accuracy and functional correctness. Our results highlight the critical role of representation design in enabling generative models for complex hardware design tasks.
匹配关键词: tool use
---

[ACADEMIC - ARXIV]
标题: Before the Shutter: Aesthetic and Actionable Portrait Photography Planning in 3D Scenes
作者: Ruixiang Jiang, Chang Wen Chen
链接: https://arxiv.org/abs/2605.30318v1
完整摘要: Portrait photography is largely decided before the shutter opens: the subject's pose, the camera configuration, and the lighting devices must be coordinated within the surrounding 3D scene. In contrast, most existing computational methods focus on post-production in 2D image space, such as retouching, relighting, or editing images that already exist; pre-capture photographic planning remains largely unexplored. We introduce 3D aesthetic portrait planning, the task of generating human pose, camera, lighting, and exposure plans that produce visually compelling portraits while satisfying geometric and photometric feasibility in a 3D scene. Our approach builds a Photographic Scene Graph that represents scene affordances, subject-scene relations, and portrait-relevant lighting structure. Built on this representation, we perform aesthetic-guided comparative planning over previous attempts and current viewfinder observations. Experiments across diverse indoor and outdoor scenes show that our method produces portraits preferred by human raters and MLLM evaluators over competitive baselines, while maintaining high physical plausibility. Together, our results suggest a path from post-capture correction toward pre-capture computational portrait planning. Project repository: https://github.com/songrise/Before-the-Shutter
匹配关键词: planning
---

[ACADEMIC - ARXIV]
标题: Knowing What to Solve Before How: Preplan Empowered LLM Mathematical Reasoning
作者: Shaojie Wang, Liang Zhang
链接: https://arxiv.org/abs/2605.30245v1
完整摘要: Current plan-based reasoning methods improve large language models (LLMs) by inserting a planning stage before execution, giving rise to the question $\rightarrow$ plan $\rightarrow$ cot paradigm. While effective, a closer examination reveals an inherent paradigm-level gap: both the planning and its execution stages decide how to solve a problem, while the prior question of what to solve; recognizing the problem type, the applicable tools, and the foreseeable pitfalls; remains entirely implicit. To bridge this gap, we propose PPC (Preplan-Plan-CoT), a framework that introduces an explicit problem-understanding stage, the preplan, yielding a new question $\rightarrow$ preplan $\rightarrow$ plan $\rightarrow$ cot paradigm. Realizing this paradigm requires safeguarding the conceptual integrity of preplan at both ends. Specifically, we design a three-stage synthesis pipeline with a spoiler-score detector that filters out leakage and spoiler failures to build clean preplan supervision, and a composite GRPO reward enforces that the generated plan genuinely follows from the preplan. Experiments across four backbones and five mathematical reasoning benchmarks show that PPC achieves the best results on 39 of 40 metrics, improving maj@16 and pass@16 by +2.23 and +3.06 over the strongest baseline without introducing additional inference token overhead.
匹配关键词: planning
---

[ACADEMIC - ARXIV]
标题: GRASP: Plan-Guided Graph Retrieval with Adaptive Fusion and Reranking on Semi-Structured Knowledge Bases
作者: Yicheng Tao, Yiqun Wang, Xiangchen Song, Xin Luo, Kai Liu, Jie Liu
链接: https://arxiv.org/abs/2605.30237v1
完整摘要: Semi-structured knowledge bases (SKBs) embed textual documents in a typed graph of entities and relations, and underpin applications such as product search, academic paper search, and precision-medicine inquiries. Existing hybrid retrieval systems on SKBs either use the graph only for query expansion, mix textual and structural branches under a global weighting, or rely on fine-tuned graph-traversal generators. We present GRASP, a three-stage SKB retrieval framework unifying plan-based graph retrieval, plan-conditioned fusion with a dense retriever, and a fine-tuned reranker over the fused candidates. GRASP substantially advances the state of the art on every metric across the three STaRK benchmarks, lifting average Hit@1 from 62.0 to 73.9. Ablation and sensitivity studies further confirm the effectiveness and robustness of GRASP.
匹配关键词: planning
---

[ACADEMIC - ARXIV]
标题: Mean-Field Diffuser: Scaling Offline MARL to Thousands of Agents
作者: Wenhao Li, Xiangfeng Wang, Bo Jin
链接: https://arxiv.org/abs/2605.30190v1
完整摘要: Diffusion-based planning has achieved strong results in single-agent offline reinforcement learning, yet scaling to many-agent systems remains intractable due to the curse of dimensionality in the joint trajectory space. We introduce MF-Diffuser, a framework that lifts trajectory planning to the Wasserstein space of trajectory distributions, where the propagation of chaos ensures a small representative subset of agents captures the full population dynamics. Our approach features a value-weighted chaotic entropy objective that reconciles generative fidelity with return maximization, and a hierarchical coarse-to-fine strategy that progressively grows the agent population during denoising. We establish end-to-end suboptimality bounds with four interpretable terms, revealing that mean-field approximation error scales as $O(H^2/\sqrt{N})$ while offline distribution shift provably does not grow with population size $N$, and prove the generated policy is an approximate mean-field Nash equilibrium with explicit convergence guarantees. Experiments on three mean-field RL benchmarks -- spanning stage games, sequential dynamics, and adversarial team competition -- show MF-Diffuser achieves the best return in the majority of settings, with the largest gains on suboptimal offline data and at extreme scales ($N \geq 10^3$).
匹配关键词: planning
---

[ACADEMIC - ARXIV]
标题: Anchorless Diversification for Parallel LLM Ideation
作者: Fares Nabil Ibrahim, Nafis Saami Azad, Raiyan Abdul Baten
链接: https://arxiv.org/abs/2605.30150v1
完整摘要: LLMs are increasingly used to generate candidate-idea pools for creative tasks where broad exploration is valuable. Parallel inference can be attractive in this setting when it broadens the pool while retaining quality and cost efficiency. We study inference-time controls for candidate-pool diversification, asking whether anchorless methods can rival methods that depend on observed seed ideas. Across three creative task families, we compare independent generation and semantic direction stratification with self-, peer-, and representative-anchor baselines, under neutral and population-referential divergent instructions. Population-referential divergence is a strong low-cost baseline, increasing semantic diversity while preserving quality proxies. Semantic direction stratification is stronger: a single planning call organizes generations across broad semantic directions, yielding the best diversity--quality--compute frontier. Anchored regeneration can be strong in final-pool diversity, but its advantage shrinks under full-pipeline token accounting. These results establish practical anchorless baselines for open-ended LLM ideation.
匹配关键词: planning
---

[ACADEMIC - ARXIV]
标题: In-Context Reward Adaptation for Robust Preference Modeling
作者: Zhenyu Sun, Zheng Xu, Ermin Wei
链接: https://arxiv.org/abs/2605.30323v1
完整摘要: Reinforcement Learning from Human Feedback (RLHF) typically relies on static reward models to align Large Language Models with human preferences. However, human values are inherently diverse and heterogeneous, and a single reward model often lacks the robustness required to generalize to unseen preference domains. While existing multi-reward frameworks attempt to address this, they are often restricted to a fixed set of known domains and fail to adapt to unseen human distributions without costly retraining. In this work, we propose In-Context Reward Adaptation, a transformer-based framework designed to model diverse and unseen human preferences on the fly. By leveraging the in-context learning capabilities of transformers, our approach adaptively infers the underlying reward structure from a small set of preference demonstrations. We demonstrate that while a standard transformer architecture is insufficient for this task by characterizing an asymptotic bias to the ground-truth, incorporating human response time as an auxiliary input signal enables the model to successfully adapt to preferences from previously unseen domains. Our findings show that this approach provides a more robust foundation for preference modeling, allowing for the representation of heterogeneous rewards and preference distribution shift, and offering a scalable path toward more flexible human-AI alignment.
匹配关键词: RLHF
---

[ACADEMIC - ARXIV]
标题: LLUMI: Improving LLM Writing Assistance for Mental Health Support with Online Community Feedback
作者: Jiwon Kim, Maya Ajit, Sherry Gong, Soorya Ram Shimgekar, Dong Whi Yoo, Eshwar Chandrasekharan, Koustuv Saha
链接: https://arxiv.org/abs/2605.30273v1
完整摘要: Large language models (LLMs) show promise in generating supportive responses for mental health queries, but improving their usefulness, empathy, and safety often requires substantial compute, expert input, and labeled data. At the same time, deploying proprietary, cloud-based models for mental health-related interactions raises important privacy and data-governance concerns, given the sensitivities. To address this challenge, we introduce LLUMI setup that can be hosted in-house within protected environments. LLUMI consists of two complementary components: a generation model (GM), which drafts supportive responses to mental health queries, and an improvement model (IM), which revises an initial human-crafted response. We leverage feedback signals from Reddit mental health communities, using community endorsement patterns such as upvotes and downvotes to construct chosen-rejected response pairs for Supervised Fine Tuning (SFT) and Direct Preference Optimization (DPO). We further align LLUMI using human evaluation across five dimensions: readability, empathy, connection, actionability, and safety. Our results show that, despite relying on smaller open-source models rather than proprietary cloud-based GPT models, LLUMI achieves comparable performance across linguistic analyses and human evaluations. These findings suggest that open-source models, when trained with community-derived preference signals, can support high-quality mental health support assistance while offering a more privacy-preserving alternative for sensitive support contexts.
匹配关键词: DPO
---

[ACADEMIC - ARXIV]
标题: Recovering Diversity Without Losing Alignment: A DPO Recipe for Post-Trained LLMs
作者: Vinay Samuel, Yapei Chang, Mohit Iyyer
链接: https://arxiv.org/abs/2605.30021v1
完整摘要: Many open-ended instructions have multiple valid answers that users can benefit from seeing, but post-training often narrows an LLM's output space toward a small set of canonical responses. We introduce REDIPO, an offline DPO data-construction pipeline for recovering distinct valid answer modes while preserving the alignment benefits of the instruct model. For each prompt, REDIPO samples responses from both base and instruct models, rewrites base-model responses with the instruct model, filters candidates for safety and instruction-following quality, and builds preference pairs that favor marginally diverse responses among candidates with similar instruction-following reward. Across Qwen3-4B, OLMo-3-7B, and LLaMA-3.1-8B, REDIPO improves NoveltyBench distinct_k by 134%, 33%, and 44% relative to the instruct checkpoints, while DivPO changes diversity by 0%, -6%, and -4% on the same models. These gains largely maintain MTBench, IFEval, and Arena-Hard performance, and reduce direct-category HarmBench attack success rate. Ablations show that marginal-diversity pair selection and base-response rewriting drive the diversity gains, while filtering and quality-bounded pairing help maintain alignment. Overall, our results show that diverse valid answers from base-model generations can be reintroduced through carefully constructed preference data while retaining the alignment benefits of post-training. We release our code and data at https://github.com/vsamuel2003/RiDiPO.
匹配关键词: DPO
---

[ACADEMIC - ARXIV]
标题: CoHyDE: Iterative Co-Training of LLM Rewriter & Dense Encoder for Tool Retrieval
作者: Vaishali Senthil, Ashutosh Hathidara, Sebastian Schreiber
链接: https://arxiv.org/abs/2605.29271v1
完整摘要: Tool retrieval over large API catalogs is a core bottleneck for LLM agents: user queries arrive in colloquial, often underspecified language, while the catalog uses technical API vocabulary that no fixed encoder can bridge on its own. The two dominant training approaches, contrastive encoder fine-tuning and HyDE-style query expansion with a frozen LLM, address this problem from opposite ends and fail in complementary directions: the fine-tuned encoder excels when the query's surface form already matches the catalog but collapses when it does not, while zero-shot HyDE is more robust to underspecified queries yet generates catalog-unaware hypothetical descriptions that degrade retrieval when queries are well-formed. We introduce CoHyDE, an iterative procedure that trains the dense encoder and the LLM rewriter as a single co-evolving system: the encoder is retrained with InfoNCE on catalog-style hypothetical descriptions produced by the rewriter, and the rewriter is preference-aligned via DPO against the encoder's retrieval scores, with both sides warm-started on the tool catalog before the loop begins. On a ~10k tool subset of the ToolBench catalog, three rounds of CoHyDE improve over the strongest single-component baseline by +2.5 pp NDCG@5 on standard queries and +6.3 pp on held-out vague queries, with gains as large as +8 pp on the hardest vague tier. Ablations confirm that co-training is the key ingredient: using either component in isolation fails to match CoHyDE on both well-formed and vague queries, with losses of up to -8 pp on vague queries.
匹配关键词: DPO
---

