# 破晓 PoXiao — 原始数据 (Raw Context)
生成时间: 2026-04-23 02:59 UTC
================================================================================

[RSS:Reddit LocalLLaMA (社区共识)]
Forgive my ignorance but how is a 27B model better than 397B?
https://www.reddit.com/r/LocalLLaMA/comments/1st11lp/forgive_my_ignorance_but_how_is_a_27b_model/
Is Qwen just incredibly good at doing dense and not so good at doing MoE? I get that dense is generally better than MoE but 27B being better than 397B just doesn’t sit right with me. What are those additional experts even doing then? &#32; submitted by &#32; /u/No_Conversation9561 [link] &#32; [comm
---

[RSS:Reddit LocalLLaMA (社区共识)]
Qwen 3.6 27B is out
https://www.reddit.com/r/LocalLLaMA/comments/1ssl1xh/qwen_36_27b_is_out/
https://huggingface.co/Qwen/Qwen3.6-27B &#32; submitted by &#32; /u/NoConcert8847 [link] &#32; [comments]
---

[RSS:Reddit LocalLLaMA (社区共识)]
Qwen3 TTS is seriously underrated - I got it running locally in real-time and it's one of the most expressive open TTS models I've tried
https://www.reddit.com/r/LocalLLaMA/comments/1ssugid/qwen3_tts_is_seriously_underrated_i_got_it/
Heya guys and gals, Around a year ago I released and posted about Persona Engine as a fun side project, trying to get the whole ASR -&gt; LLM -&gt; TTS pipeline going fully locally while having a realtime avatar that is lip-synced (think VTuber). I was able to achieve this and was super happy with t
---

[RSS:Reddit LocalLLaMA (社区共识)]
Dense vs. MoE gap is shrinking fast with the 3.6-27B release
https://www.reddit.com/r/LocalLLaMA/comments/1ssw45q/dense_vs_moe_gap_is_shrinking_fast_with_the_3627b/
27B Dense vs. 35B-A3B MoE): - Dense still holds the crown: It still wins out on most tasks overall. - The gap is closing: In 7 out of 10 benchmarks, the MoE model is quietly creeping up and closing the distance. - Coding is getting a massive boost: MoE is making serious strides here. For example, th
---

[RSS:Reddit LocalLLaMA (社区共识)]
Qwen3.6-27B released!
https://www.reddit.com/r/LocalLLaMA/comments/1ssl6ki/qwen3627b_released/
Meet Qwen3.6-27B, our latest dense, open-source model, packing flagship-level coding power! Yes, 27B, and Qwen3.6-27B punches way above its weight. 👇 What's new: - Outstanding agentic coding — surpasses Qwen3.5-397B-A17B across all major coding benchmarks - Strong reasoning across text &amp; multimo
---

[RSS:Reddit LocalLLaMA (社区共识)]
unsloth Qwen3.6-27B-GGUF
https://www.reddit.com/r/LocalLLaMA/comments/1ssnfdb/unsloth_qwen3627bgguf/
finally with files inside :) &#32; submitted by &#32; /u/jacek2023 [link] &#32; [comments]
---

[RSS:Reddit LocalLLaMA (社区共识)]
Qwen3.6-35B becomes competitive with cloud models when paired with the right agent
https://www.reddit.com/r/LocalLLaMA/comments/1ssilc3/qwen3635b_becomes_competitive_with_cloud_models/
A short follow-up to my previous post, where I showed that changing the scaffold around the same 9B Qwen model moved benchmark performance from 19.11% to 45.56%: https://www.reddit.com/r/LocalLLaMA/s/JMHuAGj1LV After feedback from people here, I tried little-coder with Qwen3.6 35B. It now lands in t
---

[RSS:Reddit LocalLLaMA (社区共识)]
Local manga translator with LLM build-in, written in Rust with llama.cpp integration
https://www.reddit.com/r/LocalLLaMA/comments/1sslwjv/local_manga_translator_with_llm_buildin_written/
Hi LocalLLaMA, I created a post a few weeks ago, but this time this project has become more reliable and easier to use. This is a manga translator that can also be used to translate any image. It uses a combination of object detection, visual LLM-based OCR, layout analysis, and fine-tuned inpainting
---

[RSS:Reddit LocalLLaMA (社区共识)]
Qwen3.6-27B Uncensored Aggressive is out with K_P quants!
https://www.reddit.com/r/LocalLLaMA/comments/1sstq1w/qwen3627b_uncensored_aggressive_is_out_with_k_p/
Thank you members for the heads-up - this current release doesn't live up to my standards and I was able to reproduce a breaking bug which takes it back to the drawing board. If this is on my end and not on llama.cpp - Expect a proper re-upload of the GGUF files hopefully tomorrow (middle of the nig
---

[RSS:Reddit LocalLLaMA (社区共识)]
MiMo-V2.5 Has released
https://www.reddit.com/r/LocalLLaMA/comments/1ssqkha/mimov25_has_released/
https://openrouter.ai/xiaomi/mimo-v2.5 &#32; submitted by &#32; /u/WhyLifeIs4 [link] &#32; [comments]
---

[RSS:Reddit LocalLLaMA (社区共识)]
I tested Qwen3.6-27B, Qwen3.6-35B-A3B, Qwen3.5-27B and Gemma 4 on the same real architecture-writing task on an RTX 5090
https://www.reddit.com/r/LocalLLaMA/comments/1st35c8/i_tested_qwen3627b_qwen3635ba3b_qwen3527b_and/
I ran a pretty simple but revealing local-LLM test. At first I was only going to post about the two Qwens and Gemma4 and go to bed, and what do you know, I go on reddit and see a post that Qwen 3.6-27B dropped. Oh well... Models tested: Gemma4 cyankiwi/gemma-4-31B-it-AWQ-4bit Qwen3.6-35B RedHatAI/Qw
---

[RSS:Reddit LocalLLaMA (社区共识)]
Note the new recommended sampling parameters for Qwen3.6 27B
https://www.reddit.com/r/LocalLLaMA/comments/1st5627/note_the_new_recommended_sampling_parameters_for/
Taken from their Huggingface Page: We recommend using the following set of sampling parameters for generation Thinking mode for general tasks: temperature=1.0, top_p=0.95, top_k=20, min_p=0.0, presence_penalty=0.0, repetition_penalty=1.0 Thinking mode for precise coding tasks (e.g. WebDev): temperat
---

[RSS:Reddit LocalLLaMA (社区共识)]
Tried Qwen3.6-27B-UD-Q6_K_XL.gguf with CloudeCode, well I can't believe but it is usable
https://www.reddit.com/r/LocalLLaMA/comments/1sszac8/tried_qwen3627budq6_k_xlgguf_with_cloudecode_well/
So I tried to run Qwen3-27B-UD-Q6_K_XL.gguf with 200K context on my RTX 5090 using llama.cpp. I'm getting around 50 tok/s, which is fine I guess, I don't really know this stuff so it might be improvable. But what I want to say is, I haven't tried local models for coding for quite a long time, and he
---

[RSS:Reddit LocalLLaMA (社区共识)]
Recent Open models from last 6 Months - Nov 2025 - Apr 2026
https://www.reddit.com/r/LocalLLaMA/comments/1sskmhv/recent_open_models_from_last_6_months_nov_2025/
I created this chart with recent open models from last 6 months. Few might be older than that possibly. Included only latest versions(Ex: Only Kimi-K2.6, no Kimi-K2.5 &amp; Kimi-K2. Also only GLM-5.1 &amp; GLM-4.7, no GLM-4.6 &amp; GLM-4.5). I couldn't add some models like Ling-2.5-1T, Ring-2.5-1T, 
---

[RSS:Reddit LocalLLaMA (社区共识)]
Given how good Qwen become, is it time to grab a 128gb m5 max?
https://www.reddit.com/r/LocalLLaMA/comments/1sszoo2/given_how_good_qwen_become_is_it_time_to_grab_a/
I was on the fence of updating my m1 pro 32gb, but seeing how got Qwen is becoming, isnt it the time to start experimenting with local models? My experience so far was that it never came close to opus, but i see that the 27b models are now getting close to the 4.5 opus (???), which sounds exciting! 
---

[RSS:Reddit LocalLLaMA (社区共识)]
Qwen 3.6 is actually useful for vibe-coding, and way cheaper than Claude
https://www.reddit.com/r/LocalLLaMA/comments/1st3m8y/qwen_36_is_actually_useful_for_vibecoding_and_way/
Launched claude code, pointed it at my running Qwen, and, well, it vibe codes perfectly fine. I started a project with Qwen3.6-35B-A3B (Q4) yesterday, and then this morning switched to 27B (Q8), and both worked fine! Running on a dual 3090 rig with 200k context. Running Unsloth Q_8. No fancy setup, 
---

[RSS:Reddit LocalLLaMA (社区共识)]
Tencent, Alibaba in Talks to Invest in DeepSeek at $20 Billion-Plus Valuation
https://www.reddit.com/r/LocalLLaMA/comments/1ssna1h/tencent_alibaba_in_talks_to_invest_in_deepseek_at/
https://www.reuters.com/world/asia-pacific/tencent-alibaba-talks-invest-deepseek-information-reports-2026-04-22/ &#32; submitted by &#32; /u/External_Mood4719 [link] &#32; [comments]
---

[RSS:Reddit LocalLLaMA (社区共识)]
Qwen3.6 35B + the right coding scaffold got my local setup to 9/10 on real Go tasks
https://www.reddit.com/r/LocalLLaMA/comments/1st4cqq/qwen36_35b_the_right_coding_scaffold_got_my_local/
I wanted to test a slightly different question than &quot;can one open model beat GPT-5.4 Codex?&quot; The question was: Can a combination of local models, scaffolding, repair loops, and routing policies running on home hardware get close enough to frontier coding models on my actual workload? Short
---

[RSS:Reddit LocalLLaMA (社区共识)]
What speed is everyone getting on Qwen3.6 27b?
https://www.reddit.com/r/LocalLLaMA/comments/1sss5og/what_speed_is_everyone_getting_on_qwen36_27b/
I'm getting ~13 tps on Q8_0, with a context window of 128000, K Q8_0, V Q8_0 this is on 3x GPUS (1x2060super 8gb, 2x5060ti 16gb), via llamacpp unsure if this is slow or to be expected? */llama-server --port 8080 --model */llama.cpp/Qwen3.6-27B-Q8_0/Qwen3.6-27B-Q8_0.gguf -mm */Qwen3.6-27B-Q8_0/mmproj
---

[RSS:Reddit LocalLLaMA (社区共识)]
Ultimate List: Best Open Models for Coding, Chat, Vision, Audio & More
https://www.reddit.com/r/LocalLLaMA/comments/1sseh00/ultimate_list_best_open_models_for_coding_chat/
Open-source AI is evolving insanely fast, but it’s hard to know which model is actually best for each use case. So I put together a list of the best open-source models across different categories Best Audio Generation Open Source Models Text-to-Speech (TTS) Qwen3-TTS → Best overall balance (quality 
---

[RSS:Reddit LocalLLaMA (社区共识)]
Best config for Qwen3.6 27b / llama.cpp / opencode
https://www.reddit.com/r/LocalLLaMA/comments/1ssp9kq/best_config_for_qwen36_27b_llamacpp_opencode/
Please share your best config &lt;3 Windows 2x3080 20GB VRAM, DDR4 256GB RAM , llama.ccp, On 100K filled context i have 400/11 pp/tg (My setup): &quot;A:/0_llama_server/llama-server.exe&quot; -m &quot;a:\0_LM_Studio\unsloth\Qwen3.6-27B-GGUF\Qwen3.6-27B-UD-Q5_K_XL.gguf&quot; --port 8080 --alias qwen3
---

[RSS:Reddit LocalLLaMA (社区共识)]
Qwen3.6-27B KLDs - INTs and NVFPs
https://www.reddit.com/r/LocalLLaMA/comments/1ssyukx/qwen3627b_klds_ints_and_nvfps/
https://preview.redd.it/oe958ecy6twg1.png?width=1484&amp;format=png&amp;auto=webp&amp;s=9649d1833be88ec140e2d4fb96b1a66b2bfe6522 Will do more, but here's a start, as you're chosing your models. Remember, USE-CASE is important: Notice the larger size of THoTD NVFP versus the other. This is because TH
---

[RSS:Reddit MachineLearning (学术风向)]
I can't believe text normalization is so underdiscussed in streaming text-to-speech [D]
https://www.reddit.com/r/MachineLearning/comments/1ssk7rk/i_cant_believe_text_normalization_is_so/
Kinda suprises me how little discussion there is around about mistakes in streaming TTS models People look for natural readers, high voice quality, expressive speech. And most models don't look dumb here and fail. They fail when you give them basic stuff like price, dates, URLs, promo codes, phone n
---

[RSS:Reddit MachineLearning (学术风向)]
GPU Compass – open-source, real-time GPU pricing across 20+ clouds [P]
https://www.reddit.com/r/MachineLearning/comments/1ssuuum/gpu_compass_opensource_realtime_gpu_pricing/
We maintain an open-source catalog of cloud GPU offerings (skypilot-catalog, Apache 2.0). It auto-fetches pricing from 20+ cloud APIs every 7 hours. We made it browsable - 50 GPU models, 2K+ offerings, on-demand and spot pricing, historical trends. A few other GPU comparison tools already use our ca
---

[RSS:Reddit MachineLearning (学术风向)]
INT3 compression+fused metal kernels [R]
https://www.reddit.com/r/MachineLearning/comments/1ssdt0z/int3_compressionfused_metal_kernels_r/
Hey guys, I am a researcher and solo founder. I compress models with INT3 at +0.14 nats and built a 2-bit KV cache for long-horizon tasks. I shipped both (INT3 model + INT2 KV) with custom fused Metal kernels for Mac (M-series). Currently Qwen 7B is available in preview. #install brew install reinfo
---

[RSS:Reddit MachineLearning (学术风向)]
How do you anonymize code for a conference submission? [D]
https://www.reddit.com/r/MachineLearning/comments/1ssojac/how_do_you_anonymize_code_for_a_conference/
Hi everyone, I have a question about anonymizing code for conference submissions . I’m submitting an AI/ML paper to a conference and would like to include the code , but the repository needs to be anonymized . In this situation, is it common to c reate a separate anonymous GitHub account , upload th
---

[RSS:Reddit MachineLearning (学术风向)]
EMNLP workshop any good? Or any other NLP venue good for VLM eval work? [D]
https://www.reddit.com/r/MachineLearning/comments/1ssticc/emnlp_workshop_any_good_or_any_other_nlp_venue/
My paper got rejected from an imaging venue (A*) because it lacked clinical validation and was more &quot;NLP suited&quot;. I'm very disappointed by the decision as the paper had strong methods and key findings suited to the specific venue. I'm thinking of EMNLP next, but I feel it is too NLP and my
---

[RSS:Reddit MachineLearning (学术风向)]
AI scientists produce results without reasoning scientifically [R]
https://www.reddit.com/r/MachineLearning/comments/1st02fw/ai_scientists_produce_results_without_reasoning/
Researchers ran 25,000 AI scientist experiments and discovered something that need attention!! AI scientists are producing results without doing science. 68% of times, the AI gathered evidence and then completely ignored it. 71% times the AI never updated its beliefs at all. Not once. Only 26% of th
---

[RSS:Reddit MachineLearning (学术风向)]
Need Info on quality benchmarks to run on DeepSeek V3.2 different quant levels [D]
https://www.reddit.com/r/MachineLearning/comments/1ss9sa5/need_info_on_quality_benchmarks_to_run_on/
I am looking at a product that will do runtime quant on DeepSeek V3.2. I want to measure quality loss compared to no quant. What kind of benchmarks can I run? &#32; submitted by &#32; /u/Chachachaudhary123 [link] &#32; [comments]
---

[RSS:Ars Technica AI (深度技术)]
Microsoft issues emergency update for macOS and Linux ASP.NET threat
https://arstechnica.com/security/2026/04/microsoft-issues-emergency-update-for-macos-and-linux-asp-net-threat/
When authentication fails, things can go very, very wrong.
---

[RSS:Reddit Jobs & Careers (职场动态)]
After being laid off 2.5 years ago and looking for 2 years, I finally got an offer.
https://www.reddit.com/r/cscareerquestions/comments/1ssshcx/after_being_laid_off_25_years_ago_and_looking_for/
Software engineer. I put in maybe 200 applications and had about 75 interviews. Things going against me are I'm older, looking for jobs at the highest IC level and I suck at leetcode no matter how much practice I have (I'm always given LC hards). Things going for me are strong sys design skills, str
---

[RSS:Reddit Jobs & Careers (职场动态)]
"Experienced" Software developer now finding my experience useless
https://www.reddit.com/r/cscareerquestions/comments/1st14cn/experienced_software_developer_now_finding_my/
I have been a software developer for around 9 years now - across 4 companies. I used to like coding and design discussion. Since last ~2 years, i have only been refactoring the code written by LLMs. Even system design I prepare, it feels like Gemini is able to improve after giving it more context. I
---

[RSS:Reddit Jobs & Careers (职场动态)]
Odd candidate
https://www.reddit.com/r/cscareerquestions/comments/1ssq4vw/odd_candidate/
I'm on the interviewer pool at a FAANG, and yesterday I had a weird experience with a candidate that recently graduated. I gave them my main question and they started with a plan. The plan was solid, caught all of the major corner cases. Candidate moved on to implementing it, and everything just com
---

[RSS:Reddit Jobs & Careers (职场动态)]
We need a union
https://www.reddit.com/r/cscareerquestions/comments/1ssn7om/we_need_a_union/
We need one this outsourcing is craxy &#32; submitted by &#32; /u/Parking_Anteater943 [link] &#32; [comments]
---

[RSS:Reddit Jobs & Careers (职场动态)]
So it seems lying and learning the stack is the way to go?
https://www.reddit.com/r/cscareerquestions/comments/1st15f6/so_it_seems_lying_and_learning_the_stack_is_the/
Noticing from my friends getting job that everyone is just lying about their stack and just learning as they go. Anyone else had similar success? &#32; submitted by &#32; /u/Impressive_Beyond521 [link] &#32; [comments]
---

[RSS:Reddit Jobs & Careers (职场动态)]
Letting AI do 100% coding FRIED my brain. HELP???
https://www.reddit.com/r/cscareerquestions/comments/1st0u7r/letting_ai_do_100_coding_fried_my_brain_help/
I've been vibe coding since the beginning of this year, and lately I found myself really struggling with my general cognitive skills and problem solving skills. Now I am in a dilemma: should I use the old-schooled way to study coding and advance my skillsets while ppl who don't know programming at a
---

[RSS:Reddit Jobs & Careers (职场动态)]
What's the point of engineering.
https://www.reddit.com/r/cscareerquestions/comments/1ssqpx2/whats_the_point_of_engineering/
Work at a MAANG tier software company. Starting to see mandates to allow sales PM etc to use Claude to ship actual code. Work on a team that manages a lot of publishing and access to apps etc.....and I am genuinely baffled at this point to what is software engineering. Is it just a way to QA now to 
---

[RSS:Reddit Jobs & Careers (职场动态)]
You worked in big tech, did that help you get your next job?
https://www.reddit.com/r/cscareerquestions/comments/1ssus9a/you_worked_in_big_tech_did_that_help_you_get_your/
With lay offs looming I keep being told having big tech on my resume is gold. I have my doubtsZ thoughts? &#32; submitted by &#32; /u/BountyMakesMeCough [link] &#32; [comments]
---

[RSS:Reddit Jobs & Careers (职场动态)]
Is figma still top tier tech company to work for?
https://www.reddit.com/r/cscareerquestions/comments/1ssjmtr/is_figma_still_top_tier_tech_company_to_work_for/
I don’t have a job offer or anything, just general question about tech job market. I know a while ago, the private companies that haven’t yet IPOd are generally look at as top tier companies to work for, because you can truly gain generational wealth from the IPO. Well figma IPO and their stock is i
---

[RSS:Reddit Jobs & Careers (职场动态)]
Should i start looking for a new job? Or will it look like job hopping?
https://www.reddit.com/r/cscareerquestions/comments/1ssmesk/should_i_start_looking_for_a_new_job_or_will_it/
So i am a junior. My first job lasted exactly 13 months then i was laid off. Now im on my second job and i have been here for the last 8 months now. Everything was going great until suddenly the company decided to implement a shit ton of micro management and tracking rules that is making work unbear
---

[RSS:Reddit Jobs & Careers (职场动态)]
Questions to ask potential manager?
https://www.reddit.com/r/cscareerquestions/comments/1st4k4q/questions_to_ask_potential_manager/
Got an offer and I have a chance to chat with the manager. I'm not sure I'll take the role. It's 50% more pay but seems more stressful. I'd be a senior SDE with 7 YOE. I plan to ask around: - WLB - oncalls - onboarding Anything else I should ask? How to tactfully ask about WLB...I don't want want to
---

[RSS:Reddit Jobs & Careers (职场动态)]
TIL most ATS treat implied skills and listed skills as completely different things
https://www.reddit.com/r/cscareerquestions/comments/1sswd8b/til_most_ats_treat_implied_skills_and_listed/
ATS parsers are looking for a distinct Skills section with keywords that match the job description. If you put skills inside experience bullets (i.e. &quot;built data pipelines in Python to support the home timeline team&quot;), the parser has to infer &quot;Python&quot; from context. Some ATS do th
---

[RSS:Reddit Jobs & Careers (职场动态)]
Job market - reinforcement learning (RL) roles? Should I add more research topics?
https://www.reddit.com/r/cscareerquestions/comments/1st4ez5/job_market_reinforcement_learning_rl_roles_should/
Currently a 2nd year PhD. I'm doing a job search and it seems like RL roles are rare, should I be adding another research topic in conjunction with RL during my PhD to be employable? e.g. computer vision, LLMs? I'm planning on adding Robotics by actually coding an RL algorithm for a robot, but would
---

[RSS:Reddit Jobs & Careers (职场动态)]
What do they ask in companies outside of big tech?
https://www.reddit.com/r/cscareerquestions/comments/1st3v9b/what_do_they_ask_in_companies_outside_of_big_tech/
I am specifically targeting front-end or full-stack software roles in the USA with some YOE. I know that big tech is pretty standard as to what they ask in interviews . So in that sense it’s easy to prepare. I mean interviews are still difficult but you’ll know what to expect at least. But smaller c
---

[RSS:Reddit Jobs & Careers (职场动态)]
How do you know if Research-Oriented ML roles are for you?
https://www.reddit.com/r/cscareerquestions/comments/1st0ptv/how_do_you_know_if_researchoriented_ml_roles_are/
I’m currently a first-year Master’s student in Data Science &amp; AI, and I’m trying to figure out whether a research-oriented career is right for me. So far, most of my experience has been in applied machine learning. None of my internships were formally titled “ML Engineer” or “ML Research,” but t
---

[RSS:Reddit Jobs & Careers (职场动态)]
SWE intern hiring (c/o 2027-2028)
https://www.reddit.com/r/cscareerquestions/comments/1ssrff8/swe_intern_hiring_co_20272028/
Will the current industry trend (AI/layoffs) also slow down intern hiring? I understand that direct new grad/entry roles have taken a hit, but does the same also go for interns? My assumption is that companies will still try to have some inflow of new engineers and will try to get by converting them
---

[RSS:Reddit Jobs & Careers (职场动态)]
Leave full time role for part time?
https://www.reddit.com/r/cscareerquestions/comments/1st05rm/leave_full_time_role_for_part_time/
I have been at my current company for almost two years (software developer). This is my first job out of college. I love my coworkers though. However, I have hated the actual work for about a year now. I dread going in. It takes so much mental energy just to get something done. I’ve had passive suic
---

[RSS:Reddit Jobs & Careers (职场动态)]
What would you do in this situation?
https://www.reddit.com/r/cscareerquestions/comments/1sssjur/what_would_you_do_in_this_situation/
Let's say you work remotely and they sold your office building so going back to office is not even an option. But one of the high level folks wants everyone to get together for a one week event in person for culture. They want you to fly across the country to their head office. But you're deathly af
---

[RSS:Reddit Jobs & Careers (职场动态)]
Is it worth leaving a stable $50K job to chase a $90K CS job?
https://www.reddit.com/r/cscareerquestions/comments/1ssc25b/is_it_worth_leaving_a_stable_50k_job_to_chase_a/
I graduated with a CS degree about 6 months ago. I wasn’t very motivated to apply for software jobs at the time, so I took a service/operations management job at a small business. It pays about $50K/year. The job is fine and low-stress, and since it’s 9–5 I have time to work on a side hustle that br
---

[RSS:Reddit Jobs & Careers (职场动态)]
Anyone recently go through Robinhood team matching for IC4/web? How long did it take?
https://www.reddit.com/r/cscareerquestions/comments/1st3huj/anyone_recently_go_through_robinhood_team/
I recently finished the virtual onsite for a Robinhood IC4 web role and was told my feedback was positive. I’m now in team matching, but recruiter communication has been pretty slow and I haven’t gotten an update in about a week. For anyone who went through this recently: How long did team matching 
---

[RSS:Reddit Jobs & Careers (职场动态)]
How to prepare for an AI Engineer internship meeting?
https://www.reddit.com/r/cscareerquestions/comments/1st1x6p/how_to_prepare_for_an_ai_engineer_internship/
Hi all, I have an internship interview for an AI Engineer position (remote) at a large insurance company coming up in a few days and I would love some insights into how I can better prepare for it. The initial discussion with the recruiter went well enough. She asked me if I've worked on any project
---

[HACKERNEWS]
Alberta startup sells no-tech tractors for half price
https://wheelfront.com/this-alberta-startup-sells-no-tech-tractors-for-half-price/
Score: 1394 | Comments: 481
---

[HACKERNEWS]
Apple fixes bug that cops used to extract deleted chat messages from iPhones
https://techcrunch.com/2026/04/22/apple-fixes-bug-that-cops-used-to-extract-deleted-chat-messages-from-iphones/
Score: 399 | Comments: 101
---

[HACKERNEWS]
We found a stable Firefox identifier linking all your private Tor identities
https://fingerprint.com/blog/firefox-tor-indexeddb-privacy-vulnerability/
Score: 468 | Comments: 139
---

[HACKERNEWS]
Qwen3.6-27B: Flagship-Level Coding in a 27B Dense Model
https://qwen.ai/blog?id=qwen3.6-27b
Score: 725 | Comments: 349
---

[HACKERNEWS]
Tempest vs. Tempest: The Making and Remaking of Atari's Iconic Video Game
https://tempest.homemade.systems
Score: 25 | Comments: 3
---

[HACKERNEWS]
Over-editing refers to a model modifying code beyond what is necessary
https://nrehiew.github.io/blog/minimal_editing/
Score: 306 | Comments: 173
---

[HACKERNEWS]
Website streamed live directly from a model
https://flipbook.page/
Score: 173 | Comments: 61
---

[HACKERNEWS]
OpenAI's response to the Axios developer tool compromise
https://openai.com/index/axios-developer-tool-compromise/
Score: 18 | Comments: 1
---

[HACKERNEWS]
Technical, cognitive, and intent debt
https://martinfowler.com/fragments/2026-04-02.html
Score: 211 | Comments: 50
---

[HACKERNEWS]
The handmade beauty of Machine Age data visualizations
https://resobscura.substack.com/p/the-handmade-beauty-of-machine-age
Score: 14 | Comments: 1
---

[HACKERNEWS]
Ping-pong robot beats top-level human players
https://www.reuters.com/sports/ping-pong-robot-ace-makes-history-by-beating-top-level-human-players-2026-04-22/
Score: 78 | Comments: 91
---

[HACKERNEWS]
Our eighth generation TPUs: two chips for the agentic era
https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/eighth-generation-tpu-agentic-era/
Score: 409 | Comments: 200
---

[HACKERNEWS]
Approximating Hyperbolic Tangent
https://jtomschroeder.com/blog/approximating-tanh/
Score: 26 | Comments: 4
---

[HACKERNEWS]
3.4M Solar Panels
https://tech.marksblogg.com/american-solar-farms-v2.html
Score: 294 | Comments: 230
---

[HACKERNEWS]
Scoring Show HN submissions for AI design patterns
https://www.adriankrebs.ch/blog/design-slop/
Score: 279 | Comments: 208
---

[HACKERNEWS]
Parallel agents in Zed
https://zed.dev/blog/parallel-agents
Score: 175 | Comments: 105
---

[HACKERNEWS]
The Illuminated Man: an unconventional portrait of JG Ballard
https://www.theguardian.com/books/2026/apr/20/the-illuminated-man-by-christopher-priest-and-nina-allan-review-an-unconventional-portrait-of-jg-ballard
Score: 49 | Comments: 17
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
标题: Near-Future Policy Optimization
作者: Chuanyu Qin, Chenxu Yang, Qingyi Si, Naibin Gu, Dingyu Yao, Zheng Lin, Peng Fu, Nan Duan, Jiaqi Wang
链接: https://arxiv.org/abs/2604.20733v1
完整摘要: Reinforcement learning with verifiable rewards (RLVR) has become a core post-training recipe. Introducing suitable off-policy trajectories into on-policy exploration accelerates RLVR convergence and raises the performance ceiling, yet finding a source of such trajectories remains the key challenge. Existing mixed-policy methods either import trajectories from external teachers (high-quality but distributionally far) or replay past training trajectories (close but capped in quality), and neither simultaneously satisfies the strong enough (higher $Q$ , more new knowledge to learn) and close enough (lower $V$ , more readily absorbed) conditions required to maximize the effective learning signal $\mathcal{S} = Q/V$. We propose \textbf{N}ear-Future \textbf{P}olicy \textbf{O}ptimization (\textbf{NPO}), a simple mixed-policy scheme that learns from a policy's own near-future self: a later checkpoint from the same training run is a natural source of auxiliary trajectories that is both stronger than the current policy and closer than any external source, directly balancing trajectory quality against variance cost. We validate NPO through two manual interventions, early-stage bootstrapping and late-stage plateau breakthrough, and further propose \textbf{AutoNPO},an adaptive variant that automatically triggers interventions from online training signals and selects the guide checkpoint that maximizes $S$. On Qwen3-VL-8B-Instruct with GRPO, NPO improves average performance from 57.88 to 62.84, and AutoNPO pushes it to 63.15, raising the final performance ceiling while accelerating convergence.
匹配关键词: GRPO
---

[ACADEMIC - ARXIV]
标题: GRPO-VPS: Enhancing Group Relative Policy Optimization with Verifiable Process Supervision for Effective Reasoning
作者: Jingyi Wang, Lei Zhu, Tengjin Weng, Song-Li Wu, Haochen Tan, Jierun Chen, Chaofan Tao, Haoli Bai, Lu Hou, Lifeng Shang, Xiao-Ping Zhang
链接: https://arxiv.org/abs/2604.20659v1
完整摘要: Reinforcement Learning with Verifiable Rewards (RLVR) has advanced the reasoning capabilities of Large Language Models (LLMs) by leveraging direct outcome verification instead of learned reward models. Building on this paradigm, Group Relative Policy Optimization (GRPO) eliminates the need for critic models but suffers from indiscriminate credit assignment for intermediate steps, which limits its ability to identify effective reasoning strategies and incurs overthinking. In this work, we introduce a model-free and verifiable process supervision via probing the model's belief in the correct answer throughout its reasoning trajectory. By segmenting the generation into discrete steps and tracking the conditional probability of the correct answer appended at each segment boundary, we efficiently compute interpretable segment-wise progress measurements to refine GRPO's trajectory-level feedback. This approach enables more targeted and sample-efficient policy updates, while avoiding the need for intermediate supervision derived from costly Monte Carlo rollouts or auxiliary models. Experiments on mathematical and general-domain benchmarks show consistent gains over GRPO across diverse models: up to 2.6-point accuracy improvements and 13.7% reasoning-length reductions on math tasks, and up to 2.4 points and 4% on general-domain tasks, demonstrating strong generalization.
匹配关键词: GRPO
---

[ACADEMIC - ARXIV]
标题: R2IF: Aligning Reasoning with Decisions via Composite Rewards for Interpretable LLM Function Calling
作者: Aijia Cheng, Kailong Wang, Ling Shi, Yongxin Zhao
链接: https://arxiv.org/abs/2604.20316v1
完整摘要: Function calling empowers large language models (LLMs) to interface with external tools, yet existing RL-based approaches suffer from misalignment between reasoning processes and tool-call decisions. We propose R2IF, a reasoning-aware RL framework for interpretable function calling, adopting a composite reward integrating format/correctness constraints, Chain-of-Thought Effectiveness Reward (CER), and Specification-Modification-Value (SMV) reward, optimized via GRPO. Experiments on BFCL/ACEBench show R2IF outperforms baselines by up to 34.62% (Llama3.2-3B on BFCL) with positive Average CoT Effectiveness (0.05 for Llama3.2-3B), enhancing both function-calling accuracy and interpretability for reliable tool-augmented LLM deployment.
匹配关键词: GRPO
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
标题: Bounded Ratio Reinforcement Learning
作者: Yunke Ao, Le Chen, Bruce D. Lee, Assefa S. Wahd, Aline Czarnobai, Philipp Fürnstahl, Bernhard Schölkopf, Andreas Krause
链接: https://arxiv.org/abs/2604.18578v2
完整摘要: Proximal Policy Optimization (PPO) has become the predominant algorithm for on-policy reinforcement learning due to its scalability and empirical robustness across domains. However, there is a significant disconnect between the underlying foundations of trust region methods and the heuristic clipped objective used in PPO. In this paper, we bridge this gap by introducing the Bounded Ratio Reinforcement Learning (BRRL) framework. We formulate a novel regularized and constrained policy optimization problem and derive its analytical optimal solution. We prove that this solution ensures monotonic performance improvement. To handle parameterized policy classes, we develop a policy optimization algorithm called Bounded Policy Optimization (BPO) that minimizes an advantage-weighted divergence between the policy and the analytic optimal solution from BRRL. We further establish a lower bound on the expected performance of the resulting policy in terms of the BPO loss function. Notably, our framework also provides a new theoretical lens to interpret the success of the PPO loss, and connects trust region policy optimization and the Cross-Entropy Method (CEM). We additionally extend BPO to Group-relative BPO (GBPO) for LLM fine-tuning. Empirical evaluations of BPO across MuJoCo, Atari, and complex IsaacLab environments (e.g., Humanoid locomotion), and of GBPO for LLM fine-tuning tasks, demonstrate that BPO and GBPO generally match or outperform PPO and GRPO in stability and final performance.
匹配关键词: PPO
---

[ACADEMIC - ARXIV]
标题: MGDA-Decoupled: Geometry-Aware Multi-Objective Optimisation for DPO-based LLM Alignment
作者: Andor Vári-Kakas, Ji Won Park, Natasa Tagasovska
链接: https://arxiv.org/abs/2604.20685v1
完整摘要: Aligning large language models (LLMs) to desirable human values requires balancing multiple, potentially conflicting objectives such as helpfulness, truthfulness, and harmlessness, which presents a multi-objective optimisation challenge. Most alignment pipelines rely on a fixed scalarisation of these objectives, which can introduce procedural unfairness by systematically under-weighting harder-to-optimise or minority objectives. To promote more equitable trade-offs, we introduce MGDA-Decoupled, a geometry-based multi-objective optimisation algorithm that finds a shared descent direction while explicitly accounting for each objective's convergence dynamics. In contrast to prior methods that depend on reinforcement learning (e.g., GAPO) or explicit reward models (e.g., MODPO), our approach operates entirely within the lightweight Direct Preference Optimisation (DPO) paradigm. Experiments on the UltraFeedback dataset show that geometry-aware methods -- and MGDA-Decoupled in particular -- achieve the highest win rates against golden responses, both overall and per objective.
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
标题: SpeechParaling-Bench: A Comprehensive Benchmark for Paralinguistic-Aware Speech Generation
作者: Ruohan Liu, Shukang Yin, Tao Wang, Dong Zhang, Weiji Zhuang, Shuhuai Ren, Ran He, Caifeng Shan, Chaoyou Fu
链接: https://arxiv.org/abs/2604.20842v1
完整摘要: Paralinguistic cues are essential for natural human-computer interaction, yet their evaluation in Large Audio-Language Models (LALMs) remains limited by coarse feature coverage and the inherent subjectivity of assessment. To address these challenges, we introduce SpeechParaling-Bench, a comprehensive benchmark for paralinguistic-aware speech generation. It expands existing coverage from fewer than 50 to over 100 fine-grained features, supported by more than 1,000 English-Chinese parallel speech queries, and is organized into three progressively challenging tasks: fine-grained control, intra-utterance variation, and context-aware adaptation. To enable reliable evaluation, we further develop a pairwise comparison pipeline, in which candidate responses are evaluated against a fixed baseline by an LALM-based judge. By framing evaluation as relative preference rather than absolute scoring, this approach mitigates subjectivity and yields more stable and scalable assessments without costly human annotation. Extensive experiments reveal substantial limitations in current LALMs. Even leading proprietary models struggle with comprehensive static control and dynamic modulation of paralinguistic features, while failure to correctly interpret paralinguistic cues accounts for 43.3% of errors in situational dialogue. These findings underscore the need for more robust paralinguistic modeling toward human-aligned voice assistants.
匹配关键词: alignment
---

[ACADEMIC - ARXIV]
标题: PokeVLA: Empowering Pocket-Sized Vision-Language-Action Model with Comprehensive World Knowledge Guidance
作者: Yupeng Zheng, Xiang Li, Songen Gu, Yuhang Zheng, Shuai Tian, Weize Li, Linbo Wang, Senyu Fei, Pengfei Li, Yinfeng Gao, Zebin Xing, Yilun Chen, Qichao Zhang, Haoran Li, Wenchao Ding
链接: https://arxiv.org/abs/2604.20834v1
完整摘要: Recent advances in Vision-Language-Action (VLA) models have opened new avenues for robot manipulation, yet existing methods exhibit limited efficiency and a lack of high-level knowledge and spatial awareness. To address these challenges, we propose PokeVLA, a lightweight yet powerful foundation model for embodied manipulation that effectively infuses vision-language understanding into action learning. Our framework introduces a two-stage training paradigm: first, we pre-train a compact vision-language model (PokeVLM) on a curated multimodal dataset of 2.4M samples encompassing spatial grounding, affordance, and embodied reasoning tasks; second, we inject manipulation-relevant representations into the action space through multi-view goal-aware semantics learning, geometry alignment, and a novel action expert. Extensive experiments demonstrate state-of-the-art performance on the LIBERO-Plus benchmark and in real-world deployment, outperforming comparable baselines in success rate and robustness under diverse perturbations. To foster reproducibility and community progress, we will open-source our code, model weights, and the scripts for the curated pre-training dataset. Project page: https://getterupper.github.io/PokeVLA
匹配关键词: alignment
---

[ACADEMIC - ARXIV]
标题: ParetoSlider: Diffusion Models Post-Training for Continuous Reward Control
作者: Shelly Golan, Michael Finkelson, Ariel Bereslavsky, Yotam Nitzan, Or Patashnik
链接: https://arxiv.org/abs/2604.20816v1
完整摘要: Reinforcement Learning (RL) post-training has become the standard for aligning generative models with human preferences, yet most methods rely on a single scalar reward. When multiple criteria matter, the prevailing practice of ``early scalarization'' collapses rewards into a fixed weighted sum. This commits the model to a single trade-off point at training time, providing no inference-time control over inherently conflicting goals -- such as prompt adherence versus source fidelity in image editing. We introduce ParetoSlider, a multi-objective RL (MORL) framework that trains a single diffusion model to approximate the entire Pareto front. By training the model with continuously varying preference weights as a conditioning signal, we enable users to navigate optimal trade-offs at inference time without retraining or maintaining multiple checkpoints. We evaluate ParetoSlider across three state-of-the-art flow-matching backbones: SD3.5, FluxKontext, and LTX-2. Our single preference-conditioned model matches or exceeds the performance of baselines trained separately for fixed reward trade-offs, while uniquely providing fine-grained control over competing generative goals.
匹配关键词: alignment
---

[ACADEMIC - ARXIV]
标题: Diagnosing CFG Interpretation in LLMs
作者: Hanqi Li, Lu Chen, Kai Yu
链接: https://arxiv.org/abs/2604.20811v1
完整摘要: As LLMs are increasingly integrated into agentic systems, they must adhere to dynamically defined, machine-interpretable interfaces. We evaluate LLMs as in-context interpreters: given a novel context-free grammar, can LLMs generate syntactically valid, behaviorally functional, and semantically faithful outputs? We introduce RoboGrid, a framework that disentangles syntax, behavior, and semantics through controlled stress-tests of recursion depth, expression complexity, and surface styles. Our experiments reveal a consistent hierarchical degradation: LLMs often maintain surface syntax but fail to preserve structural semantics. Despite the partial mitigation provided by CoT reasoning, performance collapses under structural density, specifically deep recursion and high branching, with semantic alignment vanishing at extreme depths. Furthermore, "Alien" lexicons reveal that LLMs rely on semantic bootstrapping from keywords rather than pure symbolic induction. These findings pinpoint critical gaps in hierarchical state-tracking required for reliable, grammar-agnostic agents.
匹配关键词: alignment
---

[ACADEMIC - ARXIV]
标题: Relative Principals, Pluralistic Alignment, and the Structural Value Alignment Problem
作者: Travis LaCroix
链接: https://arxiv.org/abs/2604.20805v1
完整摘要: The value alignment problem for artificial intelligence (AI) is often framed as a purely technical or normative challenge, sometimes focused on hypothetical future systems. I argue that the problem is better understood as a structural question about governance: not whether an AI system is aligned in the abstract, but whether it is aligned enough, for whom, and at what cost. Drawing on the principal-agent framework from economics, this paper reconceptualises misalignment as arising along three interacting axes: objectives, information, and principals. The three-axis framework provides a systematic way of diagnosing why misalignment arises in real-world systems and clarifies that alignment cannot be treated as a single technical property of models but an outcome shaped by how objectives are specified, how information is distributed, and whose interests count in practice. The core contribution of this paper is to show that the three-axis decomposition implies that alignment is fundamentally a problem of governance rather than engineering alone. From this perspective, alignment is inherently pluralistic and context-dependent, and resolving misalignment involves trade-offs among competing values. Because misalignment can occur along each axis -- and affect stakeholders differently -- the structural description shows that alignment cannot be "solved" through technical design alone, but must be managed through ongoing institutional processes that determine how objectives are set, how systems are evaluated, and how affected communities can contest or reshape those decisions.
匹配关键词: alignment
---

[ACADEMIC - ARXIV]
标题: SpeechParaling-Bench: A Comprehensive Benchmark for Paralinguistic-Aware Speech Generation
作者: Ruohan Liu, Shukang Yin, Tao Wang, Dong Zhang, Weiji Zhuang, Shuhuai Ren, Ran He, Caifeng Shan, Chaoyou Fu
链接: https://arxiv.org/abs/2604.20842v1
完整摘要: Paralinguistic cues are essential for natural human-computer interaction, yet their evaluation in Large Audio-Language Models (LALMs) remains limited by coarse feature coverage and the inherent subjectivity of assessment. To address these challenges, we introduce SpeechParaling-Bench, a comprehensive benchmark for paralinguistic-aware speech generation. It expands existing coverage from fewer than 50 to over 100 fine-grained features, supported by more than 1,000 English-Chinese parallel speech queries, and is organized into three progressively challenging tasks: fine-grained control, intra-utterance variation, and context-aware adaptation. To enable reliable evaluation, we further develop a pairwise comparison pipeline, in which candidate responses are evaluated against a fixed baseline by an LALM-based judge. By framing evaluation as relative preference rather than absolute scoring, this approach mitigates subjectivity and yields more stable and scalable assessments without costly human annotation. Extensive experiments reveal substantial limitations in current LALMs. Even leading proprietary models struggle with comprehensive static control and dynamic modulation of paralinguistic features, while failure to correctly interpret paralinguistic cues accounts for 43.3% of errors in situational dialogue. These findings underscore the need for more robust paralinguistic modeling toward human-aligned voice assistants.
匹配关键词: reward model
---

[ACADEMIC - ARXIV]
标题: DeVI: Physics-based Dexterous Human-Object Interaction via Synthetic Video Imitation
作者: Hyeonwoo Kim, Jeonghwan Kim, Kyungwon Cho, Hanbyul Joo
链接: https://arxiv.org/abs/2604.20841v1
完整摘要: Recent advances in video generative models enable the synthesis of realistic human-object interaction videos across a wide range of scenarios and object categories, including complex dexterous manipulations that are difficult to capture with motion capture systems. While the rich interaction knowledge embedded in these synthetic videos holds strong potential for motion planning in dexterous robotic manipulation, their limited physical fidelity and purely 2D nature make them difficult to use directly as imitation targets in physics-based character control. We present DeVI (Dexterous Video Imitation), a novel framework that leverages text-conditioned synthetic videos to enable physically plausible dexterous agent control for interacting with unseen target objects. To overcome the imprecision of generative 2D cues, we introduce a hybrid tracking reward that integrates 3D human tracking with robust 2D object tracking. Unlike methods relying on high-quality 3D kinematic demonstrations, DeVI requires only the generated video, enabling zero-shot generalization across diverse objects and interaction types. Extensive experiments demonstrate that DeVI outperforms existing approaches that imitate 3D human-object interaction demonstrations, particularly in modeling dexterous hand-object interactions. We further validate the effectiveness of DeVI in multi-object scenes and text-driven action diversity, showcasing the advantage of using video as an HOI-aware motion planner.
匹配关键词: reward model
---

[ACADEMIC - ARXIV]
标题: Parallel-SFT: Improving Zero-Shot Cross-Programming-Language Transfer for Code RL
作者: Zhaofeng Wu, Shiqi Wang, Boya Peng, Anuj Goyal, Melanie Kambadur, Sebastian Ruder, Yoon Kim, Chloe Bi
链接: https://arxiv.org/abs/2604.20835v1
完整摘要: Modern language models demonstrate impressive coding capabilities in common programming languages (PLs), such as C++ and Python, but their performance in lower-resource PLs is often limited by training data availability. In principle, however, most programming skills are universal across PLs, so the capability acquired in one PL should transfer to others. In this work, we propose the task of zero-shot cross-programming-language transfer for code RL. We find that, for Llama-3.1, RL training for code generation in a source PL fails to improve, and sometimes even degrades, the performance on other target PLs. To address this, we hypothesize that effective RL transfer requires a generalizable SFT initialization before RL. We thus propose **Parallel-SFT**, an SFT strategy that incorporates "parallel programs" -- functionally equivalent code implemented in multiple PLs -- into the data mixture. We demonstrate that this improves transferability: when we subsequently perform RL on our Parallel-SFT model, we observe better generalization to unseen PLs. Analysis of the model internal representations reveals that Parallel-SFT leads to a more functionality-centric latent space, where equivalent programs across PLs are more tightly clustered, which we hypothesize to contribute to the improved transferability.
匹配关键词: reward model
---

[ACADEMIC - ARXIV]
标题: PokeVLA: Empowering Pocket-Sized Vision-Language-Action Model with Comprehensive World Knowledge Guidance
作者: Yupeng Zheng, Xiang Li, Songen Gu, Yuhang Zheng, Shuai Tian, Weize Li, Linbo Wang, Senyu Fei, Pengfei Li, Yinfeng Gao, Zebin Xing, Yilun Chen, Qichao Zhang, Haoran Li, Wenchao Ding
链接: https://arxiv.org/abs/2604.20834v1
完整摘要: Recent advances in Vision-Language-Action (VLA) models have opened new avenues for robot manipulation, yet existing methods exhibit limited efficiency and a lack of high-level knowledge and spatial awareness. To address these challenges, we propose PokeVLA, a lightweight yet powerful foundation model for embodied manipulation that effectively infuses vision-language understanding into action learning. Our framework introduces a two-stage training paradigm: first, we pre-train a compact vision-language model (PokeVLM) on a curated multimodal dataset of 2.4M samples encompassing spatial grounding, affordance, and embodied reasoning tasks; second, we inject manipulation-relevant representations into the action space through multi-view goal-aware semantics learning, geometry alignment, and a novel action expert. Extensive experiments demonstrate state-of-the-art performance on the LIBERO-Plus benchmark and in real-world deployment, outperforming comparable baselines in success rate and robustness under diverse perturbations. To foster reproducibility and community progress, we will open-source our code, model weights, and the scripts for the curated pre-training dataset. Project page: https://getterupper.github.io/PokeVLA
匹配关键词: reward model
---

[ACADEMIC - ARXIV]
标题: AVISE: Framework for Evaluating the Security of AI Systems
作者: Mikko Lempinen, Joni Kemppainen, Niklas Raesalmi
链接: https://arxiv.org/abs/2604.20833v1
完整摘要: As artificial intelligence (AI) systems are increasingly deployed across critical domains, their security vulnerabilities pose growing risks of high-profile exploits and consequential system failures. Yet systematic approaches to evaluating AI security remain underdeveloped. In this paper, we introduce AVISE (AI Vulnerability Identification and Security Evaluation), a modular open-source framework for identifying vulnerabilities in and evaluating the security of AI systems and models. As a demonstration of the framework, we extend the theory-of-mind-based multi-turn Red Queen attack into an Adversarial Language Model (ALM) augmented attack and develop an automated Security Evaluation Test (SET) for discovering jailbreak vulnerabilities in language models. The SET comprises 25 test cases and an Evaluation Language Model (ELM) that determines whether each test case was able to jailbreak the target model, achieving 92% accuracy, an F1-score of 0.91, and a Matthews correlation coefficient of 0.83. We evaluate nine recently released language models of diverse sizes with the SET and find that all are vulnerable to the augmented Red Queen attack to varying degrees. AVISE provides researchers and industry practitioners with an extensible foundation for developing and deploying automated SETs, offering a concrete step toward more rigorous and reproducible AI security evaluation.
匹配关键词: reward model
---

[ACADEMIC - ARXIV]
标题: SpeechParaling-Bench: A Comprehensive Benchmark for Paralinguistic-Aware Speech Generation
作者: Ruohan Liu, Shukang Yin, Tao Wang, Dong Zhang, Weiji Zhuang, Shuhuai Ren, Ran He, Caifeng Shan, Chaoyou Fu
链接: https://arxiv.org/abs/2604.20842v1
完整摘要: Paralinguistic cues are essential for natural human-computer interaction, yet their evaluation in Large Audio-Language Models (LALMs) remains limited by coarse feature coverage and the inherent subjectivity of assessment. To address these challenges, we introduce SpeechParaling-Bench, a comprehensive benchmark for paralinguistic-aware speech generation. It expands existing coverage from fewer than 50 to over 100 fine-grained features, supported by more than 1,000 English-Chinese parallel speech queries, and is organized into three progressively challenging tasks: fine-grained control, intra-utterance variation, and context-aware adaptation. To enable reliable evaluation, we further develop a pairwise comparison pipeline, in which candidate responses are evaluated against a fixed baseline by an LALM-based judge. By framing evaluation as relative preference rather than absolute scoring, this approach mitigates subjectivity and yields more stable and scalable assessments without costly human annotation. Extensive experiments reveal substantial limitations in current LALMs. Even leading proprietary models struggle with comprehensive static control and dynamic modulation of paralinguistic features, while failure to correctly interpret paralinguistic cues accounts for 43.3% of errors in situational dialogue. These findings underscore the need for more robust paralinguistic modeling toward human-aligned voice assistants.
匹配关键词: preference optimization
---

[ACADEMIC - ARXIV]
标题: FedSIR: Spectral Client Identification and Relabeling for Federated Learning with Noisy Labels
作者: Sina Gholami, Abdulmoneam Ali, Tania Haghighi, Ahmed Arafa, Minhaj Nur Alam
链接: https://arxiv.org/abs/2604.20825v1
完整摘要: Federated learning (FL) enables collaborative model training without sharing raw data; however, the presence of noisy labels across distributed clients can severely degrade the learning performance. In this paper, we propose FedSIR, a multi-stage framework for robust FL under noisy labels. Different from existing approaches that mainly rely on designing noise-tolerant loss functions or exploiting loss dynamics during training, our method leverages the spectral structure of client feature representations to identify and mitigate label noise. Our framework consists of three key components. First, we identify clean and noisy clients by analyzing the spectral consistency of class-wise feature subspaces with minimal communication overhead. Second, clean clients provide spectral references that enable noisy clients to relabel potentially corrupted samples using both dominant class directions and residual subspaces. Third, we employ a noise-aware training strategy that integrates logit-adjusted loss, knowledge distillation, and distance-aware aggregation to further stabilize federated optimization. Extensive experiments on standard FL benchmarks demonstrate that FedSIR consistently outperforms state-of-the-art methods for FL with noisy labels. The code is available at https://github.com/sinagh72/FedSIR.
匹配关键词: preference optimization
---

[ACADEMIC - ARXIV]
标题: Convergent Evolution: How Different Language Models Learn Similar Number Representations
作者: Deqing Fu, Tianyi Zhou, Mikhail Belkin, Vatsal Sharan, Robin Jia
链接: https://arxiv.org/abs/2604.20817v1
完整摘要: Language models trained on natural text learn to represent numbers using periodic features with dominant periods at $T=2, 5, 10$. In this paper, we identify a two-tiered hierarchy of these features: while Transformers, Linear RNNs, LSTMs, and classical word embeddings trained in different ways all learn features that have period-$T$ spikes in the Fourier domain, only some learn geometrically separable features that can be used to linearly classify a number mod-$T$. To explain this incongruity, we prove that Fourier domain sparsity is necessary but not sufficient for mod-$T$ geometric separability. Empirically, we investigate when model training yields geometrically separable features, finding that the data, architecture, optimizer, and tokenizer all play key roles. In particular, we identify two different routes through which models can acquire geometrically separable features: they can learn them from complementary co-occurrence signals in general language data, including text-number co-occurrence and cross-number interaction, or from multi-token (but not single-token) addition problems. Overall, our results highlight the phenomenon of convergent evolution in feature learning: A diverse range of models learn similar features from different training signals.
匹配关键词: preference optimization
---

[ACADEMIC - ARXIV]
标题: ParetoSlider: Diffusion Models Post-Training for Continuous Reward Control
作者: Shelly Golan, Michael Finkelson, Ariel Bereslavsky, Yotam Nitzan, Or Patashnik
链接: https://arxiv.org/abs/2604.20816v1
完整摘要: Reinforcement Learning (RL) post-training has become the standard for aligning generative models with human preferences, yet most methods rely on a single scalar reward. When multiple criteria matter, the prevailing practice of ``early scalarization'' collapses rewards into a fixed weighted sum. This commits the model to a single trade-off point at training time, providing no inference-time control over inherently conflicting goals -- such as prompt adherence versus source fidelity in image editing. We introduce ParetoSlider, a multi-objective RL (MORL) framework that trains a single diffusion model to approximate the entire Pareto front. By training the model with continuously varying preference weights as a conditioning signal, we enable users to navigate optimal trade-offs at inference time without retraining or maintaining multiple checkpoints. We evaluate ParetoSlider across three state-of-the-art flow-matching backbones: SD3.5, FluxKontext, and LTX-2. Our single preference-conditioned model matches or exceeds the performance of baselines trained separately for fixed reward trade-offs, while uniquely providing fine-grained control over competing generative goals.
匹配关键词: preference optimization
---

[ACADEMIC - ARXIV]
标题: LEXIS: LatEnt ProXimal Interaction Signatures for 3D HOI from an Image
作者: Dimitrije Antić, Alvaro Budria, George Paschalidis, Sai Kumar Dwivedi, Dimitrios Tzionas
链接: https://arxiv.org/abs/2604.20800v1
完整摘要: Reconstructing 3D Human-Object Interaction from an RGB image is essential for perceptive systems. Yet, this remains challenging as it requires capturing the subtle physical coupling between the body and objects. While current methods rely on sparse, binary contact cues, these fail to model the continuous proximity and dense spatial relationships that characterize natural interactions. We address this limitation via InterFields, a representation that encodes dense, continuous proximity across the entire body and object surfaces. However, inferring these fields from single images is inherently ill-posed. To tackle this, our intuition is that interaction patterns are characteristically structured by the action and object geometry. We capture this structure in LEXIS, a novel discrete manifold of interaction signatures learned via a VQ-VAE. We then develop LEXIS-Flow, a diffusion framework that leverages LEXIS signatures to estimate human and object meshes alongside their InterFields. Notably, these InterFields help in a guided refinement that ensures physically-plausible, proximity-aware reconstructions without requiring post-hoc optimization. Evaluation on Open3DHOI and BEHAVE shows that LEXIS-Flow significantly outperforms existing SotA baselines in reconstruction, contact, and proximity quality. Our approach not only improves generalization but also yields reconstructions perceived as more realistic, moving us closer to holistic 3D scene understanding. Code & models will be public at https://anticdimi.github.io/lexis.
匹配关键词: preference optimization
---

[ACADEMIC - ARXIV]
标题: AVISE: Framework for Evaluating the Security of AI Systems
作者: Mikko Lempinen, Joni Kemppainen, Niklas Raesalmi
链接: https://arxiv.org/abs/2604.20833v1
完整摘要: As artificial intelligence (AI) systems are increasingly deployed across critical domains, their security vulnerabilities pose growing risks of high-profile exploits and consequential system failures. Yet systematic approaches to evaluating AI security remain underdeveloped. In this paper, we introduce AVISE (AI Vulnerability Identification and Security Evaluation), a modular open-source framework for identifying vulnerabilities in and evaluating the security of AI systems and models. As a demonstration of the framework, we extend the theory-of-mind-based multi-turn Red Queen attack into an Adversarial Language Model (ALM) augmented attack and develop an automated Security Evaluation Test (SET) for discovering jailbreak vulnerabilities in language models. The SET comprises 25 test cases and an Evaluation Language Model (ELM) that determines whether each test case was able to jailbreak the target model, achieving 92% accuracy, an F1-score of 0.91, and a Matthews correlation coefficient of 0.83. We evaluate nine recently released language models of diverse sizes with the SET and find that all are vulnerable to the augmented Red Queen attack to varying degrees. AVISE provides researchers and industry practitioners with an extensible foundation for developing and deploying automated SETs, offering a concrete step toward more rigorous and reproducible AI security evaluation.
匹配关键词: constitutional AI
---

[ACADEMIC - ARXIV]
标题: Relative Principals, Pluralistic Alignment, and the Structural Value Alignment Problem
作者: Travis LaCroix
链接: https://arxiv.org/abs/2604.20805v1
完整摘要: The value alignment problem for artificial intelligence (AI) is often framed as a purely technical or normative challenge, sometimes focused on hypothetical future systems. I argue that the problem is better understood as a structural question about governance: not whether an AI system is aligned in the abstract, but whether it is aligned enough, for whom, and at what cost. Drawing on the principal-agent framework from economics, this paper reconceptualises misalignment as arising along three interacting axes: objectives, information, and principals. The three-axis framework provides a systematic way of diagnosing why misalignment arises in real-world systems and clarifies that alignment cannot be treated as a single technical property of models but an outcome shaped by how objectives are specified, how information is distributed, and whose interests count in practice. The core contribution of this paper is to show that the three-axis decomposition implies that alignment is fundamentally a problem of governance rather than engineering alone. From this perspective, alignment is inherently pluralistic and context-dependent, and resolving misalignment involves trade-offs among competing values. Because misalignment can occur along each axis -- and affect stakeholders differently -- the structural description shows that alignment cannot be "solved" through technical design alone, but must be managed through ongoing institutional processes that determine how objectives are set, how systems are evaluated, and how affected communities can contest or reshape those decisions.
匹配关键词: constitutional AI
---

[ACADEMIC - ARXIV]
标题: LLaDA2.0-Uni: Unifying Multimodal Understanding and Generation with Diffusion Large Language Model
作者: Inclusion AI, Tiwei Bie, Haoxing Chen, Tieyuan Chen, Zhenglin Cheng, Long Cui, Kai Gan, Zhicheng Huang, Zhenzhong Lan, Haoquan Li, Jianguo Li, Tao Lin, Qi Qin, Hongjun Wang, Xiaomei Wang, Haoyuan Wu, Yi Xin, Junbo Zhao
链接: https://arxiv.org/abs/2604.20796v1
完整摘要: We present LLaDA2.0-Uni, a unified discrete diffusion large language model (dLLM) that supports multimodal understanding and generation within a natively integrated framework. Its architecture combines a fully semantic discrete tokenizer, a MoE-based dLLM backbone, and a diffusion decoder. By discretizing continuous visual inputs via SigLIP-VQ, the model enables block-level masked diffusion for both text and vision inputs within the backbone, while the decoder reconstructs visual tokens into high-fidelity images. Inference efficiency is enhanced beyond parallel decoding through prefix-aware optimizations in the backbone and few-step distillation in the decoder. Supported by carefully curated large-scale data and a tailored multi-stage training pipeline, LLaDA2.0-Uni matches specialized VLMs in multimodal understanding while delivering strong performance in image generation and editing. Its native support for interleaved generation and reasoning establishes a promising and scalable paradigm for next-generation unified foundation models. Codes and models are available at https://github.com/inclusionAI/LLaDA2.0-Uni.
匹配关键词: constitutional AI
---

[ACADEMIC - ARXIV]
标题: Automatic Ontology Construction Using LLMs as an External Layer of Memory, Verification, and Planning for Hybrid Intelligent Systems
作者: Pavel Salovskii, Iuliia Gorshkova
链接: https://arxiv.org/abs/2604.20795v1
完整摘要: This paper presents a hybrid architecture for intelligent systems in which large language models (LLMs) are extended with an external ontological memory layer. Instead of relying solely on parametric knowledge and vector-based retrieval (RAG), the proposed approach constructs and maintains a structured knowledge graph using RDF/OWL representations, enabling persistent, verifiable, and semantically grounded reasoning. The core contribution is an automated pipeline for ontology construction from heterogeneous data sources, including documents, APIs, and dialogue logs. The system performs entity recognition, relation extraction, normalization, and triple generation, followed by validation using SHACL and OWL constraints, and continuous graph updates. During inference, LLMs operate over a combined context that integrates vector-based retrieval with graph-based reasoning and external tool interaction. Experimental observations on planning tasks, including the Tower of Hanoi benchmark, indicate that ontology augmentation improves performance in multi-step reasoning scenarios compared to baseline LLM systems. In addition, the ontology layer enables formal validation of generated outputs, transforming the system into a generation-verification-correction pipeline. The proposed architecture addresses key limitations of current LLM-based systems, including lack of long-term memory, weak structural understanding, and limited reasoning capabilities. It provides a foundation for building agent-based systems, robotics applications, and enterprise AI solutions that require persistent knowledge, explainability, and reliable decision-making.
匹配关键词: constitutional AI
---

[ACADEMIC - ARXIV]
标题: Can "AI" Be a Doctor? A Study of Empathy, Readability, and Alignment in Clinical LLMs
作者: Mariano Barone, Francesco Di Serio, Roberto Moio, Marco Postiglione, Giuseppe Riccio, Antonio Romano, Vincenzo Moscato
链接: https://arxiv.org/abs/2604.20791v1
完整摘要: Large Language Models (LLMs) are increasingly deployed in healthcare, yet their communicative alignment with clinical standards remains insufficiently quantified. We conduct a multidimensional evaluation of general-purpose and domain-specialized LLMs across structured medical explanations and real-world physician-patient interactions, analyzing semantic fidelity, readability, and affective resonance. Baseline models amplify affective polarity relative to physicians (Very Negative: 43.14-45.10% vs. 37.25%) and, in larger architectures such as GPT-5 and Claude, produce substantially higher linguistic complexity (FKGL up to 16.91-17.60 vs. 11.47-12.50 in physician-authored responses). Empathy-oriented prompting reduces extreme negativity and lowers grade-level complexity (up to -6.87 FKGL points for GPT-5) but does not significantly increase semantic fidelity. Collaborative rewriting yields the strongest overall alignment. Rephrase configurations achieve the highest semantic similarity to physician answers (up to mean = 0.93) while consistently improving readability and reducing affective extremity. Dual stakeholder evaluation shows that no model surpasses physicians on epistemic criteria, whereas patients consistently prefer rewritten variants for clarity and emotional tone. These findings suggest that LLMs function most effectively as collaborative communication enhancers rather than replacements for clinical expertise.
匹配关键词: constitutional AI
---

[ACADEMIC - ARXIV]
标题: PokeVLA: Empowering Pocket-Sized Vision-Language-Action Model with Comprehensive World Knowledge Guidance
作者: Yupeng Zheng, Xiang Li, Songen Gu, Yuhang Zheng, Shuai Tian, Weize Li, Linbo Wang, Senyu Fei, Pengfei Li, Yinfeng Gao, Zebin Xing, Yilun Chen, Qichao Zhang, Haoran Li, Wenchao Ding
链接: https://arxiv.org/abs/2604.20834v1
完整摘要: Recent advances in Vision-Language-Action (VLA) models have opened new avenues for robot manipulation, yet existing methods exhibit limited efficiency and a lack of high-level knowledge and spatial awareness. To address these challenges, we propose PokeVLA, a lightweight yet powerful foundation model for embodied manipulation that effectively infuses vision-language understanding into action learning. Our framework introduces a two-stage training paradigm: first, we pre-train a compact vision-language model (PokeVLM) on a curated multimodal dataset of 2.4M samples encompassing spatial grounding, affordance, and embodied reasoning tasks; second, we inject manipulation-relevant representations into the action space through multi-view goal-aware semantics learning, geometry alignment, and a novel action expert. Extensive experiments demonstrate state-of-the-art performance on the LIBERO-Plus benchmark and in real-world deployment, outperforming comparable baselines in success rate and robustness under diverse perturbations. To foster reproducibility and community progress, we will open-source our code, model weights, and the scripts for the curated pre-training dataset. Project page: https://getterupper.github.io/PokeVLA
匹配关键词: reasoning
---

[ACADEMIC - ARXIV]
标题: Diagnosing CFG Interpretation in LLMs
作者: Hanqi Li, Lu Chen, Kai Yu
链接: https://arxiv.org/abs/2604.20811v1
完整摘要: As LLMs are increasingly integrated into agentic systems, they must adhere to dynamically defined, machine-interpretable interfaces. We evaluate LLMs as in-context interpreters: given a novel context-free grammar, can LLMs generate syntactically valid, behaviorally functional, and semantically faithful outputs? We introduce RoboGrid, a framework that disentangles syntax, behavior, and semantics through controlled stress-tests of recursion depth, expression complexity, and surface styles. Our experiments reveal a consistent hierarchical degradation: LLMs often maintain surface syntax but fail to preserve structural semantics. Despite the partial mitigation provided by CoT reasoning, performance collapses under structural density, specifically deep recursion and high branching, with semantic alignment vanishing at extreme depths. Furthermore, "Alien" lexicons reveal that LLMs rely on semantic bootstrapping from keywords rather than pure symbolic induction. These findings pinpoint critical gaps in hierarchical state-tracking required for reliable, grammar-agnostic agents.
匹配关键词: reasoning
---

[ACADEMIC - ARXIV]
标题: OMIBench: Benchmarking Olympiad-Level Multi-Image Reasoning in Large Vision-Language Model
作者: Qiguang Chen, Chengyu Luan, Jiajun Wu, Qiming Yu, Yi Yang, Yizhuo Li, Jingqi Tong, Xiachong Feng, Libo Qin, Wanxiang Che
链接: https://arxiv.org/abs/2604.20806v1
完整摘要: Large vision-language models (LVLMs) have made substantial advances in reasoning tasks at the Olympiad level. Nevertheless, current Olympiad-level multimodal reasoning benchmarks for these models often emphasize single-image analysis and fail to exploit contextual information across multiple images. We present OMIBench, a benchmark designed to evaluate Olympiad-level reasoning when the required evidence is distributed over multiple images. It contains problems from biology, chemistry, mathematics, and physics Olympiads, together with manually annotated rationales and evaluation protocols for both exact and semantic answer matching. Across extensive experiments on OMIBench, we observe meaningful performance gaps in existing models. Even the strongest LVLMs, such as Gemini-3-Pro, attain only about 50% on the benchmark. These results position OMIBench as a focused resources for studying and improving multi-image reasoning in LVLMs.
匹配关键词: reasoning
---

[ACADEMIC - ARXIV]
标题: LLaDA2.0-Uni: Unifying Multimodal Understanding and Generation with Diffusion Large Language Model
作者: Inclusion AI, Tiwei Bie, Haoxing Chen, Tieyuan Chen, Zhenglin Cheng, Long Cui, Kai Gan, Zhicheng Huang, Zhenzhong Lan, Haoquan Li, Jianguo Li, Tao Lin, Qi Qin, Hongjun Wang, Xiaomei Wang, Haoyuan Wu, Yi Xin, Junbo Zhao
链接: https://arxiv.org/abs/2604.20796v1
完整摘要: We present LLaDA2.0-Uni, a unified discrete diffusion large language model (dLLM) that supports multimodal understanding and generation within a natively integrated framework. Its architecture combines a fully semantic discrete tokenizer, a MoE-based dLLM backbone, and a diffusion decoder. By discretizing continuous visual inputs via SigLIP-VQ, the model enables block-level masked diffusion for both text and vision inputs within the backbone, while the decoder reconstructs visual tokens into high-fidelity images. Inference efficiency is enhanced beyond parallel decoding through prefix-aware optimizations in the backbone and few-step distillation in the decoder. Supported by carefully curated large-scale data and a tailored multi-stage training pipeline, LLaDA2.0-Uni matches specialized VLMs in multimodal understanding while delivering strong performance in image generation and editing. Its native support for interleaved generation and reasoning establishes a promising and scalable paradigm for next-generation unified foundation models. Codes and models are available at https://github.com/inclusionAI/LLaDA2.0-Uni.
匹配关键词: reasoning
---

[ACADEMIC - ARXIV]
标题: Automatic Ontology Construction Using LLMs as an External Layer of Memory, Verification, and Planning for Hybrid Intelligent Systems
作者: Pavel Salovskii, Iuliia Gorshkova
链接: https://arxiv.org/abs/2604.20795v1
完整摘要: This paper presents a hybrid architecture for intelligent systems in which large language models (LLMs) are extended with an external ontological memory layer. Instead of relying solely on parametric knowledge and vector-based retrieval (RAG), the proposed approach constructs and maintains a structured knowledge graph using RDF/OWL representations, enabling persistent, verifiable, and semantically grounded reasoning. The core contribution is an automated pipeline for ontology construction from heterogeneous data sources, including documents, APIs, and dialogue logs. The system performs entity recognition, relation extraction, normalization, and triple generation, followed by validation using SHACL and OWL constraints, and continuous graph updates. During inference, LLMs operate over a combined context that integrates vector-based retrieval with graph-based reasoning and external tool interaction. Experimental observations on planning tasks, including the Tower of Hanoi benchmark, indicate that ontology augmentation improves performance in multi-step reasoning scenarios compared to baseline LLM systems. In addition, the ontology layer enables formal validation of generated outputs, transforming the system into a generation-verification-correction pipeline. The proposed architecture addresses key limitations of current LLM-based systems, including lack of long-term memory, weak structural understanding, and limited reasoning capabilities. It provides a foundation for building agent-based systems, robotics applications, and enterprise AI solutions that require persistent knowledge, explainability, and reliable decision-making.
匹配关键词: reasoning
---

[ACADEMIC - ARXIV]
标题: V-tableR1: Process-Supervised Multimodal Table Reasoning with Critic-Guided Policy Optimization
作者: Yubo Jiang, Yitong An, Xin Yang, Abudukelimu Wuerkaixi, Xuxin Cheng, Fengying Xie, Zhiguo Jiang, Cao Liu, Ke Zeng, Haopeng Zhang
链接: https://arxiv.org/abs/2604.20755v1
完整摘要: We introduce V-tableR1, a process-supervised reinforcement learning framework that elicits rigorous, verifiable reasoning from multimodal large language models (MLLMs). Current MLLMs trained solely on final outcomes often treat visual reasoning as a black box, relying on superficial pattern matching rather than performing rigorous multi-step inference. While Reinforcement Learning with Verifiable Rewards could enforce transparent reasoning trajectories, extending it to visual domains remains severely hindered by the ambiguity of grounding abstract logic into continuous pixel space. We solve this by leveraging the deterministic grid structure of tables as an ideal visual testbed. V-tableR1 employs a specialized critic VLM to provide dense, step-level feedback on the explicit visual chain-of-thought generated by a policy VLM. To optimize this system, we propose Process-Guided Direct Alignment Policy Optimization (PGPO), a novel RL algorithm integrating process rewards, decoupled policy constraints, and length-aware dynamic sampling. Extensive evaluations demonstrate that V-tableR1 explicitly penalizes visual hallucinations and shortcut guessing. By fundamentally shifting multimodal inference from black-box pattern matching to verifiable logical derivation, V-tableR1 4B establishes state-of-the-art accuracy among open-source models on complex tabular benchmarks, outperforming models up to 18x its size and improving over its SFT baseline
匹配关键词: chain-of-thought
---

[ACADEMIC - ARXIV]
标题: Hybrid Latent Reasoning with Decoupled Policy Optimization
作者: Tao Cheng, Shi-Zhe Chen, Hao Zhang, Yixin Qin, Jinwen Luo, Zheng Wei
链接: https://arxiv.org/abs/2604.20328v1
完整摘要: Chain-of-Thought (CoT) reasoning significantly elevates the complex problem-solving capabilities of multimodal large language models (MLLMs). However, adapting CoT to vision typically discretizes signals to fit LLM inputs, causing early semantic collapse and discarding fine-grained details. While external tools can mitigate this, they introduce a rigid bottleneck, confining reasoning to predefined operations. Although recent latent reasoning paradigms internalize visual states to overcome these limitations, optimizing the resulting hybrid discrete-continuous action space remains challenging. In this work, we propose HyLaR (Hybrid Latent Reasoning), a framework that seamlessly interleaves discrete text generation with continuous visual latent representations. Specifically, following an initial cold-start supervised fine-tuning (SFT), we introduce DePO (Decoupled Policy Optimization) to enable effective reinforcement learning within this hybrid space. DePO decomposes the policy gradient objective, applying independent trust-region constraints to the textual and latent components, alongside an exact closed-form von Mises-Fisher (vMF) KL regularizer. Extensive experiments demonstrate that HyLaR outperforms standard MLLMs and state-of-the-art latent reasoning approaches across fine-grained perception and general multimodal understanding benchmarks. Code is available at https://github.com/EthenCheng/HyLaR.
匹配关键词: chain-of-thought
---

[ACADEMIC - ARXIV]
标题: SurgCoT: Advancing Spatiotemporal Reasoning in Surgical Videos through a Chain-of-Thought Benchmark
作者: Gui Wang, YongSong Zhou, Kaijun Deng, Wooi Ping Cheah, Rong Qu, Jianfeng Ren, Linlin Shen
链接: https://arxiv.org/abs/2604.20319v1
完整摘要: Fine-grained spatiotemporal reasoning on surgical videos is critical, yet the capabilities of Multi-modal Large Language Models (MLLMs) in this domain remain largely unexplored. To bridge this gap, we introduce SurgCoT, a unified benchmark for evaluating chain-of-thought (CoT) reasoning in MLLMs across 7 surgical specialties and 35 diverse procedures. SurgCoT assesses five core reasoning dimensions: Causal Action Ordering, Cue-Action Alignment, Affordance Mapping, Micro-Transition Localization, and Anomaly Onset Tracking, through a structured CoT framework with an intensive annotation protocol (Question-Option-Knowledge-Clue-Answer), where the Knowledge field provides essential background context and Clue provides definitive spatiotemporal evidence. Evaluation of 10 leading MLLMs shows: 1) commercial models outperform open-source and medical-specialized variants; 2) significant gaps exist in surgical CoT reasoning; 3) SurgCoT enables effective evaluation and enhances progressive spatiotemporal reasoning. SurgCoT provides a reproducible testbed to narrow the gap between MLLM capabilities and clinical reasoning demands. Code: https://github.com/CVI-SZU/SurgCoT.
匹配关键词: chain-of-thought
---

[ACADEMIC - ARXIV]
标题: R2IF: Aligning Reasoning with Decisions via Composite Rewards for Interpretable LLM Function Calling
作者: Aijia Cheng, Kailong Wang, Ling Shi, Yongxin Zhao
链接: https://arxiv.org/abs/2604.20316v1
完整摘要: Function calling empowers large language models (LLMs) to interface with external tools, yet existing RL-based approaches suffer from misalignment between reasoning processes and tool-call decisions. We propose R2IF, a reasoning-aware RL framework for interpretable function calling, adopting a composite reward integrating format/correctness constraints, Chain-of-Thought Effectiveness Reward (CER), and Specification-Modification-Value (SMV) reward, optimized via GRPO. Experiments on BFCL/ACEBench show R2IF outperforms baselines by up to 34.62% (Llama3.2-3B on BFCL) with positive Average CoT Effectiveness (0.05 for Llama3.2-3B), enhancing both function-calling accuracy and interpretability for reliable tool-augmented LLM deployment.
匹配关键词: chain-of-thought
---

[ACADEMIC - ARXIV]
标题: SAKE: Self-aware Knowledge Exploitation-Exploration for Grounded Multimodal Named Entity Recognition
作者: Jielong Tang, Xujie Yuan, Jiayang Liu, Jianxing Yu, Xiao Dong, Lin Chen, Yunlai Teng, Shimin Di, Jian Yin
链接: https://arxiv.org/abs/2604.20146v1
完整摘要: Grounded Multimodal Named Entity Recognition (GMNER) aims to extract named entities and localize their visual regions within image-text pairs, serving as a pivotal capability for various downstream applications. In open-world social media platforms, GMNER remains challenging due to the prevalence of long-tailed, rapidly evolving, and unseen entities. To tackle this, existing approaches typically rely on either external knowledge exploration through heuristic retrieval or internal knowledge exploitation via iterative refinement in Multimodal Large Language Models (MLLMs). However, heuristic retrieval often introduces noisy or conflicting evidence that degrades precision on known entities, while solely internal exploitation is constrained by the knowledge boundaries of MLLMs and prone to hallucinations. To address this, we propose SAKE, an end-to-end agentic framework that harmonizes internal knowledge exploitation and external knowledge exploration via self-aware reasoning and adaptive search tool invocation. We implement this via a two-stage training paradigm. First, we propose Difficulty-aware Search Tag Generation, which quantifies the model's entity-level uncertainty through multiple forward samplings to produce explicit knowledge-gap signals. Based on these signals, we construct SAKE-SeCoT, a high-quality Chain-of-Thought dataset that equips the model with basic self-awareness and tool-use capabilities through supervised fine-tuning. Second, we employ agentic reinforcement learning with a hybrid reward function that penalizes unnecessary retrieval, enabling the model to evolve from rigid search imitation to genuine self-aware decision-making about when retrieval is truly necessary. Extensive experiments on two widely used social media benchmarks demonstrate SAKE's effectiveness.
匹配关键词: chain-of-thought
---

[ACADEMIC - ARXIV]
标题: SpeechParaling-Bench: A Comprehensive Benchmark for Paralinguistic-Aware Speech Generation
作者: Ruohan Liu, Shukang Yin, Tao Wang, Dong Zhang, Weiji Zhuang, Shuhuai Ren, Ran He, Caifeng Shan, Chaoyou Fu
链接: https://arxiv.org/abs/2604.20842v1
完整摘要: Paralinguistic cues are essential for natural human-computer interaction, yet their evaluation in Large Audio-Language Models (LALMs) remains limited by coarse feature coverage and the inherent subjectivity of assessment. To address these challenges, we introduce SpeechParaling-Bench, a comprehensive benchmark for paralinguistic-aware speech generation. It expands existing coverage from fewer than 50 to over 100 fine-grained features, supported by more than 1,000 English-Chinese parallel speech queries, and is organized into three progressively challenging tasks: fine-grained control, intra-utterance variation, and context-aware adaptation. To enable reliable evaluation, we further develop a pairwise comparison pipeline, in which candidate responses are evaluated against a fixed baseline by an LALM-based judge. By framing evaluation as relative preference rather than absolute scoring, this approach mitigates subjectivity and yields more stable and scalable assessments without costly human annotation. Extensive experiments reveal substantial limitations in current LALMs. Even leading proprietary models struggle with comprehensive static control and dynamic modulation of paralinguistic features, while failure to correctly interpret paralinguistic cues accounts for 43.3% of errors in situational dialogue. These findings underscore the need for more robust paralinguistic modeling toward human-aligned voice assistants.
匹配关键词: test-time compute
---

[ACADEMIC - ARXIV]
标题: Stream-CQSA: Avoiding Out-of-Memory in Attention Computation via Flexible Workload Scheduling
作者: Yiming Bian, Joshua M. Akey
链接: https://arxiv.org/abs/2604.20819v1
完整摘要: The scalability of long-context large language models is fundamentally limited by the quadratic memory cost of exact self-attention, which often leads to out-of-memory (OOM) failures on modern hardware. Existing methods improve memory efficiency to near-linear complexity, while assuming that the full query, key, and value tensors fit in device memory. In this work, we remove this assumption by introducing CQS Divide, an operation derived from cyclic quorum sets (CQS) theory that decomposes attention into a set of independent subsequence computations whose recomposition yields exactly the same result as full-sequence attention. Exploiting this decomposition, we introduce Stream-CQSA, a memory-adaptive scheduling framework that partitions attention into subproblems that fit within arbitrary memory budgets. This recasts attention from a logically monolithic operation into a collection of schedulable tasks, enabling flexible execution across devices without inter-device communication. Experiments demonstrate predictable memory scaling and show that exact attention over billion-token sequences can be executed on a single GPU via streaming, without changing the underlying mathematical definition of attention or introducing approximation error.
匹配关键词: test-time compute
---

[ACADEMIC - ARXIV]
标题: Efficient Multi-Cohort Inference for Long-Term Effects and Lifetime Value in A/B Testing with User Learning
作者: Dario Simionato, Andrea Tonon, Mingxue Wang, Weiguo Wang, Tong Gui, Xiaoyue Li
链接: https://arxiv.org/abs/2604.20777v1
完整摘要: In streaming platforms churn is extremely costly, yet A/B tests are typically evaluated using outcomes observed within a limited experimental horizon. Even when both short- and predicted long-term engagement metrics are considered, they may fail to capture how a treatment affects users' retention. Consequently, an intervention may appear beneficial in the short term and neutral in the long term while still generating lower total value than the control due to users churn. To address this limitation, we introduce a method that estimates long-term treatment effects (LTE) and residual lifetime value change ($ΔERLV$) in short multi-cohort A/B tests under user learning. To estimate time-varying treatment effects efficiently, we introduce an inverse-variance weighted estimator that combines multiple cohorts estimates, reducing variance relative to standard approaches in the literature. The estimated treatment trajectory is then modeled as a parametric decay to recover both the asymptotic treatment effect and the cumulative value generated over time. Our framework enables simultaneous evaluation of steady-state impact and residual user value within a single experiment. Empirical results show improved precision in estimating LTE and $ΔERLV$ and identify scenarios in which relying on either short-term or long-term metrics alone would lead to incorrect product decisions.
匹配关键词: test-time compute
---

[ACADEMIC - ARXIV]
标题: DAIRE: A lightweight AI model for real-time detection of Controller Area Network attacks in the Internet of Vehicles
作者: Shahid Alam, Amina Jameel, Zahida Parveen, Ehab Alnfrawy, Adeela Ashraf, Raza Uddin, Jamal Aqib
链接: https://arxiv.org/abs/2604.20771v1
完整摘要: The Internet of Vehicles (IoV) is advancing modern transportation by improving safety, efficiency, and intelligence. However, the reliance on the Controller Area Network (CAN) introduces critical security risks, as CAN-based communication is highly vulnerable to cyberattacks. Addressing this challenge, we propose DAIRE (Detecting Attacks in IoV in REal-time), a lightweight machine learning framework designed for real-time detection and classification of CAN attacks. DAIRE is built on a lightweight artificial neural network (ANN) where each layer contains Ni = i x c neurons, with Ni representing the number of neurons in the ith layer and c corresponding to the total number of attack classes. Other hyperparameters are determined empirically to ensure real-time operation. To support the detection and classification of various IoV attacks, such as Denial-of-Service, Fuzzy, and Spoofing, DAIRE employs the sparse categorical cross-entropy loss function and root mean square propagation for loss minimization. In contrast to more resource-intensive architectures, DAIRE leverages a lightweight ANN to reduce computational demands while still delivering strong performance. Experimental results on the CICIoV2024 and Car-Hacking datasets demonstrate DAIRE's effectiveness, achieving an average detection rate of 99.88%, a false positive rate of 0.02%, and an overall accuracy of 99.96%. Furthermore, DAIRE significantly outperforms state-of-the-art approaches in inference speed, with a classification time of just 0.03 ms per sample. These results highlight DAIRE's effectiveness in detecting IoV cyberattacks and its practical suitability for real-time deployment in vehicular systems, underscoring its vital role in strengthening automotive cybersecurity.
匹配关键词: test-time compute
---

[ACADEMIC - ARXIV]
标题: Personalized electric vehicle energy consumption estimation framework that integrates driver behavior with map data
作者: Sreechakra Vasudeva Raju Rachavelpula, Sangwhan Cha
链接: https://arxiv.org/abs/2604.20764v1
完整摘要: This paper presents a personalized Battery Electric Vehicle (BEV) energy consumption estimation framework that integrates map-based contextual features with driver-specific velocity prediction and physics-based energy consumption modeling. The system combines route selection, detailed road feature processing, a rule-based reference velocity generator, a PID controller-based vehicle dynamics simulator, and a Bidirectional LSTM model trained to reproduce individual driving behavior. The predicted individual-specific velocity profiles are coupled with a quasi-steady backward energy consumption model to compute tractive power, regenerative braking, and State-of-Charge (SOC) evolution. Evaluation across urban, freeway, and hilly routes demonstrates that the proposed approach captures key driver behavioral patterns such as deceleration at intersections, speed-limit tracking, and road grade-dependent responses, while producing accurate power and SOC trajectories. The results highlight the effectiveness of combining learned driver behavior with map-based context and physics-based energy consumption modeling to produce accurate, personalized BEV SOC depletion profiles.
匹配关键词: test-time compute
---

[ACADEMIC - ARXIV]
标题: Exploring High-Order Self-Similarity for Video Understanding
作者: Manjin Kim, Heeseung Kwon, Karteek Alahari, Minsu Cho
链接: https://arxiv.org/abs/2604.20760v1
完整摘要: Space-time self-similarity (STSS), which captures visual correspondences across frames, provides an effective way to represent temporal dynamics for video understanding. In this work, we explore higher-order STSS and demonstrate how STSSs at different orders reveal distinct aspects of these dynamics. We then introduce the Multi-Order Self-Similarity (MOSS) module, a lightweight neural module designed to learn and integrate multi-order STSS features. It can be applied to diverse video tasks to enhance motion modeling capabilities while consuming only marginal computational cost and memory usage. Extensive experiments on video action recognition, motion-centric video VQA, and real-world robotic tasks consistently demonstrate substantial improvements, validating the broad applicability of MOSS as a general temporal modeling module. The source code and checkpoints will be publicly available.
匹配关键词: self-consistency
---

[ACADEMIC - ARXIV]
标题: Where Reasoning Breaks: Logic-Aware Path Selection by Controlling Logical Connectives in LLMs Reasoning Chains
作者: Seunghyun Park, Yuanyuan Lei
链接: https://arxiv.org/abs/2604.20564v1
完整摘要: While LLMs demonstrate impressive reasoning capabilities, they remain fragile in multi-step logical deduction, where a single transition error can propagate through the entire reasoning chain, leading to unstable performance. In this work, we identify logical connectives as primary points of this structural fragility. Through empirical analysis, we show that connective tokens function as high entropy forking points, at which models frequently struggle to determine the correct logical direction. Motivated by this observation, we hypothesize that intervening in logical connective selection can guide LLMs toward more correct logical direction, thereby improving the overall reasoning chain. To validate this hypothesis, we propose a multi-layered framework that intervenes specifically at these logic-critical junctions in the reasoning process. Our framework includes (1) Gradient-based Logical Steering to guide LLMs internal representations towards valid reasoning subspaces, (2) Localized Branching to resolve ambiguity via targeted look-ahead search, and (3) Targeted Transition Preference Optimization, a surgical reinforcement learning objective that selectively optimizes single-token preferences at logical pivots. Crucially, by concentrating intervention solely on logic-critical transitions, our framework achieves a favorable accuracy--efficiency trade-off compared to global inference time scaling methods like beam search and self-consistency.
匹配关键词: self-consistency
---

[ACADEMIC - ARXIV]
标题: Efficient Test-Time Inference via Deterministic Exploration of Truncated Decoding Trees
作者: Xueyan Li, Johannes Zenn, Ekaterina Fadeeva, Guinan Su, Mrinmaya Sachan, Jonas Geiping
链接: https://arxiv.org/abs/2604.20500v1
完整摘要: Self-consistency boosts inference-time performance by sampling multiple reasoning traces in parallel and voting. However, in constrained domains like math and code, this strategy is compute-inefficient because it samples with replacement, repeatedly revisiting the same high-probability prefixes and duplicate completions. We propose Distinct Leaf Enumeration (DLE), a deterministic decoding method that treats truncated sampling as traversal of a pruned decoding tree and systematically enumerates distinct leaves instead of sampling with replacement. This strategy improves inference efficiency in two ways. Algorithmically, it increases coverage of the truncated search space under a fixed budget by exploring previously unvisited high-probability branches. Systemically, it reuses shared prefixes and reduces redundant token generation. Empirically, DLE explores higher-quality reasoning traces than stochastic self-consistency, yielding better performance on math, coding, and general reasoning tasks.
匹配关键词: self-consistency
---

[ACADEMIC - ARXIV]
标题: Text-to-Distribution Prediction with Quantile Tokens and Neighbor Context
作者: Yilun Zhu, Yuan Zhuang, Nikhita Vedula, Dushyanta Dhyani, Shaoyuan Xu, Moyan Li, Mohsen Bayati, Bryan Wang, Shervin Malmasi
链接: https://arxiv.org/abs/2604.20216v1
完整摘要: Many applications of LLM-based text regression require predicting a full conditional distribution rather than a single point value. We study distributional regression under empirical-quantile supervision, where each input is paired with multiple observed quantile outcomes, and the target distribution is represented by a dense grid of quantiles. We address two key limitations of current approaches: the lack of local grounding for distribution estimates, and the reliance on shared representations that create an indirect bottleneck between inputs and quantile outputs. In this paper, we introduce Quantile Token Regression, which, to our knowledge, is the first work to insert dedicated quantile tokens into the input sequence, enabling direct input-output pathways for each quantile through self-attention. We further augment these quantile tokens with retrieval, incorporating semantically similar neighbor instances and their empirical distributions to ground predictions with local evidence from similar instances. We also provide the first theoretical analysis of loss functions for quantile regression, clarifying which distributional objectives each optimizes. Experiments on the Inside Airbnb and StackSample benchmark datasets with LLMs ranging from 1.7B to 14B parameters show that quantile tokens with neighbors consistently outperform baselines (~4 points lower MAPE and 2x narrower prediction intervals), with especially large gains on smaller and more challenging datasets where quantile tokens produce substantially sharper and more accurate distributions.
匹配关键词: self-consistency
---

[ACADEMIC - ARXIV]
标题: DeVI: Physics-based Dexterous Human-Object Interaction via Synthetic Video Imitation
作者: Hyeonwoo Kim, Jeonghwan Kim, Kyungwon Cho, Hanbyul Joo
链接: https://arxiv.org/abs/2604.20841v1
完整摘要: Recent advances in video generative models enable the synthesis of realistic human-object interaction videos across a wide range of scenarios and object categories, including complex dexterous manipulations that are difficult to capture with motion capture systems. While the rich interaction knowledge embedded in these synthetic videos holds strong potential for motion planning in dexterous robotic manipulation, their limited physical fidelity and purely 2D nature make them difficult to use directly as imitation targets in physics-based character control. We present DeVI (Dexterous Video Imitation), a novel framework that leverages text-conditioned synthetic videos to enable physically plausible dexterous agent control for interacting with unseen target objects. To overcome the imprecision of generative 2D cues, we introduce a hybrid tracking reward that integrates 3D human tracking with robust 2D object tracking. Unlike methods relying on high-quality 3D kinematic demonstrations, DeVI requires only the generated video, enabling zero-shot generalization across diverse objects and interaction types. Extensive experiments demonstrate that DeVI outperforms existing approaches that imitate 3D human-object interaction demonstrations, particularly in modeling dexterous hand-object interactions. We further validate the effectiveness of DeVI in multi-object scenes and text-driven action diversity, showcasing the advantage of using video as an HOI-aware motion planner.
匹配关键词: process reward
---

[ACADEMIC - ARXIV]
标题: ParetoSlider: Diffusion Models Post-Training for Continuous Reward Control
作者: Shelly Golan, Michael Finkelson, Ariel Bereslavsky, Yotam Nitzan, Or Patashnik
链接: https://arxiv.org/abs/2604.20816v1
完整摘要: Reinforcement Learning (RL) post-training has become the standard for aligning generative models with human preferences, yet most methods rely on a single scalar reward. When multiple criteria matter, the prevailing practice of ``early scalarization'' collapses rewards into a fixed weighted sum. This commits the model to a single trade-off point at training time, providing no inference-time control over inherently conflicting goals -- such as prompt adherence versus source fidelity in image editing. We introduce ParetoSlider, a multi-objective RL (MORL) framework that trains a single diffusion model to approximate the entire Pareto front. By training the model with continuously varying preference weights as a conditioning signal, we enable users to navigate optimal trade-offs at inference time without retraining or maintaining multiple checkpoints. We evaluate ParetoSlider across three state-of-the-art flow-matching backbones: SD3.5, FluxKontext, and LTX-2. Our single preference-conditioned model matches or exceeds the performance of baselines trained separately for fixed reward trade-offs, while uniquely providing fine-grained control over competing generative goals.
匹配关键词: process reward
---

[ACADEMIC - ARXIV]
标题: Relative Principals, Pluralistic Alignment, and the Structural Value Alignment Problem
作者: Travis LaCroix
链接: https://arxiv.org/abs/2604.20805v1
完整摘要: The value alignment problem for artificial intelligence (AI) is often framed as a purely technical or normative challenge, sometimes focused on hypothetical future systems. I argue that the problem is better understood as a structural question about governance: not whether an AI system is aligned in the abstract, but whether it is aligned enough, for whom, and at what cost. Drawing on the principal-agent framework from economics, this paper reconceptualises misalignment as arising along three interacting axes: objectives, information, and principals. The three-axis framework provides a systematic way of diagnosing why misalignment arises in real-world systems and clarifies that alignment cannot be treated as a single technical property of models but an outcome shaped by how objectives are specified, how information is distributed, and whose interests count in practice. The core contribution of this paper is to show that the three-axis decomposition implies that alignment is fundamentally a problem of governance rather than engineering alone. From this perspective, alignment is inherently pluralistic and context-dependent, and resolving misalignment involves trade-offs among competing values. Because misalignment can occur along each axis -- and affect stakeholders differently -- the structural description shows that alignment cannot be "solved" through technical design alone, but must be managed through ongoing institutional processes that determine how objectives are set, how systems are evaluated, and how affected communities can contest or reshape those decisions.
匹配关键词: process reward
---

[ACADEMIC - ARXIV]
标题: A Hough transform approach to safety-aware scalar field mapping using Gaussian Processes
作者: Muzaffar Qureshi, Trivikram Satharasi, Tochukwu E. Ogri, Kyle Volle, Rushikesh Kamalapurkar
链接: https://arxiv.org/abs/2604.20799v1
完整摘要: This paper presents a framework for mapping unknown scalar fields using a sensor-equipped autonomous robot operating in unsafe environments. The unsafe regions are defined as regions of high-intensity, where the field value exceeds a predefined safety threshold. For safe and efficient mapping of the scalar field, the sensor-equipped robot must avoid high-intensity regions during the measurement process. In this paper, the scalar field is modeled as a sample from a Gaussian process (GP), which enables Bayesian inference and provides closed-form expressions for both the predictive mean and the uncertainty. Concurrently, the spatial structure of the high-intensity regions is estimated in real-time using the Hough transform (HT), leveraging the evolving GP posterior. A safe sampling strategy is then employed to guide the robot towards safe measurement locations, using probabilistic safety guarantees on the evolving GP posterior. The estimated high-intensity regions also facilitate the design of safe motion plans for the robot. The effectiveness of the approach is verified through two numerical simulation studies and an indoor experiment for mapping a light-intensity field using a wheeled mobile robot.
匹配关键词: process reward
---

[ACADEMIC - ARXIV]
标题: Working Memory Constraints Scaffold Learning in Transformers under Data Scarcity
作者: Pranava Madhyastha, Dagmar Adamcova
链接: https://arxiv.org/abs/2604.20789v1
完整摘要: We investigate the integration of human-like working memory constraints into the Transformer architecture and implement several cognitively inspired attention variants, including fixed-width windows based and temporal decay based attention mechanisms. Our modified GPT-2 models are trained from scratch on developmentally plausible datasets (10M and 100M words). Performance is evaluated on grammatical judgment tasks (BLiMP) and alignment with human reading time data. Our results indicate that these cognitively-inspired constraints, particularly fixed-width attention, can significantly improve grammatical accuracy especially when training data is scarce. These constrained models also tend to show a stronger alignment with human processing metrics. The findings suggest that such constraints may serve as a beneficial inductive bias, guiding models towards more robust linguistic representations, especially in data-limited settings.
匹配关键词: process reward
---

[ACADEMIC - ARXIV]
标题: Physics-Conditioned Synthesis of Internal Ice-Layer Thickness for Incomplete Layer Traces
作者: Zesheng Liu, Maryam Rahnemoonfar
链接: https://arxiv.org/abs/2604.20783v1
完整摘要: Internal ice layers imaged by radar provide key evidence of snow accumulation and ice dynamics, but radar-derived layer boundary observations are often incomplete, with discontinuous traces and sometimes entirely missing layers, due to limited resolution, sensor noise, and signal loss. Existing graph-based models for ice stratigraphy generally assume sufficiently complete layer profiles and focus on predicting deeper-layer thickness from reliably traced shallow layers. In this work, we address the layer-completion problem itself by synthesizing complete ice-layer thickness annotations from incomplete radar-derived layer traces by conditioning on colocated physical features synchronized from physical climate models. The proposed network combines geometric learning to aggregate within-layer spatial context with a transformer-based temporal module that propagates information across layers to encourage coherent stratigraphy and consistent thickness evolution. To learn from incomplete supervision, we optimize a mask-aware robust regression objective that evaluates errors only at observed thickness values and normalizes by the number of valid entries, enabling stable training under varying sparsity without imputation and steering completions toward physically plausible values. The model preserves observed thickness where available and infers only missing regions, recovering fragmented segments and even fully absent layers while remaining consistent with measured traces. As an additional benefit, the synthesized thickness stacks provide effective pretraining supervision for a downstream deep-layer predictor, improving fine-tuned accuracy over training from scratch on the same fully traced data.
匹配关键词: pretraining
---

[ACADEMIC - ARXIV]
标题: Toward Cross-Lingual Quality Classifiers for Multilingual Pretraining Data Selection
作者: Yassine Turki, Vinko Sabolčec, Bettina Messmer, Martin Jaggi
链接: https://arxiv.org/abs/2604.20549v1
完整摘要: As Large Language Models (LLMs) scale, data curation has shifted from maximizing volume to optimizing the signal-to-noise ratio by performing quality filtering. However, for many languages, native high quality data is insufficient to train robust quality classifiers. This work investigates the idea that quality markers in embedding space may show cross-lingual consistency, which would allow high-resource languages to subsidize the filtering of low-resource ones. We evaluate various filtering strategies, including cross-lingual transfer, third quartile sampling (Q3), and retention rate tuning. Our results demonstrate that massive multilingual pooling frequently outperforms monolingual baselines in both rank stability and aggregate accuracy for a 1B model trained on 103B tokens, delivering gains for high resource languages (1.2% increase in aggregate normalized accuracy for French) and matching or exceeding monolingual baselines for low-resource languages. However, we find that scale alone does not guarantee stability. Furthermore, for high-resource languages like French, we show that refining the decision boundary through third quartile sampling (Q3) or tuning the retention rate is necessary to fully leverage the multilingual signal.
匹配关键词: pretraining
---

[ACADEMIC - ARXIV]
标题: Video-ToC: Video Tree-of-Cue Reasoning
作者: Qizhong Tan, Zhuotao Tian, Guangming Lu, Jun Yu, Wenjie Pei
链接: https://arxiv.org/abs/2604.20473v1
完整摘要: Existing Video Large Language Models (Video LLMs) struggle with complex video understanding, exhibiting limited reasoning capabilities and potential hallucinations. In particular, these methods tend to perform reasoning solely relying on the pretrained inherent reasoning rationales whilst lacking perception-aware adaptation to the input video content. To address this, we propose \textbf{Video-ToC}, a novel video reasoning framework that enhances video understanding through tree-of-cue reasoning. Specifically, our approach introduces three key innovations: (1) A tree-guided visual cue localization mechanism, which endows the model with enhanced fine-grained perceptual capabilities through structured reasoning patterns; (2) A reasoning-demand reward mechanism, which dynamically adjusts the reward value for reinforcement learning (RL) based on the estimation of reasoning demands, enabling on-demand incentives for more effective reasoning strategies; and (3) An automated annotation pipeline that constructs the Video-ToC-SFT-1k and Video-ToC-RL-2k datasets for supervised fine-tuning (SFT) and RL training, respectively. Extensive evaluations on six video understanding benchmarks and a video hallucination benchmark demonstrate the superiority of Video-ToC over baselines and recent methods. Code is available at https://github.com/qizhongtan/Video-ToC.
匹配关键词: pretraining
---

[ACADEMIC - ARXIV]
标题: Self-supervised pretraining for an iterative image size agnostic vision transformer
作者: Nedyalko Prisadnikov, Danda Pani Paudel, Yuqian Fu, Luc Van Gool
链接: https://arxiv.org/abs/2604.20392v1
完整摘要: Vision Transformers (ViTs) dominate self-supervised learning (SSL). While they have proven highly effective for large-scale pretraining, they are computationally inefficient and scale poorly with image size. Consequently, foundational models like DINO are constrained to low-resolution processing. A recent foveal-inspired transformer achieves resolution agnosticism by iteratively processing a fixed-size context of multi-zoom patches. This model demonstrated promising results via supervised learning, utilizing a sequential, recurrent-like process without backpropagation through time. To unlock its potential as a foundational backbone, we introduce a novel sequential-to-global SSL framework based on DINO's self-distillation objective. Supported by an efficient integral-image patch extraction method, our approach enables large-scale pretraining for image-size agnostic vision encoders. We achieve competitive performance on ImageNet-1K and downstream classification tasks, maintaining a constant computational budget regardless of input resolution.
匹配关键词: pretraining
---

[ACADEMIC - ARXIV]
标题: A Vision-Language-Action Model for Adaptive Ultrasound-Guided Needle Insertion and Needle Tracking
作者: Yuelin Zhang, Qingpeng Ding, Longxiang Tang, Chengyu Fang, Shing Shin Cheng
链接: https://arxiv.org/abs/2604.20347v1
完整摘要: Ultrasound (US)-guided needle insertion is a critical yet challenging procedure due to dynamic imaging conditions and difficulties in needle visualization. Many methods have been proposed for automated needle insertion, but they often rely on hand-crafted pipelines with modular controllers, whose performance degrades in challenging cases. In this paper, a Vision-Language-Action (VLA) model is proposed for adaptive and automated US-guided needle insertion and tracking on a robotic ultrasound (RUS) system. This framework provides a unified approach to needle tracking and needle insertion control, enabling real-time, dynamically adaptive adjustment of insertion based on the obtained needle position and environment awareness. To achieve real-time and end-to-end tracking, a Cross-Depth Fusion (CDF) tracking head is proposed, integrating shallow positional and deep semantic features from the large-scale vision backbone. To adapt the pretrained vision backbone for tracking tasks, a Tracking-Conditioning (TraCon) register is introduced for parameter-efficient feature conditioning. After needle tracking, an uncertainty-aware control policy and an asynchronous VLA pipeline are presented for adaptive needle insertion control, ensuring timely decision-making for improved safety and outcomes. Extensive experiments on both needle tracking and insertion show that our method consistently outperforms state-of-the-art trackers and manual operation, achieving higher tracking accuracy, improved insertion success rates, and reduced procedure time, highlighting promising directions for RUS-based intelligent intervention.
匹配关键词: pretraining
---

[ACADEMIC - ARXIV]
标题: SpeechParaling-Bench: A Comprehensive Benchmark for Paralinguistic-Aware Speech Generation
作者: Ruohan Liu, Shukang Yin, Tao Wang, Dong Zhang, Weiji Zhuang, Shuhuai Ren, Ran He, Caifeng Shan, Chaoyou Fu
链接: https://arxiv.org/abs/2604.20842v1
完整摘要: Paralinguistic cues are essential for natural human-computer interaction, yet their evaluation in Large Audio-Language Models (LALMs) remains limited by coarse feature coverage and the inherent subjectivity of assessment. To address these challenges, we introduce SpeechParaling-Bench, a comprehensive benchmark for paralinguistic-aware speech generation. It expands existing coverage from fewer than 50 to over 100 fine-grained features, supported by more than 1,000 English-Chinese parallel speech queries, and is organized into three progressively challenging tasks: fine-grained control, intra-utterance variation, and context-aware adaptation. To enable reliable evaluation, we further develop a pairwise comparison pipeline, in which candidate responses are evaluated against a fixed baseline by an LALM-based judge. By framing evaluation as relative preference rather than absolute scoring, this approach mitigates subjectivity and yields more stable and scalable assessments without costly human annotation. Extensive experiments reveal substantial limitations in current LALMs. Even leading proprietary models struggle with comprehensive static control and dynamic modulation of paralinguistic features, while failure to correctly interpret paralinguistic cues accounts for 43.3% of errors in situational dialogue. These findings underscore the need for more robust paralinguistic modeling toward human-aligned voice assistants.
匹配关键词: foundation model
---

[ACADEMIC - ARXIV]
标题: DeVI: Physics-based Dexterous Human-Object Interaction via Synthetic Video Imitation
作者: Hyeonwoo Kim, Jeonghwan Kim, Kyungwon Cho, Hanbyul Joo
链接: https://arxiv.org/abs/2604.20841v1
完整摘要: Recent advances in video generative models enable the synthesis of realistic human-object interaction videos across a wide range of scenarios and object categories, including complex dexterous manipulations that are difficult to capture with motion capture systems. While the rich interaction knowledge embedded in these synthetic videos holds strong potential for motion planning in dexterous robotic manipulation, their limited physical fidelity and purely 2D nature make them difficult to use directly as imitation targets in physics-based character control. We present DeVI (Dexterous Video Imitation), a novel framework that leverages text-conditioned synthetic videos to enable physically plausible dexterous agent control for interacting with unseen target objects. To overcome the imprecision of generative 2D cues, we introduce a hybrid tracking reward that integrates 3D human tracking with robust 2D object tracking. Unlike methods relying on high-quality 3D kinematic demonstrations, DeVI requires only the generated video, enabling zero-shot generalization across diverse objects and interaction types. Extensive experiments demonstrate that DeVI outperforms existing approaches that imitate 3D human-object interaction demonstrations, particularly in modeling dexterous hand-object interactions. We further validate the effectiveness of DeVI in multi-object scenes and text-driven action diversity, showcasing the advantage of using video as an HOI-aware motion planner.
匹配关键词: foundation model
---

[ACADEMIC - ARXIV]
标题: Parallel-SFT: Improving Zero-Shot Cross-Programming-Language Transfer for Code RL
作者: Zhaofeng Wu, Shiqi Wang, Boya Peng, Anuj Goyal, Melanie Kambadur, Sebastian Ruder, Yoon Kim, Chloe Bi
链接: https://arxiv.org/abs/2604.20835v1
完整摘要: Modern language models demonstrate impressive coding capabilities in common programming languages (PLs), such as C++ and Python, but their performance in lower-resource PLs is often limited by training data availability. In principle, however, most programming skills are universal across PLs, so the capability acquired in one PL should transfer to others. In this work, we propose the task of zero-shot cross-programming-language transfer for code RL. We find that, for Llama-3.1, RL training for code generation in a source PL fails to improve, and sometimes even degrades, the performance on other target PLs. To address this, we hypothesize that effective RL transfer requires a generalizable SFT initialization before RL. We thus propose **Parallel-SFT**, an SFT strategy that incorporates "parallel programs" -- functionally equivalent code implemented in multiple PLs -- into the data mixture. We demonstrate that this improves transferability: when we subsequently perform RL on our Parallel-SFT model, we observe better generalization to unseen PLs. Analysis of the model internal representations reveals that Parallel-SFT leads to a more functionality-centric latent space, where equivalent programs across PLs are more tightly clustered, which we hypothesize to contribute to the improved transferability.
匹配关键词: foundation model
---

[ACADEMIC - ARXIV]
标题: PokeVLA: Empowering Pocket-Sized Vision-Language-Action Model with Comprehensive World Knowledge Guidance
作者: Yupeng Zheng, Xiang Li, Songen Gu, Yuhang Zheng, Shuai Tian, Weize Li, Linbo Wang, Senyu Fei, Pengfei Li, Yinfeng Gao, Zebin Xing, Yilun Chen, Qichao Zhang, Haoran Li, Wenchao Ding
链接: https://arxiv.org/abs/2604.20834v1
完整摘要: Recent advances in Vision-Language-Action (VLA) models have opened new avenues for robot manipulation, yet existing methods exhibit limited efficiency and a lack of high-level knowledge and spatial awareness. To address these challenges, we propose PokeVLA, a lightweight yet powerful foundation model for embodied manipulation that effectively infuses vision-language understanding into action learning. Our framework introduces a two-stage training paradigm: first, we pre-train a compact vision-language model (PokeVLM) on a curated multimodal dataset of 2.4M samples encompassing spatial grounding, affordance, and embodied reasoning tasks; second, we inject manipulation-relevant representations into the action space through multi-view goal-aware semantics learning, geometry alignment, and a novel action expert. Extensive experiments demonstrate state-of-the-art performance on the LIBERO-Plus benchmark and in real-world deployment, outperforming comparable baselines in success rate and robustness under diverse perturbations. To foster reproducibility and community progress, we will open-source our code, model weights, and the scripts for the curated pre-training dataset. Project page: https://getterupper.github.io/PokeVLA
匹配关键词: foundation model
---

[ACADEMIC - ARXIV]
标题: AVISE: Framework for Evaluating the Security of AI Systems
作者: Mikko Lempinen, Joni Kemppainen, Niklas Raesalmi
链接: https://arxiv.org/abs/2604.20833v1
完整摘要: As artificial intelligence (AI) systems are increasingly deployed across critical domains, their security vulnerabilities pose growing risks of high-profile exploits and consequential system failures. Yet systematic approaches to evaluating AI security remain underdeveloped. In this paper, we introduce AVISE (AI Vulnerability Identification and Security Evaluation), a modular open-source framework for identifying vulnerabilities in and evaluating the security of AI systems and models. As a demonstration of the framework, we extend the theory-of-mind-based multi-turn Red Queen attack into an Adversarial Language Model (ALM) augmented attack and develop an automated Security Evaluation Test (SET) for discovering jailbreak vulnerabilities in language models. The SET comprises 25 test cases and an Evaluation Language Model (ELM) that determines whether each test case was able to jailbreak the target model, achieving 92% accuracy, an F1-score of 0.91, and a Matthews correlation coefficient of 0.83. We evaluate nine recently released language models of diverse sizes with the SET and find that all are vulnerable to the augmented Red Queen attack to varying degrees. AVISE provides researchers and industry practitioners with an extensible foundation for developing and deploying automated SETs, offering a concrete step toward more rigorous and reproducible AI security evaluation.
匹配关键词: foundation model
---

[ACADEMIC - ARXIV]
标题: Closing the Domain Gap in Biomedical Imaging by In-Context Control Samples
作者: Ana Sanchez-Fernandez, Thomas Pinetz, Werner Zellinger, Günter Klambauer
链接: https://arxiv.org/abs/2604.20824v1
完整摘要: The central problem in biomedical imaging are batch effects: systematic technical variations unrelated to the biological signal of interest. These batch effects critically undermine experimental reproducibility and are the primary cause of failure of deep learning systems on new experimental batches, preventing their practical use in the real world. Despite years of research, no method has succeeded in closing this performance gap for deep learning models. We propose Control-Stabilized Adaptive Risk Minimization via Batch Normalization (CS-ARM-BN), a meta-learning adaptation method that exploits negative control samples. Such unperturbed reference images are present in every experimental batch by design and serve as stable context for adaptation. We validate our novel method on Mechanism-of-Action (MoA) classification, a crucial task for drug discovery, on the large-scale JUMP-CP dataset. The accuracy of standard ResNets drops from 0.939 $\pm$ 0.005, on the training domain, to 0.862 $\pm$ 0.060 on data from new experimental batches. Foundation models, even after Typical Variation Normalization, fail to close this gap. We are the first to show that meta-learning approaches close the domain gap by achieving 0.935 $\pm$ 0.018. If the new experimental batches exhibit strong domain shifts, such as being generated in a different lab, meta-learning approaches can be stabilized with control samples, which are always available in biomedical experiments. Our work shows that batch effects in bioimaging data can be effectively neutralized through principled in-context adaptation, which also makes them practically usable and efficient.
匹配关键词: scaling law
---

[ACADEMIC - ARXIV]
标题: Global Offshore Wind Infrastructure: Deployment and Operational Dynamics from Dense Sentinel-1 Time Series
作者: Thorsten Hoeser, Felix Bachofer, Claudia Kuenzer
链接: https://arxiv.org/abs/2604.20822v1
完整摘要: The offshore wind energy sector is expanding rapidly, increasing the need for independent, high-temporal-resolution monitoring of infrastructure deployment and operation at global scale. While Earth Observation based offshore wind infrastructure mapping has matured for spatial localization, existing open datasets lack temporally dense and semantically fine-grained information on construction and operational dynamics. We introduce a global Sentinel-1 synthetic aperture radar (SAR) time series data corpus that resolves deployment and operational phases of offshore wind infrastructure from 2016Q1 to 2025Q1. Building on an updated object detection workflow, we compile 15,606 time series at detected infrastructure locations, with overall 14,840,637 events as analysis-ready 1D SAR backscatter profiles, one profile per Sentinel-1 acquisition and location. To enable direct use and benchmarking, we release (i) the analysis ready 1D SAR profiles, (ii) event-level baseline semantic labels generated by a rule-based classifier, and (iii) an expert-annotated benchmark dataset of 553 time series with 328,657 event labels. The baseline classifier achieves a macro F1 score of 0.84 in event-wise evaluation and an area under the collapsed edit similarity-quality threshold curve (AUC) of 0.785, indicating temporal coherence. We demonstrate that the resulting corpus supports global-scale analyses of deployment dynamics, the identification of differences in regional deployment patterns, vessel interactions, and operational events, and provides a reference for developing and comparing time series classification methods for offshore wind infrastructure monitoring.
匹配关键词: scaling law
---

[ACADEMIC - ARXIV]
标题: Stream-CQSA: Avoiding Out-of-Memory in Attention Computation via Flexible Workload Scheduling
作者: Yiming Bian, Joshua M. Akey
链接: https://arxiv.org/abs/2604.20819v1
完整摘要: The scalability of long-context large language models is fundamentally limited by the quadratic memory cost of exact self-attention, which often leads to out-of-memory (OOM) failures on modern hardware. Existing methods improve memory efficiency to near-linear complexity, while assuming that the full query, key, and value tensors fit in device memory. In this work, we remove this assumption by introducing CQS Divide, an operation derived from cyclic quorum sets (CQS) theory that decomposes attention into a set of independent subsequence computations whose recomposition yields exactly the same result as full-sequence attention. Exploiting this decomposition, we introduce Stream-CQSA, a memory-adaptive scheduling framework that partitions attention into subproblems that fit within arbitrary memory budgets. This recasts attention from a logically monolithic operation into a collection of schedulable tasks, enabling flexible execution across devices without inter-device communication. Experiments demonstrate predictable memory scaling and show that exact attention over billion-token sequences can be executed on a single GPU via streaming, without changing the underlying mathematical definition of attention or introducing approximation error.
匹配关键词: scaling law
---

[ACADEMIC - ARXIV]
标题: LLaDA2.0-Uni: Unifying Multimodal Understanding and Generation with Diffusion Large Language Model
作者: Inclusion AI, Tiwei Bie, Haoxing Chen, Tieyuan Chen, Zhenglin Cheng, Long Cui, Kai Gan, Zhicheng Huang, Zhenzhong Lan, Haoquan Li, Jianguo Li, Tao Lin, Qi Qin, Hongjun Wang, Xiaomei Wang, Haoyuan Wu, Yi Xin, Junbo Zhao
链接: https://arxiv.org/abs/2604.20796v1
完整摘要: We present LLaDA2.0-Uni, a unified discrete diffusion large language model (dLLM) that supports multimodal understanding and generation within a natively integrated framework. Its architecture combines a fully semantic discrete tokenizer, a MoE-based dLLM backbone, and a diffusion decoder. By discretizing continuous visual inputs via SigLIP-VQ, the model enables block-level masked diffusion for both text and vision inputs within the backbone, while the decoder reconstructs visual tokens into high-fidelity images. Inference efficiency is enhanced beyond parallel decoding through prefix-aware optimizations in the backbone and few-step distillation in the decoder. Supported by carefully curated large-scale data and a tailored multi-stage training pipeline, LLaDA2.0-Uni matches specialized VLMs in multimodal understanding while delivering strong performance in image generation and editing. Its native support for interleaved generation and reasoning establishes a promising and scalable paradigm for next-generation unified foundation models. Codes and models are available at https://github.com/inclusionAI/LLaDA2.0-Uni.
匹配关键词: scaling law
---

[ACADEMIC - ARXIV]
标题: SWE-chat: Coding Agent Interactions From Real Users in the Wild
作者: Joachim Baumann, Vishakh Padmakumar, Xiang Li, John Yang, Diyi Yang, Sanmi Koyejo
链接: https://arxiv.org/abs/2604.20779v1
完整摘要: AI coding agents are being adopted at scale, yet we lack empirical evidence on how people actually use them and how much of their output is useful in practice. We present SWE-chat, the first large-scale dataset of real coding agent sessions collected from open-source developers in the wild. The dataset currently contains 6,000 sessions, comprising more than 63,000 user prompts and 355,000 agent tool calls. SWE-chat is a living dataset; our collection pipeline automatically and continually discovers and processes sessions from public repositories. Leveraging SWE-chat, we provide an initial empirical characterization of real-world coding agent usage and failure modes. We find that coding patterns are bimodal: in 41% of sessions, agents author virtually all committed code ("vibe coding"), while in 23%, humans write all code themselves. Despite rapidly improving capabilities, coding agents remain inefficient in natural settings. Just 44% of all agent-produced code survives into user commits, and agent-written code introduces more security vulnerabilities than code authored by humans. Furthermore, users push back against agent outputs -- through corrections, failure reports, and interruptions -- in 44% of all turns. By capturing complete interaction traces with human vs. agent code authorship attribution, SWE-chat provides an empirical foundation for moving beyond curated benchmarks towards an evidence-based understanding of how AI agents perform in real developer workflows.
匹配关键词: scaling law
---

[ACADEMIC - ARXIV]
标题: SpeechParaling-Bench: A Comprehensive Benchmark for Paralinguistic-Aware Speech Generation
作者: Ruohan Liu, Shukang Yin, Tao Wang, Dong Zhang, Weiji Zhuang, Shuhuai Ren, Ran He, Caifeng Shan, Chaoyou Fu
链接: https://arxiv.org/abs/2604.20842v1
完整摘要: Paralinguistic cues are essential for natural human-computer interaction, yet their evaluation in Large Audio-Language Models (LALMs) remains limited by coarse feature coverage and the inherent subjectivity of assessment. To address these challenges, we introduce SpeechParaling-Bench, a comprehensive benchmark for paralinguistic-aware speech generation. It expands existing coverage from fewer than 50 to over 100 fine-grained features, supported by more than 1,000 English-Chinese parallel speech queries, and is organized into three progressively challenging tasks: fine-grained control, intra-utterance variation, and context-aware adaptation. To enable reliable evaluation, we further develop a pairwise comparison pipeline, in which candidate responses are evaluated against a fixed baseline by an LALM-based judge. By framing evaluation as relative preference rather than absolute scoring, this approach mitigates subjectivity and yields more stable and scalable assessments without costly human annotation. Extensive experiments reveal substantial limitations in current LALMs. Even leading proprietary models struggle with comprehensive static control and dynamic modulation of paralinguistic features, while failure to correctly interpret paralinguistic cues accounts for 43.3% of errors in situational dialogue. These findings underscore the need for more robust paralinguistic modeling toward human-aligned voice assistants.
匹配关键词: language model
---

[ACADEMIC - ARXIV]
标题: DeVI: Physics-based Dexterous Human-Object Interaction via Synthetic Video Imitation
作者: Hyeonwoo Kim, Jeonghwan Kim, Kyungwon Cho, Hanbyul Joo
链接: https://arxiv.org/abs/2604.20841v1
完整摘要: Recent advances in video generative models enable the synthesis of realistic human-object interaction videos across a wide range of scenarios and object categories, including complex dexterous manipulations that are difficult to capture with motion capture systems. While the rich interaction knowledge embedded in these synthetic videos holds strong potential for motion planning in dexterous robotic manipulation, their limited physical fidelity and purely 2D nature make them difficult to use directly as imitation targets in physics-based character control. We present DeVI (Dexterous Video Imitation), a novel framework that leverages text-conditioned synthetic videos to enable physically plausible dexterous agent control for interacting with unseen target objects. To overcome the imprecision of generative 2D cues, we introduce a hybrid tracking reward that integrates 3D human tracking with robust 2D object tracking. Unlike methods relying on high-quality 3D kinematic demonstrations, DeVI requires only the generated video, enabling zero-shot generalization across diverse objects and interaction types. Extensive experiments demonstrate that DeVI outperforms existing approaches that imitate 3D human-object interaction demonstrations, particularly in modeling dexterous hand-object interactions. We further validate the effectiveness of DeVI in multi-object scenes and text-driven action diversity, showcasing the advantage of using video as an HOI-aware motion planner.
匹配关键词: language model
---

[ACADEMIC - ARXIV]
标题: Parallel-SFT: Improving Zero-Shot Cross-Programming-Language Transfer for Code RL
作者: Zhaofeng Wu, Shiqi Wang, Boya Peng, Anuj Goyal, Melanie Kambadur, Sebastian Ruder, Yoon Kim, Chloe Bi
链接: https://arxiv.org/abs/2604.20835v1
完整摘要: Modern language models demonstrate impressive coding capabilities in common programming languages (PLs), such as C++ and Python, but their performance in lower-resource PLs is often limited by training data availability. In principle, however, most programming skills are universal across PLs, so the capability acquired in one PL should transfer to others. In this work, we propose the task of zero-shot cross-programming-language transfer for code RL. We find that, for Llama-3.1, RL training for code generation in a source PL fails to improve, and sometimes even degrades, the performance on other target PLs. To address this, we hypothesize that effective RL transfer requires a generalizable SFT initialization before RL. We thus propose **Parallel-SFT**, an SFT strategy that incorporates "parallel programs" -- functionally equivalent code implemented in multiple PLs -- into the data mixture. We demonstrate that this improves transferability: when we subsequently perform RL on our Parallel-SFT model, we observe better generalization to unseen PLs. Analysis of the model internal representations reveals that Parallel-SFT leads to a more functionality-centric latent space, where equivalent programs across PLs are more tightly clustered, which we hypothesize to contribute to the improved transferability.
匹配关键词: language model
---

[ACADEMIC - ARXIV]
标题: PokeVLA: Empowering Pocket-Sized Vision-Language-Action Model with Comprehensive World Knowledge Guidance
作者: Yupeng Zheng, Xiang Li, Songen Gu, Yuhang Zheng, Shuai Tian, Weize Li, Linbo Wang, Senyu Fei, Pengfei Li, Yinfeng Gao, Zebin Xing, Yilun Chen, Qichao Zhang, Haoran Li, Wenchao Ding
链接: https://arxiv.org/abs/2604.20834v1
完整摘要: Recent advances in Vision-Language-Action (VLA) models have opened new avenues for robot manipulation, yet existing methods exhibit limited efficiency and a lack of high-level knowledge and spatial awareness. To address these challenges, we propose PokeVLA, a lightweight yet powerful foundation model for embodied manipulation that effectively infuses vision-language understanding into action learning. Our framework introduces a two-stage training paradigm: first, we pre-train a compact vision-language model (PokeVLM) on a curated multimodal dataset of 2.4M samples encompassing spatial grounding, affordance, and embodied reasoning tasks; second, we inject manipulation-relevant representations into the action space through multi-view goal-aware semantics learning, geometry alignment, and a novel action expert. Extensive experiments demonstrate state-of-the-art performance on the LIBERO-Plus benchmark and in real-world deployment, outperforming comparable baselines in success rate and robustness under diverse perturbations. To foster reproducibility and community progress, we will open-source our code, model weights, and the scripts for the curated pre-training dataset. Project page: https://getterupper.github.io/PokeVLA
匹配关键词: language model
---

[ACADEMIC - ARXIV]
标题: AVISE: Framework for Evaluating the Security of AI Systems
作者: Mikko Lempinen, Joni Kemppainen, Niklas Raesalmi
链接: https://arxiv.org/abs/2604.20833v1
完整摘要: As artificial intelligence (AI) systems are increasingly deployed across critical domains, their security vulnerabilities pose growing risks of high-profile exploits and consequential system failures. Yet systematic approaches to evaluating AI security remain underdeveloped. In this paper, we introduce AVISE (AI Vulnerability Identification and Security Evaluation), a modular open-source framework for identifying vulnerabilities in and evaluating the security of AI systems and models. As a demonstration of the framework, we extend the theory-of-mind-based multi-turn Red Queen attack into an Adversarial Language Model (ALM) augmented attack and develop an automated Security Evaluation Test (SET) for discovering jailbreak vulnerabilities in language models. The SET comprises 25 test cases and an Evaluation Language Model (ELM) that determines whether each test case was able to jailbreak the target model, achieving 92% accuracy, an F1-score of 0.91, and a Matthews correlation coefficient of 0.83. We evaluate nine recently released language models of diverse sizes with the SET and find that all are vulnerable to the augmented Red Queen attack to varying degrees. AVISE provides researchers and industry practitioners with an extensible foundation for developing and deploying automated SETs, offering a concrete step toward more rigorous and reproducible AI security evaluation.
匹配关键词: language model
---

[ACADEMIC - ARXIV]
标题: Convergent Evolution: How Different Language Models Learn Similar Number Representations
作者: Deqing Fu, Tianyi Zhou, Mikhail Belkin, Vatsal Sharan, Robin Jia
链接: https://arxiv.org/abs/2604.20817v1
完整摘要: Language models trained on natural text learn to represent numbers using periodic features with dominant periods at $T=2, 5, 10$. In this paper, we identify a two-tiered hierarchy of these features: while Transformers, Linear RNNs, LSTMs, and classical word embeddings trained in different ways all learn features that have period-$T$ spikes in the Fourier domain, only some learn geometrically separable features that can be used to linearly classify a number mod-$T$. To explain this incongruity, we prove that Fourier domain sparsity is necessary but not sufficient for mod-$T$ geometric separability. Empirically, we investigate when model training yields geometrically separable features, finding that the data, architecture, optimizer, and tokenizer all play key roles. In particular, we identify two different routes through which models can acquire geometrically separable features: they can learn them from complementary co-occurrence signals in general language data, including text-number co-occurrence and cross-number interaction, or from multi-token (but not single-token) addition problems. Overall, our results highlight the phenomenon of convergent evolution in feature learning: A diverse range of models learn similar features from different training signals.
匹配关键词: transformer architecture
---

[ACADEMIC - ARXIV]
标题: Adapting TrOCR for Printed Tigrinya Text Recognition: Word-Aware Loss Weighting for Cross-Script Transfer Learning
作者: Yonatan Haile Medhanie, Yuanhua Ni
链接: https://arxiv.org/abs/2604.20813v1
完整摘要: Transformer-based OCR models have shown strong performance on Latin and CJK scripts, but their application to African syllabic writing systems remains limited. We present the first adaptation of TrOCR for printed Tigrinya using the Ge'ez script. Starting from a pre-trained model, we extend the byte-level BPE tokenizer to cover 230 Ge'ez characters and introduce Word-Aware Loss Weighting to resolve systematic word-boundary failures that arise when applying Latin-centric BPE conventions to a new script. The unmodified model produces no usable output on Ge'ez text. After adaptation, the TrOCR-Printed variant achieves 0.22% Character Error Rate and 97.20% exact match accuracy on a held-out test set of 5,000 synthetic images from the GLOCR dataset. An ablation study confirms that Word-Aware Loss Weighting is the critical component, reducing CER by two orders of magnitude compared to vocabulary extension alone. The full pipeline trains in under three hours on a single 8 GB consumer GPU. All code, model weights, and evaluation scripts are publicly released.
匹配关键词: transformer architecture
---

[ACADEMIC - ARXIV]
标题: A Hough transform approach to safety-aware scalar field mapping using Gaussian Processes
作者: Muzaffar Qureshi, Trivikram Satharasi, Tochukwu E. Ogri, Kyle Volle, Rushikesh Kamalapurkar
链接: https://arxiv.org/abs/2604.20799v1
完整摘要: This paper presents a framework for mapping unknown scalar fields using a sensor-equipped autonomous robot operating in unsafe environments. The unsafe regions are defined as regions of high-intensity, where the field value exceeds a predefined safety threshold. For safe and efficient mapping of the scalar field, the sensor-equipped robot must avoid high-intensity regions during the measurement process. In this paper, the scalar field is modeled as a sample from a Gaussian process (GP), which enables Bayesian inference and provides closed-form expressions for both the predictive mean and the uncertainty. Concurrently, the spatial structure of the high-intensity regions is estimated in real-time using the Hough transform (HT), leveraging the evolving GP posterior. A safe sampling strategy is then employed to guide the robot towards safe measurement locations, using probabilistic safety guarantees on the evolving GP posterior. The estimated high-intensity regions also facilitate the design of safe motion plans for the robot. The effectiveness of the approach is verified through two numerical simulation studies and an indoor experiment for mapping a light-intensity field using a wheeled mobile robot.
匹配关键词: transformer architecture
---

[ACADEMIC - ARXIV]
标题: LLaDA2.0-Uni: Unifying Multimodal Understanding and Generation with Diffusion Large Language Model
作者: Inclusion AI, Tiwei Bie, Haoxing Chen, Tieyuan Chen, Zhenglin Cheng, Long Cui, Kai Gan, Zhicheng Huang, Zhenzhong Lan, Haoquan Li, Jianguo Li, Tao Lin, Qi Qin, Hongjun Wang, Xiaomei Wang, Haoyuan Wu, Yi Xin, Junbo Zhao
链接: https://arxiv.org/abs/2604.20796v1
完整摘要: We present LLaDA2.0-Uni, a unified discrete diffusion large language model (dLLM) that supports multimodal understanding and generation within a natively integrated framework. Its architecture combines a fully semantic discrete tokenizer, a MoE-based dLLM backbone, and a diffusion decoder. By discretizing continuous visual inputs via SigLIP-VQ, the model enables block-level masked diffusion for both text and vision inputs within the backbone, while the decoder reconstructs visual tokens into high-fidelity images. Inference efficiency is enhanced beyond parallel decoding through prefix-aware optimizations in the backbone and few-step distillation in the decoder. Supported by carefully curated large-scale data and a tailored multi-stage training pipeline, LLaDA2.0-Uni matches specialized VLMs in multimodal understanding while delivering strong performance in image generation and editing. Its native support for interleaved generation and reasoning establishes a promising and scalable paradigm for next-generation unified foundation models. Codes and models are available at https://github.com/inclusionAI/LLaDA2.0-Uni.
匹配关键词: transformer architecture
---

[ACADEMIC - ARXIV]
标题: Automatic Ontology Construction Using LLMs as an External Layer of Memory, Verification, and Planning for Hybrid Intelligent Systems
作者: Pavel Salovskii, Iuliia Gorshkova
链接: https://arxiv.org/abs/2604.20795v1
完整摘要: This paper presents a hybrid architecture for intelligent systems in which large language models (LLMs) are extended with an external ontological memory layer. Instead of relying solely on parametric knowledge and vector-based retrieval (RAG), the proposed approach constructs and maintains a structured knowledge graph using RDF/OWL representations, enabling persistent, verifiable, and semantically grounded reasoning. The core contribution is an automated pipeline for ontology construction from heterogeneous data sources, including documents, APIs, and dialogue logs. The system performs entity recognition, relation extraction, normalization, and triple generation, followed by validation using SHACL and OWL constraints, and continuous graph updates. During inference, LLMs operate over a combined context that integrates vector-based retrieval with graph-based reasoning and external tool interaction. Experimental observations on planning tasks, including the Tower of Hanoi benchmark, indicate that ontology augmentation improves performance in multi-step reasoning scenarios compared to baseline LLM systems. In addition, the ontology layer enables formal validation of generated outputs, transforming the system into a generation-verification-correction pipeline. The proposed architecture addresses key limitations of current LLM-based systems, including lack of long-term memory, weak structural understanding, and limited reasoning capabilities. It provides a foundation for building agent-based systems, robotics applications, and enterprise AI solutions that require persistent knowledge, explainability, and reliable decision-making.
匹配关键词: transformer architecture
---

[ACADEMIC - ARXIV]
标题: Parallel-SFT: Improving Zero-Shot Cross-Programming-Language Transfer for Code RL
作者: Zhaofeng Wu, Shiqi Wang, Boya Peng, Anuj Goyal, Melanie Kambadur, Sebastian Ruder, Yoon Kim, Chloe Bi
链接: https://arxiv.org/abs/2604.20835v1
完整摘要: Modern language models demonstrate impressive coding capabilities in common programming languages (PLs), such as C++ and Python, but their performance in lower-resource PLs is often limited by training data availability. In principle, however, most programming skills are universal across PLs, so the capability acquired in one PL should transfer to others. In this work, we propose the task of zero-shot cross-programming-language transfer for code RL. We find that, for Llama-3.1, RL training for code generation in a source PL fails to improve, and sometimes even degrades, the performance on other target PLs. To address this, we hypothesize that effective RL transfer requires a generalizable SFT initialization before RL. We thus propose **Parallel-SFT**, an SFT strategy that incorporates "parallel programs" -- functionally equivalent code implemented in multiple PLs -- into the data mixture. We demonstrate that this improves transferability: when we subsequently perform RL on our Parallel-SFT model, we observe better generalization to unseen PLs. Analysis of the model internal representations reveals that Parallel-SFT leads to a more functionality-centric latent space, where equivalent programs across PLs are more tightly clustered, which we hypothesize to contribute to the improved transferability.
匹配关键词: mixture of experts
---

[ACADEMIC - ARXIV]
标题: PokeVLA: Empowering Pocket-Sized Vision-Language-Action Model with Comprehensive World Knowledge Guidance
作者: Yupeng Zheng, Xiang Li, Songen Gu, Yuhang Zheng, Shuai Tian, Weize Li, Linbo Wang, Senyu Fei, Pengfei Li, Yinfeng Gao, Zebin Xing, Yilun Chen, Qichao Zhang, Haoran Li, Wenchao Ding
链接: https://arxiv.org/abs/2604.20834v1
完整摘要: Recent advances in Vision-Language-Action (VLA) models have opened new avenues for robot manipulation, yet existing methods exhibit limited efficiency and a lack of high-level knowledge and spatial awareness. To address these challenges, we propose PokeVLA, a lightweight yet powerful foundation model for embodied manipulation that effectively infuses vision-language understanding into action learning. Our framework introduces a two-stage training paradigm: first, we pre-train a compact vision-language model (PokeVLM) on a curated multimodal dataset of 2.4M samples encompassing spatial grounding, affordance, and embodied reasoning tasks; second, we inject manipulation-relevant representations into the action space through multi-view goal-aware semantics learning, geometry alignment, and a novel action expert. Extensive experiments demonstrate state-of-the-art performance on the LIBERO-Plus benchmark and in real-world deployment, outperforming comparable baselines in success rate and robustness under diverse perturbations. To foster reproducibility and community progress, we will open-source our code, model weights, and the scripts for the curated pre-training dataset. Project page: https://getterupper.github.io/PokeVLA
匹配关键词: mixture of experts
---

[ACADEMIC - ARXIV]
标题: Global Offshore Wind Infrastructure: Deployment and Operational Dynamics from Dense Sentinel-1 Time Series
作者: Thorsten Hoeser, Felix Bachofer, Claudia Kuenzer
链接: https://arxiv.org/abs/2604.20822v1
完整摘要: The offshore wind energy sector is expanding rapidly, increasing the need for independent, high-temporal-resolution monitoring of infrastructure deployment and operation at global scale. While Earth Observation based offshore wind infrastructure mapping has matured for spatial localization, existing open datasets lack temporally dense and semantically fine-grained information on construction and operational dynamics. We introduce a global Sentinel-1 synthetic aperture radar (SAR) time series data corpus that resolves deployment and operational phases of offshore wind infrastructure from 2016Q1 to 2025Q1. Building on an updated object detection workflow, we compile 15,606 time series at detected infrastructure locations, with overall 14,840,637 events as analysis-ready 1D SAR backscatter profiles, one profile per Sentinel-1 acquisition and location. To enable direct use and benchmarking, we release (i) the analysis ready 1D SAR profiles, (ii) event-level baseline semantic labels generated by a rule-based classifier, and (iii) an expert-annotated benchmark dataset of 553 time series with 328,657 event labels. The baseline classifier achieves a macro F1 score of 0.84 in event-wise evaluation and an area under the collapsed edit similarity-quality threshold curve (AUC) of 0.785, indicating temporal coherence. We demonstrate that the resulting corpus supports global-scale analyses of deployment dynamics, the identification of differences in regional deployment patterns, vessel interactions, and operational events, and provides a reference for developing and comparing time series classification methods for offshore wind infrastructure monitoring.
匹配关键词: mixture of experts
---

[ACADEMIC - ARXIV]
标题: AAC: Admissible-by-Architecture Differentiable Landmark Compression for ALT
作者: An T. Le, Vien Ngo
链接: https://arxiv.org/abs/2604.20744v1
完整摘要: We introduce \textbf{AAC} (Architecturally Admissible Compressor), a differentiable landmark-selection module for ALT (A*, Landmarks, and Triangle inequality) shortest-path heuristics whose outputs are admissible by construction: each forward pass is a row-stochastic mixture of triangle-inequality lower bounds, so the heuristic is admissible for \emph{every} parameter setting without requiring convergence, calibration, or projection. At deployment, the module reduces to classical ALT on a learned subset, composing end-to-end with neural encoders while preserving the classical toolchain. The construction is the first differentiable instance of the compress-while-preserving-admissibility tradition in classical heuristic search. Under a matched per-vertex memory protocol, we establish that ALT with farthest-point-sampling landmarks (FPS-ALT) has provably near-optimal coverage on metric graphs, leaving at most a few percentage points of headroom for \emph{any} selector. AAC operates near this ceiling: the gap is $0.9$--$3.9$ percentage points on 9 road networks and ${\leq}1.3$ percentage points on synthetic graphs, with zero admissibility violations across $1{,}500+$ queries and all logged runs. At matched memory, AAC is also $1.2$--$1.5{\times}$ faster than FPS-ALT at the median query on DIMACS road networks, amortizing its offline cost within $170$--$1{,}924$ queries. A controlled ablation isolates the binding constraint: training-objective drift under default initialization, not architectural capacity; identity-on-first-$m$ initialization closes the expansion-count gap entirely. We release the module, a reusable matched-memory benchmarking protocol with paired two-one-sided-test (TOST) equivalence and pre-registration, and a reference compressed-differential-heuristics baseline.
匹配关键词: mixture of experts
---

[ACADEMIC - ARXIV]
标题: ONOTE: Benchmarking Omnimodal Notation Processing for Expert-level Music Intelligence
作者: Menghe Ma, Siqing Wei, Yuecheng Xing, Yaheng Wang, Fanhong Meng, Peijun Han, Luu Anh Tuan, Haoran Luo
链接: https://arxiv.org/abs/2604.20719v1
完整摘要: Omnimodal Notation Processing (ONP) represents a unique frontier for omnimodal AI due to the rigorous, multi-dimensional alignment required across auditory, visual, and symbolic domains. Current research remains fragmented, focusing on isolated transcription tasks that fail to bridge the gap between superficial pattern recognition and the underlying musical logic. This landscape is further complicated by severe notation biases toward Western staff and the inherent unreliability of "LLM-as-a-judge" metrics, which often mask structural reasoning failures with systemic hallucinations. To establish a more rigorous standard, we introduce ONOTE, a multi-format benchmark that utilizes a deterministic pipeline--grounded in canonical pitch projection--to eliminate subjective scoring biases across diverse notation systems. Our evaluation of leading omnimodal models exposes a fundamental disconnect between perceptual accuracy and music-theoretic comprehension, providing a necessary framework for diagnosing reasoning vulnerabilities in complex, rule-constrained domains.
匹配关键词: mixture of experts
---

[ACADEMIC - ARXIV]
标题: PokeVLA: Empowering Pocket-Sized Vision-Language-Action Model with Comprehensive World Knowledge Guidance
作者: Yupeng Zheng, Xiang Li, Songen Gu, Yuhang Zheng, Shuai Tian, Weize Li, Linbo Wang, Senyu Fei, Pengfei Li, Yinfeng Gao, Zebin Xing, Yilun Chen, Qichao Zhang, Haoran Li, Wenchao Ding
链接: https://arxiv.org/abs/2604.20834v1
完整摘要: Recent advances in Vision-Language-Action (VLA) models have opened new avenues for robot manipulation, yet existing methods exhibit limited efficiency and a lack of high-level knowledge and spatial awareness. To address these challenges, we propose PokeVLA, a lightweight yet powerful foundation model for embodied manipulation that effectively infuses vision-language understanding into action learning. Our framework introduces a two-stage training paradigm: first, we pre-train a compact vision-language model (PokeVLM) on a curated multimodal dataset of 2.4M samples encompassing spatial grounding, affordance, and embodied reasoning tasks; second, we inject manipulation-relevant representations into the action space through multi-view goal-aware semantics learning, geometry alignment, and a novel action expert. Extensive experiments demonstrate state-of-the-art performance on the LIBERO-Plus benchmark and in real-world deployment, outperforming comparable baselines in success rate and robustness under diverse perturbations. To foster reproducibility and community progress, we will open-source our code, model weights, and the scripts for the curated pre-training dataset. Project page: https://getterupper.github.io/PokeVLA
匹配关键词: multimodal
---

[ACADEMIC - ARXIV]
标题: OMIBench: Benchmarking Olympiad-Level Multi-Image Reasoning in Large Vision-Language Model
作者: Qiguang Chen, Chengyu Luan, Jiajun Wu, Qiming Yu, Yi Yang, Yizhuo Li, Jingqi Tong, Xiachong Feng, Libo Qin, Wanxiang Che
链接: https://arxiv.org/abs/2604.20806v1
完整摘要: Large vision-language models (LVLMs) have made substantial advances in reasoning tasks at the Olympiad level. Nevertheless, current Olympiad-level multimodal reasoning benchmarks for these models often emphasize single-image analysis and fail to exploit contextual information across multiple images. We present OMIBench, a benchmark designed to evaluate Olympiad-level reasoning when the required evidence is distributed over multiple images. It contains problems from biology, chemistry, mathematics, and physics Olympiads, together with manually annotated rationales and evaluation protocols for both exact and semantic answer matching. Across extensive experiments on OMIBench, we observe meaningful performance gaps in existing models. Even the strongest LVLMs, such as Gemini-3-Pro, attain only about 50% on the benchmark. These results position OMIBench as a focused resources for studying and improving multi-image reasoning in LVLMs.
匹配关键词: multimodal
---

[ACADEMIC - ARXIV]
标题: LLaDA2.0-Uni: Unifying Multimodal Understanding and Generation with Diffusion Large Language Model
作者: Inclusion AI, Tiwei Bie, Haoxing Chen, Tieyuan Chen, Zhenglin Cheng, Long Cui, Kai Gan, Zhicheng Huang, Zhenzhong Lan, Haoquan Li, Jianguo Li, Tao Lin, Qi Qin, Hongjun Wang, Xiaomei Wang, Haoyuan Wu, Yi Xin, Junbo Zhao
链接: https://arxiv.org/abs/2604.20796v1
完整摘要: We present LLaDA2.0-Uni, a unified discrete diffusion large language model (dLLM) that supports multimodal understanding and generation within a natively integrated framework. Its architecture combines a fully semantic discrete tokenizer, a MoE-based dLLM backbone, and a diffusion decoder. By discretizing continuous visual inputs via SigLIP-VQ, the model enables block-level masked diffusion for both text and vision inputs within the backbone, while the decoder reconstructs visual tokens into high-fidelity images. Inference efficiency is enhanced beyond parallel decoding through prefix-aware optimizations in the backbone and few-step distillation in the decoder. Supported by carefully curated large-scale data and a tailored multi-stage training pipeline, LLaDA2.0-Uni matches specialized VLMs in multimodal understanding while delivering strong performance in image generation and editing. Its native support for interleaved generation and reasoning establishes a promising and scalable paradigm for next-generation unified foundation models. Codes and models are available at https://github.com/inclusionAI/LLaDA2.0-Uni.
匹配关键词: multimodal
---

[ACADEMIC - ARXIV]
标题: V-tableR1: Process-Supervised Multimodal Table Reasoning with Critic-Guided Policy Optimization
作者: Yubo Jiang, Yitong An, Xin Yang, Abudukelimu Wuerkaixi, Xuxin Cheng, Fengying Xie, Zhiguo Jiang, Cao Liu, Ke Zeng, Haopeng Zhang
链接: https://arxiv.org/abs/2604.20755v1
完整摘要: We introduce V-tableR1, a process-supervised reinforcement learning framework that elicits rigorous, verifiable reasoning from multimodal large language models (MLLMs). Current MLLMs trained solely on final outcomes often treat visual reasoning as a black box, relying on superficial pattern matching rather than performing rigorous multi-step inference. While Reinforcement Learning with Verifiable Rewards could enforce transparent reasoning trajectories, extending it to visual domains remains severely hindered by the ambiguity of grounding abstract logic into continuous pixel space. We solve this by leveraging the deterministic grid structure of tables as an ideal visual testbed. V-tableR1 employs a specialized critic VLM to provide dense, step-level feedback on the explicit visual chain-of-thought generated by a policy VLM. To optimize this system, we propose Process-Guided Direct Alignment Policy Optimization (PGPO), a novel RL algorithm integrating process rewards, decoupled policy constraints, and length-aware dynamic sampling. Extensive evaluations demonstrate that V-tableR1 explicitly penalizes visual hallucinations and shortcut guessing. By fundamentally shifting multimodal inference from black-box pattern matching to verifiable logical derivation, V-tableR1 4B establishes state-of-the-art accuracy among open-source models on complex tabular benchmarks, outperforming models up to 18x its size and improving over its SFT baseline
匹配关键词: multimodal
---

[ACADEMIC - ARXIV]
标题: Where and What: Reasoning Dynamic and Implicit Preferences in Situated Conversational Recommendation
作者: Dongding Lin, Jian Wang, Yongqi Li, Wenjie Li
链接: https://arxiv.org/abs/2604.20749v1
完整摘要: Situated conversational recommendation (SCR), which utilizes visual scenes grounded in specific environments and natural language dialogue to deliver contextually appropriate recommendations, has emerged as a promising research direction due to its close alignment with real-world scenarios. Compared to traditional recommendations, SCR requires a deeper understanding of dynamic and implicit user preferences, as the surrounding scene often influences users' underlying interests, while both may evolve across conversations. This complexity significantly impacts the timing and relevance of recommendations. To address this, we propose situated preference reasoning (SiPeR), a novel framework that integrates two core mechanisms: (1) Scene transition estimation, which estimates whether the current scene satisfies user needs, and guides the user toward a more suitable scene when necessary; and (2) Bayesian inverse inference, which leverages the likelihood of multimodal large language models (MLLMs) to predict user preferences about candidate items within the scene. Extensive experiments on two representative benchmarks demonstrate SiPeR's superiority in both recommendation accuracy and response generation quality. The code and data are available at https://github.com/DongdingLin/SiPeR.
匹配关键词: multimodal
---

