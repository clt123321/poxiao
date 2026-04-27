# 破晓 PoXiao — 原始数据 (Raw Context)
生成时间: 2026-04-25 20:28 UTC
================================================================================

[RSS:Reddit LocalLLaMA (社区共识)]
AMA Announcement: Nous Research, The Opensource Lab Behind Hermes Agent (Wednesday, 8AM-11AM PST)
https://www.reddit.com/r/LocalLLaMA/comments/1suw9on/ama_announcement_nous_research_the_opensource_lab/
Hi r/LocalLLaMA 👋 We're excited for Wednesday's guests, The Nous Research Team! Kicking things off Wednesday, April. 29th, 8 AM–11 AM PST ⚠️ Note: The AMA itself will be hosted in a separate thread, please don’t post questions here. &#32; submitted by &#32; /u/XMasterrrr [link] &#32; [comments]
---

[RSS:Reddit LocalLLaMA (社区共识)]
This is where we are right now, LocalLLaMA
https://www.reddit.com/r/LocalLLaMA/comments/1suqfba/this_is_where_we_are_right_now_localllama/
the future is now &#32; submitted by &#32; /u/jacek2023 [link] &#32; [comments]
---

[RSS:Reddit LocalLLaMA (社区共识)]
Deepseek V4 AGI comfirmed
https://www.reddit.com/r/LocalLLaMA/comments/1suolda/deepseek_v4_agi_comfirmed/
&#32; submitted by &#32; /u/Swimming-Sky-7025 [link] &#32; [comments]
---

[RSS:Reddit LocalLLaMA (社区共识)]
I'm glad we have deepseek
https://www.reddit.com/r/LocalLLaMA/comments/1suyu7a/im_glad_we_have_deepseek/
other companies are slowly going away from open weight, not releasing base models, delaying open weight distribution, not releasing top models (this one I think is fair, but still), and I also noticed they stopped publishing research (old Gemma and qwen had detailed papers about the models training 
---

[RSS:Reddit LocalLLaMA (社区共识)]
Anthropic admits to have made hosted models more stupid, proving the importance of open weight, local models
https://www.reddit.com/r/LocalLLaMA/comments/1suef7t/anthropic_admits_to_have_made_hosted_models_more/
TL;DR: On March 4, we changed Claude Code's default reasoning effort from high to medium to reduce the very long latency—enough to make the UI appear frozen—some users were seeing in high mode. This was the wrong tradeoff. We reverted this change on April 7 after users told us they'd prefer to defau
---

[RSS:Reddit LocalLLaMA (社区共识)]
Qwen3.6-35B-A3B - even in VRAM limited scenarios it can be better to use bigger quants than you'd expect!
https://www.reddit.com/r/LocalLLaMA/comments/1sutct2/qwen3635ba3b_even_in_vram_limited_scenarios_it/
So maybe this is a no-brainer to many experienced local LLM users but it was not obvious for me. I am running a 3070 8gb + 64gb DDR4. Pretty lightweight setup so I chose the smallest Q4 unsloth model Qwen3.6-35B-A3B-UD-IQ4_XS.gguf - which is ~18gb. It does run ok, and with some optimizations in llam
---

[RSS:Reddit LocalLLaMA (社区共识)]
Gemma 4 and Qwen 3.6 with q8_0 and q4_0 KV cache: KL divergence results
https://www.reddit.com/r/LocalLLaMA/comments/1suh3sz/gemma_4_and_qwen_36_with_q8_0_and_q4_0_kv_cache/
&#32; submitted by &#32; /u/oobabooga4 [link] &#32; [comments]
---

[RSS:Reddit LocalLLaMA (社区共识)]
Qwen3.6 27B's surprising KV cache quantization test results (Turbo3/4 vs F16 vs Q8 vs Q4)
https://www.reddit.com/r/LocalLLaMA/comments/1suur3s/qwen36_27bs_surprising_kv_cache_quantization_test/
I've been using Qwen3.6-27B-Q5_K_M with turbo3 KV cache since it's been released, and I haven't had any issues at all (no loops, no memory loss, etc.). However, I'm also aware that K cache compression is not really recommended in most cases. So I wanted to check how it is possible and I learned that
---

[RSS:Reddit LocalLLaMA (社区共识)]
Opinion: Qwen 3.6 27b Beats Sonnet 4.6 on Feature Planning
https://www.reddit.com/r/LocalLLaMA/comments/1supft2/opinion_qwen_36_27b_beats_sonnet_46_on_feature/
I keep hearing the argument that that large models are better for high-level planning and task orchestration, since they have more general knowledge to work from when making decisions. However, I've been testing Qwen 3.6 27b (Unsloth Q5_K_M) quite a lot since its release, and it's consistently outpe
---

[RSS:Reddit LocalLLaMA (社区共识)]
I just had a little ghost in the shell moment...
https://www.reddit.com/r/LocalLLaMA/comments/1sulutq/i_just_had_a_little_ghost_in_the_shell_moment/
Somehow my Qwen3.6-35B-A3B hallucinated that its context is full, pretty much at the right moment... &#32; submitted by &#32; /u/bonobomaster [link] &#32; [comments]
---

[RSS:Reddit LocalLLaMA (社区共识)]
Tested Deepseek v4 flash with some large code change evals. It absolutely kills with too use accuracy!
https://www.reddit.com/r/LocalLLaMA/comments/1suhdki/tested_deepseek_v4_flash_with_some_large_code/
Did some test tasks with v4 flash. The context management, tool use accuracy and thinking traces all looked excellent. It is one of the few open-weights models I have tested that does not get confused with multi tool calls or complex native tool definitions It must have called at least 100 tool call
---

[RSS:Reddit LocalLLaMA (社区共识)]
DS4-Flash vs Qwen3.6
https://www.reddit.com/r/LocalLLaMA/comments/1sub71w/ds4flash_vs_qwen36/
&#32; submitted by &#32; /u/flavio_geo [link] &#32; [comments]
---

[RSS:Reddit LocalLLaMA (社区共识)]
DeepSeek-v4 has a comical 384K max output capability
https://www.reddit.com/r/LocalLLaMA/comments/1su9iio/deepseekv4_has_a_comical_384k_max_output/
was shocked when saw that spec, immediatly went to the website and asked it to make a comprehensive single-html-web-OS and it indeed generated a single 100KB html for me...I'm speechless. https://preview.redd.it/6zcbzbkvj3xg1.png?width=2878&amp;format=png&amp;auto=webp&amp;s=6279909b483b7b32e7c41172
---

[RSS:Reddit LocalLLaMA (社区共识)]
Guys, I found a use case for my 10$/m LLM Server: Cooking
https://www.reddit.com/r/LocalLLaMA/comments/1suq7ij/guys_i_found_a_use_case_for_my_10m_llm_server/
Basically, I use To Good 2 Go a lot, get random food, take a photo and ask Qwen 3.5 128B what the fuck to cook. Beyond pasta and pizza, I have zero cooking skills. So far, god bless, no food poisoning yet. Today we had grilled chicken sticks. &#32; submitted by &#32; /u/Ne00n [link] &#32; [comments]
---

[RSS:Reddit LocalLLaMA (社区共识)]
Pi.dev coding agent as no sandbox by default.
https://www.reddit.com/r/LocalLLaMA/comments/1sunkcq/pidev_coding_agent_as_no_sandbox_by_default/
I love Pi, but minimal mean minimal. I realized it when it rm -f /tmp/somefile.log without asking for permission. There a extension to prevent the most dangerous command. https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/examples/extensions/permission-gate.ts Or there actual sandbo
---

[RSS:Reddit LocalLLaMA (社区共识)]
VLLM PR : New MoE model from Cohere soon
https://www.reddit.com/r/LocalLLaMA/comments/1sujzpf/vllm_pr_new_moe_model_from_cohere_soon/
&#32; submitted by &#32; /u/LinkSea8324 [link] &#32; [comments]
---

[RSS:Reddit LocalLLaMA (社区共识)]
Deepseek flash seems like a very good replacement for Haiku at the very least
https://www.reddit.com/r/LocalLLaMA/comments/1suiruw/deepseek_flash_seems_like_a_very_good_replacement/
We have a chat system which we use haiku for because it is mostly about tool calling and summarisation of them. But we have many tools with pretty complex input schemas, and stuff like gemma didn't cut it, so we went with haiku. Haiku is pretty good. I ran the evals for deepseek v4 flash today compa
---

[RSS:Reddit LocalLLaMA (社区共识)]
Takeaways & discussion about the DeepSeek V4 architecture
https://www.reddit.com/r/LocalLLaMA/comments/1subuve/takeaways_discussion_about_the_deepseek_v4/
Spent the morning looking at the V4 tech report. The benchmarks are getting deserved attention, but I think the architecture is also worth digging into. Quick thoughts below to encourage feedback and discussions. TL;DR - Significant novelties compared to DeepSeek V3 - Hybrid attention: CSA (compress
---

[RSS:Reddit LocalLLaMA (社区共识)]
Open source multi-cursor/background computer-use (Codex-like) using Hermes Agent + Qwen3.6-35B-A3B-4bit + Cua-Driver
https://www.reddit.com/r/LocalLLaMA/comments/1suux6h/open_source_multicursorbackground_computeruse/
&#32; submitted by &#32; /u/a6oo [link] &#32; [comments]
---

[RSS:Reddit LocalLLaMA (社区共识)]
Turboquant on llama.cpp?
https://www.reddit.com/r/LocalLLaMA/comments/1sukrfx/turboquant_on_llamacpp/
Now that the financebro hype has faded, is there an implementation of turboquant for llama.cpp somewhere? Saving even 50% of kv cache memory would be nice. &#32; submitted by &#32; /u/StupidScaredSquirrel [link] &#32; [comments]
---

[RSS:Reddit LocalLLaMA (社区共识)]
Is there anyway to run bigger models at 20t/s with 24vram + 64gb ram DDR5?
https://www.reddit.com/r/LocalLLaMA/comments/1sutg18/is_there_anyway_to_run_bigger_models_at_20ts_with/
I know the new Qwen 27B is amazing right now for coding in general, but since 122b is supposed to be coming as well, it’s expected to be better I guess ? I am actually surprised at how this dense model performs I haven’t used Codex at all anymore for all my C++ programming needs. &#32; submitted by 
---

[RSS:Reddit LocalLLaMA (社区共识)]
Qwen3.6-35B-A3B-UD-IQ4_XS C++ to Rust Code Port Test: It Worked (Mostly)!
https://www.reddit.com/r/LocalLLaMA/comments/1sv3ff6/qwen3635ba3budiq4_xs_c_to_rust_code_port_test_it/
When Qwen3.6-35B-A3B was released a week or so ago, I sort of expected an iterative improvement on the previous Qwen3.5 models. After all, those models were pretty decent as compared with the previous local models I had tried, and Qwen3.5 did well on the fairly boring ThreeJS task I've been using to
---

[RSS:Reddit MachineLearning (学术风向)]
There Will Be a Scientific Theory of Deep Learning [R]
https://www.reddit.com/r/MachineLearning/comments/1sun588/there_will_be_a_scientific_theory_of_deep/
Hi, all! I'm the lead author on this ambitious (14-author!) perspective paper on deep learning theory. We've all been working seriously, and more or less exclusively, on deep learning for many years now. We believe that a theory is emerging, and we pull together five lines of evidence in recent rese
---

[RSS:Reddit MachineLearning (学术风向)]
How to find to 'collaborate' with Professors to get funding for my research papers? [D]
https://www.reddit.com/r/MachineLearning/comments/1sv1473/how_to_find_to_collaborate_with_professors_to_get/
So, I have a few research papers, which I feel are good enough for top conferences' workshops or adjacent proceedings, and maybe even the main conference itself. I recently, submitted to and got accepted at a CVPR Archival Workshop (which is considered to be great in it's niche), but was forced to w
---

[RSS:Reddit MachineLearning (学术风向)]
Everything is so casual at CS Conferences. Why charge exorbitant registration fees? [D]
https://www.reddit.com/r/MachineLearning/comments/1sumw4i/everything_is_so_casual_at_cs_conferences_why/
Why would anyone pay large amounts of registration fees and end up with empty poster boards and virtual presentations. Saw this happening at ICLR. Everything feels so casual and ignorant. No strict standards. Virtual oral talks are pre-recorded videos felt so unnatural. &#32; submitted by &#32; /u/c
---

[RSS:Reddit MachineLearning (学术风向)]
Research taste is a skill nobody talks about. How do you develop it without collaborators? [D]
https://www.reddit.com/r/MachineLearning/comments/1suguuz/research_taste_is_a_skill_nobody_talks_about_how/
if you've ever built an elegant, complex ML pipeline to solve something a 10-line prompt could've handled... this is for you. i've been thinking about what separates people who do useful research from people who do impressive-looking research. it's almost always the problems you choose rather than r
---

[RSS:Reddit MachineLearning (学术风向)]
Best swag at ICLR 2026 so far? [D]
https://www.reddit.com/r/MachineLearning/comments/1sv1o9b/best_swag_at_iclr_2026_so_far_d/
For those at ICLR 2026 in Rio: which sponsors have the best swag this year? Anything useful, fun or cute! &#32; submitted by &#32; /u/demiquasar [link] &#32; [comments]
---

[RSS:Reddit MachineLearning (学术风向)]
DharmaOCR: Open-Source Specialized SLM (3B) + Cost–Performance Benchmark against LLMs and other open-sourced models [R]
https://www.reddit.com/r/MachineLearning/comments/1sun6wt/dharmaocr_opensource_specialized_slm_3b/
Hey everyone, we just open-sourced DharmaOCR on Hugging Face. Models and datasets are all public, free to use and experiment with. We also published the paper documenting all the experimentation behind it, for those who want to dig into the methodology. We fine-tuned open-source SLMs (3B and 7B para
---

[RSS:Reddit MachineLearning (学术风向)]
[New Optimizer] 🌹 Rose: low VRAM, easy to use, great results, Apache 2.0 [P]
https://www.reddit.com/r/MachineLearning/comments/1sucjwp/new_optimizer_rose_low_vram_easy_to_use_great/
Hello, World! I recently released a new PyTorch optimizer I've been researching and developing on my own for the last couple of years. It's named &quot;Rose&quot; in memory of my mother, who loved to hear about my discoveries and progress with AI. Without going too much into the technical details (w
---

[RSS:Reddit MachineLearning (学术风向)]
Open-source 9-task benchmark for coding-agent retrieval augmentation. Per-task deltas +0.010 to +0.320, all evals reproducible [P]
https://www.reddit.com/r/MachineLearning/comments/1suzqxe/opensource_9task_benchmark_for_codingagent/
Sharing an open-source benchmark suite ( paper-lantern-challenges ) that measures coding-agent performance with vs without retrieval-augmented technique selection across 9 everyday software tasks. Disclosure: I'm the author of the retrieval system under test (paperlantern.ai/code); the artifact bein
---

[RSS:Reddit MachineLearning (学术风向)]
Is the ds/ml slowly being morphed into an AI engineer? [D]
https://www.reddit.com/r/MachineLearning/comments/1sudkoa/is_the_dsml_slowly_being_morphed_into_an_ai/
Agents are amazing. Harnesses are cool. But the fundamental role of a data scientist is not to use a generalist model in an existing workflow; it's a completely different field. AI engineering is the body of the vehicle, whereas the actual brain/engine behind it is the data scientist's playground. I
---

[RSS:Reddit MachineLearning (学术风向)]
How would you build an automated commentary engine for daily trade attribution at scale? [R]
https://www.reddit.com/r/MachineLearning/comments/1sv3cnm/how_would_you_build_an_automated_commentary/
Hey everyone, I'm currently working through a problem in the market risk reporting space and would love to hear how you all would architect this. The Use Case: &gt; I have thousands of trades coming in at varying frequencies (daily, monthly). I need to build a system that automatically analyzes this
---

[RSS:Reddit MachineLearning (学术风向)]
We're open-sourcing the first publicly available blood detection model: dataset, weights, and CLI [P] [R]
https://www.reddit.com/r/MachineLearning/comments/1sui6je/were_opensourcing_the_first_publicly_available/
Hey all, today we're releasing BloodshotNet, the world's first open-source blood detection model. We built it primarily for Trust &amp; Safety and content moderation use cases, the idea of acting as a front-line filter so users and human reviewers aren't exposed to graphic imagery. What we're open s
---

[RSS:Reddit MachineLearning (学术风向)]
ICML 2026 - Final Predictions on Average Score Needed Before Scores Come Out in 1 week? [D]
https://www.reddit.com/r/MachineLearning/comments/1su8rq1/icml_2026_final_predictions_on_average_score/
What do people think the average score threshold will be for acceptance in ICML 2026? Author notification is on April 30th &#32; submitted by &#32; /u/Fit_Scale_1464 [link] &#32; [comments]
---

[RSS:Reddit MachineLearning (学术风向)]
HPO - hyperparameter drift [D]
https://www.reddit.com/r/MachineLearning/comments/1sumzh7/hpo_hyperparameter_drift_d/
Hey all, so I am running into a problem. I am training massive ML models which take literally a day to fully train. We want to run HPO to make it so that we can get the best parameters for the model and we require very high accuracy for the task so we need the HPO step. Because the model takes a day
---

[RSS:Reddit MachineLearning (学术风向)]
Mitigating hallucination [P]
https://www.reddit.com/r/MachineLearning/comments/1sug8uc/mitigating_hallucination_p/
Hi, Everyone. I repost this since my previous one was deleted(I don't know why, might be low quality of writing?) I’ve been working on a lightweight way to reduce hallucinations in LLMs without relying on external judges, extra human labels, or heavy preference-learning pipelines. The basic idea is 
---

[RSS:Ars Technica AI (深度技术)]
Why are top university websites serving porn? It comes down to shoddy housekeeping.
https://arstechnica.com/security/2026/04/why-are-top-university-websites-serving-porn-it-comes-down-to-shoddy-housekeeping/
Hundreds of subdomains from dozens of universities have been hijacked by scammers.
---

[RSS:Reddit Jobs & Careers (职场动态)]
Resume Advice Thread - April 25, 2026
https://www.reddit.com/r/cscareerquestions/comments/1sv4ygb/resume_advice_thread_april_25_2026/
Please use this thread to ask for resume advice and critiques. You should read our Resume FAQ and implement any changes from that before you ask for more advice. Abide by the rules, don't be a jerk. Note on anonomyizing your resume: If you'd like your resume to remain anonymous, make sure you blank 
---

[RSS:Reddit Jobs & Careers (职场动态)]
This job search process is absurd
https://www.reddit.com/r/cscareerquestions/comments/1susv69/this_job_search_process_is_absurd/
Every company wants something different and they want the hyper amped up version of it. Every company wants 4-6 fucking rounds of interviews. If you study NC 150, too bad because they only ask 2 leetcode hards or 3 levels of variations of LCs. If you study more leetcode, they don't do leetcode they 
---

[RSS:Reddit Jobs & Careers (职场动态)]
Who would claude’s users be if there are no more software engineers?
https://www.reddit.com/r/cscareerquestions/comments/1suuhj6/who_would_claudes_users_be_if_there_are_no_more/
Listening to all the CTOs of these tech companies, they seem dire to replace all software engineers. However, who will be subscribing to their product if the main users no longer exist? The way they make it sound, product managers should be able to build full stack applications without anyone knowin
---

[RSS:Reddit Jobs & Careers (职场动态)]
Do Indian devs get “typecast” in Western companies?
https://www.reddit.com/r/cscareerquestions/comments/1sumpz0/do_indian_devs_get_typecast_in_western_companies/
This might be uncomfortable to ask but I’ve been noticing a pattern and wanted to sanity check In my team a lot of Indian devs including me tend to get pushed toward execution heavy work fixing bugs, grinding tickets, keeping things running. But when it comes to leading projects, owning design decis
---

[RSS:Reddit Jobs & Careers (职场动态)]
PMs and Designers are pushing changes to the code. So far they're successful. Do you have that in your company?
https://www.reddit.com/r/cscareerquestions/comments/1sv6l2h/pms_and_designers_are_pushing_changes_to_the_code/
I'm a junior with 2 yoe, and recently my company started pushing PMs and Designers yo use Claude to implement the changes they need. I saw several small things having a success. Now I'm not sure what my focus should be? This pattern potentially leads to needing less devs, if a lot of simple tasks co
---

[RSS:Reddit Jobs & Careers (职场动态)]
juniors on my team ship fast but can't debug anything they didn't actually write
https://www.reddit.com/r/cscareerquestions/comments/1subewm/juniors_on_my_team_ship_fast_but_cant_debug/
Junior on our team shipped a feature last week in like two days. Clean code, tests passed, shipped fine. Week later a null shows up somewhere it shouldn't and he sat on the bug for most of a day before asking for help because he genuinely could not trace where the bad value was coming from He wrote 
---

[RSS:Reddit Jobs & Careers (职场动态)]
I’m sick and tired of staring at a computer all day.
https://www.reddit.com/r/cscareerquestions/comments/1suob3e/im_sick_and_tired_of_staring_at_a_computer_all_day/
I’m honestly getting burned out from staring at a computer all day. I’ve been working in sql, and lately it just feels like nonstop screen time with no real break. Has anyone here dealt with this kind of burnout? Curious how others are handling this. &#32; submitted by &#32; /u/Communication_Dizzy [
---

[RSS:Reddit Jobs & Careers (职场动态)]
Are folks really seeing developers who can’t read code and are relying 100% on AI?
https://www.reddit.com/r/cscareerquestions/comments/1suiku8/are_folks_really_seeing_developers_who_cant_read/
I mean who have been hired. &#32; submitted by &#32; /u/Forsaken-Intern7941 [link] &#32; [comments]
---

[RSS:Reddit Jobs & Careers (职场动态)]
Those of you who are millionaires why are you still working?
https://www.reddit.com/r/cscareerquestions/comments/1sudga8/those_of_you_who_are_millionaires_why_are_you/
Why not retire and enjoy the money? &#32; submitted by &#32; /u/VariationLivid3193 [link] &#32; [comments]
---

[RSS:Reddit Jobs & Careers (职场动态)]
Company Is Tracking And Ranking Engineers AI Usage, Afraid I'm Not Learning Anything As A Junior. Advice?
https://www.reddit.com/r/cscareerquestions/comments/1sum75x/company_is_tracking_and_ranking_engineers_ai/
I'm around 1.5 years into my career as a full stack mobile dev at a no-name non-tech company. I was made aware today that our AI usage is being tracked and ranked against our team mates and flagged if we aren't using it enough. I've spent ~$50 of my $550 limit this month. I like to use AI as a colla
---

[RSS:Reddit Jobs & Careers (职场动态)]
Do you have big emergency fund?
https://www.reddit.com/r/cscareerquestions/comments/1suthn9/do_you_have_big_emergency_fund/
given the layoffs and rising competition with landing a new role in tech what’s the safety net that you have in emergency funds in case you were let go? Im super paranoid about being let go that I’ve been saving up for a 1 year of expenses but I still feel like that’s not enough nowadays to find a j
---

[RSS:Reddit Jobs & Careers (职场动态)]
When do personal projects still matter after getting SWE experience?
https://www.reddit.com/r/cscareerquestions/comments/1suzxf9/when_do_personal_projects_still_matter_after/
When do personal projects still matter after getting SWE experience? Based on what I’ve seen: - In general, work experience &gt;&gt; personal projects - But in practice, it seems conditional depends on topic/quality of personal projects and work experience qaulity. My experience: - During internship
---

[RSS:Reddit Jobs & Careers (职场动态)]
What do you actually learn in Computer Science?
https://www.reddit.com/r/cscareerquestions/comments/1svaq7i/what_do_you_actually_learn_in_computer_science/
What do you actually learn in Computer Science? How are the test papers like? Do you need to learn a lot of facts (as in do you need to memorize them or are you applying them like what you would do in physics/math). I've seen some cs test papers online and I found out you need to learn about network
---

[RSS:Reddit Jobs & Careers (职场动态)]
Are AI companies secretly planning to own everything?
https://www.reddit.com/r/cscareerquestions/comments/1suwzd9/are_ai_companies_secretly_planning_to_own/
I haven’t seen this idea before but perhaps someone has mentioned it. Law firms, hospitals, etc are feeding all their data into AI. Since this is training the AI, what is preventing the AI companies from eventually cutting out the law firms etc and providing the service directly to customers? Why hi
---

[RSS:Reddit Jobs & Careers (职场动态)]
Are entry level job postings looking for entry level candidates?
https://www.reddit.com/r/cscareerquestions/comments/1suzyhs/are_entry_level_job_postings_looking_for_entry/
I had yet another recruiter video call that went absolutely nowhere even though I had more than the experience required, and they decided to pursue other candidates for the next rounds. Yesterday, they reposted the same job after a week long full of interviews. They didn’t have a good enough selecti
---

[RSS:Reddit Jobs & Careers (职场动态)]
Moat AI doomer posts are from students or new grads that never saw a real product
https://www.reddit.com/r/cscareerquestions/comments/1su9t2u/moat_ai_doomer_posts_are_from_students_or_new/
I noticed that most AI doomer posts have a very &quot;junior&quot; perspective on software development and don't understand the complexity and problems happening in a real software organization. The thing is that all the university projects are made for learning purposes. AI can do that easily, that
---

[RSS:Reddit Jobs & Careers (职场动态)]
Too many email notifications
https://www.reddit.com/r/cscareerquestions/comments/1sv7zya/too_many_email_notifications/
I’ve been at 2 teams at my current job and because I’m in an iAM group (aws), there will be many days I start getting every SNS notification under the sun. There are 200 people in the group, so I don’t know what every notification is referring to and cloud is upstream of my responsibilities. I gener
---

[RSS:Reddit Jobs & Careers (职场动态)]
Recruiter Screen
https://www.reddit.com/r/cscareerquestions/comments/1suzyld/recruiter_screen/
How long have y'all waited after a recruiter screen for the recruiter to get back with interview dates? &#32; submitted by &#32; /u/Late-Hat-9256 [link] &#32; [comments]
---

[RSS:Reddit Jobs & Careers (职场动态)]
SF startup (<100 employees, unicorn status) vs London Big N
https://www.reddit.com/r/cscareerquestions/comments/1sv0nxl/sf_startup_100_employees_unicorn_status_vs_london/
New grad with offers from both (International from UK, graduating from T4 CS Bay Area) Pay at the startup is better and leadership is ex-meta/google, location is also better in terms of where I want to be in terms of life/career at the moment. WLB isn't a factor for me, but I'm rather concerned abou
---

[RSS:Reddit Jobs & Careers (职场动态)]
What skills are you building? (Tech or non tech)
https://www.reddit.com/r/cscareerquestions/comments/1sue16m/what_skills_are_you_building_tech_or_non_tech/
tldr: The industry is changing fast. What skills are you building, in tech and in life, to adapt? Ten years as a SWE at a Fortune 500. Full-stack, though I never really got deep into infra or security. We're at roughly 75% AI-written code now, and honestly it's good. Greenfield, legacy, messy codeba
---

[RSS:Reddit Jobs & Careers (职场动态)]
contractor -> FTE
https://www.reddit.com/r/cscareerquestions/comments/1sv40np/contractor_fte/
I’m contracting remotely for FAANG US, as an engineer. The issue is I’m from APAC and they have no local headcount for engineers for FTE. My pay is considered high in APAC area. Ive been enjoying this role a lot and really hope to move to FTE Anyone has advice for cross region FTE conversion? Has an
---

[RSS:Reddit Jobs & Careers (职场动态)]
Which internship to choose for summer ?
https://www.reddit.com/r/cscareerquestions/comments/1sv3gqx/which_internship_to_choose_for_summer/
Hi folks! I am incredibly fortunate to have received 2 internship offers for summer. I would like your opinions on them. Company: Softbank Role: AI Infrastructure Intern (mostly around distributed systems + GPU Cloud) Location: Bay Area Company: Modular Role: GenAI Performance Intern (This is low le
---

[HACKERNEWS]
New 10 GbE USB adapters are cooler, smaller, cheaper
https://www.jeffgeerling.com/blog/2026/new-10-gbe-usb-adapters-cooler-smaller-cheaper/
Score: 274 | Comments: 129
---

[HACKERNEWS]
A web-based RDP client built with Go WebAssembly and grdp
https://github.com/nakagami/grdpwasm
Score: 9 | Comments: 3
---

[HACKERNEWS]
Replace IBM Quantum back end with /dev/urandom
https://github.com/yuvadm/quantumslop/blob/25ad2e76ae58baa96f6219742459407db9dd17f5/URANDOM_DEMO.md
Score: 201 | Comments: 30
---

[HACKERNEWS]
Open source memory layer so any AI agent can do what Claude.ai and ChatGPT do
https://alash3al.github.io/stash?_v01
Score: 79 | Comments: 38
---

[HACKERNEWS]
Cosmology with Geometry Nodes
https://www.blender.org/user-stories/cosmology-with-geometry-nodes/
Score: 74 | Comments: 1
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
标题: Reinforcing privacy reasoning in LLMs via normative simulacra from fiction
作者: Matt Franchi, Madiha Zahrah Choksi, Harold Triedman, Helen Nissenbaum
链接: https://arxiv.org/abs/2604.20904v1
完整摘要: Information handling practices of LLM agents are broadly misaligned with the contextual privacy expectations of their users. Contextual Integrity (CI) provides a principled framework, defining privacy as the appropriate flow of information within context-relative norms. However, existing approaches either double inference cost via supervisor-assistant architectures, or fine-tune on narrow task-specific data. We propose extracting normative simulacra (structured representations of norms and information flows) from fiction novels and using them to fine-tune LLMs via supervised learning followed by GRPO reinforcement learning. Our composite reward function combines programmatic signals, including task clarity (subsuming schema validity, construct discrimination, and extraction confidence), structural completeness, internal consistency, and context identification, with an LLM judge that evaluates whether the model's privacy reasoning is grounded in the held-out normative universe of the source text. To mitigate overfitting, we introduce per-completion contrastive scoring: each completion is evaluated against both the correct normative universe and a randomly selected wrong one, teaching the model to condition on context rather than memorize source-specific norms. We evaluate on five CI-aligned benchmarks spanning distinct societal contexts and ablate the contributions of RL and normative grounding. Across seven models, SFT introduces a conservative prior toward restricting information flow, improving recognition of privacy-relevant situations but not the correctness of privacy judgments. GRPO with normative grounding achieves the highest score on a law compliance benchmark and strongest correlation with crowdsourced human privacy expectations, demonstrating that fiction-derived normative simulacra can teach contextual privacy reasoning that transfers to real-world domains.
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
标题: UniGenDet: A Unified Generative-Discriminative Framework for Co-Evolutionary Image Generation and Generated Image Detection
作者: Yanran Zhang, Wenzhao Zheng, Yifei Li, Bingyao Yu, Yu Zheng, Lei Chen, Jiwen Lu, Jie Zhou
链接: https://arxiv.org/abs/2604.21904v1
完整摘要: In recent years, significant progress has been made in both image generation and generated image detection. Despite their rapid, yet largely independent, development, these two fields have evolved distinct architectural paradigms: the former predominantly relies on generative networks, while the latter favors discriminative frameworks. A recent trend in both domains is the use of adversarial information to enhance performance, revealing potential for synergy. However, the significant architectural divergence between them presents considerable challenges. Departing from previous approaches, we propose UniGenDet: a Unified generative-discriminative framework for co-evolutionary image Generation and generated image Detection. To bridge the task gap, we design a symbiotic multimodal self-attention mechanism and a unified fine-tuning algorithm. This synergy allows the generation task to improve the interpretability of authenticity identification, while authenticity criteria guide the creation of higher-fidelity images. Furthermore, we introduce a detector-informed generative alignment mechanism to facilitate seamless information exchange. Extensive experiments on multiple datasets demonstrate that our method achieves state-of-the-art performance. Code: \href{https://github.com/Zhangyr2022/UniGenDet}{https://github.com/Zhangyr2022/UniGenDet}.
匹配关键词: alignment
---

[ACADEMIC - ARXIV]
标题: Mapping the Political Discourse in the Brazilian Chamber of Deputies: A Multi-Faceted Computational Approach
作者: Flávio Soriano, Victoria F. Mello, Pedro B. Rigueira, Gisele L. Pappa, Wagner Meira, Ana Paula Couto da Silva, Jussara M. Almeida
链接: https://arxiv.org/abs/2604.21897v1
完整摘要: Analyses of legislative behavior often rely on voting records, overlooking the rich semantic and rhetorical content of political speech. In this paper, we ask three complementary questions about parliamentary discourse: how things are said, what is being said, and who is speaking in discursively similar ways. To answer these questions, we introduce a scalable and generalizable computational framework that combines diachronic stylometric analysis, contextual topic modeling, and semantic clustering of deputies' speeches. We apply this framework to a large-scale case study of the Brazilian Chamber of Deputies, using a corpus of over 450,000 speeches from 2003 to 2025. Our results show a long-term stylistic shift toward shorter and more direct speeches, a legislative agenda that reorients sharply in response to national crises, and a granular map of discursive alignments in which regional and gender identities often prove more salient than formal party affiliation. More broadly, this work offers a robust methodology for analyzing parliamentary discourse as a multidimensional phenomenon that complements traditional vote-based approaches.
匹配关键词: alignment
---

[ACADEMIC - ARXIV]
标题: Machine Behavior in Relational Moral Dilemmas: Moral Rightness, Predicted Human Behavior, and Model Decisions
作者: Jiseon Kim, Jea Kwon, Luiz Felipe Vecchietti, Wenchao Dong, Jaehong Kim, Meeyoung Cha
链接: https://arxiv.org/abs/2604.21871v1
完整摘要: Human moral judgment is context-dependent and modulated by interpersonal relationships. As large language models (LLMs) increasingly function as decision-support systems, determining whether they encode these social nuances is critical. We characterize machine behavior using the Whistleblower's Dilemma by varying two experimental dimensions: crime severity and relational closeness. Our study evaluates three distinct perspectives: (1) moral rightness (prescriptive norms), (2) predicted human behavior (descriptive social expectations), and (3) autonomous model decision-making. By analyzing the reasoning processes, we identify a clear cross-perspective divergence: while moral rightness remains consistently fairness-oriented, predicted human behavior shifts significantly toward loyalty as relational closeness increases. Crucially, model decisions align with moral rightness judgments rather than their own behavioral predictions. This inconsistency suggests that LLM decision-making prioritizes rigid, prescriptive rules over the social sensitivity present in their internal world-modeling, which poses a gap that may lead to significant misalignments in real-world deployments.
匹配关键词: alignment
---

[ACADEMIC - ARXIV]
标题: Locating acts of mechanistic reasoning in student team conversations with mechanistic machine learning
作者: Kaitlin Gili, Mainak Nistala, Kristen Wendell, Michael C. Hughes
链接: https://arxiv.org/abs/2604.21870v1
完整摘要: STEM education researchers are often interested in identifying moments of students' mechanistic reasoning for deeper analysis, but have limited capacity to search through many team conversation transcripts to find segments with a high concentration of such reasoning. We offer a solution in the form of an interpretable machine learning model that outputs time-varying probabilities that individual students are engaging in acts of mechanistic reasoning, leveraging evidence from their own utterances as well as contributions from the rest of the group. Using the toolkit of intentionally-designed probabilistic models, we introduce a specific inductive bias that steers the probabilistic dynamics toward desired, domain-aligned behavior. Experiments compare trained models with and without the inductive bias components, investigating whether their presence improves the desired model behavior on transcripts involving never-before-seen students and a novel discussion context. Our results show that the inductive bias improves generalization -- supporting the claim that interpretability is built into the model for this task rather than imposed post hoc. We conclude with practical recommendations for STEM education researchers seeking to adopt the tool and for ML researchers aiming to extend the model's design. Overall, we hope this work encourages the development of mechanistically interpretable models that are understandable and controllable for both end users and model designers in STEM education research.
匹配关键词: alignment
---

[ACADEMIC - ARXIV]
标题: Transient Turn Injection: Exposing Stateless Multi-Turn Vulnerabilities in Large Language Models
作者: Naheed Rayhan, Sohely Jahan
链接: https://arxiv.org/abs/2604.21860v1
完整摘要: Large language models (LLMs) are increasingly integrated into sensitive workflows, raising the stakes for adversarial robustness and safety. This paper introduces Transient Turn Injection(TTI), a new multi-turn attack technique that systematically exploits stateless moderation by distributing adversarial intent across isolated interactions. TTI leverages automated attacker agents powered by large language models to iteratively test and evade policy enforcement in both commercial and open-source LLMs, marking a departure from conventional jailbreak approaches that typically depend on maintaining persistent conversational context. Our extensive evaluation across state-of-the-art models-including those from OpenAI, Anthropic, Google Gemini, Meta, and prominent open-source alternatives-uncovers significant variations in resilience to TTI attacks, with only select architectures exhibiting substantial inherent robustness. Our automated blackbox evaluation framework also uncovers previously unknown model specific vulnerabilities and attack surface patterns, especially within medical and high stakes domains. We further compare TTI against established adversarial prompting methods and detail practical mitigation strategies, such as session level context aggregation and deep alignment approaches. Our study underscores the urgent need for holistic, context aware defenses and continuous adversarial testing to future proof LLM deployments against evolving multi-turn threats.
匹配关键词: alignment
---

[ACADEMIC - ARXIV]
标题: Seeing Fast and Slow: Learning the Flow of Time in Videos
作者: Yen-Siang Wu, Rundong Luo, Jingsen Zhu, Tao Tu, Ali Farhadi, Matthew Wallingford, Yu-Chiang Frank Wang, Steve Marschner, Wei-Chiu Ma
链接: https://arxiv.org/abs/2604.21931v1
完整摘要: How can we tell whether a video has been sped up or slowed down? How can we generate videos at different speeds? Although videos have been central to modern computer vision research, little attention has been paid to perceiving and controlling the passage of time. In this paper, we study time as a learnable visual concept and develop models for reasoning about and manipulating the flow of time in videos. We first exploit the multimodal cues and temporal structure naturally present in videos to learn, in a self-supervised manner, to detect speed changes and estimate playback speed. We then show that these learned temporal reasoning models enable us to curate the largest slow-motion video dataset to date from noisy in-the-wild sources. Such slow-motion footage, typically filmed by high-speed cameras, contains substantially richer temporal detail than standard videos. Using this data, we further develop models capable of temporal control, including speed-conditioned video generation, which produces motion at specified playback speed, and temporal super-resolution, which tranforms low-FPS, blurry videos into high-FPS sequences with fine-grained temporal details. Our findings highlight time as a manipulable, perceptual dimension in video learning, opening doors to temporally controllable video generation, temporal forensics detection, and potentially richer world-models that understand how events unfold over time.
匹配关键词: reward model
---

[ACADEMIC - ARXIV]
标题: Temporal Taskification in Streaming Continual Learning: A Source of Evaluation Instability
作者: Nicolae Filat, Ahmed Hussain, Konstantinos Kalogiannis, Elena Burceanu
链接: https://arxiv.org/abs/2604.21930v1
完整摘要: Streaming Continual Learning (CL) typically converts a continuous stream into a sequence of discrete tasks through temporal partitioning. We argue that this temporal taskification step is not a neutral preprocessing choice, but a structural component of evaluation: different valid splits of the same stream can induce different CL regimes and therefore different benchmark conclusions. To study this effect, we introduce a taskification-level framework based on plasticity and stability profiles, a profile distance between taskifications, and Boundary-Profile Sensitivity (BPS), which diagnoses how strongly small boundary perturbations alter the induced regime before any CL model is trained. We evaluate continual finetuning, Experience Replay, Elastic Weight Consolidation, and Learning without Forgetting on network traffic forecasting with CESNET-Timeseries24, keeping the stream, model, and training budget fixed while varying only the temporal taskification. Across 9-, 30-, and 44-day splits, we observe substantial changes in forecasting error, forgetting, and backward transfer, showing that taskification alone can materially affect CL evaluation. We further find that shorter taskifications induce noisier distribution-level patterns, larger structural distances, and higher BPS, indicating greater sensitivity to boundary perturbations. These results show that benchmark conclusions in streaming CL depend not only on the learner and the data stream, but also on how that stream is taskified, motivating temporal taskification as a first-class evaluation variable.
匹配关键词: reward model
---

[ACADEMIC - ARXIV]
标题: Evaluation of Automatic Speech Recognition Using Generative Large Language Models
作者: Thibault Bañeras-Roux, Shashi Kumar, Driss Khalil, Sergio Burdisso, Petr Motlicek, Shiran Liu, Mickael Rouvier, Jane Wottawa, Richard Dufour
链接: https://arxiv.org/abs/2604.21928v1
完整摘要: Automatic Speech Recognition (ASR) is traditionally evaluated using Word Error Rate (WER), a metric that is insensitive to meaning. Embedding-based semantic metrics are better correlated with human perception, but decoder-based Large Language Models (LLMs) remain underexplored for this task. This paper evaluates their relevance through three approaches: (1) selecting the best hypothesis between two candidates, (2) computing semantic distance using generative embeddings, and (3) qualitative classification of errors. On the HATS dataset, the best LLMs achieve 92--94\% agreement with human annotators for hypothesis selection, compared to 63\% for WER, also outperforming semantic metrics. Embeddings from decoder-based LLMs show performance comparable to encoder models. Finally, LLMs offer a promising direction for interpretable and semantic ASR evaluation.
匹配关键词: reward model
---

[ACADEMIC - ARXIV]
标题: Fine-Tuning Regimes Define Distinct Continual Learning Problems
作者: Paul-Tiberiu Iordache, Elena Burceanu
链接: https://arxiv.org/abs/2604.21927v1
完整摘要: Continual learning (CL) studies how models acquire tasks sequentially while retaining previously learned knowledge. Despite substantial progress in benchmarking CL methods, comparative evaluations typically keep the fine-tuning regime fixed. In this paper, we argue that the fine-tuning regime, defined by the trainable parameter subspace, is itself a key evaluation variable. We formalize adaptation regimes as projected optimization over fixed trainable subspaces, showing that changing the trainable depth alters the effective update signal through which both current task fitting and knowledge preservation operate. This analysis motivates the hypothesis that method comparisons need not be invariant across regimes. We test this hypothesis in task incremental CL, five trainable depth regimes, and four standard methods: online EWC, LwF, SI, and GEM. Across five benchmark datasets, namely MNIST, Fashion MNIST, KMNIST, QMNIST, and CIFAR-100, and across 11 task orders per dataset, we find that the relative ranking of methods is not consistently preserved across regimes. We further show that deeper adaptation regimes are associated with larger update magnitudes, higher forgetting, and a stronger relationship between the two. These results show that comparative conclusions in CL can depend strongly on the chosen fine-tuning regime, motivating regime-aware evaluation protocols that treat trainable depth as an explicit experimental factor.
匹配关键词: reward model
---

[ACADEMIC - ARXIV]
标题: Seeing Without Eyes: 4D Human-Scene Understanding from Wearable IMUs
作者: Hao-Yu Hsu, Tianhang Cheng, Jing Wen, Alexander G. Schwing, Shenlong Wang
链接: https://arxiv.org/abs/2604.21926v1
完整摘要: Understanding human activities and their surrounding environments typically relies on visual perception, yet cameras pose persistent challenges in privacy, safety, energy efficiency, and scalability. We explore an alternative: 4D perception without vision. Its goal is to reconstruct human motion and 3D scene layouts purely from everyday wearable sensors. For this we introduce IMU-to-4D, a framework that repurposes large language models for non-visual spatiotemporal understanding of human-scene dynamics. IMU-to-4D uses data from a few inertial sensors from earbuds, watches, or smartphones and predicts detailed 4D human motion together with coarse scene structure. Experiments across diverse human-scene datasets show that IMU-to-4D yields more coherent and temporally stable results than SoTA cascaded pipelines, suggesting wearable motion sensors alone can support rich 4D understanding.
匹配关键词: reward model
---

[ACADEMIC - ARXIV]
标题: Fine-Tuning Regimes Define Distinct Continual Learning Problems
作者: Paul-Tiberiu Iordache, Elena Burceanu
链接: https://arxiv.org/abs/2604.21927v1
完整摘要: Continual learning (CL) studies how models acquire tasks sequentially while retaining previously learned knowledge. Despite substantial progress in benchmarking CL methods, comparative evaluations typically keep the fine-tuning regime fixed. In this paper, we argue that the fine-tuning regime, defined by the trainable parameter subspace, is itself a key evaluation variable. We formalize adaptation regimes as projected optimization over fixed trainable subspaces, showing that changing the trainable depth alters the effective update signal through which both current task fitting and knowledge preservation operate. This analysis motivates the hypothesis that method comparisons need not be invariant across regimes. We test this hypothesis in task incremental CL, five trainable depth regimes, and four standard methods: online EWC, LwF, SI, and GEM. Across five benchmark datasets, namely MNIST, Fashion MNIST, KMNIST, QMNIST, and CIFAR-100, and across 11 task orders per dataset, we find that the relative ranking of methods is not consistently preserved across regimes. We further show that deeper adaptation regimes are associated with larger update magnitudes, higher forgetting, and a stronger relationship between the two. These results show that comparative conclusions in CL can depend strongly on the chosen fine-tuning regime, motivating regime-aware evaluation protocols that treat trainable depth as an explicit experimental factor.
匹配关键词: preference optimization
---

[ACADEMIC - ARXIV]
标题: The Sample Complexity of Multicalibration
作者: Natalie Collina, Jiuyao Lu, Georgy Noarov, Aaron Roth
链接: https://arxiv.org/abs/2604.21923v1
完整摘要: We study the minimax sample complexity of multicalibration in the batch setting. A learner observes $n$ i.i.d. samples from an unknown distribution and must output a (possibly randomized) predictor whose population multicalibration error, measured by Expected Calibration Error (ECE), is at most $\varepsilon$ with respect to a given family of groups. For every fixed $κ> 0$, in the regime $|G|\le \varepsilon^{-κ}$, we prove that $\widetildeΘ(\varepsilon^{-3})$ samples are necessary and sufficient, up to polylogarithmic factors. The lower bound holds even for randomized predictors, and the upper bound is realized by a randomized predictor obtained via an online-to-batch reduction. This separates the sample complexity of multicalibration from that of marginal calibration, which scales as $\widetildeΘ(\varepsilon^{-2})$, and shows that mean-ECE multicalibration is as difficult in the batch setting as it is in the online setting, in contrast to marginal calibration which is strictly more difficult in the online setting. In contrast we observe that for $κ= 0$, the sample complexity of multicalibration remains $\widetildeΘ(\varepsilon^{-2})$ exhibiting a sharp threshold phenomenon. More generally, we establish matching upper and lower bounds, up to polylogarithmic factors, for a weighted $L_p$ multicalibration metric for all $1 \le p \le 2$, with optimal exponent $3/p$. We also extend the lower-bound template to a regular class of elicitable properties, and combine it with the online upper bounds of Hu et al. (2025) to obtain matching bounds for calibrating properties including expectiles and bounded-density quantiles.
匹配关键词: preference optimization
---

[ACADEMIC - ARXIV]
标题: When Prompts Override Vision: Prompt-Induced Hallucinations in LVLMs
作者: Pegah Khayatan, Jayneel Parekh, Arnaud Dapogny, Mustafa Shukor, Alasdair Newson, Matthieu Cord
链接: https://arxiv.org/abs/2604.21911v1
完整摘要: Despite impressive progress in capabilities of large vision-language models (LVLMs), these systems remain vulnerable to hallucinations, i.e., outputs that are not grounded in the visual input. Prior work has attributed hallucinations in LVLMs to factors such as limitations of the vision backbone or the dominance of the language component, yet the relative importance of these factors remains unclear. To resolve this ambiguity, We propose HalluScope, a benchmark to better understand the extent to which different factors induce hallucinations. Our analysis indicates that hallucinations largely stem from excessive reliance on textual priors and background knowledge, especially information introduced through textual instructions. To mitigate hallucinations induced by textual instruction priors, we propose HalluVL-DPO, a framework for fine-tuning off-the-shelf LVLMs towards more visually grounded responses. HalluVL-DPO leverages preference optimization using a curated training dataset that we construct, guiding the model to prefer grounded responses over hallucinated ones. We demonstrate that our optimized model effectively mitigates the targeted hallucination failure mode, while preserving or improving performance on other hallucination benchmarks and visual capability evaluations. To support reproducibility and further research, we will publicly release our evaluation benchmark, preference training dataset, and code at https://pegah-kh.github.io/projects/prompts-override-vision/ .
匹配关键词: preference optimization
---

[ACADEMIC - ARXIV]
标题: From Research Question to Scientific Workflow: Leveraging Agentic AI for Science Automation
作者: Bartosz Balis, Michal Orzechowski, Piotr Kica, Michal Dygas, Michal Kuszewski
链接: https://arxiv.org/abs/2604.21910v1
完整摘要: Scientific workflow systems automate execution -- scheduling, fault tolerance, resource management -- but not the semantic translation that precedes it. Scientists still manually convert research questions into workflow specifications, a task requiring both domain knowledge and infrastructure expertise. We propose an agentic architecture that closes this gap through three layers: an LLM interprets natural language into structured intents (semantic layer); validated generators produce reproducible workflow DAGs (deterministic layer); and domain experts author ``Skills'': markdown documents encoding vocabulary mappings, parameter constraints, and optimization strategies (knowledge layer). This decomposition confines LLM non-determinism to intent extraction: identical intents always yield identical workflows. We implement and evaluate the architecture on the 1000 Genomes population genetics workflow and Hyperflow WMS running on Kubernetes. In an ablation study on 150 queries, Skills raise full-match intent accuracy from 44% to 83%; skill-driven deferred workflow generation reduces data transfer by 92\%; and the end-to-end pipeline completes queries on Kubernetes with LLM overhead below 15 seconds and cost under $0.001 per query.
匹配关键词: preference optimization
---

[ACADEMIC - ARXIV]
标题: Low-Rank Adaptation Redux for Large Models
作者: Bingcong Li, Yilang Zhang, Georgios B. Giannakis
链接: https://arxiv.org/abs/2604.21905v1
完整摘要: Low-rank adaptation (LoRA) has emerged as the de facto standard for parameter-efficient fine-tuning (PEFT) of foundation models, enabling the adaptation of billion-parameter networks with minimal computational and memory overhead. Despite its empirical success and rapid proliferation of variants, it remains elusive which architectural choices, optimization techniques, and deployment constraints should guide practical method selection. This overview revisits LoRA through the lens of signal processing (SP), bridging modern adapter designs with classical low-rank modeling tools and inverse problems, as well as highlighting how SP principles can inform principled advances of fine-tuning approaches. Rather than providing a comprehensive enumeration and empirical comparisons of LoRA variants, emphasis is placed on the technical mechanisms underpinning these approaches to justify their effectiveness. These advances are categorized into three complementary axes: architectural design, efficient optimization, and pertinent applications. The first axis builds on singular value decomposition (SVD)-based factorization, rank-augmentation constructions, and cross-layer tensorization, while the second axis deals with initialization, alternating solvers, gauge-invariant optimization, and parameterization-aware methods. Beyond fine-tuning, emerging applications of LoRA are accounted across the entire lifecycle of large models, ranging from pre- and post-training to serving/deployment. Finally, open research directions are outlined at the confluence of SP and deep learning to catalyze a bidirectional frontier: classical SP tools provide a principled vocabulary for designing principled PEFT methods, while the unique challenges facing modern deep learning, especially the overwhelming scale and prohibitive overhead, also offer new research lines benefiting the SP community in return.
匹配关键词: preference optimization
---

[ACADEMIC - ARXIV]
标题: From Research Question to Scientific Workflow: Leveraging Agentic AI for Science Automation
作者: Bartosz Balis, Michal Orzechowski, Piotr Kica, Michal Dygas, Michal Kuszewski
链接: https://arxiv.org/abs/2604.21910v1
完整摘要: Scientific workflow systems automate execution -- scheduling, fault tolerance, resource management -- but not the semantic translation that precedes it. Scientists still manually convert research questions into workflow specifications, a task requiring both domain knowledge and infrastructure expertise. We propose an agentic architecture that closes this gap through three layers: an LLM interprets natural language into structured intents (semantic layer); validated generators produce reproducible workflow DAGs (deterministic layer); and domain experts author ``Skills'': markdown documents encoding vocabulary mappings, parameter constraints, and optimization strategies (knowledge layer). This decomposition confines LLM non-determinism to intent extraction: identical intents always yield identical workflows. We implement and evaluate the architecture on the 1000 Genomes population genetics workflow and Hyperflow WMS running on Kubernetes. In an ablation study on 150 queries, Skills raise full-match intent accuracy from 44% to 83%; skill-driven deferred workflow generation reduces data transfer by 92\%; and the end-to-end pipeline completes queries on Kubernetes with LLM overhead below 15 seconds and cost under $0.001 per query.
匹配关键词: constitutional AI
---

[ACADEMIC - ARXIV]
标题: Nemobot Games: Crafting Strategic AI Gaming Agents for Interactive Learning with Large Language Models
作者: Chee Wei Tan, Yuchen Wang, Shangxin Guo
链接: https://arxiv.org/abs/2604.21896v1
完整摘要: This paper introduces a new paradigm for AI game programming, leveraging large language models (LLMs) to extend and operationalize Claude Shannon's taxonomy of game-playing machines. Central to this paradigm is Nemobot, an interactive agentic engineering environment that enables users to create, customize, and deploy LLM-powered game agents while actively engaging with AI-driven strategies. The LLM-based chatbot, integrated within Nemobot, demonstrates its capabilities across four distinct classes of games. For dictionary-based games, it compresses state-action mappings into efficient, generalized models for rapid adaptability. In rigorously solvable games, it employs mathematical reasoning to compute optimal strategies and generates human-readable explanations for its decisions. For heuristic-based games, it synthesizes strategies by combining insights from classical minimax algorithms (see, e.g., shannon1950chess) with crowd-sourced data. Finally, in learning-based games, it utilizes reinforcement learning with human feedback and self-critique to iteratively refine strategies through trial-and-error and imitation learning. Nemobot amplifies this framework by offering a programmable environment where users can experiment with tool-augmented generation and fine-tuning of strategic game agents. From strategic games to role-playing games, Nemobot demonstrates how AI agents can achieve a form of self-programming by integrating crowdsourced learning and human creativity to iteratively refine their own logic. This represents a step toward the long-term goal of self-programming AI.
匹配关键词: constitutional AI
---

[ACADEMIC - ARXIV]
标题: Addressing Image Authenticity When Cameras Use Generative AI
作者: Umar Masud, Abhijith Punnappurath, Luxi Zhao, David B. Lindell, Michael S. Brown
链接: https://arxiv.org/abs/2604.21879v1
完整摘要: The ability of generative AI (GenAI) methods to photorealistically alter camera images has raised awareness about the authenticity of images shared online. Interestingly, images captured directly by our cameras are considered authentic and faithful. However, with the increasing integration of deep-learning modules into cameras' capture-time hardware -- namely, the image signal processor (ISP) -- there is now a potential for hallucinated content in images directly output by our cameras. Hallucinated capture-time image content is typically benign, such as enhanced edges or texture, but in certain operations, such as AI-based digital zoom or low-light image enhancement, hallucinations can potentially alter the semantics and interpretation of the image content. As a result, users may not realize that the content in their camera images is not authentic. This paper addresses this issue by enabling users to recover the 'unhallucinated' version of the camera image to avoid misinterpretation of the image content. Our approach works by optimizing an image-specific multi-layer perceptron (MLP) decoder together with a modality-specific encoder so that, given the camera image, we can recover the image before hallucinated content was added. The encoder and MLP are self-contained and can be applied post-capture to the image without requiring access to the camera ISP. Moreover, the encoder and MLP decoder require only 180 KB of storage and can be readily saved as metadata within standard image formats such as JPEG and HEIC.
匹配关键词: constitutional AI
---

[ACADEMIC - ARXIV]
标题: Bounding the Black Box: A Statistical Certification Framework for AI Risk Regulation
作者: Natan Levy, Gadi Perl
链接: https://arxiv.org/abs/2604.21854v1
完整摘要: Artificial intelligence now decides who receives a loan, who is flagged for criminal investigation, and whether an autonomous vehicle brakes in time. Governments have responded: the EU AI Act, the NIST Risk Management Framework, and the Council of Europe Convention all demand that high-risk systems demonstrate safety before deployment. Yet beneath this regulatory consensus lies a critical vacuum: none specifies what ``acceptable risk'' means in quantitative terms, and none provides a technical method for verifying that a deployed system actually meets such a threshold. The regulatory architecture is in place; the verification instrument is not. This gap is not theoretical. As the EU AI Act moves into full enforcement, developers face mandatory conformity assessments without established methodologies for producing quantitative safety evidence - and the systems most in need of oversight are opaque statistical inference engines that resist white-box scrutiny. This paper provides the missing instrument. Drawing on the aviation certification paradigm, we propose a two-stage framework that transforms AI risk regulation into engineering practice. In Stage One, a competent authority formally fixes an acceptable failure probability $δ$ and an operational input domain $\varepsilon$ - a normative act with direct civil liability implications. In Stage Two, the RoMA and gRoMA statistical verification tools compute a definitive, auditable upper bound on the system's true failure rate, requiring no access to model internals and scaling to arbitrary architectures. We demonstrate how this certificate satisfies existing regulatory obligations, shifts accountability upstream to developers, and integrates with the legal frameworks that exist today.
匹配关键词: constitutional AI
---

[ACADEMIC - ARXIV]
标题: Alignment has a Fantasia Problem
作者: Nathanael Jo, Zoe De Simone, Mitchell Gordon, Ashia Wilson
链接: https://arxiv.org/abs/2604.21827v1
完整摘要: Modern AI assistants are trained to follow instructions, implicitly assuming that users can clearly articulate their goals and the kind of assistance they need. Decades of behavioral research, however, show that people often engage with AI systems before their goals are fully formed. When AI systems treat prompts as complete expressions of intent, they can appear to be useful or convenient, but not necessarily aligned with the users' needs. We call these failures Fantasia interactions. We argue that Fantasia interactions demand a rethinking of alignment research: rather than treating users as rational oracles, AI should provide cognitive support by actively helping users form and refine their intent through time. This requires an interdisciplinary approach that bridges machine learning, interface design, and behavioral science. We synthesize insights from these fields to characterize the mechanisms and failures of Fantasia interactions. We then show why existing interventions are insufficient, and propose a research agenda for designing and evaluating AI systems that better help humans navigate uncertainty in their tasks.
匹配关键词: constitutional AI
---

[ACADEMIC - ARXIV]
标题: Seeing Fast and Slow: Learning the Flow of Time in Videos
作者: Yen-Siang Wu, Rundong Luo, Jingsen Zhu, Tao Tu, Ali Farhadi, Matthew Wallingford, Yu-Chiang Frank Wang, Steve Marschner, Wei-Chiu Ma
链接: https://arxiv.org/abs/2604.21931v1
完整摘要: How can we tell whether a video has been sped up or slowed down? How can we generate videos at different speeds? Although videos have been central to modern computer vision research, little attention has been paid to perceiving and controlling the passage of time. In this paper, we study time as a learnable visual concept and develop models for reasoning about and manipulating the flow of time in videos. We first exploit the multimodal cues and temporal structure naturally present in videos to learn, in a self-supervised manner, to detect speed changes and estimate playback speed. We then show that these learned temporal reasoning models enable us to curate the largest slow-motion video dataset to date from noisy in-the-wild sources. Such slow-motion footage, typically filmed by high-speed cameras, contains substantially richer temporal detail than standard videos. Using this data, we further develop models capable of temporal control, including speed-conditioned video generation, which produces motion at specified playback speed, and temporal super-resolution, which tranforms low-FPS, blurry videos into high-FPS sequences with fine-grained temporal details. Our findings highlight time as a manipulable, perceptual dimension in video learning, opening doors to temporally controllable video generation, temporal forensics detection, and potentially richer world-models that understand how events unfold over time.
匹配关键词: reasoning
---

[ACADEMIC - ARXIV]
标题: Long-Horizon Manipulation via Trace-Conditioned VLA Planning
作者: Isabella Liu, An-Chieh Cheng, Rui Yan, Geng Chen, Ri-Zhao Qiu, Xueyan Zou, Sha Yi, Hongxu Yin, Xiaolong Wang, Sifei Liu
链接: https://arxiv.org/abs/2604.21924v1
完整摘要: Long-horizon manipulation remains challenging for vision-language-action (VLA) policies: real tasks are multi-step, progress-dependent, and brittle to compounding execution errors. We present LoHo-Manip, a modular framework that scales short-horizon VLA execution to long-horizon instruction following via a dedicated task-management VLM. The manager is decoupled from the executor and is invoked in a receding-horizon manner: given the current observation, it predicts a progress-aware remaining plan that combines (i) a subtask sequence with an explicit done + remaining split as lightweight language memory, and (ii) a visual trace -- a compact 2D keypoint trajectory prompt specifying where to go and what to approach next. The executor VLA is adapted to condition on the rendered trace, thereby turning long-horizon decision-making into repeated local control by following the trace. Crucially, predicting the remaining plan at each step yields an implicit closed loop: failed steps persist in subsequent outputs, and traces update accordingly, enabling automatic continuation and replanning without hand-crafted recovery logic or brittle visual-history buffers. Extensive experiments spanning embodied planning, long-horizon reasoning, trajectory prediction, and end-to-end manipulation in simulation and on a real Franka robot demonstrate strong gains in long-horizon success, robustness, and out-of-distribution generalization. Project page: https://www.liuisabella.com/LoHoManip
匹配关键词: reasoning
---

[ACADEMIC - ARXIV]
标题: Context Unrolling in Omni Models
作者: Ceyuan Yang, Zhijie Lin, Yang Zhao, Fei Xiao, Hao He, Qi Zhao, Chaorui Deng, Kunchang Li, Zihan Ding, Yuwei Guo, Fuyun Wang, Fangqi Zhu, Xiaonan Nie, Shenhan Zhu, Shanchuan Lin, Hongsheng Li, Weilin Huang, Guang Shi, Haoqi Fan
链接: https://arxiv.org/abs/2604.21921v1
完整摘要: We present Omni, a unified multimodal model natively trained on diverse modalities, including text, images, videos, 3D geometry, and hidden representations. We find that such training enables Context Unrolling, where the model explicitly reasons across multiple modal representations before producing predictions. This process enables the model to aggregate complementary information across heterogeneous modalities, facilitating a more faithful approximation of the shared multimodal knowledge manifold and improving downstream reasoning fidelity. As a result, Omni achieves strong performance on both multimodal generation and understanding benchmarks, while demonstrating advanced multimodal reasoning capabilities, including in-context generation of text, image, video, and 3D geometry.
匹配关键词: reasoning
---

[ACADEMIC - ARXIV]
标题: Nemobot Games: Crafting Strategic AI Gaming Agents for Interactive Learning with Large Language Models
作者: Chee Wei Tan, Yuchen Wang, Shangxin Guo
链接: https://arxiv.org/abs/2604.21896v1
完整摘要: This paper introduces a new paradigm for AI game programming, leveraging large language models (LLMs) to extend and operationalize Claude Shannon's taxonomy of game-playing machines. Central to this paradigm is Nemobot, an interactive agentic engineering environment that enables users to create, customize, and deploy LLM-powered game agents while actively engaging with AI-driven strategies. The LLM-based chatbot, integrated within Nemobot, demonstrates its capabilities across four distinct classes of games. For dictionary-based games, it compresses state-action mappings into efficient, generalized models for rapid adaptability. In rigorously solvable games, it employs mathematical reasoning to compute optimal strategies and generates human-readable explanations for its decisions. For heuristic-based games, it synthesizes strategies by combining insights from classical minimax algorithms (see, e.g., shannon1950chess) with crowd-sourced data. Finally, in learning-based games, it utilizes reinforcement learning with human feedback and self-critique to iteratively refine strategies through trial-and-error and imitation learning. Nemobot amplifies this framework by offering a programmable environment where users can experiment with tool-augmented generation and fine-tuning of strategic game agents. From strategic games to role-playing games, Nemobot demonstrates how AI agents can achieve a form of self-programming by integrating crowdsourced learning and human creativity to iteratively refine their own logic. This represents a step toward the long-term goal of self-programming AI.
匹配关键词: reasoning
---

[ACADEMIC - ARXIV]
标题: Task-Driven Co-Design of Heterogeneous Multi-Robot Systems
作者: Maximilian Stralz, Meshal Alharbi, Yujun Huang, Gioele Zardini
链接: https://arxiv.org/abs/2604.21894v1
完整摘要: Designing multi-agent robotic systems requires reasoning across tightly coupled decisions spanning heterogeneous domains, including robot design, fleet composition, and planning. Much effort has been devoted to isolated improvements in these domains, whereas system-level co-design considering trade-offs and task requirements remains underexplored. In this work, we present a formal and compositional framework for the task-driven co-design of heterogeneous multi-robot systems. Building on a monotone co-design theory, we introduce general abstractions of robots, fleets, planners, executors, and evaluators as interconnected design problems with well-defined interfaces that are agnostic to both implementations and tasks. This structure enables efficient joint optimization of robot design, fleet composition, and planning under task-specific performance constraints. A series of case studies demonstrates the capabilities of the framework. Various component models can be seamlessly incorporated, including new robot types, task profiles, and probabilistic sensing objectives, while non-obvious design alternatives are systematically uncovered with optimality guarantees. The results highlight the flexibility, scalability, and interpretability of the proposed approach, and illustrate how formal co-design enables principled reasoning about complex heterogeneous multi-robot systems.
匹配关键词: reasoning
---

[ACADEMIC - ARXIV]
标题: From Codebooks to VLMs: Evaluating Automated Visual Discourse Analysis for Climate Change on Social Media
作者: Katharina Prasse, Steffen Jung, Isaac Bravo, Stefanie Walter, Patrick Knab, Christian Bartelt, Margret Keuper
链接: https://arxiv.org/abs/2604.21786v1
完整摘要: Social media platforms have become primary arenas for climate communication, generating millions of images and posts that - if systematically analysed - can reveal which communication strategies mobilise public concern and which fall flat. We aim to facilitate such research by analysing how computer vision methods can be used for social media discourse analysis. This analysis includes application-based taxonomy design, model selection, prompt engineering, and validation. We benchmark six promptable vision-language models and 15 zero-shot CLIP-like models on two datasets from X (formerly Twitter) - a 1,038-image expert-annotated set and a larger corpus of over 1.2 million images, with 50,000 labels manually validated - spanning five annotation dimensions: animal content, climate change consequences, climate action, image setting, and image type. Among the models benchmarked, Gemini-3.1-flash-lite outperforms all others across all super-categories and both datasets, while the gap to open-weight models of moderate size remains relatively small. Beyond instance-level metrics, we advocate for distributional evaluation: VLM predictions can reliably recover population level trends even when per-image accuracy is moderate, making them a viable starting point for discourse analysis at scale. We find that chain-of-thought reasoning reduces rather than improves performance, and that annotation dimension specific prompt design improves performance. We release tweet IDs and labels along with our code at https://github.com/KathPra/Codebooks2VLMs.git.
匹配关键词: chain-of-thought
---

[ACADEMIC - ARXIV]
标题: Thinking with Reasoning Skills: Fewer Tokens, More Accuracy
作者: Guangxiang Zhao, Qilong Shi, Xusen Xiao, Xiangzheng Zhang, Tong Yang, Lin Sun
链接: https://arxiv.org/abs/2604.21764v1
完整摘要: Reasoning LLMs often spend substantial tokens on long intermediate reasoning traces (e.g., chain-of-thought) when solving new problems. We propose to summarize and store reusable reasoning skills distilled from extensive deliberation and trial-and-error exploration, and to retrieve these skills at inference time to guide future reasoning. Unlike the prevailing \emph{reasoning from scratch} paradigm, our approach first recalls relevant skills for each query, helping the model avoid redundant detours and focus on effective solution paths. We evaluate our method on coding and mathematical reasoning tasks, and find that it significantly reduces reasoning tokens while improving overall performance. The resulting lower per-request cost indicates strong practical and economic potential for real-world deployment.
匹配关键词: chain-of-thought
---

[ACADEMIC - ARXIV]
标题: Language as a Latent Variable for Reasoning Optimization
作者: Linjuan Wu, Haoran Wei, Jialong Tang, Shuang Luo, Baosong Yang, Yongliang Shen, Weiming Lu
链接: https://arxiv.org/abs/2604.21593v1
完整摘要: As LLMs reduce English-centric bias, a surprising trend emerges: non-English responses sometimes outperform English on reasoning tasks. We hypothesize that language functions as a latent variable that structurally modulates the model's internal inference pathways, rather than merely serving as an output medium. To test this, we conducted a Polyglot Thinking Experiment, in which models were prompted to solve identical problems under language-constrained and language-unconstrained conditions. Results show that non-English responses often achieve higher accuracy, and the best performance frequently occur when language is unconstrained, suggesting that multilinguality broadens the model's latent reasoning space. Based on this insight, we propose polyGRPO (Polyglot Group Relative Policy Optimization), an RL framework that treats language variation as an implicit exploration signal. It generates polyglot preference data online under language-constrained and unconstrained conditions, optimizing the policy with respect to both answer accuracy and reasoning structure. Trained on only 18.1K multilingual math problems without chain-of-thought annotations, polyGRPO improves the base model (Qwen2.5-7B-Instruct) by 6.72% absolute accuracy on four English reasoning testset and 6.89% in their multilingual benchmark. Remarkably, it is the only method that surpasses the base LLM on English commonsense reasoning task (4.9%), despite being trained solely on math data-highlighting its strong cross-task generalization. Further analysis reveals that treating language as a latent variable expands the model's latent reasoning space, yielding consistent and generalizable improvements in reasoning performance.
匹配关键词: chain-of-thought
---

[ACADEMIC - ARXIV]
标题: S1-VL: Scientific Multimodal Reasoning Model with Thinking-with-Images
作者: Qingxiao Li, Lifeng Xu, QingLi Wang, Yudong Bai, Mingwei Ou, Shu Hu, Nan Xu
链接: https://arxiv.org/abs/2604.21409v1
完整摘要: We present S1-VL, a multimodal reasoning model for scientific domains that natively supports two complementary reasoning paradigms: Scientific Reasoning, which relies on structured chain-of-thought, and Thinking-with-Images, which enables the model to actively manipulate images through Python code execution during reasoning. In the Thinking-with-Images mode, the model generates and executes image-processing code in a sandbox environment, obtains intermediate visual results, and continues reasoning in a multi-turn iterative manner. This design is particularly effective for challenging scenarios such as high-resolution scientific chart interpretation, microscopic image understanding, and geometry-assisted reasoning. To construct the training data, we collect scientific multimodal datasets spanning six disciplines: mathematics, physics, chemistry, astronomy, geography, and biology. We further develop a six-dimensional quality filtering framework for reasoning trajectories. To mitigate redundant, ineffective, and erroneous visual operations commonly found in existing datasets, we propose a multi-stage filtering pipeline together with an adaptive data routing strategy. This strategy converts samples with low visual information gain into pure Reasoning-mode data, enabling the model to learn when image operations are truly necessary. S1-VL is trained through a four-stage progressive pipeline: scientific multimodal SFT, Thinking-with-Images cold-start SFT, and two stages of reinforcement learning with SAPO. We build S1-VL-32B on top of Qwen3-VL-32B-Thinking and evaluate it on 13 benchmarks. Experimental results show that S1-VL-32B achieves state-of-the-art performance on all five Thinking-with-Images benchmarks, including HRBench-4K, HRBench-8K, MME-RealWorld-CN, MME-RealWorld-Lite, and V*, and outperforms compared systems on scientific reasoning benchmarks such as Physics and VRSBench.
匹配关键词: chain-of-thought
---

[ACADEMIC - ARXIV]
标题: VG-CoT: Towards Trustworthy Visual Reasoning via Grounded Chain-of-Thought
作者: Byeonggeuk Lim, Kyeonghyun Kim, JungMin Yun, YoungBin Kim
链接: https://arxiv.org/abs/2604.21396v1
完整摘要: The advancement of Large Vision-Language Models (LVLMs) requires precise local region-based reasoning that faithfully grounds the model's logic in actual visual evidence. However, existing datasets face limitations in scalability due to extensive manual annotation and lack of explicit alignment between multi-step reasoning and corresponding image regions, which constrains the evaluation of model trustworthiness. To address these challenges, we propose the Visual Grounding Chain-of-Thought (VG-CoT) dataset, which explicitly links each reasoning step to real visual evidence within the image through a fully automated three-stage pipeline. The pipeline first extracts object- and text-level visual evidence using state-of-the-art detection and OCR models, then generates step-by-step grounded reasoning with GPT-4o, and finally refines the grounding through a rationale-driven open-set detection process. In addition, we introduce a new benchmark that comprehensively evaluates LVLMs reasoning across three complementary dimensions: Rationale Quality, Answer Accuracy, and Reasoning-Answer Alignment. Experiments with representative LVLMs, including LLaVA-1.5 and Qwen2-VL, demonstrate consistent improvements on most evaluation metrics, confirming that VG-CoT effectively enhances trustworthy, evidence-based reasoning while maintaining scalable and cost-efficient dataset construction. The dataset and code will be released publicly upon acceptance to facilitate further research.
匹配关键词: chain-of-thought
---

[ACADEMIC - ARXIV]
标题: Seeing Fast and Slow: Learning the Flow of Time in Videos
作者: Yen-Siang Wu, Rundong Luo, Jingsen Zhu, Tao Tu, Ali Farhadi, Matthew Wallingford, Yu-Chiang Frank Wang, Steve Marschner, Wei-Chiu Ma
链接: https://arxiv.org/abs/2604.21931v1
完整摘要: How can we tell whether a video has been sped up or slowed down? How can we generate videos at different speeds? Although videos have been central to modern computer vision research, little attention has been paid to perceiving and controlling the passage of time. In this paper, we study time as a learnable visual concept and develop models for reasoning about and manipulating the flow of time in videos. We first exploit the multimodal cues and temporal structure naturally present in videos to learn, in a self-supervised manner, to detect speed changes and estimate playback speed. We then show that these learned temporal reasoning models enable us to curate the largest slow-motion video dataset to date from noisy in-the-wild sources. Such slow-motion footage, typically filmed by high-speed cameras, contains substantially richer temporal detail than standard videos. Using this data, we further develop models capable of temporal control, including speed-conditioned video generation, which produces motion at specified playback speed, and temporal super-resolution, which tranforms low-FPS, blurry videos into high-FPS sequences with fine-grained temporal details. Our findings highlight time as a manipulable, perceptual dimension in video learning, opening doors to temporally controllable video generation, temporal forensics detection, and potentially richer world-models that understand how events unfold over time.
匹配关键词: test-time compute
---

[ACADEMIC - ARXIV]
标题: Evaluation of Automatic Speech Recognition Using Generative Large Language Models
作者: Thibault Bañeras-Roux, Shashi Kumar, Driss Khalil, Sergio Burdisso, Petr Motlicek, Shiran Liu, Mickael Rouvier, Jane Wottawa, Richard Dufour
链接: https://arxiv.org/abs/2604.21928v1
完整摘要: Automatic Speech Recognition (ASR) is traditionally evaluated using Word Error Rate (WER), a metric that is insensitive to meaning. Embedding-based semantic metrics are better correlated with human perception, but decoder-based Large Language Models (LLMs) remain underexplored for this task. This paper evaluates their relevance through three approaches: (1) selecting the best hypothesis between two candidates, (2) computing semantic distance using generative embeddings, and (3) qualitative classification of errors. On the HATS dataset, the best LLMs achieve 92--94\% agreement with human annotators for hypothesis selection, compared to 63\% for WER, also outperforming semantic metrics. Embeddings from decoder-based LLMs show performance comparable to encoder models. Finally, LLMs offer a promising direction for interpretable and semantic ASR evaluation.
匹配关键词: test-time compute
---

[ACADEMIC - ARXIV]
标题: VistaBot: View-Robust Robot Manipulation via Spatiotemporal-Aware View Synthesis
作者: Songen Gu, Yuhang Zheng, Weize Li, Yupeng Zheng, Yating Feng, Xiang Li, Yilun Chen, Pengfei Li, Wenchao Ding
链接: https://arxiv.org/abs/2604.21914v1
完整摘要: Recently, end-to-end robotic manipulation models have gained significant attention for their generalizability and scalability. However, they often suffer from limited robustness to camera viewpoint changes when training with a fixed camera. In this paper, we propose VistaBot, a novel framework that integrates feed-forward geometric models with video diffusion models to achieve view-robust closed-loop manipulation without requiring camera calibration at test time. Our approach consists of three key components: 4D geometry estimation, view synthesis latent extraction, and latent action learning. VistaBot is integrated into both action-chunking (ACT) and diffusion-based ($π_0$) policies and evaluated across simulation and real-world tasks. We further introduce the View Generalization Score (VGS) as a new metric for comprehensive evaluation of cross-view generalization. Results show that VistaBot improves VGS by 2.79$\times$ and 2.63$\times$ over ACT and $π_0$, respectively, while also achieving high-quality novel view synthesis. Our contributions include a geometry-aware synthesis model, a latent action planner, a new benchmark metric, and extensive validation across diverse environments. The code and models will be made publicly available.
匹配关键词: test-time compute
---

[ACADEMIC - ARXIV]
标题: Low-Rank Adaptation Redux for Large Models
作者: Bingcong Li, Yilang Zhang, Georgios B. Giannakis
链接: https://arxiv.org/abs/2604.21905v1
完整摘要: Low-rank adaptation (LoRA) has emerged as the de facto standard for parameter-efficient fine-tuning (PEFT) of foundation models, enabling the adaptation of billion-parameter networks with minimal computational and memory overhead. Despite its empirical success and rapid proliferation of variants, it remains elusive which architectural choices, optimization techniques, and deployment constraints should guide practical method selection. This overview revisits LoRA through the lens of signal processing (SP), bridging modern adapter designs with classical low-rank modeling tools and inverse problems, as well as highlighting how SP principles can inform principled advances of fine-tuning approaches. Rather than providing a comprehensive enumeration and empirical comparisons of LoRA variants, emphasis is placed on the technical mechanisms underpinning these approaches to justify their effectiveness. These advances are categorized into three complementary axes: architectural design, efficient optimization, and pertinent applications. The first axis builds on singular value decomposition (SVD)-based factorization, rank-augmentation constructions, and cross-layer tensorization, while the second axis deals with initialization, alternating solvers, gauge-invariant optimization, and parameterization-aware methods. Beyond fine-tuning, emerging applications of LoRA are accounted across the entire lifecycle of large models, ranging from pre- and post-training to serving/deployment. Finally, open research directions are outlined at the confluence of SP and deep learning to catalyze a bidirectional frontier: classical SP tools provide a principled vocabulary for designing principled PEFT methods, while the unique challenges facing modern deep learning, especially the overwhelming scale and prohibitive overhead, also offer new research lines benefiting the SP community in return.
匹配关键词: test-time compute
---

[ACADEMIC - ARXIV]
标题: Mapping the Political Discourse in the Brazilian Chamber of Deputies: A Multi-Faceted Computational Approach
作者: Flávio Soriano, Victoria F. Mello, Pedro B. Rigueira, Gisele L. Pappa, Wagner Meira, Ana Paula Couto da Silva, Jussara M. Almeida
链接: https://arxiv.org/abs/2604.21897v1
完整摘要: Analyses of legislative behavior often rely on voting records, overlooking the rich semantic and rhetorical content of political speech. In this paper, we ask three complementary questions about parliamentary discourse: how things are said, what is being said, and who is speaking in discursively similar ways. To answer these questions, we introduce a scalable and generalizable computational framework that combines diachronic stylometric analysis, contextual topic modeling, and semantic clustering of deputies' speeches. We apply this framework to a large-scale case study of the Brazilian Chamber of Deputies, using a corpus of over 450,000 speeches from 2003 to 2025. Our results show a long-term stylistic shift toward shorter and more direct speeches, a legislative agenda that reorients sharply in response to national crises, and a granular map of discursive alignments in which regional and gender identities often prove more salient than formal party affiliation. More broadly, this work offers a robust methodology for analyzing parliamentary discourse as a multidimensional phenomenon that complements traditional vote-based approaches.
匹配关键词: test-time compute
---

[ACADEMIC - ARXIV]
标题: Reshoot-Anything: A Self-Supervised Model for In-the-Wild Video Reshooting
作者: Avinash Paliwal, Adithya Iyer, Shivin Yadav, Muhammad Ali Afridi, Midhun Harikumar
链接: https://arxiv.org/abs/2604.21776v1
完整摘要: Precise camera control for reshooting dynamic videos is bottlenecked by the severe scarcity of paired multi-view data for non-rigid scenes. We overcome this limitation with a highly scalable self-supervised framework capable of leveraging internet-scale monocular videos. Our core contribution is the generation of pseudo multi-view training triplets, consisting of a source video, a geometric anchor, and a target video. We achieve this by extracting distinct smooth random-walk crop trajectories from a single input video to serve as the source and target views. The anchor is synthetically generated by forward-warping the first frame of the source with a dense tracking field, which effectively simulates the distorted point-cloud inputs expected at inference. Because our independent cropping strategy introduces spatial misalignment and artificial occlusions, the model cannot simply copy information from the current source frame. Instead, it is forced to implicitly learn 4D spatiotemporal structures by actively routing and re-projecting missing high-fidelity textures across distinct times and viewpoints from the source video to reconstruct the target. At inference, our minimally adapted diffusion transformer utilizes a 4D point-cloud derived anchor to achieve state-of-the-art temporal consistency, robust camera control, and high-fidelity novel view synthesis on complex dynamic scenes.
匹配关键词: self-consistency
---

[ACADEMIC - ARXIV]
标题: DualSplat: Robust 3D Gaussian Splatting via Pseudo-Mask Bootstrapping from Reconstruction Failures
作者: Xu Wang, Zhiru Wang, Shiyun Xie, Chengwei Pan, Yisong Chen
链接: https://arxiv.org/abs/2604.21631v1
完整摘要: While 3D Gaussian Splatting (3DGS) achieves real-time photorealistic rendering, its performance degrades significantly when training images contain transient objects that violate multi-view consistency. Existing methods face a circular dependency: accurate transient detection requires a well-reconstructed static scene, while clean reconstruction itself depends on reliable transient masks. We address this challenge with DualSplat, a Failure-to-Prior framework that converts first-pass reconstruction failures into explicit priors for a second reconstruction stage. We observe that transients, which appear in only a subset of views, often manifest as incomplete fragments during conservative initial training. We exploit these failures to construct object-level pseudo-masks by combining photometric residuals, feature mismatches, and SAM2 instance boundaries. These pseudo-masks then guide a clean second-pass 3DGS optimization, while a lightweight MLP refines them online by gradually shifting from prior supervision to self-consistency. Experiments on RobustNeRF and NeRF On-the-go show that DualSplat outperforms existing baselines, demonstrating particularly clear advantages in transient-heavy scenes and transient regions.
匹配关键词: self-consistency
---

[ACADEMIC - ARXIV]
标题: Process Supervision via Verbal Critique Improves Reasoning in Large Language Models
作者: Hao-Yuan Chen
链接: https://arxiv.org/abs/2604.21611v1
完整摘要: Inference-time scaling for LLM reasoning has focused on three axes: chain depth, sample breadth, and learned step-scorers (PRMs). We introduce a fourth axis, granularity of external verbal supervision, via Verbal Process Supervision (VPS), a training-free framework that uses structured natural-language critique from a stronger supervisor to guide an iterative generate-critique-refine loop up to a round budget R. Across GPQA Diamond, AIME 2025, and LiveCodeBench V6 (covering both closed and open models), VPS yields three key results. First, on GPQA Diamond, GPT-5.4 (High) | GPT-5.4 (Low) reaches 94.9% at R=4, surpassing the 94.1% state of the art without gradient updates. Second, on AIME 2025, VPS enables strong weak-actor rescue, boosting scores from 11.7-26.7% to 63.3-90.0% (up to +63.3 points). Third, at matched compute, VPS outperforms Reflexion by +8.5 to +12.1 points and Self-Consistency@5 by +5.0 pp (GPQA) and +8.3 pp (LiveCodeBench), isolating critique granularity as the key driver. Performance scales with the supervisor-actor capability gap (Pearson r=0.90) and degrades when errors are not linguistically expressible (e.g., code synthesis), motivating hybrid verbal-executable methods. These results establish critique granularity as a new axis of inference-time scaling.
匹配关键词: self-consistency
---

[ACADEMIC - ARXIV]
标题: Trust-SSL: Additive-Residual Selective Invariance for Robust Aerial Self-Supervised Learning
作者: Wadii Boulila, Adel Ammar, Bilel Benjdira, Maha Driss
链接: https://arxiv.org/abs/2604.21349v1
完整摘要: Self-supervised learning (SSL) is a standard approach for representation learning in aerial imagery. Existing methods enforce invariance between augmented views, which works well when augmentations preserve semantic content. However, aerial images are frequently degraded by haze, motion blur, rain, and occlusion that remove critical evidence. Enforcing alignment between a clean and a severely degraded view can introduce spurious structure into the latent space. This study proposes a training strategy and architectural modification to enhance SSL robustness to such corruptions. It introduces a per-sample, per-factor trust weight into the alignment objective, combined with the base contrastive loss as an additive residual. A stop-gradient is applied to the trust weight instead of a multiplicative gate. While a multiplicative gate is a natural choice, experiments show it impairs the backbone, whereas our additive-residual approach improves it. Using a 200-epoch protocol on a 210,000-image corpus, the method achieves the highest mean linear-probe accuracy among six backbones on EuroSAT, AID, and NWPU-RESISC45 (90.20% compared to 88.46% for SimCLR and 89.82% for VICReg). It yields the largest improvements under severe information-erasing corruptions on EuroSAT (+19.9 points on haze at s=5 over SimCLR). The method also demonstrates consistent gains of +1 to +3 points in Mahalanobis AUROC on a zero-shot cross-domain stress test using BDD100K weather splits. Two ablations (scalar uncertainty and cosine gate) indicate the additive-residual formulation is the primary source of these improvements. An evidential variant using Dempster-Shafer fusion introduces interpretable signals of conflict and ignorance. These findings offer a concrete design principle for uncertainty-aware SSL. Code is publicly available at https://github.com/WadiiBoulila/trust-ssl.
匹配关键词: self-consistency
---

[ACADEMIC - ARXIV]
标题: Measure Twice, Click Once: Co-evolving Proposer and Visual Critic via Reinforcement Learning for GUI Grounding
作者: Wenkai Wang, Xiyun Li, Hongcan Guo, Wenhao Yu, Tianqing Fang, Haitao Mi, Dong Yu, Shengyu Zhang
链接: https://arxiv.org/abs/2604.21268v1
完整摘要: Graphical User Interface (GUI) grounding requires mapping natural language instructions to precise pixel coordinates. However, due to visually homogeneous elements and dense layouts, models typically grasp semantic intent yet struggle with achieving precise localization. While scaling sampling attempts (Pass@k) reveals potential gains, static self-consistency strategies derived from geometric clustering often yield limited improvements, as the model's predictions tend to be spatially dispersed. In this paper, we propose replacing static consistency strategies with a learnable selection mechanism that selects the optimal target by critiquing its own proposals rendered on the screenshot. Given the significant disparity between the model's grounding and critiquing capabilities, we propose a co-evolving Propose-then-Critic framework. To jointly optimize these, we introduce a maturity-aware adaptive co-evolutionary reinforcement learning paradigm. This approach dynamically balances the training objectives of proposer and critic, where the diversity of the proposer's outputs enhances critic robustness, while the critic's maturing discrimination capability conversely unlocks the proposer's potential for extensive spatial exploration, fostering the mutual reinforcement and co-evolution of both capabilities, thereby ensuring generalizability to adapt to diverse and complex interface layouts. Extensive experiments over 6 benchmarks show that our method significantly enhances both grounding accuracy and critic reliability.
匹配关键词: self-consistency
---

[ACADEMIC - ARXIV]
标题: Context Unrolling in Omni Models
作者: Ceyuan Yang, Zhijie Lin, Yang Zhao, Fei Xiao, Hao He, Qi Zhao, Chaorui Deng, Kunchang Li, Zihan Ding, Yuwei Guo, Fuyun Wang, Fangqi Zhu, Xiaonan Nie, Shenhan Zhu, Shanchuan Lin, Hongsheng Li, Weilin Huang, Guang Shi, Haoqi Fan
链接: https://arxiv.org/abs/2604.21921v1
完整摘要: We present Omni, a unified multimodal model natively trained on diverse modalities, including text, images, videos, 3D geometry, and hidden representations. We find that such training enables Context Unrolling, where the model explicitly reasons across multiple modal representations before producing predictions. This process enables the model to aggregate complementary information across heterogeneous modalities, facilitating a more faithful approximation of the shared multimodal knowledge manifold and improving downstream reasoning fidelity. As a result, Omni achieves strong performance on both multimodal generation and understanding benchmarks, while demonstrating advanced multimodal reasoning capabilities, including in-context generation of text, image, video, and 3D geometry.
匹配关键词: process reward
---

[ACADEMIC - ARXIV]
标题: Low-Rank Adaptation Redux for Large Models
作者: Bingcong Li, Yilang Zhang, Georgios B. Giannakis
链接: https://arxiv.org/abs/2604.21905v1
完整摘要: Low-rank adaptation (LoRA) has emerged as the de facto standard for parameter-efficient fine-tuning (PEFT) of foundation models, enabling the adaptation of billion-parameter networks with minimal computational and memory overhead. Despite its empirical success and rapid proliferation of variants, it remains elusive which architectural choices, optimization techniques, and deployment constraints should guide practical method selection. This overview revisits LoRA through the lens of signal processing (SP), bridging modern adapter designs with classical low-rank modeling tools and inverse problems, as well as highlighting how SP principles can inform principled advances of fine-tuning approaches. Rather than providing a comprehensive enumeration and empirical comparisons of LoRA variants, emphasis is placed on the technical mechanisms underpinning these approaches to justify their effectiveness. These advances are categorized into three complementary axes: architectural design, efficient optimization, and pertinent applications. The first axis builds on singular value decomposition (SVD)-based factorization, rank-augmentation constructions, and cross-layer tensorization, while the second axis deals with initialization, alternating solvers, gauge-invariant optimization, and parameterization-aware methods. Beyond fine-tuning, emerging applications of LoRA are accounted across the entire lifecycle of large models, ranging from pre- and post-training to serving/deployment. Finally, open research directions are outlined at the confluence of SP and deep learning to catalyze a bidirectional frontier: classical SP tools provide a principled vocabulary for designing principled PEFT methods, while the unique challenges facing modern deep learning, especially the overwhelming scale and prohibitive overhead, also offer new research lines benefiting the SP community in return.
匹配关键词: process reward
---

[ACADEMIC - ARXIV]
标题: A Multi-Stage Warm-Start Deep Learning Framework for Unit Commitment
作者: Muhy Eddin Za'ter, Anna Van Boven, Bri-Mathias Hodge, Kyri Baker
链接: https://arxiv.org/abs/2604.21891v1
完整摘要: Maintaining instantaneous balance between electricity supply and demand is critical for reliability and grid instability. System operators achieve this through solving the task of Unit Commitment (UC),ca high dimensional large-scale Mixed-integer Linear Programming (MILP) problem that is strictly and heavily governed by the grid physical constraints. As grid integrate variable renewable sources, and new technologies such as long duration storage in the grid, UC must be optimally solved for multi-day horizons and potentially with greater frequency. Therefore, traditional MILP solvers increasingly struggle to compute solutions within these tightening operational time limits. To bypass these computational bottlenecks, this paper proposes a novel framework utilizing a transformer-based architecture to predict generator commitment schedules over a 72-hour horizon. Also, because raw predictions in highly dimensional spaces often yield physically infeasible results, the pipeline integrates the self-attention network with deterministic post-processing heuristics that systematically enforce minimum up/down times and minimize excess capacity. Finally, these refined predictions are utilized as a warm start for a downstream MILP solver, while employing a confidence-based variable fixation strategy to drastically reduce the combinatorial search space. Validated on a single-bus test system, the complete multi-stage pipeline achieves 100\% feasibility and significantly accelerates computation times. Notably, in approximately 20\% of test instances, the proposed model reached a feasible operational schedule with a lower overall system cost than relying solely on the solver.
匹配关键词: process reward
---

[ACADEMIC - ARXIV]
标题: Machine Behavior in Relational Moral Dilemmas: Moral Rightness, Predicted Human Behavior, and Model Decisions
作者: Jiseon Kim, Jea Kwon, Luiz Felipe Vecchietti, Wenchao Dong, Jaehong Kim, Meeyoung Cha
链接: https://arxiv.org/abs/2604.21871v1
完整摘要: Human moral judgment is context-dependent and modulated by interpersonal relationships. As large language models (LLMs) increasingly function as decision-support systems, determining whether they encode these social nuances is critical. We characterize machine behavior using the Whistleblower's Dilemma by varying two experimental dimensions: crime severity and relational closeness. Our study evaluates three distinct perspectives: (1) moral rightness (prescriptive norms), (2) predicted human behavior (descriptive social expectations), and (3) autonomous model decision-making. By analyzing the reasoning processes, we identify a clear cross-perspective divergence: while moral rightness remains consistently fairness-oriented, predicted human behavior shifts significantly toward loyalty as relational closeness increases. Crucially, model decisions align with moral rightness judgments rather than their own behavioral predictions. This inconsistency suggests that LLM decision-making prioritizes rigid, prescriptive rules over the social sensitivity present in their internal world-modeling, which poses a gap that may lead to significant misalignments in real-world deployments.
匹配关键词: process reward
---

[ACADEMIC - ARXIV]
标题: GFlowState: Visualizing the Training of Generative Flow Networks Beyond the Reward
作者: Florian Holeczek, Andreas Hinterreiter, Alex Hernandez-Garcia, Marc Streit, Christina Humer
链接: https://arxiv.org/abs/2604.21830v1
完整摘要: We present GFlowState, a visual analytics system designed to illuminate the training process of Generative Flow Networks (GFlowNets or GFNs). GFlowNets are a probabilistic framework for generating samples proportionally to a reward function. While GFlowNets have proved to be powerful tools in applications such as molecule and material discovery, their training dynamics remain difficult to interpret. Standard machine learning tools allow metric tracking but do not reveal how models explore the sample space, construct sample trajectories, or shift sampling probabilities during training. Our solution, GFlowState, allows users to analyze sampling trajectories, compare the sample space relative to reference datasets, and analyze the training dynamics. To this end, we introduce multiple views, including a chart of candidate rankings, a state projection, a node-link diagram of the trajectory network, and a transition heatmap. These visualizations enable GFlowNet developers and users to investigate sampling behavior and policy evolution, and to identify underexplored regions and sources of training failure. Case studies demonstrate how the system supports debugging and assessing the quality of GFlowNets across application domains. By making the structural dynamics of GFlowNets observable, our work enhances their interpretability and can accelerate GFlowNet development in practice.
匹配关键词: process reward
---

[ACADEMIC - ARXIV]
标题: Revealing Geography-Driven Signals in Zone-Level Claim Frequency Models: An Empirical Study using Environmental and Visual Predictors
作者: Sherly Alfonso-Sánchez, Cristián Bravo, Kristina G. Stankova
链接: https://arxiv.org/abs/2604.21893v1
完整摘要: Geographic context is often consider relevant to motor insurance risk, yet public actuarial datasets provide limited location identifiers, constraining how this information can be incorporated and evaluated in claim-frequency models. This study examines how geographic information from alternative data sources can be incorporated into actuarial models for Motor Third Party Liability (MTPL) claim prediction under such constraints. Using the BeMTPL97 dataset, we adopt a zone-level modeling framework and evaluate predictive performance on unseen postcodes. Geographic information is introduced through two channels: environmental indicators from OpenStreetMap and CORINE Land Cover, and orthoimagery released by the Belgian National Geographic Institute for academic use. We evaluate the predictive contribution of coordinates, environmental features, and image embeddings across three baseline models: generalized linear models (GLMs), regularized GLMs, and gradient-boosted trees, while raw imagery is modeled using convolutional neural networks. Our results show that augmenting actuarial variables with constructed geographic information improves accuracy. Across experiments, both linear and tree-based models benefit most from combining coordinates with environmental features extracted at 5 km scale, while smaller neighborhoods also improve baseline specifications. Generally, image embeddings do not improve performance when environmental features are available; however, when such features are absent, pretrained vision-transformer embeddings enhance accuracy and stability for regularized GLMs. Our results show that the predictive value of geographic information in zone-level MTPL frequency models depends less on model complexity than on how geography is represented, and illustrate that geographic context can be incorporated despite limited individual-level spatial information.
匹配关键词: pretraining
---

[ACADEMIC - ARXIV]
标题: Replay-buffer engineering for noise-robust quantum circuit optimization
作者: Akash Kundu, Sebastian Feld
链接: https://arxiv.org/abs/2604.21863v1
完整摘要: Deep reinforcement learning (RL) for quantum circuit optimization faces three fundamental bottlenecks: replay buffers that ignore the reliability of temporal-difference (TD) targets, curriculum-based architecture search that triggers a full quantum-classical evaluation at every environment step, and the routine discard of noiseless trajectories when retraining under hardware noise. We address all three by treating the replay buffer as a primary algorithmic lever for quantum optimization. We introduce ReaPER$+$, an annealed replay rule that transitions from TD error-driven prioritization early in training to reliability-aware sampling as value estimates mature, achieving $4-32\times$ gains in sample efficiency over fixed PER, ReaPER, and uniform replay while consistently discovering more compact circuits across quantum compilation and QAS benchmarks; validation on LunarLander-v3 confirms the principle is domain-agnostic. Furthermore we eliminate the quantum-classical evaluation bottleneck in curriculum RL by introducing OptCRLQAS which amortizes expensive evaluations over multiple architectural edits, cutting wall-clock time per episode by up to $67.5\%$ on a 12-qubit optimization problem without degrading solution quality. Finally we introduce a lightweight replay-buffer transfer scheme that warm-starts noisy-setting learning by reusing noiseless trajectories, without network-weight transfer or $ε$-greedy pretraining. This reduces steps to chemical accuracy by up to $85-90\%$ and final energy error by up to $90\%$ over from-scratch baselines on 6-, 8-, and 12-qubit molecular tasks. Together, these results establish that experience storage, sampling, and transfer are decisive levers for scalable, noise-robust quantum circuit optimization.
匹配关键词: pretraining
---

[ACADEMIC - ARXIV]
标题: SemEval-2026 Task 4: Narrative Story Similarity and Narrative Representation Learning
作者: Hans Ole Hatzel, Ekaterina Artemova, Haimo Paul Stiemer, Evelyn Gius, Chris Biemann
链接: https://arxiv.org/abs/2604.21782v1
完整摘要: We present the shared task on narrative similarity and narrative representation learning - NSNRL (pronounced "nass-na-rel"). The task operationalizes narrative similarity as a binary classification problem: determining which of two stories is more similar to an anchor story. We introduce a novel definition of narrative similarity, compatible with both narrative theory and intuitive judgment. Based on the similarity judgments collected under this concept, we also evaluate narrative embedding representations. We collected at least two annotations each for more than 1,000 story summary triples, with each annotation being backed by at least two annotators in agreement. This paper describes the sampling and annotation process for the dataset; further, we give an overview of the submitted systems and the techniques they employ. We received a total of 71 final submissions from 46 teams across our two tracks. In our triple-based classification setup, LLM ensembles make up many of the top-scoring systems, while in the embedding setup, systems with pre- and post-processing on pretrained embedding models perform about on par with custom fine-tuned solutions. Our analysis identifies potential headroom for improvement of automated systems in both tracks. The task website includes visualizations of embeddings alongside instance-level classification results for all teams.
匹配关键词: pretraining
---

[ACADEMIC - ARXIV]
标题: Hi-WM: Human-in-the-World-Model for Scalable Robot Post-Training
作者: Yaxuan Li, Zhongyi Zhou, Yefei Chen, Yanjiang Guo, Jiaming Liu, Shanghang Zhang, Jianyu Chen, Yichen Zhu
链接: https://arxiv.org/abs/2604.21741v1
完整摘要: Post-training is essential for turning pretrained generalist robot policies into reliable task-specific controllers, but existing human-in-the-loop pipelines remain tied to physical execution: each correction requires robot time, scene setup, resets, and operator supervision in the real world. Meanwhile, action-conditioned world models have been studied mainly for imagination, synthetic data generation, and policy evaluation. We propose \textbf{Human-in-the-World-Model (Hi-WM)}, a post-training framework that uses a learned world model as a reusable corrective substrate for failure-targeted policy improvement. A policy is first rolled out in closed loop inside the world model; when the rollout becomes incorrect or failure-prone, a human intervenes directly in the model to provide short corrective actions. Hi-WM caches intermediate states and supports rollback and branching, allowing a single failure state to be reused for multiple corrective continuations and yielding dense supervision around behaviors that the base policy handles poorly. The resulting corrective trajectories are then added back to the training set for post-training. We evaluate Hi-WM on three real-world manipulation tasks spanning both rigid and deformable object interaction, and on two policy backbones. Hi-WM improves real-world success by 37.9 points on average over the base policy and by 19.0 points over a world-model closed-loop baseline, while world-model evaluation correlates strongly with real-world performance (r = 0.953). These results suggest that world models can serve not only as generators or evaluators, but also as effective corrective substrates for scalable robot post-training.
匹配关键词: pretraining
---

[ACADEMIC - ARXIV]
标题: Ramen: Robust Test-Time Adaptation of Vision-Language Models with Active Sample Selection
作者: Wenxuan Bao, Yanjun Zhao, Xiyuan Yang, Jingrui He
链接: https://arxiv.org/abs/2604.21728v1
完整摘要: Pretrained vision-language models such as CLIP exhibit strong zero-shot generalization but remain sensitive to distribution shifts. Test-time adaptation adapts models during inference without access to source data or target labels, offering a practical way to handle such shifts. However, existing methods typically assume that test samples come from a single, consistent domain, while in practice, test data often include samples from mixed domains with distinct characteristics. Consequently, their performance degrades under mixed-domain settings. To address this, we present Ramen, a framework for robust test-time adaptation through active sample selection. For each incoming test sample, Ramen retrieves a customized batch of relevant samples from previously seen data based on two criteria: domain consistency, which ensures that adaptation focuses on data from similar domains, and prediction balance, which mitigates adaptation bias caused by skewed predictions. To improve efficiency, Ramen employs an embedding-gradient cache that stores the embeddings and sample-level gradients of past test images. The stored embeddings are used to retrieve relevant samples, and the corresponding gradients are aggregated for model updates, eliminating the need for any additional forward or backward passes. Our theoretical analysis provides insight into why the proposed adaptation mechanism is effective under mixed-domain shifts. Experiments on multiple image corruption and domain-shift benchmarks demonstrate that Ramen achieves strong and consistent performance, offering robust and efficient adaptation in complex mixed-domain scenarios. Our code is available at https://github.com/baowenxuan/Ramen .
匹配关键词: pretraining
---

[ACADEMIC - ARXIV]
标题: Seeing Fast and Slow: Learning the Flow of Time in Videos
作者: Yen-Siang Wu, Rundong Luo, Jingsen Zhu, Tao Tu, Ali Farhadi, Matthew Wallingford, Yu-Chiang Frank Wang, Steve Marschner, Wei-Chiu Ma
链接: https://arxiv.org/abs/2604.21931v1
完整摘要: How can we tell whether a video has been sped up or slowed down? How can we generate videos at different speeds? Although videos have been central to modern computer vision research, little attention has been paid to perceiving and controlling the passage of time. In this paper, we study time as a learnable visual concept and develop models for reasoning about and manipulating the flow of time in videos. We first exploit the multimodal cues and temporal structure naturally present in videos to learn, in a self-supervised manner, to detect speed changes and estimate playback speed. We then show that these learned temporal reasoning models enable us to curate the largest slow-motion video dataset to date from noisy in-the-wild sources. Such slow-motion footage, typically filmed by high-speed cameras, contains substantially richer temporal detail than standard videos. Using this data, we further develop models capable of temporal control, including speed-conditioned video generation, which produces motion at specified playback speed, and temporal super-resolution, which tranforms low-FPS, blurry videos into high-FPS sequences with fine-grained temporal details. Our findings highlight time as a manipulable, perceptual dimension in video learning, opening doors to temporally controllable video generation, temporal forensics detection, and potentially richer world-models that understand how events unfold over time.
匹配关键词: foundation model
---

[ACADEMIC - ARXIV]
标题: Temporal Taskification in Streaming Continual Learning: A Source of Evaluation Instability
作者: Nicolae Filat, Ahmed Hussain, Konstantinos Kalogiannis, Elena Burceanu
链接: https://arxiv.org/abs/2604.21930v1
完整摘要: Streaming Continual Learning (CL) typically converts a continuous stream into a sequence of discrete tasks through temporal partitioning. We argue that this temporal taskification step is not a neutral preprocessing choice, but a structural component of evaluation: different valid splits of the same stream can induce different CL regimes and therefore different benchmark conclusions. To study this effect, we introduce a taskification-level framework based on plasticity and stability profiles, a profile distance between taskifications, and Boundary-Profile Sensitivity (BPS), which diagnoses how strongly small boundary perturbations alter the induced regime before any CL model is trained. We evaluate continual finetuning, Experience Replay, Elastic Weight Consolidation, and Learning without Forgetting on network traffic forecasting with CESNET-Timeseries24, keeping the stream, model, and training budget fixed while varying only the temporal taskification. Across 9-, 30-, and 44-day splits, we observe substantial changes in forecasting error, forgetting, and backward transfer, showing that taskification alone can materially affect CL evaluation. We further find that shorter taskifications induce noisier distribution-level patterns, larger structural distances, and higher BPS, indicating greater sensitivity to boundary perturbations. These results show that benchmark conclusions in streaming CL depend not only on the learner and the data stream, but also on how that stream is taskified, motivating temporal taskification as a first-class evaluation variable.
匹配关键词: foundation model
---

[ACADEMIC - ARXIV]
标题: Evaluation of Automatic Speech Recognition Using Generative Large Language Models
作者: Thibault Bañeras-Roux, Shashi Kumar, Driss Khalil, Sergio Burdisso, Petr Motlicek, Shiran Liu, Mickael Rouvier, Jane Wottawa, Richard Dufour
链接: https://arxiv.org/abs/2604.21928v1
完整摘要: Automatic Speech Recognition (ASR) is traditionally evaluated using Word Error Rate (WER), a metric that is insensitive to meaning. Embedding-based semantic metrics are better correlated with human perception, but decoder-based Large Language Models (LLMs) remain underexplored for this task. This paper evaluates their relevance through three approaches: (1) selecting the best hypothesis between two candidates, (2) computing semantic distance using generative embeddings, and (3) qualitative classification of errors. On the HATS dataset, the best LLMs achieve 92--94\% agreement with human annotators for hypothesis selection, compared to 63\% for WER, also outperforming semantic metrics. Embeddings from decoder-based LLMs show performance comparable to encoder models. Finally, LLMs offer a promising direction for interpretable and semantic ASR evaluation.
匹配关键词: foundation model
---

[ACADEMIC - ARXIV]
标题: Fine-Tuning Regimes Define Distinct Continual Learning Problems
作者: Paul-Tiberiu Iordache, Elena Burceanu
链接: https://arxiv.org/abs/2604.21927v1
完整摘要: Continual learning (CL) studies how models acquire tasks sequentially while retaining previously learned knowledge. Despite substantial progress in benchmarking CL methods, comparative evaluations typically keep the fine-tuning regime fixed. In this paper, we argue that the fine-tuning regime, defined by the trainable parameter subspace, is itself a key evaluation variable. We formalize adaptation regimes as projected optimization over fixed trainable subspaces, showing that changing the trainable depth alters the effective update signal through which both current task fitting and knowledge preservation operate. This analysis motivates the hypothesis that method comparisons need not be invariant across regimes. We test this hypothesis in task incremental CL, five trainable depth regimes, and four standard methods: online EWC, LwF, SI, and GEM. Across five benchmark datasets, namely MNIST, Fashion MNIST, KMNIST, QMNIST, and CIFAR-100, and across 11 task orders per dataset, we find that the relative ranking of methods is not consistently preserved across regimes. We further show that deeper adaptation regimes are associated with larger update magnitudes, higher forgetting, and a stronger relationship between the two. These results show that comparative conclusions in CL can depend strongly on the chosen fine-tuning regime, motivating regime-aware evaluation protocols that treat trainable depth as an explicit experimental factor.
匹配关键词: foundation model
---

[ACADEMIC - ARXIV]
标题: Seeing Without Eyes: 4D Human-Scene Understanding from Wearable IMUs
作者: Hao-Yu Hsu, Tianhang Cheng, Jing Wen, Alexander G. Schwing, Shenlong Wang
链接: https://arxiv.org/abs/2604.21926v1
完整摘要: Understanding human activities and their surrounding environments typically relies on visual perception, yet cameras pose persistent challenges in privacy, safety, energy efficiency, and scalability. We explore an alternative: 4D perception without vision. Its goal is to reconstruct human motion and 3D scene layouts purely from everyday wearable sensors. For this we introduce IMU-to-4D, a framework that repurposes large language models for non-visual spatiotemporal understanding of human-scene dynamics. IMU-to-4D uses data from a few inertial sensors from earbuds, watches, or smartphones and predicts detailed 4D human motion together with coarse scene structure. Experiments across diverse human-scene datasets show that IMU-to-4D yields more coherent and temporally stable results than SoTA cascaded pipelines, suggesting wearable motion sensors alone can support rich 4D understanding.
匹配关键词: foundation model
---

[ACADEMIC - ARXIV]
标题: Long-Horizon Manipulation via Trace-Conditioned VLA Planning
作者: Isabella Liu, An-Chieh Cheng, Rui Yan, Geng Chen, Ri-Zhao Qiu, Xueyan Zou, Sha Yi, Hongxu Yin, Xiaolong Wang, Sifei Liu
链接: https://arxiv.org/abs/2604.21924v1
完整摘要: Long-horizon manipulation remains challenging for vision-language-action (VLA) policies: real tasks are multi-step, progress-dependent, and brittle to compounding execution errors. We present LoHo-Manip, a modular framework that scales short-horizon VLA execution to long-horizon instruction following via a dedicated task-management VLM. The manager is decoupled from the executor and is invoked in a receding-horizon manner: given the current observation, it predicts a progress-aware remaining plan that combines (i) a subtask sequence with an explicit done + remaining split as lightweight language memory, and (ii) a visual trace -- a compact 2D keypoint trajectory prompt specifying where to go and what to approach next. The executor VLA is adapted to condition on the rendered trace, thereby turning long-horizon decision-making into repeated local control by following the trace. Crucially, predicting the remaining plan at each step yields an implicit closed loop: failed steps persist in subsequent outputs, and traces update accordingly, enabling automatic continuation and replanning without hand-crafted recovery logic or brittle visual-history buffers. Extensive experiments spanning embodied planning, long-horizon reasoning, trajectory prediction, and end-to-end manipulation in simulation and on a real Franka robot demonstrate strong gains in long-horizon success, robustness, and out-of-distribution generalization. Project page: https://www.liuisabella.com/LoHoManip
匹配关键词: scaling law
---

[ACADEMIC - ARXIV]
标题: The Sample Complexity of Multicalibration
作者: Natalie Collina, Jiuyao Lu, Georgy Noarov, Aaron Roth
链接: https://arxiv.org/abs/2604.21923v1
完整摘要: We study the minimax sample complexity of multicalibration in the batch setting. A learner observes $n$ i.i.d. samples from an unknown distribution and must output a (possibly randomized) predictor whose population multicalibration error, measured by Expected Calibration Error (ECE), is at most $\varepsilon$ with respect to a given family of groups. For every fixed $κ> 0$, in the regime $|G|\le \varepsilon^{-κ}$, we prove that $\widetildeΘ(\varepsilon^{-3})$ samples are necessary and sufficient, up to polylogarithmic factors. The lower bound holds even for randomized predictors, and the upper bound is realized by a randomized predictor obtained via an online-to-batch reduction. This separates the sample complexity of multicalibration from that of marginal calibration, which scales as $\widetildeΘ(\varepsilon^{-2})$, and shows that mean-ECE multicalibration is as difficult in the batch setting as it is in the online setting, in contrast to marginal calibration which is strictly more difficult in the online setting. In contrast we observe that for $κ= 0$, the sample complexity of multicalibration remains $\widetildeΘ(\varepsilon^{-2})$ exhibiting a sharp threshold phenomenon. More generally, we establish matching upper and lower bounds, up to polylogarithmic factors, for a weighted $L_p$ multicalibration metric for all $1 \le p \le 2$, with optimal exponent $3/p$. We also extend the lower-bound template to a regular class of elicitable properties, and combine it with the online upper bounds of Hu et al. (2025) to obtain matching bounds for calibrating properties including expectiles and bounded-density quantiles.
匹配关键词: scaling law
---

[ACADEMIC - ARXIV]
标题: Low-Rank Adaptation Redux for Large Models
作者: Bingcong Li, Yilang Zhang, Georgios B. Giannakis
链接: https://arxiv.org/abs/2604.21905v1
完整摘要: Low-rank adaptation (LoRA) has emerged as the de facto standard for parameter-efficient fine-tuning (PEFT) of foundation models, enabling the adaptation of billion-parameter networks with minimal computational and memory overhead. Despite its empirical success and rapid proliferation of variants, it remains elusive which architectural choices, optimization techniques, and deployment constraints should guide practical method selection. This overview revisits LoRA through the lens of signal processing (SP), bridging modern adapter designs with classical low-rank modeling tools and inverse problems, as well as highlighting how SP principles can inform principled advances of fine-tuning approaches. Rather than providing a comprehensive enumeration and empirical comparisons of LoRA variants, emphasis is placed on the technical mechanisms underpinning these approaches to justify their effectiveness. These advances are categorized into three complementary axes: architectural design, efficient optimization, and pertinent applications. The first axis builds on singular value decomposition (SVD)-based factorization, rank-augmentation constructions, and cross-layer tensorization, while the second axis deals with initialization, alternating solvers, gauge-invariant optimization, and parameterization-aware methods. Beyond fine-tuning, emerging applications of LoRA are accounted across the entire lifecycle of large models, ranging from pre- and post-training to serving/deployment. Finally, open research directions are outlined at the confluence of SP and deep learning to catalyze a bidirectional frontier: classical SP tools provide a principled vocabulary for designing principled PEFT methods, while the unique challenges facing modern deep learning, especially the overwhelming scale and prohibitive overhead, also offer new research lines benefiting the SP community in return.
匹配关键词: scaling law
---

[ACADEMIC - ARXIV]
标题: A Scale-Adaptive Framework for Joint Spatiotemporal Super-Resolution with Diffusion Models
作者: Max Defez, Filippo Quarenghi, Mathieu Vrac, Stephan Mandt, Tom Beucler
链接: https://arxiv.org/abs/2604.21903v1
完整摘要: Deep-learning video super-resolution has progressed rapidly, but climate applications typically super-resolve (increase resolution) either space or time, and joint spatiotemporal models are often designed for a single pair of super-resolution (SR) factors (upscaling spatial and temporal ratio between the low-resolution sequence and the high-resolution sequence), limiting transfer across spatial resolutions and temporal cadences (frame rates). We present a scale-adaptive framework that reuses the same architecture across factors by decomposing spatiotemporal SR into a deterministic prediction of the conditional mean, with attention, and a residual conditional diffusion model, with an optional mass-conservation (same precipitation amount in inputs and outputs) transform to preserve aggregated totals. Assuming that larger SR factors primarily increase underdetermination (hence required context and residual uncertainty) rather than changing the conditional-mean structure, scale adaptivity is achieved by retuning three factor-dependent hyperparameters before retraining: the diffusion noise schedule amplitude beta (larger for larger factors to increase diversity), the temporal context length L (set to maintain comparable attention horizons across cadences) and optionally a third, the mass-conservation function f (tapered to limit the amplification of extremes for large factors). Demonstrated on reanalysis precipitation over France (Comephore), the same architecture spans super-resolution factors from 1 to 25 in space and 1 to 6 in time, yielding a reusable architecture and tuning recipe for joint spatiotemporal super-resolution across scales.
匹配关键词: scaling law
---

[ACADEMIC - ARXIV]
标题: Mapping the Political Discourse in the Brazilian Chamber of Deputies: A Multi-Faceted Computational Approach
作者: Flávio Soriano, Victoria F. Mello, Pedro B. Rigueira, Gisele L. Pappa, Wagner Meira, Ana Paula Couto da Silva, Jussara M. Almeida
链接: https://arxiv.org/abs/2604.21897v1
完整摘要: Analyses of legislative behavior often rely on voting records, overlooking the rich semantic and rhetorical content of political speech. In this paper, we ask three complementary questions about parliamentary discourse: how things are said, what is being said, and who is speaking in discursively similar ways. To answer these questions, we introduce a scalable and generalizable computational framework that combines diachronic stylometric analysis, contextual topic modeling, and semantic clustering of deputies' speeches. We apply this framework to a large-scale case study of the Brazilian Chamber of Deputies, using a corpus of over 450,000 speeches from 2003 to 2025. Our results show a long-term stylistic shift toward shorter and more direct speeches, a legislative agenda that reorients sharply in response to national crises, and a granular map of discursive alignments in which regional and gender identities often prove more salient than formal party affiliation. More broadly, this work offers a robust methodology for analyzing parliamentary discourse as a multidimensional phenomenon that complements traditional vote-based approaches.
匹配关键词: scaling law
---

[ACADEMIC - ARXIV]
标题: Seeing Fast and Slow: Learning the Flow of Time in Videos
作者: Yen-Siang Wu, Rundong Luo, Jingsen Zhu, Tao Tu, Ali Farhadi, Matthew Wallingford, Yu-Chiang Frank Wang, Steve Marschner, Wei-Chiu Ma
链接: https://arxiv.org/abs/2604.21931v1
完整摘要: How can we tell whether a video has been sped up or slowed down? How can we generate videos at different speeds? Although videos have been central to modern computer vision research, little attention has been paid to perceiving and controlling the passage of time. In this paper, we study time as a learnable visual concept and develop models for reasoning about and manipulating the flow of time in videos. We first exploit the multimodal cues and temporal structure naturally present in videos to learn, in a self-supervised manner, to detect speed changes and estimate playback speed. We then show that these learned temporal reasoning models enable us to curate the largest slow-motion video dataset to date from noisy in-the-wild sources. Such slow-motion footage, typically filmed by high-speed cameras, contains substantially richer temporal detail than standard videos. Using this data, we further develop models capable of temporal control, including speed-conditioned video generation, which produces motion at specified playback speed, and temporal super-resolution, which tranforms low-FPS, blurry videos into high-FPS sequences with fine-grained temporal details. Our findings highlight time as a manipulable, perceptual dimension in video learning, opening doors to temporally controllable video generation, temporal forensics detection, and potentially richer world-models that understand how events unfold over time.
匹配关键词: language model
---

[ACADEMIC - ARXIV]
标题: Temporal Taskification in Streaming Continual Learning: A Source of Evaluation Instability
作者: Nicolae Filat, Ahmed Hussain, Konstantinos Kalogiannis, Elena Burceanu
链接: https://arxiv.org/abs/2604.21930v1
完整摘要: Streaming Continual Learning (CL) typically converts a continuous stream into a sequence of discrete tasks through temporal partitioning. We argue that this temporal taskification step is not a neutral preprocessing choice, but a structural component of evaluation: different valid splits of the same stream can induce different CL regimes and therefore different benchmark conclusions. To study this effect, we introduce a taskification-level framework based on plasticity and stability profiles, a profile distance between taskifications, and Boundary-Profile Sensitivity (BPS), which diagnoses how strongly small boundary perturbations alter the induced regime before any CL model is trained. We evaluate continual finetuning, Experience Replay, Elastic Weight Consolidation, and Learning without Forgetting on network traffic forecasting with CESNET-Timeseries24, keeping the stream, model, and training budget fixed while varying only the temporal taskification. Across 9-, 30-, and 44-day splits, we observe substantial changes in forecasting error, forgetting, and backward transfer, showing that taskification alone can materially affect CL evaluation. We further find that shorter taskifications induce noisier distribution-level patterns, larger structural distances, and higher BPS, indicating greater sensitivity to boundary perturbations. These results show that benchmark conclusions in streaming CL depend not only on the learner and the data stream, but also on how that stream is taskified, motivating temporal taskification as a first-class evaluation variable.
匹配关键词: language model
---

[ACADEMIC - ARXIV]
标题: Evaluation of Automatic Speech Recognition Using Generative Large Language Models
作者: Thibault Bañeras-Roux, Shashi Kumar, Driss Khalil, Sergio Burdisso, Petr Motlicek, Shiran Liu, Mickael Rouvier, Jane Wottawa, Richard Dufour
链接: https://arxiv.org/abs/2604.21928v1
完整摘要: Automatic Speech Recognition (ASR) is traditionally evaluated using Word Error Rate (WER), a metric that is insensitive to meaning. Embedding-based semantic metrics are better correlated with human perception, but decoder-based Large Language Models (LLMs) remain underexplored for this task. This paper evaluates their relevance through three approaches: (1) selecting the best hypothesis between two candidates, (2) computing semantic distance using generative embeddings, and (3) qualitative classification of errors. On the HATS dataset, the best LLMs achieve 92--94\% agreement with human annotators for hypothesis selection, compared to 63\% for WER, also outperforming semantic metrics. Embeddings from decoder-based LLMs show performance comparable to encoder models. Finally, LLMs offer a promising direction for interpretable and semantic ASR evaluation.
匹配关键词: language model
---

[ACADEMIC - ARXIV]
标题: Fine-Tuning Regimes Define Distinct Continual Learning Problems
作者: Paul-Tiberiu Iordache, Elena Burceanu
链接: https://arxiv.org/abs/2604.21927v1
完整摘要: Continual learning (CL) studies how models acquire tasks sequentially while retaining previously learned knowledge. Despite substantial progress in benchmarking CL methods, comparative evaluations typically keep the fine-tuning regime fixed. In this paper, we argue that the fine-tuning regime, defined by the trainable parameter subspace, is itself a key evaluation variable. We formalize adaptation regimes as projected optimization over fixed trainable subspaces, showing that changing the trainable depth alters the effective update signal through which both current task fitting and knowledge preservation operate. This analysis motivates the hypothesis that method comparisons need not be invariant across regimes. We test this hypothesis in task incremental CL, five trainable depth regimes, and four standard methods: online EWC, LwF, SI, and GEM. Across five benchmark datasets, namely MNIST, Fashion MNIST, KMNIST, QMNIST, and CIFAR-100, and across 11 task orders per dataset, we find that the relative ranking of methods is not consistently preserved across regimes. We further show that deeper adaptation regimes are associated with larger update magnitudes, higher forgetting, and a stronger relationship between the two. These results show that comparative conclusions in CL can depend strongly on the chosen fine-tuning regime, motivating regime-aware evaluation protocols that treat trainable depth as an explicit experimental factor.
匹配关键词: language model
---

[ACADEMIC - ARXIV]
标题: Seeing Without Eyes: 4D Human-Scene Understanding from Wearable IMUs
作者: Hao-Yu Hsu, Tianhang Cheng, Jing Wen, Alexander G. Schwing, Shenlong Wang
链接: https://arxiv.org/abs/2604.21926v1
完整摘要: Understanding human activities and their surrounding environments typically relies on visual perception, yet cameras pose persistent challenges in privacy, safety, energy efficiency, and scalability. We explore an alternative: 4D perception without vision. Its goal is to reconstruct human motion and 3D scene layouts purely from everyday wearable sensors. For this we introduce IMU-to-4D, a framework that repurposes large language models for non-visual spatiotemporal understanding of human-scene dynamics. IMU-to-4D uses data from a few inertial sensors from earbuds, watches, or smartphones and predicts detailed 4D human motion together with coarse scene structure. Experiments across diverse human-scene datasets show that IMU-to-4D yields more coherent and temporally stable results than SoTA cascaded pipelines, suggesting wearable motion sensors alone can support rich 4D understanding.
匹配关键词: language model
---

[ACADEMIC - ARXIV]
标题: From Research Question to Scientific Workflow: Leveraging Agentic AI for Science Automation
作者: Bartosz Balis, Michal Orzechowski, Piotr Kica, Michal Dygas, Michal Kuszewski
链接: https://arxiv.org/abs/2604.21910v1
完整摘要: Scientific workflow systems automate execution -- scheduling, fault tolerance, resource management -- but not the semantic translation that precedes it. Scientists still manually convert research questions into workflow specifications, a task requiring both domain knowledge and infrastructure expertise. We propose an agentic architecture that closes this gap through three layers: an LLM interprets natural language into structured intents (semantic layer); validated generators produce reproducible workflow DAGs (deterministic layer); and domain experts author ``Skills'': markdown documents encoding vocabulary mappings, parameter constraints, and optimization strategies (knowledge layer). This decomposition confines LLM non-determinism to intent extraction: identical intents always yield identical workflows. We implement and evaluate the architecture on the 1000 Genomes population genetics workflow and Hyperflow WMS running on Kubernetes. In an ablation study on 150 queries, Skills raise full-match intent accuracy from 44% to 83%; skill-driven deferred workflow generation reduces data transfer by 92\%; and the end-to-end pipeline completes queries on Kubernetes with LLM overhead below 15 seconds and cost under $0.001 per query.
匹配关键词: transformer architecture
---

[ACADEMIC - ARXIV]
标题: Low-Rank Adaptation Redux for Large Models
作者: Bingcong Li, Yilang Zhang, Georgios B. Giannakis
链接: https://arxiv.org/abs/2604.21905v1
完整摘要: Low-rank adaptation (LoRA) has emerged as the de facto standard for parameter-efficient fine-tuning (PEFT) of foundation models, enabling the adaptation of billion-parameter networks with minimal computational and memory overhead. Despite its empirical success and rapid proliferation of variants, it remains elusive which architectural choices, optimization techniques, and deployment constraints should guide practical method selection. This overview revisits LoRA through the lens of signal processing (SP), bridging modern adapter designs with classical low-rank modeling tools and inverse problems, as well as highlighting how SP principles can inform principled advances of fine-tuning approaches. Rather than providing a comprehensive enumeration and empirical comparisons of LoRA variants, emphasis is placed on the technical mechanisms underpinning these approaches to justify their effectiveness. These advances are categorized into three complementary axes: architectural design, efficient optimization, and pertinent applications. The first axis builds on singular value decomposition (SVD)-based factorization, rank-augmentation constructions, and cross-layer tensorization, while the second axis deals with initialization, alternating solvers, gauge-invariant optimization, and parameterization-aware methods. Beyond fine-tuning, emerging applications of LoRA are accounted across the entire lifecycle of large models, ranging from pre- and post-training to serving/deployment. Finally, open research directions are outlined at the confluence of SP and deep learning to catalyze a bidirectional frontier: classical SP tools provide a principled vocabulary for designing principled PEFT methods, while the unique challenges facing modern deep learning, especially the overwhelming scale and prohibitive overhead, also offer new research lines benefiting the SP community in return.
匹配关键词: transformer architecture
---

[ACADEMIC - ARXIV]
标题: UniGenDet: A Unified Generative-Discriminative Framework for Co-Evolutionary Image Generation and Generated Image Detection
作者: Yanran Zhang, Wenzhao Zheng, Yifei Li, Bingyao Yu, Yu Zheng, Lei Chen, Jiwen Lu, Jie Zhou
链接: https://arxiv.org/abs/2604.21904v1
完整摘要: In recent years, significant progress has been made in both image generation and generated image detection. Despite their rapid, yet largely independent, development, these two fields have evolved distinct architectural paradigms: the former predominantly relies on generative networks, while the latter favors discriminative frameworks. A recent trend in both domains is the use of adversarial information to enhance performance, revealing potential for synergy. However, the significant architectural divergence between them presents considerable challenges. Departing from previous approaches, we propose UniGenDet: a Unified generative-discriminative framework for co-evolutionary image Generation and generated image Detection. To bridge the task gap, we design a symbiotic multimodal self-attention mechanism and a unified fine-tuning algorithm. This synergy allows the generation task to improve the interpretability of authenticity identification, while authenticity criteria guide the creation of higher-fidelity images. Furthermore, we introduce a detector-informed generative alignment mechanism to facilitate seamless information exchange. Extensive experiments on multiple datasets demonstrate that our method achieves state-of-the-art performance. Code: \href{https://github.com/Zhangyr2022/UniGenDet}{https://github.com/Zhangyr2022/UniGenDet}.
匹配关键词: transformer architecture
---

[ACADEMIC - ARXIV]
标题: A Scale-Adaptive Framework for Joint Spatiotemporal Super-Resolution with Diffusion Models
作者: Max Defez, Filippo Quarenghi, Mathieu Vrac, Stephan Mandt, Tom Beucler
链接: https://arxiv.org/abs/2604.21903v1
完整摘要: Deep-learning video super-resolution has progressed rapidly, but climate applications typically super-resolve (increase resolution) either space or time, and joint spatiotemporal models are often designed for a single pair of super-resolution (SR) factors (upscaling spatial and temporal ratio between the low-resolution sequence and the high-resolution sequence), limiting transfer across spatial resolutions and temporal cadences (frame rates). We present a scale-adaptive framework that reuses the same architecture across factors by decomposing spatiotemporal SR into a deterministic prediction of the conditional mean, with attention, and a residual conditional diffusion model, with an optional mass-conservation (same precipitation amount in inputs and outputs) transform to preserve aggregated totals. Assuming that larger SR factors primarily increase underdetermination (hence required context and residual uncertainty) rather than changing the conditional-mean structure, scale adaptivity is achieved by retuning three factor-dependent hyperparameters before retraining: the diffusion noise schedule amplitude beta (larger for larger factors to increase diversity), the temporal context length L (set to maintain comparable attention horizons across cadences) and optionally a third, the mass-conservation function f (tapered to limit the amplification of extremes for large factors). Demonstrated on reanalysis precipitation over France (Comephore), the same architecture spans super-resolution factors from 1 to 25 in space and 1 to 6 in time, yielding a reusable architecture and tuning recipe for joint spatiotemporal super-resolution across scales.
匹配关键词: transformer architecture
---

[ACADEMIC - ARXIV]
标题: Revealing Geography-Driven Signals in Zone-Level Claim Frequency Models: An Empirical Study using Environmental and Visual Predictors
作者: Sherly Alfonso-Sánchez, Cristián Bravo, Kristina G. Stankova
链接: https://arxiv.org/abs/2604.21893v1
完整摘要: Geographic context is often consider relevant to motor insurance risk, yet public actuarial datasets provide limited location identifiers, constraining how this information can be incorporated and evaluated in claim-frequency models. This study examines how geographic information from alternative data sources can be incorporated into actuarial models for Motor Third Party Liability (MTPL) claim prediction under such constraints. Using the BeMTPL97 dataset, we adopt a zone-level modeling framework and evaluate predictive performance on unseen postcodes. Geographic information is introduced through two channels: environmental indicators from OpenStreetMap and CORINE Land Cover, and orthoimagery released by the Belgian National Geographic Institute for academic use. We evaluate the predictive contribution of coordinates, environmental features, and image embeddings across three baseline models: generalized linear models (GLMs), regularized GLMs, and gradient-boosted trees, while raw imagery is modeled using convolutional neural networks. Our results show that augmenting actuarial variables with constructed geographic information improves accuracy. Across experiments, both linear and tree-based models benefit most from combining coordinates with environmental features extracted at 5 km scale, while smaller neighborhoods also improve baseline specifications. Generally, image embeddings do not improve performance when environmental features are available; however, when such features are absent, pretrained vision-transformer embeddings enhance accuracy and stability for regularized GLMs. Our results show that the predictive value of geographic information in zone-level MTPL frequency models depends less on model complexity than on how geography is represented, and illustrate that geographic context can be incorporated despite limited individual-level spatial information.
匹配关键词: transformer architecture
---

[ACADEMIC - ARXIV]
标题: From Research Question to Scientific Workflow: Leveraging Agentic AI for Science Automation
作者: Bartosz Balis, Michal Orzechowski, Piotr Kica, Michal Dygas, Michal Kuszewski
链接: https://arxiv.org/abs/2604.21910v1
完整摘要: Scientific workflow systems automate execution -- scheduling, fault tolerance, resource management -- but not the semantic translation that precedes it. Scientists still manually convert research questions into workflow specifications, a task requiring both domain knowledge and infrastructure expertise. We propose an agentic architecture that closes this gap through three layers: an LLM interprets natural language into structured intents (semantic layer); validated generators produce reproducible workflow DAGs (deterministic layer); and domain experts author ``Skills'': markdown documents encoding vocabulary mappings, parameter constraints, and optimization strategies (knowledge layer). This decomposition confines LLM non-determinism to intent extraction: identical intents always yield identical workflows. We implement and evaluate the architecture on the 1000 Genomes population genetics workflow and Hyperflow WMS running on Kubernetes. In an ablation study on 150 queries, Skills raise full-match intent accuracy from 44% to 83%; skill-driven deferred workflow generation reduces data transfer by 92\%; and the end-to-end pipeline completes queries on Kubernetes with LLM overhead below 15 seconds and cost under $0.001 per query.
匹配关键词: mixture of experts
---

[ACADEMIC - ARXIV]
标题: Inferring High-Level Events from Timestamped Data: Complexity and Medical Applications
作者: Yvon K. Awuklu, Meghyn Bienvenu, Katsumi Inoue, Vianney Jouhet, Fleur Mougin
链接: https://arxiv.org/abs/2604.21793v1
完整摘要: In this paper, we develop a novel logic-based approach to detecting high-level temporally extended events from timestamped data and background knowledge. Our framework employs logical rules to capture existence and termination conditions for simple temporal events and to combine these into meta-events. In the medical domain, for example, disease episodes and therapies are inferred from timestamped clinical observations, such as diagnoses and drug administrations stored in patient records, and can be further combined into higher-level disease events. As some incorrect events might be inferred, we use constraints to identify incompatible combinations of events and propose a repair mechanism to select preferred consistent sets of events. While reasoning in the full framework is intractable, we identify relevant restrictions that ensure polynomial-time data complexity. Our prototype system implements core components of the approach using answer set programming. An evaluation on a lung cancer use case supports the interest of the approach, both in terms of computational feasibility and positive alignment of our results with medical expert opinions. While strongly motivated by the needs of the healthcare domain, our framework is purposely generic, enabling its reuse in other areas.
匹配关键词: mixture of experts
---

[ACADEMIC - ARXIV]
标题: From Codebooks to VLMs: Evaluating Automated Visual Discourse Analysis for Climate Change on Social Media
作者: Katharina Prasse, Steffen Jung, Isaac Bravo, Stefanie Walter, Patrick Knab, Christian Bartelt, Margret Keuper
链接: https://arxiv.org/abs/2604.21786v1
完整摘要: Social media platforms have become primary arenas for climate communication, generating millions of images and posts that - if systematically analysed - can reveal which communication strategies mobilise public concern and which fall flat. We aim to facilitate such research by analysing how computer vision methods can be used for social media discourse analysis. This analysis includes application-based taxonomy design, model selection, prompt engineering, and validation. We benchmark six promptable vision-language models and 15 zero-shot CLIP-like models on two datasets from X (formerly Twitter) - a 1,038-image expert-annotated set and a larger corpus of over 1.2 million images, with 50,000 labels manually validated - spanning five annotation dimensions: animal content, climate change consequences, climate action, image setting, and image type. Among the models benchmarked, Gemini-3.1-flash-lite outperforms all others across all super-categories and both datasets, while the gap to open-weight models of moderate size remains relatively small. Beyond instance-level metrics, we advocate for distributional evaluation: VLM predictions can reliably recover population level trends even when per-image accuracy is moderate, making them a viable starting point for discourse analysis at scale. We find that chain-of-thought reasoning reduces rather than improves performance, and that annotation dimension specific prompt design improves performance. We release tweet IDs and labels along with our code at https://github.com/KathPra/Codebooks2VLMs.git.
匹配关键词: mixture of experts
---

[ACADEMIC - ARXIV]
标题: Agentic AI-assisted coding offers a unique opportunity to instill epistemic grounding during software development
作者: Magnus Palmblad, Jared M. Ragland, Benjamin A. Neely
链接: https://arxiv.org/abs/2604.21744v1
完整摘要: The capabilities of AI-assisted coding are progressing at breakneck speed. Chat-based vibe coding has evolved into fully fledged AI-assisted, agentic software development using agent scaffolds where the human developer creates a plan that agentic AIs implement. One current trend is utilizing documents beyond this plan document, such as project and method-scoped documents. Here we propose GROUNDING$.$md, a community-governed, field-scoped epistemic grounding document, using mass spectrometry-based proteomics as an example. This explicit field-scoped grounding document encodes Hard Constraints (non-negotiable validity invariants empirically required for scientific correctness) and Convention Parameters (community-agreed defaults) that override all other contexts to enforce validity, regardless of what the user prompts. In practice, this will empower a non-domain expert to generate code, tools, and software that have best practices baked in at the ground level, providing confidence to the software developer but also to those reviewing or using the final product. Undoubtedly it is easier to have agentic AIs adhere to guidelines than humans, and this opportunity allows for organizations to develop epistemic grounding documents in such a way as to keep domain experts in the loop in a future of democratized generation of bespoke software solutions.
匹配关键词: mixture of experts
---

[ACADEMIC - ARXIV]
标题: Separable Expert Architecture: Toward Privacy-Preserving LLM Personalization via Composable Adapters and Deletable User Proxies
作者: Chris Schneider, Philipp Schoenegger, Ben Bariach
链接: https://arxiv.org/abs/2604.21571v1
完整摘要: Current model training approaches incorporate user information directly into shared weights, making individual data removal computationally infeasible without retraining. This paper presents a three-layer architecture that decouples personal data from shared weights by combining a static base model, composable domain-expert LoRA adapters that shape behavior without imparting user data, and per-user proxy artefacts whose deletion constitutes deterministic unlearning. Evaluation on Phi-3.5-mini and Llama-3.1-8B confirms per-user differentiation in which personal data influences outputs while remaining isolated, verified by a return to baseline after proxy removal (KL divergence of approximately 0.21 nats, 82-89% verification pass rate) and near-zero cross-user contamination. Because user-specific information never enters shared weights, the architecture mitigates model inversion, membership inference, and training-data extraction against shared model components by construction. The approach converts machine unlearning from an intractable weight-editing problem into a deterministic deletion operation that preserves personalization alongside privacy-enhancing guarantees and is compatible with differentially private stochastic gradient descent (DP-SGD) for privacy-preserving shared model improvement.
匹配关键词: mixture of experts
---

[ACADEMIC - ARXIV]
标题: Seeing Fast and Slow: Learning the Flow of Time in Videos
作者: Yen-Siang Wu, Rundong Luo, Jingsen Zhu, Tao Tu, Ali Farhadi, Matthew Wallingford, Yu-Chiang Frank Wang, Steve Marschner, Wei-Chiu Ma
链接: https://arxiv.org/abs/2604.21931v1
完整摘要: How can we tell whether a video has been sped up or slowed down? How can we generate videos at different speeds? Although videos have been central to modern computer vision research, little attention has been paid to perceiving and controlling the passage of time. In this paper, we study time as a learnable visual concept and develop models for reasoning about and manipulating the flow of time in videos. We first exploit the multimodal cues and temporal structure naturally present in videos to learn, in a self-supervised manner, to detect speed changes and estimate playback speed. We then show that these learned temporal reasoning models enable us to curate the largest slow-motion video dataset to date from noisy in-the-wild sources. Such slow-motion footage, typically filmed by high-speed cameras, contains substantially richer temporal detail than standard videos. Using this data, we further develop models capable of temporal control, including speed-conditioned video generation, which produces motion at specified playback speed, and temporal super-resolution, which tranforms low-FPS, blurry videos into high-FPS sequences with fine-grained temporal details. Our findings highlight time as a manipulable, perceptual dimension in video learning, opening doors to temporally controllable video generation, temporal forensics detection, and potentially richer world-models that understand how events unfold over time.
匹配关键词: multimodal
---

[ACADEMIC - ARXIV]
标题: Context Unrolling in Omni Models
作者: Ceyuan Yang, Zhijie Lin, Yang Zhao, Fei Xiao, Hao He, Qi Zhao, Chaorui Deng, Kunchang Li, Zihan Ding, Yuwei Guo, Fuyun Wang, Fangqi Zhu, Xiaonan Nie, Shenhan Zhu, Shanchuan Lin, Hongsheng Li, Weilin Huang, Guang Shi, Haoqi Fan
链接: https://arxiv.org/abs/2604.21921v1
完整摘要: We present Omni, a unified multimodal model natively trained on diverse modalities, including text, images, videos, 3D geometry, and hidden representations. We find that such training enables Context Unrolling, where the model explicitly reasons across multiple modal representations before producing predictions. This process enables the model to aggregate complementary information across heterogeneous modalities, facilitating a more faithful approximation of the shared multimodal knowledge manifold and improving downstream reasoning fidelity. As a result, Omni achieves strong performance on both multimodal generation and understanding benchmarks, while demonstrating advanced multimodal reasoning capabilities, including in-context generation of text, image, video, and 3D geometry.
匹配关键词: multimodal
---

[ACADEMIC - ARXIV]
标题: UniGenDet: A Unified Generative-Discriminative Framework for Co-Evolutionary Image Generation and Generated Image Detection
作者: Yanran Zhang, Wenzhao Zheng, Yifei Li, Bingyao Yu, Yu Zheng, Lei Chen, Jiwen Lu, Jie Zhou
链接: https://arxiv.org/abs/2604.21904v1
完整摘要: In recent years, significant progress has been made in both image generation and generated image detection. Despite their rapid, yet largely independent, development, these two fields have evolved distinct architectural paradigms: the former predominantly relies on generative networks, while the latter favors discriminative frameworks. A recent trend in both domains is the use of adversarial information to enhance performance, revealing potential for synergy. However, the significant architectural divergence between them presents considerable challenges. Departing from previous approaches, we propose UniGenDet: a Unified generative-discriminative framework for co-evolutionary image Generation and generated image Detection. To bridge the task gap, we design a symbiotic multimodal self-attention mechanism and a unified fine-tuning algorithm. This synergy allows the generation task to improve the interpretability of authenticity identification, while authenticity criteria guide the creation of higher-fidelity images. Furthermore, we introduce a detector-informed generative alignment mechanism to facilitate seamless information exchange. Extensive experiments on multiple datasets demonstrate that our method achieves state-of-the-art performance. Code: \href{https://github.com/Zhangyr2022/UniGenDet}{https://github.com/Zhangyr2022/UniGenDet}.
匹配关键词: multimodal
---

[ACADEMIC - ARXIV]
标题: A Multimodal Text- and Graph-Based Approach for Open-Domain Event Extraction from Documents
作者: Praval Sharma
链接: https://arxiv.org/abs/2604.21885v1
完整摘要: Event extraction is essential for event understanding and analysis. It supports tasks such as document summarization and decision-making in emergency scenarios. However, existing event extraction approaches have limitations: (1) closed-domain algorithms are restricted to predefined event types and thus rarely generalize to unseen types and (2) open-domain event extraction algorithms, capable of handling unconstrained event types, have largely overlooked the potential of large language models (LLMs) despite their advanced abilities. Additionally, they do not explicitly model document-level contextual, structural, and semantic reasoning, which are crucial for effective event extraction but remain challenging for LLMs due to lost-in-the-middle phenomenon and attention dilution. To address these limitations, we propose multimodal open-domain event extraction, MODEE , a novel approach for open-domain event extraction that combines graph-based learning with text-based representation from LLMs to model document-level reasoning. Empirical evaluations on large datasets demonstrate that MODEE outperforms state-of-the-art open-domain event extraction approaches and can be generalized to closed-domain event extraction, where it outperforms existing algorithms.
匹配关键词: multimodal
---

[ACADEMIC - ARXIV]
标题: TEMA: Anchor the Image, Follow the Text for Multi-Modification Composed Image Retrieval
作者: Zixu Li, Yupeng Hu, Zhiheng Fu, Zhiwei Chen, Yongqi Li, Liqiang Nie
链接: https://arxiv.org/abs/2604.21806v1
完整摘要: Composed Image Retrieval (CIR) is an important image retrieval paradigm that enables users to retrieve a target image using a multimodal query that consists of a reference image and modification text. Although research on CIR has made significant progress, prevailing setups still rely simple modification texts that typically cover only a limited range of salient changes, which induces two limitations highly relevant to practical applications, namely Insufficient Entity Coverage and Clause-Entity Misalignment. In order to address these issues and bring CIR closer to real-world use, we construct two instruction-rich multi-modification datasets, M-FashionIQ and M-CIRR. In addition, we propose TEMA, the Text-oriented Entity Mapping Architecture, which is the first CIR framework designed for multi-modification while also accommodating simple modifications. Extensive experiments on four benchmark datasets demonstrate that TEMA's superiority in both original and multi-modification scenarios, while maintaining an optimal balance between retrieval accuracy and computational efficiency. Our codes and constructed multi-modification dataset (M-FashionIQ and M-CIRR) are available at https://github.com/lee-zixu/ACL26-TEMA/.
匹配关键词: multimodal
---

[ACADEMIC - ARXIV]
标题: Seeing Fast and Slow: Learning the Flow of Time in Videos
作者: Yen-Siang Wu, Rundong Luo, Jingsen Zhu, Tao Tu, Ali Farhadi, Matthew Wallingford, Yu-Chiang Frank Wang, Steve Marschner, Wei-Chiu Ma
链接: https://arxiv.org/abs/2604.21931v1
完整摘要: How can we tell whether a video has been sped up or slowed down? How can we generate videos at different speeds? Although videos have been central to modern computer vision research, little attention has been paid to perceiving and controlling the passage of time. In this paper, we study time as a learnable visual concept and develop models for reasoning about and manipulating the flow of time in videos. We first exploit the multimodal cues and temporal structure naturally present in videos to learn, in a self-supervised manner, to detect speed changes and estimate playback speed. We then show that these learned temporal reasoning models enable us to curate the largest slow-motion video dataset to date from noisy in-the-wild sources. Such slow-motion footage, typically filmed by high-speed cameras, contains substantially richer temporal detail than standard videos. Using this data, we further develop models capable of temporal control, including speed-conditioned video generation, which produces motion at specified playback speed, and temporal super-resolution, which tranforms low-FPS, blurry videos into high-FPS sequences with fine-grained temporal details. Our findings highlight time as a manipulable, perceptual dimension in video learning, opening doors to temporally controllable video generation, temporal forensics detection, and potentially richer world-models that understand how events unfold over time.
匹配关键词: vision language model
---

[ACADEMIC - ARXIV]
标题: Temporal Taskification in Streaming Continual Learning: A Source of Evaluation Instability
作者: Nicolae Filat, Ahmed Hussain, Konstantinos Kalogiannis, Elena Burceanu
链接: https://arxiv.org/abs/2604.21930v1
完整摘要: Streaming Continual Learning (CL) typically converts a continuous stream into a sequence of discrete tasks through temporal partitioning. We argue that this temporal taskification step is not a neutral preprocessing choice, but a structural component of evaluation: different valid splits of the same stream can induce different CL regimes and therefore different benchmark conclusions. To study this effect, we introduce a taskification-level framework based on plasticity and stability profiles, a profile distance between taskifications, and Boundary-Profile Sensitivity (BPS), which diagnoses how strongly small boundary perturbations alter the induced regime before any CL model is trained. We evaluate continual finetuning, Experience Replay, Elastic Weight Consolidation, and Learning without Forgetting on network traffic forecasting with CESNET-Timeseries24, keeping the stream, model, and training budget fixed while varying only the temporal taskification. Across 9-, 30-, and 44-day splits, we observe substantial changes in forecasting error, forgetting, and backward transfer, showing that taskification alone can materially affect CL evaluation. We further find that shorter taskifications induce noisier distribution-level patterns, larger structural distances, and higher BPS, indicating greater sensitivity to boundary perturbations. These results show that benchmark conclusions in streaming CL depend not only on the learner and the data stream, but also on how that stream is taskified, motivating temporal taskification as a first-class evaluation variable.
匹配关键词: vision language model
---

[ACADEMIC - ARXIV]
标题: Evaluation of Automatic Speech Recognition Using Generative Large Language Models
作者: Thibault Bañeras-Roux, Shashi Kumar, Driss Khalil, Sergio Burdisso, Petr Motlicek, Shiran Liu, Mickael Rouvier, Jane Wottawa, Richard Dufour
链接: https://arxiv.org/abs/2604.21928v1
完整摘要: Automatic Speech Recognition (ASR) is traditionally evaluated using Word Error Rate (WER), a metric that is insensitive to meaning. Embedding-based semantic metrics are better correlated with human perception, but decoder-based Large Language Models (LLMs) remain underexplored for this task. This paper evaluates their relevance through three approaches: (1) selecting the best hypothesis between two candidates, (2) computing semantic distance using generative embeddings, and (3) qualitative classification of errors. On the HATS dataset, the best LLMs achieve 92--94\% agreement with human annotators for hypothesis selection, compared to 63\% for WER, also outperforming semantic metrics. Embeddings from decoder-based LLMs show performance comparable to encoder models. Finally, LLMs offer a promising direction for interpretable and semantic ASR evaluation.
匹配关键词: vision language model
---

[ACADEMIC - ARXIV]
标题: Fine-Tuning Regimes Define Distinct Continual Learning Problems
作者: Paul-Tiberiu Iordache, Elena Burceanu
链接: https://arxiv.org/abs/2604.21927v1
完整摘要: Continual learning (CL) studies how models acquire tasks sequentially while retaining previously learned knowledge. Despite substantial progress in benchmarking CL methods, comparative evaluations typically keep the fine-tuning regime fixed. In this paper, we argue that the fine-tuning regime, defined by the trainable parameter subspace, is itself a key evaluation variable. We formalize adaptation regimes as projected optimization over fixed trainable subspaces, showing that changing the trainable depth alters the effective update signal through which both current task fitting and knowledge preservation operate. This analysis motivates the hypothesis that method comparisons need not be invariant across regimes. We test this hypothesis in task incremental CL, five trainable depth regimes, and four standard methods: online EWC, LwF, SI, and GEM. Across five benchmark datasets, namely MNIST, Fashion MNIST, KMNIST, QMNIST, and CIFAR-100, and across 11 task orders per dataset, we find that the relative ranking of methods is not consistently preserved across regimes. We further show that deeper adaptation regimes are associated with larger update magnitudes, higher forgetting, and a stronger relationship between the two. These results show that comparative conclusions in CL can depend strongly on the chosen fine-tuning regime, motivating regime-aware evaluation protocols that treat trainable depth as an explicit experimental factor.
匹配关键词: vision language model
---

[ACADEMIC - ARXIV]
标题: Seeing Without Eyes: 4D Human-Scene Understanding from Wearable IMUs
作者: Hao-Yu Hsu, Tianhang Cheng, Jing Wen, Alexander G. Schwing, Shenlong Wang
链接: https://arxiv.org/abs/2604.21926v1
完整摘要: Understanding human activities and their surrounding environments typically relies on visual perception, yet cameras pose persistent challenges in privacy, safety, energy efficiency, and scalability. We explore an alternative: 4D perception without vision. Its goal is to reconstruct human motion and 3D scene layouts purely from everyday wearable sensors. For this we introduce IMU-to-4D, a framework that repurposes large language models for non-visual spatiotemporal understanding of human-scene dynamics. IMU-to-4D uses data from a few inertial sensors from earbuds, watches, or smartphones and predicts detailed 4D human motion together with coarse scene structure. Experiments across diverse human-scene datasets show that IMU-to-4D yields more coherent and temporally stable results than SoTA cascaded pipelines, suggesting wearable motion sensors alone can support rich 4D understanding.
匹配关键词: vision language model
---

[ACADEMIC - ARXIV]
标题: Long-Horizon Manipulation via Trace-Conditioned VLA Planning
作者: Isabella Liu, An-Chieh Cheng, Rui Yan, Geng Chen, Ri-Zhao Qiu, Xueyan Zou, Sha Yi, Hongxu Yin, Xiaolong Wang, Sifei Liu
链接: https://arxiv.org/abs/2604.21924v1
完整摘要: Long-horizon manipulation remains challenging for vision-language-action (VLA) policies: real tasks are multi-step, progress-dependent, and brittle to compounding execution errors. We present LoHo-Manip, a modular framework that scales short-horizon VLA execution to long-horizon instruction following via a dedicated task-management VLM. The manager is decoupled from the executor and is invoked in a receding-horizon manner: given the current observation, it predicts a progress-aware remaining plan that combines (i) a subtask sequence with an explicit done + remaining split as lightweight language memory, and (ii) a visual trace -- a compact 2D keypoint trajectory prompt specifying where to go and what to approach next. The executor VLA is adapted to condition on the rendered trace, thereby turning long-horizon decision-making into repeated local control by following the trace. Crucially, predicting the remaining plan at each step yields an implicit closed loop: failed steps persist in subsequent outputs, and traces update accordingly, enabling automatic continuation and replanning without hand-crafted recovery logic or brittle visual-history buffers. Extensive experiments spanning embodied planning, long-horizon reasoning, trajectory prediction, and end-to-end manipulation in simulation and on a real Franka robot demonstrate strong gains in long-horizon success, robustness, and out-of-distribution generalization. Project page: https://www.liuisabella.com/LoHoManip
匹配关键词: VLM
---

[ACADEMIC - ARXIV]
标题: From Codebooks to VLMs: Evaluating Automated Visual Discourse Analysis for Climate Change on Social Media
作者: Katharina Prasse, Steffen Jung, Isaac Bravo, Stefanie Walter, Patrick Knab, Christian Bartelt, Margret Keuper
链接: https://arxiv.org/abs/2604.21786v1
完整摘要: Social media platforms have become primary arenas for climate communication, generating millions of images and posts that - if systematically analysed - can reveal which communication strategies mobilise public concern and which fall flat. We aim to facilitate such research by analysing how computer vision methods can be used for social media discourse analysis. This analysis includes application-based taxonomy design, model selection, prompt engineering, and validation. We benchmark six promptable vision-language models and 15 zero-shot CLIP-like models on two datasets from X (formerly Twitter) - a 1,038-image expert-annotated set and a larger corpus of over 1.2 million images, with 50,000 labels manually validated - spanning five annotation dimensions: animal content, climate change consequences, climate action, image setting, and image type. Among the models benchmarked, Gemini-3.1-flash-lite outperforms all others across all super-categories and both datasets, while the gap to open-weight models of moderate size remains relatively small. Beyond instance-level metrics, we advocate for distributional evaluation: VLM predictions can reliably recover population level trends even when per-image accuracy is moderate, making them a viable starting point for discourse analysis at scale. We find that chain-of-thought reasoning reduces rather than improves performance, and that annotation dimension specific prompt design improves performance. We release tweet IDs and labels along with our code at https://github.com/KathPra/Codebooks2VLMs.git.
匹配关键词: VLM
---

[ACADEMIC - ARXIV]
标题: WorldMark: A Unified Benchmark Suite for Interactive Video World Models
作者: Xiaojie Xu, Zhengyuan Lin, Kang He, Yukang Feng, Xiaofeng Mao, Yuanyang Yin, Kaipeng Zhang, Yongtao Ge
链接: https://arxiv.org/abs/2604.21686v1
完整摘要: Interactive video generation models such as Genie, YUME, HY-World, and Matrix-Game are advancing rapidly, yet every model is evaluated on its own benchmark with private scenes and trajectories, making fair cross-model comparison impossible. Existing public benchmarks offer useful metrics such as trajectory error, aesthetic scores, and VLM-based judgments, but none supplies the standardized test conditions -- identical scenes, identical action sequences, and a unified control interface -- needed to make those metrics comparable across models with heterogeneous inputs. We introduce WorldMark, the first benchmark that provides such a common playing field for interactive Image-to-Video world models. WorldMark contributes: (1) a unified action-mapping layer that translates a shared WASD-style action vocabulary into each model's native control format, enabling apples-to-apples comparison across six major models on identical scenes and trajectories; (2) a hierarchical test suite of 500 evaluation cases covering first- and third-person viewpoints, photorealistic and stylized scenes, and three difficulty tiers from Easy to Hard spanning 20-60s; and (3) a modular evaluation toolkit for Visual Quality, Control Alignment, and World Consistency, designed so that researchers can reuse our standardized inputs while plugging in their own metrics as the field evolves. We will release all data, evaluation code, and model outputs to facilitate future research. Beyond offline metrics, we launch World Model Arena (warena.ai), an online platform where anyone can pit leading world models against each other in side-by-side battles and watch the live leaderboard.
匹配关键词: VLM
---

[ACADEMIC - ARXIV]
标题: Seeing Isn't Believing: Uncovering Blind Spots in Evaluator Vision-Language Models
作者: Mohammed Safi Ur Rahman Khan, Sanjay Suryanarayanan, Tushar Anand, Mitesh M. Khapra
链接: https://arxiv.org/abs/2604.21523v1
完整摘要: Large Vision-Language Models (VLMs) are increasingly used to evaluate outputs of other models, for image-to-text (I2T) tasks such as visual question answering, and text-to-image (T2I) generation tasks. Despite this growing reliance, the reliability of these Evaluator VLMs remains under explored. In this work, we systematically evaluate the reliability of Evaluator VLMs across both I2T and T2I tasks. We introduce targeted perturbations that degrade output quality along key error dimensions, including object hallucinations, spatial reasoning, factual grounding, and visual fidelity. These perturbations test whether Evaluator VLMs can reliably account for these quality degrading errors in their evaluations. Using a comprehensive benchmark of over 4000 perturbed instances spanning 40 perturbation dimensions, we evaluate 4 prominent VLMs using single-answer scoring, pairwise comparison, and reference-guided paradigms. Our findings reveal that current VLM evaluators exhibit substantial blind spots: they often fail to detect perturbed outputs - in some cases exceeding 50%, struggle particularly with fine-grained compositional and spatial errors, and are often insensitive to hallucinated content that contradicts the input image. Pairwise comparison proves more reliable, though failure rates persist. These results highlight the unreliable nature of current Evaluator VLMs and urge caution in their deployment for benchmarking and development decisions. Code and data have been made publicly available.
匹配关键词: VLM
---

[ACADEMIC - ARXIV]
标题: A Deployable Embodied Vision-Language Navigation System with Hierarchical Cognition and Context-Aware Exploration
作者: Kuan Xu, Ruimeng Liu, Yizhuo Yang, Denan Liang, Tongxing Jin, Shenghai Yuan, Chen Wang, Lihua Xie
链接: https://arxiv.org/abs/2604.21363v1
完整摘要: Bridging the gap between embodied intelligence and embedded deployment remains a key challenge in intelligent robotic systems, where perception, reasoning, and planning must operate under strict constraints on computation, memory, energy, and real-time execution. In vision-language navigation (VLN), existing approaches often face a fundamental trade-off between strong reasoning capabilities and efficient deployment on real-world platforms. In this paper, we present a deployable embodied VLN system that achieves both high efficiency and robust high-level reasoning on real-world robotic platforms. To achieve this, we decouple the system into three asynchronous modules: a real-time perception module for continuous environment sensing, a memory integration module for spatial-semantic aggregation, and a reasoning module for high-level decision making. We incrementally construct a cognitive memory graph to encode scene information, which is further decomposed into subgraphs to enable reasoning with a vision-language model (VLM). To further improve navigation efficiency and accuracy, we also leverage the cognitive memory graph to formulate the exploration problem as a context-aware Weighted Traveling Repairman Problem (WTRP), which minimizes the weighted waiting time of viewpoints. Extensive experiments in both simulation and real-world robotic platforms demonstrate improved navigation success and efficiency over existing VLN approaches, while maintaining real-time performance on resource-constrained hardware.
匹配关键词: VLM
---

[ACADEMIC - ARXIV]
标题: Seeing Fast and Slow: Learning the Flow of Time in Videos
作者: Yen-Siang Wu, Rundong Luo, Jingsen Zhu, Tao Tu, Ali Farhadi, Matthew Wallingford, Yu-Chiang Frank Wang, Steve Marschner, Wei-Chiu Ma
链接: https://arxiv.org/abs/2604.21931v1
完整摘要: How can we tell whether a video has been sped up or slowed down? How can we generate videos at different speeds? Although videos have been central to modern computer vision research, little attention has been paid to perceiving and controlling the passage of time. In this paper, we study time as a learnable visual concept and develop models for reasoning about and manipulating the flow of time in videos. We first exploit the multimodal cues and temporal structure naturally present in videos to learn, in a self-supervised manner, to detect speed changes and estimate playback speed. We then show that these learned temporal reasoning models enable us to curate the largest slow-motion video dataset to date from noisy in-the-wild sources. Such slow-motion footage, typically filmed by high-speed cameras, contains substantially richer temporal detail than standard videos. Using this data, we further develop models capable of temporal control, including speed-conditioned video generation, which produces motion at specified playback speed, and temporal super-resolution, which tranforms low-FPS, blurry videos into high-FPS sequences with fine-grained temporal details. Our findings highlight time as a manipulable, perceptual dimension in video learning, opening doors to temporally controllable video generation, temporal forensics detection, and potentially richer world-models that understand how events unfold over time.
匹配关键词: image generation
---

[ACADEMIC - ARXIV]
标题: Evaluation of Automatic Speech Recognition Using Generative Large Language Models
作者: Thibault Bañeras-Roux, Shashi Kumar, Driss Khalil, Sergio Burdisso, Petr Motlicek, Shiran Liu, Mickael Rouvier, Jane Wottawa, Richard Dufour
链接: https://arxiv.org/abs/2604.21928v1
完整摘要: Automatic Speech Recognition (ASR) is traditionally evaluated using Word Error Rate (WER), a metric that is insensitive to meaning. Embedding-based semantic metrics are better correlated with human perception, but decoder-based Large Language Models (LLMs) remain underexplored for this task. This paper evaluates their relevance through three approaches: (1) selecting the best hypothesis between two candidates, (2) computing semantic distance using generative embeddings, and (3) qualitative classification of errors. On the HATS dataset, the best LLMs achieve 92--94\% agreement with human annotators for hypothesis selection, compared to 63\% for WER, also outperforming semantic metrics. Embeddings from decoder-based LLMs show performance comparable to encoder models. Finally, LLMs offer a promising direction for interpretable and semantic ASR evaluation.
匹配关键词: image generation
---

[ACADEMIC - ARXIV]
标题: Long-Horizon Manipulation via Trace-Conditioned VLA Planning
作者: Isabella Liu, An-Chieh Cheng, Rui Yan, Geng Chen, Ri-Zhao Qiu, Xueyan Zou, Sha Yi, Hongxu Yin, Xiaolong Wang, Sifei Liu
链接: https://arxiv.org/abs/2604.21924v1
完整摘要: Long-horizon manipulation remains challenging for vision-language-action (VLA) policies: real tasks are multi-step, progress-dependent, and brittle to compounding execution errors. We present LoHo-Manip, a modular framework that scales short-horizon VLA execution to long-horizon instruction following via a dedicated task-management VLM. The manager is decoupled from the executor and is invoked in a receding-horizon manner: given the current observation, it predicts a progress-aware remaining plan that combines (i) a subtask sequence with an explicit done + remaining split as lightweight language memory, and (ii) a visual trace -- a compact 2D keypoint trajectory prompt specifying where to go and what to approach next. The executor VLA is adapted to condition on the rendered trace, thereby turning long-horizon decision-making into repeated local control by following the trace. Crucially, predicting the remaining plan at each step yields an implicit closed loop: failed steps persist in subsequent outputs, and traces update accordingly, enabling automatic continuation and replanning without hand-crafted recovery logic or brittle visual-history buffers. Extensive experiments spanning embodied planning, long-horizon reasoning, trajectory prediction, and end-to-end manipulation in simulation and on a real Franka robot demonstrate strong gains in long-horizon success, robustness, and out-of-distribution generalization. Project page: https://www.liuisabella.com/LoHoManip
匹配关键词: image generation
---

[ACADEMIC - ARXIV]
标题: The Sample Complexity of Multicalibration
作者: Natalie Collina, Jiuyao Lu, Georgy Noarov, Aaron Roth
链接: https://arxiv.org/abs/2604.21923v1
完整摘要: We study the minimax sample complexity of multicalibration in the batch setting. A learner observes $n$ i.i.d. samples from an unknown distribution and must output a (possibly randomized) predictor whose population multicalibration error, measured by Expected Calibration Error (ECE), is at most $\varepsilon$ with respect to a given family of groups. For every fixed $κ> 0$, in the regime $|G|\le \varepsilon^{-κ}$, we prove that $\widetildeΘ(\varepsilon^{-3})$ samples are necessary and sufficient, up to polylogarithmic factors. The lower bound holds even for randomized predictors, and the upper bound is realized by a randomized predictor obtained via an online-to-batch reduction. This separates the sample complexity of multicalibration from that of marginal calibration, which scales as $\widetildeΘ(\varepsilon^{-2})$, and shows that mean-ECE multicalibration is as difficult in the batch setting as it is in the online setting, in contrast to marginal calibration which is strictly more difficult in the online setting. In contrast we observe that for $κ= 0$, the sample complexity of multicalibration remains $\widetildeΘ(\varepsilon^{-2})$ exhibiting a sharp threshold phenomenon. More generally, we establish matching upper and lower bounds, up to polylogarithmic factors, for a weighted $L_p$ multicalibration metric for all $1 \le p \le 2$, with optimal exponent $3/p$. We also extend the lower-bound template to a regular class of elicitable properties, and combine it with the online upper bounds of Hu et al. (2025) to obtain matching bounds for calibrating properties including expectiles and bounded-density quantiles.
匹配关键词: image generation
---

[ACADEMIC - ARXIV]
标题: Context Unrolling in Omni Models
作者: Ceyuan Yang, Zhijie Lin, Yang Zhao, Fei Xiao, Hao He, Qi Zhao, Chaorui Deng, Kunchang Li, Zihan Ding, Yuwei Guo, Fuyun Wang, Fangqi Zhu, Xiaonan Nie, Shenhan Zhu, Shanchuan Lin, Hongsheng Li, Weilin Huang, Guang Shi, Haoqi Fan
链接: https://arxiv.org/abs/2604.21921v1
完整摘要: We present Omni, a unified multimodal model natively trained on diverse modalities, including text, images, videos, 3D geometry, and hidden representations. We find that such training enables Context Unrolling, where the model explicitly reasons across multiple modal representations before producing predictions. This process enables the model to aggregate complementary information across heterogeneous modalities, facilitating a more faithful approximation of the shared multimodal knowledge manifold and improving downstream reasoning fidelity. As a result, Omni achieves strong performance on both multimodal generation and understanding benchmarks, while demonstrating advanced multimodal reasoning capabilities, including in-context generation of text, image, video, and 3D geometry.
匹配关键词: image generation
---

[ACADEMIC - ARXIV]
标题: Seeing Fast and Slow: Learning the Flow of Time in Videos
作者: Yen-Siang Wu, Rundong Luo, Jingsen Zhu, Tao Tu, Ali Farhadi, Matthew Wallingford, Yu-Chiang Frank Wang, Steve Marschner, Wei-Chiu Ma
链接: https://arxiv.org/abs/2604.21931v1
完整摘要: How can we tell whether a video has been sped up or slowed down? How can we generate videos at different speeds? Although videos have been central to modern computer vision research, little attention has been paid to perceiving and controlling the passage of time. In this paper, we study time as a learnable visual concept and develop models for reasoning about and manipulating the flow of time in videos. We first exploit the multimodal cues and temporal structure naturally present in videos to learn, in a self-supervised manner, to detect speed changes and estimate playback speed. We then show that these learned temporal reasoning models enable us to curate the largest slow-motion video dataset to date from noisy in-the-wild sources. Such slow-motion footage, typically filmed by high-speed cameras, contains substantially richer temporal detail than standard videos. Using this data, we further develop models capable of temporal control, including speed-conditioned video generation, which produces motion at specified playback speed, and temporal super-resolution, which tranforms low-FPS, blurry videos into high-FPS sequences with fine-grained temporal details. Our findings highlight time as a manipulable, perceptual dimension in video learning, opening doors to temporally controllable video generation, temporal forensics detection, and potentially richer world-models that understand how events unfold over time.
匹配关键词: video generation
---

[ACADEMIC - ARXIV]
标题: Evaluation of Automatic Speech Recognition Using Generative Large Language Models
作者: Thibault Bañeras-Roux, Shashi Kumar, Driss Khalil, Sergio Burdisso, Petr Motlicek, Shiran Liu, Mickael Rouvier, Jane Wottawa, Richard Dufour
链接: https://arxiv.org/abs/2604.21928v1
完整摘要: Automatic Speech Recognition (ASR) is traditionally evaluated using Word Error Rate (WER), a metric that is insensitive to meaning. Embedding-based semantic metrics are better correlated with human perception, but decoder-based Large Language Models (LLMs) remain underexplored for this task. This paper evaluates their relevance through three approaches: (1) selecting the best hypothesis between two candidates, (2) computing semantic distance using generative embeddings, and (3) qualitative classification of errors. On the HATS dataset, the best LLMs achieve 92--94\% agreement with human annotators for hypothesis selection, compared to 63\% for WER, also outperforming semantic metrics. Embeddings from decoder-based LLMs show performance comparable to encoder models. Finally, LLMs offer a promising direction for interpretable and semantic ASR evaluation.
匹配关键词: video generation
---

[ACADEMIC - ARXIV]
标题: Long-Horizon Manipulation via Trace-Conditioned VLA Planning
作者: Isabella Liu, An-Chieh Cheng, Rui Yan, Geng Chen, Ri-Zhao Qiu, Xueyan Zou, Sha Yi, Hongxu Yin, Xiaolong Wang, Sifei Liu
链接: https://arxiv.org/abs/2604.21924v1
完整摘要: Long-horizon manipulation remains challenging for vision-language-action (VLA) policies: real tasks are multi-step, progress-dependent, and brittle to compounding execution errors. We present LoHo-Manip, a modular framework that scales short-horizon VLA execution to long-horizon instruction following via a dedicated task-management VLM. The manager is decoupled from the executor and is invoked in a receding-horizon manner: given the current observation, it predicts a progress-aware remaining plan that combines (i) a subtask sequence with an explicit done + remaining split as lightweight language memory, and (ii) a visual trace -- a compact 2D keypoint trajectory prompt specifying where to go and what to approach next. The executor VLA is adapted to condition on the rendered trace, thereby turning long-horizon decision-making into repeated local control by following the trace. Crucially, predicting the remaining plan at each step yields an implicit closed loop: failed steps persist in subsequent outputs, and traces update accordingly, enabling automatic continuation and replanning without hand-crafted recovery logic or brittle visual-history buffers. Extensive experiments spanning embodied planning, long-horizon reasoning, trajectory prediction, and end-to-end manipulation in simulation and on a real Franka robot demonstrate strong gains in long-horizon success, robustness, and out-of-distribution generalization. Project page: https://www.liuisabella.com/LoHoManip
匹配关键词: video generation
---

[ACADEMIC - ARXIV]
标题: The Sample Complexity of Multicalibration
作者: Natalie Collina, Jiuyao Lu, Georgy Noarov, Aaron Roth
链接: https://arxiv.org/abs/2604.21923v1
完整摘要: We study the minimax sample complexity of multicalibration in the batch setting. A learner observes $n$ i.i.d. samples from an unknown distribution and must output a (possibly randomized) predictor whose population multicalibration error, measured by Expected Calibration Error (ECE), is at most $\varepsilon$ with respect to a given family of groups. For every fixed $κ> 0$, in the regime $|G|\le \varepsilon^{-κ}$, we prove that $\widetildeΘ(\varepsilon^{-3})$ samples are necessary and sufficient, up to polylogarithmic factors. The lower bound holds even for randomized predictors, and the upper bound is realized by a randomized predictor obtained via an online-to-batch reduction. This separates the sample complexity of multicalibration from that of marginal calibration, which scales as $\widetildeΘ(\varepsilon^{-2})$, and shows that mean-ECE multicalibration is as difficult in the batch setting as it is in the online setting, in contrast to marginal calibration which is strictly more difficult in the online setting. In contrast we observe that for $κ= 0$, the sample complexity of multicalibration remains $\widetildeΘ(\varepsilon^{-2})$ exhibiting a sharp threshold phenomenon. More generally, we establish matching upper and lower bounds, up to polylogarithmic factors, for a weighted $L_p$ multicalibration metric for all $1 \le p \le 2$, with optimal exponent $3/p$. We also extend the lower-bound template to a regular class of elicitable properties, and combine it with the online upper bounds of Hu et al. (2025) to obtain matching bounds for calibrating properties including expectiles and bounded-density quantiles.
匹配关键词: video generation
---

[ACADEMIC - ARXIV]
标题: Context Unrolling in Omni Models
作者: Ceyuan Yang, Zhijie Lin, Yang Zhao, Fei Xiao, Hao He, Qi Zhao, Chaorui Deng, Kunchang Li, Zihan Ding, Yuwei Guo, Fuyun Wang, Fangqi Zhu, Xiaonan Nie, Shenhan Zhu, Shanchuan Lin, Hongsheng Li, Weilin Huang, Guang Shi, Haoqi Fan
链接: https://arxiv.org/abs/2604.21921v1
完整摘要: We present Omni, a unified multimodal model natively trained on diverse modalities, including text, images, videos, 3D geometry, and hidden representations. We find that such training enables Context Unrolling, where the model explicitly reasons across multiple modal representations before producing predictions. This process enables the model to aggregate complementary information across heterogeneous modalities, facilitating a more faithful approximation of the shared multimodal knowledge manifold and improving downstream reasoning fidelity. As a result, Omni achieves strong performance on both multimodal generation and understanding benchmarks, while demonstrating advanced multimodal reasoning capabilities, including in-context generation of text, image, video, and 3D geometry.
匹配关键词: video generation
---

[ACADEMIC - ARXIV]
标题: Seeing Fast and Slow: Learning the Flow of Time in Videos
作者: Yen-Siang Wu, Rundong Luo, Jingsen Zhu, Tao Tu, Ali Farhadi, Matthew Wallingford, Yu-Chiang Frank Wang, Steve Marschner, Wei-Chiu Ma
链接: https://arxiv.org/abs/2604.21931v1
完整摘要: How can we tell whether a video has been sped up or slowed down? How can we generate videos at different speeds? Although videos have been central to modern computer vision research, little attention has been paid to perceiving and controlling the passage of time. In this paper, we study time as a learnable visual concept and develop models for reasoning about and manipulating the flow of time in videos. We first exploit the multimodal cues and temporal structure naturally present in videos to learn, in a self-supervised manner, to detect speed changes and estimate playback speed. We then show that these learned temporal reasoning models enable us to curate the largest slow-motion video dataset to date from noisy in-the-wild sources. Such slow-motion footage, typically filmed by high-speed cameras, contains substantially richer temporal detail than standard videos. Using this data, we further develop models capable of temporal control, including speed-conditioned video generation, which produces motion at specified playback speed, and temporal super-resolution, which tranforms low-FPS, blurry videos into high-FPS sequences with fine-grained temporal details. Our findings highlight time as a manipulable, perceptual dimension in video learning, opening doors to temporally controllable video generation, temporal forensics detection, and potentially richer world-models that understand how events unfold over time.
匹配关键词: visual reasoning
---

[ACADEMIC - ARXIV]
标题: Seeing Without Eyes: 4D Human-Scene Understanding from Wearable IMUs
作者: Hao-Yu Hsu, Tianhang Cheng, Jing Wen, Alexander G. Schwing, Shenlong Wang
链接: https://arxiv.org/abs/2604.21926v1
完整摘要: Understanding human activities and their surrounding environments typically relies on visual perception, yet cameras pose persistent challenges in privacy, safety, energy efficiency, and scalability. We explore an alternative: 4D perception without vision. Its goal is to reconstruct human motion and 3D scene layouts purely from everyday wearable sensors. For this we introduce IMU-to-4D, a framework that repurposes large language models for non-visual spatiotemporal understanding of human-scene dynamics. IMU-to-4D uses data from a few inertial sensors from earbuds, watches, or smartphones and predicts detailed 4D human motion together with coarse scene structure. Experiments across diverse human-scene datasets show that IMU-to-4D yields more coherent and temporally stable results than SoTA cascaded pipelines, suggesting wearable motion sensors alone can support rich 4D understanding.
匹配关键词: visual reasoning
---

[ACADEMIC - ARXIV]
标题: Long-Horizon Manipulation via Trace-Conditioned VLA Planning
作者: Isabella Liu, An-Chieh Cheng, Rui Yan, Geng Chen, Ri-Zhao Qiu, Xueyan Zou, Sha Yi, Hongxu Yin, Xiaolong Wang, Sifei Liu
链接: https://arxiv.org/abs/2604.21924v1
完整摘要: Long-horizon manipulation remains challenging for vision-language-action (VLA) policies: real tasks are multi-step, progress-dependent, and brittle to compounding execution errors. We present LoHo-Manip, a modular framework that scales short-horizon VLA execution to long-horizon instruction following via a dedicated task-management VLM. The manager is decoupled from the executor and is invoked in a receding-horizon manner: given the current observation, it predicts a progress-aware remaining plan that combines (i) a subtask sequence with an explicit done + remaining split as lightweight language memory, and (ii) a visual trace -- a compact 2D keypoint trajectory prompt specifying where to go and what to approach next. The executor VLA is adapted to condition on the rendered trace, thereby turning long-horizon decision-making into repeated local control by following the trace. Crucially, predicting the remaining plan at each step yields an implicit closed loop: failed steps persist in subsequent outputs, and traces update accordingly, enabling automatic continuation and replanning without hand-crafted recovery logic or brittle visual-history buffers. Extensive experiments spanning embodied planning, long-horizon reasoning, trajectory prediction, and end-to-end manipulation in simulation and on a real Franka robot demonstrate strong gains in long-horizon success, robustness, and out-of-distribution generalization. Project page: https://www.liuisabella.com/LoHoManip
匹配关键词: visual reasoning
---

[ACADEMIC - ARXIV]
标题: Context Unrolling in Omni Models
作者: Ceyuan Yang, Zhijie Lin, Yang Zhao, Fei Xiao, Hao He, Qi Zhao, Chaorui Deng, Kunchang Li, Zihan Ding, Yuwei Guo, Fuyun Wang, Fangqi Zhu, Xiaonan Nie, Shenhan Zhu, Shanchuan Lin, Hongsheng Li, Weilin Huang, Guang Shi, Haoqi Fan
链接: https://arxiv.org/abs/2604.21921v1
完整摘要: We present Omni, a unified multimodal model natively trained on diverse modalities, including text, images, videos, 3D geometry, and hidden representations. We find that such training enables Context Unrolling, where the model explicitly reasons across multiple modal representations before producing predictions. This process enables the model to aggregate complementary information across heterogeneous modalities, facilitating a more faithful approximation of the shared multimodal knowledge manifold and improving downstream reasoning fidelity. As a result, Omni achieves strong performance on both multimodal generation and understanding benchmarks, while demonstrating advanced multimodal reasoning capabilities, including in-context generation of text, image, video, and 3D geometry.
匹配关键词: visual reasoning
---

[ACADEMIC - ARXIV]
标题: Vista4D: Video Reshooting with 4D Point Clouds
作者: Kuan Heng Lin, Zhizheng Liu, Pablo Salamanca, Yash Kant, Ryan Burgert, Yuancheng Xu, Koichi Namekata, Yiwei Zhao, Bolei Zhou, Micah Goldblum, Paul Debevec, Ning Yu
链接: https://arxiv.org/abs/2604.21915v1
完整摘要: We present Vista4D, a robust and flexible video reshooting framework that grounds the input video and target cameras in a 4D point cloud. Specifically, given an input video, our method re-synthesizes the scene with the same dynamics from a different camera trajectory and viewpoint. Existing video reshooting methods often struggle with depth estimation artifacts of real-world dynamic videos, while also failing to preserve content appearance and failing to maintain precise camera control for challenging new trajectories. We build a 4D-grounded point cloud representation with static pixel segmentation and 4D reconstruction to explicitly preserve seen content and provide rich camera signals, and we train with reconstructed multiview dynamic data for robustness against point cloud artifacts during real-world inference. Our results demonstrate improved 4D consistency, camera control, and visual quality compared to state-of-the-art baselines under a variety of videos and camera paths. Moreover, our method generalizes to real-world applications such as dynamic scene expansion and 4D scene recomposition. See our project page for results, code, and models: https://eyeline-labs.github.io/Vista4D
匹配关键词: visual reasoning
---

[ACADEMIC - ARXIV]
标题: Seeing Fast and Slow: Learning the Flow of Time in Videos
作者: Yen-Siang Wu, Rundong Luo, Jingsen Zhu, Tao Tu, Ali Farhadi, Matthew Wallingford, Yu-Chiang Frank Wang, Steve Marschner, Wei-Chiu Ma
链接: https://arxiv.org/abs/2604.21931v1
完整摘要: How can we tell whether a video has been sped up or slowed down? How can we generate videos at different speeds? Although videos have been central to modern computer vision research, little attention has been paid to perceiving and controlling the passage of time. In this paper, we study time as a learnable visual concept and develop models for reasoning about and manipulating the flow of time in videos. We first exploit the multimodal cues and temporal structure naturally present in videos to learn, in a self-supervised manner, to detect speed changes and estimate playback speed. We then show that these learned temporal reasoning models enable us to curate the largest slow-motion video dataset to date from noisy in-the-wild sources. Such slow-motion footage, typically filmed by high-speed cameras, contains substantially richer temporal detail than standard videos. Using this data, we further develop models capable of temporal control, including speed-conditioned video generation, which produces motion at specified playback speed, and temporal super-resolution, which tranforms low-FPS, blurry videos into high-FPS sequences with fine-grained temporal details. Our findings highlight time as a manipulable, perceptual dimension in video learning, opening doors to temporally controllable video generation, temporal forensics detection, and potentially richer world-models that understand how events unfold over time.
匹配关键词: diffusion model
---

[ACADEMIC - ARXIV]
标题: Temporal Taskification in Streaming Continual Learning: A Source of Evaluation Instability
作者: Nicolae Filat, Ahmed Hussain, Konstantinos Kalogiannis, Elena Burceanu
链接: https://arxiv.org/abs/2604.21930v1
完整摘要: Streaming Continual Learning (CL) typically converts a continuous stream into a sequence of discrete tasks through temporal partitioning. We argue that this temporal taskification step is not a neutral preprocessing choice, but a structural component of evaluation: different valid splits of the same stream can induce different CL regimes and therefore different benchmark conclusions. To study this effect, we introduce a taskification-level framework based on plasticity and stability profiles, a profile distance between taskifications, and Boundary-Profile Sensitivity (BPS), which diagnoses how strongly small boundary perturbations alter the induced regime before any CL model is trained. We evaluate continual finetuning, Experience Replay, Elastic Weight Consolidation, and Learning without Forgetting on network traffic forecasting with CESNET-Timeseries24, keeping the stream, model, and training budget fixed while varying only the temporal taskification. Across 9-, 30-, and 44-day splits, we observe substantial changes in forecasting error, forgetting, and backward transfer, showing that taskification alone can materially affect CL evaluation. We further find that shorter taskifications induce noisier distribution-level patterns, larger structural distances, and higher BPS, indicating greater sensitivity to boundary perturbations. These results show that benchmark conclusions in streaming CL depend not only on the learner and the data stream, but also on how that stream is taskified, motivating temporal taskification as a first-class evaluation variable.
匹配关键词: diffusion model
---

[ACADEMIC - ARXIV]
标题: Evaluation of Automatic Speech Recognition Using Generative Large Language Models
作者: Thibault Bañeras-Roux, Shashi Kumar, Driss Khalil, Sergio Burdisso, Petr Motlicek, Shiran Liu, Mickael Rouvier, Jane Wottawa, Richard Dufour
链接: https://arxiv.org/abs/2604.21928v1
完整摘要: Automatic Speech Recognition (ASR) is traditionally evaluated using Word Error Rate (WER), a metric that is insensitive to meaning. Embedding-based semantic metrics are better correlated with human perception, but decoder-based Large Language Models (LLMs) remain underexplored for this task. This paper evaluates their relevance through three approaches: (1) selecting the best hypothesis between two candidates, (2) computing semantic distance using generative embeddings, and (3) qualitative classification of errors. On the HATS dataset, the best LLMs achieve 92--94\% agreement with human annotators for hypothesis selection, compared to 63\% for WER, also outperforming semantic metrics. Embeddings from decoder-based LLMs show performance comparable to encoder models. Finally, LLMs offer a promising direction for interpretable and semantic ASR evaluation.
匹配关键词: diffusion model
---

[ACADEMIC - ARXIV]
标题: Fine-Tuning Regimes Define Distinct Continual Learning Problems
作者: Paul-Tiberiu Iordache, Elena Burceanu
链接: https://arxiv.org/abs/2604.21927v1
完整摘要: Continual learning (CL) studies how models acquire tasks sequentially while retaining previously learned knowledge. Despite substantial progress in benchmarking CL methods, comparative evaluations typically keep the fine-tuning regime fixed. In this paper, we argue that the fine-tuning regime, defined by the trainable parameter subspace, is itself a key evaluation variable. We formalize adaptation regimes as projected optimization over fixed trainable subspaces, showing that changing the trainable depth alters the effective update signal through which both current task fitting and knowledge preservation operate. This analysis motivates the hypothesis that method comparisons need not be invariant across regimes. We test this hypothesis in task incremental CL, five trainable depth regimes, and four standard methods: online EWC, LwF, SI, and GEM. Across five benchmark datasets, namely MNIST, Fashion MNIST, KMNIST, QMNIST, and CIFAR-100, and across 11 task orders per dataset, we find that the relative ranking of methods is not consistently preserved across regimes. We further show that deeper adaptation regimes are associated with larger update magnitudes, higher forgetting, and a stronger relationship between the two. These results show that comparative conclusions in CL can depend strongly on the chosen fine-tuning regime, motivating regime-aware evaluation protocols that treat trainable depth as an explicit experimental factor.
匹配关键词: diffusion model
---

[ACADEMIC - ARXIV]
标题: Seeing Without Eyes: 4D Human-Scene Understanding from Wearable IMUs
作者: Hao-Yu Hsu, Tianhang Cheng, Jing Wen, Alexander G. Schwing, Shenlong Wang
链接: https://arxiv.org/abs/2604.21926v1
完整摘要: Understanding human activities and their surrounding environments typically relies on visual perception, yet cameras pose persistent challenges in privacy, safety, energy efficiency, and scalability. We explore an alternative: 4D perception without vision. Its goal is to reconstruct human motion and 3D scene layouts purely from everyday wearable sensors. For this we introduce IMU-to-4D, a framework that repurposes large language models for non-visual spatiotemporal understanding of human-scene dynamics. IMU-to-4D uses data from a few inertial sensors from earbuds, watches, or smartphones and predicts detailed 4D human motion together with coarse scene structure. Experiments across diverse human-scene datasets show that IMU-to-4D yields more coherent and temporally stable results than SoTA cascaded pipelines, suggesting wearable motion sensors alone can support rich 4D understanding.
匹配关键词: diffusion model
---

[ACADEMIC - ARXIV]
标题: Evaluation of Automatic Speech Recognition Using Generative Large Language Models
作者: Thibault Bañeras-Roux, Shashi Kumar, Driss Khalil, Sergio Burdisso, Petr Motlicek, Shiran Liu, Mickael Rouvier, Jane Wottawa, Richard Dufour
链接: https://arxiv.org/abs/2604.21928v1
完整摘要: Automatic Speech Recognition (ASR) is traditionally evaluated using Word Error Rate (WER), a metric that is insensitive to meaning. Embedding-based semantic metrics are better correlated with human perception, but decoder-based Large Language Models (LLMs) remain underexplored for this task. This paper evaluates their relevance through three approaches: (1) selecting the best hypothesis between two candidates, (2) computing semantic distance using generative embeddings, and (3) qualitative classification of errors. On the HATS dataset, the best LLMs achieve 92--94\% agreement with human annotators for hypothesis selection, compared to 63\% for WER, also outperforming semantic metrics. Embeddings from decoder-based LLMs show performance comparable to encoder models. Finally, LLMs offer a promising direction for interpretable and semantic ASR evaluation.
匹配关键词: speech synthesis
---

[ACADEMIC - ARXIV]
标题: VistaBot: View-Robust Robot Manipulation via Spatiotemporal-Aware View Synthesis
作者: Songen Gu, Yuhang Zheng, Weize Li, Yupeng Zheng, Yating Feng, Xiang Li, Yilun Chen, Pengfei Li, Wenchao Ding
链接: https://arxiv.org/abs/2604.21914v1
完整摘要: Recently, end-to-end robotic manipulation models have gained significant attention for their generalizability and scalability. However, they often suffer from limited robustness to camera viewpoint changes when training with a fixed camera. In this paper, we propose VistaBot, a novel framework that integrates feed-forward geometric models with video diffusion models to achieve view-robust closed-loop manipulation without requiring camera calibration at test time. Our approach consists of three key components: 4D geometry estimation, view synthesis latent extraction, and latent action learning. VistaBot is integrated into both action-chunking (ACT) and diffusion-based ($π_0$) policies and evaluated across simulation and real-world tasks. We further introduce the View Generalization Score (VGS) as a new metric for comprehensive evaluation of cross-view generalization. Results show that VistaBot improves VGS by 2.79$\times$ and 2.63$\times$ over ACT and $π_0$, respectively, while also achieving high-quality novel view synthesis. Our contributions include a geometry-aware synthesis model, a latent action planner, a new benchmark metric, and extensive validation across diverse environments. The code and models will be made publicly available.
匹配关键词: speech synthesis
---

[ACADEMIC - ARXIV]
标题: Mapping the Political Discourse in the Brazilian Chamber of Deputies: A Multi-Faceted Computational Approach
作者: Flávio Soriano, Victoria F. Mello, Pedro B. Rigueira, Gisele L. Pappa, Wagner Meira, Ana Paula Couto da Silva, Jussara M. Almeida
链接: https://arxiv.org/abs/2604.21897v1
完整摘要: Analyses of legislative behavior often rely on voting records, overlooking the rich semantic and rhetorical content of political speech. In this paper, we ask three complementary questions about parliamentary discourse: how things are said, what is being said, and who is speaking in discursively similar ways. To answer these questions, we introduce a scalable and generalizable computational framework that combines diachronic stylometric analysis, contextual topic modeling, and semantic clustering of deputies' speeches. We apply this framework to a large-scale case study of the Brazilian Chamber of Deputies, using a corpus of over 450,000 speeches from 2003 to 2025. Our results show a long-term stylistic shift toward shorter and more direct speeches, a legislative agenda that reorients sharply in response to national crises, and a granular map of discursive alignments in which regional and gender identities often prove more salient than formal party affiliation. More broadly, this work offers a robust methodology for analyzing parliamentary discourse as a multidimensional phenomenon that complements traditional vote-based approaches.
匹配关键词: speech synthesis
---

[ACADEMIC - ARXIV]
标题: Reshoot-Anything: A Self-Supervised Model for In-the-Wild Video Reshooting
作者: Avinash Paliwal, Adithya Iyer, Shivin Yadav, Muhammad Ali Afridi, Midhun Harikumar
链接: https://arxiv.org/abs/2604.21776v1
完整摘要: Precise camera control for reshooting dynamic videos is bottlenecked by the severe scarcity of paired multi-view data for non-rigid scenes. We overcome this limitation with a highly scalable self-supervised framework capable of leveraging internet-scale monocular videos. Our core contribution is the generation of pseudo multi-view training triplets, consisting of a source video, a geometric anchor, and a target video. We achieve this by extracting distinct smooth random-walk crop trajectories from a single input video to serve as the source and target views. The anchor is synthetically generated by forward-warping the first frame of the source with a dense tracking field, which effectively simulates the distorted point-cloud inputs expected at inference. Because our independent cropping strategy introduces spatial misalignment and artificial occlusions, the model cannot simply copy information from the current source frame. Instead, it is forced to implicitly learn 4D spatiotemporal structures by actively routing and re-projecting missing high-fidelity textures across distinct times and viewpoints from the source video to reconstruct the target. At inference, our minimally adapted diffusion transformer utilizes a 4D point-cloud derived anchor to achieve state-of-the-art temporal consistency, robust camera control, and high-fidelity novel view synthesis on complex dynamic scenes.
匹配关键词: speech synthesis
---

[ACADEMIC - ARXIV]
标题: Phonological Subspace Collapse Is Aetiology-Specific and Cross-Lingually Stable: Evidence from 3,374 Speakers
作者: Bernard Muller, Antonio Armando Ortiz Barrañón, LaVonne Roberts
链接: https://arxiv.org/abs/2604.21706v1
完整摘要: We previously introduced a training-free method for dysarthria severity assessment based on d-prime separability of phonological feature subspaces in frozen self-supervised speech representations, validated on 890 speakers across 5 languages with HuBERT-base. Here, we scale the analysis to 3,374 speakers from 25 datasets spanning 12 languages and 5 aetiologies (Parkinson's disease, cerebral palsy, ALS, Down syndrome, and stroke), plus healthy controls, using 6 SSL backbones. We report three findings. First, aetiology-specific degradation profiles are distinguishable at the group level: 10 of 13 features yield large effect sizes (epsilon-squared > 0.14, Holm-corrected p < 0.001), with Parkinson's disease separable from the articulatory execution group at Cohen's d = 0.83; individual-level classification remains limited (22.6% macro F1). Second, profiles show cross-lingual profile-shape stability: cosine similarity of 5-dimensional consonant d-prime profiles exceeds 0.95 across the languages available for each aetiology. Absolute d-prime magnitudes are not cross-lingually calibrated, so the method supports language-independent phenotyping of degradation patterns but requires within-corpus calibration for absolute severity interpretation. Third, the method is architecture-independent: all 6 backbones produce monotonic severity gradients with inter-model agreement exceeding rho = 0.77. Fixed-token d-prime estimation preserves the severity correlation (rho = -0.733 at 200 tokens per class), confirming that the signal is not a token-count artefact. These results support phonological subspace analysis as a robust, training-free framework for aetiology-aware dysarthria characterisation, with evidence of cross-lingual profile-shape stability and cross-backbone robustness in the represented sample.
匹配关键词: speech synthesis
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
标题: Anonymization, Not Elimination: Utility-Preserved Speech Anonymization
作者: Yunchong Xiao, Yuxiang Zhao, Ziyang Ma, Shuai Wang, Kai Yu, Jiachun Liao, Xie Chen
链接: https://arxiv.org/abs/2604.17000v1
完整摘要: The growing reliance on large-scale speech data has made privacy protection a critical concern. However, existing anonymization approaches often degrade data utility, for example by disrupting acoustic continuity or reducing vocal diversity, which compromises the value of speech data for downstream tasks such as Automatic Speech Recognition (ASR), Text-to-Speech (TTS), and Speech Emotion Recognition (SER). Current evaluation practices are also limited, as they mainly rely on direct testing of anonymized speech with pretrained models, providing only a partial view of utility. To address these issues, we propose a novel two-stage framework that protects both linguistic content and acoustic identity while maintaining usability. For content privacy, we employ a generative speech editing model to seamlessly replace personally identifiable information (PII), and for voice privacy, we introduce F3-VA, a flow-matching-based anonymization framework with a three-stage design that produces diverse and distinct anonymized speakers. To enable a more comprehensive assessment, we evaluate privacy using both acoustic- and content-based speaker verification metrics, and assess utility by training ASR, TTS, and SER models from scratch. Experimental results show that our framework achieves stronger privacy protection with minimal utility degradation compared to baselines from the VoicePrivacy Challenge, while the proposed evaluation protocol provides a more realistic reflection of the utility of anonymized speech under privacy protection.
匹配关键词: TTS
---

[ACADEMIC - ARXIV]
标题: AST: Adaptive, Seamless, and Training-Free Precise Speech Editing
作者: Sihan Lv, Yechen Jin, Zhen Li, Jintao Chen, Jinshan Zhang, Ying Li, Jianwei Yin, Meng Xi
链接: https://arxiv.org/abs/2604.16056v1
完整摘要: Text-based speech editing aims to modify specific segments while preserving speaker identity and acoustic context. Existing methods rely on task-specific training, which incurs high data costs and struggles with temporal fidelity in unedited regions. Meanwhile, adapting Text-to-Speech (TTS) models often faces a trade-off between editing quality and consistency. To address these issues, we propose AST, an Adaptive, Seamless, and Training-free precise speech editing framework. Leveraging a pre-trained autoregressive TTS model, AST introduces Latent Recomposition to selectively stitch preserved source segments with newly synthesized targets. Furthermore, AST extends this latent manipulation to enable precise style editing for specific speech segments. To prevent artifacts at these edit boundaries, the framework incorporates Adaptive Weak Fact Guidance (AWFG). AWFG dynamically modulates a mel-space guidance signal, enforcing structural constraints only where necessary without disrupting the generative manifold. To fill the gap of publicly accessible benchmarks, we introduce LibriSpeech-Edit, a new and larger speech editing dataset. As existing metrics poorly evaluate temporal consistency in unedited regions, we propose Word-level Dynamic Time Warping (WDTW). Extensive experiments demonstrate that AST resolves the controllability-quality trade-off without extra training. Compared to the previous most temporally consistent baseline, AST improves consistency while reducing Word Error Rate by nearly 70%. Moreover, applying AST to a foundation TTS model reduces WDTW by 27%, achieving state-of-the-art speaker preservation and temporal fidelity.
匹配关键词: TTS
---

[ACADEMIC - ARXIV]
标题: Evaluation of Automatic Speech Recognition Using Generative Large Language Models
作者: Thibault Bañeras-Roux, Shashi Kumar, Driss Khalil, Sergio Burdisso, Petr Motlicek, Shiran Liu, Mickael Rouvier, Jane Wottawa, Richard Dufour
链接: https://arxiv.org/abs/2604.21928v1
完整摘要: Automatic Speech Recognition (ASR) is traditionally evaluated using Word Error Rate (WER), a metric that is insensitive to meaning. Embedding-based semantic metrics are better correlated with human perception, but decoder-based Large Language Models (LLMs) remain underexplored for this task. This paper evaluates their relevance through three approaches: (1) selecting the best hypothesis between two candidates, (2) computing semantic distance using generative embeddings, and (3) qualitative classification of errors. On the HATS dataset, the best LLMs achieve 92--94\% agreement with human annotators for hypothesis selection, compared to 63\% for WER, also outperforming semantic metrics. Embeddings from decoder-based LLMs show performance comparable to encoder models. Finally, LLMs offer a promising direction for interpretable and semantic ASR evaluation.
匹配关键词: ASR
---

[ACADEMIC - ARXIV]
标题: Stealthy Backdoor Attacks against LLMs Based on Natural Style Triggers
作者: Jiali Wei, Ming Fan, Guoheng Sun, Xicheng Zhang, Haijun Wang, Ting Liu
链接: https://arxiv.org/abs/2604.21700v1
完整摘要: The growing application of large language models (LLMs) in safety-critical domains has raised urgent concerns about their security. Many recent studies have demonstrated the feasibility of backdoor attacks against LLMs. However, existing methods suffer from three key shortcomings: explicit trigger patterns that compromise naturalness, unreliable injection of attacker-specified payloads in long-form generation, and incompletely specified threat models that obscure how backdoors are delivered and activated in practice. To address these gaps, we present BadStyle, a complete backdoor attack framework and pipeline. BadStyle leverages an LLM as a poisoned sample generator to construct natural and stealthy poisoned samples that carry imperceptible style-level triggers while preserving semantics and fluency. To stabilize payload injection during fine-tuning, we design an auxiliary target loss that reinforces the attacker-specified target content in responses to poisoned inputs and penalizes its emergence in benign responses. We further ground the attack in a realistic threat model and systematically evaluate BadStyle under both prompt-induced and PEFT-based injection strategies. Extensive experiments across seven victim LLMs, including LLaMA, Phi, DeepSeek, and GPT series, demonstrate that BadStyle achieves high attack success rates (ASRs) while maintaining strong stealthiness. The proposed auxiliary target loss substantially improves the stability of backdoor activation, yielding an average ASR improvement of around 30% across style-level triggers. Even in downstream deployment scenarios unknown during injection, the implanted backdoor remains effective. Moreover, BadStyle consistently evades representative input-level defenses and bypasses output-level defenses through simple camouflage.
匹配关键词: ASR
---

[ACADEMIC - ARXIV]
标题: "This Wasn't Made for Me": Recentering User Experience and Emotional Impact in the Evaluation of ASR Bias
作者: Siyu Liang, Alicia Beckford Wassink
链接: https://arxiv.org/abs/2604.21148v1
完整摘要: Studies on bias in Automatic Speech Recognition (ASR) tend to focus on reporting error rates for speakers of underrepresented dialects, yet less research examines the human side of system bias: how do system failures shape users' lived experiences, how do users feel about and react to them, and what emotional toll do these repeated failures exact? We conducted user experience studies across four U.S. locations (Atlanta, Gulf Coast, Miami Beach, and Tucson) representing distinct English dialect communities. Our findings reveal that most participants report technologies fail to consider their cultural backgrounds and require constant adjustment to achieve basic functionality. Despite these experiences, participants maintain high expectations for ASR performance and express strong willingness to contribute to model improvement. Qualitative analysis of open-ended narratives exposes the deeper costs of these failures. Participants report frustration, annoyance, and feelings of inadequacy, yet the emotional impact extends beyond momentary reactions. Participants recognize that systems were not designed for them, yet often internalize failures as personal inadequacy despite this critical awareness. They perform extensive invisible labor, including code-switching, hyper-articulation, and emotional management, to make failing systems functional. Meanwhile, their linguistic and cultural knowledge remains unrecognized by technologies that encode particular varieties as standard while rendering others marginal. These findings demonstrate that algorithmic fairness assessments based on accuracy metrics alone miss critical dimensions of harm: the emotional labor of managing repeated technological rejection, the cognitive burden of constant self-monitoring, and the psychological toll of feeling inadequate in one's native language variety.
匹配关键词: ASR
---

[ACADEMIC - ARXIV]
标题: Breaking MCP with Function Hijacking Attacks: Novel Threats for Function Calling and Agentic Models
作者: Yannis Belkhiter, Giulio Zizzo, Sergio Maffeis, Seshu Tirupathi, John D. Kelleher
链接: https://arxiv.org/abs/2604.20994v1
完整摘要: The growth of agentic AI has drawn significant attention to function calling Large Language Models (LLMs), which are designed to extend the capabilities of AI-powered system by invoking external functions. Injection and jailbreaking attacks have been extensively explored to showcase the vulnerabilities of LLMs to user prompt manipulation. The expanded capabilities of agentic models introduce further vulnerabilities via their function calling interface. Recent work in LLM security showed that function calling can be abused, leading to data tampering and theft, causing disruptive behavior such as endless loops, or causing LLMs to produce harmful content in the style of jailbreaking attacks. This paper introduces a novel function hijacking attack (FHA) that manipulates the tool selection process of agentic models to force the invocation of a specific, attacker-chosen function. While existing attacks focus on semantic preference of the model for function-calling tasks, we show that FHA is largely agnostic to the context semantics and robust to the function sets, making it applicable across diverse domains. We further demonstrate that FHA can be trained to produce universal adversarial functions, enabling a single attacked function to hijack tool selection across multiple queries and payload configurations. We conducted experiments on 5 different models, including instructed and reasoning variants, reaching 70% to 100% ASR over the established BFCL dataset. Our findings further demonstrate the need for strong guardrails and security modules for agentic systems.
匹配关键词: ASR
---

[ACADEMIC - ARXIV]
标题: ATIR: Towards Audio-Text Interleaved Contextual Retrieval
作者: Tong Zhao, Chenghao Zhang, Yutao Zhu, Zhicheng Dou
链接: https://arxiv.org/abs/2604.20267v1
完整摘要: Audio carries richer information than text, including emotion, speaker traits, and environmental context, while also enabling lower-latency processing compared to speech-to-text pipelines. However, recent multimodal information retrieval research has predominantly focused on images, largely overlooking audio, especially in the setting of interleaved audio-text contextual retrieval. In this work, we introduce the Audio-Text Interleaved contextual Retrieval (ATIR) task, where queries can alternate between audio and text modalities. We construct an ATIR benchmark by integrating several Automatic Speech Recognition (ASR), QA, and retrieval datasets, ultimately unifying four types of contextual retrieval tasks. This benchmark substantially addresses the limitations of existing audio retrieval datasets in semantic retrieval. To study this task, we evaluate several off-the-shelf retrievers and train our ATIR model based on a Multimodal Large Language Model (MLLM). We further introduce a novel token compression mechanism that is orthogonal to existing compression methods, thereby alleviating the issue of excessive audio tokens in MLLM-based ATIR models. Experimental results demonstrate that our ATIR model achieves substantial improvements over strong baselines.
匹配关键词: ASR
---

[ACADEMIC - ARXIV]
标题: Seeing Fast and Slow: Learning the Flow of Time in Videos
作者: Yen-Siang Wu, Rundong Luo, Jingsen Zhu, Tao Tu, Ali Farhadi, Matthew Wallingford, Yu-Chiang Frank Wang, Steve Marschner, Wei-Chiu Ma
链接: https://arxiv.org/abs/2604.21931v1
完整摘要: How can we tell whether a video has been sped up or slowed down? How can we generate videos at different speeds? Although videos have been central to modern computer vision research, little attention has been paid to perceiving and controlling the passage of time. In this paper, we study time as a learnable visual concept and develop models for reasoning about and manipulating the flow of time in videos. We first exploit the multimodal cues and temporal structure naturally present in videos to learn, in a self-supervised manner, to detect speed changes and estimate playback speed. We then show that these learned temporal reasoning models enable us to curate the largest slow-motion video dataset to date from noisy in-the-wild sources. Such slow-motion footage, typically filmed by high-speed cameras, contains substantially richer temporal detail than standard videos. Using this data, we further develop models capable of temporal control, including speed-conditioned video generation, which produces motion at specified playback speed, and temporal super-resolution, which tranforms low-FPS, blurry videos into high-FPS sequences with fine-grained temporal details. Our findings highlight time as a manipulable, perceptual dimension in video learning, opening doors to temporally controllable video generation, temporal forensics detection, and potentially richer world-models that understand how events unfold over time.
匹配关键词: speech recognition
---

[ACADEMIC - ARXIV]
标题: Evaluation of Automatic Speech Recognition Using Generative Large Language Models
作者: Thibault Bañeras-Roux, Shashi Kumar, Driss Khalil, Sergio Burdisso, Petr Motlicek, Shiran Liu, Mickael Rouvier, Jane Wottawa, Richard Dufour
链接: https://arxiv.org/abs/2604.21928v1
完整摘要: Automatic Speech Recognition (ASR) is traditionally evaluated using Word Error Rate (WER), a metric that is insensitive to meaning. Embedding-based semantic metrics are better correlated with human perception, but decoder-based Large Language Models (LLMs) remain underexplored for this task. This paper evaluates their relevance through three approaches: (1) selecting the best hypothesis between two candidates, (2) computing semantic distance using generative embeddings, and (3) qualitative classification of errors. On the HATS dataset, the best LLMs achieve 92--94\% agreement with human annotators for hypothesis selection, compared to 63\% for WER, also outperforming semantic metrics. Embeddings from decoder-based LLMs show performance comparable to encoder models. Finally, LLMs offer a promising direction for interpretable and semantic ASR evaluation.
匹配关键词: speech recognition
---

[ACADEMIC - ARXIV]
标题: Seeing Without Eyes: 4D Human-Scene Understanding from Wearable IMUs
作者: Hao-Yu Hsu, Tianhang Cheng, Jing Wen, Alexander G. Schwing, Shenlong Wang
链接: https://arxiv.org/abs/2604.21926v1
完整摘要: Understanding human activities and their surrounding environments typically relies on visual perception, yet cameras pose persistent challenges in privacy, safety, energy efficiency, and scalability. We explore an alternative: 4D perception without vision. Its goal is to reconstruct human motion and 3D scene layouts purely from everyday wearable sensors. For this we introduce IMU-to-4D, a framework that repurposes large language models for non-visual spatiotemporal understanding of human-scene dynamics. IMU-to-4D uses data from a few inertial sensors from earbuds, watches, or smartphones and predicts detailed 4D human motion together with coarse scene structure. Experiments across diverse human-scene datasets show that IMU-to-4D yields more coherent and temporally stable results than SoTA cascaded pipelines, suggesting wearable motion sensors alone can support rich 4D understanding.
匹配关键词: speech recognition
---

[ACADEMIC - ARXIV]
标题: Context Unrolling in Omni Models
作者: Ceyuan Yang, Zhijie Lin, Yang Zhao, Fei Xiao, Hao He, Qi Zhao, Chaorui Deng, Kunchang Li, Zihan Ding, Yuwei Guo, Fuyun Wang, Fangqi Zhu, Xiaonan Nie, Shenhan Zhu, Shanchuan Lin, Hongsheng Li, Weilin Huang, Guang Shi, Haoqi Fan
链接: https://arxiv.org/abs/2604.21921v1
完整摘要: We present Omni, a unified multimodal model natively trained on diverse modalities, including text, images, videos, 3D geometry, and hidden representations. We find that such training enables Context Unrolling, where the model explicitly reasons across multiple modal representations before producing predictions. This process enables the model to aggregate complementary information across heterogeneous modalities, facilitating a more faithful approximation of the shared multimodal knowledge manifold and improving downstream reasoning fidelity. As a result, Omni achieves strong performance on both multimodal generation and understanding benchmarks, while demonstrating advanced multimodal reasoning capabilities, including in-context generation of text, image, video, and 3D geometry.
匹配关键词: speech recognition
---

[ACADEMIC - ARXIV]
标题: Vista4D: Video Reshooting with 4D Point Clouds
作者: Kuan Heng Lin, Zhizheng Liu, Pablo Salamanca, Yash Kant, Ryan Burgert, Yuancheng Xu, Koichi Namekata, Yiwei Zhao, Bolei Zhou, Micah Goldblum, Paul Debevec, Ning Yu
链接: https://arxiv.org/abs/2604.21915v1
完整摘要: We present Vista4D, a robust and flexible video reshooting framework that grounds the input video and target cameras in a 4D point cloud. Specifically, given an input video, our method re-synthesizes the scene with the same dynamics from a different camera trajectory and viewpoint. Existing video reshooting methods often struggle with depth estimation artifacts of real-world dynamic videos, while also failing to preserve content appearance and failing to maintain precise camera control for challenging new trajectories. We build a 4D-grounded point cloud representation with static pixel segmentation and 4D reconstruction to explicitly preserve seen content and provide rich camera signals, and we train with reconstructed multiview dynamic data for robustness against point cloud artifacts during real-world inference. Our results demonstrate improved 4D consistency, camera control, and visual quality compared to state-of-the-art baselines under a variety of videos and camera paths. Moreover, our method generalizes to real-world applications such as dynamic scene expansion and 4D scene recomposition. See our project page for results, code, and models: https://eyeline-labs.github.io/Vista4D
匹配关键词: speech recognition
---

[ACADEMIC - ARXIV]
标题: Seeing Fast and Slow: Learning the Flow of Time in Videos
作者: Yen-Siang Wu, Rundong Luo, Jingsen Zhu, Tao Tu, Ali Farhadi, Matthew Wallingford, Yu-Chiang Frank Wang, Steve Marschner, Wei-Chiu Ma
链接: https://arxiv.org/abs/2604.21931v1
完整摘要: How can we tell whether a video has been sped up or slowed down? How can we generate videos at different speeds? Although videos have been central to modern computer vision research, little attention has been paid to perceiving and controlling the passage of time. In this paper, we study time as a learnable visual concept and develop models for reasoning about and manipulating the flow of time in videos. We first exploit the multimodal cues and temporal structure naturally present in videos to learn, in a self-supervised manner, to detect speed changes and estimate playback speed. We then show that these learned temporal reasoning models enable us to curate the largest slow-motion video dataset to date from noisy in-the-wild sources. Such slow-motion footage, typically filmed by high-speed cameras, contains substantially richer temporal detail than standard videos. Using this data, we further develop models capable of temporal control, including speed-conditioned video generation, which produces motion at specified playback speed, and temporal super-resolution, which tranforms low-FPS, blurry videos into high-FPS sequences with fine-grained temporal details. Our findings highlight time as a manipulable, perceptual dimension in video learning, opening doors to temporally controllable video generation, temporal forensics detection, and potentially richer world-models that understand how events unfold over time.
匹配关键词: audio language model
---

[ACADEMIC - ARXIV]
标题: Temporal Taskification in Streaming Continual Learning: A Source of Evaluation Instability
作者: Nicolae Filat, Ahmed Hussain, Konstantinos Kalogiannis, Elena Burceanu
链接: https://arxiv.org/abs/2604.21930v1
完整摘要: Streaming Continual Learning (CL) typically converts a continuous stream into a sequence of discrete tasks through temporal partitioning. We argue that this temporal taskification step is not a neutral preprocessing choice, but a structural component of evaluation: different valid splits of the same stream can induce different CL regimes and therefore different benchmark conclusions. To study this effect, we introduce a taskification-level framework based on plasticity and stability profiles, a profile distance between taskifications, and Boundary-Profile Sensitivity (BPS), which diagnoses how strongly small boundary perturbations alter the induced regime before any CL model is trained. We evaluate continual finetuning, Experience Replay, Elastic Weight Consolidation, and Learning without Forgetting on network traffic forecasting with CESNET-Timeseries24, keeping the stream, model, and training budget fixed while varying only the temporal taskification. Across 9-, 30-, and 44-day splits, we observe substantial changes in forecasting error, forgetting, and backward transfer, showing that taskification alone can materially affect CL evaluation. We further find that shorter taskifications induce noisier distribution-level patterns, larger structural distances, and higher BPS, indicating greater sensitivity to boundary perturbations. These results show that benchmark conclusions in streaming CL depend not only on the learner and the data stream, but also on how that stream is taskified, motivating temporal taskification as a first-class evaluation variable.
匹配关键词: audio language model
---

[ACADEMIC - ARXIV]
标题: Evaluation of Automatic Speech Recognition Using Generative Large Language Models
作者: Thibault Bañeras-Roux, Shashi Kumar, Driss Khalil, Sergio Burdisso, Petr Motlicek, Shiran Liu, Mickael Rouvier, Jane Wottawa, Richard Dufour
链接: https://arxiv.org/abs/2604.21928v1
完整摘要: Automatic Speech Recognition (ASR) is traditionally evaluated using Word Error Rate (WER), a metric that is insensitive to meaning. Embedding-based semantic metrics are better correlated with human perception, but decoder-based Large Language Models (LLMs) remain underexplored for this task. This paper evaluates their relevance through three approaches: (1) selecting the best hypothesis between two candidates, (2) computing semantic distance using generative embeddings, and (3) qualitative classification of errors. On the HATS dataset, the best LLMs achieve 92--94\% agreement with human annotators for hypothesis selection, compared to 63\% for WER, also outperforming semantic metrics. Embeddings from decoder-based LLMs show performance comparable to encoder models. Finally, LLMs offer a promising direction for interpretable and semantic ASR evaluation.
匹配关键词: audio language model
---

[ACADEMIC - ARXIV]
标题: Fine-Tuning Regimes Define Distinct Continual Learning Problems
作者: Paul-Tiberiu Iordache, Elena Burceanu
链接: https://arxiv.org/abs/2604.21927v1
完整摘要: Continual learning (CL) studies how models acquire tasks sequentially while retaining previously learned knowledge. Despite substantial progress in benchmarking CL methods, comparative evaluations typically keep the fine-tuning regime fixed. In this paper, we argue that the fine-tuning regime, defined by the trainable parameter subspace, is itself a key evaluation variable. We formalize adaptation regimes as projected optimization over fixed trainable subspaces, showing that changing the trainable depth alters the effective update signal through which both current task fitting and knowledge preservation operate. This analysis motivates the hypothesis that method comparisons need not be invariant across regimes. We test this hypothesis in task incremental CL, five trainable depth regimes, and four standard methods: online EWC, LwF, SI, and GEM. Across five benchmark datasets, namely MNIST, Fashion MNIST, KMNIST, QMNIST, and CIFAR-100, and across 11 task orders per dataset, we find that the relative ranking of methods is not consistently preserved across regimes. We further show that deeper adaptation regimes are associated with larger update magnitudes, higher forgetting, and a stronger relationship between the two. These results show that comparative conclusions in CL can depend strongly on the chosen fine-tuning regime, motivating regime-aware evaluation protocols that treat trainable depth as an explicit experimental factor.
匹配关键词: audio language model
---

[ACADEMIC - ARXIV]
标题: Seeing Without Eyes: 4D Human-Scene Understanding from Wearable IMUs
作者: Hao-Yu Hsu, Tianhang Cheng, Jing Wen, Alexander G. Schwing, Shenlong Wang
链接: https://arxiv.org/abs/2604.21926v1
完整摘要: Understanding human activities and their surrounding environments typically relies on visual perception, yet cameras pose persistent challenges in privacy, safety, energy efficiency, and scalability. We explore an alternative: 4D perception without vision. Its goal is to reconstruct human motion and 3D scene layouts purely from everyday wearable sensors. For this we introduce IMU-to-4D, a framework that repurposes large language models for non-visual spatiotemporal understanding of human-scene dynamics. IMU-to-4D uses data from a few inertial sensors from earbuds, watches, or smartphones and predicts detailed 4D human motion together with coarse scene structure. Experiments across diverse human-scene datasets show that IMU-to-4D yields more coherent and temporally stable results than SoTA cascaded pipelines, suggesting wearable motion sensors alone can support rich 4D understanding.
匹配关键词: audio language model
---

[ACADEMIC - ARXIV]
标题: Seeing Fast and Slow: Learning the Flow of Time in Videos
作者: Yen-Siang Wu, Rundong Luo, Jingsen Zhu, Tao Tu, Ali Farhadi, Matthew Wallingford, Yu-Chiang Frank Wang, Steve Marschner, Wei-Chiu Ma
链接: https://arxiv.org/abs/2604.21931v1
完整摘要: How can we tell whether a video has been sped up or slowed down? How can we generate videos at different speeds? Although videos have been central to modern computer vision research, little attention has been paid to perceiving and controlling the passage of time. In this paper, we study time as a learnable visual concept and develop models for reasoning about and manipulating the flow of time in videos. We first exploit the multimodal cues and temporal structure naturally present in videos to learn, in a self-supervised manner, to detect speed changes and estimate playback speed. We then show that these learned temporal reasoning models enable us to curate the largest slow-motion video dataset to date from noisy in-the-wild sources. Such slow-motion footage, typically filmed by high-speed cameras, contains substantially richer temporal detail than standard videos. Using this data, we further develop models capable of temporal control, including speed-conditioned video generation, which produces motion at specified playback speed, and temporal super-resolution, which tranforms low-FPS, blurry videos into high-FPS sequences with fine-grained temporal details. Our findings highlight time as a manipulable, perceptual dimension in video learning, opening doors to temporally controllable video generation, temporal forensics detection, and potentially richer world-models that understand how events unfold over time.
匹配关键词: voice generation
---

[ACADEMIC - ARXIV]
标题: Evaluation of Automatic Speech Recognition Using Generative Large Language Models
作者: Thibault Bañeras-Roux, Shashi Kumar, Driss Khalil, Sergio Burdisso, Petr Motlicek, Shiran Liu, Mickael Rouvier, Jane Wottawa, Richard Dufour
链接: https://arxiv.org/abs/2604.21928v1
完整摘要: Automatic Speech Recognition (ASR) is traditionally evaluated using Word Error Rate (WER), a metric that is insensitive to meaning. Embedding-based semantic metrics are better correlated with human perception, but decoder-based Large Language Models (LLMs) remain underexplored for this task. This paper evaluates their relevance through three approaches: (1) selecting the best hypothesis between two candidates, (2) computing semantic distance using generative embeddings, and (3) qualitative classification of errors. On the HATS dataset, the best LLMs achieve 92--94\% agreement with human annotators for hypothesis selection, compared to 63\% for WER, also outperforming semantic metrics. Embeddings from decoder-based LLMs show performance comparable to encoder models. Finally, LLMs offer a promising direction for interpretable and semantic ASR evaluation.
匹配关键词: voice generation
---

[ACADEMIC - ARXIV]
标题: Long-Horizon Manipulation via Trace-Conditioned VLA Planning
作者: Isabella Liu, An-Chieh Cheng, Rui Yan, Geng Chen, Ri-Zhao Qiu, Xueyan Zou, Sha Yi, Hongxu Yin, Xiaolong Wang, Sifei Liu
链接: https://arxiv.org/abs/2604.21924v1
完整摘要: Long-horizon manipulation remains challenging for vision-language-action (VLA) policies: real tasks are multi-step, progress-dependent, and brittle to compounding execution errors. We present LoHo-Manip, a modular framework that scales short-horizon VLA execution to long-horizon instruction following via a dedicated task-management VLM. The manager is decoupled from the executor and is invoked in a receding-horizon manner: given the current observation, it predicts a progress-aware remaining plan that combines (i) a subtask sequence with an explicit done + remaining split as lightweight language memory, and (ii) a visual trace -- a compact 2D keypoint trajectory prompt specifying where to go and what to approach next. The executor VLA is adapted to condition on the rendered trace, thereby turning long-horizon decision-making into repeated local control by following the trace. Crucially, predicting the remaining plan at each step yields an implicit closed loop: failed steps persist in subsequent outputs, and traces update accordingly, enabling automatic continuation and replanning without hand-crafted recovery logic or brittle visual-history buffers. Extensive experiments spanning embodied planning, long-horizon reasoning, trajectory prediction, and end-to-end manipulation in simulation and on a real Franka robot demonstrate strong gains in long-horizon success, robustness, and out-of-distribution generalization. Project page: https://www.liuisabella.com/LoHoManip
匹配关键词: voice generation
---

[ACADEMIC - ARXIV]
标题: The Sample Complexity of Multicalibration
作者: Natalie Collina, Jiuyao Lu, Georgy Noarov, Aaron Roth
链接: https://arxiv.org/abs/2604.21923v1
完整摘要: We study the minimax sample complexity of multicalibration in the batch setting. A learner observes $n$ i.i.d. samples from an unknown distribution and must output a (possibly randomized) predictor whose population multicalibration error, measured by Expected Calibration Error (ECE), is at most $\varepsilon$ with respect to a given family of groups. For every fixed $κ> 0$, in the regime $|G|\le \varepsilon^{-κ}$, we prove that $\widetildeΘ(\varepsilon^{-3})$ samples are necessary and sufficient, up to polylogarithmic factors. The lower bound holds even for randomized predictors, and the upper bound is realized by a randomized predictor obtained via an online-to-batch reduction. This separates the sample complexity of multicalibration from that of marginal calibration, which scales as $\widetildeΘ(\varepsilon^{-2})$, and shows that mean-ECE multicalibration is as difficult in the batch setting as it is in the online setting, in contrast to marginal calibration which is strictly more difficult in the online setting. In contrast we observe that for $κ= 0$, the sample complexity of multicalibration remains $\widetildeΘ(\varepsilon^{-2})$ exhibiting a sharp threshold phenomenon. More generally, we establish matching upper and lower bounds, up to polylogarithmic factors, for a weighted $L_p$ multicalibration metric for all $1 \le p \le 2$, with optimal exponent $3/p$. We also extend the lower-bound template to a regular class of elicitable properties, and combine it with the online upper bounds of Hu et al. (2025) to obtain matching bounds for calibrating properties including expectiles and bounded-density quantiles.
匹配关键词: voice generation
---

[ACADEMIC - ARXIV]
标题: Context Unrolling in Omni Models
作者: Ceyuan Yang, Zhijie Lin, Yang Zhao, Fei Xiao, Hao He, Qi Zhao, Chaorui Deng, Kunchang Li, Zihan Ding, Yuwei Guo, Fuyun Wang, Fangqi Zhu, Xiaonan Nie, Shenhan Zhu, Shanchuan Lin, Hongsheng Li, Weilin Huang, Guang Shi, Haoqi Fan
链接: https://arxiv.org/abs/2604.21921v1
完整摘要: We present Omni, a unified multimodal model natively trained on diverse modalities, including text, images, videos, 3D geometry, and hidden representations. We find that such training enables Context Unrolling, where the model explicitly reasons across multiple modal representations before producing predictions. This process enables the model to aggregate complementary information across heterogeneous modalities, facilitating a more faithful approximation of the shared multimodal knowledge manifold and improving downstream reasoning fidelity. As a result, Omni achieves strong performance on both multimodal generation and understanding benchmarks, while demonstrating advanced multimodal reasoning capabilities, including in-context generation of text, image, video, and 3D geometry.
匹配关键词: voice generation
---

[ACADEMIC - ARXIV]
标题: Long-Horizon Manipulation via Trace-Conditioned VLA Planning
作者: Isabella Liu, An-Chieh Cheng, Rui Yan, Geng Chen, Ri-Zhao Qiu, Xueyan Zou, Sha Yi, Hongxu Yin, Xiaolong Wang, Sifei Liu
链接: https://arxiv.org/abs/2604.21924v1
完整摘要: Long-horizon manipulation remains challenging for vision-language-action (VLA) policies: real tasks are multi-step, progress-dependent, and brittle to compounding execution errors. We present LoHo-Manip, a modular framework that scales short-horizon VLA execution to long-horizon instruction following via a dedicated task-management VLM. The manager is decoupled from the executor and is invoked in a receding-horizon manner: given the current observation, it predicts a progress-aware remaining plan that combines (i) a subtask sequence with an explicit done + remaining split as lightweight language memory, and (ii) a visual trace -- a compact 2D keypoint trajectory prompt specifying where to go and what to approach next. The executor VLA is adapted to condition on the rendered trace, thereby turning long-horizon decision-making into repeated local control by following the trace. Crucially, predicting the remaining plan at each step yields an implicit closed loop: failed steps persist in subsequent outputs, and traces update accordingly, enabling automatic continuation and replanning without hand-crafted recovery logic or brittle visual-history buffers. Extensive experiments spanning embodied planning, long-horizon reasoning, trajectory prediction, and end-to-end manipulation in simulation and on a real Franka robot demonstrate strong gains in long-horizon success, robustness, and out-of-distribution generalization. Project page: https://www.liuisabella.com/LoHoManip
匹配关键词: robotics
---

[ACADEMIC - ARXIV]
标题: VistaBot: View-Robust Robot Manipulation via Spatiotemporal-Aware View Synthesis
作者: Songen Gu, Yuhang Zheng, Weize Li, Yupeng Zheng, Yating Feng, Xiang Li, Yilun Chen, Pengfei Li, Wenchao Ding
链接: https://arxiv.org/abs/2604.21914v1
完整摘要: Recently, end-to-end robotic manipulation models have gained significant attention for their generalizability and scalability. However, they often suffer from limited robustness to camera viewpoint changes when training with a fixed camera. In this paper, we propose VistaBot, a novel framework that integrates feed-forward geometric models with video diffusion models to achieve view-robust closed-loop manipulation without requiring camera calibration at test time. Our approach consists of three key components: 4D geometry estimation, view synthesis latent extraction, and latent action learning. VistaBot is integrated into both action-chunking (ACT) and diffusion-based ($π_0$) policies and evaluated across simulation and real-world tasks. We further introduce the View Generalization Score (VGS) as a new metric for comprehensive evaluation of cross-view generalization. Results show that VistaBot improves VGS by 2.79$\times$ and 2.63$\times$ over ACT and $π_0$, respectively, while also achieving high-quality novel view synthesis. Our contributions include a geometry-aware synthesis model, a latent action planner, a new benchmark metric, and extensive validation across diverse environments. The code and models will be made publicly available.
匹配关键词: robotics
---

[ACADEMIC - ARXIV]
标题: Task-Driven Co-Design of Heterogeneous Multi-Robot Systems
作者: Maximilian Stralz, Meshal Alharbi, Yujun Huang, Gioele Zardini
链接: https://arxiv.org/abs/2604.21894v1
完整摘要: Designing multi-agent robotic systems requires reasoning across tightly coupled decisions spanning heterogeneous domains, including robot design, fleet composition, and planning. Much effort has been devoted to isolated improvements in these domains, whereas system-level co-design considering trade-offs and task requirements remains underexplored. In this work, we present a formal and compositional framework for the task-driven co-design of heterogeneous multi-robot systems. Building on a monotone co-design theory, we introduce general abstractions of robots, fleets, planners, executors, and evaluators as interconnected design problems with well-defined interfaces that are agnostic to both implementations and tasks. This structure enables efficient joint optimization of robot design, fleet composition, and planning under task-specific performance constraints. A series of case studies demonstrates the capabilities of the framework. Various component models can be seamlessly incorporated, including new robot types, task profiles, and probabilistic sensing objectives, while non-obvious design alternatives are systematically uncovered with optimality guarantees. The results highlight the flexibility, scalability, and interpretability of the proposed approach, and illustrate how formal co-design enables principled reasoning about complex heterogeneous multi-robot systems.
匹配关键词: robotics
---

[ACADEMIC - ARXIV]
标题: Hi-WM: Human-in-the-World-Model for Scalable Robot Post-Training
作者: Yaxuan Li, Zhongyi Zhou, Yefei Chen, Yanjiang Guo, Jiaming Liu, Shanghang Zhang, Jianyu Chen, Yichen Zhu
链接: https://arxiv.org/abs/2604.21741v1
完整摘要: Post-training is essential for turning pretrained generalist robot policies into reliable task-specific controllers, but existing human-in-the-loop pipelines remain tied to physical execution: each correction requires robot time, scene setup, resets, and operator supervision in the real world. Meanwhile, action-conditioned world models have been studied mainly for imagination, synthetic data generation, and policy evaluation. We propose \textbf{Human-in-the-World-Model (Hi-WM)}, a post-training framework that uses a learned world model as a reusable corrective substrate for failure-targeted policy improvement. A policy is first rolled out in closed loop inside the world model; when the rollout becomes incorrect or failure-prone, a human intervenes directly in the model to provide short corrective actions. Hi-WM caches intermediate states and supports rollback and branching, allowing a single failure state to be reused for multiple corrective continuations and yielding dense supervision around behaviors that the base policy handles poorly. The resulting corrective trajectories are then added back to the training set for post-training. We evaluate Hi-WM on three real-world manipulation tasks spanning both rigid and deformable object interaction, and on two policy backbones. Hi-WM improves real-world success by 37.9 points on average over the base policy and by 19.0 points over a world-model closed-loop baseline, while world-model evaluation correlates strongly with real-world performance (r = 0.953). These results suggest that world models can serve not only as generators or evaluators, but also as effective corrective substrates for scalable robot post-training.
匹配关键词: robotics
---

[ACADEMIC - ARXIV]
标题: A Case Study in Recovery of Drones using Discrete-Event Systems
作者: Liam P. Burns, Dayse M. Cavalcanti, Felipe G. Cabral, Max H. de Queiroz, Melissa Greeff, Publio M. M. Lima, Karen Rudie
链接: https://arxiv.org/abs/2604.21740v1
完整摘要: Discrete-event systems and supervisory control theory provide a rigorous framework for specifying correct-by-construction behavior. However, their practical application to swarm robotics remains largely underexplored. In this paper, we investigate a topological recovery method based on discrete-event-systems within a swarm robotics context. We propose a hybrid architecture that combines a high-level discrete event systems supervisor with a low-level continuous controller, allowing lost drones to safely recover from fault or attack events and re-enter a controlled region. The method is demonstrated using ten simulated UAVs in the py-bullet-drones framework. We show recovery performance across four distinct scenarios, each with varying initial state estimates. Additionally, we introduce a secondary recovery supervisor that manages the regrouping process for a drone after it has re-entered the operational region.
匹配关键词: robotics
---

[ACADEMIC - ARXIV]
标题: Long-Horizon Manipulation via Trace-Conditioned VLA Planning
作者: Isabella Liu, An-Chieh Cheng, Rui Yan, Geng Chen, Ri-Zhao Qiu, Xueyan Zou, Sha Yi, Hongxu Yin, Xiaolong Wang, Sifei Liu
链接: https://arxiv.org/abs/2604.21924v1
完整摘要: Long-horizon manipulation remains challenging for vision-language-action (VLA) policies: real tasks are multi-step, progress-dependent, and brittle to compounding execution errors. We present LoHo-Manip, a modular framework that scales short-horizon VLA execution to long-horizon instruction following via a dedicated task-management VLM. The manager is decoupled from the executor and is invoked in a receding-horizon manner: given the current observation, it predicts a progress-aware remaining plan that combines (i) a subtask sequence with an explicit done + remaining split as lightweight language memory, and (ii) a visual trace -- a compact 2D keypoint trajectory prompt specifying where to go and what to approach next. The executor VLA is adapted to condition on the rendered trace, thereby turning long-horizon decision-making into repeated local control by following the trace. Crucially, predicting the remaining plan at each step yields an implicit closed loop: failed steps persist in subsequent outputs, and traces update accordingly, enabling automatic continuation and replanning without hand-crafted recovery logic or brittle visual-history buffers. Extensive experiments spanning embodied planning, long-horizon reasoning, trajectory prediction, and end-to-end manipulation in simulation and on a real Franka robot demonstrate strong gains in long-horizon success, robustness, and out-of-distribution generalization. Project page: https://www.liuisabella.com/LoHoManip
匹配关键词: humanoid robot
---

[ACADEMIC - ARXIV]
标题: VistaBot: View-Robust Robot Manipulation via Spatiotemporal-Aware View Synthesis
作者: Songen Gu, Yuhang Zheng, Weize Li, Yupeng Zheng, Yating Feng, Xiang Li, Yilun Chen, Pengfei Li, Wenchao Ding
链接: https://arxiv.org/abs/2604.21914v1
完整摘要: Recently, end-to-end robotic manipulation models have gained significant attention for their generalizability and scalability. However, they often suffer from limited robustness to camera viewpoint changes when training with a fixed camera. In this paper, we propose VistaBot, a novel framework that integrates feed-forward geometric models with video diffusion models to achieve view-robust closed-loop manipulation without requiring camera calibration at test time. Our approach consists of three key components: 4D geometry estimation, view synthesis latent extraction, and latent action learning. VistaBot is integrated into both action-chunking (ACT) and diffusion-based ($π_0$) policies and evaluated across simulation and real-world tasks. We further introduce the View Generalization Score (VGS) as a new metric for comprehensive evaluation of cross-view generalization. Results show that VistaBot improves VGS by 2.79$\times$ and 2.63$\times$ over ACT and $π_0$, respectively, while also achieving high-quality novel view synthesis. Our contributions include a geometry-aware synthesis model, a latent action planner, a new benchmark metric, and extensive validation across diverse environments. The code and models will be made publicly available.
匹配关键词: humanoid robot
---

[ACADEMIC - ARXIV]
标题: Task-Driven Co-Design of Heterogeneous Multi-Robot Systems
作者: Maximilian Stralz, Meshal Alharbi, Yujun Huang, Gioele Zardini
链接: https://arxiv.org/abs/2604.21894v1
完整摘要: Designing multi-agent robotic systems requires reasoning across tightly coupled decisions spanning heterogeneous domains, including robot design, fleet composition, and planning. Much effort has been devoted to isolated improvements in these domains, whereas system-level co-design considering trade-offs and task requirements remains underexplored. In this work, we present a formal and compositional framework for the task-driven co-design of heterogeneous multi-robot systems. Building on a monotone co-design theory, we introduce general abstractions of robots, fleets, planners, executors, and evaluators as interconnected design problems with well-defined interfaces that are agnostic to both implementations and tasks. This structure enables efficient joint optimization of robot design, fleet composition, and planning under task-specific performance constraints. A series of case studies demonstrates the capabilities of the framework. Various component models can be seamlessly incorporated, including new robot types, task profiles, and probabilistic sensing objectives, while non-obvious design alternatives are systematically uncovered with optimality guarantees. The results highlight the flexibility, scalability, and interpretability of the proposed approach, and illustrate how formal co-design enables principled reasoning about complex heterogeneous multi-robot systems.
匹配关键词: humanoid robot
---

[ACADEMIC - ARXIV]
标题: Hi-WM: Human-in-the-World-Model for Scalable Robot Post-Training
作者: Yaxuan Li, Zhongyi Zhou, Yefei Chen, Yanjiang Guo, Jiaming Liu, Shanghang Zhang, Jianyu Chen, Yichen Zhu
链接: https://arxiv.org/abs/2604.21741v1
完整摘要: Post-training is essential for turning pretrained generalist robot policies into reliable task-specific controllers, but existing human-in-the-loop pipelines remain tied to physical execution: each correction requires robot time, scene setup, resets, and operator supervision in the real world. Meanwhile, action-conditioned world models have been studied mainly for imagination, synthetic data generation, and policy evaluation. We propose \textbf{Human-in-the-World-Model (Hi-WM)}, a post-training framework that uses a learned world model as a reusable corrective substrate for failure-targeted policy improvement. A policy is first rolled out in closed loop inside the world model; when the rollout becomes incorrect or failure-prone, a human intervenes directly in the model to provide short corrective actions. Hi-WM caches intermediate states and supports rollback and branching, allowing a single failure state to be reused for multiple corrective continuations and yielding dense supervision around behaviors that the base policy handles poorly. The resulting corrective trajectories are then added back to the training set for post-training. We evaluate Hi-WM on three real-world manipulation tasks spanning both rigid and deformable object interaction, and on two policy backbones. Hi-WM improves real-world success by 37.9 points on average over the base policy and by 19.0 points over a world-model closed-loop baseline, while world-model evaluation correlates strongly with real-world performance (r = 0.953). These results suggest that world models can serve not only as generators or evaluators, but also as effective corrective substrates for scalable robot post-training.
匹配关键词: humanoid robot
---

[ACADEMIC - ARXIV]
标题: A Case Study in Recovery of Drones using Discrete-Event Systems
作者: Liam P. Burns, Dayse M. Cavalcanti, Felipe G. Cabral, Max H. de Queiroz, Melissa Greeff, Publio M. M. Lima, Karen Rudie
链接: https://arxiv.org/abs/2604.21740v1
完整摘要: Discrete-event systems and supervisory control theory provide a rigorous framework for specifying correct-by-construction behavior. However, their practical application to swarm robotics remains largely underexplored. In this paper, we investigate a topological recovery method based on discrete-event-systems within a swarm robotics context. We propose a hybrid architecture that combines a high-level discrete event systems supervisor with a low-level continuous controller, allowing lost drones to safely recover from fault or attack events and re-enter a controlled region. The method is demonstrated using ten simulated UAVs in the py-bullet-drones framework. We show recovery performance across four distinct scenarios, each with varying initial state estimates. Additionally, we introduce a secondary recovery supervisor that manages the regrouping process for a drone after it has re-entered the operational region.
匹配关键词: humanoid robot
---

[ACADEMIC - ARXIV]
标题: Seeing Fast and Slow: Learning the Flow of Time in Videos
作者: Yen-Siang Wu, Rundong Luo, Jingsen Zhu, Tao Tu, Ali Farhadi, Matthew Wallingford, Yu-Chiang Frank Wang, Steve Marschner, Wei-Chiu Ma
链接: https://arxiv.org/abs/2604.21931v1
完整摘要: How can we tell whether a video has been sped up or slowed down? How can we generate videos at different speeds? Although videos have been central to modern computer vision research, little attention has been paid to perceiving and controlling the passage of time. In this paper, we study time as a learnable visual concept and develop models for reasoning about and manipulating the flow of time in videos. We first exploit the multimodal cues and temporal structure naturally present in videos to learn, in a self-supervised manner, to detect speed changes and estimate playback speed. We then show that these learned temporal reasoning models enable us to curate the largest slow-motion video dataset to date from noisy in-the-wild sources. Such slow-motion footage, typically filmed by high-speed cameras, contains substantially richer temporal detail than standard videos. Using this data, we further develop models capable of temporal control, including speed-conditioned video generation, which produces motion at specified playback speed, and temporal super-resolution, which tranforms low-FPS, blurry videos into high-FPS sequences with fine-grained temporal details. Our findings highlight time as a manipulable, perceptual dimension in video learning, opening doors to temporally controllable video generation, temporal forensics detection, and potentially richer world-models that understand how events unfold over time.
匹配关键词: manipulation
---

[ACADEMIC - ARXIV]
标题: Long-Horizon Manipulation via Trace-Conditioned VLA Planning
作者: Isabella Liu, An-Chieh Cheng, Rui Yan, Geng Chen, Ri-Zhao Qiu, Xueyan Zou, Sha Yi, Hongxu Yin, Xiaolong Wang, Sifei Liu
链接: https://arxiv.org/abs/2604.21924v1
完整摘要: Long-horizon manipulation remains challenging for vision-language-action (VLA) policies: real tasks are multi-step, progress-dependent, and brittle to compounding execution errors. We present LoHo-Manip, a modular framework that scales short-horizon VLA execution to long-horizon instruction following via a dedicated task-management VLM. The manager is decoupled from the executor and is invoked in a receding-horizon manner: given the current observation, it predicts a progress-aware remaining plan that combines (i) a subtask sequence with an explicit done + remaining split as lightweight language memory, and (ii) a visual trace -- a compact 2D keypoint trajectory prompt specifying where to go and what to approach next. The executor VLA is adapted to condition on the rendered trace, thereby turning long-horizon decision-making into repeated local control by following the trace. Crucially, predicting the remaining plan at each step yields an implicit closed loop: failed steps persist in subsequent outputs, and traces update accordingly, enabling automatic continuation and replanning without hand-crafted recovery logic or brittle visual-history buffers. Extensive experiments spanning embodied planning, long-horizon reasoning, trajectory prediction, and end-to-end manipulation in simulation and on a real Franka robot demonstrate strong gains in long-horizon success, robustness, and out-of-distribution generalization. Project page: https://www.liuisabella.com/LoHoManip
匹配关键词: manipulation
---

[ACADEMIC - ARXIV]
标题: VistaBot: View-Robust Robot Manipulation via Spatiotemporal-Aware View Synthesis
作者: Songen Gu, Yuhang Zheng, Weize Li, Yupeng Zheng, Yating Feng, Xiang Li, Yilun Chen, Pengfei Li, Wenchao Ding
链接: https://arxiv.org/abs/2604.21914v1
完整摘要: Recently, end-to-end robotic manipulation models have gained significant attention for their generalizability and scalability. However, they often suffer from limited robustness to camera viewpoint changes when training with a fixed camera. In this paper, we propose VistaBot, a novel framework that integrates feed-forward geometric models with video diffusion models to achieve view-robust closed-loop manipulation without requiring camera calibration at test time. Our approach consists of three key components: 4D geometry estimation, view synthesis latent extraction, and latent action learning. VistaBot is integrated into both action-chunking (ACT) and diffusion-based ($π_0$) policies and evaluated across simulation and real-world tasks. We further introduce the View Generalization Score (VGS) as a new metric for comprehensive evaluation of cross-view generalization. Results show that VistaBot improves VGS by 2.79$\times$ and 2.63$\times$ over ACT and $π_0$, respectively, while also achieving high-quality novel view synthesis. Our contributions include a geometry-aware synthesis model, a latent action planner, a new benchmark metric, and extensive validation across diverse environments. The code and models will be made publicly available.
匹配关键词: manipulation
---

[ACADEMIC - ARXIV]
标题: Interpretable facial dynamics as behavioral and perceptual traces of deepfakes
作者: Timothy Joseph Murphy, Jennifer Cook, Hélio Clemente José Cuve
链接: https://arxiv.org/abs/2604.21760v1
完整摘要: Deepfake detection research has largely converged on deep learning approaches that, despite strong benchmark performance, offer limited insight into what distinguishes real from manipulated facial behavior. This study presents an interpretable alternative grounded in bio-behavioral features of facial dynamics and evaluates how computational detection strategies relate to human perceptual judgments. We identify core low-dimensional patterns of facial movement, from which temporal features characterizing spatiotemporal structure were derived. Traditional machine learning classifiers trained on these features achieved modest but significant above-chance deepfake classification, driven by higher-order temporal irregularities that were more pronounced in manipulated than real facial dynamics. Notably, detection was substantially more accurate for videos containing emotive expressions than those without. An emotional valence classification analysis further indicated that emotive signals are systematically degraded in deepfakes, explaining the differential impact of emotive dynamics on detection. Furthermore, we provide an additional and often overlooked dimension of explainability by assessing the relationship between model decisions and human perceptual detection. Model and human judgments converged for emotive but diverged for non-emotive videos, and even where outputs aligned, underlying detection strategies differed. These findings demonstrate that face-swapped deepfakes carry a measurable behavioral fingerprint, most salient during emotional expression. Additionally, model-human comparisons suggest that interpretable computational features and human perception may offer complementary rather than redundant routes to detection.
匹配关键词: manipulation
---

[ACADEMIC - ARXIV]
标题: Hi-WM: Human-in-the-World-Model for Scalable Robot Post-Training
作者: Yaxuan Li, Zhongyi Zhou, Yefei Chen, Yanjiang Guo, Jiaming Liu, Shanghang Zhang, Jianyu Chen, Yichen Zhu
链接: https://arxiv.org/abs/2604.21741v1
完整摘要: Post-training is essential for turning pretrained generalist robot policies into reliable task-specific controllers, but existing human-in-the-loop pipelines remain tied to physical execution: each correction requires robot time, scene setup, resets, and operator supervision in the real world. Meanwhile, action-conditioned world models have been studied mainly for imagination, synthetic data generation, and policy evaluation. We propose \textbf{Human-in-the-World-Model (Hi-WM)}, a post-training framework that uses a learned world model as a reusable corrective substrate for failure-targeted policy improvement. A policy is first rolled out in closed loop inside the world model; when the rollout becomes incorrect or failure-prone, a human intervenes directly in the model to provide short corrective actions. Hi-WM caches intermediate states and supports rollback and branching, allowing a single failure state to be reused for multiple corrective continuations and yielding dense supervision around behaviors that the base policy handles poorly. The resulting corrective trajectories are then added back to the training set for post-training. We evaluate Hi-WM on three real-world manipulation tasks spanning both rigid and deformable object interaction, and on two policy backbones. Hi-WM improves real-world success by 37.9 points on average over the base policy and by 19.0 points over a world-model closed-loop baseline, while world-model evaluation correlates strongly with real-world performance (r = 0.953). These results suggest that world models can serve not only as generators or evaluators, but also as effective corrective substrates for scalable robot post-training.
匹配关键词: manipulation
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
标题: ProMMSearchAgent: A Generalizable Multimodal Search Agent Trained with Process-Oriented Rewards
作者: Wentao Yan, Shengqin Wang, Huichi Zhou, Yihang Chen, Kun Shao, Yuan Xie, Zhizhong Zhang
链接: https://arxiv.org/abs/2604.20486v1
完整摘要: Training multimodal agents via reinforcement learning for knowledge-intensive visual reasoning is fundamentally hindered by the extreme sparsity of outcome-based supervision and the unpredictability of live web environments. To resolve these algorithmic and environmental bottlenecks, we introduce ProMMSearchAgent, establishing a novel Sim-to-Real training paradigm for multimodal search. We decouple policy learning into a deterministic, local static sandbox. Crucially, to learn effectively within this constrained environment, we propose an introspective process-oriented reward. By probing the agent's own parametric knowledge boundaries, we generate dense behavioral metadata that explicitly rewards the correct cognitive decision, initiating a multimodal or text search only when visually or factually uncertain. Extensive experiments demonstrate that our locally-trained policy transfers zero-shot to the live Google Search API. ProMMSearchAgent achieves new SOTA performance, outperforming MMSearch-R1 by +5.1% on FVQA-test, +6.3% on InfoSeek, and +11.3% on MMSearch.
匹配关键词: sim-to-real
---

[ACADEMIC - ARXIV]
标题: Learning Hybrid-Control Policies for High-Precision In-Contact Manipulation Under Uncertainty
作者: Hunter L. Brown, Geoffrey Hollinger, Stefan Lee
链接: https://arxiv.org/abs/2604.19677v1
完整摘要: Reinforcement learning-based control policies have been frequently demonstrated to be more effective than analytical techniques for many manipulation tasks. Commonly, these methods learn neural control policies that predict end-effector pose changes directly from observed state information. For tasks like inserting delicate connectors which induce force constraints, pose-based policies have limited explicit control over force and rely on carefully tuned low-level controllers to avoid executing damaging actions. In this work, we present hybrid position-force control policies that learn to dynamically select when to use force or position control in each control dimension. To improve learning efficiency of these policies, we introduce Mode-Aware Training for Contact Handling (MATCH) which adjusts policy action probabilities to explicitly mirror the mode selection behavior in hybrid control. We validate MATCH's learned policy effectiveness using fragile peg-in-hole tasks under extreme localization uncertainty. We find MATCH substantially outperforms pose-control policies -- solving these tasks with up to 10% higher success rates and 5x fewer peg breaks than pose-only policies under common types of state estimation error. MATCH also demonstrates data efficiency equal to pose-control policies, despite learning in a larger and more complex action space. In over 1600 sim-to-real experiments, we find MATCH succeeds twice as often as pose policies in high noise settings (33% vs.~68%) and applies ~30% less force on average compared to variable impedance policies on a Franka FR3 in laboratory conditions.
匹配关键词: sim-to-real
---

[ACADEMIC - ARXIV]
标题: Multi-Gait Learning for Humanoid Robots Using Reinforcement Learning with Selective Adversarial Motion Prior
作者: Yuanye Wu, Keyi Wang, Linqi Ye, Boyang Xing
链接: https://arxiv.org/abs/2604.19102v1
完整摘要: Learning diverse locomotion skills for humanoid robots in a unified reinforcement learning framework remains challenging due to the conflicting requirements of stability and dynamic expressiveness across different gaits. We present a multi-gait learning approach that enables a humanoid robot to master five distinct gaits -- walking, goose-stepping, running, stair climbing, and jumping -- using a consistent policy structure, action space, and reward formulation. The key contribution is a selective Adversarial Motion Prior (AMP) strategy: AMP is applied to periodic, stability-critical gaits (walking, goose-stepping, stair climbing) where it accelerates convergence and suppresses erratic behavior, while being deliberately omitted for highly dynamic gaits (running, jumping) where its regularization would over-constrain the motion. Policies are trained via PPO with domain randomization in simulation and deployed on a physical 12-DOF humanoid robot through zero-shot sim-to-real transfer. Quantitative comparisons demonstrate that selective AMP outperforms a uniform AMP policy across all five gaits, achieving faster convergence, lower tracking error, and higher success rates on stability-focused gaits without sacrificing the agility required for dynamic ones.
匹配关键词: sim-to-real
---

[ACADEMIC - ARXIV]
标题: Seeing Fast and Slow: Learning the Flow of Time in Videos
作者: Yen-Siang Wu, Rundong Luo, Jingsen Zhu, Tao Tu, Ali Farhadi, Matthew Wallingford, Yu-Chiang Frank Wang, Steve Marschner, Wei-Chiu Ma
链接: https://arxiv.org/abs/2604.21931v1
完整摘要: How can we tell whether a video has been sped up or slowed down? How can we generate videos at different speeds? Although videos have been central to modern computer vision research, little attention has been paid to perceiving and controlling the passage of time. In this paper, we study time as a learnable visual concept and develop models for reasoning about and manipulating the flow of time in videos. We first exploit the multimodal cues and temporal structure naturally present in videos to learn, in a self-supervised manner, to detect speed changes and estimate playback speed. We then show that these learned temporal reasoning models enable us to curate the largest slow-motion video dataset to date from noisy in-the-wild sources. Such slow-motion footage, typically filmed by high-speed cameras, contains substantially richer temporal detail than standard videos. Using this data, we further develop models capable of temporal control, including speed-conditioned video generation, which produces motion at specified playback speed, and temporal super-resolution, which tranforms low-FPS, blurry videos into high-FPS sequences with fine-grained temporal details. Our findings highlight time as a manipulable, perceptual dimension in video learning, opening doors to temporally controllable video generation, temporal forensics detection, and potentially richer world-models that understand how events unfold over time.
匹配关键词: world model
---

[ACADEMIC - ARXIV]
标题: Temporal Taskification in Streaming Continual Learning: A Source of Evaluation Instability
作者: Nicolae Filat, Ahmed Hussain, Konstantinos Kalogiannis, Elena Burceanu
链接: https://arxiv.org/abs/2604.21930v1
完整摘要: Streaming Continual Learning (CL) typically converts a continuous stream into a sequence of discrete tasks through temporal partitioning. We argue that this temporal taskification step is not a neutral preprocessing choice, but a structural component of evaluation: different valid splits of the same stream can induce different CL regimes and therefore different benchmark conclusions. To study this effect, we introduce a taskification-level framework based on plasticity and stability profiles, a profile distance between taskifications, and Boundary-Profile Sensitivity (BPS), which diagnoses how strongly small boundary perturbations alter the induced regime before any CL model is trained. We evaluate continual finetuning, Experience Replay, Elastic Weight Consolidation, and Learning without Forgetting on network traffic forecasting with CESNET-Timeseries24, keeping the stream, model, and training budget fixed while varying only the temporal taskification. Across 9-, 30-, and 44-day splits, we observe substantial changes in forecasting error, forgetting, and backward transfer, showing that taskification alone can materially affect CL evaluation. We further find that shorter taskifications induce noisier distribution-level patterns, larger structural distances, and higher BPS, indicating greater sensitivity to boundary perturbations. These results show that benchmark conclusions in streaming CL depend not only on the learner and the data stream, but also on how that stream is taskified, motivating temporal taskification as a first-class evaluation variable.
匹配关键词: world model
---

[ACADEMIC - ARXIV]
标题: Evaluation of Automatic Speech Recognition Using Generative Large Language Models
作者: Thibault Bañeras-Roux, Shashi Kumar, Driss Khalil, Sergio Burdisso, Petr Motlicek, Shiran Liu, Mickael Rouvier, Jane Wottawa, Richard Dufour
链接: https://arxiv.org/abs/2604.21928v1
完整摘要: Automatic Speech Recognition (ASR) is traditionally evaluated using Word Error Rate (WER), a metric that is insensitive to meaning. Embedding-based semantic metrics are better correlated with human perception, but decoder-based Large Language Models (LLMs) remain underexplored for this task. This paper evaluates their relevance through three approaches: (1) selecting the best hypothesis between two candidates, (2) computing semantic distance using generative embeddings, and (3) qualitative classification of errors. On the HATS dataset, the best LLMs achieve 92--94\% agreement with human annotators for hypothesis selection, compared to 63\% for WER, also outperforming semantic metrics. Embeddings from decoder-based LLMs show performance comparable to encoder models. Finally, LLMs offer a promising direction for interpretable and semantic ASR evaluation.
匹配关键词: world model
---

[ACADEMIC - ARXIV]
标题: Fine-Tuning Regimes Define Distinct Continual Learning Problems
作者: Paul-Tiberiu Iordache, Elena Burceanu
链接: https://arxiv.org/abs/2604.21927v1
完整摘要: Continual learning (CL) studies how models acquire tasks sequentially while retaining previously learned knowledge. Despite substantial progress in benchmarking CL methods, comparative evaluations typically keep the fine-tuning regime fixed. In this paper, we argue that the fine-tuning regime, defined by the trainable parameter subspace, is itself a key evaluation variable. We formalize adaptation regimes as projected optimization over fixed trainable subspaces, showing that changing the trainable depth alters the effective update signal through which both current task fitting and knowledge preservation operate. This analysis motivates the hypothesis that method comparisons need not be invariant across regimes. We test this hypothesis in task incremental CL, five trainable depth regimes, and four standard methods: online EWC, LwF, SI, and GEM. Across five benchmark datasets, namely MNIST, Fashion MNIST, KMNIST, QMNIST, and CIFAR-100, and across 11 task orders per dataset, we find that the relative ranking of methods is not consistently preserved across regimes. We further show that deeper adaptation regimes are associated with larger update magnitudes, higher forgetting, and a stronger relationship between the two. These results show that comparative conclusions in CL can depend strongly on the chosen fine-tuning regime, motivating regime-aware evaluation protocols that treat trainable depth as an explicit experimental factor.
匹配关键词: world model
---

[ACADEMIC - ARXIV]
标题: Seeing Without Eyes: 4D Human-Scene Understanding from Wearable IMUs
作者: Hao-Yu Hsu, Tianhang Cheng, Jing Wen, Alexander G. Schwing, Shenlong Wang
链接: https://arxiv.org/abs/2604.21926v1
完整摘要: Understanding human activities and their surrounding environments typically relies on visual perception, yet cameras pose persistent challenges in privacy, safety, energy efficiency, and scalability. We explore an alternative: 4D perception without vision. Its goal is to reconstruct human motion and 3D scene layouts purely from everyday wearable sensors. For this we introduce IMU-to-4D, a framework that repurposes large language models for non-visual spatiotemporal understanding of human-scene dynamics. IMU-to-4D uses data from a few inertial sensors from earbuds, watches, or smartphones and predicts detailed 4D human motion together with coarse scene structure. Experiments across diverse human-scene datasets show that IMU-to-4D yields more coherent and temporally stable results than SoTA cascaded pipelines, suggesting wearable motion sensors alone can support rich 4D understanding.
匹配关键词: world model
---

[ACADEMIC - ARXIV]
标题: From Research Question to Scientific Workflow: Leveraging Agentic AI for Science Automation
作者: Bartosz Balis, Michal Orzechowski, Piotr Kica, Michal Dygas, Michal Kuszewski
链接: https://arxiv.org/abs/2604.21910v1
完整摘要: Scientific workflow systems automate execution -- scheduling, fault tolerance, resource management -- but not the semantic translation that precedes it. Scientists still manually convert research questions into workflow specifications, a task requiring both domain knowledge and infrastructure expertise. We propose an agentic architecture that closes this gap through three layers: an LLM interprets natural language into structured intents (semantic layer); validated generators produce reproducible workflow DAGs (deterministic layer); and domain experts author ``Skills'': markdown documents encoding vocabulary mappings, parameter constraints, and optimization strategies (knowledge layer). This decomposition confines LLM non-determinism to intent extraction: identical intents always yield identical workflows. We implement and evaluate the architecture on the 1000 Genomes population genetics workflow and Hyperflow WMS running on Kubernetes. In an ablation study on 150 queries, Skills raise full-match intent accuracy from 44% to 83%; skill-driven deferred workflow generation reduces data transfer by 92\%; and the end-to-end pipeline completes queries on Kubernetes with LLM overhead below 15 seconds and cost under $0.001 per query.
匹配关键词: agent
---

[ACADEMIC - ARXIV]
标题: Nemobot Games: Crafting Strategic AI Gaming Agents for Interactive Learning with Large Language Models
作者: Chee Wei Tan, Yuchen Wang, Shangxin Guo
链接: https://arxiv.org/abs/2604.21896v1
完整摘要: This paper introduces a new paradigm for AI game programming, leveraging large language models (LLMs) to extend and operationalize Claude Shannon's taxonomy of game-playing machines. Central to this paradigm is Nemobot, an interactive agentic engineering environment that enables users to create, customize, and deploy LLM-powered game agents while actively engaging with AI-driven strategies. The LLM-based chatbot, integrated within Nemobot, demonstrates its capabilities across four distinct classes of games. For dictionary-based games, it compresses state-action mappings into efficient, generalized models for rapid adaptability. In rigorously solvable games, it employs mathematical reasoning to compute optimal strategies and generates human-readable explanations for its decisions. For heuristic-based games, it synthesizes strategies by combining insights from classical minimax algorithms (see, e.g., shannon1950chess) with crowd-sourced data. Finally, in learning-based games, it utilizes reinforcement learning with human feedback and self-critique to iteratively refine strategies through trial-and-error and imitation learning. Nemobot amplifies this framework by offering a programmable environment where users can experiment with tool-augmented generation and fine-tuning of strategic game agents. From strategic games to role-playing games, Nemobot demonstrates how AI agents can achieve a form of self-programming by integrating crowdsourced learning and human creativity to iteratively refine their own logic. This represents a step toward the long-term goal of self-programming AI.
匹配关键词: agent
---

[ACADEMIC - ARXIV]
标题: Task-Driven Co-Design of Heterogeneous Multi-Robot Systems
作者: Maximilian Stralz, Meshal Alharbi, Yujun Huang, Gioele Zardini
链接: https://arxiv.org/abs/2604.21894v1
完整摘要: Designing multi-agent robotic systems requires reasoning across tightly coupled decisions spanning heterogeneous domains, including robot design, fleet composition, and planning. Much effort has been devoted to isolated improvements in these domains, whereas system-level co-design considering trade-offs and task requirements remains underexplored. In this work, we present a formal and compositional framework for the task-driven co-design of heterogeneous multi-robot systems. Building on a monotone co-design theory, we introduce general abstractions of robots, fleets, planners, executors, and evaluators as interconnected design problems with well-defined interfaces that are agnostic to both implementations and tasks. This structure enables efficient joint optimization of robot design, fleet composition, and planning under task-specific performance constraints. A series of case studies demonstrates the capabilities of the framework. Various component models can be seamlessly incorporated, including new robot types, task profiles, and probabilistic sensing objectives, while non-obvious design alternatives are systematically uncovered with optimality guarantees. The results highlight the flexibility, scalability, and interpretability of the proposed approach, and illustrate how formal co-design enables principled reasoning about complex heterogeneous multi-robot systems.
匹配关键词: agent
---

[ACADEMIC - ARXIV]
标题: Transient Turn Injection: Exposing Stateless Multi-Turn Vulnerabilities in Large Language Models
作者: Naheed Rayhan, Sohely Jahan
链接: https://arxiv.org/abs/2604.21860v1
完整摘要: Large language models (LLMs) are increasingly integrated into sensitive workflows, raising the stakes for adversarial robustness and safety. This paper introduces Transient Turn Injection(TTI), a new multi-turn attack technique that systematically exploits stateless moderation by distributing adversarial intent across isolated interactions. TTI leverages automated attacker agents powered by large language models to iteratively test and evade policy enforcement in both commercial and open-source LLMs, marking a departure from conventional jailbreak approaches that typically depend on maintaining persistent conversational context. Our extensive evaluation across state-of-the-art models-including those from OpenAI, Anthropic, Google Gemini, Meta, and prominent open-source alternatives-uncovers significant variations in resilience to TTI attacks, with only select architectures exhibiting substantial inherent robustness. Our automated blackbox evaluation framework also uncovers previously unknown model specific vulnerabilities and attack surface patterns, especially within medical and high stakes domains. We further compare TTI against established adversarial prompting methods and detail practical mitigation strategies, such as session level context aggregation and deep alignment approaches. Our study underscores the urgent need for holistic, context aware defenses and continuous adversarial testing to future proof LLM deployments against evolving multi-turn threats.
匹配关键词: agent
---

[ACADEMIC - ARXIV]
标题: TraceScope: Interactive URL Triage via Decoupled Checklist Adjudication
作者: Haolin Zhang, William Reber, Yuxuan Zhang, Guofei Gu, Jeff Huang
链接: https://arxiv.org/abs/2604.21840v1
完整摘要: Modern phishing campaigns increasingly evade snapshot-based URL classifiers using interaction gates (e.g., checkbox/slider challenges), delayed content rendering, and logo-less credential harvesters. This shifts URL triage from static classification toward an interactive forensics task: an analyst must actively navigate the page while isolating themselves from potential runtime exploits. We present TraceScope, a decoupled triage pipeline that operationalizes this workflow at scale. To prevent the observer effect and ensure safety, a sandboxed operator agent drives a real GUI browser guided by visual motivation to elicit page behavior, freezing the session into an immutable evidence bundle. Separately, an adjudicator agent circumvents LLM context limitations by querying evidence on demand to verify a MITRE ATT&CK checklist, and generates an audit-ready report with extracted indicators of compromise (IOCs) and a final verdict. Evaluated on 708 reachable URLs from existing dataset (241 verified phishing from PhishTank and 467 benign from Tranco-derived crawling), TraceScope achieves 0.94 precision and 0.78 recall, substantially improving recall over three prior visual/reference-based classifiers while producing reproducible, analyst-grade evidence suitable for review. More importantly, we manually curated a dataset of real-world phishing emails to evaluate our system in a practical setting. Our evaluation reveals that TraceScope demonstrates superior performance in a real-world scenario as well, successfully detecting sophisticated phishing attempts that current state-of-the-art defenses fail to identify.
匹配关键词: agent
---

[ACADEMIC - ARXIV]
标题: Task-Driven Co-Design of Heterogeneous Multi-Robot Systems
作者: Maximilian Stralz, Meshal Alharbi, Yujun Huang, Gioele Zardini
链接: https://arxiv.org/abs/2604.21894v1
完整摘要: Designing multi-agent robotic systems requires reasoning across tightly coupled decisions spanning heterogeneous domains, including robot design, fleet composition, and planning. Much effort has been devoted to isolated improvements in these domains, whereas system-level co-design considering trade-offs and task requirements remains underexplored. In this work, we present a formal and compositional framework for the task-driven co-design of heterogeneous multi-robot systems. Building on a monotone co-design theory, we introduce general abstractions of robots, fleets, planners, executors, and evaluators as interconnected design problems with well-defined interfaces that are agnostic to both implementations and tasks. This structure enables efficient joint optimization of robot design, fleet composition, and planning under task-specific performance constraints. A series of case studies demonstrates the capabilities of the framework. Various component models can be seamlessly incorporated, including new robot types, task profiles, and probabilistic sensing objectives, while non-obvious design alternatives are systematically uncovered with optimality guarantees. The results highlight the flexibility, scalability, and interpretability of the proposed approach, and illustrate how formal co-design enables principled reasoning about complex heterogeneous multi-robot systems.
匹配关键词: multi-agent
---

[ACADEMIC - ARXIV]
标题: Transient Turn Injection: Exposing Stateless Multi-Turn Vulnerabilities in Large Language Models
作者: Naheed Rayhan, Sohely Jahan
链接: https://arxiv.org/abs/2604.21860v1
完整摘要: Large language models (LLMs) are increasingly integrated into sensitive workflows, raising the stakes for adversarial robustness and safety. This paper introduces Transient Turn Injection(TTI), a new multi-turn attack technique that systematically exploits stateless moderation by distributing adversarial intent across isolated interactions. TTI leverages automated attacker agents powered by large language models to iteratively test and evade policy enforcement in both commercial and open-source LLMs, marking a departure from conventional jailbreak approaches that typically depend on maintaining persistent conversational context. Our extensive evaluation across state-of-the-art models-including those from OpenAI, Anthropic, Google Gemini, Meta, and prominent open-source alternatives-uncovers significant variations in resilience to TTI attacks, with only select architectures exhibiting substantial inherent robustness. Our automated blackbox evaluation framework also uncovers previously unknown model specific vulnerabilities and attack surface patterns, especially within medical and high stakes domains. We further compare TTI against established adversarial prompting methods and detail practical mitigation strategies, such as session level context aggregation and deep alignment approaches. Our study underscores the urgent need for holistic, context aware defenses and continuous adversarial testing to future proof LLM deployments against evolving multi-turn threats.
匹配关键词: multi-agent
---

[ACADEMIC - ARXIV]
标题: Tool Attention Is All You Need: Dynamic Tool Gating and Lazy Schema Loading for Eliminating the MCP/Tools Tax in Scalable Agentic Workflows
作者: Anuj Sadani, Deepak Kumar
链接: https://arxiv.org/abs/2604.21816v1
完整摘要: The Model Context Protocol (MCP) has become a common interface for connecting large language model (LLM) agents to external tools, but its reliance on stateless, eager schema injection imposes a hidden per-turn overhead the MCP Tax or Tools Tax that practitioner reports place between roughly 10k and 60k tokens in typical multi-server deployments. This payload inflates the key-value cache, is associated with reasoning degradation as context utilization approaches published fracture points around 70%, and turns token budgets into a recurring operational cost. We introduce Tool Attention, a middleware-layer mechanism that generalizes the "Attention Is All You Need" paradigm from self-attention over tokens to gated attention over tools. Tool Attention combines (i) an Intent Schema Overlap (ISO) score from sentence embeddings, (ii) a state-aware gating function enforcing preconditions and access scopes, and (iii) a two-phase lazy schema loader that keeps a compact summary pool in context and promotes full JSON schemas only for top-k gated tools. We evaluate on a simulated 120-tool, six-server benchmark whose per-server token counts are calibrated to public audits of real MCP deployments. In this simulation, Tool Attention directly reduces measured per-turn tool tokens by 95.0% (47.3k -> 2.4k) and raises effective context utilization (a token-ratio quantity) from 24% to 91%. End-to-end figures for task success, latency, cost, and reasoning quality are reported as projections derived from the measured token counts combined with published deployment telemetry; they are not measured on live LLM agents, and we mark projected values explicitly throughout. Taken together, the results support a simple thesis: protocol-level efficiency, not raw context length, is a binding constraint on scalable gentic systems. The code for this work is accessible at https://github.com/asadani/tool-attention
匹配关键词: multi-agent
---

[ACADEMIC - ARXIV]
标题: Learning to Communicate: Toward End-to-End Optimization of Multi-Agent Language Systems
作者: Ye Yu, Heming Liu, Haibo Jin, Xiaopeng Yuan, Peng Kuang, Haohan Wang
链接: https://arxiv.org/abs/2604.21794v1
完整摘要: Multi-agent systems built on large language models have shown strong performance on complex reasoning tasks, yet most work focuses on agent roles and orchestration while treating inter-agent communication as a fixed interface. Latent communication through internal representations such as key-value caches offers a promising alternative to text-based protocols, but existing approaches do not jointly optimize communication with multi-agent reasoning. Therefore we propose DiffMAS, a training framework that treats latent communication as a learnable component of multi-agent systems. DiffMAS performs parameter-efficient supervised training over multi-agent latent trajectories, enabling agents to jointly learn how information should be encoded and interpreted across interactions. Experiments on mathematical reasoning, scientific QA, code generation, and commonsense benchmarks show that DiffMAS consistently improves reasoning accuracy and decoding stability over single-agent inference, text-based multi-agent systems, and prior latent communication methods, achieving 26.7% on AIME24, 20.2% on GPQA-Diamond, and consistent gains across reasoning benchmarks.
匹配关键词: multi-agent
---

[ACADEMIC - ARXIV]
标题: StructMem: Structured Memory for Long-Horizon Behavior in LLMs
作者: Buqiang Xu, Yijun Chen, Jizhan Fang, Ruobin Zhong, Yunzhi Yao, Yuqi Zhu, Lun Du, Shumin Deng
链接: https://arxiv.org/abs/2604.21748v1
完整摘要: Long-term conversational agents need memory systems that capture relationships between events, not merely isolated facts, to support temporal reasoning and multi-hop question answering. Current approaches face a fundamental trade-off: flat memory is efficient but fails to model relational structure, while graph-based memory enables structured reasoning at the cost of expensive and fragile construction. To address these issues, we propose \textbf{StructMem}, a structure-enriched hierarchical memory framework that preserves event-level bindings and induces cross-event connections. By temporally anchoring dual perspectives and performing periodic semantic consolidation, StructMem improves temporal reasoning and multi-hop performance on \texttt{LoCoMo}, while substantially reducing token usage, API calls, and runtime compared to prior memory systems, see https://github.com/zjunlp/LightMem .
匹配关键词: multi-agent
---

[ACADEMIC - ARXIV]
标题: Seeing Fast and Slow: Learning the Flow of Time in Videos
作者: Yen-Siang Wu, Rundong Luo, Jingsen Zhu, Tao Tu, Ali Farhadi, Matthew Wallingford, Yu-Chiang Frank Wang, Steve Marschner, Wei-Chiu Ma
链接: https://arxiv.org/abs/2604.21931v1
完整摘要: How can we tell whether a video has been sped up or slowed down? How can we generate videos at different speeds? Although videos have been central to modern computer vision research, little attention has been paid to perceiving and controlling the passage of time. In this paper, we study time as a learnable visual concept and develop models for reasoning about and manipulating the flow of time in videos. We first exploit the multimodal cues and temporal structure naturally present in videos to learn, in a self-supervised manner, to detect speed changes and estimate playback speed. We then show that these learned temporal reasoning models enable us to curate the largest slow-motion video dataset to date from noisy in-the-wild sources. Such slow-motion footage, typically filmed by high-speed cameras, contains substantially richer temporal detail than standard videos. Using this data, we further develop models capable of temporal control, including speed-conditioned video generation, which produces motion at specified playback speed, and temporal super-resolution, which tranforms low-FPS, blurry videos into high-FPS sequences with fine-grained temporal details. Our findings highlight time as a manipulable, perceptual dimension in video learning, opening doors to temporally controllable video generation, temporal forensics detection, and potentially richer world-models that understand how events unfold over time.
匹配关键词: tool use
---

[ACADEMIC - ARXIV]
标题: Evaluation of Automatic Speech Recognition Using Generative Large Language Models
作者: Thibault Bañeras-Roux, Shashi Kumar, Driss Khalil, Sergio Burdisso, Petr Motlicek, Shiran Liu, Mickael Rouvier, Jane Wottawa, Richard Dufour
链接: https://arxiv.org/abs/2604.21928v1
完整摘要: Automatic Speech Recognition (ASR) is traditionally evaluated using Word Error Rate (WER), a metric that is insensitive to meaning. Embedding-based semantic metrics are better correlated with human perception, but decoder-based Large Language Models (LLMs) remain underexplored for this task. This paper evaluates their relevance through three approaches: (1) selecting the best hypothesis between two candidates, (2) computing semantic distance using generative embeddings, and (3) qualitative classification of errors. On the HATS dataset, the best LLMs achieve 92--94\% agreement with human annotators for hypothesis selection, compared to 63\% for WER, also outperforming semantic metrics. Embeddings from decoder-based LLMs show performance comparable to encoder models. Finally, LLMs offer a promising direction for interpretable and semantic ASR evaluation.
匹配关键词: tool use
---

[ACADEMIC - ARXIV]
标题: Seeing Without Eyes: 4D Human-Scene Understanding from Wearable IMUs
作者: Hao-Yu Hsu, Tianhang Cheng, Jing Wen, Alexander G. Schwing, Shenlong Wang
链接: https://arxiv.org/abs/2604.21926v1
完整摘要: Understanding human activities and their surrounding environments typically relies on visual perception, yet cameras pose persistent challenges in privacy, safety, energy efficiency, and scalability. We explore an alternative: 4D perception without vision. Its goal is to reconstruct human motion and 3D scene layouts purely from everyday wearable sensors. For this we introduce IMU-to-4D, a framework that repurposes large language models for non-visual spatiotemporal understanding of human-scene dynamics. IMU-to-4D uses data from a few inertial sensors from earbuds, watches, or smartphones and predicts detailed 4D human motion together with coarse scene structure. Experiments across diverse human-scene datasets show that IMU-to-4D yields more coherent and temporally stable results than SoTA cascaded pipelines, suggesting wearable motion sensors alone can support rich 4D understanding.
匹配关键词: tool use
---

[ACADEMIC - ARXIV]
标题: When Prompts Override Vision: Prompt-Induced Hallucinations in LVLMs
作者: Pegah Khayatan, Jayneel Parekh, Arnaud Dapogny, Mustafa Shukor, Alasdair Newson, Matthieu Cord
链接: https://arxiv.org/abs/2604.21911v1
完整摘要: Despite impressive progress in capabilities of large vision-language models (LVLMs), these systems remain vulnerable to hallucinations, i.e., outputs that are not grounded in the visual input. Prior work has attributed hallucinations in LVLMs to factors such as limitations of the vision backbone or the dominance of the language component, yet the relative importance of these factors remains unclear. To resolve this ambiguity, We propose HalluScope, a benchmark to better understand the extent to which different factors induce hallucinations. Our analysis indicates that hallucinations largely stem from excessive reliance on textual priors and background knowledge, especially information introduced through textual instructions. To mitigate hallucinations induced by textual instruction priors, we propose HalluVL-DPO, a framework for fine-tuning off-the-shelf LVLMs towards more visually grounded responses. HalluVL-DPO leverages preference optimization using a curated training dataset that we construct, guiding the model to prefer grounded responses over hallucinated ones. We demonstrate that our optimized model effectively mitigates the targeted hallucination failure mode, while preserving or improving performance on other hallucination benchmarks and visual capability evaluations. To support reproducibility and further research, we will publicly release our evaluation benchmark, preference training dataset, and code at https://pegah-kh.github.io/projects/prompts-override-vision/ .
匹配关键词: tool use
---

[ACADEMIC - ARXIV]
标题: Directional Confusions Reveal Divergent Inductive Biases Through Rate-Distortion Geometry in Human and Machine Vision
作者: Leyla Roksan Caglar, Pedro A. M. Mediano, Baihan Lin
链接: https://arxiv.org/abs/2604.21909v1
完整摘要: Humans and modern vision models can reach similar classification accuracy while making systematically different kinds of mistakes - differing not in how often they err, but in who gets mistaken for whom, and in which direction. We show that these directional confusions reveal distinct inductive biases that are invisible to accuracy alone. Using matched human and deep vision model responses on a natural-image categorization task under 12 perturbation types, we quantify asymmetry in confusion matrices and link it to generalization geometry through a Rate-Distortion (RD) framework, summarized by three geometric signatures (slope (beta), curvature (kappa)) and efficiency (AUC). We find that humans exhibit broad but weak asymmetries, whereas deep vision models show sparser, stronger directional collapses. Robustness training reduces global asymmetry but fails to recover the human-like breadth-strength profile of graded similarity. Mechanistic simulations further show that different asymmetry organizations shift the RD frontier in opposite directions, even when matched for performance. Together, these results position directional confusions and RD geometry as compact, interpretable signatures of inductive bias under distribution shift.
匹配关键词: tool use
---

[ACADEMIC - ARXIV]
标题: Tool Attention Is All You Need: Dynamic Tool Gating and Lazy Schema Loading for Eliminating the MCP/Tools Tax in Scalable Agentic Workflows
作者: Anuj Sadani, Deepak Kumar
链接: https://arxiv.org/abs/2604.21816v1
完整摘要: The Model Context Protocol (MCP) has become a common interface for connecting large language model (LLM) agents to external tools, but its reliance on stateless, eager schema injection imposes a hidden per-turn overhead the MCP Tax or Tools Tax that practitioner reports place between roughly 10k and 60k tokens in typical multi-server deployments. This payload inflates the key-value cache, is associated with reasoning degradation as context utilization approaches published fracture points around 70%, and turns token budgets into a recurring operational cost. We introduce Tool Attention, a middleware-layer mechanism that generalizes the "Attention Is All You Need" paradigm from self-attention over tokens to gated attention over tools. Tool Attention combines (i) an Intent Schema Overlap (ISO) score from sentence embeddings, (ii) a state-aware gating function enforcing preconditions and access scopes, and (iii) a two-phase lazy schema loader that keeps a compact summary pool in context and promotes full JSON schemas only for top-k gated tools. We evaluate on a simulated 120-tool, six-server benchmark whose per-server token counts are calibrated to public audits of real MCP deployments. In this simulation, Tool Attention directly reduces measured per-turn tool tokens by 95.0% (47.3k -> 2.4k) and raises effective context utilization (a token-ratio quantity) from 24% to 91%. End-to-end figures for task success, latency, cost, and reasoning quality are reported as projections derived from the measured token counts combined with published deployment telemetry; they are not measured on live LLM agents, and we mark projected values explicitly throughout. Taken together, the results support a simple thesis: protocol-level efficiency, not raw context length, is a binding constraint on scalable gentic systems. The code for this work is accessible at https://github.com/asadani/tool-attention
匹配关键词: MCP
---

[ACADEMIC - ARXIV]
标题: Breaking MCP with Function Hijacking Attacks: Novel Threats for Function Calling and Agentic Models
作者: Yannis Belkhiter, Giulio Zizzo, Sergio Maffeis, Seshu Tirupathi, John D. Kelleher
链接: https://arxiv.org/abs/2604.20994v1
完整摘要: The growth of agentic AI has drawn significant attention to function calling Large Language Models (LLMs), which are designed to extend the capabilities of AI-powered system by invoking external functions. Injection and jailbreaking attacks have been extensively explored to showcase the vulnerabilities of LLMs to user prompt manipulation. The expanded capabilities of agentic models introduce further vulnerabilities via their function calling interface. Recent work in LLM security showed that function calling can be abused, leading to data tampering and theft, causing disruptive behavior such as endless loops, or causing LLMs to produce harmful content in the style of jailbreaking attacks. This paper introduces a novel function hijacking attack (FHA) that manipulates the tool selection process of agentic models to force the invocation of a specific, attacker-chosen function. While existing attacks focus on semantic preference of the model for function-calling tasks, we show that FHA is largely agnostic to the context semantics and robust to the function sets, making it applicable across diverse domains. We further demonstrate that FHA can be trained to produce universal adversarial functions, enabling a single attacked function to hijack tool selection across multiple queries and payload configurations. We conducted experiments on 5 different models, including instructed and reasoning variants, reaching 70% to 100% ASR over the established BFCL dataset. Our findings further demonstrate the need for strong guardrails and security modules for agentic systems.
匹配关键词: MCP
---

[ACADEMIC - ARXIV]
标题: Learning to Evolve: A Self-Improving Framework for Multi-Agent Systems via Textual Parameter Graph Optimization
作者: Shan He, Runze Wang, Zhuoyun Du, Huiyu Bai, Zouying Cao, Yu Cheng, Bo Zheng
链接: https://arxiv.org/abs/2604.20714v1
完整摘要: Designing and optimizing multi-agent systems (MAS) is a complex, labor-intensive process of "Agent Engineering." Existing automatic optimization methods, primarily focused on flat prompt tuning, lack the structural awareness to debug the intricate web of interactions in MAS. More critically, these optimizers are static; they do not learn from experience to improve their own optimization strategies. To address these gaps, we introduce Textual Parameter Graph Optimization (TPGO), a framework that enables a multi-agent system to learn to evolve. TPGO first models the MAS as a Textual Parameter Graph (TPG), where agents, tools, and workflows are modular, optimizable nodes. To guide evolution, we derive "textual gradients," structured natural language feedback from execution traces, to pinpoint failures and suggest granular modifications. The core of our framework is Group Relative Agent Optimization (GRAO), a novel meta-learning strategy that learns from historical optimization experiences. By analyzing past successes and failures, GRAO becomes progressively better at proposing effective updates, allowing the system to learn how to optimize itself. Extensive experiments on complex benchmarks like GAIA and MCP-Universe show that TPGO significantly enhances the performance of state-of-the-art agent frameworks, achieving higher success rates through automated, self-improving optimization.
匹配关键词: MCP
---

[ACADEMIC - ARXIV]
标题: Framelet-Based Blind Image Restoration with Minimax Concave Regularization
作者: Heng Zhang, Reza Parvaz, Rui Yang
链接: https://arxiv.org/abs/2604.19314v1
完整摘要: Recovering corrupted images is one of the most challenging problems in image processing. Among various restoration tasks, blind image deblurring has been extensively studied due to its practical importance and inherent difficulty. In this problem, both the point spread function (PSF) and the underlying latent sharp image must be estimated simultaneously. This problem cannot be solved directly due to its ill-posed nature. One powerful tool for solving such problems is total variation (TV) regularization. The $\ell_0$-norm regularization within the TV framework has been widely adopted to promote sparsity in image gradients or transform domains, leading to improved preservation of edges and fine structures. However, the use of the $\ell_0$-norm results in a highly nonconvex and computationally intractable optimization problem, which limits its practical applicability. To overcome these difficulties, we employ the minimax concave penalty (MCP), which promotes enhanced sparsity and provides a closer approximation to the $\ell_0$-norm. In addition, a reweighted $\ell_1$-norm regularization is incorporated to further reduce estimation bias and improve the preservation of fine image details and textures. After introducing the proposed model, a numerical algorithm is developed to solve the resulting optimization problem. The effectiveness of the proposed approach is then demonstrated through experimental evaluations on several test images.
匹配关键词: MCP
---

[ACADEMIC - ARXIV]
标题: How Adversarial Environments Mislead Agentic AI?
作者: Zhonghao Zhan, Huichi Zhou, Zhenhao Li, Peiyuan Jing, Krinos Li, Hamed Haddadi
链接: https://arxiv.org/abs/2604.18874v1
完整摘要: Tool-integrated agents are deployed on the premise that external tools ground their outputs in reality. Yet this very reliance creates a critical attack surface. Current evaluations benchmark capability in benign settings, asking "can the agent use tools correctly" but never "what if the tools lie". We identify this Trust Gap: agents are evaluated for performance, not for skepticism. We formalize this vulnerability as Adversarial Environmental Injection (AEI), a threat model where adversaries compromise tool outputs to deceive agents. AEI constitutes environmental deception: constructing a "fake world" of poisoned search results and fabricated reference networks around unsuspecting agents. We operationalize this via POTEMKIN, a Model Context Protocol (MCP)-compatible harness for plug-and-play robustness testing. We identify two orthogonal attack surfaces: The Illusion (breadth attacks) poison retrieval to induce epistemic drift toward false beliefs, while The Maze (depth attacks) exploit structural traps to cause policy collapse into infinite loops. Across 11,000+ runs on five frontier agents, we find a stark robustness gap: resistance to one attack often increases vulnerability to the other, demonstrating that epistemic and navigational robustness are distinct capabilities.
匹配关键词: MCP
---

[ACADEMIC - ARXIV]
标题: Long-Horizon Manipulation via Trace-Conditioned VLA Planning
作者: Isabella Liu, An-Chieh Cheng, Rui Yan, Geng Chen, Ri-Zhao Qiu, Xueyan Zou, Sha Yi, Hongxu Yin, Xiaolong Wang, Sifei Liu
链接: https://arxiv.org/abs/2604.21924v1
完整摘要: Long-horizon manipulation remains challenging for vision-language-action (VLA) policies: real tasks are multi-step, progress-dependent, and brittle to compounding execution errors. We present LoHo-Manip, a modular framework that scales short-horizon VLA execution to long-horizon instruction following via a dedicated task-management VLM. The manager is decoupled from the executor and is invoked in a receding-horizon manner: given the current observation, it predicts a progress-aware remaining plan that combines (i) a subtask sequence with an explicit done + remaining split as lightweight language memory, and (ii) a visual trace -- a compact 2D keypoint trajectory prompt specifying where to go and what to approach next. The executor VLA is adapted to condition on the rendered trace, thereby turning long-horizon decision-making into repeated local control by following the trace. Crucially, predicting the remaining plan at each step yields an implicit closed loop: failed steps persist in subsequent outputs, and traces update accordingly, enabling automatic continuation and replanning without hand-crafted recovery logic or brittle visual-history buffers. Extensive experiments spanning embodied planning, long-horizon reasoning, trajectory prediction, and end-to-end manipulation in simulation and on a real Franka robot demonstrate strong gains in long-horizon success, robustness, and out-of-distribution generalization. Project page: https://www.liuisabella.com/LoHoManip
匹配关键词: planning
---

[ACADEMIC - ARXIV]
标题: Task-Driven Co-Design of Heterogeneous Multi-Robot Systems
作者: Maximilian Stralz, Meshal Alharbi, Yujun Huang, Gioele Zardini
链接: https://arxiv.org/abs/2604.21894v1
完整摘要: Designing multi-agent robotic systems requires reasoning across tightly coupled decisions spanning heterogeneous domains, including robot design, fleet composition, and planning. Much effort has been devoted to isolated improvements in these domains, whereas system-level co-design considering trade-offs and task requirements remains underexplored. In this work, we present a formal and compositional framework for the task-driven co-design of heterogeneous multi-robot systems. Building on a monotone co-design theory, we introduce general abstractions of robots, fleets, planners, executors, and evaluators as interconnected design problems with well-defined interfaces that are agnostic to both implementations and tasks. This structure enables efficient joint optimization of robot design, fleet composition, and planning under task-specific performance constraints. A series of case studies demonstrates the capabilities of the framework. Various component models can be seamlessly incorporated, including new robot types, task profiles, and probabilistic sensing objectives, while non-obvious design alternatives are systematically uncovered with optimality guarantees. The results highlight the flexibility, scalability, and interpretability of the proposed approach, and illustrate how formal co-design enables principled reasoning about complex heterogeneous multi-robot systems.
匹配关键词: planning
---

[ACADEMIC - ARXIV]
标题: Agentic AI-assisted coding offers a unique opportunity to instill epistemic grounding during software development
作者: Magnus Palmblad, Jared M. Ragland, Benjamin A. Neely
链接: https://arxiv.org/abs/2604.21744v1
完整摘要: The capabilities of AI-assisted coding are progressing at breakneck speed. Chat-based vibe coding has evolved into fully fledged AI-assisted, agentic software development using agent scaffolds where the human developer creates a plan that agentic AIs implement. One current trend is utilizing documents beyond this plan document, such as project and method-scoped documents. Here we propose GROUNDING$.$md, a community-governed, field-scoped epistemic grounding document, using mass spectrometry-based proteomics as an example. This explicit field-scoped grounding document encodes Hard Constraints (non-negotiable validity invariants empirically required for scientific correctness) and Convention Parameters (community-agreed defaults) that override all other contexts to enforce validity, regardless of what the user prompts. In practice, this will empower a non-domain expert to generate code, tools, and software that have best practices baked in at the ground level, providing confidence to the software developer but also to those reviewing or using the final product. Undoubtedly it is easier to have agentic AIs adhere to guidelines than humans, and this opportunity allows for organizations to develop epistemic grounding documents in such a way as to keep domain experts in the loop in a future of democratized generation of bespoke software solutions.
匹配关键词: planning
---

[ACADEMIC - ARXIV]
标题: DryRUN: On the Role of Public Tests in LLM-Driven Code Generation
作者: Kaushitha Silva, Srinath Perera
链接: https://arxiv.org/abs/2604.21598v1
完整摘要: Multi-agent frameworks are widely used in autonomous code generation and have applications in complex algorithmic problem-solving. Recent work has addressed the challenge of generating functionally correct code by incorporating simulation-driven planning and debugging, where language models trace execution steps to verify logic. However, these approaches depend on human-provided public test cases to ground the debugging and simulation loop. Manually authoring comprehensive input-output examples is a labor-intensive bottleneck in the software development lifecycle. Because ground-truth input-output examples are rarely available prior to implementation in real-world software engineering, this dependency restricts methods to curated competitive programming benchmarks. Furthermore, we identify that reliance on these public tests induces an ``overconfidence gap,'' causing frameworks to overfit to simplistic examples and fail on hidden evaluations. In contrast, we observe that external sample inputs are not strictly necessary for code generation. We demonstrate that large language models can autonomously generate valid inputs and simulate execution traces to self-correct. Consequently, we develop DryRUN, a framework that eliminates the need for ground-truth samples by allowing the LLM to iteratively plan, autonomously generate its own inputs and simulate execution, mitigating algorithmic overconfidence. Evaluations on the LiveCodeBench v6 dataset (post-March 2025) demonstrate that DryRUN matches performance against CodeSIM, a state-of-the-art and public-test-dependent framework, while operating entirely without public test cases or external execution feedback while reducing output token consumption.
匹配关键词: planning
---

[ACADEMIC - ARXIV]
标题: MISTY: High-Throughput Motion Planning via Mixer-based Single-step Drifting
作者: Yining Xing, Zehong Ke, Yiqian Tu, Zhiyuan Liu, Wenhao Yu, Jianqiang Wang
链接: https://arxiv.org/abs/2604.21489v1
完整摘要: Multi-modal trajectory generation is essential for safe autonomous driving, yet existing diffusion-based planners suffer from high inference latency due to iterative neural function evaluations. This paper presents MISTY (Mixer-based Inference for Single-step Trajectory-drifting Yield), a high-throughput generative motion planner that achieves state-of-the-art closed-loop performance with pure single-step inference. MISTY integrates a vectorized Sub-Graph encoder to capture environment context, a Variational Autoencoder to structure expert trajectories into a compact 32-dimensional latent manifold, and an ultra-lightweight MLP-Mixer decoder to eliminate quadratic attention complexity. Importantly, we introduce a latent-space drifting loss that shifts the complex distribution evolution entirely to the training phase. By formulating explicit attractive and repulsive forces, this mechanism empowers the model to synthesize novel, proactive maneuvers, such as active overtaking, that are virtually absent from the raw expert demonstrations. Extensive evaluations on the nuPlan benchmark demonstrate that MISTY achieves state-of-the-art results on the challenging Test14-hard split, with comprehensive scores of 80.32 and 82.21 in non-reactive and reactive settings, respectively. Operating at over 99 FPS with an end-to-end latency of 10.1 ms, MISTY offers an order-of-magnitude speedup over iterative diffusion planners while while achieving significantly robust generation.
匹配关键词: planning
---

[ACADEMIC - ARXIV]
标题: Long-Horizon Manipulation via Trace-Conditioned VLA Planning
作者: Isabella Liu, An-Chieh Cheng, Rui Yan, Geng Chen, Ri-Zhao Qiu, Xueyan Zou, Sha Yi, Hongxu Yin, Xiaolong Wang, Sifei Liu
链接: https://arxiv.org/abs/2604.21924v1
完整摘要: Long-horizon manipulation remains challenging for vision-language-action (VLA) policies: real tasks are multi-step, progress-dependent, and brittle to compounding execution errors. We present LoHo-Manip, a modular framework that scales short-horizon VLA execution to long-horizon instruction following via a dedicated task-management VLM. The manager is decoupled from the executor and is invoked in a receding-horizon manner: given the current observation, it predicts a progress-aware remaining plan that combines (i) a subtask sequence with an explicit done + remaining split as lightweight language memory, and (ii) a visual trace -- a compact 2D keypoint trajectory prompt specifying where to go and what to approach next. The executor VLA is adapted to condition on the rendered trace, thereby turning long-horizon decision-making into repeated local control by following the trace. Crucially, predicting the remaining plan at each step yields an implicit closed loop: failed steps persist in subsequent outputs, and traces update accordingly, enabling automatic continuation and replanning without hand-crafted recovery logic or brittle visual-history buffers. Extensive experiments spanning embodied planning, long-horizon reasoning, trajectory prediction, and end-to-end manipulation in simulation and on a real Franka robot demonstrate strong gains in long-horizon success, robustness, and out-of-distribution generalization. Project page: https://www.liuisabella.com/LoHoManip
匹配关键词: long-horizon
---

[ACADEMIC - ARXIV]
标题: A Multi-Stage Warm-Start Deep Learning Framework for Unit Commitment
作者: Muhy Eddin Za'ter, Anna Van Boven, Bri-Mathias Hodge, Kyri Baker
链接: https://arxiv.org/abs/2604.21891v1
完整摘要: Maintaining instantaneous balance between electricity supply and demand is critical for reliability and grid instability. System operators achieve this through solving the task of Unit Commitment (UC),ca high dimensional large-scale Mixed-integer Linear Programming (MILP) problem that is strictly and heavily governed by the grid physical constraints. As grid integrate variable renewable sources, and new technologies such as long duration storage in the grid, UC must be optimally solved for multi-day horizons and potentially with greater frequency. Therefore, traditional MILP solvers increasingly struggle to compute solutions within these tightening operational time limits. To bypass these computational bottlenecks, this paper proposes a novel framework utilizing a transformer-based architecture to predict generator commitment schedules over a 72-hour horizon. Also, because raw predictions in highly dimensional spaces often yield physically infeasible results, the pipeline integrates the self-attention network with deterministic post-processing heuristics that systematically enforce minimum up/down times and minimize excess capacity. Finally, these refined predictions are utilized as a warm start for a downstream MILP solver, while employing a confidence-based variable fixation strategy to drastically reduce the combinatorial search space. Validated on a single-bus test system, the complete multi-stage pipeline achieves 100\% feasibility and significantly accelerates computation times. Notably, in approximately 20\% of test instances, the proposed model reached a feasible operational schedule with a lower overall system cost than relying solely on the solver.
匹配关键词: long-horizon
---

[ACADEMIC - ARXIV]
标题: StructMem: Structured Memory for Long-Horizon Behavior in LLMs
作者: Buqiang Xu, Yijun Chen, Jizhan Fang, Ruobin Zhong, Yunzhi Yao, Yuqi Zhu, Lun Du, Shumin Deng
链接: https://arxiv.org/abs/2604.21748v1
完整摘要: Long-term conversational agents need memory systems that capture relationships between events, not merely isolated facts, to support temporal reasoning and multi-hop question answering. Current approaches face a fundamental trade-off: flat memory is efficient but fails to model relational structure, while graph-based memory enables structured reasoning at the cost of expensive and fragile construction. To address these issues, we propose \textbf{StructMem}, a structure-enriched hierarchical memory framework that preserves event-level bindings and induces cross-event connections. By temporally anchoring dual perspectives and performing periodic semantic consolidation, StructMem improves temporal reasoning and multi-hop performance on \texttt{LoCoMo}, while substantially reducing token usage, API calls, and runtime compared to prior memory systems, see https://github.com/zjunlp/LightMem .
匹配关键词: long-horizon
---

[ACADEMIC - ARXIV]
标题: HiCrew: Hierarchical Reasoning for Long-Form Video Understanding via Question-Aware Multi-Agent Collaboration
作者: Yuehan Zhu, Jingqi Zhao, Jiawen Zhao, Xudong Mao, Baoquan Zhao
链接: https://arxiv.org/abs/2604.21444v1
完整摘要: Long-form video understanding remains fundamentally challenged by pervasive spatiotemporal redundancy and intricate narrative dependencies that span extended temporal horizons. While recent structured representations compress visual information effectively, they frequently sacrifice temporal coherence, which is critical for causal reasoning. Meanwhile, existing multi-agent frameworks operate through rigid, pre-defined workflows that fail to adapt their reasoning strategies to question-specific demands. In this paper, we introduce HiCrew, a hierarchical multi-agent framework that addresses these limitations through three core contributions. First, we propose a Hybrid Tree structure that leverages shot boundary detection to preserve temporal topology while performing relevance-guided hierarchical clustering within semantically coherent segments. Second, we develop a Question-Aware Captioning mechanism that synthesizes intent-driven visual prompts to generate precision-oriented semantic descriptions. Third, we integrate a Planning Layer that dynamically orchestrates agent collaboration by adaptively selecting roles and execution paths based on question complexity. Extensive experiments on EgoSchema and NExT-QA validate the effectiveness of our approach, demonstrating strong performance across diverse question types with particularly pronounced gains in temporal and causal reasoning tasks that benefit from our hierarchical structure-preserving design.
匹配关键词: long-horizon
---

[ACADEMIC - ARXIV]
标题: FingerViP: Learning Real-World Dexterous Manipulation with Fingertip Visual Perception
作者: Zhen Zhang, Weinan Wang, Hejia Sun, Qingpeng Ding, Xiangyu Chu, Guoxin Fang, K. W. Samuel Au
链接: https://arxiv.org/abs/2604.21331v1
完整摘要: The current practice of dexterous manipulation generally relies on a single wrist-mounted view, which is often occluded and limits performance on tasks requiring multi-view perception. In this work, we present FingerViP, a learning system that utilizes a visuomotor policy with fingertip visual perception for dexterous manipulation. Specifically, we design a vision-enhanced fingertip module with an embedded miniature camera and install the modules on each finger of a multi-fingered hand. The fingertip cameras substantially improve visual perception by providing comprehensive, multi-view feedback of both the hand and its surrounding environment. Building on the integrated fingertip modules, we develop a diffusion-based whole-body visuomotor policy conditioned on a third-view camera and multi-view fingertip vision, which effectively learns complex manipulation skills directly from human demonstrations. To improve view-proprioception alignment and contact awareness, each fingertip visual feature is augmented with its corresponding camera pose encoding and per-finger joint-current encoding. We validate the effectiveness of the multi-view fingertip vision and demonstrate the robustness and adaptability of FingerViP on various challenging real-world tasks, including pressing buttons inside a confined box, retrieving sticks from an unstable support, retrieving objects behind an occluding curtain, and performing long-horizon cabinet opening and object retrieval, achieving an overall success rate of 80.8%. All hardware designs and code will be fully open-sourced.
匹配关键词: long-horizon
---

[ACADEMIC - ARXIV]
标题: From Research Question to Scientific Workflow: Leveraging Agentic AI for Science Automation
作者: Bartosz Balis, Michal Orzechowski, Piotr Kica, Michal Dygas, Michal Kuszewski
链接: https://arxiv.org/abs/2604.21910v1
完整摘要: Scientific workflow systems automate execution -- scheduling, fault tolerance, resource management -- but not the semantic translation that precedes it. Scientists still manually convert research questions into workflow specifications, a task requiring both domain knowledge and infrastructure expertise. We propose an agentic architecture that closes this gap through three layers: an LLM interprets natural language into structured intents (semantic layer); validated generators produce reproducible workflow DAGs (deterministic layer); and domain experts author ``Skills'': markdown documents encoding vocabulary mappings, parameter constraints, and optimization strategies (knowledge layer). This decomposition confines LLM non-determinism to intent extraction: identical intents always yield identical workflows. We implement and evaluate the architecture on the 1000 Genomes population genetics workflow and Hyperflow WMS running on Kubernetes. In an ablation study on 150 queries, Skills raise full-match intent accuracy from 44% to 83%; skill-driven deferred workflow generation reduces data transfer by 92\%; and the end-to-end pipeline completes queries on Kubernetes with LLM overhead below 15 seconds and cost under $0.001 per query.
匹配关键词: agentic
---

[ACADEMIC - ARXIV]
标题: Nemobot Games: Crafting Strategic AI Gaming Agents for Interactive Learning with Large Language Models
作者: Chee Wei Tan, Yuchen Wang, Shangxin Guo
链接: https://arxiv.org/abs/2604.21896v1
完整摘要: This paper introduces a new paradigm for AI game programming, leveraging large language models (LLMs) to extend and operationalize Claude Shannon's taxonomy of game-playing machines. Central to this paradigm is Nemobot, an interactive agentic engineering environment that enables users to create, customize, and deploy LLM-powered game agents while actively engaging with AI-driven strategies. The LLM-based chatbot, integrated within Nemobot, demonstrates its capabilities across four distinct classes of games. For dictionary-based games, it compresses state-action mappings into efficient, generalized models for rapid adaptability. In rigorously solvable games, it employs mathematical reasoning to compute optimal strategies and generates human-readable explanations for its decisions. For heuristic-based games, it synthesizes strategies by combining insights from classical minimax algorithms (see, e.g., shannon1950chess) with crowd-sourced data. Finally, in learning-based games, it utilizes reinforcement learning with human feedback and self-critique to iteratively refine strategies through trial-and-error and imitation learning. Nemobot amplifies this framework by offering a programmable environment where users can experiment with tool-augmented generation and fine-tuning of strategic game agents. From strategic games to role-playing games, Nemobot demonstrates how AI agents can achieve a form of self-programming by integrating crowdsourced learning and human creativity to iteratively refine their own logic. This represents a step toward the long-term goal of self-programming AI.
匹配关键词: agentic
---

[ACADEMIC - ARXIV]
标题: Task-Driven Co-Design of Heterogeneous Multi-Robot Systems
作者: Maximilian Stralz, Meshal Alharbi, Yujun Huang, Gioele Zardini
链接: https://arxiv.org/abs/2604.21894v1
完整摘要: Designing multi-agent robotic systems requires reasoning across tightly coupled decisions spanning heterogeneous domains, including robot design, fleet composition, and planning. Much effort has been devoted to isolated improvements in these domains, whereas system-level co-design considering trade-offs and task requirements remains underexplored. In this work, we present a formal and compositional framework for the task-driven co-design of heterogeneous multi-robot systems. Building on a monotone co-design theory, we introduce general abstractions of robots, fleets, planners, executors, and evaluators as interconnected design problems with well-defined interfaces that are agnostic to both implementations and tasks. This structure enables efficient joint optimization of robot design, fleet composition, and planning under task-specific performance constraints. A series of case studies demonstrates the capabilities of the framework. Various component models can be seamlessly incorporated, including new robot types, task profiles, and probabilistic sensing objectives, while non-obvious design alternatives are systematically uncovered with optimality guarantees. The results highlight the flexibility, scalability, and interpretability of the proposed approach, and illustrate how formal co-design enables principled reasoning about complex heterogeneous multi-robot systems.
匹配关键词: agentic
---

[ACADEMIC - ARXIV]
标题: Transient Turn Injection: Exposing Stateless Multi-Turn Vulnerabilities in Large Language Models
作者: Naheed Rayhan, Sohely Jahan
链接: https://arxiv.org/abs/2604.21860v1
完整摘要: Large language models (LLMs) are increasingly integrated into sensitive workflows, raising the stakes for adversarial robustness and safety. This paper introduces Transient Turn Injection(TTI), a new multi-turn attack technique that systematically exploits stateless moderation by distributing adversarial intent across isolated interactions. TTI leverages automated attacker agents powered by large language models to iteratively test and evade policy enforcement in both commercial and open-source LLMs, marking a departure from conventional jailbreak approaches that typically depend on maintaining persistent conversational context. Our extensive evaluation across state-of-the-art models-including those from OpenAI, Anthropic, Google Gemini, Meta, and prominent open-source alternatives-uncovers significant variations in resilience to TTI attacks, with only select architectures exhibiting substantial inherent robustness. Our automated blackbox evaluation framework also uncovers previously unknown model specific vulnerabilities and attack surface patterns, especially within medical and high stakes domains. We further compare TTI against established adversarial prompting methods and detail practical mitigation strategies, such as session level context aggregation and deep alignment approaches. Our study underscores the urgent need for holistic, context aware defenses and continuous adversarial testing to future proof LLM deployments against evolving multi-turn threats.
匹配关键词: agentic
---

[ACADEMIC - ARXIV]
标题: TraceScope: Interactive URL Triage via Decoupled Checklist Adjudication
作者: Haolin Zhang, William Reber, Yuxuan Zhang, Guofei Gu, Jeff Huang
链接: https://arxiv.org/abs/2604.21840v1
完整摘要: Modern phishing campaigns increasingly evade snapshot-based URL classifiers using interaction gates (e.g., checkbox/slider challenges), delayed content rendering, and logo-less credential harvesters. This shifts URL triage from static classification toward an interactive forensics task: an analyst must actively navigate the page while isolating themselves from potential runtime exploits. We present TraceScope, a decoupled triage pipeline that operationalizes this workflow at scale. To prevent the observer effect and ensure safety, a sandboxed operator agent drives a real GUI browser guided by visual motivation to elicit page behavior, freezing the session into an immutable evidence bundle. Separately, an adjudicator agent circumvents LLM context limitations by querying evidence on demand to verify a MITRE ATT&CK checklist, and generates an audit-ready report with extracted indicators of compromise (IOCs) and a final verdict. Evaluated on 708 reachable URLs from existing dataset (241 verified phishing from PhishTank and 467 benign from Tranco-derived crawling), TraceScope achieves 0.94 precision and 0.78 recall, substantially improving recall over three prior visual/reference-based classifiers while producing reproducible, analyst-grade evidence suitable for review. More importantly, we manually curated a dataset of real-world phishing emails to evaluate our system in a practical setting. Our evaluation reveals that TraceScope demonstrates superior performance in a real-world scenario as well, successfully detecting sophisticated phishing attempts that current state-of-the-art defenses fail to identify.
匹配关键词: agentic
---

[ACADEMIC - ARXIV]
标题: Super Apriel: One Checkpoint, Many Speeds
作者: SLAM Labs, :, Oleksiy Ostapenko, Raymond Li, Torsten Scholak, Alireza Mousavi-Hosseini, Aman Tiwari, Denis Kocetkov, Joel Lamy Poirier, Kelechi Ogueji, Nanda H Krishna, Rafael Pardinas, Sathwik Tejaswi Madhusudhan, Shruthan Radhakrishna, Srinivas Sunkara, Valerie Becaert
链接: https://arxiv.org/abs/2604.19877v1
完整摘要: We release Super Apriel, a 15B-parameter supernet in which every decoder layer provides four trained mixer choices -- Full Attention (FA), Sliding Window Attention (SWA), Kimi Delta Attention (KDA), and Gated DeltaNet (GDN). A placement selects one mixer per layer; placements can be switched between requests at serving time without reloading weights, enabling multiple speed presets from a single checkpoint. The shared checkpoint also enables speculative decoding without a separate draft model. The all-FA preset matches the Apriel 1.6 teacher on all reported benchmarks; recommended hybrid presets span $2.9\times$ to $10.7\times$ decode throughput at 96% to 77% quality retention, with throughput advantages that compound at longer context lengths. With four mixer types across 48 layers, the configuration space is vast. A surrogate that predicts placement quality from the per-layer mixer assignment makes the speed-quality landscape tractable and identifies the best tradeoffs at each speed level. We investigate whether the best configurations at each speed level can be identified early in training or only after convergence. Rankings stabilize quickly at 0.5B scale, but the most efficient configurations exhibit higher instability at 15B, cautioning against extrapolation from smaller models. Super Apriel is trained by stochastic distillation from a frozen Apriel 1.6 teacher, followed by supervised fine-tuning. We release the supernet weights, Fast-LLM training code, vLLM serving code, and a placement optimization toolkit.
匹配关键词: vLLM
---

[ACADEMIC - ARXIV]
标题: SLO-Guard: Crash-Aware, Budget-Consistent Autotuning for SLO-Constrained LLM Serving
作者: Christian Lysenstøen
链接: https://arxiv.org/abs/2604.17627v1
完整摘要: Serving large language models under latency service-level objectives (SLOs) is a configuration-heavy systems problem with an unusually failure-prone search space: many plausible configurations crash outright or miss user-visible latency targets, and standard black-box optimizers treat these failures as wasted trials. We present SLO-Guard, a crash-aware autotuner for vLLM serving that treats crashes as first-class observations. SLO-Guard combines a feasible-first Thermal Budget Annealing (TBA) exploration phase with a warm-started Tree-structured Parzen Estimator (TPE) exploitation phase; the handoff replays all exploration history, including crashes encoded as extreme constraint violations. We additionally contribute a configuration-repair pass, a GPU-aware KV-cache memory guard, and a four-category crash taxonomy. We evaluate SLO-Guard on Qwen2-1.5B served with vLLM 0.19 on an NVIDIA A100 40GB. Across a pre-specified five-seed study, both SLO-Guard and uniform random search attain 75/75 feasibility with zero crashes under the corrected concurrent harness, and are statistically tied on best-achieved latency (Mann-Whitney two-sided p=0.84). SLO-Guard's advantage is in budget consistency: more trials in the fast-serving regime (10.20 vs. 7.40 out of 15; one-sided p=0.014) and higher post-handoff consistency (0.876 vs. 0.539; p=0.010). Under concurrent load, SLO-Guard's cross-seed standard deviation on best latency is 4.4x tighter than random search's (2.26 ms vs. 10.00 ms). A harness-replication analysis shows that the consistency findings survive an independent sequential-dispatch measurement condition. The central claim is not that SLO-Guard finds a better final configuration, but that it spends a fixed tuning budget more predictably once the fast regime has been found.
匹配关键词: vLLM
---

[ACADEMIC - ARXIV]
标题: Bit-Flip Vulnerability of Shared KV-Cache Blocks in LLM Serving Systems
作者: Yuji Yamamoto, Satoshi Matsuura
链接: https://arxiv.org/abs/2604.17249v1
完整摘要: Rowhammer on GPU DRAM has enabled adversarial bit flips in model weights; shared KV-cache blocks in LLM serving systems present an analogous but previously unexamined target. In vLLM's Prefix Caching, these blocks exist as a single physical copy without integrity protection. Using software fault injection under ideal bit targeting, we characterize worst-case severity and identify three properties: (1) Silent divergence - 13 of 16 BF16 bit positions produce coherent but altered outputs, indistinguishable from legitimate responses without a clean baseline. (2) Selective propagation - only requests sharing the targeted prefix are affected. (3) Persistent accumulation - no temporal decay occurs, so cumulative damage grows linearly with subsequent requests. Together, these constitute a threat profile distinct from weight corruption: silent divergence and selective propagation enable detection evasion; persistent accumulation then proceeds unchecked, yielding damage amplification bounded only by how long the block remains cached. A checksum-based countermeasure detects any single-bit corruption at scheduling time, bounding cumulative damage to one batch independent of the block's cache lifetime, with negligible overhead. These results argue for integrity protection of prefix blocks before end-to-end exploitation is demonstrated.
匹配关键词: vLLM
---

[ACADEMIC - ARXIV]
标题: UCCL-Zip: Lossless Compression Supercharged GPU Communication
作者: Shuang Ma, Chon Lam Lao, Zhiying Xu, Zhuang Wang, Ziming Mao, Delong Meng, Jia Zhen, Jun Wu, Ion Stoica, Yida Wang, Yang Zhou
链接: https://arxiv.org/abs/2604.17172v2
完整摘要: The rapid growth of large language models (LLMs) has made GPU communication a critical bottleneck. While prior work reduces communication volume via quantization or lossy compression, these approaches introduce numerical errors that can degrade convergence, accuracy, and stability. We present UCCL-Zip, a unified design that integrates lossless compression directly into GPU communication primitives. UCCL-Zip supports both point-to-point (P2P) and collective communication without modifying user-facing APIs or compromising numerical correctness. For P2P communication, Uzip-P2P employs a split-send pipeline that exposes transmissible data early and overlaps compression with communication, while preserving high GPU efficiency by operating on large data blocks. For collective communication, Uzip-NCCL integrates compression into NCCL's persistent kernel model via fused execution, eliminating redundant memory traffic and kernel launches. In real workloads, UCCL-Zip accelerates RL weight synchronization by up to 47.5% and reduces vLLM end-to-end inference latency by up to 10%, all without application changes.
匹配关键词: vLLM
---

[ACADEMIC - ARXIV]
标题: Ragged Paged Attention: A High-Performance and Flexible LLM Inference Kernel for TPU
作者: Jevin Jiang, Ying Chen, Blake A. Hechtman, Fenghui Zhang, Yarong Mu
链接: https://arxiv.org/abs/2604.15464v1
完整摘要: Large Language Model (LLM) deployment is increasingly shifting to cost-efficient accelerators like Google's Tensor Processing Units (TPUs), prioritizing both performance and total cost of ownership (TCO). However, existing LLM inference kernels and serving systems remain largely GPU-centric, and there is no well-established approach for efficiently mapping LLM workloads onto TPU architectures--particularly under the dynamic and ragged execution patterns common in modern serving. In this paper, we present Ragged Paged Attention (RPA), a high-performance and flexible attention kernel for TPUs, implemented using Pallas and Mosaic. RPA addresses these challenges through three key techniques: (1) fine-grained tiling to enable efficient dynamic slicing over ragged memory, (2) a custom software pipeline that fuses KV cache updates with attention computation, and (3) a distribution-aware compilation strategy that generates specialized kernels for decode, prefill, and mixed workloads. Evaluated on Llama 3 8B on TPU7x, RPA achieves up to 86% memory bandwidth utilization (MBU) in decode and 73% model FLOPs utilization (MFU) in prefill. Integrated as the primary TPU backend in vLLM and SGLang, RPA provides a production-grade foundation for efficient TPU inference and offers practical insights into kernel design.
匹配关键词: vLLM
---

[ACADEMIC - ARXIV]
标题: Tool Attention Is All You Need: Dynamic Tool Gating and Lazy Schema Loading for Eliminating the MCP/Tools Tax in Scalable Agentic Workflows
作者: Anuj Sadani, Deepak Kumar
链接: https://arxiv.org/abs/2604.21816v1
完整摘要: The Model Context Protocol (MCP) has become a common interface for connecting large language model (LLM) agents to external tools, but its reliance on stateless, eager schema injection imposes a hidden per-turn overhead the MCP Tax or Tools Tax that practitioner reports place between roughly 10k and 60k tokens in typical multi-server deployments. This payload inflates the key-value cache, is associated with reasoning degradation as context utilization approaches published fracture points around 70%, and turns token budgets into a recurring operational cost. We introduce Tool Attention, a middleware-layer mechanism that generalizes the "Attention Is All You Need" paradigm from self-attention over tokens to gated attention over tools. Tool Attention combines (i) an Intent Schema Overlap (ISO) score from sentence embeddings, (ii) a state-aware gating function enforcing preconditions and access scopes, and (iii) a two-phase lazy schema loader that keeps a compact summary pool in context and promotes full JSON schemas only for top-k gated tools. We evaluate on a simulated 120-tool, six-server benchmark whose per-server token counts are calibrated to public audits of real MCP deployments. In this simulation, Tool Attention directly reduces measured per-turn tool tokens by 95.0% (47.3k -> 2.4k) and raises effective context utilization (a token-ratio quantity) from 24% to 91%. End-to-end figures for task success, latency, cost, and reasoning quality are reported as projections derived from the measured token counts combined with published deployment telemetry; they are not measured on live LLM agents, and we mark projected values explicitly throughout. Taken together, the results support a simple thesis: protocol-level efficiency, not raw context length, is a binding constraint on scalable gentic systems. The code for this work is accessible at https://github.com/asadani/tool-attention
匹配关键词: KV cache
---

[ACADEMIC - ARXIV]
标题: Learning to Communicate: Toward End-to-End Optimization of Multi-Agent Language Systems
作者: Ye Yu, Heming Liu, Haibo Jin, Xiaopeng Yuan, Peng Kuang, Haohan Wang
链接: https://arxiv.org/abs/2604.21794v1
完整摘要: Multi-agent systems built on large language models have shown strong performance on complex reasoning tasks, yet most work focuses on agent roles and orchestration while treating inter-agent communication as a fixed interface. Latent communication through internal representations such as key-value caches offers a promising alternative to text-based protocols, but existing approaches do not jointly optimize communication with multi-agent reasoning. Therefore we propose DiffMAS, a training framework that treats latent communication as a learnable component of multi-agent systems. DiffMAS performs parameter-efficient supervised training over multi-agent latent trajectories, enabling agents to jointly learn how information should be encoded and interpreted across interactions. Experiments on mathematical reasoning, scientific QA, code generation, and commonsense benchmarks show that DiffMAS consistently improves reasoning accuracy and decoding stability over single-agent inference, text-based multi-agent systems, and prior latent communication methods, achieving 26.7% on AIME24, 20.2% on GPQA-Diamond, and consistent gains across reasoning benchmarks.
匹配关键词: KV cache
---

[ACADEMIC - ARXIV]
标题: Hi-WM: Human-in-the-World-Model for Scalable Robot Post-Training
作者: Yaxuan Li, Zhongyi Zhou, Yefei Chen, Yanjiang Guo, Jiaming Liu, Shanghang Zhang, Jianyu Chen, Yichen Zhu
链接: https://arxiv.org/abs/2604.21741v1
完整摘要: Post-training is essential for turning pretrained generalist robot policies into reliable task-specific controllers, but existing human-in-the-loop pipelines remain tied to physical execution: each correction requires robot time, scene setup, resets, and operator supervision in the real world. Meanwhile, action-conditioned world models have been studied mainly for imagination, synthetic data generation, and policy evaluation. We propose \textbf{Human-in-the-World-Model (Hi-WM)}, a post-training framework that uses a learned world model as a reusable corrective substrate for failure-targeted policy improvement. A policy is first rolled out in closed loop inside the world model; when the rollout becomes incorrect or failure-prone, a human intervenes directly in the model to provide short corrective actions. Hi-WM caches intermediate states and supports rollback and branching, allowing a single failure state to be reused for multiple corrective continuations and yielding dense supervision around behaviors that the base policy handles poorly. The resulting corrective trajectories are then added back to the training set for post-training. We evaluate Hi-WM on three real-world manipulation tasks spanning both rigid and deformable object interaction, and on two policy backbones. Hi-WM improves real-world success by 37.9 points on average over the base policy and by 19.0 points over a world-model closed-loop baseline, while world-model evaluation correlates strongly with real-world performance (r = 0.953). These results suggest that world models can serve not only as generators or evaluators, but also as effective corrective substrates for scalable robot post-training.
匹配关键词: KV cache
---

[ACADEMIC - ARXIV]
标题: Ramen: Robust Test-Time Adaptation of Vision-Language Models with Active Sample Selection
作者: Wenxuan Bao, Yanjun Zhao, Xiyuan Yang, Jingrui He
链接: https://arxiv.org/abs/2604.21728v1
完整摘要: Pretrained vision-language models such as CLIP exhibit strong zero-shot generalization but remain sensitive to distribution shifts. Test-time adaptation adapts models during inference without access to source data or target labels, offering a practical way to handle such shifts. However, existing methods typically assume that test samples come from a single, consistent domain, while in practice, test data often include samples from mixed domains with distinct characteristics. Consequently, their performance degrades under mixed-domain settings. To address this, we present Ramen, a framework for robust test-time adaptation through active sample selection. For each incoming test sample, Ramen retrieves a customized batch of relevant samples from previously seen data based on two criteria: domain consistency, which ensures that adaptation focuses on data from similar domains, and prediction balance, which mitigates adaptation bias caused by skewed predictions. To improve efficiency, Ramen employs an embedding-gradient cache that stores the embeddings and sample-level gradients of past test images. The stored embeddings are used to retrieve relevant samples, and the corresponding gradients are aggregated for model updates, eliminating the need for any additional forward or backward passes. Our theoretical analysis provides insight into why the proposed adaptation mechanism is effective under mixed-domain shifts. Experiments on multiple image corruption and domain-shift benchmarks demonstrate that Ramen achieves strong and consistent performance, offering robust and efficient adaptation in complex mixed-domain scenarios. Our code is available at https://github.com/baowenxuan/Ramen .
匹配关键词: KV cache
---

[ACADEMIC - ARXIV]
标题: Prototype-Based Test-Time Adaptation of Vision-Language Models
作者: Zhaohong Huang, Yuxin Zhang, Wenjing Liu, Fei Chao, Rongrong Ji
链接: https://arxiv.org/abs/2604.21360v1
完整摘要: Test-time adaptation (TTA) has emerged as a promising paradigm for vision-language models (VLMs) to bridge the distribution gap between pre-training and test data. Recent works have focused on backpropagation-free TTA methods that rely on cache-based designs, but these introduce two key limitations. First, inference latency increases as the cache grows with the number of classes, leading to inefficiencies in large-scale settings. Second, suboptimal performance occurs when the cache contains insufficient or incorrect samples. In this paper, we present Prototype-Based Test-Time Adaptation (PTA), an efficient and effective TTA paradigm that uses a set of class-specific knowledge prototypes to accumulate knowledge from test samples. Particularly, knowledge prototypes are adaptively weighted based on the zero-shot class confidence of each test sample, incorporating the sample's visual features into the corresponding class-specific prototype. It is worth highlighting that the knowledge from past test samples is integrated and utilized solely in the prototypes, eliminating the overhead of cache population and retrieval that hinders the efficiency of existing TTA methods. This endows PTA with extremely high efficiency while achieving state-of-the-art performance on 15 image recognition benchmarks and 4 robust point cloud analysis benchmarks. For example, PTA improves CLIP's accuracy from 65.64% to 69.38% on 10 cross-domain benchmarks, while retaining 92% of CLIP's inference speed on large-scale ImageNet-1K. In contrast, the cache-based TDA achieves a lower accuracy of 67.97% and operates at only 50% of CLIP's inference speed.
匹配关键词: KV cache
---

[ACADEMIC - ARXIV]
标题: Bridging the Training-Deployment Gap: Gated Encoding and Multi-Scale Refinement for Efficient Quantization-Aware Image Enhancement
作者: Dat To-Thanh, Nghia Nguyen-Trong, Hoang Vo, Hieu Bui-Minh, Tinh-Anh Nguyen-Nhu
链接: https://arxiv.org/abs/2604.21743v1
完整摘要: Image enhancement models for mobile devices often struggle to balance high output quality with the fast processing speeds required by mobile hardware. While recent deep learning models can enhance low-quality mobile photos into high-quality images, their performance is often degraded when converted to lower-precision formats for actual use on mobile phones. To address this training-deployment mismatch, we propose an efficient image enhancement model designed specifically for mobile deployment. Our approach uses a hierarchical network architecture with gated encoder blocks and multiscale refinement to preserve fine-grained visual features. Moreover, we incorporate Quantization-Aware Training (QAT) to simulate the effects of low-precision representation during the training process. This allows the network to adapt and prevents the typical drop in quality seen with standard post-training quantization (PTQ). Experimental results demonstrate that the proposed method produces high-fidelity visual output while maintaining the low computational overhead needed for practical use on standard mobile devices. The code will be available at https://github.com/GenAI4E/QATIE.git.
匹配关键词: quantization
---

[ACADEMIC - ARXIV]
标题: GS-Quant: Granular Semantic and Generative Structural Quantization for Knowledge Graph Completion
作者: Qizhuo Xie, Yunhui Liu, Yu Xing, Qianzi Hou, Xudong Jin, Tao Zheng, Tieke He
链接: https://arxiv.org/abs/2604.21649v1
完整摘要: Large Language Models (LLMs) have shown immense potential in Knowledge Graph Completion (KGC), yet bridging the modality gap between continuous graph embeddings and discrete LLM tokens remains a critical challenge. While recent quantization-based approaches attempt to align these modalities, they typically treat quantization as flat numerical compression, resulting in semantically entangled codes that fail to mirror the hierarchical nature of human reasoning. In this paper, we propose GS-Quant, a novel framework that generates semantically coherent and structurally stratified discrete codes for KG entities. Unlike prior methods, GS-Quant is grounded in the insight that entity representations should follow a linguistic coarse-to-fine logic. We introduce a Granular Semantic Enhancement module that injects hierarchical knowledge into the codebook, ensuring that earlier codes capture global semantic categories while later codes refine specific attributes. Furthermore, a Generative Structural Reconstruction module imposes causal dependencies on the code sequence, transforming independent discrete units into structured semantic descriptors. By expanding the LLM vocabulary with these learned codes, we enable the model to reason over graph structures isomorphically to natural language generation. Experimental results demonstrate that GS-Quant significantly outperforms existing text-based and embedding-based baselines. Our code is publicly available at https://github.com/mikumifa/GS-Quant.
匹配关键词: quantization
---

[ACADEMIC - ARXIV]
标题: Large-Scale Data Parallelization of Product Quantization and Inverted Indexing Using Dask
作者: Ashley N. Abraham, Andrew Strelzoff, Haley R. Dozier, Althea C. Henslee, Mark A. Chappell
链接: https://arxiv.org/abs/2604.21645v1
完整摘要: Large-scale Nearest Neighbor (NN) search, though widely utilized in the similarity search field, remains challenged by the computational limitations inherent in processing large scale data. In an effort to decrease the computational expense needed, Approximate Nearest Neighbor (ANN) search is often used in applications that do not require the exact similarity search, but instead can rely on an approximation. Product Quantization (PQ) is a memory-efficient ANN effective for clustering all sizes of datasets. Clustering large-scale, high dimensional data requires a heavy computational expense, in both memory-cost and execution time. This work focuses on a unique way to divide and conquer the large scale data in Python using PQ, Inverted Indexing and Dask, combining the results without compromising the accuracy and reducing computational requirements to the level required when using medium-scale data.
匹配关键词: quantization
---

[ACADEMIC - ARXIV]
标题: On the Role of Preprocessing and Memristor Dynamics in Reservoir Computing for Image Classification
作者: Rishona Daniels, Duna Wattad, Ronny Ronen, David Saad, Shahar Kvatinsky
链接: https://arxiv.org/abs/2604.21602v1
完整摘要: Reservoir computing (RC) is an emerging recurrent neural network architecture that has attracted growing attention for its low training cost and modest hardware requirements. Memristor-based circuits are particularly promising for RC, as their intrinsic dynamics can reduce network size and parameter overhead in tasks such as time-series prediction and image recognition. Although RC has been demonstrated with several memristive devices, a comprehensive evaluation of device-level requirements remains limited. In this paper, we analyze and explain the operation of a parallel delayed feedback network (PDFN) RC architecture with volatile memristors, focusing on how device characteristics -- such as decay rate, quantization, and variability -- affect reservoir performance. We further discuss strategies to improve data representation in the reservoir using preprocessing methods and suggest potential improvements. The proposed approach achieves 95.89% classification accuracy on MNIST, comparable with the best reported memristor-based RC implementations. Furthermore, the method maintains high robustness under 20% device variability, achieving an accuracy of up to 94.2%. These results demonstrate that volatile memristors can support reliable spatio-temporal information processing and reinforce their potential as key building blocks for compact, high-speed, and energy-efficient neuromorphic computing systems.
匹配关键词: quantization
---

[ACADEMIC - ARXIV]
标题: ImageHD: Energy-Efficient On-Device Continual Learning of Visual Representations via Hyperdimensional Computing
作者: Jebacyril Arockiaraj, Dhruv Parikh, Viktor Prasanna
链接: https://arxiv.org/abs/2604.21280v1
完整摘要: On-device continual learning (CL) is critical for edge AI systems operating on non-stationary data streams, but most existing methods rely on backpropagation or exemplar-heavy classifiers, incurring substantial compute, memory, and latency overheads. Hyperdimensional computing (HDC) offers a lightweight alternative through fast, non-iterative online updates. Combined with a compact convolutional neural network (CNN) feature extractor, HDC enables efficient on-device adaptation with strong visual representations. However, prior HDC-based CL systems often depend on multi-tier memory hierarchies and complex cluster management, limiting deployability on resource-constrained hardware. We present ImageHD, an FPGA accelerator for on-device continual learning of visual data based on HDC. ImageHD targets streaming CL under strict latency and on-chip memory constraints, avoiding costly iterative optimization. At the algorithmic level, we introduce a hardware-aware CL method that bounds class exemplars through a unified exemplar memory and a hardware-efficient cluster merging strategy, while incorporating a quantized CNN front-end to reduce deployment overhead without sacrificing accuracy. At the system level, ImageHD is implemented as a streaming dataflow architecture on the AMD Zynq ZCU104 FPGA, integrating HDC encoding, similarity search, and bounded cluster management using word-packed binary hypervectors for massively parallel bitwise computation within tight on-chip resource budgets. On CORe50, ImageHD achieves up to 40.4x (4.84x) speedup and 383x (105.1x) energy efficiency over optimized CPU (GPU) baselines, demonstrating the practicality of HDC-enabled continual learning for real-time edge AI.
匹配关键词: quantization
---

[ACADEMIC - ARXIV]
标题: Evaluation of Automatic Speech Recognition Using Generative Large Language Models
作者: Thibault Bañeras-Roux, Shashi Kumar, Driss Khalil, Sergio Burdisso, Petr Motlicek, Shiran Liu, Mickael Rouvier, Jane Wottawa, Richard Dufour
链接: https://arxiv.org/abs/2604.21928v1
完整摘要: Automatic Speech Recognition (ASR) is traditionally evaluated using Word Error Rate (WER), a metric that is insensitive to meaning. Embedding-based semantic metrics are better correlated with human perception, but decoder-based Large Language Models (LLMs) remain underexplored for this task. This paper evaluates their relevance through three approaches: (1) selecting the best hypothesis between two candidates, (2) computing semantic distance using generative embeddings, and (3) qualitative classification of errors. On the HATS dataset, the best LLMs achieve 92--94\% agreement with human annotators for hypothesis selection, compared to 63\% for WER, also outperforming semantic metrics. Embeddings from decoder-based LLMs show performance comparable to encoder models. Finally, LLMs offer a promising direction for interpretable and semantic ASR evaluation.
匹配关键词: speculative decoding
---

[ACADEMIC - ARXIV]
标题: Addressing Image Authenticity When Cameras Use Generative AI
作者: Umar Masud, Abhijith Punnappurath, Luxi Zhao, David B. Lindell, Michael S. Brown
链接: https://arxiv.org/abs/2604.21879v1
完整摘要: The ability of generative AI (GenAI) methods to photorealistically alter camera images has raised awareness about the authenticity of images shared online. Interestingly, images captured directly by our cameras are considered authentic and faithful. However, with the increasing integration of deep-learning modules into cameras' capture-time hardware -- namely, the image signal processor (ISP) -- there is now a potential for hallucinated content in images directly output by our cameras. Hallucinated capture-time image content is typically benign, such as enhanced edges or texture, but in certain operations, such as AI-based digital zoom or low-light image enhancement, hallucinations can potentially alter the semantics and interpretation of the image content. As a result, users may not realize that the content in their camera images is not authentic. This paper addresses this issue by enabling users to recover the 'unhallucinated' version of the camera image to avoid misinterpretation of the image content. Our approach works by optimizing an image-specific multi-layer perceptron (MLP) decoder together with a modality-specific encoder so that, given the camera image, we can recover the image before hallucinated content was added. The encoder and MLP are self-contained and can be applied post-capture to the image without requiring access to the camera ISP. Moreover, the encoder and MLP decoder require only 180 KB of storage and can be readily saved as metadata within standard image formats such as JPEG and HEIC.
匹配关键词: speculative decoding
---

[ACADEMIC - ARXIV]
标题: Learning to Communicate: Toward End-to-End Optimization of Multi-Agent Language Systems
作者: Ye Yu, Heming Liu, Haibo Jin, Xiaopeng Yuan, Peng Kuang, Haohan Wang
链接: https://arxiv.org/abs/2604.21794v1
完整摘要: Multi-agent systems built on large language models have shown strong performance on complex reasoning tasks, yet most work focuses on agent roles and orchestration while treating inter-agent communication as a fixed interface. Latent communication through internal representations such as key-value caches offers a promising alternative to text-based protocols, but existing approaches do not jointly optimize communication with multi-agent reasoning. Therefore we propose DiffMAS, a training framework that treats latent communication as a learnable component of multi-agent systems. DiffMAS performs parameter-efficient supervised training over multi-agent latent trajectories, enabling agents to jointly learn how information should be encoded and interpreted across interactions. Experiments on mathematical reasoning, scientific QA, code generation, and commonsense benchmarks show that DiffMAS consistently improves reasoning accuracy and decoding stability over single-agent inference, text-based multi-agent systems, and prior latent communication methods, achieving 26.7% on AIME24, 20.2% on GPQA-Diamond, and consistent gains across reasoning benchmarks.
匹配关键词: speculative decoding
---

[ACADEMIC - ARXIV]
标题: To See the Unseen: on the Generalization Ability of Transformers in Symbolic Reasoning
作者: Nevena Lazić, Liam Fowl, András György, Csaba Szepesvári
链接: https://arxiv.org/abs/2604.21632v1
完整摘要: We investigate the ability of decoder-only transformer models to perform abstract symbolic reasoning; specifically solving propositional logic reasoning problems given in-context. Previous work demonstrated that models fail to generalize to problems involving variable names that were not observed during training, and it was shown that one reason behind this is the difficulty of copying (or generating) unseen tokens. We show both theoretically and empirically that a particular representational collapse also has a crucial role: the unembeddings (last-layer weights) of unseen tokens collapse to nearly the same vector during training. The collapse makes distinguishing multiple unseen variables difficult for the model (especially when the embedding and unembedding parameters are shared), and provides a mechanistic explanation for the effectiveness of existing heuristic interventions like "active forgetting", which periodically reset the token (un)embeddings. Based on these observations, we devise a combination of techniques, involving a small architecture change facilitating copying, data diversity, and freezing or resetting (un)embeddings, that achieves generalization to unseen tokens. We support our claims with extensive controlled experiments on propositional logic reasoning problems. Beyond synthetic experiments, we also observe evidence of (un)embedding collapse in the open-weight models in the Gemma 3 family, which includes 99 unused tokens reserved for downstream use. Empirically we find that the correlated embeddings of these tokens are a poor initialization for finetuning applications.
匹配关键词: speculative decoding
---

[ACADEMIC - ARXIV]
标题: OmniFit: Multi-modal 3D Body Fitting via Scale-agnostic Dense Landmark Prediction
作者: Zeyu Cai, Yuliang Xiu, Renke Wang, Zhijing Shao, Xiaoben Li, Siyuan Yu, Chao Xu, Yang Liu, Baigui Sun, Jian Yang, Zhenyu Zhang
链接: https://arxiv.org/abs/2604.21575v1
完整摘要: Fitting an underlying body model to 3D clothed human assets has been extensively studied, yet most approaches focus on either single-modal inputs such as point clouds or multi-view images alone, often requiring a known metric scale. This constraint is frequently impractical, especially for AI-generated assets where scale distortion is common. We propose OmniFit, a method that can seamlessly handle diverse multi-modal inputs, including full scans, partial depth observations, and image captures, while remaining scale-agnostic for both real and synthetic assets. Our key innovation is a simple yet effective conditional transformer decoder that directly maps surface points to dense body landmarks, which are then used for SMPL-X parameter fitting. In addition, an optional plug-and-play image adapter incorporates visual cues to compensate for missing geometric information. We further introduce a dedicated scale predictor that rescales subjects to canonical body proportions. OmniFit substantially outperforms state-of-the-art methods by 57.1 to 80.9 percent across daily and loose clothing scenarios. To the best of our knowledge, it is the first body fitting method to surpass multi-view optimization baselines and the first to achieve millimeter-level accuracy on the CAPE and 4D-DRESS benchmarks.
匹配关键词: speculative decoding
---

[ACADEMIC - ARXIV]
标题: Teacher-Guided Routing for Sparse Vision Mixture-of-Experts
作者: Masahiro Kada, Ryota Yoshihashi, Satoshi Ikehata, Rei Kawakami, Ikuro Sato
链接: https://arxiv.org/abs/2604.21330v1
完整摘要: Recent progress in deep learning has been driven by increasingly large-scale models, but the resulting computational cost has become a critical bottleneck. Sparse Mixture of Experts (MoE) offers an effective solution by activating only a small subset of experts for each input, achieving high scalability without sacrificing inference speed. Although effective, sparse MoE training exhibits characteristic optimization difficulties. Because the router receives informative gradients only through the experts selected in the forward pass, it suffers from gradient blocking and obtains little information from unselected routes. This limited, highly localized feedback makes it difficult for the router to learn appropriate expert-selection scores and often leads to unstable routing dynamics, such as fluctuating expert assignments during training. To address this issue, we propose TGR-MoE: Teacher-Guided Routing for Sparse Vision Mixture-of-Experts, a simple yet effective method that stabilizes router learning using supervision derived from a pretrained dense teacher model. TGR-MoE constructs a teacher router from the teacher's intermediate representations and uses its routing outputs as pseudo-supervision for the student router, suppressing frequent routing fluctuations during training and enabling knowledge-guided expert selection from the early stages of training. Extensive experiments on ImageNet-1K and CIFAR-100 demonstrate that TGR consistently improves both accuracy and routing consistency, while maintaining stable training even under highly sparse configurations.
匹配关键词: MoE
---

[ACADEMIC - ARXIV]
标题: Enhancing Online Recruitment with Category-Aware MoE and LLM-based Data Augmentation
作者: Minping Chen, Bing Xu, Zulong Chen, Chuanfei Xu, Ying Zhou, Zui Tao, Zeyi Wen
链接: https://arxiv.org/abs/2604.21264v1
完整摘要: Person-Job Fit (PJF) is a critical component for online recruitment. Existing approaches face several challenges, particularly in handling low-quality job descriptions and similar candidate-job pairs, which impair model performance. To address these challenges, this paper proposes a large language model (LLM) based method with two novel techniques: (1) LLM-based data augmentation, which polishes and rewrites low-quality job descriptions by leveraging chain-of-thought (COT) prompts, and (2) category-aware Mixture of Experts (MoE) that assists in identifying similar candidate-job pairs. This MoE module incorporates category embeddings to dynamically assign weights to the experts and learns more distinguishable patterns for similar candidate-job pairs. We perform offline evaluations and online A/B tests on our recruitment platform. Our method relatively surpasses existing methods by 2.40% in AUC and 7.46% in GAUC, and boosts click-through conversion rate (CTCVR) by 19.4% in online tests, saving millions of CNY in external headhunting expenses.
匹配关键词: MoE
---

[ACADEMIC - ARXIV]
标题: LLaDA2.0-Uni: Unifying Multimodal Understanding and Generation with Diffusion Large Language Model
作者: Inclusion AI, Tiwei Bie, Haoxing Chen, Tieyuan Chen, Zhenglin Cheng, Long Cui, Kai Gan, Zhicheng Huang, Zhenzhong Lan, Haoquan Li, Jianguo Li, Tao Lin, Qi Qin, Hongjun Wang, Xiaomei Wang, Haoyuan Wu, Yi Xin, Junbo Zhao
链接: https://arxiv.org/abs/2604.20796v1
完整摘要: We present LLaDA2.0-Uni, a unified discrete diffusion large language model (dLLM) that supports multimodal understanding and generation within a natively integrated framework. Its architecture combines a fully semantic discrete tokenizer, a MoE-based dLLM backbone, and a diffusion decoder. By discretizing continuous visual inputs via SigLIP-VQ, the model enables block-level masked diffusion for both text and vision inputs within the backbone, while the decoder reconstructs visual tokens into high-fidelity images. Inference efficiency is enhanced beyond parallel decoding through prefix-aware optimizations in the backbone and few-step distillation in the decoder. Supported by carefully curated large-scale data and a tailored multi-stage training pipeline, LLaDA2.0-Uni matches specialized VLMs in multimodal understanding while delivering strong performance in image generation and editing. Its native support for interleaved generation and reasoning establishes a promising and scalable paradigm for next-generation unified foundation models. Codes and models are available at https://github.com/inclusionAI/LLaDA2.0-Uni.
匹配关键词: MoE
---

[ACADEMIC - ARXIV]
标题: MD-Face: MoE-Enhanced Label-Free Disentangled Representation for Interactive Facial Attribute Editing
作者: Xuan Cui, Yunfei Zhao, Bo Liu, Wei Duan, Xingrong Fan
链接: https://arxiv.org/abs/2604.20317v1
完整摘要: GAN-based facial attribute editing is widely used in virtual avatars and social media but often suffers from attribute entanglement, where modifying one face attribute unintentionally alters others. While supervised disentangled representation learning can address this, it relies heavily on labeled data, incurring high annotation costs. To address these challenges, we propose MD-Face, a label-free disentangled representation learning framework based on Mixture of Experts (MoE). MD-Face utilizes a MoE backbone with a gating mechanism that dynamically allocates experts, enabling the model to learn semantic vectors with greater independence. To further enhance attribute entanglement, we introduce a geometry-aware loss, which aligns each semantic vector with its corresponding Semantic Boundary Vector (SBV) through a Jacobian-based pushforward method. Experiments with ProGAN and StyleGAN show that MD-Face outperforms unsupervised baselines and competes with supervised ones. Compared to diffusion-based methods, it offers better image quality and lower inference latency, making it ideal for interactive editing.
匹配关键词: MoE
---

[ACADEMIC - ARXIV]
标题: Multi-Perspective Evidence Synthesis and Reasoning for Unsupervised Multimodal Entity Linking
作者: Mo Zhou, Jianwei Wang, Kai Wang, Helen Paik, Ying Zhang, Wenjie Zhang
链接: https://arxiv.org/abs/2604.20283v1
完整摘要: Multimodal Entity Linking (MEL) is a fundamental task in data management that maps ambiguous mentions with diverse modalities to the multimodal entities in a knowledge base. However, most existing MEL approaches primarily focus on optimizing instance-centric features and evidence, leaving broader forms of evidence and their intricate interdependencies insufficiently explored. Motivated by the observation that human expert decision-making process relies on multi-perspective judgment, in this work, we propose MSR-MEL, a Multi-perspective Evidence Synthesis and Reasoning framework with Large Language Models (LLMs) for unsupervised MEL. Specifically, we adopt a two-stage framework: (1) Offline Multi-Perspective Evidence Synthesis constructs a comprehensive set of evidence. This includes instance-centric evidence capturing the instance-centric multimodal information of mentions and entities, group-level evidence that aggregates neighborhood information, lexical evidence based on string overlap ratio, and statistical evidence based on simple summary statistics. A core contribution of our framework is the synthesis of group-level evidence, which effectively aggregates vital neighborhood information by graph. We first construct LLM-enhanced contextualized graphs. Subsequently, different modalities are jointly aligned through an asymmetric teacher-student graph neural network. (2) Online Multi-Perspective Evidence Reasoning leverages the power of LLM as a reasoning module to analyze the correlation and semantics of the multi-perspective evidence to induce an effective ranking strategy for accurate entity linking without supervision. Extensive experiments on widely used MEL benchmarks demonstrate that MSR-MEL consistently outperforms state-of-the-art unsupervised methods. The source code of this paper was available at: https://anonymous.4open.science/r/MSR-MEL-C21E/.
匹配关键词: MoE
---

[ACADEMIC - ARXIV]
标题: Fine-Tuning Regimes Define Distinct Continual Learning Problems
作者: Paul-Tiberiu Iordache, Elena Burceanu
链接: https://arxiv.org/abs/2604.21927v1
完整摘要: Continual learning (CL) studies how models acquire tasks sequentially while retaining previously learned knowledge. Despite substantial progress in benchmarking CL methods, comparative evaluations typically keep the fine-tuning regime fixed. In this paper, we argue that the fine-tuning regime, defined by the trainable parameter subspace, is itself a key evaluation variable. We formalize adaptation regimes as projected optimization over fixed trainable subspaces, showing that changing the trainable depth alters the effective update signal through which both current task fitting and knowledge preservation operate. This analysis motivates the hypothesis that method comparisons need not be invariant across regimes. We test this hypothesis in task incremental CL, five trainable depth regimes, and four standard methods: online EWC, LwF, SI, and GEM. Across five benchmark datasets, namely MNIST, Fashion MNIST, KMNIST, QMNIST, and CIFAR-100, and across 11 task orders per dataset, we find that the relative ranking of methods is not consistently preserved across regimes. We further show that deeper adaptation regimes are associated with larger update magnitudes, higher forgetting, and a stronger relationship between the two. These results show that comparative conclusions in CL can depend strongly on the chosen fine-tuning regime, motivating regime-aware evaluation protocols that treat trainable depth as an explicit experimental factor.
匹配关键词: kernel optimization
---

[ACADEMIC - ARXIV]
标题: The Sample Complexity of Multicalibration
作者: Natalie Collina, Jiuyao Lu, Georgy Noarov, Aaron Roth
链接: https://arxiv.org/abs/2604.21923v1
完整摘要: We study the minimax sample complexity of multicalibration in the batch setting. A learner observes $n$ i.i.d. samples from an unknown distribution and must output a (possibly randomized) predictor whose population multicalibration error, measured by Expected Calibration Error (ECE), is at most $\varepsilon$ with respect to a given family of groups. For every fixed $κ> 0$, in the regime $|G|\le \varepsilon^{-κ}$, we prove that $\widetildeΘ(\varepsilon^{-3})$ samples are necessary and sufficient, up to polylogarithmic factors. The lower bound holds even for randomized predictors, and the upper bound is realized by a randomized predictor obtained via an online-to-batch reduction. This separates the sample complexity of multicalibration from that of marginal calibration, which scales as $\widetildeΘ(\varepsilon^{-2})$, and shows that mean-ECE multicalibration is as difficult in the batch setting as it is in the online setting, in contrast to marginal calibration which is strictly more difficult in the online setting. In contrast we observe that for $κ= 0$, the sample complexity of multicalibration remains $\widetildeΘ(\varepsilon^{-2})$ exhibiting a sharp threshold phenomenon. More generally, we establish matching upper and lower bounds, up to polylogarithmic factors, for a weighted $L_p$ multicalibration metric for all $1 \le p \le 2$, with optimal exponent $3/p$. We also extend the lower-bound template to a regular class of elicitable properties, and combine it with the online upper bounds of Hu et al. (2025) to obtain matching bounds for calibrating properties including expectiles and bounded-density quantiles.
匹配关键词: kernel optimization
---

[ACADEMIC - ARXIV]
标题: When Prompts Override Vision: Prompt-Induced Hallucinations in LVLMs
作者: Pegah Khayatan, Jayneel Parekh, Arnaud Dapogny, Mustafa Shukor, Alasdair Newson, Matthieu Cord
链接: https://arxiv.org/abs/2604.21911v1
完整摘要: Despite impressive progress in capabilities of large vision-language models (LVLMs), these systems remain vulnerable to hallucinations, i.e., outputs that are not grounded in the visual input. Prior work has attributed hallucinations in LVLMs to factors such as limitations of the vision backbone or the dominance of the language component, yet the relative importance of these factors remains unclear. To resolve this ambiguity, We propose HalluScope, a benchmark to better understand the extent to which different factors induce hallucinations. Our analysis indicates that hallucinations largely stem from excessive reliance on textual priors and background knowledge, especially information introduced through textual instructions. To mitigate hallucinations induced by textual instruction priors, we propose HalluVL-DPO, a framework for fine-tuning off-the-shelf LVLMs towards more visually grounded responses. HalluVL-DPO leverages preference optimization using a curated training dataset that we construct, guiding the model to prefer grounded responses over hallucinated ones. We demonstrate that our optimized model effectively mitigates the targeted hallucination failure mode, while preserving or improving performance on other hallucination benchmarks and visual capability evaluations. To support reproducibility and further research, we will publicly release our evaluation benchmark, preference training dataset, and code at https://pegah-kh.github.io/projects/prompts-override-vision/ .
匹配关键词: kernel optimization
---

[ACADEMIC - ARXIV]
标题: From Research Question to Scientific Workflow: Leveraging Agentic AI for Science Automation
作者: Bartosz Balis, Michal Orzechowski, Piotr Kica, Michal Dygas, Michal Kuszewski
链接: https://arxiv.org/abs/2604.21910v1
完整摘要: Scientific workflow systems automate execution -- scheduling, fault tolerance, resource management -- but not the semantic translation that precedes it. Scientists still manually convert research questions into workflow specifications, a task requiring both domain knowledge and infrastructure expertise. We propose an agentic architecture that closes this gap through three layers: an LLM interprets natural language into structured intents (semantic layer); validated generators produce reproducible workflow DAGs (deterministic layer); and domain experts author ``Skills'': markdown documents encoding vocabulary mappings, parameter constraints, and optimization strategies (knowledge layer). This decomposition confines LLM non-determinism to intent extraction: identical intents always yield identical workflows. We implement and evaluate the architecture on the 1000 Genomes population genetics workflow and Hyperflow WMS running on Kubernetes. In an ablation study on 150 queries, Skills raise full-match intent accuracy from 44% to 83%; skill-driven deferred workflow generation reduces data transfer by 92\%; and the end-to-end pipeline completes queries on Kubernetes with LLM overhead below 15 seconds and cost under $0.001 per query.
匹配关键词: kernel optimization
---

[ACADEMIC - ARXIV]
标题: Low-Rank Adaptation Redux for Large Models
作者: Bingcong Li, Yilang Zhang, Georgios B. Giannakis
链接: https://arxiv.org/abs/2604.21905v1
完整摘要: Low-rank adaptation (LoRA) has emerged as the de facto standard for parameter-efficient fine-tuning (PEFT) of foundation models, enabling the adaptation of billion-parameter networks with minimal computational and memory overhead. Despite its empirical success and rapid proliferation of variants, it remains elusive which architectural choices, optimization techniques, and deployment constraints should guide practical method selection. This overview revisits LoRA through the lens of signal processing (SP), bridging modern adapter designs with classical low-rank modeling tools and inverse problems, as well as highlighting how SP principles can inform principled advances of fine-tuning approaches. Rather than providing a comprehensive enumeration and empirical comparisons of LoRA variants, emphasis is placed on the technical mechanisms underpinning these approaches to justify their effectiveness. These advances are categorized into three complementary axes: architectural design, efficient optimization, and pertinent applications. The first axis builds on singular value decomposition (SVD)-based factorization, rank-augmentation constructions, and cross-layer tensorization, while the second axis deals with initialization, alternating solvers, gauge-invariant optimization, and parameterization-aware methods. Beyond fine-tuning, emerging applications of LoRA are accounted across the entire lifecycle of large models, ranging from pre- and post-training to serving/deployment. Finally, open research directions are outlined at the confluence of SP and deep learning to catalyze a bidirectional frontier: classical SP tools provide a principled vocabulary for designing principled PEFT methods, while the unique challenges facing modern deep learning, especially the overwhelming scale and prohibitive overhead, also offer new research lines benefiting the SP community in return.
匹配关键词: kernel optimization
---

[ACADEMIC - ARXIV]
标题: Temporal Taskification in Streaming Continual Learning: A Source of Evaluation Instability
作者: Nicolae Filat, Ahmed Hussain, Konstantinos Kalogiannis, Elena Burceanu
链接: https://arxiv.org/abs/2604.21930v1
完整摘要: Streaming Continual Learning (CL) typically converts a continuous stream into a sequence of discrete tasks through temporal partitioning. We argue that this temporal taskification step is not a neutral preprocessing choice, but a structural component of evaluation: different valid splits of the same stream can induce different CL regimes and therefore different benchmark conclusions. To study this effect, we introduce a taskification-level framework based on plasticity and stability profiles, a profile distance between taskifications, and Boundary-Profile Sensitivity (BPS), which diagnoses how strongly small boundary perturbations alter the induced regime before any CL model is trained. We evaluate continual finetuning, Experience Replay, Elastic Weight Consolidation, and Learning without Forgetting on network traffic forecasting with CESNET-Timeseries24, keeping the stream, model, and training budget fixed while varying only the temporal taskification. Across 9-, 30-, and 44-day splits, we observe substantial changes in forecasting error, forgetting, and backward transfer, showing that taskification alone can materially affect CL evaluation. We further find that shorter taskifications induce noisier distribution-level patterns, larger structural distances, and higher BPS, indicating greater sensitivity to boundary perturbations. These results show that benchmark conclusions in streaming CL depend not only on the learner and the data stream, but also on how that stream is taskified, motivating temporal taskification as a first-class evaluation variable.
匹配关键词: distributed training
---

[ACADEMIC - ARXIV]
标题: Long-Horizon Manipulation via Trace-Conditioned VLA Planning
作者: Isabella Liu, An-Chieh Cheng, Rui Yan, Geng Chen, Ri-Zhao Qiu, Xueyan Zou, Sha Yi, Hongxu Yin, Xiaolong Wang, Sifei Liu
链接: https://arxiv.org/abs/2604.21924v1
完整摘要: Long-horizon manipulation remains challenging for vision-language-action (VLA) policies: real tasks are multi-step, progress-dependent, and brittle to compounding execution errors. We present LoHo-Manip, a modular framework that scales short-horizon VLA execution to long-horizon instruction following via a dedicated task-management VLM. The manager is decoupled from the executor and is invoked in a receding-horizon manner: given the current observation, it predicts a progress-aware remaining plan that combines (i) a subtask sequence with an explicit done + remaining split as lightweight language memory, and (ii) a visual trace -- a compact 2D keypoint trajectory prompt specifying where to go and what to approach next. The executor VLA is adapted to condition on the rendered trace, thereby turning long-horizon decision-making into repeated local control by following the trace. Crucially, predicting the remaining plan at each step yields an implicit closed loop: failed steps persist in subsequent outputs, and traces update accordingly, enabling automatic continuation and replanning without hand-crafted recovery logic or brittle visual-history buffers. Extensive experiments spanning embodied planning, long-horizon reasoning, trajectory prediction, and end-to-end manipulation in simulation and on a real Franka robot demonstrate strong gains in long-horizon success, robustness, and out-of-distribution generalization. Project page: https://www.liuisabella.com/LoHoManip
匹配关键词: distributed training
---

[ACADEMIC - ARXIV]
标题: The Sample Complexity of Multicalibration
作者: Natalie Collina, Jiuyao Lu, Georgy Noarov, Aaron Roth
链接: https://arxiv.org/abs/2604.21923v1
完整摘要: We study the minimax sample complexity of multicalibration in the batch setting. A learner observes $n$ i.i.d. samples from an unknown distribution and must output a (possibly randomized) predictor whose population multicalibration error, measured by Expected Calibration Error (ECE), is at most $\varepsilon$ with respect to a given family of groups. For every fixed $κ> 0$, in the regime $|G|\le \varepsilon^{-κ}$, we prove that $\widetildeΘ(\varepsilon^{-3})$ samples are necessary and sufficient, up to polylogarithmic factors. The lower bound holds even for randomized predictors, and the upper bound is realized by a randomized predictor obtained via an online-to-batch reduction. This separates the sample complexity of multicalibration from that of marginal calibration, which scales as $\widetildeΘ(\varepsilon^{-2})$, and shows that mean-ECE multicalibration is as difficult in the batch setting as it is in the online setting, in contrast to marginal calibration which is strictly more difficult in the online setting. In contrast we observe that for $κ= 0$, the sample complexity of multicalibration remains $\widetildeΘ(\varepsilon^{-2})$ exhibiting a sharp threshold phenomenon. More generally, we establish matching upper and lower bounds, up to polylogarithmic factors, for a weighted $L_p$ multicalibration metric for all $1 \le p \le 2$, with optimal exponent $3/p$. We also extend the lower-bound template to a regular class of elicitable properties, and combine it with the online upper bounds of Hu et al. (2025) to obtain matching bounds for calibrating properties including expectiles and bounded-density quantiles.
匹配关键词: distributed training
---

[ACADEMIC - ARXIV]
标题: Context Unrolling in Omni Models
作者: Ceyuan Yang, Zhijie Lin, Yang Zhao, Fei Xiao, Hao He, Qi Zhao, Chaorui Deng, Kunchang Li, Zihan Ding, Yuwei Guo, Fuyun Wang, Fangqi Zhu, Xiaonan Nie, Shenhan Zhu, Shanchuan Lin, Hongsheng Li, Weilin Huang, Guang Shi, Haoqi Fan
链接: https://arxiv.org/abs/2604.21921v1
完整摘要: We present Omni, a unified multimodal model natively trained on diverse modalities, including text, images, videos, 3D geometry, and hidden representations. We find that such training enables Context Unrolling, where the model explicitly reasons across multiple modal representations before producing predictions. This process enables the model to aggregate complementary information across heterogeneous modalities, facilitating a more faithful approximation of the shared multimodal knowledge manifold and improving downstream reasoning fidelity. As a result, Omni achieves strong performance on both multimodal generation and understanding benchmarks, while demonstrating advanced multimodal reasoning capabilities, including in-context generation of text, image, video, and 3D geometry.
匹配关键词: distributed training
---

[ACADEMIC - ARXIV]
标题: Vista4D: Video Reshooting with 4D Point Clouds
作者: Kuan Heng Lin, Zhizheng Liu, Pablo Salamanca, Yash Kant, Ryan Burgert, Yuancheng Xu, Koichi Namekata, Yiwei Zhao, Bolei Zhou, Micah Goldblum, Paul Debevec, Ning Yu
链接: https://arxiv.org/abs/2604.21915v1
完整摘要: We present Vista4D, a robust and flexible video reshooting framework that grounds the input video and target cameras in a 4D point cloud. Specifically, given an input video, our method re-synthesizes the scene with the same dynamics from a different camera trajectory and viewpoint. Existing video reshooting methods often struggle with depth estimation artifacts of real-world dynamic videos, while also failing to preserve content appearance and failing to maintain precise camera control for challenging new trajectories. We build a 4D-grounded point cloud representation with static pixel segmentation and 4D reconstruction to explicitly preserve seen content and provide rich camera signals, and we train with reconstructed multiview dynamic data for robustness against point cloud artifacts during real-world inference. Our results demonstrate improved 4D consistency, camera control, and visual quality compared to state-of-the-art baselines under a variety of videos and camera paths. Moreover, our method generalizes to real-world applications such as dynamic scene expansion and 4D scene recomposition. See our project page for results, code, and models: https://eyeline-labs.github.io/Vista4D
匹配关键词: distributed training
---

[ACADEMIC - ARXIV]
标题: Seeing Without Eyes: 4D Human-Scene Understanding from Wearable IMUs
作者: Hao-Yu Hsu, Tianhang Cheng, Jing Wen, Alexander G. Schwing, Shenlong Wang
链接: https://arxiv.org/abs/2604.21926v1
完整摘要: Understanding human activities and their surrounding environments typically relies on visual perception, yet cameras pose persistent challenges in privacy, safety, energy efficiency, and scalability. We explore an alternative: 4D perception without vision. Its goal is to reconstruct human motion and 3D scene layouts purely from everyday wearable sensors. For this we introduce IMU-to-4D, a framework that repurposes large language models for non-visual spatiotemporal understanding of human-scene dynamics. IMU-to-4D uses data from a few inertial sensors from earbuds, watches, or smartphones and predicts detailed 4D human motion together with coarse scene structure. Experiments across diverse human-scene datasets show that IMU-to-4D yields more coherent and temporally stable results than SoTA cascaded pipelines, suggesting wearable motion sensors alone can support rich 4D understanding.
匹配关键词: memory efficiency
---

[ACADEMIC - ARXIV]
标题: Long-Horizon Manipulation via Trace-Conditioned VLA Planning
作者: Isabella Liu, An-Chieh Cheng, Rui Yan, Geng Chen, Ri-Zhao Qiu, Xueyan Zou, Sha Yi, Hongxu Yin, Xiaolong Wang, Sifei Liu
链接: https://arxiv.org/abs/2604.21924v1
完整摘要: Long-horizon manipulation remains challenging for vision-language-action (VLA) policies: real tasks are multi-step, progress-dependent, and brittle to compounding execution errors. We present LoHo-Manip, a modular framework that scales short-horizon VLA execution to long-horizon instruction following via a dedicated task-management VLM. The manager is decoupled from the executor and is invoked in a receding-horizon manner: given the current observation, it predicts a progress-aware remaining plan that combines (i) a subtask sequence with an explicit done + remaining split as lightweight language memory, and (ii) a visual trace -- a compact 2D keypoint trajectory prompt specifying where to go and what to approach next. The executor VLA is adapted to condition on the rendered trace, thereby turning long-horizon decision-making into repeated local control by following the trace. Crucially, predicting the remaining plan at each step yields an implicit closed loop: failed steps persist in subsequent outputs, and traces update accordingly, enabling automatic continuation and replanning without hand-crafted recovery logic or brittle visual-history buffers. Extensive experiments spanning embodied planning, long-horizon reasoning, trajectory prediction, and end-to-end manipulation in simulation and on a real Franka robot demonstrate strong gains in long-horizon success, robustness, and out-of-distribution generalization. Project page: https://www.liuisabella.com/LoHoManip
匹配关键词: memory efficiency
---

[ACADEMIC - ARXIV]
标题: Directional Confusions Reveal Divergent Inductive Biases Through Rate-Distortion Geometry in Human and Machine Vision
作者: Leyla Roksan Caglar, Pedro A. M. Mediano, Baihan Lin
链接: https://arxiv.org/abs/2604.21909v1
完整摘要: Humans and modern vision models can reach similar classification accuracy while making systematically different kinds of mistakes - differing not in how often they err, but in who gets mistaken for whom, and in which direction. We show that these directional confusions reveal distinct inductive biases that are invisible to accuracy alone. Using matched human and deep vision model responses on a natural-image categorization task under 12 perturbation types, we quantify asymmetry in confusion matrices and link it to generalization geometry through a Rate-Distortion (RD) framework, summarized by three geometric signatures (slope (beta), curvature (kappa)) and efficiency (AUC). We find that humans exhibit broad but weak asymmetries, whereas deep vision models show sparser, stronger directional collapses. Robustness training reduces global asymmetry but fails to recover the human-like breadth-strength profile of graded similarity. Mechanistic simulations further show that different asymmetry organizations shift the RD frontier in opposite directions, even when matched for performance. Together, these results position directional confusions and RD geometry as compact, interpretable signatures of inductive bias under distribution shift.
匹配关键词: memory efficiency
---

[ACADEMIC - ARXIV]
标题: Low-Rank Adaptation Redux for Large Models
作者: Bingcong Li, Yilang Zhang, Georgios B. Giannakis
链接: https://arxiv.org/abs/2604.21905v1
完整摘要: Low-rank adaptation (LoRA) has emerged as the de facto standard for parameter-efficient fine-tuning (PEFT) of foundation models, enabling the adaptation of billion-parameter networks with minimal computational and memory overhead. Despite its empirical success and rapid proliferation of variants, it remains elusive which architectural choices, optimization techniques, and deployment constraints should guide practical method selection. This overview revisits LoRA through the lens of signal processing (SP), bridging modern adapter designs with classical low-rank modeling tools and inverse problems, as well as highlighting how SP principles can inform principled advances of fine-tuning approaches. Rather than providing a comprehensive enumeration and empirical comparisons of LoRA variants, emphasis is placed on the technical mechanisms underpinning these approaches to justify their effectiveness. These advances are categorized into three complementary axes: architectural design, efficient optimization, and pertinent applications. The first axis builds on singular value decomposition (SVD)-based factorization, rank-augmentation constructions, and cross-layer tensorization, while the second axis deals with initialization, alternating solvers, gauge-invariant optimization, and parameterization-aware methods. Beyond fine-tuning, emerging applications of LoRA are accounted across the entire lifecycle of large models, ranging from pre- and post-training to serving/deployment. Finally, open research directions are outlined at the confluence of SP and deep learning to catalyze a bidirectional frontier: classical SP tools provide a principled vocabulary for designing principled PEFT methods, while the unique challenges facing modern deep learning, especially the overwhelming scale and prohibitive overhead, also offer new research lines benefiting the SP community in return.
匹配关键词: memory efficiency
---

[ACADEMIC - ARXIV]
标题: GiVA: Gradient-Informed Bases for Vector-Based Adaptation
作者: Neeraj Gangwar, Rishabh Deshmukh, Michael Shavlovsky, Hancao Li, Vivek Mittal, Lexing Ying, Nickvash Kani
链接: https://arxiv.org/abs/2604.21901v1
完整摘要: As model sizes continue to grow, parameter-efficient fine-tuning has emerged as a powerful alternative to full fine-tuning. While LoRA is widely adopted among these methods, recent research has explored vector-based adaptation methods due to their extreme parameter efficiency. However, these methods typically require substantially higher ranks than LoRA to match its performance, leading to increased training costs. This work introduces GiVA, a gradient-based initialization strategy for vector-based adaptation. It achieves training times comparable to LoRA and maintains the extreme parameter efficiency of vector-based adaptation. We evaluate GiVA across diverse benchmarks, including natural language understanding, natural language generation, and image classification. Experiments show that our approach consistently outperforms or achieves performance competitive with existing vector-based adaptation methods and LoRA while reducing rank requirements by a factor of eight ($8\times$).
匹配关键词: memory efficiency
---

[ACADEMIC - ARXIV]
标题: Automatic Ontology Construction Using LLMs as an External Layer of Memory, Verification, and Planning for Hybrid Intelligent Systems
作者: Pavel Salovskii, Iuliia Gorshkova
链接: https://arxiv.org/abs/2604.20795v1
完整摘要: This paper presents a hybrid architecture for intelligent systems in which large language models (LLMs) are extended with an external ontological memory layer. Instead of relying solely on parametric knowledge and vector-based retrieval (RAG), the proposed approach constructs and maintains a structured knowledge graph using RDF/OWL representations, enabling persistent, verifiable, and semantically grounded reasoning. The core contribution is an automated pipeline for ontology construction from heterogeneous data sources, including documents, APIs, and dialogue logs. The system performs entity recognition, relation extraction, normalization, and triple generation, followed by validation using SHACL and OWL constraints, and continuous graph updates. During inference, LLMs operate over a combined context that integrates vector-based retrieval with graph-based reasoning and external tool interaction. Experimental observations on planning tasks, including the Tower of Hanoi benchmark, indicate that ontology augmentation improves performance in multi-step reasoning scenarios compared to baseline LLM systems. In addition, the ontology layer enables formal validation of generated outputs, transforming the system into a generation-verification-correction pipeline. The proposed architecture addresses key limitations of current LLM-based systems, including lack of long-term memory, weak structural understanding, and limited reasoning capabilities. It provides a foundation for building agent-based systems, robotics applications, and enterprise AI solutions that require persistent knowledge, explainability, and reliable decision-making.
匹配关键词: RAG
---

[ACADEMIC - ARXIV]
标题: Coverage, Not Averages: Semantic Stratification for Trustworthy Retrieval Evaluation
作者: Andrew Klearman, Radu Revutchi, Rohin Garg, Rishav Chakravarti, Samuel Marc Denton, Yuan Xue
链接: https://arxiv.org/abs/2604.20763v1
完整摘要: Retrieval quality is the primary bottleneck for accuracy and robustness in retrieval-augmented generation (RAG). Current evaluation relies on heuristically constructed query sets, which introduce a hidden intrinsic bias. We formalize retrieval evaluation as a statistical estimation problem, showing that metric reliability is fundamentally limited by the evaluation-set construction. We further introduce \emph{semantic stratification}, which grounds evaluation in corpus structure by organizing documents into an interpretable global space of entity-based clusters and systematically generating queries for missing strata. This yields (1) formal semantic coverage guarantees across retrieval regimes and (2) interpretable visibility into retrieval failure modes. Experiments across multiple benchmarks and retrieval methods validate our framework. The results expose systematic coverage gaps, identify structural signals that explain variance in retrieval performance, and show that stratified evaluation yields more stable and transparent assessments while supporting more trustworthy decision-making than aggregate metrics.
匹配关键词: RAG
---

[ACADEMIC - ARXIV]
标题: Self-Aware Vector Embeddings for Retrieval-Augmented Generation: A Neuroscience-Inspired Framework for Temporal, Confidence-Weighted, and Relational Knowledge
作者: Naizhong Xu
链接: https://arxiv.org/abs/2604.20598v1
完整摘要: Modern retrieval-augmented generation (RAG) systems treat vector embeddings as static, context-free artifacts: an embedding has no notion of when it was created, how trustworthy its source is, or which other embeddings depend on it. This flattening of knowledge has a measurable cost: recent work on VersionRAG reports that conventional RAG achieves only 58% accuracy on versioned technical queries, because retrieval returns semantically similar but temporally invalid content. We propose SmartVector, a framework that augments dense embeddings with three explicit properties -- temporal awareness, confidence decay, and relational awareness -- and a five-stage lifecycle modeled on hippocampal-neocortical memory consolidation. A retrieval pipeline replaces pure cosine similarity with a four-signal score that mixes semantic relevance, temporal validity, live confidence, and graph-relational importance. A background consolidation agent detects contradictions, builds dependency edges, and propagates updates along those edges as graph-neural-network-style messages. Confidence is governed by a closed-form function combining an Ebbinghaus-style exponential decay, user-feedback reconsolidation, and logarithmic access reinforcement. We formalize the model, relate it to temporal knowledge graph embedding, agentic memory architectures, and uncertainty-aware RAG, and present a reference implementation. On a reproducible synthetic versioned-policy benchmark of 258 vectors and 138 queries, SmartVector roughly doubles top-1 accuracy over plain cosine RAG (62.0% vs. 31.0% on a held-out split), drops stale-answer rate from 35.0% to 13.3%, cuts Expected Calibration Error by nearly 2x (0.244 vs. 0.470), reduces re-embedding cost per single-word edit by 77%, and is robust across contradiction-injection rates from 0% to 75%.
匹配关键词: RAG
---

[ACADEMIC - ARXIV]
标题: Knowledge Capsules: Structured Nonparametric Memory Units for LLMs
作者: Bin Ju, Shenfeng Weng, Danying Zhou, Rongkai Xu, Kunkai Su
链接: https://arxiv.org/abs/2604.20487v2
完整摘要: Large language models (LLMs) encode knowledge in parametric weights, making it costly to update or extend without retraining. Retrieval-augmented generation (RAG) mitigates this limitation by appending retrieved text to the input, but operates purely through context expansion, where external knowledge competes as tokens within the attention mechanism. As a result, its influence is indirect and often unstable, particularly in long context and multi hop reasoning scenarios. We propose Knowledge Capsules, structured nonparametric memory units that represent normalized relational knowledge and can be constructed directly from document corpora using a frozen base model. Instead of injecting knowledge as text, we introduce an External Key Value Injection (KVI) framework that compiles capsules into attention-compatible key value representations, enabling external knowledge to directly participate in the model's attention computation. By shifting knowledge integration from context-level augmentation to memory level interaction, the proposed framework consistently outperforms RAG and GraphRAG across multiple QA benchmarks, with improved stability and accuracy in long context and multi hop reasoning, while requiring no parameter updates.
匹配关键词: RAG
---

[ACADEMIC - ARXIV]
标题: Adaptive Defense Orchestration for RAG: A Sentinel-Strategist Architecture against Multi-Vector Attacks
作者: Pranav Pallerla, Wilson Naik Bhukya, Bharath Vemula, Charan Ramtej Kodi
链接: https://arxiv.org/abs/2604.20932v1
完整摘要: Retrieval-augmented generation (RAG) systems are increasingly deployed in sensitive domains such as healthcare and law, where they rely on private, domain-specific knowledge. This capability introduces significant security risks, including membership inference, data poisoning, and unintended content leakage. A straightforward mitigation is to enable all relevant defenses simultaneously, but doing so incurs a substantial utility cost. In our experiments, an always-on defense stack reduces contextual recall by more than 40%, indicating that retrieval degradation is the primary failure mode. To mitigate this trade-off in RAG systems, we propose the Sentinel-Strategist architecture, a context-aware framework for risk analysis and defense selection. A Sentinel detects anomalous retrieval behavior, after which a Strategist selectively deploys only the defenses warranted by the query context. Evaluated across three benchmark datasets and five orchestration models, ADO is shown to eliminate MBA-style membership inference leakage while substantially recovering retrieval utility relative to a fully static defense stack, approaching undefended baseline levels. Under data poisoning, the strongest ADO variants reduce attack success to near zero while restoring contextual recall to more than 75% of the undefended baseline, although robustness remains sensitive to model choice. Overall, these findings show that adaptive, query-aware defense can substantially reduce the security-utility trade-off in RAG systems.
匹配关键词: RAG
---

[ACADEMIC - ARXIV]
标题: Seeing Fast and Slow: Learning the Flow of Time in Videos
作者: Yen-Siang Wu, Rundong Luo, Jingsen Zhu, Tao Tu, Ali Farhadi, Matthew Wallingford, Yu-Chiang Frank Wang, Steve Marschner, Wei-Chiu Ma
链接: https://arxiv.org/abs/2604.21931v1
完整摘要: How can we tell whether a video has been sped up or slowed down? How can we generate videos at different speeds? Although videos have been central to modern computer vision research, little attention has been paid to perceiving and controlling the passage of time. In this paper, we study time as a learnable visual concept and develop models for reasoning about and manipulating the flow of time in videos. We first exploit the multimodal cues and temporal structure naturally present in videos to learn, in a self-supervised manner, to detect speed changes and estimate playback speed. We then show that these learned temporal reasoning models enable us to curate the largest slow-motion video dataset to date from noisy in-the-wild sources. Such slow-motion footage, typically filmed by high-speed cameras, contains substantially richer temporal detail than standard videos. Using this data, we further develop models capable of temporal control, including speed-conditioned video generation, which produces motion at specified playback speed, and temporal super-resolution, which tranforms low-FPS, blurry videos into high-FPS sequences with fine-grained temporal details. Our findings highlight time as a manipulable, perceptual dimension in video learning, opening doors to temporally controllable video generation, temporal forensics detection, and potentially richer world-models that understand how events unfold over time.
匹配关键词: code generation
---

[ACADEMIC - ARXIV]
标题: Evaluation of Automatic Speech Recognition Using Generative Large Language Models
作者: Thibault Bañeras-Roux, Shashi Kumar, Driss Khalil, Sergio Burdisso, Petr Motlicek, Shiran Liu, Mickael Rouvier, Jane Wottawa, Richard Dufour
链接: https://arxiv.org/abs/2604.21928v1
完整摘要: Automatic Speech Recognition (ASR) is traditionally evaluated using Word Error Rate (WER), a metric that is insensitive to meaning. Embedding-based semantic metrics are better correlated with human perception, but decoder-based Large Language Models (LLMs) remain underexplored for this task. This paper evaluates their relevance through three approaches: (1) selecting the best hypothesis between two candidates, (2) computing semantic distance using generative embeddings, and (3) qualitative classification of errors. On the HATS dataset, the best LLMs achieve 92--94\% agreement with human annotators for hypothesis selection, compared to 63\% for WER, also outperforming semantic metrics. Embeddings from decoder-based LLMs show performance comparable to encoder models. Finally, LLMs offer a promising direction for interpretable and semantic ASR evaluation.
匹配关键词: code generation
---

[ACADEMIC - ARXIV]
标题: Long-Horizon Manipulation via Trace-Conditioned VLA Planning
作者: Isabella Liu, An-Chieh Cheng, Rui Yan, Geng Chen, Ri-Zhao Qiu, Xueyan Zou, Sha Yi, Hongxu Yin, Xiaolong Wang, Sifei Liu
链接: https://arxiv.org/abs/2604.21924v1
完整摘要: Long-horizon manipulation remains challenging for vision-language-action (VLA) policies: real tasks are multi-step, progress-dependent, and brittle to compounding execution errors. We present LoHo-Manip, a modular framework that scales short-horizon VLA execution to long-horizon instruction following via a dedicated task-management VLM. The manager is decoupled from the executor and is invoked in a receding-horizon manner: given the current observation, it predicts a progress-aware remaining plan that combines (i) a subtask sequence with an explicit done + remaining split as lightweight language memory, and (ii) a visual trace -- a compact 2D keypoint trajectory prompt specifying where to go and what to approach next. The executor VLA is adapted to condition on the rendered trace, thereby turning long-horizon decision-making into repeated local control by following the trace. Crucially, predicting the remaining plan at each step yields an implicit closed loop: failed steps persist in subsequent outputs, and traces update accordingly, enabling automatic continuation and replanning without hand-crafted recovery logic or brittle visual-history buffers. Extensive experiments spanning embodied planning, long-horizon reasoning, trajectory prediction, and end-to-end manipulation in simulation and on a real Franka robot demonstrate strong gains in long-horizon success, robustness, and out-of-distribution generalization. Project page: https://www.liuisabella.com/LoHoManip
匹配关键词: code generation
---

[ACADEMIC - ARXIV]
标题: The Sample Complexity of Multicalibration
作者: Natalie Collina, Jiuyao Lu, Georgy Noarov, Aaron Roth
链接: https://arxiv.org/abs/2604.21923v1
完整摘要: We study the minimax sample complexity of multicalibration in the batch setting. A learner observes $n$ i.i.d. samples from an unknown distribution and must output a (possibly randomized) predictor whose population multicalibration error, measured by Expected Calibration Error (ECE), is at most $\varepsilon$ with respect to a given family of groups. For every fixed $κ> 0$, in the regime $|G|\le \varepsilon^{-κ}$, we prove that $\widetildeΘ(\varepsilon^{-3})$ samples are necessary and sufficient, up to polylogarithmic factors. The lower bound holds even for randomized predictors, and the upper bound is realized by a randomized predictor obtained via an online-to-batch reduction. This separates the sample complexity of multicalibration from that of marginal calibration, which scales as $\widetildeΘ(\varepsilon^{-2})$, and shows that mean-ECE multicalibration is as difficult in the batch setting as it is in the online setting, in contrast to marginal calibration which is strictly more difficult in the online setting. In contrast we observe that for $κ= 0$, the sample complexity of multicalibration remains $\widetildeΘ(\varepsilon^{-2})$ exhibiting a sharp threshold phenomenon. More generally, we establish matching upper and lower bounds, up to polylogarithmic factors, for a weighted $L_p$ multicalibration metric for all $1 \le p \le 2$, with optimal exponent $3/p$. We also extend the lower-bound template to a regular class of elicitable properties, and combine it with the online upper bounds of Hu et al. (2025) to obtain matching bounds for calibrating properties including expectiles and bounded-density quantiles.
匹配关键词: code generation
---

[ACADEMIC - ARXIV]
标题: Context Unrolling in Omni Models
作者: Ceyuan Yang, Zhijie Lin, Yang Zhao, Fei Xiao, Hao He, Qi Zhao, Chaorui Deng, Kunchang Li, Zihan Ding, Yuwei Guo, Fuyun Wang, Fangqi Zhu, Xiaonan Nie, Shenhan Zhu, Shanchuan Lin, Hongsheng Li, Weilin Huang, Guang Shi, Haoqi Fan
链接: https://arxiv.org/abs/2604.21921v1
完整摘要: We present Omni, a unified multimodal model natively trained on diverse modalities, including text, images, videos, 3D geometry, and hidden representations. We find that such training enables Context Unrolling, where the model explicitly reasons across multiple modal representations before producing predictions. This process enables the model to aggregate complementary information across heterogeneous modalities, facilitating a more faithful approximation of the shared multimodal knowledge manifold and improving downstream reasoning fidelity. As a result, Omni achieves strong performance on both multimodal generation and understanding benchmarks, while demonstrating advanced multimodal reasoning capabilities, including in-context generation of text, image, video, and 3D geometry.
匹配关键词: code generation
---

[ACADEMIC - ARXIV]
标题: Temporal Taskification in Streaming Continual Learning: A Source of Evaluation Instability
作者: Nicolae Filat, Ahmed Hussain, Konstantinos Kalogiannis, Elena Burceanu
链接: https://arxiv.org/abs/2604.21930v1
完整摘要: Streaming Continual Learning (CL) typically converts a continuous stream into a sequence of discrete tasks through temporal partitioning. We argue that this temporal taskification step is not a neutral preprocessing choice, but a structural component of evaluation: different valid splits of the same stream can induce different CL regimes and therefore different benchmark conclusions. To study this effect, we introduce a taskification-level framework based on plasticity and stability profiles, a profile distance between taskifications, and Boundary-Profile Sensitivity (BPS), which diagnoses how strongly small boundary perturbations alter the induced regime before any CL model is trained. We evaluate continual finetuning, Experience Replay, Elastic Weight Consolidation, and Learning without Forgetting on network traffic forecasting with CESNET-Timeseries24, keeping the stream, model, and training budget fixed while varying only the temporal taskification. Across 9-, 30-, and 44-day splits, we observe substantial changes in forecasting error, forgetting, and backward transfer, showing that taskification alone can materially affect CL evaluation. We further find that shorter taskifications induce noisier distribution-level patterns, larger structural distances, and higher BPS, indicating greater sensitivity to boundary perturbations. These results show that benchmark conclusions in streaming CL depend not only on the learner and the data stream, but also on how that stream is taskified, motivating temporal taskification as a first-class evaluation variable.
匹配关键词: LLM evaluation
---

[ACADEMIC - ARXIV]
标题: Evaluation of Automatic Speech Recognition Using Generative Large Language Models
作者: Thibault Bañeras-Roux, Shashi Kumar, Driss Khalil, Sergio Burdisso, Petr Motlicek, Shiran Liu, Mickael Rouvier, Jane Wottawa, Richard Dufour
链接: https://arxiv.org/abs/2604.21928v1
完整摘要: Automatic Speech Recognition (ASR) is traditionally evaluated using Word Error Rate (WER), a metric that is insensitive to meaning. Embedding-based semantic metrics are better correlated with human perception, but decoder-based Large Language Models (LLMs) remain underexplored for this task. This paper evaluates their relevance through three approaches: (1) selecting the best hypothesis between two candidates, (2) computing semantic distance using generative embeddings, and (3) qualitative classification of errors. On the HATS dataset, the best LLMs achieve 92--94\% agreement with human annotators for hypothesis selection, compared to 63\% for WER, also outperforming semantic metrics. Embeddings from decoder-based LLMs show performance comparable to encoder models. Finally, LLMs offer a promising direction for interpretable and semantic ASR evaluation.
匹配关键词: LLM evaluation
---

[ACADEMIC - ARXIV]
标题: Fine-Tuning Regimes Define Distinct Continual Learning Problems
作者: Paul-Tiberiu Iordache, Elena Burceanu
链接: https://arxiv.org/abs/2604.21927v1
完整摘要: Continual learning (CL) studies how models acquire tasks sequentially while retaining previously learned knowledge. Despite substantial progress in benchmarking CL methods, comparative evaluations typically keep the fine-tuning regime fixed. In this paper, we argue that the fine-tuning regime, defined by the trainable parameter subspace, is itself a key evaluation variable. We formalize adaptation regimes as projected optimization over fixed trainable subspaces, showing that changing the trainable depth alters the effective update signal through which both current task fitting and knowledge preservation operate. This analysis motivates the hypothesis that method comparisons need not be invariant across regimes. We test this hypothesis in task incremental CL, five trainable depth regimes, and four standard methods: online EWC, LwF, SI, and GEM. Across five benchmark datasets, namely MNIST, Fashion MNIST, KMNIST, QMNIST, and CIFAR-100, and across 11 task orders per dataset, we find that the relative ranking of methods is not consistently preserved across regimes. We further show that deeper adaptation regimes are associated with larger update magnitudes, higher forgetting, and a stronger relationship between the two. These results show that comparative conclusions in CL can depend strongly on the chosen fine-tuning regime, motivating regime-aware evaluation protocols that treat trainable depth as an explicit experimental factor.
匹配关键词: LLM evaluation
---

[ACADEMIC - ARXIV]
标题: MathDuels: Evaluating LLMs as Problem Posers and Solvers
作者: Zhiqiu Xu, Shibo Jin, Shreya Arya, Mayur Naik
链接: https://arxiv.org/abs/2604.21916v1
完整摘要: As frontier language models attain near-ceiling performance on static mathematical benchmarks, existing evaluations are increasingly unable to differentiate model capabilities, largely because they cast models solely as solvers of fixed problem sets. We introduce MathDuels, a self-play benchmark in which models occupy dual roles: each authors math problems under adversarial prompting and solves problems authored by every other participant. Problems are produced through a three-stage generation pipeline (meta-prompting, problem generation, and difficulty amplification), and validated by an independent verifier that excludes ill-posed questions. A Rasch model (Rasch, 1993) jointly estimates solver abilities and problem difficulties; author quality is derived from the difficulties of each model's authored problems. Experiments across 19 frontier models reveal that authoring and solving capabilities are partially decoupled, and that dual-role evaluation reveals capability separations invisible in single-role benchmarks. As newer models enter the arena, they produce problems that defeat previously dominant solvers, so the benchmark's difficulty co-evolves with participant strength rather than saturating at a fixed ceiling. We host a public leaderboard that updates as new models are released.
匹配关键词: LLM evaluation
---

[ACADEMIC - ARXIV]
标题: VistaBot: View-Robust Robot Manipulation via Spatiotemporal-Aware View Synthesis
作者: Songen Gu, Yuhang Zheng, Weize Li, Yupeng Zheng, Yating Feng, Xiang Li, Yilun Chen, Pengfei Li, Wenchao Ding
链接: https://arxiv.org/abs/2604.21914v1
完整摘要: Recently, end-to-end robotic manipulation models have gained significant attention for their generalizability and scalability. However, they often suffer from limited robustness to camera viewpoint changes when training with a fixed camera. In this paper, we propose VistaBot, a novel framework that integrates feed-forward geometric models with video diffusion models to achieve view-robust closed-loop manipulation without requiring camera calibration at test time. Our approach consists of three key components: 4D geometry estimation, view synthesis latent extraction, and latent action learning. VistaBot is integrated into both action-chunking (ACT) and diffusion-based ($π_0$) policies and evaluated across simulation and real-world tasks. We further introduce the View Generalization Score (VGS) as a new metric for comprehensive evaluation of cross-view generalization. Results show that VistaBot improves VGS by 2.79$\times$ and 2.63$\times$ over ACT and $π_0$, respectively, while also achieving high-quality novel view synthesis. Our contributions include a geometry-aware synthesis model, a latent action planner, a new benchmark metric, and extensive validation across diverse environments. The code and models will be made publicly available.
匹配关键词: LLM evaluation
---

[ACADEMIC - ARXIV]
标题: Temporal Taskification in Streaming Continual Learning: A Source of Evaluation Instability
作者: Nicolae Filat, Ahmed Hussain, Konstantinos Kalogiannis, Elena Burceanu
链接: https://arxiv.org/abs/2604.21930v1
完整摘要: Streaming Continual Learning (CL) typically converts a continuous stream into a sequence of discrete tasks through temporal partitioning. We argue that this temporal taskification step is not a neutral preprocessing choice, but a structural component of evaluation: different valid splits of the same stream can induce different CL regimes and therefore different benchmark conclusions. To study this effect, we introduce a taskification-level framework based on plasticity and stability profiles, a profile distance between taskifications, and Boundary-Profile Sensitivity (BPS), which diagnoses how strongly small boundary perturbations alter the induced regime before any CL model is trained. We evaluate continual finetuning, Experience Replay, Elastic Weight Consolidation, and Learning without Forgetting on network traffic forecasting with CESNET-Timeseries24, keeping the stream, model, and training budget fixed while varying only the temporal taskification. Across 9-, 30-, and 44-day splits, we observe substantial changes in forecasting error, forgetting, and backward transfer, showing that taskification alone can materially affect CL evaluation. We further find that shorter taskifications induce noisier distribution-level patterns, larger structural distances, and higher BPS, indicating greater sensitivity to boundary perturbations. These results show that benchmark conclusions in streaming CL depend not only on the learner and the data stream, but also on how that stream is taskified, motivating temporal taskification as a first-class evaluation variable.
匹配关键词: benchmark
---

[ACADEMIC - ARXIV]
标题: Fine-Tuning Regimes Define Distinct Continual Learning Problems
作者: Paul-Tiberiu Iordache, Elena Burceanu
链接: https://arxiv.org/abs/2604.21927v1
完整摘要: Continual learning (CL) studies how models acquire tasks sequentially while retaining previously learned knowledge. Despite substantial progress in benchmarking CL methods, comparative evaluations typically keep the fine-tuning regime fixed. In this paper, we argue that the fine-tuning regime, defined by the trainable parameter subspace, is itself a key evaluation variable. We formalize adaptation regimes as projected optimization over fixed trainable subspaces, showing that changing the trainable depth alters the effective update signal through which both current task fitting and knowledge preservation operate. This analysis motivates the hypothesis that method comparisons need not be invariant across regimes. We test this hypothesis in task incremental CL, five trainable depth regimes, and four standard methods: online EWC, LwF, SI, and GEM. Across five benchmark datasets, namely MNIST, Fashion MNIST, KMNIST, QMNIST, and CIFAR-100, and across 11 task orders per dataset, we find that the relative ranking of methods is not consistently preserved across regimes. We further show that deeper adaptation regimes are associated with larger update magnitudes, higher forgetting, and a stronger relationship between the two. These results show that comparative conclusions in CL can depend strongly on the chosen fine-tuning regime, motivating regime-aware evaluation protocols that treat trainable depth as an explicit experimental factor.
匹配关键词: benchmark
---

[ACADEMIC - ARXIV]
标题: Context Unrolling in Omni Models
作者: Ceyuan Yang, Zhijie Lin, Yang Zhao, Fei Xiao, Hao He, Qi Zhao, Chaorui Deng, Kunchang Li, Zihan Ding, Yuwei Guo, Fuyun Wang, Fangqi Zhu, Xiaonan Nie, Shenhan Zhu, Shanchuan Lin, Hongsheng Li, Weilin Huang, Guang Shi, Haoqi Fan
链接: https://arxiv.org/abs/2604.21921v1
完整摘要: We present Omni, a unified multimodal model natively trained on diverse modalities, including text, images, videos, 3D geometry, and hidden representations. We find that such training enables Context Unrolling, where the model explicitly reasons across multiple modal representations before producing predictions. This process enables the model to aggregate complementary information across heterogeneous modalities, facilitating a more faithful approximation of the shared multimodal knowledge manifold and improving downstream reasoning fidelity. As a result, Omni achieves strong performance on both multimodal generation and understanding benchmarks, while demonstrating advanced multimodal reasoning capabilities, including in-context generation of text, image, video, and 3D geometry.
匹配关键词: benchmark
---

[ACADEMIC - ARXIV]
标题: MathDuels: Evaluating LLMs as Problem Posers and Solvers
作者: Zhiqiu Xu, Shibo Jin, Shreya Arya, Mayur Naik
链接: https://arxiv.org/abs/2604.21916v1
完整摘要: As frontier language models attain near-ceiling performance on static mathematical benchmarks, existing evaluations are increasingly unable to differentiate model capabilities, largely because they cast models solely as solvers of fixed problem sets. We introduce MathDuels, a self-play benchmark in which models occupy dual roles: each authors math problems under adversarial prompting and solves problems authored by every other participant. Problems are produced through a three-stage generation pipeline (meta-prompting, problem generation, and difficulty amplification), and validated by an independent verifier that excludes ill-posed questions. A Rasch model (Rasch, 1993) jointly estimates solver abilities and problem difficulties; author quality is derived from the difficulties of each model's authored problems. Experiments across 19 frontier models reveal that authoring and solving capabilities are partially decoupled, and that dual-role evaluation reveals capability separations invisible in single-role benchmarks. As newer models enter the arena, they produce problems that defeat previously dominant solvers, so the benchmark's difficulty co-evolves with participant strength rather than saturating at a fixed ceiling. We host a public leaderboard that updates as new models are released.
匹配关键词: benchmark
---

[ACADEMIC - ARXIV]
标题: VistaBot: View-Robust Robot Manipulation via Spatiotemporal-Aware View Synthesis
作者: Songen Gu, Yuhang Zheng, Weize Li, Yupeng Zheng, Yating Feng, Xiang Li, Yilun Chen, Pengfei Li, Wenchao Ding
链接: https://arxiv.org/abs/2604.21914v1
完整摘要: Recently, end-to-end robotic manipulation models have gained significant attention for their generalizability and scalability. However, they often suffer from limited robustness to camera viewpoint changes when training with a fixed camera. In this paper, we propose VistaBot, a novel framework that integrates feed-forward geometric models with video diffusion models to achieve view-robust closed-loop manipulation without requiring camera calibration at test time. Our approach consists of three key components: 4D geometry estimation, view synthesis latent extraction, and latent action learning. VistaBot is integrated into both action-chunking (ACT) and diffusion-based ($π_0$) policies and evaluated across simulation and real-world tasks. We further introduce the View Generalization Score (VGS) as a new metric for comprehensive evaluation of cross-view generalization. Results show that VistaBot improves VGS by 2.79$\times$ and 2.63$\times$ over ACT and $π_0$, respectively, while also achieving high-quality novel view synthesis. Our contributions include a geometry-aware synthesis model, a latent action planner, a new benchmark metric, and extensive validation across diverse environments. The code and models will be made publicly available.
匹配关键词: benchmark
---

[ACADEMIC - ARXIV]
标题: When Prompts Override Vision: Prompt-Induced Hallucinations in LVLMs
作者: Pegah Khayatan, Jayneel Parekh, Arnaud Dapogny, Mustafa Shukor, Alasdair Newson, Matthieu Cord
链接: https://arxiv.org/abs/2604.21911v1
完整摘要: Despite impressive progress in capabilities of large vision-language models (LVLMs), these systems remain vulnerable to hallucinations, i.e., outputs that are not grounded in the visual input. Prior work has attributed hallucinations in LVLMs to factors such as limitations of the vision backbone or the dominance of the language component, yet the relative importance of these factors remains unclear. To resolve this ambiguity, We propose HalluScope, a benchmark to better understand the extent to which different factors induce hallucinations. Our analysis indicates that hallucinations largely stem from excessive reliance on textual priors and background knowledge, especially information introduced through textual instructions. To mitigate hallucinations induced by textual instruction priors, we propose HalluVL-DPO, a framework for fine-tuning off-the-shelf LVLMs towards more visually grounded responses. HalluVL-DPO leverages preference optimization using a curated training dataset that we construct, guiding the model to prefer grounded responses over hallucinated ones. We demonstrate that our optimized model effectively mitigates the targeted hallucination failure mode, while preserving or improving performance on other hallucination benchmarks and visual capability evaluations. To support reproducibility and further research, we will publicly release our evaluation benchmark, preference training dataset, and code at https://pegah-kh.github.io/projects/prompts-override-vision/ .
匹配关键词: hallucination
---

[ACADEMIC - ARXIV]
标题: Addressing Image Authenticity When Cameras Use Generative AI
作者: Umar Masud, Abhijith Punnappurath, Luxi Zhao, David B. Lindell, Michael S. Brown
链接: https://arxiv.org/abs/2604.21879v1
完整摘要: The ability of generative AI (GenAI) methods to photorealistically alter camera images has raised awareness about the authenticity of images shared online. Interestingly, images captured directly by our cameras are considered authentic and faithful. However, with the increasing integration of deep-learning modules into cameras' capture-time hardware -- namely, the image signal processor (ISP) -- there is now a potential for hallucinated content in images directly output by our cameras. Hallucinated capture-time image content is typically benign, such as enhanced edges or texture, but in certain operations, such as AI-based digital zoom or low-light image enhancement, hallucinations can potentially alter the semantics and interpretation of the image content. As a result, users may not realize that the content in their camera images is not authentic. This paper addresses this issue by enabling users to recover the 'unhallucinated' version of the camera image to avoid misinterpretation of the image content. Our approach works by optimizing an image-specific multi-layer perceptron (MLP) decoder together with a modality-specific encoder so that, given the camera image, we can recover the image before hallucinated content was added. The encoder and MLP are self-contained and can be applied post-capture to the image without requiring access to the camera ISP. Moreover, the encoder and MLP decoder require only 180 KB of storage and can be readily saved as metadata within standard image formats such as JPEG and HEIC.
匹配关键词: hallucination
---

[ACADEMIC - ARXIV]
标题: Job Skill Extraction via LLM-Centric Multi-Module Framework
作者: Guojing Li, Zichuan Fu, Junyi Li, Faxue Liu, Wenxia Zhou, Yejing Wang, Jingtong Gao, Maolin Wang, Rungen Liu, Wenlin Zhang, Xiangyu Zhao
链接: https://arxiv.org/abs/2604.21525v1
完整摘要: Span-level skill extraction from job advertisements underpins candidate-job matching and labor-market analytics, yet generative large language models (LLMs) often yield malformed spans, boundary drift, and hallucinations, especially with long-tail terms and cross-domain shift. We present SRICL, an LLM-centric framework that combines semantic retrieval (SR), in-context learning (ICL), and supervised fine-tuning (SFT) with a deterministic verifier. SR pulls in-domain annotated sentences and definitions from ESCO to form format-constrained prompts that stabilize boundaries and handle coordination. SFT aligns output behavior, while the verifier enforces pairing, non-overlap, and BIO legality with minimal retries. On six public span-labeled corpora of job-ad sentences across sectors and languages, SRICL achieves substantial STRICT-F1 improvements over GPT-3.5 prompting baselines and sharply reduces invalid tags and hallucinated spans, enabling dependable sentence-level deployment in low-resource, multi-domain settings.
匹配关键词: hallucination
---

[ACADEMIC - ARXIV]
标题: Seeing Isn't Believing: Uncovering Blind Spots in Evaluator Vision-Language Models
作者: Mohammed Safi Ur Rahman Khan, Sanjay Suryanarayanan, Tushar Anand, Mitesh M. Khapra
链接: https://arxiv.org/abs/2604.21523v1
完整摘要: Large Vision-Language Models (VLMs) are increasingly used to evaluate outputs of other models, for image-to-text (I2T) tasks such as visual question answering, and text-to-image (T2I) generation tasks. Despite this growing reliance, the reliability of these Evaluator VLMs remains under explored. In this work, we systematically evaluate the reliability of Evaluator VLMs across both I2T and T2I tasks. We introduce targeted perturbations that degrade output quality along key error dimensions, including object hallucinations, spatial reasoning, factual grounding, and visual fidelity. These perturbations test whether Evaluator VLMs can reliably account for these quality degrading errors in their evaluations. Using a comprehensive benchmark of over 4000 perturbed instances spanning 40 perturbation dimensions, we evaluate 4 prominent VLMs using single-answer scoring, pairwise comparison, and reference-guided paradigms. Our findings reveal that current VLM evaluators exhibit substantial blind spots: they often fail to detect perturbed outputs - in some cases exceeding 50%, struggle particularly with fine-grained compositional and spatial errors, and are often insensitive to hallucinated content that contradicts the input image. Pairwise comparison proves more reliable, though failure rates persist. These results highlight the unreliable nature of current Evaluator VLMs and urge caution in their deployment for benchmarking and development decisions. Code and data have been made publicly available.
匹配关键词: hallucination
---

[ACADEMIC - ARXIV]
标题: Preferences of a Voice-First Nation: Large-Scale Pairwise Evaluation and Preference Analysis for TTS in Indian Languages
作者: Srija Anand, Ashwin Sankar, Ishvinder Sethi, Aaditya Pareek, Kartik Rajput, Gaurav Yadav, Nikhil Narasimhan, Adish Pandya, Deepon Halder, Mohammed Safi Ur Rahman Khan, Praveen S, Shobhit Banga, Mitesh M Khapra
链接: https://arxiv.org/abs/2604.21481v1
完整摘要: Crowdsourced pairwise evaluation has emerged as a scalable approach for assessing foundation models. However, applying it to Text to Speech(TTS) introduces high variance due to linguistic diversity and multidimensional nature of speech perception. We present a controlled multidimensional pairwise evaluation framework for multilingual TTS that combines linguistic control with perceptually grounded annotation. Using 5K+ native and code-mixed sentences across 10 Indic languages, we evaluate 7 state-of-the-art TTS systems and collect over 120K pairwise comparisons from over 1900 native raters. In addition to overall preference, raters provide judgments across 6 perceptual dimensions: intelligibility, expressiveness, voice quality, liveliness, noise, and hallucinations. Using Bradley-Terry modeling, we construct a multilingual leaderboard, interpret human preference using SHAP analysis and analyze leaderboard reliability alongside model strengths and trade-offs across perceptual dimensions.
匹配关键词: hallucination
---

[ACADEMIC - ARXIV]
标题: Seeing Without Eyes: 4D Human-Scene Understanding from Wearable IMUs
作者: Hao-Yu Hsu, Tianhang Cheng, Jing Wen, Alexander G. Schwing, Shenlong Wang
链接: https://arxiv.org/abs/2604.21926v1
完整摘要: Understanding human activities and their surrounding environments typically relies on visual perception, yet cameras pose persistent challenges in privacy, safety, energy efficiency, and scalability. We explore an alternative: 4D perception without vision. Its goal is to reconstruct human motion and 3D scene layouts purely from everyday wearable sensors. For this we introduce IMU-to-4D, a framework that repurposes large language models for non-visual spatiotemporal understanding of human-scene dynamics. IMU-to-4D uses data from a few inertial sensors from earbuds, watches, or smartphones and predicts detailed 4D human motion together with coarse scene structure. Experiments across diverse human-scene datasets show that IMU-to-4D yields more coherent and temporally stable results than SoTA cascaded pipelines, suggesting wearable motion sensors alone can support rich 4D understanding.
匹配关键词: safety
---

[ACADEMIC - ARXIV]
标题: Transient Turn Injection: Exposing Stateless Multi-Turn Vulnerabilities in Large Language Models
作者: Naheed Rayhan, Sohely Jahan
链接: https://arxiv.org/abs/2604.21860v1
完整摘要: Large language models (LLMs) are increasingly integrated into sensitive workflows, raising the stakes for adversarial robustness and safety. This paper introduces Transient Turn Injection(TTI), a new multi-turn attack technique that systematically exploits stateless moderation by distributing adversarial intent across isolated interactions. TTI leverages automated attacker agents powered by large language models to iteratively test and evade policy enforcement in both commercial and open-source LLMs, marking a departure from conventional jailbreak approaches that typically depend on maintaining persistent conversational context. Our extensive evaluation across state-of-the-art models-including those from OpenAI, Anthropic, Google Gemini, Meta, and prominent open-source alternatives-uncovers significant variations in resilience to TTI attacks, with only select architectures exhibiting substantial inherent robustness. Our automated blackbox evaluation framework also uncovers previously unknown model specific vulnerabilities and attack surface patterns, especially within medical and high stakes domains. We further compare TTI against established adversarial prompting methods and detail practical mitigation strategies, such as session level context aggregation and deep alignment approaches. Our study underscores the urgent need for holistic, context aware defenses and continuous adversarial testing to future proof LLM deployments against evolving multi-turn threats.
匹配关键词: safety
---

[ACADEMIC - ARXIV]
标题: Bounding the Black Box: A Statistical Certification Framework for AI Risk Regulation
作者: Natan Levy, Gadi Perl
链接: https://arxiv.org/abs/2604.21854v1
完整摘要: Artificial intelligence now decides who receives a loan, who is flagged for criminal investigation, and whether an autonomous vehicle brakes in time. Governments have responded: the EU AI Act, the NIST Risk Management Framework, and the Council of Europe Convention all demand that high-risk systems demonstrate safety before deployment. Yet beneath this regulatory consensus lies a critical vacuum: none specifies what ``acceptable risk'' means in quantitative terms, and none provides a technical method for verifying that a deployed system actually meets such a threshold. The regulatory architecture is in place; the verification instrument is not. This gap is not theoretical. As the EU AI Act moves into full enforcement, developers face mandatory conformity assessments without established methodologies for producing quantitative safety evidence - and the systems most in need of oversight are opaque statistical inference engines that resist white-box scrutiny. This paper provides the missing instrument. Drawing on the aviation certification paradigm, we propose a two-stage framework that transforms AI risk regulation into engineering practice. In Stage One, a competent authority formally fixes an acceptable failure probability $δ$ and an operational input domain $\varepsilon$ - a normative act with direct civil liability implications. In Stage Two, the RoMA and gRoMA statistical verification tools compute a definitive, auditable upper bound on the system's true failure rate, requiring no access to model internals and scaling to arbitrary architectures. We demonstrate how this certificate satisfies existing regulatory obligations, shifts accountability upstream to developers, and integrates with the legal frameworks that exist today.
匹配关键词: safety
---

[ACADEMIC - ARXIV]
标题: TraceScope: Interactive URL Triage via Decoupled Checklist Adjudication
作者: Haolin Zhang, William Reber, Yuxuan Zhang, Guofei Gu, Jeff Huang
链接: https://arxiv.org/abs/2604.21840v1
完整摘要: Modern phishing campaigns increasingly evade snapshot-based URL classifiers using interaction gates (e.g., checkbox/slider challenges), delayed content rendering, and logo-less credential harvesters. This shifts URL triage from static classification toward an interactive forensics task: an analyst must actively navigate the page while isolating themselves from potential runtime exploits. We present TraceScope, a decoupled triage pipeline that operationalizes this workflow at scale. To prevent the observer effect and ensure safety, a sandboxed operator agent drives a real GUI browser guided by visual motivation to elicit page behavior, freezing the session into an immutable evidence bundle. Separately, an adjudicator agent circumvents LLM context limitations by querying evidence on demand to verify a MITRE ATT&CK checklist, and generates an audit-ready report with extracted indicators of compromise (IOCs) and a final verdict. Evaluated on 708 reachable URLs from existing dataset (241 verified phishing from PhishTank and 467 benign from Tranco-derived crawling), TraceScope achieves 0.94 precision and 0.78 recall, substantially improving recall over three prior visual/reference-based classifiers while producing reproducible, analyst-grade evidence suitable for review. More importantly, we manually curated a dataset of real-world phishing emails to evaluate our system in a practical setting. Our evaluation reveals that TraceScope demonstrates superior performance in a real-world scenario as well, successfully detecting sophisticated phishing attempts that current state-of-the-art defenses fail to identify.
匹配关键词: safety
---

[ACADEMIC - ARXIV]
标题: Enabling and Inhibitory Pathways of University Students' Willingness to Disclose AI Use: A Cognition-Affect-Conation Perspective
作者: Yiran Du, Huimin He
链接: https://arxiv.org/abs/2604.21733v1
完整摘要: The increasing integration of artificial intelligence (AI) in higher education has raised important questions regarding students' transparency in reporting AI-assisted work. This study investigates the psychological mechanisms underlying university students' willingness to disclose AI use by applying the Cognition--Affect--Conation (CAC) framework. A sequential explanatory mixed-methods design was employed. In the quantitative phase, survey data were collected from 546 university students and analysed using structural equation modelling to examine the relationships among cognitive perceptions, affective responses, and disclosure intention. In the qualitative phase, semi-structured interviews with 22 students were conducted to further interpret the quantitative findings. The results indicate that psychological safety significantly increases students' willingness to disclose AI use and is positively shaped by perceived fairness, perceived teacher support, and perceived organisational support. Conversely, evaluation apprehension reduces disclosure intention and psychological safety, and is strengthened by perceived stigma, perceived uncertainty, and privacy concern. Qualitative findings further reveal that institutional clarity and supportive instructional practices encourage openness, whereas policy ambiguity and fear of negative evaluation often lead students to adopt cautious or strategic disclosure practices. Overall, the study highlights the dual role of enabling and inhibitory psychological mechanisms in shaping AI-use disclosure and underscores the importance of supportive institutional environments and clear guidance for promoting responsible AI transparency in higher education.
匹配关键词: safety
---

