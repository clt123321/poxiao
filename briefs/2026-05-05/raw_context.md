# 破晓 PoXiao — 原始数据 (Raw Context)
生成时间: 2026-05-05 10:27 UTC
================================================================================

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

[RSS:Reddit LocalLLaMA (社区共识)]
DeepSeek V4 Pro matches GPT-5.2 on FoodTruck Bench, our agentic benchmark — 10 weeks later, ~17× cheaper
https://www.reddit.com/r/LocalLLaMA/comments/1t47qbw/deepseek_v4_pro_matches_gpt52_on_foodtruck_bench/
Tested DeepSeek V4 Pro on FoodTruck Bench — our 30-day agentic benchmark where models run a food truck via 34 tools (locations, pricing, inventory, staff, weather, events) with persistent memory and daily reflection. First Chinese model to land in the frontier tier on our benchmark. Tied with Grok 4
---

[RSS:Reddit LocalLLaMA (社区共识)]
vibevoice.cpp: Microsoft VibeVoice (TTS + long-form ASR with diarization) ported to ggml/C++, runs on CPU/CUDA/Metal/Vulkan, no Python at inference
https://www.reddit.com/r/LocalLLaMA/comments/1t48fkt/vibevoicecpp_microsoft_vibevoice_tts_longform_asr/
A few weeks ago I shipped vibevoice.cpp , a pure-C++ ggml port of Microsoft VibeVoice (the speech-to-speech model with voice cloning, https://github.com/microsoft/VibeVoice ). Wanted to post a follow-up here because we're at a point where the engine has grown well past &quot;first-pass port&quot; an
---

[RSS:Reddit LocalLLaMA (社区共识)]
White House Considers Vetting A.I. Models Before They Are Released
https://www.reddit.com/r/LocalLLaMA/comments/1t3ro1w/white_house_considers_vetting_ai_models_before/
&#32; submitted by &#32; /u/fallingdowndizzyvr [link] &#32; [comments]
---

[RSS:Reddit LocalLLaMA (社区共识)]
As MTP prepares to land in llama.cpp, Models that support MTP
https://www.reddit.com/r/LocalLLaMA/comments/1t46o09/as_mtp_prepares_to_land_in_llamacpp_models_that/
DeepSeekv3 OG DeepSeekv3.2/4 Qwen3.5 GLM4.5+ MiniMax2.5+ Step3.5Flash Mimo v2+ Until we get mtp weights, you need to download HF weights and convert to gguf. I think I'm going to try either qwen3.5-122b or glm4.5-air first. &#32; submitted by &#32; /u/segmond [link] &#32; [comments]
---

[RSS:Reddit LocalLLaMA (社区共识)]
vLLM Just Merged TurboQuant Fix for Qwen 3.5+
https://www.reddit.com/r/LocalLLaMA/comments/1t3zu7u/vllm_just_merged_turboquant_fix_for_qwen_35/
Previously it was throwing a 'Not Implemented' error due to Mamba layers. Going to test it now! https://github.com/vllm-project/vllm/pull/39931 Edit: Works with Qwen 3.6, tested with 27B Can be used with argument; --kv-cache-dtype turboquant_4bit_nc Other available options; turboquant_k8v4 turboquan
---

[RSS:Reddit LocalLLaMA (社区共识)]
Llama.cpp MTP support now in beta!
https://www.reddit.com/r/LocalLLaMA/comments/1t3guzw/llamacpp_mtp_support_now_in_beta/
Happy to report that llama.cpp MTP support is now in beta, thanks to Aman (and all the others that have pushed the various issues in the meantime). This has the potential to actually get merged soon-ish. Currently contains support for Qwen3.5 MTP, but other models are likely to follow suit. Between 
---

[RSS:Reddit LocalLLaMA (社区共识)]
FastDMS: 6.4X KV-cache compression running faster than vLLM BF16/FP8
https://www.reddit.com/r/LocalLLaMA/comments/1t3vlrx/fastdms_64x_kvcache_compression_running_faster/
Last year researchers affiliated with NVIDIA, University of Warsaw, and University of Edinburgh published Dynamic Memory Sparsification (DMS) , a KV-cache sparsification technique using learned per-head token eviction, reporting up to 8x KV-cache compression. I found the results intriguing to build 
---

[RSS:Reddit LocalLLaMA (社区共识)]
MTPLX | 2.24x faster TPS | The native MTP inference engine for Apple Silicon
https://www.reddit.com/r/LocalLLaMA/comments/1t3zuvy/mtplx_224x_faster_tps_the_native_mtp_inference/
TLDR: 28 tok/s → 63 tok/s on Qwen3.6-27B on a MacBook Pro M5 Max. 2.24× faster at real temperature 0.6. Works for coding, creative writing, and chat https://i.redd.it/i9x794c0q7zg1.gif Works on ANY MTP model: No external drafter. No extra memory usage. Uses the model's own built-in MTP heads. Works 
---

[RSS:Reddit LocalLLaMA (社区共识)]
US GUARD Act: Age Verification for AI Chatbots
https://www.reddit.com/r/LocalLLaMA/comments/1t465yx/us_guard_act_age_verification_for_ai_chatbots/
There's been a growing number of AI regulation proposals I've been seeing in the US, and this bill in particular came to my attention today after seeing this article . The bill (which has just been &quot;unanimously advanced to the Senate floor&quot;), similar to other age verification policies, use
---

[RSS:Reddit LocalLLaMA (社区共识)]
Prompt injection benchmark: delimiter + strict prompt took Gemma 4 from 21% to 100% defense rate (15 models, 6100+ tests)
https://www.reddit.com/r/LocalLLaMA/comments/1t47z4q/prompt_injection_benchmark_delimiter_strict/
When dealing with untrusted outside input, I think you should handle it based on the situation. If you're processing structured data files, it's better to use tools to isolate and handle them. I made DataGate for that. But if it's web documents that the model has to read and understand directly (whi
---

[RSS:Reddit LocalLLaMA (社区共识)]
it's time to update your Gemma 4 GGUFs
https://www.reddit.com/r/LocalLLaMA/comments/1t3dfvp/its_time_to_update_your_gemma_4_ggufs/
Chat Template was fixed a few days ago choose your fav dealer: https://huggingface.co/bartowski/google_gemma-4-31B-it-GGUF https://huggingface.co/bartowski/google_gemma-4-26B-A4B-it-GGUF https://huggingface.co/bartowski/google_gemma-4-E4B-it-GGUF https://huggingface.co/bartowski/google_gemma-4-E2B-i
---

[RSS:Reddit LocalLLaMA (社区共识)]
APEX MoE quants update: 25+ new models since the Qwen 3.5 post + new I-Nano tier
https://www.reddit.com/r/LocalLLaMA/comments/1t3n6jo/apex_moe_quants_update_25_new_models_since_the/
Quick follow-up on APEX, the MoE-aware mixed-precision quant strategy. The original post was just about Qwen 3.5 35B-A3B ( https://www.reddit.com/r/LocalLLaMA/comments/1s9vzry/apex_moe_quantized_models_boost_with_33_faster/ ); since then the collection has grown to 30+ MoEs across most major familie
---

[RSS:Reddit LocalLLaMA (社区共识)]
Trying to train tiny LLMs on length constrained reddit posts summarization task using GRPO on 3xMac Minis - updates!
https://www.reddit.com/r/LocalLLaMA/comments/1t494ja/trying_to_train_tiny_llms_on_length_constrained/
So, here's an update to my GRPO training on length constrained reddit posts summarization on 3x Mac minis - a new direction! Gist- been trying to test how good of a summarization model can be trained for summarization using exactly 64 tokens! So, once all the t-test and evals were done for LFM2.5.-3
---

[RSS:Reddit LocalLLaMA (社区共识)]
About Kimi K2.6
https://www.reddit.com/r/LocalLLaMA/comments/1t3ue53/about_kimi_k26/
Recently, I’ve seen lots of ads for the Kimi K2.6 across various social media platforms, and I’d like to hear from people who have used it. Is it genuinely that good, or is it just a model with impressive benchmark scores that doesn't perform well in real use? &#32; submitted by &#32; /u/Exact_Law_6
---

[RSS:Reddit LocalLLaMA (社区共识)]
qwen 3.6 27B looping problem
https://www.reddit.com/r/LocalLLaMA/comments/1t45m77/qwen_36_27b_looping_problem/
Whenever I write here that I use gemma 31B I get answers that qwen 27B is better. I switched in the pi from gemma 31B Q5 to qwen 27B Q8 and generally I manage to code, document and run tests but somewhere after exceeding 100k context qwen keeps getting into loops. Do you have any solution for this? 
---

[RSS:Reddit LocalLLaMA (社区共识)]
The more I use it, the more I'm impressed
https://www.reddit.com/r/LocalLLaMA/comments/1t3i219/the_more_i_use_it_the_more_im_impressed/
Qwen 3.6 27b vs Codex GPT 5.5 / Claude Opus 4.7 My local llm discovered a bug that they both missed And it turns out it's critical GPT 5.5 and Claude both stood their ground and didn't give up until the end - they claimed to be right all along. I told my Qwen to provide detailed proof of his argumen
---

[RSS:Reddit LocalLLaMA (社区共识)]
Struggling with Qwen3.6 27B / 35B locally (3090) slow responses, breaking code looking for better setup + auto model switching
https://www.reddit.com/r/LocalLLaMA/comments/1t49pqu/struggling_with_qwen36_27b_35b_locally_3090_slow/
Hey everyone, I’ve been experimenting with running Qwen models locally on my setup: GPU: RTX 3090 (24GB VRAM) RAM: 64GB CPU: Ryzen 5700X OS: Windows 11 What I’m currently running Qwen 3.6 35B (UD Q4_K_M) llama-server.exe -m &quot;C:\Users\Dino\.lmstudio\models\unsloth\Qwen3.6-35B-A3B-GGUF\Qwen3.6-35
---

[RSS:Reddit LocalLLaMA (社区共识)]
Ryzen AI Max+ 495 (Gorgon Halo) with 192GB VRAM!
https://www.reddit.com/r/LocalLLaMA/comments/1t3duwm/ryzen_ai_max_495_gorgon_halo_with_192gb_vram/
https://www.srware.net/en/news/1094/AMD-Ryzen-AI-Max+-PRO-495-leak-points-to-a-bigger-Halo-APU-with-192-GB-memory This is fantastic news! Unfortunately, the device will of course be very expensive due to the storage crisis. But that means Medusa Halo should easily have 256 GB (in 2027) - or what do 
---

[RSS:Reddit LocalLLaMA (社区共识)]
Why is no open weight model inference provider hosting Mimo-v2.5 or Mimo-v2.5-pro?
https://www.reddit.com/r/LocalLLaMA/comments/1t3u8jg/why_is_no_open_weight_model_inference_provider/
Literally no 3rd party api inference provider is hosting the mimo-2.5 series models from Xiaomi. They seem to be reallly good. High token efficiency and very low halucination rate compared to Kimi-k2.6, Deepseek-V4 or GLM-5.1, and yet no provider not even chutes is hosting it other than Xiaomi thems
---

[RSS:Reddit LocalLLaMA (社区共识)]
I made a voice controlled Tic-Tac-Toe game as a learning project
https://www.reddit.com/r/LocalLLaMA/comments/1t46pwq/i_made_a_voice_controlled_tictactoe_game_as_a/
Hi, First of all, I know this might be a silly project, but I made it specifically as an educational project for me in order to learn about finetuning SLMs and utilizing a full pipeline of ASR (Transcription) -&gt; SLM (Intent Parsing) -&gt; Executing Actions -&gt; TTS (Synthesizing results). I gene
---

[RSS:Reddit MachineLearning (学术风向)]
Is there a notable increase in demand for privacy-preserving AI/ML with the advent of LLMs? [D]
https://www.reddit.com/r/MachineLearning/comments/1t3u2jh/is_there_a_notable_increase_in_demand_for/
While browsing through this subreddit, I encountered this old discussion post about demand for AI with the rise of privacy regulation. It got me thinking that, 6 years on, the demand for AI hasn't slowed at all, obviously. But with the rise of LLMs and papers showing how to de-anonymize online users
---

[RSS:Reddit MachineLearning (学术风向)]
Building a 9-ball AI player: Candidate generation for direct cut shots [P]
https://www.reddit.com/r/MachineLearning/comments/1t3xplr/building_a_9ball_ai_player_candidate_generation/
I'm building a 9-ball-player to help with pattern play. There are many ways to make the next ball, and sometimes in more than one obvious pocket. Which should should you choose depends on probability of making that shot AND ending up in a favorable spot for the next shot, that is also amenable to ge
---

[RSS:Reddit MachineLearning (学术风向)]
Why SSMs struggle in parameter-constrained training: empirical findings at 25M parameters [R]
https://www.reddit.com/r/MachineLearning/comments/1t3hxsy/why_ssms_struggle_in_parameterconstrained/
After ~3 weeks of experimentation in OpenAI's Parameter Golf competition, I wrote up why SSMs are structurally disadvantaged relative to transformers in a time- and size-constrained regime (10 min training, 16MB artifact, 25M parameters) on 8xH100s: https://mradassaad.github.io/posts/why-ssms-strugg
---

[RSS:Reddit MachineLearning (学术风向)]
How do you experiment with a (very) large model architecture? [D]
https://www.reddit.com/r/MachineLearning/comments/1t3savv/how_do_you_experiment_with_a_very_large_model/
Im trying to reproduce a paper (a very particular kind of diffusion model), and their training regime is incredibly compute heavy. In general, how are quick experiments performed to validate hypotheses when the models are large and compute is expensive? Some cursory browsing yields the following: 1)
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

[RSS:Reddit MachineLearning (学术风向)]
[D] What Happened to Neurips Creative AI Track? [R]
https://www.reddit.com/r/MachineLearning/comments/1t3hfcs/d_what_happened_to_neurips_creative_ai_track_r/
At Neurips 2025, the Creative AI Track was announced as part of the official proceedings: https://neurips.cc/Conferences/2025/CallForCreativeAI &quot;Please note that this year the Creative AI track will be part of the NeurIPS conference proceedings and papers will be presented as posters during the
---

[RSS:Reddit MachineLearning (学术风向)]
[P] QLoRA Fine-Tuning of Qwen2.5-1.5B for CEFR English Proficiency Classification (A1–C2) [P]
https://www.reddit.com/r/MachineLearning/comments/1t3ogbw/p_qlora_finetuning_of_qwen2515b_for_cefr_english/
I fine-tuned Qwen2.5-1.5B for multi-class CEFR English proficiency classification using QLoRA (4-bit NF4). The goal was to classify English text into one of the 6 CEFR levels (A1 → C2), which can be useful for: adaptive language learning systems, placement testing, readability estimation, educationa
---

[RSS:Reddit MachineLearning (学术风向)]
Neurips, how can i submit the "link" to the code? [D]
https://www.reddit.com/r/MachineLearning/comments/1t3zovv/neurips_how_can_i_submit_the_link_to_the_code_d/
It seems that the supplementary section doesn't accept text. Can I just submit the PDF file that has link to it? &#32; submitted by &#32; /u/BetterbeBattery [link] &#32; [comments]
---

[RSS:Reddit MachineLearning (学术风向)]
Parax v0.5: Parametric Modeling in JAX [P]
https://www.reddit.com/r/MachineLearning/comments/1t3jmdc/parax_v05_parametric_modeling_in_jax_p/
Hi everyone! Just sharing an update on my project Parax , which caters for &quot;parametric modeling&quot; in JAX. Previously, Parax was more focused on scientific applications, however I've since generalized it to be a tool useful for any type of JAX work. It now has a strong focus on a clean, exta
---

[RSS:Reddit MachineLearning (学术风向)]
Confusion about the NeurIPS 2026 page limit [R]
https://www.reddit.com/r/MachineLearning/comments/1t3y3nu/confusion_about_the_neurips_2026_page_limit_r/
Hello, I’m preparing a submission for NeurIPS, and I’m a bit confused about the page limit policy stated on the website. &quot;Papers are limited to eight pages, including figures and tables, in the NeurIPS style. However, an additional ninth page containing only cited references is allowed. Papers 
---

[RSS:Reddit MachineLearning (学术风向)]
AutoBe benchmark: structured harness narrows frontier-vs-local gap in backend generation [D]
https://www.reddit.com/r/MachineLearning/comments/1t3hks9/autobe_benchmark_structured_harness_narrows/
AutoBe is a benchmark for end-to-end backend generation. One natural language request produces six outputs: requirements analysis, ERD, OpenAPI spec, E2E tests, NestJS implementation, and a type-safe SDK. Each phase fills a predefined AST via structured function calling rather than generating unstru
---

[RSS:Ars Technica AI (深度技术)]
GameStop offers $56 billion for eBay, struggles to explain how it'll pay for it
https://arstechnica.com/tech-policy/2026/05/gamestop-offers-56-billion-for-ebay-struggles-to-explain-how-itll-pay-for-it/
Amid falling revenue and store closures, GameStop wants to buy the much larger eBay.
---

[RSS:Reddit Jobs & Careers (职场动态)]
Resume Advice Thread - May 05, 2026
https://www.reddit.com/r/cscareerquestions/comments/1t47vi7/resume_advice_thread_may_05_2026/
Please use this thread to ask for resume advice and critiques. You should read our Resume FAQ and implement any changes from that before you ask for more advice. Abide by the rules, don't be a jerk. Note on anonomyizing your resume: If you'd like your resume to remain anonymous, make sure you blank 
---

[RSS:Reddit Jobs & Careers (职场动态)]
My company stopped doing LC for SWE roles and is now testing candidates on what they can build on the spot with AI, and how they use it
https://www.reddit.com/r/cscareerquestions/comments/1t3rvsg/my_company_stopped_doing_lc_for_swe_roles_and_is/
I work for a very well known tech company and we stopped doing LC interview rounds. I sat in an interview and our candidates are now tested on what they can build using AI tools for the technical round. There is no real right or wrong answer, you essentially show what you can design, build, and then
---

[RSS:Reddit Jobs & Careers (职场动态)]
Do layoffs target less experienced SWEs first?
https://www.reddit.com/r/cscareerquestions/comments/1t44j82/do_layoffs_target_less_experienced_swes_first/
Currently E3 at Meta. Wondering if this level would be disproportionately affected by the upcoming layoff. I know levels are in consideration but I’m wondering what has been true in the past. Tech companies laid off a lot 2022-present. During these layoffs, are entry level engineers affected the mos
---

[RSS:Reddit Jobs & Careers (职场动态)]
Do I give up? 6 YOE/2 degrees. I'm totally lost.
https://www.reddit.com/r/cscareerquestions/comments/1t40kad/do_i_give_up_6_yoe2_degrees_im_totally_lost/
1.) 2 BSc degrees Computer science being my 2nd, I stopped putting the first BSc on there even though I believe the published research in pharmacology and human anatomy division work I did is very relevant to anything biosci related. But I'm also not sure how much these companies would/wouldn't scru
---

[RSS:Reddit Jobs & Careers (职场动态)]
Why do people have such radically different views on how AI will affect the industry?
https://www.reddit.com/r/cscareerquestions/comments/1t3vmgs/why_do_people_have_such_radically_different_views/
TL;DR: The reason people have such wildly different views on how much work AI will replace or eliminate is because different industries/companies have fundamentally different exposure levels to said automation. So think about that before arguing with someone about how far AI will go in automating ev
---

[RSS:Reddit Jobs & Careers (职场动态)]
Opinion from a retired engineer: Coding is more technician work and SWE is here to stay.
https://www.reddit.com/r/cscareerquestions/comments/1t3nwf4/opinion_from_a_retired_engineer_coding_is_more/
In the field of software engineering, there hasn’t traditionally been a clear “technician” role like in other engineering disciplines. In those fields, technicians focus on implementation, installation, and troubleshooting, handling detailed tasks while following established procedures and specifica
---

[RSS:Reddit Jobs & Careers (职场动态)]
Which is harder: first internship (no experience) or first job
https://www.reddit.com/r/cscareerquestions/comments/1t4489f/which_is_harder_first_internship_no_experience_or/
I know mileage will vary but I'd like to learn your takes on this. For the current market, in general, do you think it would be harder for someone with no experience but good projects + college to get their first internship OR someone with 2 internships at that same college to get their first job as
---

[RSS:Reddit Jobs & Careers (职场动态)]
Is anyone getting hired off cold LinkedIn applications this year?
https://www.reddit.com/r/cscareerquestions/comments/1t3hvz1/is_anyone_getting_hired_off_cold_linkedin/
I’ve been hitting it hard since the start of the year, but I’m starting to lose trust that any of these jobs are real. Mostly want to know if I’m wasting my time or should keep at it. For context, I have 5-6 years real work experience. I think I’m a solid mid dev level. Comfortable full stack and us
---

[RSS:Reddit Jobs & Careers (职场动态)]
2 years in dev, but I think I don’t enjoy programming anymore. Skill issue or time to pivot?
https://www.reddit.com/r/cscareerquestions/comments/1t46dsy/2_years_in_dev_but_i_think_i_dont_enjoy/
Hi, I’m 24 and I’ve been working as a freelance/outsourced developer for almost 2 years with a UK-based client. I’m starting to question if I’m actually into programming or if I just forced myself into it. I was initially hired for backend work, including Go, even though I had almost no experience w
---

[RSS:Reddit Jobs & Careers (职场动态)]
Hacker News alternative
https://www.reddit.com/r/cscareerquestions/comments/1t46jlh/hacker_news_alternative/
I like reading interesting articles, commentary, etc broadly around contemporary tech. I do not like reading reams of mealy-mouthed pontification on AI with so much hedging they put the gardens of Versailles to shame, from a community of people too many of whom would have fallen for an opium panacea
---

[RSS:Reddit Jobs & Careers (职场动态)]
First time contract job as C2C - what do I need?
https://www.reddit.com/r/cscareerquestions/comments/1t469ad/first_time_contract_job_as_c2c_what_do_i_need/
I got offered a contract job with a state government. They have contractors onboard through approved vendors. The state will pay the vendor $85/hour, the vendor would take a cut and pay me. I had to get quotes from a bunch of approved vendors, one of them gives the choice of $80/hour as C2C or $65 a
---

[RSS:Reddit Jobs & Careers (职场动态)]
Is it normal for a company to do this after they already invited you for an on-site?
https://www.reddit.com/r/cscareerquestions/comments/1t3vegs/is_it_normal_for_a_company_to_do_this_after_they/
I'm kinda confused right now. A couple of days ago, I was invited for a final on-site interview by a company, but today they sent me an email saying &quot;Before the on-site, we would lile you to meet our Head of Software online&quot;. During the initial screening they told me the whole process woul
---

[RSS:Reddit Jobs & Careers (职场动态)]
Is the "10x developer" myth actually hurting junior devs?
https://www.reddit.com/r/cscareerquestions/comments/1t3ezdd/is_the_10x_developer_myth_actually_hurting_junior/
Companies keep chasing unicorns instead of building good teams. Anyone else notice this? &#32; submitted by &#32; /u/1vim [link] &#32; [comments]
---

[RSS:Reddit Jobs & Careers (职场动态)]
Do hiring managers actually read your GitHub or just check if it exists?
https://www.reddit.com/r/cscareerquestions/comments/1t3f1fy/do_hiring_managers_actually_read_your_github_or/
Spent 3 months polishing repos. Wondering if anyone actually looks. &#32; submitted by &#32; /u/1vim [link] &#32; [comments]
---

[RSS:Reddit Jobs & Careers (职场动态)]
Made it to the final round for 2 startups - looking for some advice on them
https://www.reddit.com/r/cscareerquestions/comments/1t46xta/made_it_to_the_final_round_for_2_startups_looking/
Looking for some advice on final round interviews for 2 companies I have upcoming. These are both healthcare startups for a React Native role. For one company, they're having me do a 1 hour &quot;Teach Me&quot; presentation on site. https://pastebin.com/Z6V93RnF Anyone have any suggestions on what s
---

[RSS:Reddit Jobs & Careers (职场动态)]
I’m so bad at this field,
https://www.reddit.com/r/cscareerquestions/comments/1t46mo5/im_so_bad_at_this_field/
It doesn’t help that everyone around me (friends, family, classmates) seems to be alright with it. The programming makes sense some of, probably most of, the time (like OOP, hardware and software, even things like systems programming) it’s like I’m the only person who struggles with it. It genuinely
---

[RSS:Reddit Jobs & Careers (职场动态)]
SWE NYC vs Seattle
https://www.reddit.com/r/cscareerquestions/comments/1t46qbh/swe_nyc_vs_seattle/
24 years old 1.5 YOE. I work remotely from nyc on a team closely related to the ai mission of my company but on a particular product and not dealing with actual ai infra. I have an opportunity to go to Seattle and work on actual ai infra (same company) used by this product and others in an ai eng ca
---

[RSS:Reddit Jobs & Careers (职场动态)]
Would pivoting from "Java Spring Boot Developer" to "Cloud-Native Java Engineer" improve my chances of landing a job?
https://www.reddit.com/r/cscareerquestions/comments/1t3k1th/would_pivoting_from_java_spring_boot_developer_to/
So it seems like it's almost impossible to land a job as a backend developer (specialized in Java Spring Boot like myself) - there's literally 100s of applications for each opening. I talked to AI about this and it recommended I learn some cloud skills such as AWS, Kubernetes, and Terraform and rebr
---

[RSS:Reddit Jobs & Careers (职场动态)]
what if i do dummy job for work experience ?
https://www.reddit.com/r/cscareerquestions/comments/1t46ajh/what_if_i_do_dummy_job_for_work_experience/
if soemone (mechanical, state gov college) got himself a dummy job in a friend’s immigration agency for ~2 years. loction: India On paper Salary: ~45k/month($2000 ppp adjusted) No EPFO He sends the money to his friend, and it’s routed back as salary but in reality wont be working there full time, wi
---

[RSS:Reddit Jobs & Careers (职场动态)]
How important is LinkedIn
https://www.reddit.com/r/cscareerquestions/comments/1t45uni/how_important_is_linkedin/
I have about 2.5 YoE, my job is decent enough but layoff threat is real we are about to have a major merger so I’ve been applying pretty much to anything still in the “decent” tier Zero responses yet but I have noticed maybe about 10 LinkedIn profile views from people at companies I’ve applied to, s
---

[RSS:Reddit Jobs & Careers (职场动态)]
Should I choose system integration test role at ODM vs operations role at hyperscaler?
https://www.reddit.com/r/cscareerquestions/comments/1t3yju1/should_i_choose_system_integration_test_role_at/
Looking for outside perspective on a career decision I'm stuck on Background: Mid-career, ~4 years experience Software-leaning skill set: Python, Bash, automation, infrastructure scripting Past role was at a server ODM doing test infrastructure for a major hyperscaler customer — automation, RTP vali
---

[RSS:Reddit Jobs & Careers (职场动态)]
Are there some platforms where I can teach people coding for free?
https://www.reddit.com/r/cscareerquestions/comments/1t3k0io/are_there_some_platforms_where_i_can_teach_people/
I'd like to teach people coding (16 years of experience here). I don't need to take them to private channels, but I'm free in the evenings and I can teach people or go over their work and give feedback. Are there platforms like that? &#32; submitted by &#32; /u/HyperDanon [link] &#32; [comments]
---

[RSS:Reddit Jobs & Careers (职场动态)]
L4 iOS at Google
https://www.reddit.com/r/cscareerquestions/comments/1t3hmuh/l4_ios_at_google/
Hi everyone, I have a mid-level iOS domain specific interview coming up at Google. Does anyone know what I can expect? Any experience or advice is appreciated!! &#32; submitted by &#32; /u/King-Code-Monkey [link] &#32; [comments]
---

[HACKERNEWS]
Async Rust never left the MVP state
https://tweedegolf.nl/en/blog/237/async-rust-never-left-the-mvp-state
Score: 113 | Comments: 57
---

[HACKERNEWS]
Hand Drawn QR Codes
https://sethmlarson.dev/hand-drawn-qr-codes
Score: 94 | Comments: 10
---

[HACKERNEWS]
CVE-2026-31431: Copy Fail vs. rootless containers
https://www.dragonsreach.it/2026/05/04/cve-2026-31431-copy-fail-rootless-containers/
Score: 100 | Comments: 34
---

[HACKERNEWS]
How OpenAI delivers low-latency voice AI at scale
https://openai.com/index/delivering-low-latency-voice-ai-at-scale/
Score: 405 | Comments: 123
---

[HACKERNEWS]
Bun is being ported from Zig to Rust
https://github.com/oven-sh/bun/commit/46d3bc29f270fa881dd5730ef1549e88407701a5
Score: 495 | Comments: 351
---

[HACKERNEWS]
Google Chrome silently installs a 4 GB AI model on your device without consent
https://www.thatprivacyguy.com/blog/chrome-silent-nano-install/
Score: 173 | Comments: 183
---

[HACKERNEWS]
Train Your Own LLM from Scratch
https://github.com/angelos-p/llm-from-scratch
Score: 235 | Comments: 28
---

[HACKERNEWS]
Agent Skills
https://addyosmani.com/blog/agent-skills/
Score: 252 | Comments: 112
---

[HACKERNEWS]
Empty Screenings – Finds AMC movie screenings with few or no tickets sold
https://walzr.com/empty-screenings
Score: 143 | Comments: 116
---

[HACKERNEWS]
The Frog for Whom the Bell Tolls
https://sethmlarson.dev/the-frog-for-whom-the-bell-tolls
Score: 8 | Comments: 1
---

[HACKERNEWS]
Gap between national food production and food-based dietary guidance (2025)
https://www.nature.com/articles/s43016-025-01173-4
Score: 59 | Comments: 38
---

[HACKERNEWS]
Securing a DoD contractor: Finding a multi-tenant authorization vulnerability
https://www.strix.ai/blog/how-strix-found-zero-auth-vulnerability-dod-backed-startup
Score: 197 | Comments: 81
---

[HACKERNEWS]
Does Employment Slow Cognitive Decline? Evidence from Labor Market Shocks
https://www.nber.org/papers/w35117
Score: 286 | Comments: 267
---

[HACKERNEWS]
2-D Mathematical Curves
https://www.2dcurves.com/
Score: 30 | Comments: 1
---

[HACKERNEWS]
When Networking Doesn't Work
https://www.os2museum.com/wp/when-networking-doesnt-work/
Score: 63 | Comments: 11
---

[HACKERNEWS]
Redis array: short story of a long development process
https://antirez.com/news/164
Score: 282 | Comments: 97
---

[GITHUB]
vllm-project/vllm released v0.20.1
https://github.com/vllm-project/vllm/releases/tag/v0.20.1
Author: khluu
# vLLM v0.20.1 This is a patch release on top of `v0.20.0` primarily focused on **DeepSeek V4 stabilization and performance improvements**, along with several important bug fixes. ### DeepSeek V4 * Base model support (#41006). * Multi-stream pre-attention GEMM (#41061), configurable pre-attn GEMM kn
---

[ACADEMIC - ARXIV]
标题: Reinforcement Learning for LLM-based Multi-Agent Systems through Orchestration Traces
作者: Chenchen Zhang
链接: https://arxiv.org/abs/2605.02801v1
完整摘要: As large language model (LLM) agents evolve from isolated tool users into coordinated teams, reinforcement learning (RL) must optimize not only individual actions but also how work is spawned, delegated, communicated, aggregated, and stopped. This paper studies RL for LLM-based multi-agent systems through orchestration traces: temporal interaction graphs whose events include sub-agent spawning, delegation, communication, tool use, return, aggregation, and stopping decisions. Using this lens, we identify three technical axes. First, reward design spans eight families, including orchestration rewards for parallelism speedup, split correctness, and aggregation quality. Second, reward and credit signals attach to eight credit- or signal-bearing units from token to team; explicit counterfactual message-level credit remains especially sparse in our curated pool. Third, orchestration learning decomposes into five sub-decisions: when to spawn, whom to delegate to, how to communicate, how to aggregate, and when to stop. In our curated pool as of May 4, 2026, we found no explicit RL training method for the stopping decision. We connect academic methods to public industrial evidence from Kimi Agent Swarm, OpenAI Codex, and Anthropic Claude Code. The resulting scale gap is a gap between publicly reported deployment envelopes and open academic evaluation regimes, not independent verification of industrial training traces. We release the artifact at https://github.com/xxzcc/awesome-llm-mas-rl, including an 84-entry tagged paper pool, a 32-record exclusion log, scripted corpus statistics, and a minimal JSON schema for replayable orchestration traces.
匹配关键词: multi-agent
---

[ACADEMIC - ARXIV]
标题: Mitigating Misalignment Contagion by Steering with Implicit Traits
作者: Maria Chang, Ronny Luss, Miao Lui, Keerthiram Murugesan, Karthikeyan Ramamurthy, Djallel Bouneffouf
链接: https://arxiv.org/abs/2605.02751v1
完整摘要: Language models (LMs) are increasingly used in high-stakes, multi-agent settings, where following instructions and maintaining value alignment are critical. Most alignment research focuses on interactions between a single LM and a single user, failing to address the risk of misaligned behavior spreading between multiple LMs in multi-turn interactions. We find evidence of this phenomenon, which we call misalignment contagion, across multiple LMs as they engage multi-turn conversational social dilemma games. Specifically, we find that LMs become more anti-social after gameplay and that this effect is intensified when other players are steered to act maliciously. We explore different steering techniques to mitigate such misalignment contagion and find that reinforcing an LM's system prompt is insufficient and often harmful. Instead, we propose steering with implicit traits: a technique that intermittently injects system prompts with statements that reinforce an LMs initial traits and is more effective than system prompt repetition at keeping models in line with their initial pro-social behaviors. Importantly, this method does not require access to model parameters or internal model states, making it suitable for increasingly common use cases where complex multi-agent workflows are being designed with black box models.
匹配关键词: multi-agent
---

[ACADEMIC - ARXIV]
标题: AI-Generated Smells: An Analysis of Code and Architecture in LLM and Agent-Driven Development
作者: Yuecai Zhu, Nikolaos Tsantalis, Peter C. Rigby
链接: https://arxiv.org/abs/2605.02741v1
完整摘要: The promise of Large Language Models in automated software engineering is often measured by functional correctness, overlooking the critical issue of long term maintainability. This paper presents a systematic audit of technical debt in AI-generated software, revealing that AI does not eliminate flaws but rather introduces a distinct machine signature of defects. Our multi-scale analysis, spanning single-file algorithmic tasks and complex, agent generated systems, identifies a fundamental Reasoning-Complexity Trade-off: as models become more capable, they generate increasingly bloated and coupled code. This architectural decay is so pronounced that we establish a Volume-Quality Inverse Law, where code volume is a near perfect predictor of structural degradation. Crucially, we demonstrate that neither functional correctness nor detailed prompting mitigates this decay. These findings challenge the current paradigm of prompt-driven generation, reframing the central problem of AI-based software engineering from one of code generation to one of architectural complexity management. We conclude that future progress depends on equipping agents with explicit architectural foresight to ensure the software they build is not just functional, but also maintainable.
匹配关键词: multi-agent
---

[ACADEMIC - ARXIV]
标题: Hybrid Inspection and Task-Based Access Control in Zero-Trust Agentic AI
作者: Majed El Helou, Benjamin Ryder, Chiara Troiani, Jean Diaconu, Hervé Muyal, Marcelo Yannuzzi
链接: https://arxiv.org/abs/2605.02682v1
完整摘要: Authorizing Large Language Model (LLM)-driven agents to dynamically invoke tools and access protected resources introduces significant security risks, and the risks grow dramatically as agents engage in multi-turn conversations and scale toward distributed collaboration. A compromised or malicious agentic application can tamper with tool calls, falsify results, or request permissions beyond the scope of the subject's intended tasks, which could go unnoticed with current delegated authorization flows given their lack of visibility into the original subject's intent. In light of this, we make the following contributions towards Continuous Agent Semantic Authorization (CASA). First, we propose a hybrid runtime enforcement model that combines deterministic and semantic controls enabled by a zero-trust interception layer. Five deterministic controls enforce structural and data-integrity guarantees over the message flow, while a semantic inspection layer evaluates whether tool call choices align with the intended tasks commissioned to the agent. Second, differently from prior Task-Based Access Control (TBAC) techniques that operate on single-turn interactions, we decompose the semantic layer into two stages: i) a task-extraction step that distills the subject's objectives from multi-turn conversations at the interception layer, and ii) a task-tool semantic matching step at the authorization server that evaluates whether the requested tools are appropriate for the extracted tasks. Third, we extend the ASTRA dataset that we introduced in a prior work, by generating novel conversation-tool datasets with multi-turn interactions containing relevant and irrelevant tool calls for a given task. Lastly, we provide the first experimental results for TBAC under multi-turn conversations.
匹配关键词: multi-agent
---

[ACADEMIC - ARXIV]
标题: AcademiClaw: When Students Set Challenges for AI Agents
作者: Junjie Yu, Pengrui Lu, Weiye Si, Hongliang Lu, Jiabao Wu, Kaiwen Tao, Kun Wang, Lingyu Yang, Qiran Zhang, Xiuting Guo, Xuanyu Wang, Yang Wang, Yanjie Wang, Yi Yang, Zijian Hu, Ziyi Yang, Zonghan Zhou, Binghao Qiang, Borui Zhang, Chenning Li, Enchang Zhang, Feifan Chen, Feng Jian, Fengyin Sun, Hao Qiu, Hao Zheng, Haoran Zhu, Hongyu Liu, Jianbin Deng, Jiaxin Song, Jiaying Chi, Jiayou Shi, Jie Fang, Jinghui Zhong, Jingyu Zhou, Jinze Li, Junfeng Yi, Junyan Yu, Junzhi Xue, Ni Song, Pengyi Chen, Qi Chen, Quansheng Li, Rui Tao, Shenghai Gong, Shenhang Lu, Tianqi Shen, Tianxiang Zhu, Tiehan Kang, Tingyu Li, Wendi Wu, Xiao Shen, Xiao Zhou, Xiaotao Zhang, Xinrong Li, Xuankun Yang, Xun Zhang, Yan Li, Ye Lu, Yi Wang, Yibo Zhou, Yichi Zhang, Yihao Sun, Yijun Huang, Yixin Zhu, Yixuan Wu, Yuchen Sun, Yue Wu, Yuheng Sun, Yukun Li, Yutian Tu, Yuxuan Qin, Yuzhuo Wu, Zeyu Li, Zhengyu Lou, Zhenning Ran, Zizhu He, Pengfei Liu
链接: https://arxiv.org/abs/2605.02661v1
完整摘要: Benchmarks within the OpenClaw ecosystem have thus far evaluated exclusively assistant-level tasks, leaving the academic-level capabilities of OpenClaw largely unexamined. We introduce AcademiClaw, a bilingual benchmark of 80 complex, long-horizon tasks sourced directly from university students' real academic workflows -- homework, research projects, competitions, and personal projects -- that they found current AI agents unable to solve effectively. Curated from 230 student-submitted candidates through rigorous expert review, the final task set spans 25+ professional domains, ranging from olympiad-level mathematics and linguistics problems to GPU-intensive reinforcement learning and full-stack system debugging, with 16 tasks requiring CUDA GPU execution. Each task executes in an isolated Docker sandbox and is scored on task completion by multi-dimensional rubrics combining six complementary techniques, with an independent five-category safety audit providing additional behavioral analysis. Experiments on six frontier models show that even the best achieves only a 55\% pass rate. Further analysis uncovers sharp capability boundaries across task domains, divergent behavioral strategies among models, and a disconnect between token consumption and output quality, providing fine-grained diagnostic signals beyond what aggregate metrics reveal. We hope that AcademiClaw and its open-sourced data and code can serve as a useful resource for the OpenClaw community, driving progress toward agents that are more capable and versatile across the full breadth of real-world academic demands. All data and code are available at https://github.com/GAIR-NLP/AcademiClaw.
匹配关键词: multi-agent
---

[ACADEMIC - ARXIV]
标题: SpecKV: Adaptive Speculative Decoding with Compression-Aware Gamma Selection
作者: Shikhar Shukla
链接: https://arxiv.org/abs/2605.02888v1
完整摘要: Speculative decoding accelerates large language model (LLM) inference by using a small draft model to propose candidate tokens that a larger target model verifies. A critical hyperparameter in this process is the speculation length~$γ$, which determines how many tokens the draft model proposes per step. Nearly all existing systems use a fixed~$γ$ (typically~4), yet empirical evidence suggests that the optimal value varies across task types and, crucially, depends on the compression level applied to the target model. In this paper, we present \textbf{SpecKV}, a lightweight adaptive controller that selects~$γ$ per speculation step using signals extracted from the draft model itself. We profile speculative decoding across 4~task categories, 4~speculation lengths, and 3~compression levels (FP16, INT8, NF4), collecting 5,112 step-level records with per-step acceptance rates, draft entropy, and draft confidence. We demonstrate that the optimal~$γ$ shifts across compression regimes and that draft model confidence and entropy are strong predictors of acceptance rate (correlation~$\approx 0.56$). SpecKV uses a small MLP trained on these signals to maximize expected tokens per speculation step, achieving a 56.0\% improvement over the fixed-$γ$=4 baseline with only 0.34\,ms overhead per decision ($<$0.5\% of step time). The improvement is statistically significant ($p < 0.001$, paired bootstrap test). We release all profiling data, trained models, and notebooks as open-source artifacts.
匹配关键词: swarm intelligence
---

[ACADEMIC - ARXIV]
标题: Enhancing RL Generalizability in Robotics through SHAP Analysis of Algorithms and Hyperparameters
作者: Lingxiao Kong, Cong Yang, Oya Deniz Beyan, Zeyd Boukhers
链接: https://arxiv.org/abs/2605.02867v1
完整摘要: Despite significant advances in Reinforcement Learning (RL), model performance remains highly sensitive to algorithm and hyperparameter configurations, while generalization gaps across environments complicate real-world deployment. Although prior work has studied RL generalization, the relative contribution of specific configurations to the generalization gap has not been quantitatively decomposed and systematically leveraged for configuration selection. To address this limitation, we propose an explainable framework that evaluates RL performance across robotic environments using SHapley Additive exPlanations (SHAP) to quantify configuration impacts. We establish a theoretical foundation connecting Shapley values to generalizability, empirically analyze configuration impact patterns, and introduce SHAP-guided configuration selection to enhance generalization. Our results reveal distinct patterns across algorithms and hyperparameters, with consistent configuration impacts across diverse tasks and environments. By applying these insights to configuration selection, we achieve improved RL generalizability and provide actionable guidance for practitioners.
匹配关键词: swarm intelligence
---

[ACADEMIC - ARXIV]
标题: Standing on the Shoulders of Giants: Stabilized Knowledge Distillation for Cross--Language Code Clone Detection
作者: Mohamad Khajezade, Fatemeh H. Fard, Mohamed Sami Shehata
链接: https://arxiv.org/abs/2605.02860v1
完整摘要: Cross-language code clone detection (X-CCD) is challenging because semantically equivalent programs written in different languages often share little surface similarity. Although large language models (LLMs) have shown promise for semantic clone detection, their use as black-box systems raises concerns about cost, reproducibility, privacy, and unreliable output formatting. In particular, compact open-source models often struggle to follow reasoning-oriented prompts and to produce outputs that can be consistently mapped to binary clone labels. To address these limitations, we propose a knowledge distillation framework that transfers reasoning capabilities from DeepSeek-R1 into compact open-source student models for X-CCD. Using cross-language code pairs derived from Project CodeNet, we construct reasoning-oriented synthetic training data and fine-tune Phi3 and Qwen-Coder with LoRA adapters. We further introduce response stabilization methods, including forced conclusion prompting, a binary classification head, and a contrastive classification head, and evaluate model behavior using both predictive metrics and response rate. Experiments on Python--Java, Rust--Java, Rust--Python, and Rust--Ruby show that knowledge distillation consistently improves the reliability of compact models and often improves predictive performance, especially under distribution shift. In addition, classification-head variants substantially reduce inference time compared to generation-based inference. Overall, our results show that reasoning-oriented distillation combined with response stabilization makes compact open-source models more practical and reliable for X-CCD detection.
匹配关键词: swarm intelligence
---

[ACADEMIC - ARXIV]
标题: From Sensors to Insight: Rapid, Edge-to-Core Application Development for Sensor-Driven Applications
作者: Komal Thareja, Anirban Mandal, Ewa Deelman
链接: https://arxiv.org/abs/2605.02859v1
完整摘要: Scientists increasingly rely on sensor-based data, yet transforming raw streams into insights across the edge-to-cloud continuum remains difficult. Provisioning heterogeneous infrastructure and managing execution on emerging platforms like Data Processing Units typically requires cross-domain expertise, creating significant barriers to rapid prototyping. This paper introduces an experience-driven methodology for the rapid development of sensor-driven applications. By combining pattern-based workflow engineering with AI-assisted development-implemented via Pegasus on the FABRIC testbed - we utilize an existing Orcasound hydrophone workflow as a reusable template. We introduce a pattern-based engineering methodology to generate and refine workflows for air quality, earthquake, and soil moisture monitoring. Furthermore, we show how these abstract structures are extended to edge resources through modular configuration and placement. Our evaluation focuses on user productivity and practical lessons rather than peak performance. Through these case studies, we illustrate how AI-assisted, pattern-based development lowers the entry barrier for non-experts and enables iterative exploration of sensor-driven applications across distributed infrastructures.
匹配关键词: swarm intelligence
---

[ACADEMIC - ARXIV]
标题: (POSTER) From Sensors to Insight: Rapid, Edge-to-Core Application Development for Sensor-Driven Applications
作者: Komal Thareja, Anirban Mandal, Ewa Deelman
链接: https://arxiv.org/abs/2605.02844v1
完整摘要: Scientists increasingly rely on sensor-based data; however transforming raw streams into insights across the edge-to-cloud continuum remains difficult due to the breadth of expertise required to coordinate the necessary data and computation flow. This paper introduces a pattern-based, AI-assisted methodology for rapid development of sensor-driven applications. Using Pegasus workflows executing on the FABRIC testbed, we demonstrate a 5-step development loop that shifts workflow construction and deployment from code-first to intent-first design. Starting from an existing Orcasound hydrophone workflow as a reusable template, we generate and refine workflows for air quality, earthquake, and soil moisture monitoring applications. We further show how these workflows extend to edge resources-including BlueField-3 DPUs and Raspberry Pis-through configuration and placement rather than workflow redesign. Our evaluation, from the perspective of a novice Pegasus user, shows that AI-assisted pattern reuse compresses multi-stage workflow development to 1-1.5 days per workflow while preserving the rigor and portability of workflow-based execution.
匹配关键词: swarm intelligence
---

[ACADEMIC - ARXIV]
标题: HAAS: A Policy-Aware Framework for Adaptive Task Allocation Between Humans and Artificial Intelligence Systems
作者: Vicente Pelechanoa, Antoni Mestre, Manoli Albert, Miriam Gil
链接: https://arxiv.org/abs/2605.02832v1
完整摘要: Deciding how to distribute work between humans and AI systems is a central challenge in organisational design. Most approaches treat this as a binary choice, yet the operational reality is richer: humans and AI routinely share tasks or take complementary roles depending on context, fatigue, and the stakes involved. Governing that distribution -- balancing efficiency, oversight, and human capability -- remains an open problem. This paper presents Human-AI Adaptive Symbiosis (HAAS), an implemented framework for adaptive task allocation in software engineering and manufacturing. HAAS combines two coupled components: a rule-based expert system that enforces governance constraints before any learning occurs, and a contextual-bandit learner that selects among feasible collaboration modes from outcome feedback. Task-agent fit is represented through five auditable cognitive dimensions and a five-mode autonomy spectrum -- from human-only to fully autonomous -- embedded in a reproducible benchmark spanning both domains. Three empirical findings emerge. First, governance is not a binary switch but a tunable design variable: tighter constraints predictably convert autonomous AI assignments into supervised collaborations, with domain-specific costs and benefits. Second, in manufacturing, stronger governance can improve operational performance and reduce fatigue simultaneously -- a workload-buffering effect that contradicts the usual framing of governance as pure overhead. Third, no single governance setting dominates across all contexts; moderate governance becomes increasingly competitive as the learner accumulates experience within the governed action space. Together, these findings position HAAS as a pre-deployment workbench for comparing and inspecting human--AI allocation policies before organisational commitment.
匹配关键词: game theory agent
---

[ACADEMIC - ARXIV]
标题: FlexSQL: Flexible Exploration and Execution Make Better Text-to-SQL Agents
作者: Quang Hieu Pham, Yang He, Ping Nie, Canwen Xu, Davood Rafiei, Yuepeng Wang, Xi Ye, Jocelyn Qiaochu Chen
链接: https://arxiv.org/abs/2605.02815v1
完整摘要: Text-to-SQL over large analytical databases requires navigating complex schemas, resolving ambiguous queries, and grounding decisions in actual data. Most current systems follow a fixed pipeline where schema elements are retrieved once upfront and the database is only revisited for post-hoc repair, limiting recovery from early mistakes. We present FlexSQL, a text-to-SQL agent whose core design principle is flexible database interaction: the agent can explore schema structure, inspect data values, and run verification queries at any point during reasoning. FlexSQL generates diverse execution plans to cover multiple query interpretations, implements each plan in either SQL or Python depending on the task, and uses a two-tiered repair mechanism that can backtrack from code-level errors to plan-level revisions. On Spider2-Snow, using gpt-oss-120b, FlexSQL achieves a 65.4\% score, outperforming strong open-source baselines that use stronger, larger models such as gpt-o3 and DeepSeek-R1. When integrated into a general-purpose coding agent (as skills in Claude Code), our approach yields over 10\% relative improvement on Spider2-Snow. Further analysis shows that flexible exploration and flexible execution jointly contribute to the effectiveness of our approach, highlighting flexibility as a key design principle. Our code is available at: https://github.com/StringNLPLAB/FlexSQL
匹配关键词: game theory agent
---

[ACADEMIC - ARXIV]
标题: Reinforcement Learning for LLM-based Multi-Agent Systems through Orchestration Traces
作者: Chenchen Zhang
链接: https://arxiv.org/abs/2605.02801v1
完整摘要: As large language model (LLM) agents evolve from isolated tool users into coordinated teams, reinforcement learning (RL) must optimize not only individual actions but also how work is spawned, delegated, communicated, aggregated, and stopped. This paper studies RL for LLM-based multi-agent systems through orchestration traces: temporal interaction graphs whose events include sub-agent spawning, delegation, communication, tool use, return, aggregation, and stopping decisions. Using this lens, we identify three technical axes. First, reward design spans eight families, including orchestration rewards for parallelism speedup, split correctness, and aggregation quality. Second, reward and credit signals attach to eight credit- or signal-bearing units from token to team; explicit counterfactual message-level credit remains especially sparse in our curated pool. Third, orchestration learning decomposes into five sub-decisions: when to spawn, whom to delegate to, how to communicate, how to aggregate, and when to stop. In our curated pool as of May 4, 2026, we found no explicit RL training method for the stopping decision. We connect academic methods to public industrial evidence from Kimi Agent Swarm, OpenAI Codex, and Anthropic Claude Code. The resulting scale gap is a gap between publicly reported deployment envelopes and open academic evaluation regimes, not independent verification of industrial training traces. We release the artifact at https://github.com/xxzcc/awesome-llm-mas-rl, including an 84-entry tagged paper pool, a 32-record exclusion log, scripted corpus statistics, and a minimal JSON schema for replayable orchestration traces.
匹配关键词: game theory agent
---

[ACADEMIC - ARXIV]
标题: DynoSLAM: Dynamic SLAM with Generative Graph Neural Networks for Real-World Social Navigation
作者: Danil Tokhchukov, Veronika Morozova, Gonzalo Ferrer
链接: https://arxiv.org/abs/2605.02759v1
完整摘要: Traditional Simultaneous Localization and Mapping (SLAM) algorithms rely heavily on the static environment assumption, which severely limits their applicability in real-world spaces populated by moving entities, such as pedestrians. In this work, we propose DynoSLAM, a tightly-coupled Dynamic GraphSLAM architecture that integrates socially-aware Graph Neural Networks (GNNs) directly into the factor graph optimization. Unlike conventional approaches that use rigid constant-velocity heuristics or deterministic single-agent neural priors, our framework formulates pedestrian motion forecasting as a stochastic World Model. By utilizing Monte Carlo rollouts from a trained GNN, we capture the multimodal epistemic uncertainty of human interactions and embed it into the SLAM graph via a dynamic Mahalanobis distance factor. We demonstrate through extensive simulated experiments that this stochastic formulation not only maintains highly accurate retrospective tracking but also prevents the optimization failures caused by the deterministic "argmax problem". Ultimately, extracting the empirical mean and covariance matrices of future pedestrian states provides a mathematically rigorous, probabilistic safety envelope for downstream local planners, enabling anticipatory and collision-free robot navigation in densely crowded environments.
匹配关键词: game theory agent
---

[ACADEMIC - ARXIV]
标题: Mitigating Misalignment Contagion by Steering with Implicit Traits
作者: Maria Chang, Ronny Luss, Miao Lui, Keerthiram Murugesan, Karthikeyan Ramamurthy, Djallel Bouneffouf
链接: https://arxiv.org/abs/2605.02751v1
完整摘要: Language models (LMs) are increasingly used in high-stakes, multi-agent settings, where following instructions and maintaining value alignment are critical. Most alignment research focuses on interactions between a single LM and a single user, failing to address the risk of misaligned behavior spreading between multiple LMs in multi-turn interactions. We find evidence of this phenomenon, which we call misalignment contagion, across multiple LMs as they engage multi-turn conversational social dilemma games. Specifically, we find that LMs become more anti-social after gameplay and that this effect is intensified when other players are steered to act maliciously. We explore different steering techniques to mitigate such misalignment contagion and find that reinforcing an LM's system prompt is insufficient and often harmful. Instead, we propose steering with implicit traits: a technique that intermittently injects system prompts with statements that reinforce an LMs initial traits and is more effective than system prompt repetition at keeping models in line with their initial pro-social behaviors. Importantly, this method does not require access to model parameters or internal model states, making it suitable for increasingly common use cases where complex multi-agent workflows are being designed with black box models.
匹配关键词: game theory agent
---

[ACADEMIC - ARXIV]
标题: HAAS: A Policy-Aware Framework for Adaptive Task Allocation Between Humans and Artificial Intelligence Systems
作者: Vicente Pelechanoa, Antoni Mestre, Manoli Albert, Miriam Gil
链接: https://arxiv.org/abs/2605.02832v1
完整摘要: Deciding how to distribute work between humans and AI systems is a central challenge in organisational design. Most approaches treat this as a binary choice, yet the operational reality is richer: humans and AI routinely share tasks or take complementary roles depending on context, fatigue, and the stakes involved. Governing that distribution -- balancing efficiency, oversight, and human capability -- remains an open problem. This paper presents Human-AI Adaptive Symbiosis (HAAS), an implemented framework for adaptive task allocation in software engineering and manufacturing. HAAS combines two coupled components: a rule-based expert system that enforces governance constraints before any learning occurs, and a contextual-bandit learner that selects among feasible collaboration modes from outcome feedback. Task-agent fit is represented through five auditable cognitive dimensions and a five-mode autonomy spectrum -- from human-only to fully autonomous -- embedded in a reproducible benchmark spanning both domains. Three empirical findings emerge. First, governance is not a binary switch but a tunable design variable: tighter constraints predictably convert autonomous AI assignments into supervised collaborations, with domain-specific costs and benefits. Second, in manufacturing, stronger governance can improve operational performance and reduce fatigue simultaneously -- a workload-buffering effect that contradicts the usual framing of governance as pure overhead. Third, no single governance setting dominates across all contexts; moderate governance becomes increasingly competitive as the learner accumulates experience within the governed action space. Together, these findings position HAAS as a pre-deployment workbench for comparing and inspecting human--AI allocation policies before organisational commitment.
匹配关键词: agent communication
---

[ACADEMIC - ARXIV]
标题: FlexSQL: Flexible Exploration and Execution Make Better Text-to-SQL Agents
作者: Quang Hieu Pham, Yang He, Ping Nie, Canwen Xu, Davood Rafiei, Yuepeng Wang, Xi Ye, Jocelyn Qiaochu Chen
链接: https://arxiv.org/abs/2605.02815v1
完整摘要: Text-to-SQL over large analytical databases requires navigating complex schemas, resolving ambiguous queries, and grounding decisions in actual data. Most current systems follow a fixed pipeline where schema elements are retrieved once upfront and the database is only revisited for post-hoc repair, limiting recovery from early mistakes. We present FlexSQL, a text-to-SQL agent whose core design principle is flexible database interaction: the agent can explore schema structure, inspect data values, and run verification queries at any point during reasoning. FlexSQL generates diverse execution plans to cover multiple query interpretations, implements each plan in either SQL or Python depending on the task, and uses a two-tiered repair mechanism that can backtrack from code-level errors to plan-level revisions. On Spider2-Snow, using gpt-oss-120b, FlexSQL achieves a 65.4\% score, outperforming strong open-source baselines that use stronger, larger models such as gpt-o3 and DeepSeek-R1. When integrated into a general-purpose coding agent (as skills in Claude Code), our approach yields over 10\% relative improvement on Spider2-Snow. Further analysis shows that flexible exploration and flexible execution jointly contribute to the effectiveness of our approach, highlighting flexibility as a key design principle. Our code is available at: https://github.com/StringNLPLAB/FlexSQL
匹配关键词: agent communication
---

[ACADEMIC - ARXIV]
标题: Reinforcement Learning for LLM-based Multi-Agent Systems through Orchestration Traces
作者: Chenchen Zhang
链接: https://arxiv.org/abs/2605.02801v1
完整摘要: As large language model (LLM) agents evolve from isolated tool users into coordinated teams, reinforcement learning (RL) must optimize not only individual actions but also how work is spawned, delegated, communicated, aggregated, and stopped. This paper studies RL for LLM-based multi-agent systems through orchestration traces: temporal interaction graphs whose events include sub-agent spawning, delegation, communication, tool use, return, aggregation, and stopping decisions. Using this lens, we identify three technical axes. First, reward design spans eight families, including orchestration rewards for parallelism speedup, split correctness, and aggregation quality. Second, reward and credit signals attach to eight credit- or signal-bearing units from token to team; explicit counterfactual message-level credit remains especially sparse in our curated pool. Third, orchestration learning decomposes into five sub-decisions: when to spawn, whom to delegate to, how to communicate, how to aggregate, and when to stop. In our curated pool as of May 4, 2026, we found no explicit RL training method for the stopping decision. We connect academic methods to public industrial evidence from Kimi Agent Swarm, OpenAI Codex, and Anthropic Claude Code. The resulting scale gap is a gap between publicly reported deployment envelopes and open academic evaluation regimes, not independent verification of industrial training traces. We release the artifact at https://github.com/xxzcc/awesome-llm-mas-rl, including an 84-entry tagged paper pool, a 32-record exclusion log, scripted corpus statistics, and a minimal JSON schema for replayable orchestration traces.
匹配关键词: agent communication
---

[ACADEMIC - ARXIV]
标题: DynoSLAM: Dynamic SLAM with Generative Graph Neural Networks for Real-World Social Navigation
作者: Danil Tokhchukov, Veronika Morozova, Gonzalo Ferrer
链接: https://arxiv.org/abs/2605.02759v1
完整摘要: Traditional Simultaneous Localization and Mapping (SLAM) algorithms rely heavily on the static environment assumption, which severely limits their applicability in real-world spaces populated by moving entities, such as pedestrians. In this work, we propose DynoSLAM, a tightly-coupled Dynamic GraphSLAM architecture that integrates socially-aware Graph Neural Networks (GNNs) directly into the factor graph optimization. Unlike conventional approaches that use rigid constant-velocity heuristics or deterministic single-agent neural priors, our framework formulates pedestrian motion forecasting as a stochastic World Model. By utilizing Monte Carlo rollouts from a trained GNN, we capture the multimodal epistemic uncertainty of human interactions and embed it into the SLAM graph via a dynamic Mahalanobis distance factor. We demonstrate through extensive simulated experiments that this stochastic formulation not only maintains highly accurate retrospective tracking but also prevents the optimization failures caused by the deterministic "argmax problem". Ultimately, extracting the empirical mean and covariance matrices of future pedestrian states provides a mathematically rigorous, probabilistic safety envelope for downstream local planners, enabling anticipatory and collision-free robot navigation in densely crowded environments.
匹配关键词: agent communication
---

[ACADEMIC - ARXIV]
标题: Mitigating Misalignment Contagion by Steering with Implicit Traits
作者: Maria Chang, Ronny Luss, Miao Lui, Keerthiram Murugesan, Karthikeyan Ramamurthy, Djallel Bouneffouf
链接: https://arxiv.org/abs/2605.02751v1
完整摘要: Language models (LMs) are increasingly used in high-stakes, multi-agent settings, where following instructions and maintaining value alignment are critical. Most alignment research focuses on interactions between a single LM and a single user, failing to address the risk of misaligned behavior spreading between multiple LMs in multi-turn interactions. We find evidence of this phenomenon, which we call misalignment contagion, across multiple LMs as they engage multi-turn conversational social dilemma games. Specifically, we find that LMs become more anti-social after gameplay and that this effect is intensified when other players are steered to act maliciously. We explore different steering techniques to mitigate such misalignment contagion and find that reinforcing an LM's system prompt is insufficient and often harmful. Instead, we propose steering with implicit traits: a technique that intermittently injects system prompts with statements that reinforce an LMs initial traits and is more effective than system prompt repetition at keeping models in line with their initial pro-social behaviors. Importantly, this method does not require access to model parameters or internal model states, making it suitable for increasingly common use cases where complex multi-agent workflows are being designed with black box models.
匹配关键词: agent communication
---

[ACADEMIC - ARXIV]
标题: Semantic Risk-Aware Heuristic Planning for Robotic Navigation in Dynamic Environments: An LLM-Inspired Approach
作者: Hamza Ahmed Durrani, Rafay Suleman Durrani
链接: https://arxiv.org/abs/2605.02862v1
完整摘要: The integration of Large Language Model (LLM) reasoning principles into classical robot path planning represents a rapidly emerging research direction. In this paper, we propose a Semantic Risk-Aware Heuristic (SRAH) planner that encodes LLM-inspired cost functions penalising geometrically cluttered or high-risk zones into an A$^*$ search framework, augmented with closed-loop replanning upon dynamic obstacle detection. We evaluate SRAH against two established baselines Breadth-First Search (BFS) with replanning and a Greedy heuristic without replanning across 200 randomised trials in a $15{\times}15$ grid-world with 20\% static obstacle density and stochastic dynamic obstacles. SRAH achieves a task success rate of 62.0\%, outperforming BFS (56.5\%) by 9.7\% relative improvement and Greedy (4.0\%) by a large margin. We further analyse the trade-off between planning overhead, path efficiency, and failure-recovery count, and demonstrate via an obstacle-density ablation that semantic cost shaping consistently improves navigation across environments of varying difficulty. Our results suggest that even lightweight, LLM-inspired heuristics provide measurable safety and robustness gains for autonomous robot navigation.
匹配关键词: emergent behavior
---

[ACADEMIC - ARXIV]
标题: Standing on the Shoulders of Giants: Stabilized Knowledge Distillation for Cross--Language Code Clone Detection
作者: Mohamad Khajezade, Fatemeh H. Fard, Mohamed Sami Shehata
链接: https://arxiv.org/abs/2605.02860v1
完整摘要: Cross-language code clone detection (X-CCD) is challenging because semantically equivalent programs written in different languages often share little surface similarity. Although large language models (LLMs) have shown promise for semantic clone detection, their use as black-box systems raises concerns about cost, reproducibility, privacy, and unreliable output formatting. In particular, compact open-source models often struggle to follow reasoning-oriented prompts and to produce outputs that can be consistently mapped to binary clone labels. To address these limitations, we propose a knowledge distillation framework that transfers reasoning capabilities from DeepSeek-R1 into compact open-source student models for X-CCD. Using cross-language code pairs derived from Project CodeNet, we construct reasoning-oriented synthetic training data and fine-tune Phi3 and Qwen-Coder with LoRA adapters. We further introduce response stabilization methods, including forced conclusion prompting, a binary classification head, and a contrastive classification head, and evaluate model behavior using both predictive metrics and response rate. Experiments on Python--Java, Rust--Java, Rust--Python, and Rust--Ruby show that knowledge distillation consistently improves the reliability of compact models and often improves predictive performance, especially under distribution shift. In addition, classification-head variants substantially reduce inference time compared to generation-based inference. Overall, our results show that reasoning-oriented distillation combined with response stabilization makes compact open-source models more practical and reliable for X-CCD detection.
匹配关键词: emergent behavior
---

[ACADEMIC - ARXIV]
标题: From Sensors to Insight: Rapid, Edge-to-Core Application Development for Sensor-Driven Applications
作者: Komal Thareja, Anirban Mandal, Ewa Deelman
链接: https://arxiv.org/abs/2605.02859v1
完整摘要: Scientists increasingly rely on sensor-based data, yet transforming raw streams into insights across the edge-to-cloud continuum remains difficult. Provisioning heterogeneous infrastructure and managing execution on emerging platforms like Data Processing Units typically requires cross-domain expertise, creating significant barriers to rapid prototyping. This paper introduces an experience-driven methodology for the rapid development of sensor-driven applications. By combining pattern-based workflow engineering with AI-assisted development-implemented via Pegasus on the FABRIC testbed - we utilize an existing Orcasound hydrophone workflow as a reusable template. We introduce a pattern-based engineering methodology to generate and refine workflows for air quality, earthquake, and soil moisture monitoring. Furthermore, we show how these abstract structures are extended to edge resources through modular configuration and placement. Our evaluation focuses on user productivity and practical lessons rather than peak performance. Through these case studies, we illustrate how AI-assisted, pattern-based development lowers the entry barrier for non-experts and enables iterative exploration of sensor-driven applications across distributed infrastructures.
匹配关键词: emergent behavior
---

[ACADEMIC - ARXIV]
标题: HAAS: A Policy-Aware Framework for Adaptive Task Allocation Between Humans and Artificial Intelligence Systems
作者: Vicente Pelechanoa, Antoni Mestre, Manoli Albert, Miriam Gil
链接: https://arxiv.org/abs/2605.02832v1
完整摘要: Deciding how to distribute work between humans and AI systems is a central challenge in organisational design. Most approaches treat this as a binary choice, yet the operational reality is richer: humans and AI routinely share tasks or take complementary roles depending on context, fatigue, and the stakes involved. Governing that distribution -- balancing efficiency, oversight, and human capability -- remains an open problem. This paper presents Human-AI Adaptive Symbiosis (HAAS), an implemented framework for adaptive task allocation in software engineering and manufacturing. HAAS combines two coupled components: a rule-based expert system that enforces governance constraints before any learning occurs, and a contextual-bandit learner that selects among feasible collaboration modes from outcome feedback. Task-agent fit is represented through five auditable cognitive dimensions and a five-mode autonomy spectrum -- from human-only to fully autonomous -- embedded in a reproducible benchmark spanning both domains. Three empirical findings emerge. First, governance is not a binary switch but a tunable design variable: tighter constraints predictably convert autonomous AI assignments into supervised collaborations, with domain-specific costs and benefits. Second, in manufacturing, stronger governance can improve operational performance and reduce fatigue simultaneously -- a workload-buffering effect that contradicts the usual framing of governance as pure overhead. Third, no single governance setting dominates across all contexts; moderate governance becomes increasingly competitive as the learner accumulates experience within the governed action space. Together, these findings position HAAS as a pre-deployment workbench for comparing and inspecting human--AI allocation policies before organisational commitment.
匹配关键词: emergent behavior
---

[ACADEMIC - ARXIV]
标题: First-Order Efficiency for Probabilistic Value Estimation via A Statistical Viewpoint
作者: Ziqi Liu, Kiljae Lee, Yuan Zhang, Weijing Tang
链接: https://arxiv.org/abs/2605.02827v1
完整摘要: Probabilistic values, including Shapley values and semivalues, provide a model-agnostic framework to attribute the behavior of a black-box model to data points or features, with a wide range of applications including explainable artificial intelligence and data valuation. However, their exact computation requires utility evaluations over exponentially many coalitions, making Monte Carlo approximation essential in modern machine learning applications. Existing estimators are often developed through different identification strategies, including weighted averages, self-normalized weighting, regression adjustment, and weighted least squares. Our key observation is that these seemingly distinct constructions share a common first-order error structure, in which the leading term is an augmented inverse-probability weighted influence term determined by the sampling law and a working surrogate function. This first-order representation yields an explicit expression for the leading mean squared error (MSE), which characterizes how the sampling law and the surrogate jointly determine statistical efficiency. Guided by this criterion, we propose an Efficiency-Aware Surrogate-adjusted Estimator (EASE) that directly chooses the sampling law and surrogate to minimize the first-order MSE. We demonstrate that EASE consistently outperforms state-of-the-art estimators for various probabilistic values.
匹配关键词: emergent behavior
---

[ACADEMIC - ARXIV]
标题: AlbumFill: Album-Guided Reasoning and Retrieval for Personalized Image Completion
作者: Yu-Ju Tsai, Brian Price, Qing Liu, Luis Figueroa, Daniil Pakhomov, Zhihong Ding, Scott Cohen, Ming-Hsuan Yang
链接: https://arxiv.org/abs/2605.02892v1
完整摘要: Personalized image completion aims to restore occluded regions in personal photos while preserving identity and appearance. Existing methods either rely on generic inpainting models that often fail to maintain identity consistency, or assume that suitable reference images are explicitly provided. In practice, suitable references are often not explicitly provided, requiring the system to search for identity-consistent images within personal photo collections. We present AlbumFill, a training-free framework that retrieves identity-consistent references from personal albums for personalized completion. Given an occluded image and a personal album, a vision-language model infers missing semantic cues to guide composed image retrieval, and the retrieved references are used by reference-based completion models. To facilitate this task, we introduce a dataset containing 54K human-centric samples with associated album images. Experiments across multiple baselines demonstrate the difficulty of personalized completion and highlight the importance of identity-consistent reference retrieval. Project Page: https://liagm.github.io/AlbumFill/
匹配关键词: reasoning
---

[ACADEMIC - ARXIV]
标题: MolmoAct2: Action Reasoning Models for Real-world Deployment
作者: Haoquan Fang, Jiafei Duan, Donovan Clay, Sam Wang, Shuo Liu, Weikai Huang, Xiang Fan, Wei-Chuan Tsai, Shirui Chen, Yi Ru Wang, Shanli Xing, Jaemin Cho, Jae Sung Park, Ainaz Eftekhar, Peter Sushko, Karen Farley, Angad Wadhwa, Cole Harrison, Winson Han, Ying-Chun Lee, Eli VanderBilt, Rose Hendrix, Suveen Ellawela, Lucas Ngoo, Joyce Chai, Zhongzheng Ren, Ali Farhadi, Dieter Fox, Ranjay Krishna
链接: https://arxiv.org/abs/2605.02881v1
完整摘要: Vision-Language-Action (VLA) models aim to provide a single generalist controller for robots, but today's systems fall short on the criteria that matter for real-world deployment. Frontier models are closed, open-weight alternatives are tied to expensive hardware, reasoning-augmented policies pay prohibitive latency for their grounding, and fine-tuned success rates remain below the threshold for dependable use. We present MolmoAct2, a fully open action reasoning model built for practical deployment, advancing its predecessor along five axes. We introduce MolmoER, a VLM backbone specialized for spatial and embodied reasoning, trained on a 3.3M-sample corpus with a specialize-then-rehearse recipe. We release three new datasets spanning low-to-medium cost platforms, including MolmoAct2-BimanualYAM, 720 hours of teleoperated bimanual trajectories that constitute the largest open bimanual dataset to date, together with quality-filtered Franka (DROID) and SO100/101 subsets. We provide OpenFAST, an open-weight, open-data action tokenizer trained on millions of trajectories across five embodiments. We redesign the architecture to graft a flow-matching continuous-action expert onto a discrete-token VLM via per-layer KV-cache conditioning. Finally, we propose MolmoThink, an adaptive-depth reasoning variant that re-predicts depth tokens only for scene regions that change between timesteps, retaining geometric grounding at a fraction of prior latency. In the most extensive empirical study of any open VLA to date, spanning 7 simulation and real-world benchmarks, MolmoAct2 outperforms strong baselines including Pi-05, while MolmoER surpasses GPT-5 and Gemini Robotics ER-1.5 across 13 embodied-reasoning benchmarks. We release model weights, training code, and complete training data. Project page: https://allenai.org/blog/molmoact2
匹配关键词: reasoning
---

[ACADEMIC - ARXIV]
标题: Semantic Risk-Aware Heuristic Planning for Robotic Navigation in Dynamic Environments: An LLM-Inspired Approach
作者: Hamza Ahmed Durrani, Rafay Suleman Durrani
链接: https://arxiv.org/abs/2605.02862v1
完整摘要: The integration of Large Language Model (LLM) reasoning principles into classical robot path planning represents a rapidly emerging research direction. In this paper, we propose a Semantic Risk-Aware Heuristic (SRAH) planner that encodes LLM-inspired cost functions penalising geometrically cluttered or high-risk zones into an A$^*$ search framework, augmented with closed-loop replanning upon dynamic obstacle detection. We evaluate SRAH against two established baselines Breadth-First Search (BFS) with replanning and a Greedy heuristic without replanning across 200 randomised trials in a $15{\times}15$ grid-world with 20\% static obstacle density and stochastic dynamic obstacles. SRAH achieves a task success rate of 62.0\%, outperforming BFS (56.5\%) by 9.7\% relative improvement and Greedy (4.0\%) by a large margin. We further analyse the trade-off between planning overhead, path efficiency, and failure-recovery count, and demonstrate via an obstacle-density ablation that semantic cost shaping consistently improves navigation across environments of varying difficulty. Our results suggest that even lightweight, LLM-inspired heuristics provide measurable safety and robustness gains for autonomous robot navigation.
匹配关键词: reasoning
---

[ACADEMIC - ARXIV]
标题: Standing on the Shoulders of Giants: Stabilized Knowledge Distillation for Cross--Language Code Clone Detection
作者: Mohamad Khajezade, Fatemeh H. Fard, Mohamed Sami Shehata
链接: https://arxiv.org/abs/2605.02860v1
完整摘要: Cross-language code clone detection (X-CCD) is challenging because semantically equivalent programs written in different languages often share little surface similarity. Although large language models (LLMs) have shown promise for semantic clone detection, their use as black-box systems raises concerns about cost, reproducibility, privacy, and unreliable output formatting. In particular, compact open-source models often struggle to follow reasoning-oriented prompts and to produce outputs that can be consistently mapped to binary clone labels. To address these limitations, we propose a knowledge distillation framework that transfers reasoning capabilities from DeepSeek-R1 into compact open-source student models for X-CCD. Using cross-language code pairs derived from Project CodeNet, we construct reasoning-oriented synthetic training data and fine-tune Phi3 and Qwen-Coder with LoRA adapters. We further introduce response stabilization methods, including forced conclusion prompting, a binary classification head, and a contrastive classification head, and evaluate model behavior using both predictive metrics and response rate. Experiments on Python--Java, Rust--Java, Rust--Python, and Rust--Ruby show that knowledge distillation consistently improves the reliability of compact models and often improves predictive performance, especially under distribution shift. In addition, classification-head variants substantially reduce inference time compared to generation-based inference. Overall, our results show that reasoning-oriented distillation combined with response stabilization makes compact open-source models more practical and reliable for X-CCD detection.
匹配关键词: reasoning
---

[ACADEMIC - ARXIV]
标题: SCPRM: A Schema-aware Cumulative Process Reward Model for Knowledge Graph Question Answering
作者: Jiujiu Chen, Yazheng Liu, Sihong Xie, Hui Xiong
链接: https://arxiv.org/abs/2605.02819v1
完整摘要: Large language models excel at complex reasoning, yet evaluating their intermediate steps remains challenging. Although process reward models provide step-wise supervision, they often suffer from a risk compensation effect, where incorrect steps are offset by later correct ones, assigning high rewards to flawed reasoning paths. This issue is further exacerbated in knowledge graph (KG) reasoning, as there may exist multiple paths between the start and end entities in the KGs, and a risky step can make the reasoning path flawed. Those limitations are problematic in risk-sensitive tasks such as medical and legal KG reasoning. To address the issues, we propose a Schema-aware Cumulative Process Reward Model (SCPRM) that evaluates reasoning paths by conditioning on the reasoning prefix , and incorporating schema distance between current reasoning step and the implicit target parsed from the query, which provides cumulative and future rewards to guide the path explorations. We further integrate SCPRM into Monte Carlo Tree Search (MCTS) as SCPRM-MCTS to conduct multi-hop reasoning on KGs for question answering (QA) tasks. Across medical and legal KGQA and CWQ, SCPRM-MCTS improves the performance of Hits@k by an average of 1.18% over strong baselines, demonstrating more accurate and risk-sensitive reasoning evaluation.
匹配关键词: reasoning
---

[ACADEMIC - ARXIV]
标题: Bolek: A Multimodal Language Model for Molecular Reasoning
作者: Frederic Grabowski, Jacek Szczerbiński, Maciej Jaśkowski, Kalina Jasińska-Kobus, Paweł Dąbrowski-Tumański, Tomasz Jetka, Bartosz Topolski
链接: https://arxiv.org/abs/2605.02745v1
完整摘要: Molecular property models increasingly support high-stakes drug-discovery decisions, but their outputs are often difficult to audit: classical predictors return scores without rationale, while language models can produce fluent explanations weakly grounded in the input molecule. We introduce Bolek, a compact multimodal language model that grounds natural-language reasoning in molecular structure by injecting a Morgan fingerprint embedding into an instruction-tuned text decoder. Bolek is fine-tuned on molecular alignment tasks, including molecule description, RDKit descriptor prediction, and substructure detection, and on downstream reasoning over 15 TDC binary classification tasks using synthetic chains-of-thought anchored in concrete molecular features. Across these tasks, Bolek outperforms its Qwen3-4B-Instruct base on all endpoints in yes/no mode and on 13 of 15 in chain-of-thought mode, raising mean ROC/PR AUC from 0.55 to 0.76. It also outperforms TxGemma-9B-Chat on 13 of 15 binary classification tasks despite being less than half its size. Bolek's explanations are more grounded than those of the baseline LLMs: it cites numerical descriptors 10-100x more often per chain-of-thought, and the cited values agree strongly with RDKit for key descriptors such as TPSA, MolLogP, and MolWt (Spearman rho = 0.87-0.91). Generalisation extends beyond the training panel: on 15 unseen TDC classification endpoints, Bolek matches TxGemma on five, and it produces non-trivial rank correlations on three held-out regression endpoints despite never seeing downstream regression during training. These results suggest that targeted modality injection and reasoning supervision tied to verifiable molecular features can yield compact, auditable molecular reasoning models.
匹配关键词: chain-of-thought
---

[ACADEMIC - ARXIV]
标题: Visual Latents Know More Than They Say: Unsilencing Latent Reasoning in MLLMs
作者: Xin Zhang, Qiqi Tao, Jiawei Du, Moyun Liu, Joey Tianyi Zhou
链接: https://arxiv.org/abs/2605.02735v1
完整摘要: Continuous latent-space reasoning offers a compact alternative to textual chain-of-thought for multimodal models, enabling high-dimensional visual evidence to be integrated without explicit reasoning tokens. However, we identify a previously overlooked optimization pathology in existing latent visual reasoning methods: although visual latents become semantically enriched during training, their contribution to final answer prediction is systematically suppressed. Within the shared parameter space, the autoregressive objective favors shortcut reliance on direct visual input, driving latent tokens toward transition-like states rather than informative reasoning content. We term this phenomenon Silenced Visual Latents. To address it, we disentangle the two conflicting objectives by directly optimizing the latent reasoning at inference time, keeping backbone parameters frozen. In Stage I, visual latents are warmed up via query-guided contrastive latent--visual alignment, improving semantic quality while preventing latent collapse. In Stage II, the latent reasoning is further optimized via a confidence-progression reward, which incentivizes predicted token distributions along the latent span to become progressively more concentrated, routing predictions through the latent reasoning rather than bypassing it. Experiments across eight benchmarks and four model backbones show that inference-time latent optimization, without any parameter updates, effectively unleashes the suppressed reasoning capacity of visual latents.
匹配关键词: chain-of-thought
---

[ACADEMIC - ARXIV]
标题: Position: How can Graphs Help Large Language Models?
作者: Xiyuan Wang, Yi Hu, Yanbo Wang, Chuan Shi, Muhan Zhang
链接: https://arxiv.org/abs/2605.02452v1
完整摘要: With the rapid advancement of large language models (LLMs), classic graph learning tasks have greatly benefited from LLMs, including improved encoding of textual features, more efficient construction of graphs from text, and enhanced reasoning over knowledge graphs. In this paper, we ask a complementary question: How can graphs help LLMs? We address this question from three perspectives: 1) graphs provide an up-to-date knowledge source that helps reduce LLM hallucinations, 2) graph-based prompting techniques-such as Chain-of-Thought (CoT), Tree-of-Thought (ToT), and Graph-of-Thought (GoT)-enhance LLM reasoning capabilities, and 3) integrating graphs into LLMs improves their understanding of structured data, expanding their applicability to domains such as e-commerce, code, and relational databases (RDBs). We further outlook some future directions including designing sparse LLM architectures based on graphs and brain-inspired memory systems.
匹配关键词: chain-of-thought
---

[ACADEMIC - ARXIV]
标题: SpecKV: Adaptive Speculative Decoding with Compression-Aware Gamma Selection
作者: Shikhar Shukla
链接: https://arxiv.org/abs/2605.02888v1
完整摘要: Speculative decoding accelerates large language model (LLM) inference by using a small draft model to propose candidate tokens that a larger target model verifies. A critical hyperparameter in this process is the speculation length~$γ$, which determines how many tokens the draft model proposes per step. Nearly all existing systems use a fixed~$γ$ (typically~4), yet empirical evidence suggests that the optimal value varies across task types and, crucially, depends on the compression level applied to the target model. In this paper, we present \textbf{SpecKV}, a lightweight adaptive controller that selects~$γ$ per speculation step using signals extracted from the draft model itself. We profile speculative decoding across 4~task categories, 4~speculation lengths, and 3~compression levels (FP16, INT8, NF4), collecting 5,112 step-level records with per-step acceptance rates, draft entropy, and draft confidence. We demonstrate that the optimal~$γ$ shifts across compression regimes and that draft model confidence and entropy are strong predictors of acceptance rate (correlation~$\approx 0.56$). SpecKV uses a small MLP trained on these signals to maximize expected tokens per speculation step, achieving a 56.0\% improvement over the fixed-$γ$=4 baseline with only 0.34\,ms overhead per decision ($<$0.5\% of step time). The improvement is statistically significant ($p < 0.001$, paired bootstrap test). We release all profiling data, trained models, and notebooks as open-source artifacts.
匹配关键词: test-time compute
---

[ACADEMIC - ARXIV]
标题: (POSTER) From Sensors to Insight: Rapid, Edge-to-Core Application Development for Sensor-Driven Applications
作者: Komal Thareja, Anirban Mandal, Ewa Deelman
链接: https://arxiv.org/abs/2605.02844v1
完整摘要: Scientists increasingly rely on sensor-based data; however transforming raw streams into insights across the edge-to-cloud continuum remains difficult due to the breadth of expertise required to coordinate the necessary data and computation flow. This paper introduces a pattern-based, AI-assisted methodology for rapid development of sensor-driven applications. Using Pegasus workflows executing on the FABRIC testbed, we demonstrate a 5-step development loop that shifts workflow construction and deployment from code-first to intent-first design. Starting from an existing Orcasound hydrophone workflow as a reusable template, we generate and refine workflows for air quality, earthquake, and soil moisture monitoring applications. We further show how these workflows extend to edge resources-including BlueField-3 DPUs and Raspberry Pis-through configuration and placement rather than workflow redesign. Our evaluation, from the perspective of a novice Pegasus user, shows that AI-assisted pattern reuse compresses multi-stage workflow development to 1-1.5 days per workflow while preserving the rigor and portability of workflow-based execution.
匹配关键词: test-time compute
---

[ACADEMIC - ARXIV]
标题: VideoNet: A Large-Scale Dataset for Domain-Specific Action Recognition
作者: Tanush Yadav, Mohammadreza Salehi, Jae Sung Park, Vivek Ramanujan, Hannaneh Hajishirzi, Yejin Choi, Ali Farhadi, Rohun Tripathi, Ranjay Krishna
链接: https://arxiv.org/abs/2605.02834v1
完整摘要: Videos are unique in their ability to capture actions which transcend multiple frames. Accordingly, for many years action recognition was the quintessential task for video understanding. Unfortunately, due to a lack of sufficiently diverse and challenging data, modern vision-language models (VLMs) are no longer evaluated on their action recognition capabilities. To revitalize action recognition in the era of VLMs, we advocate for a returned focus on domain-specific actions. To this end, we introduce VideoNet, a domain-specific action recognition benchmark covering 1,000 distinct actions from 37 domains. We begin with a multiple-choice evaluation setting, where the difference between closed and open models is stark: Gemini 3.1 Pro attains 69.9% accuracy while Qwen3-VL-8B gets a mere 45.0%. To understand why VLMs struggle on VideoNet, we relax the questions into a binary setting, where random chance is 50%. Still, Qwen achieves only 59.2% accuracy. Further relaxing the evaluation setup, we provide $k\in\{1,2,3\}$ in-context examples of the action. Some models excel in the few-shot setting, while others falter; Qwen improves $+7.0\%$, while Gemini declines $-4.8\%$. Notably, these gains fall short of the $+13.6\%$ improvement in non-expert humans when given few-shot examples. Finding that VLMs struggle to fully exploit in-context examples, we shift from test-time improvements to the training side. We collect the first large-scale training dataset for domain-specific actions, totaling nearly 500k video question-answer pairs. Fine-tuning a Molmo2-4B model on our data, we surpass all open-weight 8B models on the VideoNet benchmark.
匹配关键词: test-time compute
---

[ACADEMIC - ARXIV]
标题: First-Order Efficiency for Probabilistic Value Estimation via A Statistical Viewpoint
作者: Ziqi Liu, Kiljae Lee, Yuan Zhang, Weijing Tang
链接: https://arxiv.org/abs/2605.02827v1
完整摘要: Probabilistic values, including Shapley values and semivalues, provide a model-agnostic framework to attribute the behavior of a black-box model to data points or features, with a wide range of applications including explainable artificial intelligence and data valuation. However, their exact computation requires utility evaluations over exponentially many coalitions, making Monte Carlo approximation essential in modern machine learning applications. Existing estimators are often developed through different identification strategies, including weighted averages, self-normalized weighting, regression adjustment, and weighted least squares. Our key observation is that these seemingly distinct constructions share a common first-order error structure, in which the leading term is an augmented inverse-probability weighted influence term determined by the sampling law and a working surrogate function. This first-order representation yields an explicit expression for the leading mean squared error (MSE), which characterizes how the sampling law and the surrogate jointly determine statistical efficiency. Guided by this criterion, we propose an Efficiency-Aware Surrogate-adjusted Estimator (EASE) that directly chooses the sampling law and surrogate to minimize the first-order MSE. We demonstrate that EASE consistently outperforms state-of-the-art estimators for various probabilistic values.
匹配关键词: test-time compute
---

[ACADEMIC - ARXIV]
标题: Multi-Axis Speech Similarity via Factor-Partitioned Embeddings
作者: Jim O'Regan, Jens Edlund
链接: https://arxiv.org/abs/2605.02804v1
完整摘要: Speech encodes multiple simultaneous attributes--linguistic content, speaker identity, dialect, gender--that conventional single-vector embeddings conflate. We present a factor-partitioned embedding framework that maps each utterance into a single vector whose subspaces correspond to distinct axes of variation. A shared acoustic encoder feeds per-axis linear projection heads, each trained via distillation from a specialist teacher or a contrastive objective over shared-label pairs. The resulting embeddings support attribute-conditioned retrieval: similarity is computed as a signed weighted sum over per-axis cosine scores, allowing retrieval that jointly considers what was said and how --or explicitly suppresses one attribute to surface another. We evaluate on cross-corpus retrieval over corpora sharing the Harvard sentence prompts, demonstrating that signed axis weighting can suppress same-speaker bias and surface semantically matched utterances across recording conditions.
匹配关键词: test-time compute
---

[ACADEMIC - ARXIV]
标题: First-Order Efficiency for Probabilistic Value Estimation via A Statistical Viewpoint
作者: Ziqi Liu, Kiljae Lee, Yuan Zhang, Weijing Tang
链接: https://arxiv.org/abs/2605.02827v1
完整摘要: Probabilistic values, including Shapley values and semivalues, provide a model-agnostic framework to attribute the behavior of a black-box model to data points or features, with a wide range of applications including explainable artificial intelligence and data valuation. However, their exact computation requires utility evaluations over exponentially many coalitions, making Monte Carlo approximation essential in modern machine learning applications. Existing estimators are often developed through different identification strategies, including weighted averages, self-normalized weighting, regression adjustment, and weighted least squares. Our key observation is that these seemingly distinct constructions share a common first-order error structure, in which the leading term is an augmented inverse-probability weighted influence term determined by the sampling law and a working surrogate function. This first-order representation yields an explicit expression for the leading mean squared error (MSE), which characterizes how the sampling law and the surrogate jointly determine statistical efficiency. Guided by this criterion, we propose an Efficiency-Aware Surrogate-adjusted Estimator (EASE) that directly chooses the sampling law and surrogate to minimize the first-order MSE. We demonstrate that EASE consistently outperforms state-of-the-art estimators for various probabilistic values.
匹配关键词: self-consistency
---

[ACADEMIC - ARXIV]
标题: Representation learning from OCT images
作者: Hedi Tabia, Désiré Sidibé, Nawres Khlifa, Ahmed Tabia, Ines Rahmany, Noura Aboudi, Zainab Haddad, Hajer Khachnaoui, Hsouna Zgolli
链接: https://arxiv.org/abs/2605.02589v1
完整摘要: Optical Coherence Tomography (OCT) has become one of the most used imaging modality in ophthalmology. It provides high-resolution, non-invasive visualization of retinal microarchitecture. The automated analysis of OCT images through representation learning has emerged as a central research frontier. This has mainly been driven by the clinical need to process large acquisition volumes. The objective is to reduce the reliance on expert annotation, and improve diagnostic consistency across devices and populations. This survey provides a comprehensive and structured review of representation learning methods for retinal OCT image analysis. It covers the period from early deep learning approaches to the most recent developments in foundation models and vision-language systems. We organize the literature along a principled taxonomy of learning paradigms, encompassing supervised learning with CNN-based and transformer-based architectures, self-supervised and semi-supervised methods, generative approaches, as well as 3D volumetric modeling, multimodal representation learning, and large-scale pretrained foundation models. For each paradigm, we analyze the core methodological contributions, identify persistent limitations, and trace the connections between successive approaches. We further provide a structured overview of publicly available OCT datasets, discuss evaluation protocol considerations, and present a unified problem formulation that situates each learning paradigm within a common mathematical framework. Building on this analysis, we identify and discuss the most pressing open research directions emerging in the literature. This includes volumetric foundation model pretraining, uncertainty-aware representation learning, federated and privacy-preserving training, fairness and bias mitigation, concept-based interpretability,...
匹配关键词: self-consistency
---

[ACADEMIC - ARXIV]
标题: SpecKV: Adaptive Speculative Decoding with Compression-Aware Gamma Selection
作者: Shikhar Shukla
链接: https://arxiv.org/abs/2605.02888v1
完整摘要: Speculative decoding accelerates large language model (LLM) inference by using a small draft model to propose candidate tokens that a larger target model verifies. A critical hyperparameter in this process is the speculation length~$γ$, which determines how many tokens the draft model proposes per step. Nearly all existing systems use a fixed~$γ$ (typically~4), yet empirical evidence suggests that the optimal value varies across task types and, crucially, depends on the compression level applied to the target model. In this paper, we present \textbf{SpecKV}, a lightweight adaptive controller that selects~$γ$ per speculation step using signals extracted from the draft model itself. We profile speculative decoding across 4~task categories, 4~speculation lengths, and 3~compression levels (FP16, INT8, NF4), collecting 5,112 step-level records with per-step acceptance rates, draft entropy, and draft confidence. We demonstrate that the optimal~$γ$ shifts across compression regimes and that draft model confidence and entropy are strong predictors of acceptance rate (correlation~$\approx 0.56$). SpecKV uses a small MLP trained on these signals to maximize expected tokens per speculation step, achieving a 56.0\% improvement over the fixed-$γ$=4 baseline with only 0.34\,ms overhead per decision ($<$0.5\% of step time). The improvement is statistically significant ($p < 0.001$, paired bootstrap test). We release all profiling data, trained models, and notebooks as open-source artifacts.
匹配关键词: process reward
---

[ACADEMIC - ARXIV]
标题: Multi-fidelity surrogates for mechanics of composites: from co-kriging to multi-fidelity neural networks
作者: Haizhou Wen, Elham Kiyani, Gang Li, Srikanth Pilla, George Em Karniadakis, Zhen Li
链接: https://arxiv.org/abs/2605.02871v1
完整摘要: Composite materials exhibit strongly hierarchical and anisotropic properties governed by coupled mechanisms spanning constituents, plies, laminates, structures, and manufacturing history. This intrinsic complexity makes predictive modeling of composites expensive, because repeated experiments and high-fidelity simulations are needed to cover large design spaces of material, structure, and manufacturing. Multi-fidelity surrogate modeling addresses this challenge by combining abundant, less expensive data with limited high-accuracy data to recover reliable high-fidelity predictions. This review presents a structured overview of multi-fidelity modeling for composite mechanics, covering Gaussian-process or Kriging-based methods, including co-Kriging, coregionalization models, autoregressive formulations, nonlinear autoregressive Gaussian processes, multi-fidelity deep Gaussian processes, and multi-fidelity neural networks. Their distinctions are examined in terms of cross-fidelity correlation, discrepancy representation, uncertainty quantification, and scalability. Selected examples of their applications to composites are introduced according to the roles that multi-fidelity surrogates play in engineering problems, including forward prediction for rapid exploration of material design spaces, inverse optimization for composite parameter identification and design search under limited high-fidelity access, and workflow integration, where heterogeneous data sources, constraints, and validation requirements determine model utility. Open question discussions highlight recurring challenges specific to composites, such as regime-dependent fidelity gaps associated with nonlinear damage and manufacturing history, mismatches between simulations and experiments, and uncertainty propagation across multi-fidelity models.
匹配关键词: process reward
---

[ACADEMIC - ARXIV]
标题: Laplacian Frequency Interaction Network for Rural Thematic Road Extraction
作者: Baiyan Chen, Weixin Zhai
链接: https://arxiv.org/abs/2605.02866v1
完整摘要: Rural thematic road network construction aims to extract topological road structures from movement trajectory images of agricultural machinery. However, this task faces challenges where downsampling methods commonly used in existing studies tend to blur the sparse high-frequency road structures, and the heavy noise from dense field operations often leads to fragmented or redundant topologies in the extracted networks. To address these challenges, we propose LFINet, a Laplacian Frequency Interaction Network. The network begins with a Laplacian Multi-scale Separator (LMS) to decouple the image into low-frequency semantic contexts and high-frequency structural details. These components are then processed by the Cross-Frequency Interaction Block (CFIB) through a dual-pathway architecture in which a High-Frequency Block (HFB) refines local structures while a Spatial Transformer (ST) captures global semantics. Subsequently, a Frequency Gated Modulation (FGM) mechanism integrates the features from pathways by leveraging semantic contexts to calibrate the structural details. Finally, a Progressive Reconstruction Decoder iteratively fuses multi-scale features to ensure topological consistency. Experiments conducted on a real-world agricultural trajectories dataset from Henan Province, China, show that LFINet establishes a new state-of-the-art. Specifically, it achieves an F1-score of 92.54% and an IoU of 86.12%, surpassing the second-ranked method by 0.64% and 1.1%, respectively. This confirms its capability to effectively construct topological road networks from noisy and sparse field data.
匹配关键词: process reward
---

[ACADEMIC - ARXIV]
标题: Pixel Perfect: Relational Image Quality Assessment with Spatially-Aware Distortions
作者: Fadeel Sher Khan, Long N. Le, Abhinau K. Venkataramanan, Seok-Jun Lee, Hamid R. Sheikh
链接: https://arxiv.org/abs/2605.02863v1
完整摘要: Traditional image quality assessment (IQA) methods rely on mean opinion scores (MOS), which are resource-intensive to collect and fail to provide interpretable, localized feedback on specific image distortions. We overcome these limitations by shifting from absolute quality prediction to a relational and directional assessment. Our approach utilizes a self-supervised synthetic distortion engine to generate training data, eliminating the need for manual annotation. A distortion prediction network is trained with an anti-symmetric objective to produce spatially-aware, disentangled maps that identify the type, intensity, and direction of distortions relative to a reference image. Subsequently, a scoring network is trained via contrastive learning on ordinally ranked image sets to predict a relational quality score. Our method provides a more granular and interpretable approach to IQA for the targeted optimization of image processing algorithms without requiring any human-labeled quality scores.
匹配关键词: process reward
---

[ACADEMIC - ARXIV]
标题: From Sensors to Insight: Rapid, Edge-to-Core Application Development for Sensor-Driven Applications
作者: Komal Thareja, Anirban Mandal, Ewa Deelman
链接: https://arxiv.org/abs/2605.02859v1
完整摘要: Scientists increasingly rely on sensor-based data, yet transforming raw streams into insights across the edge-to-cloud continuum remains difficult. Provisioning heterogeneous infrastructure and managing execution on emerging platforms like Data Processing Units typically requires cross-domain expertise, creating significant barriers to rapid prototyping. This paper introduces an experience-driven methodology for the rapid development of sensor-driven applications. By combining pattern-based workflow engineering with AI-assisted development-implemented via Pegasus on the FABRIC testbed - we utilize an existing Orcasound hydrophone workflow as a reusable template. We introduce a pattern-based engineering methodology to generate and refine workflows for air quality, earthquake, and soil moisture monitoring. Furthermore, we show how these abstract structures are extended to edge resources through modular configuration and placement. Our evaluation focuses on user productivity and practical lessons rather than peak performance. Through these case studies, we illustrate how AI-assisted, pattern-based development lowers the entry barrier for non-experts and enables iterative exploration of sensor-driven applications across distributed infrastructures.
匹配关键词: process reward
---

[ACADEMIC - ARXIV]
标题: Compress Then Adapt? No, Do It Together via Task-aware Union of Subspaces
作者: Jingze Ge, Yun Liu, Xue Geng, Wanqi Dong, Wang Zhe Mark, Min Wu, Xulei Yang
链接: https://arxiv.org/abs/2605.02829v1
完整摘要: Adapting large pretrained models to diverse tasks is now routine, yet the two dominant strategies of parameter-efficient fine-tuning (PEFT) and low-rank compression are typically composed in sequence. This decoupled practice first compresses and then fine-tunes adapters, potentially misaligning the compressed subspace with downstream objectives and squandering a global parameter budget. To overcome this limitation, we introduce JACTUS (Joint Adaptation and Compression with a Task-aware Union of Subspaces), a single framework that unifies compression and adaptation. From a small calibration set, JACTUS estimates input and pre-activation gradient covariances, forms their orthogonal union with the pretrained weight subspace, performs a projected low-rank approximation inside this union, allocates rank globally by marginal gain per parameter, and trains only a compact core matrix. This explicitly mitigates the potential misalignment between the compressed subspace and downstream objectives by coupling the directions preserved for compression with those required for adaptation, yielding a deployable low-rank model that avoids retaining full frozen weights while enabling fast and robust tuning. On vision, JACTUS attains an average 89.2% accuracy on ViT-Base across eight datasets at 80% retained parameters, surpassing strong 100% PEFT baselines (e.g., DoRA 87.9%). On language, JACTUS achieves an 80.9% average on Llama2-7B commonsense QA at the same 80% retained-parameter budget, outperforming 100% PEFT (e.g., DoRA 79.7%) and exceeding prior compress-then-finetune pipelines under the same ratained-parameter budget. We will release code.
匹配关键词: pretraining
---

[ACADEMIC - ARXIV]
标题: Linearizing Vision Transformer with Test-Time Training
作者: Yining Li, Dongchen Han, Zeyu Liu, Hanyi Wang, Yulin Wang, Gao Huang
链接: https://arxiv.org/abs/2605.02772v1
完整摘要: While linear-complexity attention mechanisms offer a promising alternative to Softmax attention for overcoming the quadratic bottleneck, training such models from scratch remains prohibitively expensive. Inheriting weights from pretrained Transformers provides an appealing shortcut, yet the fundamental representational gap between Softmax and linear attention prevents effective weight transfer. In this work, we address this conversion challenge from two perspectives: architectural alignment and representational alignment. We identify Test-Time Training (TTT) as a linear-complexity architecture whose two-layer dynamic formulation is structurally aligned with Softmax attention, enabling direct inheritance of pretrained attention weights. To further align representational properties, including key shift-invariance and locality, we introduce key instance normalization and a lightweight locality enhancement module. We validate our approach by linearizing Stable Diffusion 3.5 and introduce SD3.5-T$^5$ (Transformer To Test Time Training). With only 1 hour of fine-tuning on 4$\times$H20 GPUs, SD3.5-T$^5$ achieves comparable text-to-image quality to the fine-tuned Softmax model, while accelerating inference by 1.32$\times$ and 1.47$\times$ at 1K and 2K resolutions.
匹配关键词: pretraining
---

[ACADEMIC - ARXIV]
标题: Virtual Scanning for NSCLC Histology: Investigating the Discriminatory Power of Synthetic PET
作者: Fatih Aksu, Laura Ciuffetti, Francesco Di Feola, Filippo Ruffini, Giulia Romoli, Fabrizia Gelardi, Arturo Chiti, Valerio Guarrasi, Paolo Soda
链接: https://arxiv.org/abs/2605.02746v1
完整摘要: Accurate histological differentiation between adenocarcinoma (ADC) and squamous cell carcinoma (SCC) is critical for personalized treatment in non-small cell lung cancer (NSCLC). While [$^{18}$F]FDG PET/CT is a standard tool for the clinical evaluation of lung cancer, its utility is often limited by high costs and radiation exposure. In this paper, we investigate the feasibility of "virtual scanning" as a feature-enhancement strategy by evaluating whether synthetic PET data can provide complementary feature representations to supplement anatomical CT scans in histological subtype classification. We propose a framework that leverages a 3D Pix2Pix Generative Adversarial Network (GAN), pretrained on the FDG-PET/CT Lesions dataset, to synthesize pseudo-PET volumes from anatomical CT scans. These synthetic volumes are integrated with structural CT data within the MINT framework, a multi-stage intermediate fusion architecture. Our experiments, conducted on a multi-center dataset of 714 subjects, demonstrate that the inclusion of synthetic metabolic features significantly improves classification performance over a CT-only baseline. The multimodal approach achieved a statistically significant increase in the Area Under the Curve (AUC) from 0.489 to 0.591 and improved the Geometric Mean (GMean) from 0.305 to 0.524. These results suggest that synthetic PET scans provide discriminatory metabolic cues that enable deep learning models to exploit complementary cross-modal information, offering a potential feature-enhancement strategy for clinical scenarios where physical PET scans are unavailable.
匹配关键词: pretraining
---

[ACADEMIC - ARXIV]
标题: Rethinking Low-Light Image Enhancement: A Log-Domain Intensity--Chromaticity Decoupling Perspective
作者: Guangrui Bai, Yifan Mei, Yahui Deng, Yuhan Chen, Yuze Qiu, Wenhai Liu, Erbao Dong
链接: https://arxiv.org/abs/2605.02627v1
完整摘要: Explicit reconstruction constraints derived from the decoupled representation are further imposed to suppress abnormal channel amplification and chromatic noise. Experiments on LOLv2-Real, MIT-Adobe FiveK, and LSRW show that the proposed method achieves competitive or superior quantitative and visual performance, reaching 29.71 dB PSNR and 0.89 SSIM on LOLv2-Real. DarkFace experiments further indicate improved downstream face detection under low-light conditions. Code and pretrained models are available at: https://github.com/mubaisam/ICD.
匹配关键词: pretraining
---

[ACADEMIC - ARXIV]
标题: Representation learning from OCT images
作者: Hedi Tabia, Désiré Sidibé, Nawres Khlifa, Ahmed Tabia, Ines Rahmany, Noura Aboudi, Zainab Haddad, Hajer Khachnaoui, Hsouna Zgolli
链接: https://arxiv.org/abs/2605.02589v1
完整摘要: Optical Coherence Tomography (OCT) has become one of the most used imaging modality in ophthalmology. It provides high-resolution, non-invasive visualization of retinal microarchitecture. The automated analysis of OCT images through representation learning has emerged as a central research frontier. This has mainly been driven by the clinical need to process large acquisition volumes. The objective is to reduce the reliance on expert annotation, and improve diagnostic consistency across devices and populations. This survey provides a comprehensive and structured review of representation learning methods for retinal OCT image analysis. It covers the period from early deep learning approaches to the most recent developments in foundation models and vision-language systems. We organize the literature along a principled taxonomy of learning paradigms, encompassing supervised learning with CNN-based and transformer-based architectures, self-supervised and semi-supervised methods, generative approaches, as well as 3D volumetric modeling, multimodal representation learning, and large-scale pretrained foundation models. For each paradigm, we analyze the core methodological contributions, identify persistent limitations, and trace the connections between successive approaches. We further provide a structured overview of publicly available OCT datasets, discuss evaluation protocol considerations, and present a unified problem formulation that situates each learning paradigm within a common mathematical framework. Building on this analysis, we identify and discuss the most pressing open research directions emerging in the literature. This includes volumetric foundation model pretraining, uncertainty-aware representation learning, federated and privacy-preserving training, fairness and bias mitigation, concept-based interpretability,...
匹配关键词: pretraining
---

[ACADEMIC - ARXIV]
标题: AlbumFill: Album-Guided Reasoning and Retrieval for Personalized Image Completion
作者: Yu-Ju Tsai, Brian Price, Qing Liu, Luis Figueroa, Daniil Pakhomov, Zhihong Ding, Scott Cohen, Ming-Hsuan Yang
链接: https://arxiv.org/abs/2605.02892v1
完整摘要: Personalized image completion aims to restore occluded regions in personal photos while preserving identity and appearance. Existing methods either rely on generic inpainting models that often fail to maintain identity consistency, or assume that suitable reference images are explicitly provided. In practice, suitable references are often not explicitly provided, requiring the system to search for identity-consistent images within personal photo collections. We present AlbumFill, a training-free framework that retrieves identity-consistent references from personal albums for personalized completion. Given an occluded image and a personal album, a vision-language model infers missing semantic cues to guide composed image retrieval, and the retrieved references are used by reference-based completion models. To facilitate this task, we introduce a dataset containing 54K human-centric samples with associated album images. Experiments across multiple baselines demonstrate the difficulty of personalized completion and highlight the importance of identity-consistent reference retrieval. Project Page: https://liagm.github.io/AlbumFill/
匹配关键词: foundation model
---

[ACADEMIC - ARXIV]
标题: SpecKV: Adaptive Speculative Decoding with Compression-Aware Gamma Selection
作者: Shikhar Shukla
链接: https://arxiv.org/abs/2605.02888v1
完整摘要: Speculative decoding accelerates large language model (LLM) inference by using a small draft model to propose candidate tokens that a larger target model verifies. A critical hyperparameter in this process is the speculation length~$γ$, which determines how many tokens the draft model proposes per step. Nearly all existing systems use a fixed~$γ$ (typically~4), yet empirical evidence suggests that the optimal value varies across task types and, crucially, depends on the compression level applied to the target model. In this paper, we present \textbf{SpecKV}, a lightweight adaptive controller that selects~$γ$ per speculation step using signals extracted from the draft model itself. We profile speculative decoding across 4~task categories, 4~speculation lengths, and 3~compression levels (FP16, INT8, NF4), collecting 5,112 step-level records with per-step acceptance rates, draft entropy, and draft confidence. We demonstrate that the optimal~$γ$ shifts across compression regimes and that draft model confidence and entropy are strong predictors of acceptance rate (correlation~$\approx 0.56$). SpecKV uses a small MLP trained on these signals to maximize expected tokens per speculation step, achieving a 56.0\% improvement over the fixed-$γ$=4 baseline with only 0.34\,ms overhead per decision ($<$0.5\% of step time). The improvement is statistically significant ($p < 0.001$, paired bootstrap test). We release all profiling data, trained models, and notebooks as open-source artifacts.
匹配关键词: foundation model
---

[ACADEMIC - ARXIV]
标题: MolmoAct2: Action Reasoning Models for Real-world Deployment
作者: Haoquan Fang, Jiafei Duan, Donovan Clay, Sam Wang, Shuo Liu, Weikai Huang, Xiang Fan, Wei-Chuan Tsai, Shirui Chen, Yi Ru Wang, Shanli Xing, Jaemin Cho, Jae Sung Park, Ainaz Eftekhar, Peter Sushko, Karen Farley, Angad Wadhwa, Cole Harrison, Winson Han, Ying-Chun Lee, Eli VanderBilt, Rose Hendrix, Suveen Ellawela, Lucas Ngoo, Joyce Chai, Zhongzheng Ren, Ali Farhadi, Dieter Fox, Ranjay Krishna
链接: https://arxiv.org/abs/2605.02881v1
完整摘要: Vision-Language-Action (VLA) models aim to provide a single generalist controller for robots, but today's systems fall short on the criteria that matter for real-world deployment. Frontier models are closed, open-weight alternatives are tied to expensive hardware, reasoning-augmented policies pay prohibitive latency for their grounding, and fine-tuned success rates remain below the threshold for dependable use. We present MolmoAct2, a fully open action reasoning model built for practical deployment, advancing its predecessor along five axes. We introduce MolmoER, a VLM backbone specialized for spatial and embodied reasoning, trained on a 3.3M-sample corpus with a specialize-then-rehearse recipe. We release three new datasets spanning low-to-medium cost platforms, including MolmoAct2-BimanualYAM, 720 hours of teleoperated bimanual trajectories that constitute the largest open bimanual dataset to date, together with quality-filtered Franka (DROID) and SO100/101 subsets. We provide OpenFAST, an open-weight, open-data action tokenizer trained on millions of trajectories across five embodiments. We redesign the architecture to graft a flow-matching continuous-action expert onto a discrete-token VLM via per-layer KV-cache conditioning. Finally, we propose MolmoThink, an adaptive-depth reasoning variant that re-predicts depth tokens only for scene regions that change between timesteps, retaining geometric grounding at a fraction of prior latency. In the most extensive empirical study of any open VLA to date, spanning 7 simulation and real-world benchmarks, MolmoAct2 outperforms strong baselines including Pi-05, while MolmoER surpasses GPT-5 and Gemini Robotics ER-1.5 across 13 embodied-reasoning benchmarks. We release model weights, training code, and complete training data. Project page: https://allenai.org/blog/molmoact2
匹配关键词: foundation model
---

[ACADEMIC - ARXIV]
标题: Multi-fidelity surrogates for mechanics of composites: from co-kriging to multi-fidelity neural networks
作者: Haizhou Wen, Elham Kiyani, Gang Li, Srikanth Pilla, George Em Karniadakis, Zhen Li
链接: https://arxiv.org/abs/2605.02871v1
完整摘要: Composite materials exhibit strongly hierarchical and anisotropic properties governed by coupled mechanisms spanning constituents, plies, laminates, structures, and manufacturing history. This intrinsic complexity makes predictive modeling of composites expensive, because repeated experiments and high-fidelity simulations are needed to cover large design spaces of material, structure, and manufacturing. Multi-fidelity surrogate modeling addresses this challenge by combining abundant, less expensive data with limited high-accuracy data to recover reliable high-fidelity predictions. This review presents a structured overview of multi-fidelity modeling for composite mechanics, covering Gaussian-process or Kriging-based methods, including co-Kriging, coregionalization models, autoregressive formulations, nonlinear autoregressive Gaussian processes, multi-fidelity deep Gaussian processes, and multi-fidelity neural networks. Their distinctions are examined in terms of cross-fidelity correlation, discrepancy representation, uncertainty quantification, and scalability. Selected examples of their applications to composites are introduced according to the roles that multi-fidelity surrogates play in engineering problems, including forward prediction for rapid exploration of material design spaces, inverse optimization for composite parameter identification and design search under limited high-fidelity access, and workflow integration, where heterogeneous data sources, constraints, and validation requirements determine model utility. Open question discussions highlight recurring challenges specific to composites, such as regime-dependent fidelity gaps associated with nonlinear damage and manufacturing history, mismatches between simulations and experiments, and uncertainty propagation across multi-fidelity models.
匹配关键词: foundation model
---

[ACADEMIC - ARXIV]
标题: Enhancing RL Generalizability in Robotics through SHAP Analysis of Algorithms and Hyperparameters
作者: Lingxiao Kong, Cong Yang, Oya Deniz Beyan, Zeyd Boukhers
链接: https://arxiv.org/abs/2605.02867v1
完整摘要: Despite significant advances in Reinforcement Learning (RL), model performance remains highly sensitive to algorithm and hyperparameter configurations, while generalization gaps across environments complicate real-world deployment. Although prior work has studied RL generalization, the relative contribution of specific configurations to the generalization gap has not been quantitatively decomposed and systematically leveraged for configuration selection. To address this limitation, we propose an explainable framework that evaluates RL performance across robotic environments using SHapley Additive exPlanations (SHAP) to quantify configuration impacts. We establish a theoretical foundation connecting Shapley values to generalizability, empirically analyze configuration impact patterns, and introduce SHAP-guided configuration selection to enhance generalization. Our results reveal distinct patterns across algorithms and hyperparameters, with consistent configuration impacts across diverse tasks and environments. By applying these insights to configuration selection, we achieve improved RL generalizability and provide actionable guidance for practitioners.
匹配关键词: foundation model
---

[ACADEMIC - ARXIV]
标题: Laplacian Frequency Interaction Network for Rural Thematic Road Extraction
作者: Baiyan Chen, Weixin Zhai
链接: https://arxiv.org/abs/2605.02866v1
完整摘要: Rural thematic road network construction aims to extract topological road structures from movement trajectory images of agricultural machinery. However, this task faces challenges where downsampling methods commonly used in existing studies tend to blur the sparse high-frequency road structures, and the heavy noise from dense field operations often leads to fragmented or redundant topologies in the extracted networks. To address these challenges, we propose LFINet, a Laplacian Frequency Interaction Network. The network begins with a Laplacian Multi-scale Separator (LMS) to decouple the image into low-frequency semantic contexts and high-frequency structural details. These components are then processed by the Cross-Frequency Interaction Block (CFIB) through a dual-pathway architecture in which a High-Frequency Block (HFB) refines local structures while a Spatial Transformer (ST) captures global semantics. Subsequently, a Frequency Gated Modulation (FGM) mechanism integrates the features from pathways by leveraging semantic contexts to calibrate the structural details. Finally, a Progressive Reconstruction Decoder iteratively fuses multi-scale features to ensure topological consistency. Experiments conducted on a real-world agricultural trajectories dataset from Henan Province, China, show that LFINet establishes a new state-of-the-art. Specifically, it achieves an F1-score of 92.54% and an IoU of 86.12%, surpassing the second-ranked method by 0.64% and 1.1%, respectively. This confirms its capability to effectively construct topological road networks from noisy and sparse field data.
匹配关键词: scaling law
---

[ACADEMIC - ARXIV]
标题: A Closed-Form Persistence-Landmark Pipeline for Certified Point-Cloud and Graph Classification
作者: Sushovan Majhi, Atish Mitra, Žiga Virk, Pramita Bagchi
链接: https://arxiv.org/abs/2605.02836v1
完整摘要: We introduce PLACE (Persistence-Landmark Analytic Classification Engine), a closed-form pipeline for classifying point clouds and graphs through their persistent-homology signatures. Three quantitative guarantees -- a margin-based excess-risk rate, a closed-form descriptor-selection rule, and a per-prediction certificate -- are derived from training labels alone, with no learned weights or held-out calibration. The embedding sums Mitra-Virk single-point coordinate functions over a sparse landmark grid; closed-form weights maximize a structural distortion constant $λ(ν)$ (a Lipschitz lower bound on $\mathcal{D}_n$ under non-interference). (i) An $O(kR/(Δ\sqrt{m_{\min}}))$ margin bound, driven by class-mean separation $Δ$ and embedding radius $R$, matched by a sample-starved minimax lower bound. (ii) The Mahalanobis margin under Ledoit-Wolf-shrunk covariance is the strongest closed-form descriptor selector on a heterogeneous 64-descriptor chemical-graph pool (mean Spearman $ρ\approx +0.54$ across 10 benchmarks, positive on 9 of 10); the isotropic surrogate $Δ/\sqrt\ell$ admits a closed-form selection-consistency rate on homogeneous (14-15 descriptor) protein/social pools. (iii) A training-time-decided certificate with no per-prediction overhead, in non-asymptotic Pinelis and asymptotic Gaussian plug-in forms. Empirically, PLACE is the strongest diagram-based method on Orbit5k and matches the strongest topology-based baseline within statistical noise on MUTAG and COX2. The remaining gaps fall into two diagnosable regimes: descriptor blindness on NCI1/NCI109, and pool-coverage limits elsewhere. Both radii exceed the firing threshold $\hatΔ/2$ on every benchmark at our training-set sizes, dominated by the $\sqrt\ell$ scaling of the multivariate-norm bound; the per-prediction certificate is constructive but not yet operational at these sizes.
匹配关键词: scaling law
---

[ACADEMIC - ARXIV]
标题: VideoNet: A Large-Scale Dataset for Domain-Specific Action Recognition
作者: Tanush Yadav, Mohammadreza Salehi, Jae Sung Park, Vivek Ramanujan, Hannaneh Hajishirzi, Yejin Choi, Ali Farhadi, Rohun Tripathi, Ranjay Krishna
链接: https://arxiv.org/abs/2605.02834v1
完整摘要: Videos are unique in their ability to capture actions which transcend multiple frames. Accordingly, for many years action recognition was the quintessential task for video understanding. Unfortunately, due to a lack of sufficiently diverse and challenging data, modern vision-language models (VLMs) are no longer evaluated on their action recognition capabilities. To revitalize action recognition in the era of VLMs, we advocate for a returned focus on domain-specific actions. To this end, we introduce VideoNet, a domain-specific action recognition benchmark covering 1,000 distinct actions from 37 domains. We begin with a multiple-choice evaluation setting, where the difference between closed and open models is stark: Gemini 3.1 Pro attains 69.9% accuracy while Qwen3-VL-8B gets a mere 45.0%. To understand why VLMs struggle on VideoNet, we relax the questions into a binary setting, where random chance is 50%. Still, Qwen achieves only 59.2% accuracy. Further relaxing the evaluation setup, we provide $k\in\{1,2,3\}$ in-context examples of the action. Some models excel in the few-shot setting, while others falter; Qwen improves $+7.0\%$, while Gemini declines $-4.8\%$. Notably, these gains fall short of the $+13.6\%$ improvement in non-expert humans when given few-shot examples. Finding that VLMs struggle to fully exploit in-context examples, we shift from test-time improvements to the training side. We collect the first large-scale training dataset for domain-specific actions, totaling nearly 500k video question-answer pairs. Fine-tuning a Molmo2-4B model on our data, we surpass all open-weight 8B models on the VideoNet benchmark.
匹配关键词: scaling law
---

[ACADEMIC - ARXIV]
标题: First-Order Efficiency for Probabilistic Value Estimation via A Statistical Viewpoint
作者: Ziqi Liu, Kiljae Lee, Yuan Zhang, Weijing Tang
链接: https://arxiv.org/abs/2605.02827v1
完整摘要: Probabilistic values, including Shapley values and semivalues, provide a model-agnostic framework to attribute the behavior of a black-box model to data points or features, with a wide range of applications including explainable artificial intelligence and data valuation. However, their exact computation requires utility evaluations over exponentially many coalitions, making Monte Carlo approximation essential in modern machine learning applications. Existing estimators are often developed through different identification strategies, including weighted averages, self-normalized weighting, regression adjustment, and weighted least squares. Our key observation is that these seemingly distinct constructions share a common first-order error structure, in which the leading term is an augmented inverse-probability weighted influence term determined by the sampling law and a working surrogate function. This first-order representation yields an explicit expression for the leading mean squared error (MSE), which characterizes how the sampling law and the surrogate jointly determine statistical efficiency. Guided by this criterion, we propose an Efficiency-Aware Surrogate-adjusted Estimator (EASE) that directly chooses the sampling law and surrogate to minimize the first-order MSE. We demonstrate that EASE consistently outperforms state-of-the-art estimators for various probabilistic values.
匹配关键词: scaling law
---

[ACADEMIC - ARXIV]
标题: LiDAR Teach, Radar Repeat: Robust Cross-Modal Navigation in Degenerate and Varying Environments
作者: Renxiang Xiao, Yichen Chen, Yuanfan Zhang, Qianyi Shao, Yushuai Chen, Yuxuan Han, Yunjiang Lou, Liang Hu
链接: https://arxiv.org/abs/2605.02809v1
完整摘要: Long-term autonomy requires robust navigation in environments subject to dynamic and static changes, as well as adverse weather conditions. Teach-and-Repeat (T\&R) navigation offers a reliable and cost-effective solution by avoiding the need for consistent global mapping; however, existing T\&R systems lack a systematic solution to tackle various environmental variations such as weather degradation, ephemeral dynamics, and structural changes. This work proposes LTR$^2$, the first cross-modal, cross-platform LiDAR-Teach-and-Radar-Repeat system that systematically addresses these challenges. LTR$^2$ leverages LiDAR during the teaching phase to capture precise structural information under normal conditions and utilizes 4D millimeter-wave radar during the repeating phase for robust operation under environmental degradations. To align sparse and noisy forward-looking 4D radar with dense and accurate omnidirectional 3D LiDAR data, we introduce a Cross-Modal Registration (CMR) network that jointly exploits Doppler-based motion priors and the physical laws governing LiDAR intensity and radar power density. Furthermore, we propose an adaptive fine-tuning strategy that incrementally updates the CMR network based on localization errors, enabling long-term adaptability to static environmental changes without ground-truth labels. We demonstrate that the proposed CMR network achieves state-of-the-art cross-modal registration performance on the open-access dataset. Then we validate LTR$^2$ across three robot platforms over a large-scale, long-term deployment (40+ km over 6 months), including challenging conditions such as nighttime smoke. Experimental results and ablation studies demonstrate centimeter-level accuracy and strong robustness against diverse environmental disturbances, significantly outperforming existing approaches.
匹配关键词: scaling law
---

[ACADEMIC - ARXIV]
标题: AlbumFill: Album-Guided Reasoning and Retrieval for Personalized Image Completion
作者: Yu-Ju Tsai, Brian Price, Qing Liu, Luis Figueroa, Daniil Pakhomov, Zhihong Ding, Scott Cohen, Ming-Hsuan Yang
链接: https://arxiv.org/abs/2605.02892v1
完整摘要: Personalized image completion aims to restore occluded regions in personal photos while preserving identity and appearance. Existing methods either rely on generic inpainting models that often fail to maintain identity consistency, or assume that suitable reference images are explicitly provided. In practice, suitable references are often not explicitly provided, requiring the system to search for identity-consistent images within personal photo collections. We present AlbumFill, a training-free framework that retrieves identity-consistent references from personal albums for personalized completion. Given an occluded image and a personal album, a vision-language model infers missing semantic cues to guide composed image retrieval, and the retrieved references are used by reference-based completion models. To facilitate this task, we introduce a dataset containing 54K human-centric samples with associated album images. Experiments across multiple baselines demonstrate the difficulty of personalized completion and highlight the importance of identity-consistent reference retrieval. Project Page: https://liagm.github.io/AlbumFill/
匹配关键词: language model
---

[ACADEMIC - ARXIV]
标题: SpecKV: Adaptive Speculative Decoding with Compression-Aware Gamma Selection
作者: Shikhar Shukla
链接: https://arxiv.org/abs/2605.02888v1
完整摘要: Speculative decoding accelerates large language model (LLM) inference by using a small draft model to propose candidate tokens that a larger target model verifies. A critical hyperparameter in this process is the speculation length~$γ$, which determines how many tokens the draft model proposes per step. Nearly all existing systems use a fixed~$γ$ (typically~4), yet empirical evidence suggests that the optimal value varies across task types and, crucially, depends on the compression level applied to the target model. In this paper, we present \textbf{SpecKV}, a lightweight adaptive controller that selects~$γ$ per speculation step using signals extracted from the draft model itself. We profile speculative decoding across 4~task categories, 4~speculation lengths, and 3~compression levels (FP16, INT8, NF4), collecting 5,112 step-level records with per-step acceptance rates, draft entropy, and draft confidence. We demonstrate that the optimal~$γ$ shifts across compression regimes and that draft model confidence and entropy are strong predictors of acceptance rate (correlation~$\approx 0.56$). SpecKV uses a small MLP trained on these signals to maximize expected tokens per speculation step, achieving a 56.0\% improvement over the fixed-$γ$=4 baseline with only 0.34\,ms overhead per decision ($<$0.5\% of step time). The improvement is statistically significant ($p < 0.001$, paired bootstrap test). We release all profiling data, trained models, and notebooks as open-source artifacts.
匹配关键词: language model
---

[ACADEMIC - ARXIV]
标题: MolmoAct2: Action Reasoning Models for Real-world Deployment
作者: Haoquan Fang, Jiafei Duan, Donovan Clay, Sam Wang, Shuo Liu, Weikai Huang, Xiang Fan, Wei-Chuan Tsai, Shirui Chen, Yi Ru Wang, Shanli Xing, Jaemin Cho, Jae Sung Park, Ainaz Eftekhar, Peter Sushko, Karen Farley, Angad Wadhwa, Cole Harrison, Winson Han, Ying-Chun Lee, Eli VanderBilt, Rose Hendrix, Suveen Ellawela, Lucas Ngoo, Joyce Chai, Zhongzheng Ren, Ali Farhadi, Dieter Fox, Ranjay Krishna
链接: https://arxiv.org/abs/2605.02881v1
完整摘要: Vision-Language-Action (VLA) models aim to provide a single generalist controller for robots, but today's systems fall short on the criteria that matter for real-world deployment. Frontier models are closed, open-weight alternatives are tied to expensive hardware, reasoning-augmented policies pay prohibitive latency for their grounding, and fine-tuned success rates remain below the threshold for dependable use. We present MolmoAct2, a fully open action reasoning model built for practical deployment, advancing its predecessor along five axes. We introduce MolmoER, a VLM backbone specialized for spatial and embodied reasoning, trained on a 3.3M-sample corpus with a specialize-then-rehearse recipe. We release three new datasets spanning low-to-medium cost platforms, including MolmoAct2-BimanualYAM, 720 hours of teleoperated bimanual trajectories that constitute the largest open bimanual dataset to date, together with quality-filtered Franka (DROID) and SO100/101 subsets. We provide OpenFAST, an open-weight, open-data action tokenizer trained on millions of trajectories across five embodiments. We redesign the architecture to graft a flow-matching continuous-action expert onto a discrete-token VLM via per-layer KV-cache conditioning. Finally, we propose MolmoThink, an adaptive-depth reasoning variant that re-predicts depth tokens only for scene regions that change between timesteps, retaining geometric grounding at a fraction of prior latency. In the most extensive empirical study of any open VLA to date, spanning 7 simulation and real-world benchmarks, MolmoAct2 outperforms strong baselines including Pi-05, while MolmoER surpasses GPT-5 and Gemini Robotics ER-1.5 across 13 embodied-reasoning benchmarks. We release model weights, training code, and complete training data. Project page: https://allenai.org/blog/molmoact2
匹配关键词: language model
---

[ACADEMIC - ARXIV]
标题: Multi-fidelity surrogates for mechanics of composites: from co-kriging to multi-fidelity neural networks
作者: Haizhou Wen, Elham Kiyani, Gang Li, Srikanth Pilla, George Em Karniadakis, Zhen Li
链接: https://arxiv.org/abs/2605.02871v1
完整摘要: Composite materials exhibit strongly hierarchical and anisotropic properties governed by coupled mechanisms spanning constituents, plies, laminates, structures, and manufacturing history. This intrinsic complexity makes predictive modeling of composites expensive, because repeated experiments and high-fidelity simulations are needed to cover large design spaces of material, structure, and manufacturing. Multi-fidelity surrogate modeling addresses this challenge by combining abundant, less expensive data with limited high-accuracy data to recover reliable high-fidelity predictions. This review presents a structured overview of multi-fidelity modeling for composite mechanics, covering Gaussian-process or Kriging-based methods, including co-Kriging, coregionalization models, autoregressive formulations, nonlinear autoregressive Gaussian processes, multi-fidelity deep Gaussian processes, and multi-fidelity neural networks. Their distinctions are examined in terms of cross-fidelity correlation, discrepancy representation, uncertainty quantification, and scalability. Selected examples of their applications to composites are introduced according to the roles that multi-fidelity surrogates play in engineering problems, including forward prediction for rapid exploration of material design spaces, inverse optimization for composite parameter identification and design search under limited high-fidelity access, and workflow integration, where heterogeneous data sources, constraints, and validation requirements determine model utility. Open question discussions highlight recurring challenges specific to composites, such as regime-dependent fidelity gaps associated with nonlinear damage and manufacturing history, mismatches between simulations and experiments, and uncertainty propagation across multi-fidelity models.
匹配关键词: language model
---

[ACADEMIC - ARXIV]
标题: Enhancing RL Generalizability in Robotics through SHAP Analysis of Algorithms and Hyperparameters
作者: Lingxiao Kong, Cong Yang, Oya Deniz Beyan, Zeyd Boukhers
链接: https://arxiv.org/abs/2605.02867v1
完整摘要: Despite significant advances in Reinforcement Learning (RL), model performance remains highly sensitive to algorithm and hyperparameter configurations, while generalization gaps across environments complicate real-world deployment. Although prior work has studied RL generalization, the relative contribution of specific configurations to the generalization gap has not been quantitatively decomposed and systematically leveraged for configuration selection. To address this limitation, we propose an explainable framework that evaluates RL performance across robotic environments using SHapley Additive exPlanations (SHAP) to quantify configuration impacts. We establish a theoretical foundation connecting Shapley values to generalizability, empirically analyze configuration impact patterns, and introduce SHAP-guided configuration selection to enhance generalization. Our results reveal distinct patterns across algorithms and hyperparameters, with consistent configuration impacts across diverse tasks and environments. By applying these insights to configuration selection, we achieve improved RL generalizability and provide actionable guidance for practitioners.
匹配关键词: language model
---

[ACADEMIC - ARXIV]
标题: MolmoAct2: Action Reasoning Models for Real-world Deployment
作者: Haoquan Fang, Jiafei Duan, Donovan Clay, Sam Wang, Shuo Liu, Weikai Huang, Xiang Fan, Wei-Chuan Tsai, Shirui Chen, Yi Ru Wang, Shanli Xing, Jaemin Cho, Jae Sung Park, Ainaz Eftekhar, Peter Sushko, Karen Farley, Angad Wadhwa, Cole Harrison, Winson Han, Ying-Chun Lee, Eli VanderBilt, Rose Hendrix, Suveen Ellawela, Lucas Ngoo, Joyce Chai, Zhongzheng Ren, Ali Farhadi, Dieter Fox, Ranjay Krishna
链接: https://arxiv.org/abs/2605.02881v1
完整摘要: Vision-Language-Action (VLA) models aim to provide a single generalist controller for robots, but today's systems fall short on the criteria that matter for real-world deployment. Frontier models are closed, open-weight alternatives are tied to expensive hardware, reasoning-augmented policies pay prohibitive latency for their grounding, and fine-tuned success rates remain below the threshold for dependable use. We present MolmoAct2, a fully open action reasoning model built for practical deployment, advancing its predecessor along five axes. We introduce MolmoER, a VLM backbone specialized for spatial and embodied reasoning, trained on a 3.3M-sample corpus with a specialize-then-rehearse recipe. We release three new datasets spanning low-to-medium cost platforms, including MolmoAct2-BimanualYAM, 720 hours of teleoperated bimanual trajectories that constitute the largest open bimanual dataset to date, together with quality-filtered Franka (DROID) and SO100/101 subsets. We provide OpenFAST, an open-weight, open-data action tokenizer trained on millions of trajectories across five embodiments. We redesign the architecture to graft a flow-matching continuous-action expert onto a discrete-token VLM via per-layer KV-cache conditioning. Finally, we propose MolmoThink, an adaptive-depth reasoning variant that re-predicts depth tokens only for scene regions that change between timesteps, retaining geometric grounding at a fraction of prior latency. In the most extensive empirical study of any open VLA to date, spanning 7 simulation and real-world benchmarks, MolmoAct2 outperforms strong baselines including Pi-05, while MolmoER surpasses GPT-5 and Gemini Robotics ER-1.5 across 13 embodied-reasoning benchmarks. We release model weights, training code, and complete training data. Project page: https://allenai.org/blog/molmoact2
匹配关键词: mixture of experts
---

[ACADEMIC - ARXIV]
标题: From Sensors to Insight: Rapid, Edge-to-Core Application Development for Sensor-Driven Applications
作者: Komal Thareja, Anirban Mandal, Ewa Deelman
链接: https://arxiv.org/abs/2605.02859v1
完整摘要: Scientists increasingly rely on sensor-based data, yet transforming raw streams into insights across the edge-to-cloud continuum remains difficult. Provisioning heterogeneous infrastructure and managing execution on emerging platforms like Data Processing Units typically requires cross-domain expertise, creating significant barriers to rapid prototyping. This paper introduces an experience-driven methodology for the rapid development of sensor-driven applications. By combining pattern-based workflow engineering with AI-assisted development-implemented via Pegasus on the FABRIC testbed - we utilize an existing Orcasound hydrophone workflow as a reusable template. We introduce a pattern-based engineering methodology to generate and refine workflows for air quality, earthquake, and soil moisture monitoring. Furthermore, we show how these abstract structures are extended to edge resources through modular configuration and placement. Our evaluation focuses on user productivity and practical lessons rather than peak performance. Through these case studies, we illustrate how AI-assisted, pattern-based development lowers the entry barrier for non-experts and enables iterative exploration of sensor-driven applications across distributed infrastructures.
匹配关键词: mixture of experts
---

[ACADEMIC - ARXIV]
标题: VideoNet: A Large-Scale Dataset for Domain-Specific Action Recognition
作者: Tanush Yadav, Mohammadreza Salehi, Jae Sung Park, Vivek Ramanujan, Hannaneh Hajishirzi, Yejin Choi, Ali Farhadi, Rohun Tripathi, Ranjay Krishna
链接: https://arxiv.org/abs/2605.02834v1
完整摘要: Videos are unique in their ability to capture actions which transcend multiple frames. Accordingly, for many years action recognition was the quintessential task for video understanding. Unfortunately, due to a lack of sufficiently diverse and challenging data, modern vision-language models (VLMs) are no longer evaluated on their action recognition capabilities. To revitalize action recognition in the era of VLMs, we advocate for a returned focus on domain-specific actions. To this end, we introduce VideoNet, a domain-specific action recognition benchmark covering 1,000 distinct actions from 37 domains. We begin with a multiple-choice evaluation setting, where the difference between closed and open models is stark: Gemini 3.1 Pro attains 69.9% accuracy while Qwen3-VL-8B gets a mere 45.0%. To understand why VLMs struggle on VideoNet, we relax the questions into a binary setting, where random chance is 50%. Still, Qwen achieves only 59.2% accuracy. Further relaxing the evaluation setup, we provide $k\in\{1,2,3\}$ in-context examples of the action. Some models excel in the few-shot setting, while others falter; Qwen improves $+7.0\%$, while Gemini declines $-4.8\%$. Notably, these gains fall short of the $+13.6\%$ improvement in non-expert humans when given few-shot examples. Finding that VLMs struggle to fully exploit in-context examples, we shift from test-time improvements to the training side. We collect the first large-scale training dataset for domain-specific actions, totaling nearly 500k video question-answer pairs. Fine-tuning a Molmo2-4B model on our data, we surpass all open-weight 8B models on the VideoNet benchmark.
匹配关键词: mixture of experts
---

[ACADEMIC - ARXIV]
标题: HAAS: A Policy-Aware Framework for Adaptive Task Allocation Between Humans and Artificial Intelligence Systems
作者: Vicente Pelechanoa, Antoni Mestre, Manoli Albert, Miriam Gil
链接: https://arxiv.org/abs/2605.02832v1
完整摘要: Deciding how to distribute work between humans and AI systems is a central challenge in organisational design. Most approaches treat this as a binary choice, yet the operational reality is richer: humans and AI routinely share tasks or take complementary roles depending on context, fatigue, and the stakes involved. Governing that distribution -- balancing efficiency, oversight, and human capability -- remains an open problem. This paper presents Human-AI Adaptive Symbiosis (HAAS), an implemented framework for adaptive task allocation in software engineering and manufacturing. HAAS combines two coupled components: a rule-based expert system that enforces governance constraints before any learning occurs, and a contextual-bandit learner that selects among feasible collaboration modes from outcome feedback. Task-agent fit is represented through five auditable cognitive dimensions and a five-mode autonomy spectrum -- from human-only to fully autonomous -- embedded in a reproducible benchmark spanning both domains. Three empirical findings emerge. First, governance is not a binary switch but a tunable design variable: tighter constraints predictably convert autonomous AI assignments into supervised collaborations, with domain-specific costs and benefits. Second, in manufacturing, stronger governance can improve operational performance and reduce fatigue simultaneously -- a workload-buffering effect that contradicts the usual framing of governance as pure overhead. Third, no single governance setting dominates across all contexts; moderate governance becomes increasingly competitive as the learner accumulates experience within the governed action space. Together, these findings position HAAS as a pre-deployment workbench for comparing and inspecting human--AI allocation policies before organisational commitment.
匹配关键词: mixture of experts
---

[ACADEMIC - ARXIV]
标题: When Audio-Language Models Fail to Leverage Multimodal Context for Dysarthric Speech Recognition
作者: Pehuén Moure, Niclas Pokel, Bilal Bounajma, Yingqiang Gao, Roman Boehringer, Longbiao Cheng, Shih-Chii Liu
链接: https://arxiv.org/abs/2605.02782v1
完整摘要: Automatic speech recognition (ASR) systems remain brittle on dysarthric and other atypical speech. Recent audio-language models raise the possibility of improving performance by conditioning on additional clinical context at inference time, but it is unclear whether these models can make use of such information. We introduce a benchmark built on the Speech Accessibility Project (SAP) dataset that tests whether diagnosis labels, clinician-derived speech ratings, and progressively richer clinical descriptions improve transcription accuracy for dysarthric speech. Across matched comparisons on nine models, we find that current models do not meaningfully use this context: diagnosis-informed and clinically detailed prompts yield negligible improvements and often degrade word error rate. We complement the prompting analysis with context-dependent fine-tuning, showing that LoRA adaptation with a mixture of clinical prompt formats achieves a WER of 0.066, a 52% relative reduction over the frozen baseline, while preserving performance when context is unavailable. Subgroup analyses reveal significant gains for Down syndrome and mild-severity speakers. These results clarify where current models fall short and provide a testbed for measuring progress toward more inclusive ASR.
匹配关键词: mixture of experts
---

[ACADEMIC - ARXIV]
标题: MolmoAct2: Action Reasoning Models for Real-world Deployment
作者: Haoquan Fang, Jiafei Duan, Donovan Clay, Sam Wang, Shuo Liu, Weikai Huang, Xiang Fan, Wei-Chuan Tsai, Shirui Chen, Yi Ru Wang, Shanli Xing, Jaemin Cho, Jae Sung Park, Ainaz Eftekhar, Peter Sushko, Karen Farley, Angad Wadhwa, Cole Harrison, Winson Han, Ying-Chun Lee, Eli VanderBilt, Rose Hendrix, Suveen Ellawela, Lucas Ngoo, Joyce Chai, Zhongzheng Ren, Ali Farhadi, Dieter Fox, Ranjay Krishna
链接: https://arxiv.org/abs/2605.02881v1
完整摘要: Vision-Language-Action (VLA) models aim to provide a single generalist controller for robots, but today's systems fall short on the criteria that matter for real-world deployment. Frontier models are closed, open-weight alternatives are tied to expensive hardware, reasoning-augmented policies pay prohibitive latency for their grounding, and fine-tuned success rates remain below the threshold for dependable use. We present MolmoAct2, a fully open action reasoning model built for practical deployment, advancing its predecessor along five axes. We introduce MolmoER, a VLM backbone specialized for spatial and embodied reasoning, trained on a 3.3M-sample corpus with a specialize-then-rehearse recipe. We release three new datasets spanning low-to-medium cost platforms, including MolmoAct2-BimanualYAM, 720 hours of teleoperated bimanual trajectories that constitute the largest open bimanual dataset to date, together with quality-filtered Franka (DROID) and SO100/101 subsets. We provide OpenFAST, an open-weight, open-data action tokenizer trained on millions of trajectories across five embodiments. We redesign the architecture to graft a flow-matching continuous-action expert onto a discrete-token VLM via per-layer KV-cache conditioning. Finally, we propose MolmoThink, an adaptive-depth reasoning variant that re-predicts depth tokens only for scene regions that change between timesteps, retaining geometric grounding at a fraction of prior latency. In the most extensive empirical study of any open VLA to date, spanning 7 simulation and real-world benchmarks, MolmoAct2 outperforms strong baselines including Pi-05, while MolmoER surpasses GPT-5 and Gemini Robotics ER-1.5 across 13 embodied-reasoning benchmarks. We release model weights, training code, and complete training data. Project page: https://allenai.org/blog/molmoact2
匹配关键词: transformer architecture
---

[ACADEMIC - ARXIV]
标题: Laplacian Frequency Interaction Network for Rural Thematic Road Extraction
作者: Baiyan Chen, Weixin Zhai
链接: https://arxiv.org/abs/2605.02866v1
完整摘要: Rural thematic road network construction aims to extract topological road structures from movement trajectory images of agricultural machinery. However, this task faces challenges where downsampling methods commonly used in existing studies tend to blur the sparse high-frequency road structures, and the heavy noise from dense field operations often leads to fragmented or redundant topologies in the extracted networks. To address these challenges, we propose LFINet, a Laplacian Frequency Interaction Network. The network begins with a Laplacian Multi-scale Separator (LMS) to decouple the image into low-frequency semantic contexts and high-frequency structural details. These components are then processed by the Cross-Frequency Interaction Block (CFIB) through a dual-pathway architecture in which a High-Frequency Block (HFB) refines local structures while a Spatial Transformer (ST) captures global semantics. Subsequently, a Frequency Gated Modulation (FGM) mechanism integrates the features from pathways by leveraging semantic contexts to calibrate the structural details. Finally, a Progressive Reconstruction Decoder iteratively fuses multi-scale features to ensure topological consistency. Experiments conducted on a real-world agricultural trajectories dataset from Henan Province, China, show that LFINet establishes a new state-of-the-art. Specifically, it achieves an F1-score of 92.54% and an IoU of 86.12%, surpassing the second-ranked method by 0.64% and 1.1%, respectively. This confirms its capability to effectively construct topological road networks from noisy and sparse field data.
匹配关键词: transformer architecture
---

[ACADEMIC - ARXIV]
标题: From Sensors to Insight: Rapid, Edge-to-Core Application Development for Sensor-Driven Applications
作者: Komal Thareja, Anirban Mandal, Ewa Deelman
链接: https://arxiv.org/abs/2605.02859v1
完整摘要: Scientists increasingly rely on sensor-based data, yet transforming raw streams into insights across the edge-to-cloud continuum remains difficult. Provisioning heterogeneous infrastructure and managing execution on emerging platforms like Data Processing Units typically requires cross-domain expertise, creating significant barriers to rapid prototyping. This paper introduces an experience-driven methodology for the rapid development of sensor-driven applications. By combining pattern-based workflow engineering with AI-assisted development-implemented via Pegasus on the FABRIC testbed - we utilize an existing Orcasound hydrophone workflow as a reusable template. We introduce a pattern-based engineering methodology to generate and refine workflows for air quality, earthquake, and soil moisture monitoring. Furthermore, we show how these abstract structures are extended to edge resources through modular configuration and placement. Our evaluation focuses on user productivity and practical lessons rather than peak performance. Through these case studies, we illustrate how AI-assisted, pattern-based development lowers the entry barrier for non-experts and enables iterative exploration of sensor-driven applications across distributed infrastructures.
匹配关键词: transformer architecture
---

[ACADEMIC - ARXIV]
标题: Trust, but Verify: Peeling Low-Bit Transformer Networks for Training Monitoring
作者: Arian Eamaz, Farhang Yeganegi, Mojtaba Soltanalian
链接: https://arxiv.org/abs/2605.02853v1
完整摘要: Understanding whether deep neural networks are effectively optimized remains challenging, as training occurs in highly nonconvex landscapes and standard metrics provide limited visibility into layer-wise learning quality. This challenge is particularly acute for transformer-based language models, where training is expensive, models are often reused in frozen form, and poorly optimized layers can silently degrade performance. We propose a layer-wise peeling framework for monitoring training dynamics, in which each transformer layer is locally optimized against intermediate representations of the trained model. By constructing lightweight, layer-specific reference solutions and projecting layers onto multiple intermediate outputs via different permutations, we obtain achievable baselines that enable fine-grained diagnosis of under-optimized layers. Experiments on decoder-only transformer models show that these layer-wise reference bounds can match or even surpass the trained model at various stages of training, exposing inefficiencies that remain hidden in aggregate loss curves. We further demonstrate that this analysis remains effective under binarization and quantized settings, where training dynamics are particularly fragile. Across all numerical results, the proposed bounds consistently separate apparent convergence from effective optimality, highlighting optimization opportunities that are invisible when relying on training loss alone.
匹配关键词: transformer architecture
---

[ACADEMIC - ARXIV]
标题: (POSTER) From Sensors to Insight: Rapid, Edge-to-Core Application Development for Sensor-Driven Applications
作者: Komal Thareja, Anirban Mandal, Ewa Deelman
链接: https://arxiv.org/abs/2605.02844v1
完整摘要: Scientists increasingly rely on sensor-based data; however transforming raw streams into insights across the edge-to-cloud continuum remains difficult due to the breadth of expertise required to coordinate the necessary data and computation flow. This paper introduces a pattern-based, AI-assisted methodology for rapid development of sensor-driven applications. Using Pegasus workflows executing on the FABRIC testbed, we demonstrate a 5-step development loop that shifts workflow construction and deployment from code-first to intent-first design. Starting from an existing Orcasound hydrophone workflow as a reusable template, we generate and refine workflows for air quality, earthquake, and soil moisture monitoring applications. We further show how these workflows extend to edge resources-including BlueField-3 DPUs and Raspberry Pis-through configuration and placement rather than workflow redesign. Our evaluation, from the perspective of a novice Pegasus user, shows that AI-assisted pattern reuse compresses multi-stage workflow development to 1-1.5 days per workflow while preserving the rigor and portability of workflow-based execution.
匹配关键词: transformer architecture
---

[ACADEMIC - ARXIV]
标题: Foundation Models to Unlock Real-World Evidence from Nationwide Medical Claims
作者: Fan Ma, Yuntian Liu, Xiang Lan, Weipeng Zhou, Jun Ni, Mauro Giuffrè, Lingfei Qian, Xueqing Peng, Yujia Zhou, Ruey-Ling Weng, Huan He, Lu Li, Qingyu Chen, Andrew Loza, Laila Rasmy, Degui Zhi, Yuan Lu, Chenjie Zeng, Joshua C Denny, Lee Schwamm, Daniella Meeker, Lucila Ohno-Machado, Yong Chen, Hua Xu
链接: https://arxiv.org/abs/2605.02740v1
完整摘要: Evidence derived from large-scale real-world data (RWD) is increasingly informing regulatory evaluation and healthcare decision-making. Administrative claims provide population-scale, longitudinal records of healthcare utilization, expenditure, and detailed coding of diagnoses, procedures, and medications, yet their potential as a substrate for healthcare foundation models remains largely unexplored. Here we present ReClaim, a generative transformer trained from scratch on 43.8 billion medical events from more than 200 million enrollees in the MarketScan claims data spanning 2008-2022. ReClaim models longitudinal trajectories across diagnoses, procedures, medications, and expenditure, and was scaled to 140 million, 700 million, and 1.7 billion parameters. Across over 1,000 disease-onset prediction tasks, ReClaim achieved a mean AUC of 75.6%, substantially outperforming disease-specific LightGBM (66.3%) and the transformer-based Delphi model (69.4%), with the largest gains for rare diseases. These advantages held across retrospective and prospective evaluations and in external validation on two independent datasets. Performance improved monotonically with scale, and post-training added 13.8 percentage points over pre-training alone. Beyond disease prediction, ReClaim captured financial outcomes and improved real-world evidence (RWE) analyses: for healthcare expenditure forecasting it increased explained variance from 0.28 to 0.37 relative to LightGBM, and in a target trial emulation it reduced systematic bias by 72% on average relative to Delphi. Together, these results establish administrative claims as a scalable substrate for healthcare foundation models and show that learned representations generalize across time periods and data sources, supporting disease surveillance, expenditure forecasting, and RWE generation.
匹配关键词: post-training
---

[ACADEMIC - ARXIV]
标题: Beating the Style Detector: Three Hours of Agentic Research on the AI-Text Arms Race
作者: Andreas Maier, Moritz Zaiss, Siming Bayer
链接: https://arxiv.org/abs/2605.02620v1
完整摘要: Reproducing an empirical NLP study used to take weeks. Given the released data and a modern agentic-research harness, we redo every experiment of a recent ACL\,2026 study on personal-style post-editing of LLM drafts -- and add three new ones -- with the human investigator acting only as a reviewer-in-the-loop. We reproduce all seven preregistered hypotheses and recover the paper's headline correlation between perceived self-similarity and embedding-measured self-similarity to three decimal places ($r{=}{+}0.244$, $p{<}10^{-8}$, $n{=}648$). Under a leakage-free held-out protocol, GPT-5.5 and Claude\,Opus\,4.7 close $71$--$75\,\%$ of the style gap to the same-author ceiling on $324$ paired tasks, against $24\,\%$ for the human post-edit, and beat the human post-edit on $\sim$$80\,\%$ of tasks. We then frame the same data as an AI-text detection arms race. A leave-authors-out linear SVM on LUAR-MUD embeddings reaches AUC $0.93$--$1.00$ across approaches; six diagnostics show that GPT-5.5 detection is mostly a length confound while Opus detection is a genuine stylistic signature. Given $T{=}20$ feedback iterations against the frozen detector, an Opus agent flips two of five held-out test mimics to the human half-space and shrinks every margin by an order of magnitude. With moderate effort against a known detector, a frontier LLM can already efficiently lower its own AI-detection probability. All code, $648$ mimic drafts, trained detectors, diagnostics, and adversarial trajectories are released.
匹配关键词: post-training
---

[ACADEMIC - ARXIV]
标题: Strategy-Aware Optimization Modeling with Reasoning LLMs
作者: Ruiqing Zhao, Fengzhi Li, Yuan Zuo, Rui Liu, Yansong Liu, Yunfei Ma, Fanyu Meng, Junlan Feng
链接: https://arxiv.org/abs/2605.02545v1
完整摘要: Large language models (LLMs) can generate syntactically valid optimization programs, yet often struggle to reliably choose an effective modeling strategy, leading to incorrect formulations and inefficient solver behavior. We propose SAGE, a strategy-aware framework that makes Modeling Strategy explicit in both data construction and post-training. SAGE builds a solver-verified multi-strategy dataset and trains a student model with supervised fine-tuning followed by Segment-Weighted GRPO using a composite reward over format compliance, correctness, and solver efficiency. Across eight benchmarks spanning synthetic and real-world settings, SAGE improves average pass@1 from 72.7 to 80.3 over the strongest open-source baseline. With multiple generations, SAGE discovers more distinct correct formulations and improves component-level diversity at pass@16 by 19-29%. At the largest scale, SAGE produces more compact constraint systems with 14.2% fewer constraints than the baseline, consistent with solver-efficient modeling. Overall, these results show that making Modeling Strategy explicit improves automated optimization modeling. Code is available at https://github.com/rachhhhing/SAGE.
匹配关键词: post-training
---

[ACADEMIC - ARXIV]
标题: The Model Knows, the Decoder Finds: Future Value Guided Particle Power Sampling
作者: Tu Nguyen, Rasul Tutunov, Xiaotong Ji, Matthieu Zimmer
链接: https://arxiv.org/abs/2605.02427v1
完整摘要: A recurring pattern in "reasoning without training" is that base LLMs already assign non-trivial probability mass to correct multi-step solutions; the bottleneck is locating these modes efficiently at inference time. Power sampling provides a principled way to bias decoding toward such modes by targeting p_theta(x)^alpha with alpha > 1, but practical approximations must account for future-dependent correction factors that determine which prefixes remain promising. We introduce Auxiliary Particle Power Sampling (APPS), a blockwise particle algorithm for approximating the sequence-level power target with a bounded population of partial solutions. APPS propagates hypotheses in parallel using proposal-corrected power reweighting and refines their survival through future-value-guided selection at resampling boundaries. This redistributes finite compute across competing prefixes rather than committing to a single unfolding path, while providing a direct scaling knob in the particle count and predictable peak memory. We instantiate the future-value signal with short-horizon rollouts and also study an amortized variant that replaces rollouts with a lightweight learned selection head. Across reasoning benchmarks, APPS improves the accuracy-runtime trade-off of training-free decoding and suggests that part of the gap to post-trained systems can be recovered through more faithful inference-time power approximation.
匹配关键词: post-training
---

[ACADEMIC - ARXIV]
标题: MolmoAct2: Action Reasoning Models for Real-world Deployment
作者: Haoquan Fang, Jiafei Duan, Donovan Clay, Sam Wang, Shuo Liu, Weikai Huang, Xiang Fan, Wei-Chuan Tsai, Shirui Chen, Yi Ru Wang, Shanli Xing, Jaemin Cho, Jae Sung Park, Ainaz Eftekhar, Peter Sushko, Karen Farley, Angad Wadhwa, Cole Harrison, Winson Han, Ying-Chun Lee, Eli VanderBilt, Rose Hendrix, Suveen Ellawela, Lucas Ngoo, Joyce Chai, Zhongzheng Ren, Ali Farhadi, Dieter Fox, Ranjay Krishna
链接: https://arxiv.org/abs/2605.02881v1
完整摘要: Vision-Language-Action (VLA) models aim to provide a single generalist controller for robots, but today's systems fall short on the criteria that matter for real-world deployment. Frontier models are closed, open-weight alternatives are tied to expensive hardware, reasoning-augmented policies pay prohibitive latency for their grounding, and fine-tuned success rates remain below the threshold for dependable use. We present MolmoAct2, a fully open action reasoning model built for practical deployment, advancing its predecessor along five axes. We introduce MolmoER, a VLM backbone specialized for spatial and embodied reasoning, trained on a 3.3M-sample corpus with a specialize-then-rehearse recipe. We release three new datasets spanning low-to-medium cost platforms, including MolmoAct2-BimanualYAM, 720 hours of teleoperated bimanual trajectories that constitute the largest open bimanual dataset to date, together with quality-filtered Franka (DROID) and SO100/101 subsets. We provide OpenFAST, an open-weight, open-data action tokenizer trained on millions of trajectories across five embodiments. We redesign the architecture to graft a flow-matching continuous-action expert onto a discrete-token VLM via per-layer KV-cache conditioning. Finally, we propose MolmoThink, an adaptive-depth reasoning variant that re-predicts depth tokens only for scene regions that change between timesteps, retaining geometric grounding at a fraction of prior latency. In the most extensive empirical study of any open VLA to date, spanning 7 simulation and real-world benchmarks, MolmoAct2 outperforms strong baselines including Pi-05, while MolmoER surpasses GPT-5 and Gemini Robotics ER-1.5 across 13 embodied-reasoning benchmarks. We release model weights, training code, and complete training data. Project page: https://allenai.org/blog/molmoact2
匹配关键词: fine-tuning
---

[ACADEMIC - ARXIV]
标题: Standing on the Shoulders of Giants: Stabilized Knowledge Distillation for Cross--Language Code Clone Detection
作者: Mohamad Khajezade, Fatemeh H. Fard, Mohamed Sami Shehata
链接: https://arxiv.org/abs/2605.02860v1
完整摘要: Cross-language code clone detection (X-CCD) is challenging because semantically equivalent programs written in different languages often share little surface similarity. Although large language models (LLMs) have shown promise for semantic clone detection, their use as black-box systems raises concerns about cost, reproducibility, privacy, and unreliable output formatting. In particular, compact open-source models often struggle to follow reasoning-oriented prompts and to produce outputs that can be consistently mapped to binary clone labels. To address these limitations, we propose a knowledge distillation framework that transfers reasoning capabilities from DeepSeek-R1 into compact open-source student models for X-CCD. Using cross-language code pairs derived from Project CodeNet, we construct reasoning-oriented synthetic training data and fine-tune Phi3 and Qwen-Coder with LoRA adapters. We further introduce response stabilization methods, including forced conclusion prompting, a binary classification head, and a contrastive classification head, and evaluate model behavior using both predictive metrics and response rate. Experiments on Python--Java, Rust--Java, Rust--Python, and Rust--Ruby show that knowledge distillation consistently improves the reliability of compact models and often improves predictive performance, especially under distribution shift. In addition, classification-head variants substantially reduce inference time compared to generation-based inference. Overall, our results show that reasoning-oriented distillation combined with response stabilization makes compact open-source models more practical and reliable for X-CCD detection.
匹配关键词: fine-tuning
---

[ACADEMIC - ARXIV]
标题: VideoNet: A Large-Scale Dataset for Domain-Specific Action Recognition
作者: Tanush Yadav, Mohammadreza Salehi, Jae Sung Park, Vivek Ramanujan, Hannaneh Hajishirzi, Yejin Choi, Ali Farhadi, Rohun Tripathi, Ranjay Krishna
链接: https://arxiv.org/abs/2605.02834v1
完整摘要: Videos are unique in their ability to capture actions which transcend multiple frames. Accordingly, for many years action recognition was the quintessential task for video understanding. Unfortunately, due to a lack of sufficiently diverse and challenging data, modern vision-language models (VLMs) are no longer evaluated on their action recognition capabilities. To revitalize action recognition in the era of VLMs, we advocate for a returned focus on domain-specific actions. To this end, we introduce VideoNet, a domain-specific action recognition benchmark covering 1,000 distinct actions from 37 domains. We begin with a multiple-choice evaluation setting, where the difference between closed and open models is stark: Gemini 3.1 Pro attains 69.9% accuracy while Qwen3-VL-8B gets a mere 45.0%. To understand why VLMs struggle on VideoNet, we relax the questions into a binary setting, where random chance is 50%. Still, Qwen achieves only 59.2% accuracy. Further relaxing the evaluation setup, we provide $k\in\{1,2,3\}$ in-context examples of the action. Some models excel in the few-shot setting, while others falter; Qwen improves $+7.0\%$, while Gemini declines $-4.8\%$. Notably, these gains fall short of the $+13.6\%$ improvement in non-expert humans when given few-shot examples. Finding that VLMs struggle to fully exploit in-context examples, we shift from test-time improvements to the training side. We collect the first large-scale training dataset for domain-specific actions, totaling nearly 500k video question-answer pairs. Fine-tuning a Molmo2-4B model on our data, we surpass all open-weight 8B models on the VideoNet benchmark.
匹配关键词: fine-tuning
---

[ACADEMIC - ARXIV]
标题: Compress Then Adapt? No, Do It Together via Task-aware Union of Subspaces
作者: Jingze Ge, Yun Liu, Xue Geng, Wanqi Dong, Wang Zhe Mark, Min Wu, Xulei Yang
链接: https://arxiv.org/abs/2605.02829v1
完整摘要: Adapting large pretrained models to diverse tasks is now routine, yet the two dominant strategies of parameter-efficient fine-tuning (PEFT) and low-rank compression are typically composed in sequence. This decoupled practice first compresses and then fine-tunes adapters, potentially misaligning the compressed subspace with downstream objectives and squandering a global parameter budget. To overcome this limitation, we introduce JACTUS (Joint Adaptation and Compression with a Task-aware Union of Subspaces), a single framework that unifies compression and adaptation. From a small calibration set, JACTUS estimates input and pre-activation gradient covariances, forms their orthogonal union with the pretrained weight subspace, performs a projected low-rank approximation inside this union, allocates rank globally by marginal gain per parameter, and trains only a compact core matrix. This explicitly mitigates the potential misalignment between the compressed subspace and downstream objectives by coupling the directions preserved for compression with those required for adaptation, yielding a deployable low-rank model that avoids retaining full frozen weights while enabling fast and robust tuning. On vision, JACTUS attains an average 89.2% accuracy on ViT-Base across eight datasets at 80% retained parameters, surpassing strong 100% PEFT baselines (e.g., DoRA 87.9%). On language, JACTUS achieves an 80.9% average on Llama2-7B commonsense QA at the same 80% retained-parameter budget, outperforming 100% PEFT (e.g., DoRA 79.7%) and exceeding prior compress-then-finetune pipelines under the same ratained-parameter budget. We will release code.
匹配关键词: fine-tuning
---

[ACADEMIC - ARXIV]
标题: LiDAR Teach, Radar Repeat: Robust Cross-Modal Navigation in Degenerate and Varying Environments
作者: Renxiang Xiao, Yichen Chen, Yuanfan Zhang, Qianyi Shao, Yushuai Chen, Yuxuan Han, Yunjiang Lou, Liang Hu
链接: https://arxiv.org/abs/2605.02809v1
完整摘要: Long-term autonomy requires robust navigation in environments subject to dynamic and static changes, as well as adverse weather conditions. Teach-and-Repeat (T\&R) navigation offers a reliable and cost-effective solution by avoiding the need for consistent global mapping; however, existing T\&R systems lack a systematic solution to tackle various environmental variations such as weather degradation, ephemeral dynamics, and structural changes. This work proposes LTR$^2$, the first cross-modal, cross-platform LiDAR-Teach-and-Radar-Repeat system that systematically addresses these challenges. LTR$^2$ leverages LiDAR during the teaching phase to capture precise structural information under normal conditions and utilizes 4D millimeter-wave radar during the repeating phase for robust operation under environmental degradations. To align sparse and noisy forward-looking 4D radar with dense and accurate omnidirectional 3D LiDAR data, we introduce a Cross-Modal Registration (CMR) network that jointly exploits Doppler-based motion priors and the physical laws governing LiDAR intensity and radar power density. Furthermore, we propose an adaptive fine-tuning strategy that incrementally updates the CMR network based on localization errors, enabling long-term adaptability to static environmental changes without ground-truth labels. We demonstrate that the proposed CMR network achieves state-of-the-art cross-modal registration performance on the open-access dataset. Then we validate LTR$^2$ across three robot platforms over a large-scale, long-term deployment (40+ km over 6 months), including challenging conditions such as nighttime smoke. Experimental results and ablation studies demonstrate centimeter-level accuracy and strong robustness against diverse environmental disturbances, significantly outperforming existing approaches.
匹配关键词: fine-tuning
---

[ACADEMIC - ARXIV]
标题: Gradient-Gated DPO: Stabilizing Preference Optimization in Language Models
作者: Inoussa Mouiche
链接: https://arxiv.org/abs/2605.02626v1
完整摘要: Preference optimization has become a central paradigm for aligning large language models with human feedback. Direct Preference Optimization (DPO) simplifies reinforcement learning from human feedback by directly optimizing pairwise preferences, removing the need for reward modeling and policy optimization. However, recent work shows that DPO exhibits a squeezing effect, where negative gradients applied to rejected responses concentrate probability mass on high-confidence predictions while suppressing alternative responses. This phenomenon arises even in simple softmax models and can lead to systematic probability collapse during training. We introduce Gradient-Gated Preference Optimization (Gate-DPO), a method that stabilizes training by modulating rejected gradients according to the model's probability geometry. When updates target extremely low-probability responses, the gate attenuates harmful gradients while preserving standard optimization behavior. Gate-DPO addresses this optimization pathology without modifying the underlying preference objective and is complementary to existing methods such as extended SFT, IPO, and Cal-DPO. Experiments across multiple architectures and preference datasets show that Gate-DPO consistently reduces squeezing and improves chosen-response likelihood. Mass-dynamics analysis further reveals healthier optimization behavior, with improved preferred responses and reduced suppression of the overall distribution. Notably, smaller gated models can exhibit stronger chosen-response improvements than larger ungated models, suggesting that controlling gradient dynamics, rather than scale alone, is key to stable and efficient alignment.
匹配关键词: SFT
---

[ACADEMIC - ARXIV]
标题: Reference-Sampled Boltzmann Projection for KL-Regularized RLVR: Target-Matched Weighted SFT, Finite One-Shot Gaps, and Policy Mirror Descent
作者: Yao Shu, Chenxing Wei, Hongbin Lin, Shuang Qiu, Hui Xiong
链接: https://arxiv.org/abs/2605.02469v1
完整摘要: Online reinforcement learning with verifiable rewards (RLVR) turns checkable outcomes into a scalable training signal, but it keeps rollout generation, verifier scoring, and reference-policy evaluations on the optimization path. Static weighted supervised fine-tuning (SFT) on precomputed rollouts seems to remove this bottleneck, yet a weighted likelihood is not specified by rewards alone: its sampler and weights induce the policy being fit. This paper identifies the reference-sampled weighted-SFT objective whose induced policy equals the fixed-reference KL-regularized RLVR optimizer. The optimizer is the standard Boltzmann target policy, obtained by exponentially tilting the reference policy by verifier reward. Matching a weighted-SFT induced policy to this target forces density-ratio weights; in the reference-sampled subclass, this reduces uniquely, up to prompt scaling, to the prompt-normalized Boltzmann weight $\exp(r(x,y)/β)/Z(x)$. BOLT, a Boltzmann-Targeted SFT procedure, is the empirical estimator of this projection. The finite one-shot analysis separates the exact stored-support price $β\log(1/π^*(S_N\mid x))$ from partition estimation, effective-sample-size variance, generalization, optimization, and approximation errors. This decomposition explains why extra SFT epochs cannot repair missing reference-policy coverage and exposes the temperature--coverage--variance frontier. When coverage needs adaptive sampling, refreshed Boltzmann projections become KL policy mirror descent; finite inner solves enter as additive drift from the exact mirror step. Single-run Qwen experiments provide projection evidence for the target-matched weight, one-shot saturation, refreshed-sampler gains, and optimization-time savings, within the stated single-run scope.
匹配关键词: SFT
---

[ACADEMIC - ARXIV]
标题: MolmoAct2: Action Reasoning Models for Real-world Deployment
作者: Haoquan Fang, Jiafei Duan, Donovan Clay, Sam Wang, Shuo Liu, Weikai Huang, Xiang Fan, Wei-Chuan Tsai, Shirui Chen, Yi Ru Wang, Shanli Xing, Jaemin Cho, Jae Sung Park, Ainaz Eftekhar, Peter Sushko, Karen Farley, Angad Wadhwa, Cole Harrison, Winson Han, Ying-Chun Lee, Eli VanderBilt, Rose Hendrix, Suveen Ellawela, Lucas Ngoo, Joyce Chai, Zhongzheng Ren, Ali Farhadi, Dieter Fox, Ranjay Krishna
链接: https://arxiv.org/abs/2605.02881v1
完整摘要: Vision-Language-Action (VLA) models aim to provide a single generalist controller for robots, but today's systems fall short on the criteria that matter for real-world deployment. Frontier models are closed, open-weight alternatives are tied to expensive hardware, reasoning-augmented policies pay prohibitive latency for their grounding, and fine-tuned success rates remain below the threshold for dependable use. We present MolmoAct2, a fully open action reasoning model built for practical deployment, advancing its predecessor along five axes. We introduce MolmoER, a VLM backbone specialized for spatial and embodied reasoning, trained on a 3.3M-sample corpus with a specialize-then-rehearse recipe. We release three new datasets spanning low-to-medium cost platforms, including MolmoAct2-BimanualYAM, 720 hours of teleoperated bimanual trajectories that constitute the largest open bimanual dataset to date, together with quality-filtered Franka (DROID) and SO100/101 subsets. We provide OpenFAST, an open-weight, open-data action tokenizer trained on millions of trajectories across five embodiments. We redesign the architecture to graft a flow-matching continuous-action expert onto a discrete-token VLM via per-layer KV-cache conditioning. Finally, we propose MolmoThink, an adaptive-depth reasoning variant that re-predicts depth tokens only for scene regions that change between timesteps, retaining geometric grounding at a fraction of prior latency. In the most extensive empirical study of any open VLA to date, spanning 7 simulation and real-world benchmarks, MolmoAct2 outperforms strong baselines including Pi-05, while MolmoER surpasses GPT-5 and Gemini Robotics ER-1.5 across 13 embodied-reasoning benchmarks. We release model weights, training code, and complete training data. Project page: https://allenai.org/blog/molmoact2
匹配关键词: instruction tuning
---

[ACADEMIC - ARXIV]
标题: Standing on the Shoulders of Giants: Stabilized Knowledge Distillation for Cross--Language Code Clone Detection
作者: Mohamad Khajezade, Fatemeh H. Fard, Mohamed Sami Shehata
链接: https://arxiv.org/abs/2605.02860v1
完整摘要: Cross-language code clone detection (X-CCD) is challenging because semantically equivalent programs written in different languages often share little surface similarity. Although large language models (LLMs) have shown promise for semantic clone detection, their use as black-box systems raises concerns about cost, reproducibility, privacy, and unreliable output formatting. In particular, compact open-source models often struggle to follow reasoning-oriented prompts and to produce outputs that can be consistently mapped to binary clone labels. To address these limitations, we propose a knowledge distillation framework that transfers reasoning capabilities from DeepSeek-R1 into compact open-source student models for X-CCD. Using cross-language code pairs derived from Project CodeNet, we construct reasoning-oriented synthetic training data and fine-tune Phi3 and Qwen-Coder with LoRA adapters. We further introduce response stabilization methods, including forced conclusion prompting, a binary classification head, and a contrastive classification head, and evaluate model behavior using both predictive metrics and response rate. Experiments on Python--Java, Rust--Java, Rust--Python, and Rust--Ruby show that knowledge distillation consistently improves the reliability of compact models and often improves predictive performance, especially under distribution shift. In addition, classification-head variants substantially reduce inference time compared to generation-based inference. Overall, our results show that reasoning-oriented distillation combined with response stabilization makes compact open-source models more practical and reliable for X-CCD detection.
匹配关键词: instruction tuning
---

[ACADEMIC - ARXIV]
标题: VideoNet: A Large-Scale Dataset for Domain-Specific Action Recognition
作者: Tanush Yadav, Mohammadreza Salehi, Jae Sung Park, Vivek Ramanujan, Hannaneh Hajishirzi, Yejin Choi, Ali Farhadi, Rohun Tripathi, Ranjay Krishna
链接: https://arxiv.org/abs/2605.02834v1
完整摘要: Videos are unique in their ability to capture actions which transcend multiple frames. Accordingly, for many years action recognition was the quintessential task for video understanding. Unfortunately, due to a lack of sufficiently diverse and challenging data, modern vision-language models (VLMs) are no longer evaluated on their action recognition capabilities. To revitalize action recognition in the era of VLMs, we advocate for a returned focus on domain-specific actions. To this end, we introduce VideoNet, a domain-specific action recognition benchmark covering 1,000 distinct actions from 37 domains. We begin with a multiple-choice evaluation setting, where the difference between closed and open models is stark: Gemini 3.1 Pro attains 69.9% accuracy while Qwen3-VL-8B gets a mere 45.0%. To understand why VLMs struggle on VideoNet, we relax the questions into a binary setting, where random chance is 50%. Still, Qwen achieves only 59.2% accuracy. Further relaxing the evaluation setup, we provide $k\in\{1,2,3\}$ in-context examples of the action. Some models excel in the few-shot setting, while others falter; Qwen improves $+7.0\%$, while Gemini declines $-4.8\%$. Notably, these gains fall short of the $+13.6\%$ improvement in non-expert humans when given few-shot examples. Finding that VLMs struggle to fully exploit in-context examples, we shift from test-time improvements to the training side. We collect the first large-scale training dataset for domain-specific actions, totaling nearly 500k video question-answer pairs. Fine-tuning a Molmo2-4B model on our data, we surpass all open-weight 8B models on the VideoNet benchmark.
匹配关键词: instruction tuning
---

[ACADEMIC - ARXIV]
标题: Compress Then Adapt? No, Do It Together via Task-aware Union of Subspaces
作者: Jingze Ge, Yun Liu, Xue Geng, Wanqi Dong, Wang Zhe Mark, Min Wu, Xulei Yang
链接: https://arxiv.org/abs/2605.02829v1
完整摘要: Adapting large pretrained models to diverse tasks is now routine, yet the two dominant strategies of parameter-efficient fine-tuning (PEFT) and low-rank compression are typically composed in sequence. This decoupled practice first compresses and then fine-tunes adapters, potentially misaligning the compressed subspace with downstream objectives and squandering a global parameter budget. To overcome this limitation, we introduce JACTUS (Joint Adaptation and Compression with a Task-aware Union of Subspaces), a single framework that unifies compression and adaptation. From a small calibration set, JACTUS estimates input and pre-activation gradient covariances, forms their orthogonal union with the pretrained weight subspace, performs a projected low-rank approximation inside this union, allocates rank globally by marginal gain per parameter, and trains only a compact core matrix. This explicitly mitigates the potential misalignment between the compressed subspace and downstream objectives by coupling the directions preserved for compression with those required for adaptation, yielding a deployable low-rank model that avoids retaining full frozen weights while enabling fast and robust tuning. On vision, JACTUS attains an average 89.2% accuracy on ViT-Base across eight datasets at 80% retained parameters, surpassing strong 100% PEFT baselines (e.g., DoRA 87.9%). On language, JACTUS achieves an 80.9% average on Llama2-7B commonsense QA at the same 80% retained-parameter budget, outperforming 100% PEFT (e.g., DoRA 79.7%) and exceeding prior compress-then-finetune pipelines under the same ratained-parameter budget. We will release code.
匹配关键词: instruction tuning
---

[ACADEMIC - ARXIV]
标题: LiDAR Teach, Radar Repeat: Robust Cross-Modal Navigation in Degenerate and Varying Environments
作者: Renxiang Xiao, Yichen Chen, Yuanfan Zhang, Qianyi Shao, Yushuai Chen, Yuxuan Han, Yunjiang Lou, Liang Hu
链接: https://arxiv.org/abs/2605.02809v1
完整摘要: Long-term autonomy requires robust navigation in environments subject to dynamic and static changes, as well as adverse weather conditions. Teach-and-Repeat (T\&R) navigation offers a reliable and cost-effective solution by avoiding the need for consistent global mapping; however, existing T\&R systems lack a systematic solution to tackle various environmental variations such as weather degradation, ephemeral dynamics, and structural changes. This work proposes LTR$^2$, the first cross-modal, cross-platform LiDAR-Teach-and-Radar-Repeat system that systematically addresses these challenges. LTR$^2$ leverages LiDAR during the teaching phase to capture precise structural information under normal conditions and utilizes 4D millimeter-wave radar during the repeating phase for robust operation under environmental degradations. To align sparse and noisy forward-looking 4D radar with dense and accurate omnidirectional 3D LiDAR data, we introduce a Cross-Modal Registration (CMR) network that jointly exploits Doppler-based motion priors and the physical laws governing LiDAR intensity and radar power density. Furthermore, we propose an adaptive fine-tuning strategy that incrementally updates the CMR network based on localization errors, enabling long-term adaptability to static environmental changes without ground-truth labels. We demonstrate that the proposed CMR network achieves state-of-the-art cross-modal registration performance on the open-access dataset. Then we validate LTR$^2$ across three robot platforms over a large-scale, long-term deployment (40+ km over 6 months), including challenging conditions such as nighttime smoke. Experimental results and ablation studies demonstrate centimeter-level accuracy and strong robustness against diverse environmental disturbances, significantly outperforming existing approaches.
匹配关键词: instruction tuning
---

[ACADEMIC - ARXIV]
标题: From Sensors to Insight: Rapid, Edge-to-Core Application Development for Sensor-Driven Applications
作者: Komal Thareja, Anirban Mandal, Ewa Deelman
链接: https://arxiv.org/abs/2605.02859v1
完整摘要: Scientists increasingly rely on sensor-based data, yet transforming raw streams into insights across the edge-to-cloud continuum remains difficult. Provisioning heterogeneous infrastructure and managing execution on emerging platforms like Data Processing Units typically requires cross-domain expertise, creating significant barriers to rapid prototyping. This paper introduces an experience-driven methodology for the rapid development of sensor-driven applications. By combining pattern-based workflow engineering with AI-assisted development-implemented via Pegasus on the FABRIC testbed - we utilize an existing Orcasound hydrophone workflow as a reusable template. We introduce a pattern-based engineering methodology to generate and refine workflows for air quality, earthquake, and soil moisture monitoring. Furthermore, we show how these abstract structures are extended to edge resources through modular configuration and placement. Our evaluation focuses on user productivity and practical lessons rather than peak performance. Through these case studies, we illustrate how AI-assisted, pattern-based development lowers the entry barrier for non-experts and enables iterative exploration of sensor-driven applications across distributed infrastructures.
匹配关键词: AI scientist
---

[ACADEMIC - ARXIV]
标题: (POSTER) From Sensors to Insight: Rapid, Edge-to-Core Application Development for Sensor-Driven Applications
作者: Komal Thareja, Anirban Mandal, Ewa Deelman
链接: https://arxiv.org/abs/2605.02844v1
完整摘要: Scientists increasingly rely on sensor-based data; however transforming raw streams into insights across the edge-to-cloud continuum remains difficult due to the breadth of expertise required to coordinate the necessary data and computation flow. This paper introduces a pattern-based, AI-assisted methodology for rapid development of sensor-driven applications. Using Pegasus workflows executing on the FABRIC testbed, we demonstrate a 5-step development loop that shifts workflow construction and deployment from code-first to intent-first design. Starting from an existing Orcasound hydrophone workflow as a reusable template, we generate and refine workflows for air quality, earthquake, and soil moisture monitoring applications. We further show how these workflows extend to edge resources-including BlueField-3 DPUs and Raspberry Pis-through configuration and placement rather than workflow redesign. Our evaluation, from the perspective of a novice Pegasus user, shows that AI-assisted pattern reuse compresses multi-stage workflow development to 1-1.5 days per workflow while preserving the rigor and portability of workflow-based execution.
匹配关键词: AI scientist
---

[ACADEMIC - ARXIV]
标题: HAAS: A Policy-Aware Framework for Adaptive Task Allocation Between Humans and Artificial Intelligence Systems
作者: Vicente Pelechanoa, Antoni Mestre, Manoli Albert, Miriam Gil
链接: https://arxiv.org/abs/2605.02832v1
完整摘要: Deciding how to distribute work between humans and AI systems is a central challenge in organisational design. Most approaches treat this as a binary choice, yet the operational reality is richer: humans and AI routinely share tasks or take complementary roles depending on context, fatigue, and the stakes involved. Governing that distribution -- balancing efficiency, oversight, and human capability -- remains an open problem. This paper presents Human-AI Adaptive Symbiosis (HAAS), an implemented framework for adaptive task allocation in software engineering and manufacturing. HAAS combines two coupled components: a rule-based expert system that enforces governance constraints before any learning occurs, and a contextual-bandit learner that selects among feasible collaboration modes from outcome feedback. Task-agent fit is represented through five auditable cognitive dimensions and a five-mode autonomy spectrum -- from human-only to fully autonomous -- embedded in a reproducible benchmark spanning both domains. Three empirical findings emerge. First, governance is not a binary switch but a tunable design variable: tighter constraints predictably convert autonomous AI assignments into supervised collaborations, with domain-specific costs and benefits. Second, in manufacturing, stronger governance can improve operational performance and reduce fatigue simultaneously -- a workload-buffering effect that contradicts the usual framing of governance as pure overhead. Third, no single governance setting dominates across all contexts; moderate governance becomes increasingly competitive as the learner accumulates experience within the governed action space. Together, these findings position HAAS as a pre-deployment workbench for comparing and inspecting human--AI allocation policies before organisational commitment.
匹配关键词: AI scientist
---

[ACADEMIC - ARXIV]
标题: AIs and Humans with Agency
作者: David Mumford
链接: https://arxiv.org/abs/2605.02810v1
完整摘要: This paper compares agency in humans with potential agency in AI programs. Human agency takes many years to develop, as the frontal lobe is activated. Early attempts to endow LLMs agency have met serious obstacles. Progress requires a new architecture where actions and plans are formulated jointly with the human actors in each real world setting.
匹配关键词: AI scientist
---

[ACADEMIC - ARXIV]
标题: Adaptive Interpolation-Synthesis for Motion In-Betweening on Keyframe-Based Animation
作者: Anton Raël, Julien Boucher, Antoine Lhermitte
链接: https://arxiv.org/abs/2605.02742v1
完整摘要: Motion in-betweening is one of the most artistically demanding and time consuming stages of 3D animation, where the expressivity and rhythm of motion are defined. The level of creative control it requires makes it a major production bottleneck, underscoring the need for intelligent tools that assist animators in this process. Although recent deep learning approaches have achieved strong results in motion synthesis and in-betweening, they assume data characteristics, motion styles, and problem formulations that diverge from professional animation workflows. To bridge this gap, we propose a method explicitly aligned with the constraints of motion in-betweening for keyframe-based animation in production environments. At its core, the Adaptive Interpolation-Synthesis (AIS) layer mirrors the animator's creative process by dynamically balancing learned interpolation and direct pose synthesis. In addition, a domain-based input keypose schedule reflects the distribution of production data, improving stylistic consistency and alignment between training and real-world usage. Our method achieves state-of-the-art performance on production data; when integrated into Autodesk Maya, it enables animators to complete in-betweening tasks with a 3.5x speedup.
匹配关键词: AI scientist
---

[ACADEMIC - ARXIV]
标题: Semantic Risk-Aware Heuristic Planning for Robotic Navigation in Dynamic Environments: An LLM-Inspired Approach
作者: Hamza Ahmed Durrani, Rafay Suleman Durrani
链接: https://arxiv.org/abs/2605.02862v1
完整摘要: The integration of Large Language Model (LLM) reasoning principles into classical robot path planning represents a rapidly emerging research direction. In this paper, we propose a Semantic Risk-Aware Heuristic (SRAH) planner that encodes LLM-inspired cost functions penalising geometrically cluttered or high-risk zones into an A$^*$ search framework, augmented with closed-loop replanning upon dynamic obstacle detection. We evaluate SRAH against two established baselines Breadth-First Search (BFS) with replanning and a Greedy heuristic without replanning across 200 randomised trials in a $15{\times}15$ grid-world with 20\% static obstacle density and stochastic dynamic obstacles. SRAH achieves a task success rate of 62.0\%, outperforming BFS (56.5\%) by 9.7\% relative improvement and Greedy (4.0\%) by a large margin. We further analyse the trade-off between planning overhead, path efficiency, and failure-recovery count, and demonstrate via an obstacle-density ablation that semantic cost shaping consistently improves navigation across environments of varying difficulty. Our results suggest that even lightweight, LLM-inspired heuristics provide measurable safety and robustness gains for autonomous robot navigation.
匹配关键词: automated research
---

[ACADEMIC - ARXIV]
标题: Mitigating Misalignment Contagion by Steering with Implicit Traits
作者: Maria Chang, Ronny Luss, Miao Lui, Keerthiram Murugesan, Karthikeyan Ramamurthy, Djallel Bouneffouf
链接: https://arxiv.org/abs/2605.02751v1
完整摘要: Language models (LMs) are increasingly used in high-stakes, multi-agent settings, where following instructions and maintaining value alignment are critical. Most alignment research focuses on interactions between a single LM and a single user, failing to address the risk of misaligned behavior spreading between multiple LMs in multi-turn interactions. We find evidence of this phenomenon, which we call misalignment contagion, across multiple LMs as they engage multi-turn conversational social dilemma games. Specifically, we find that LMs become more anti-social after gameplay and that this effect is intensified when other players are steered to act maliciously. We explore different steering techniques to mitigate such misalignment contagion and find that reinforcing an LM's system prompt is insufficient and often harmful. Instead, we propose steering with implicit traits: a technique that intermittently injects system prompts with statements that reinforce an LMs initial traits and is more effective than system prompt repetition at keeping models in line with their initial pro-social behaviors. Importantly, this method does not require access to model parameters or internal model states, making it suitable for increasingly common use cases where complex multi-agent workflows are being designed with black box models.
匹配关键词: automated research
---

[ACADEMIC - ARXIV]
标题: AI-Generated Smells: An Analysis of Code and Architecture in LLM and Agent-Driven Development
作者: Yuecai Zhu, Nikolaos Tsantalis, Peter C. Rigby
链接: https://arxiv.org/abs/2605.02741v1
完整摘要: The promise of Large Language Models in automated software engineering is often measured by functional correctness, overlooking the critical issue of long term maintainability. This paper presents a systematic audit of technical debt in AI-generated software, revealing that AI does not eliminate flaws but rather introduces a distinct machine signature of defects. Our multi-scale analysis, spanning single-file algorithmic tasks and complex, agent generated systems, identifies a fundamental Reasoning-Complexity Trade-off: as models become more capable, they generate increasingly bloated and coupled code. This architectural decay is so pronounced that we establish a Volume-Quality Inverse Law, where code volume is a near perfect predictor of structural degradation. Crucially, we demonstrate that neither functional correctness nor detailed prompting mitigates this decay. These findings challenge the current paradigm of prompt-driven generation, reframing the central problem of AI-based software engineering from one of code generation to one of architectural complexity management. We conclude that future progress depends on equipping agents with explicit architectural foresight to ensure the software they build is not just functional, but also maintainable.
匹配关键词: automated research
---

[ACADEMIC - ARXIV]
标题: AI and Open-data Driven Scalable Solar Power Profiling
作者: Shiliang Zhang, Sabita Maharjan, Damla Turgut
链接: https://arxiv.org/abs/2605.02738v1
完整摘要: Solar photovoltaic (PV) deployment is expanding rapidly, yet detailed, up-to-date information on the spatial distribution and capacity of rooftop PV remains limited. This paper presents an open, scalable framework for detecting solar panels from open data and generating city-level solar power profiles. We leverage foundation vision AI models to detect solar panel geometries from open-source satellite imagery. This avoids manual data labeling and case-specific model training while maintaining robustness across heterogeneous imagery. Detected solar panels are converted into georeferenced polygons, yielding spatially explicit and incrementally extensible inventories. By integrating open weather data, we translate panel footprints into regional solar power profiles. The framework reduces dependency on proprietary imagery, manual labeling, and closed-source models, and offers a transparent and scalable approach for solar planning and analysis. We released the data and an API resulted from this work. For any user-specified building location, our API retrieves aerial imagery, detects rooftop solar panels, and returns georeferenced polygons. This empowers researchers and developers to scan user-defined areas to build solar panel maps and associated solar production profiles, thus facilitating advanced analysis like distributed solar production integration, local power flow optimization, energy tariff design, and infrastructure planning.
匹配关键词: automated research
---

[ACADEMIC - ARXIV]
标题: SIAM: Head and Brain MRI Segmentation from Few High-Quality Templates via Synthetic Training
作者: Romain Valabregue, Ines Khemir, Eric Badinet, François Rousseau, Guillaume Auzias, Reuben Dorent
链接: https://arxiv.org/abs/2605.02737v1
完整摘要: Synthetic training has recently advanced brain MRI segmentation by enabling contrast-agnostic models trained entirely on generated data. However, most existing approaches rely on hundreds of automatically labeled templates, introducing systematic biases and limiting their flexibility to incorporate new anatomical structures. We present the Segment It All Model (SIAM), a 3D whole-head segmentation framework for 16 anatomical structures, trained using only six high-quality, manually annotated templates. SIAM extends domain randomization to both intensity and shape domains: synthetic image generation ensures contrast variability, while high-resolution spatial transformations model anatomical differences in cortical thickness and deep nuclei morphology. Unlike prior synthetic models, SIAM simultaneously segments brain as well as extra-cerebral tissues, including cerebrospinal fluid, vessels, dura mater, skull, and skin, enabling fully automated, preprocessing-free analysis. Evaluation across eight heterogeneous datasets (N=301), that include multiple contrasts (T1-weighted, T2-weighted, CT) and span a wide range of ages, demonstrates that SIAM matches or outperforms state-of-the-art methods for brain structures, in addition to extending automated segmentation to non-brain structures. The model also exhibits superior consistency across contrasts and repeated acquisitions, together with improved sensitivity to subtle gray matter atrophy. We openly release the model and the label templates at https://github.com/romainVala/SIAM.
匹配关键词: automated research
---

[ACADEMIC - ARXIV]
标题: Edge-Efficient Image Restoration: Transformer Distillation into State-Space Models
作者: Srinivas Soumitri Miriyala, Sowmya Vajrala, Sravanth Kodavanti, Vikram Nelvoy Rajendiran, Sharan Kumar Allur
链接: https://arxiv.org/abs/2605.02794v1
完整摘要: We propose a modular framework for hybrid image restoration that integrates transformer and state-space model (SSM) blocks with a focus on improving runtime efficiency on edge hardware. While transformers provide strong global modeling through self-attention, their attention kernels incur substantial latency on mobile devices, especially for high-resolution inputs. In contrast, SSMs such as Mamba offer lineartime sequence modeling with lower runtime overhead but may underperform on fine grained restoration tasks. To balance accuracy and efficiency, we train lightweight SSM blocks as feature-distilled surrogates of transformer blocks and use them to construct hybrid U-Net-style architectures. To automatically discover effective block combinations, we introduce Efficient Network Search (ENS), a multi-objective search strategy that selects task-specific hybrid configurations from pre-aligned components. ENS optimizes restoration quality while penalizing transformer usage, serving as a lightweight proxy for latency and enabling architecture discovery without repeated hardware profiling. On a Snapdragon 8 Elite CPU, the Restormer baseline requires 10119.52 ms for inference. In contrast, ENS-discovered hybrids significantly reduce runtime: ENS-Deblurring runs in 2973 ms (3.4x faster), ENS-Deraining in 5816 ms (1.74x faster), and ENS-Denoising in 8666 ms (1.17x faster), while maintaining competitive restoration quality.
匹配关键词: scientific discovery
---

[ACADEMIC - ARXIV]
标题: Fine-Grained Graph Generation through Latent Mixture Scheduling
作者: Nidhi Vakil, Hadi Amiri
链接: https://arxiv.org/abs/2605.02780v1
完整摘要: Structure aware graph generation aims to generate graphs that satisfy given topological properties. It has applications in domains such as drug discovery, social network modeling, and knowledge graph construction. Unlike existing methods that only provide coarse control over graph properties, we introduce a novel conditional variational autoencoder for fine-grained structural control in graph generation. The approach refines the decoder's latent space by dynamically aligning graph- and property-driven representations to improve both graph fidelity and control satisfaction. Specifically, the approach implements a mixture scheduler that progressively integrates graph and control priors. Experiments on five real-world datasets show the efficacy of the proposed model compared to recent baselines, achieving high generation quality while maintaining high controllability.
匹配关键词: scientific discovery
---

[ACADEMIC - ARXIV]
标题: TOC-SR: Task-Optimal Compact diffusion for Image Super Resolution
作者: Sowmya Vajrala, Akshay Bankar, Manjunath Arveti, Shreyas Pandith, Sravanth Kodavanti, Subhajit Sanyal, Amit Unde, Srinivas Soumitri Miriyala
链接: https://arxiv.org/abs/2605.02767v1
完整摘要: Diffusion models have recently demonstrated strong performance for image restoration tasks, including super-resolution. However, their large model size and iterative sampling procedures make them computationally expensive for practical deployment. In this work, we present TOC-SR, a framework for building efficient one-step super-resolution models by first discovering a compact diffusion backbone. Starting from a sixteen-channel latent diffusion model, we construct parameter-efficient surrogate blocks using feature-wise generative distillation and perform architecture discovery using epsilon-constrained Bayesian Optimization to minimize model complexity while preserving generative fidelity. The resulting compact diffusion backbone achieves a 6.6x reduction in parameters and a 2.8x reduction in GMACs compared to the expanded diffusion model. We then adapt this backbone for super-resolution and distill the diffusion process into a single-step generator. Experiments demonstrate that the proposed approach enables efficient super-resolution while maintaining strong reconstruction quality.
匹配关键词: scientific discovery
---

[ACADEMIC - ARXIV]
标题: Bolek: A Multimodal Language Model for Molecular Reasoning
作者: Frederic Grabowski, Jacek Szczerbiński, Maciej Jaśkowski, Kalina Jasińska-Kobus, Paweł Dąbrowski-Tumański, Tomasz Jetka, Bartosz Topolski
链接: https://arxiv.org/abs/2605.02745v1
完整摘要: Molecular property models increasingly support high-stakes drug-discovery decisions, but their outputs are often difficult to audit: classical predictors return scores without rationale, while language models can produce fluent explanations weakly grounded in the input molecule. We introduce Bolek, a compact multimodal language model that grounds natural-language reasoning in molecular structure by injecting a Morgan fingerprint embedding into an instruction-tuned text decoder. Bolek is fine-tuned on molecular alignment tasks, including molecule description, RDKit descriptor prediction, and substructure detection, and on downstream reasoning over 15 TDC binary classification tasks using synthetic chains-of-thought anchored in concrete molecular features. Across these tasks, Bolek outperforms its Qwen3-4B-Instruct base on all endpoints in yes/no mode and on 13 of 15 in chain-of-thought mode, raising mean ROC/PR AUC from 0.55 to 0.76. It also outperforms TxGemma-9B-Chat on 13 of 15 binary classification tasks despite being less than half its size. Bolek's explanations are more grounded than those of the baseline LLMs: it cites numerical descriptors 10-100x more often per chain-of-thought, and the cited values agree strongly with RDKit for key descriptors such as TPSA, MolLogP, and MolWt (Spearman rho = 0.87-0.91). Generalisation extends beyond the training panel: on 15 unseen TDC classification endpoints, Bolek matches TxGemma on five, and it produces non-trivial rank correlations on three held-out regression endpoints despite never seeing downstream regression during training. These results suggest that targeted modality injection and reasoning supervision tied to verifiable molecular features can yield compact, auditable molecular reasoning models.
匹配关键词: scientific discovery
---

[ACADEMIC - ARXIV]
标题: PubMed-Ophtha: An open resource for training ophthalmology vision-language models on scientific literature
作者: Verena Jasmin Hallitschke, Carsten Eickhoff, Philipp Berens
链接: https://arxiv.org/abs/2605.02720v1
完整摘要: Vision-language models hold considerable promise for ophthalmology, but their development depends on large-scale, high-quality image-text datasets that remain scarce. We present PubMed-Ophtha, a hierarchical dataset of 102,023 ophthalmological image-caption pairs extracted from 15,842 open-access articles in PubMed Central. Unlike existing datasets, figures are extracted directly from article PDFs at full resolution and decomposed into their constituent panels, panel identifiers, and individual images. Each image is annotated with its imaging modality -- color fundus photography, optical coherence tomography, retinal imaging, or other -- and a mark status indicating the presence of annotation marks such as arrows. Figure captions are split into panel-level subcaptions using a two-step LLM approach, achieving a mean average sentence BLEU score of 0.913 on human-annotated data. Panel and image detection models reach a mAP@0.50 of 0.909 and 0.892, respectively, and figure extraction achieves a median IoU of 0.997. To support reproducibility, we additionally release the human-annotated ground-truth data, all trained models, and the full dataset generation pipeline.
匹配关键词: scientific discovery
---

[ACADEMIC - ARXIV]
标题: AlbumFill: Album-Guided Reasoning and Retrieval for Personalized Image Completion
作者: Yu-Ju Tsai, Brian Price, Qing Liu, Luis Figueroa, Daniil Pakhomov, Zhihong Ding, Scott Cohen, Ming-Hsuan Yang
链接: https://arxiv.org/abs/2605.02892v1
完整摘要: Personalized image completion aims to restore occluded regions in personal photos while preserving identity and appearance. Existing methods either rely on generic inpainting models that often fail to maintain identity consistency, or assume that suitable reference images are explicitly provided. In practice, suitable references are often not explicitly provided, requiring the system to search for identity-consistent images within personal photo collections. We present AlbumFill, a training-free framework that retrieves identity-consistent references from personal albums for personalized completion. Given an occluded image and a personal album, a vision-language model infers missing semantic cues to guide composed image retrieval, and the retrieved references are used by reference-based completion models. To facilitate this task, we introduce a dataset containing 54K human-centric samples with associated album images. Experiments across multiple baselines demonstrate the difficulty of personalized completion and highlight the importance of identity-consistent reference retrieval. Project Page: https://liagm.github.io/AlbumFill/
匹配关键词: hypothesis generation
---

[ACADEMIC - ARXIV]
标题: Enhancing RL Generalizability in Robotics through SHAP Analysis of Algorithms and Hyperparameters
作者: Lingxiao Kong, Cong Yang, Oya Deniz Beyan, Zeyd Boukhers
链接: https://arxiv.org/abs/2605.02867v1
完整摘要: Despite significant advances in Reinforcement Learning (RL), model performance remains highly sensitive to algorithm and hyperparameter configurations, while generalization gaps across environments complicate real-world deployment. Although prior work has studied RL generalization, the relative contribution of specific configurations to the generalization gap has not been quantitatively decomposed and systematically leveraged for configuration selection. To address this limitation, we propose an explainable framework that evaluates RL performance across robotic environments using SHapley Additive exPlanations (SHAP) to quantify configuration impacts. We establish a theoretical foundation connecting Shapley values to generalizability, empirically analyze configuration impact patterns, and introduce SHAP-guided configuration selection to enhance generalization. Our results reveal distinct patterns across algorithms and hyperparameters, with consistent configuration impacts across diverse tasks and environments. By applying these insights to configuration selection, we achieve improved RL generalizability and provide actionable guidance for practitioners.
匹配关键词: hypothesis generation
---

[ACADEMIC - ARXIV]
标题: Pixel Perfect: Relational Image Quality Assessment with Spatially-Aware Distortions
作者: Fadeel Sher Khan, Long N. Le, Abhinau K. Venkataramanan, Seok-Jun Lee, Hamid R. Sheikh
链接: https://arxiv.org/abs/2605.02863v1
完整摘要: Traditional image quality assessment (IQA) methods rely on mean opinion scores (MOS), which are resource-intensive to collect and fail to provide interpretable, localized feedback on specific image distortions. We overcome these limitations by shifting from absolute quality prediction to a relational and directional assessment. Our approach utilizes a self-supervised synthetic distortion engine to generate training data, eliminating the need for manual annotation. A distortion prediction network is trained with an anti-symmetric objective to produce spatially-aware, disentangled maps that identify the type, intensity, and direction of distortions relative to a reference image. Subsequently, a scoring network is trained via contrastive learning on ordinally ranked image sets to predict a relational quality score. Our method provides a more granular and interpretable approach to IQA for the targeted optimization of image processing algorithms without requiring any human-labeled quality scores.
匹配关键词: hypothesis generation
---

[ACADEMIC - ARXIV]
标题: Standing on the Shoulders of Giants: Stabilized Knowledge Distillation for Cross--Language Code Clone Detection
作者: Mohamad Khajezade, Fatemeh H. Fard, Mohamed Sami Shehata
链接: https://arxiv.org/abs/2605.02860v1
完整摘要: Cross-language code clone detection (X-CCD) is challenging because semantically equivalent programs written in different languages often share little surface similarity. Although large language models (LLMs) have shown promise for semantic clone detection, their use as black-box systems raises concerns about cost, reproducibility, privacy, and unreliable output formatting. In particular, compact open-source models often struggle to follow reasoning-oriented prompts and to produce outputs that can be consistently mapped to binary clone labels. To address these limitations, we propose a knowledge distillation framework that transfers reasoning capabilities from DeepSeek-R1 into compact open-source student models for X-CCD. Using cross-language code pairs derived from Project CodeNet, we construct reasoning-oriented synthetic training data and fine-tune Phi3 and Qwen-Coder with LoRA adapters. We further introduce response stabilization methods, including forced conclusion prompting, a binary classification head, and a contrastive classification head, and evaluate model behavior using both predictive metrics and response rate. Experiments on Python--Java, Rust--Java, Rust--Python, and Rust--Ruby show that knowledge distillation consistently improves the reliability of compact models and often improves predictive performance, especially under distribution shift. In addition, classification-head variants substantially reduce inference time compared to generation-based inference. Overall, our results show that reasoning-oriented distillation combined with response stabilization makes compact open-source models more practical and reliable for X-CCD detection.
匹配关键词: hypothesis generation
---

[ACADEMIC - ARXIV]
标题: From Sensors to Insight: Rapid, Edge-to-Core Application Development for Sensor-Driven Applications
作者: Komal Thareja, Anirban Mandal, Ewa Deelman
链接: https://arxiv.org/abs/2605.02859v1
完整摘要: Scientists increasingly rely on sensor-based data, yet transforming raw streams into insights across the edge-to-cloud continuum remains difficult. Provisioning heterogeneous infrastructure and managing execution on emerging platforms like Data Processing Units typically requires cross-domain expertise, creating significant barriers to rapid prototyping. This paper introduces an experience-driven methodology for the rapid development of sensor-driven applications. By combining pattern-based workflow engineering with AI-assisted development-implemented via Pegasus on the FABRIC testbed - we utilize an existing Orcasound hydrophone workflow as a reusable template. We introduce a pattern-based engineering methodology to generate and refine workflows for air quality, earthquake, and soil moisture monitoring. Furthermore, we show how these abstract structures are extended to edge resources through modular configuration and placement. Our evaluation focuses on user productivity and practical lessons rather than peak performance. Through these case studies, we illustrate how AI-assisted, pattern-based development lowers the entry barrier for non-experts and enables iterative exploration of sensor-driven applications across distributed infrastructures.
匹配关键词: hypothesis generation
---

[ACADEMIC - ARXIV]
标题: AlbumFill: Album-Guided Reasoning and Retrieval for Personalized Image Completion
作者: Yu-Ju Tsai, Brian Price, Qing Liu, Luis Figueroa, Daniil Pakhomov, Zhihong Ding, Scott Cohen, Ming-Hsuan Yang
链接: https://arxiv.org/abs/2605.02892v1
完整摘要: Personalized image completion aims to restore occluded regions in personal photos while preserving identity and appearance. Existing methods either rely on generic inpainting models that often fail to maintain identity consistency, or assume that suitable reference images are explicitly provided. In practice, suitable references are often not explicitly provided, requiring the system to search for identity-consistent images within personal photo collections. We present AlbumFill, a training-free framework that retrieves identity-consistent references from personal albums for personalized completion. Given an occluded image and a personal album, a vision-language model infers missing semantic cues to guide composed image retrieval, and the retrieved references are used by reference-based completion models. To facilitate this task, we introduce a dataset containing 54K human-centric samples with associated album images. Experiments across multiple baselines demonstrate the difficulty of personalized completion and highlight the importance of identity-consistent reference retrieval. Project Page: https://liagm.github.io/AlbumFill/
匹配关键词: autonomous experiment
---

[ACADEMIC - ARXIV]
标题: Multi-fidelity surrogates for mechanics of composites: from co-kriging to multi-fidelity neural networks
作者: Haizhou Wen, Elham Kiyani, Gang Li, Srikanth Pilla, George Em Karniadakis, Zhen Li
链接: https://arxiv.org/abs/2605.02871v1
完整摘要: Composite materials exhibit strongly hierarchical and anisotropic properties governed by coupled mechanisms spanning constituents, plies, laminates, structures, and manufacturing history. This intrinsic complexity makes predictive modeling of composites expensive, because repeated experiments and high-fidelity simulations are needed to cover large design spaces of material, structure, and manufacturing. Multi-fidelity surrogate modeling addresses this challenge by combining abundant, less expensive data with limited high-accuracy data to recover reliable high-fidelity predictions. This review presents a structured overview of multi-fidelity modeling for composite mechanics, covering Gaussian-process or Kriging-based methods, including co-Kriging, coregionalization models, autoregressive formulations, nonlinear autoregressive Gaussian processes, multi-fidelity deep Gaussian processes, and multi-fidelity neural networks. Their distinctions are examined in terms of cross-fidelity correlation, discrepancy representation, uncertainty quantification, and scalability. Selected examples of their applications to composites are introduced according to the roles that multi-fidelity surrogates play in engineering problems, including forward prediction for rapid exploration of material design spaces, inverse optimization for composite parameter identification and design search under limited high-fidelity access, and workflow integration, where heterogeneous data sources, constraints, and validation requirements determine model utility. Open question discussions highlight recurring challenges specific to composites, such as regime-dependent fidelity gaps associated with nonlinear damage and manufacturing history, mismatches between simulations and experiments, and uncertainty propagation across multi-fidelity models.
匹配关键词: autonomous experiment
---

[ACADEMIC - ARXIV]
标题: Laplacian Frequency Interaction Network for Rural Thematic Road Extraction
作者: Baiyan Chen, Weixin Zhai
链接: https://arxiv.org/abs/2605.02866v1
完整摘要: Rural thematic road network construction aims to extract topological road structures from movement trajectory images of agricultural machinery. However, this task faces challenges where downsampling methods commonly used in existing studies tend to blur the sparse high-frequency road structures, and the heavy noise from dense field operations often leads to fragmented or redundant topologies in the extracted networks. To address these challenges, we propose LFINet, a Laplacian Frequency Interaction Network. The network begins with a Laplacian Multi-scale Separator (LMS) to decouple the image into low-frequency semantic contexts and high-frequency structural details. These components are then processed by the Cross-Frequency Interaction Block (CFIB) through a dual-pathway architecture in which a High-Frequency Block (HFB) refines local structures while a Spatial Transformer (ST) captures global semantics. Subsequently, a Frequency Gated Modulation (FGM) mechanism integrates the features from pathways by leveraging semantic contexts to calibrate the structural details. Finally, a Progressive Reconstruction Decoder iteratively fuses multi-scale features to ensure topological consistency. Experiments conducted on a real-world agricultural trajectories dataset from Henan Province, China, show that LFINet establishes a new state-of-the-art. Specifically, it achieves an F1-score of 92.54% and an IoU of 86.12%, surpassing the second-ranked method by 0.64% and 1.1%, respectively. This confirms its capability to effectively construct topological road networks from noisy and sparse field data.
匹配关键词: autonomous experiment
---

[ACADEMIC - ARXIV]
标题: Semantic Risk-Aware Heuristic Planning for Robotic Navigation in Dynamic Environments: An LLM-Inspired Approach
作者: Hamza Ahmed Durrani, Rafay Suleman Durrani
链接: https://arxiv.org/abs/2605.02862v1
完整摘要: The integration of Large Language Model (LLM) reasoning principles into classical robot path planning represents a rapidly emerging research direction. In this paper, we propose a Semantic Risk-Aware Heuristic (SRAH) planner that encodes LLM-inspired cost functions penalising geometrically cluttered or high-risk zones into an A$^*$ search framework, augmented with closed-loop replanning upon dynamic obstacle detection. We evaluate SRAH against two established baselines Breadth-First Search (BFS) with replanning and a Greedy heuristic without replanning across 200 randomised trials in a $15{\times}15$ grid-world with 20\% static obstacle density and stochastic dynamic obstacles. SRAH achieves a task success rate of 62.0\%, outperforming BFS (56.5\%) by 9.7\% relative improvement and Greedy (4.0\%) by a large margin. We further analyse the trade-off between planning overhead, path efficiency, and failure-recovery count, and demonstrate via an obstacle-density ablation that semantic cost shaping consistently improves navigation across environments of varying difficulty. Our results suggest that even lightweight, LLM-inspired heuristics provide measurable safety and robustness gains for autonomous robot navigation.
匹配关键词: autonomous experiment
---

[ACADEMIC - ARXIV]
标题: Standing on the Shoulders of Giants: Stabilized Knowledge Distillation for Cross--Language Code Clone Detection
作者: Mohamad Khajezade, Fatemeh H. Fard, Mohamed Sami Shehata
链接: https://arxiv.org/abs/2605.02860v1
完整摘要: Cross-language code clone detection (X-CCD) is challenging because semantically equivalent programs written in different languages often share little surface similarity. Although large language models (LLMs) have shown promise for semantic clone detection, their use as black-box systems raises concerns about cost, reproducibility, privacy, and unreliable output formatting. In particular, compact open-source models often struggle to follow reasoning-oriented prompts and to produce outputs that can be consistently mapped to binary clone labels. To address these limitations, we propose a knowledge distillation framework that transfers reasoning capabilities from DeepSeek-R1 into compact open-source student models for X-CCD. Using cross-language code pairs derived from Project CodeNet, we construct reasoning-oriented synthetic training data and fine-tune Phi3 and Qwen-Coder with LoRA adapters. We further introduce response stabilization methods, including forced conclusion prompting, a binary classification head, and a contrastive classification head, and evaluate model behavior using both predictive metrics and response rate. Experiments on Python--Java, Rust--Java, Rust--Python, and Rust--Ruby show that knowledge distillation consistently improves the reliability of compact models and often improves predictive performance, especially under distribution shift. In addition, classification-head variants substantially reduce inference time compared to generation-based inference. Overall, our results show that reasoning-oriented distillation combined with response stabilization makes compact open-source models more practical and reliable for X-CCD detection.
匹配关键词: autonomous experiment
---

[ACADEMIC - ARXIV]
标题: AI-Generated Smells: An Analysis of Code and Architecture in LLM and Agent-Driven Development
作者: Yuecai Zhu, Nikolaos Tsantalis, Peter C. Rigby
链接: https://arxiv.org/abs/2605.02741v1
完整摘要: The promise of Large Language Models in automated software engineering is often measured by functional correctness, overlooking the critical issue of long term maintainability. This paper presents a systematic audit of technical debt in AI-generated software, revealing that AI does not eliminate flaws but rather introduces a distinct machine signature of defects. Our multi-scale analysis, spanning single-file algorithmic tasks and complex, agent generated systems, identifies a fundamental Reasoning-Complexity Trade-off: as models become more capable, they generate increasingly bloated and coupled code. This architectural decay is so pronounced that we establish a Volume-Quality Inverse Law, where code volume is a near perfect predictor of structural degradation. Crucially, we demonstrate that neither functional correctness nor detailed prompting mitigates this decay. These findings challenge the current paradigm of prompt-driven generation, reframing the central problem of AI-based software engineering from one of code generation to one of architectural complexity management. We conclude that future progress depends on equipping agents with explicit architectural foresight to ensure the software they build is not just functional, but also maintainable.
匹配关键词: lab automation
---

[ACADEMIC - ARXIV]
标题: SIAM: Head and Brain MRI Segmentation from Few High-Quality Templates via Synthetic Training
作者: Romain Valabregue, Ines Khemir, Eric Badinet, François Rousseau, Guillaume Auzias, Reuben Dorent
链接: https://arxiv.org/abs/2605.02737v1
完整摘要: Synthetic training has recently advanced brain MRI segmentation by enabling contrast-agnostic models trained entirely on generated data. However, most existing approaches rely on hundreds of automatically labeled templates, introducing systematic biases and limiting their flexibility to incorporate new anatomical structures. We present the Segment It All Model (SIAM), a 3D whole-head segmentation framework for 16 anatomical structures, trained using only six high-quality, manually annotated templates. SIAM extends domain randomization to both intensity and shape domains: synthetic image generation ensures contrast variability, while high-resolution spatial transformations model anatomical differences in cortical thickness and deep nuclei morphology. Unlike prior synthetic models, SIAM simultaneously segments brain as well as extra-cerebral tissues, including cerebrospinal fluid, vessels, dura mater, skull, and skin, enabling fully automated, preprocessing-free analysis. Evaluation across eight heterogeneous datasets (N=301), that include multiple contrasts (T1-weighted, T2-weighted, CT) and span a wide range of ages, demonstrates that SIAM matches or outperforms state-of-the-art methods for brain structures, in addition to extending automated segmentation to non-brain structures. The model also exhibits superior consistency across contrasts and repeated acquisitions, together with improved sensitivity to subtle gray matter atrophy. We openly release the model and the label templates at https://github.com/romainVala/SIAM.
匹配关键词: lab automation
---

[ACADEMIC - ARXIV]
标题: An Empirical Study of Agent Skills for Healthcare: Practice, Gaps, and Governance
作者: Gelei Xu, Ningzhi Tang, Xueyang Li, Toby Jia-Jun Li, Zhi Zheng, Wei Jin, Yiyu Shi
链接: https://arxiv.org/abs/2605.02709v1
完整摘要: Healthcare automation is shaped by local procedures and organizational constraints, so agent capabilities rarely transfer unchanged across settings. Agent skills, self-contained directories that package reusable procedures for AI agents, are emerging as a procedural layer for adapting healthcare agents across diverse healthcare settings. We present the first empirical analysis of healthcare agent skills, drawing on 557 healthcare-related skills filtered from 58,159 public skills on ClawHub and annotated along ten dimensions covering function, deployment context, autonomy, and safety. We find that public healthcare skills emphasize patient-facing workflow automation and monitoring rather than the diagnostic and treatment-oriented tasks foregrounded in healthcare-agent research; coverage of the healthcare lifecycle and specialized clinical inputs remains uneven; and general technical risk does not reliably capture clinical risk. These findings position healthcare skills as a procedural layer not yet addressed by current benchmarks and risk frameworks.
匹配关键词: lab automation
---

[ACADEMIC - ARXIV]
标题: Temporally Consistent Object 6D Pose Estimation for Robot Control
作者: Kateryna Zorina, Vojtech Priban, Mederic Fourmy, Josef Sivic, Vladimir Petrik
链接: https://arxiv.org/abs/2605.02708v1
完整摘要: Single-view RGB object pose estimators have reached a level of precision and efficiency that makes them good candidates for vision-based robot control. However, off-the-shelf methods lack temporal consistency and robustness that are mandatory for a stable feedback control. In this work, we develop a factor graph approach to enforce temporal consistency of the object pose estimates. In particular, the proposed approach: (i) incorporates object motion models, (ii) explicitly estimates the object pose measurement uncertainty, and (iii) integrates the above two components in an online optimization-based estimator. We demonstrate that with appropriate outlier rejection and smoothing using the proposed factor graph approach, we can significantly improve the results on standardized pose estimation benchmarks. We experimentally validate the stability of the proposed approach for a feedback-based robot control task in which the object is tracked by the camera attached to a torque controlled manipulator.
匹配关键词: lab automation
---

[ACADEMIC - ARXIV]
标题: Caliper-in-the-Loop: Black-Box Optimization for Hyperledger Fabric Performance Tuning
作者: Yash Madhwal, Arseny Bolotnikov, Mark Prikhno, Irina Lebedeva, Ivan Laishevskiy, Vladimir Gorgadze, Artem Barger, Yury Yanovich
链接: https://arxiv.org/abs/2605.02690v1
完整摘要: Hyperledger Fabric performance depends on many interacting configuration parameters, making manual tuning difficult. We study automated throughput tuning by treating benchmarking as a noisy black-box optimization problem and applying Bayesian optimization (BO) with dimensionality reduction (DR). We implement an end-to-end Caliper-in-the-loop pipeline that deploys candidate configurations, benchmarks them, and updates the optimizer from observed throughput. The search space, derived from Fabric configuration files, has 317 dimensions. In a cloud testbed, we evaluate 16 BO+DR variants and a random-search baseline. The best method, DYCORS-PCA, achieves a 12% TPS improvement relative to the first evaluated configuration, while MPI-REMBO achieves 9%. These results suggest that BO with DR is a practical approach for high-dimensional Hyperledger Fabric tuning, while also highlighting the role of measurement noise in interpreting gains.
匹配关键词: lab automation
---

[ACADEMIC - ARXIV]
标题: AlbumFill: Album-Guided Reasoning and Retrieval for Personalized Image Completion
作者: Yu-Ju Tsai, Brian Price, Qing Liu, Luis Figueroa, Daniil Pakhomov, Zhihong Ding, Scott Cohen, Ming-Hsuan Yang
链接: https://arxiv.org/abs/2605.02892v1
完整摘要: Personalized image completion aims to restore occluded regions in personal photos while preserving identity and appearance. Existing methods either rely on generic inpainting models that often fail to maintain identity consistency, or assume that suitable reference images are explicitly provided. In practice, suitable references are often not explicitly provided, requiring the system to search for identity-consistent images within personal photo collections. We present AlbumFill, a training-free framework that retrieves identity-consistent references from personal albums for personalized completion. Given an occluded image and a personal album, a vision-language model infers missing semantic cues to guide composed image retrieval, and the retrieved references are used by reference-based completion models. To facilitate this task, we introduce a dataset containing 54K human-centric samples with associated album images. Experiments across multiple baselines demonstrate the difficulty of personalized completion and highlight the importance of identity-consistent reference retrieval. Project Page: https://liagm.github.io/AlbumFill/
匹配关键词: AI for science
---

[ACADEMIC - ARXIV]
标题: SpecKV: Adaptive Speculative Decoding with Compression-Aware Gamma Selection
作者: Shikhar Shukla
链接: https://arxiv.org/abs/2605.02888v1
完整摘要: Speculative decoding accelerates large language model (LLM) inference by using a small draft model to propose candidate tokens that a larger target model verifies. A critical hyperparameter in this process is the speculation length~$γ$, which determines how many tokens the draft model proposes per step. Nearly all existing systems use a fixed~$γ$ (typically~4), yet empirical evidence suggests that the optimal value varies across task types and, crucially, depends on the compression level applied to the target model. In this paper, we present \textbf{SpecKV}, a lightweight adaptive controller that selects~$γ$ per speculation step using signals extracted from the draft model itself. We profile speculative decoding across 4~task categories, 4~speculation lengths, and 3~compression levels (FP16, INT8, NF4), collecting 5,112 step-level records with per-step acceptance rates, draft entropy, and draft confidence. We demonstrate that the optimal~$γ$ shifts across compression regimes and that draft model confidence and entropy are strong predictors of acceptance rate (correlation~$\approx 0.56$). SpecKV uses a small MLP trained on these signals to maximize expected tokens per speculation step, achieving a 56.0\% improvement over the fixed-$γ$=4 baseline with only 0.34\,ms overhead per decision ($<$0.5\% of step time). The improvement is statistically significant ($p < 0.001$, paired bootstrap test). We release all profiling data, trained models, and notebooks as open-source artifacts.
匹配关键词: AI for science
---

[ACADEMIC - ARXIV]
标题: Unsupervised Machine Learning for Detecting Structural Anomalies in European Regional Statistics
作者: Bogdan Oancea
链接: https://arxiv.org/abs/2605.02884v1
完整摘要: Ensuring the coherence of regional socio-economic statistics is a central task for national statistical institutes. Traditional validation tools, such as range edits, ratio checks, or univariate outlier detection, are effective for identifying extreme values in individual series but are less suited for detecting unusual combinations of indicators in high-dimensional settings. This paper proposes an unsupervised machine learning framework for identifying structurally atypical regional profiles within Europe using publicly available Eurostat data. We construct a cross-sectional dataset of NUTS2 regions (2022) covering four key indicators: GDP per capita in PPS, unemployment rate, tertiary educational attainment, and population density. We apply and compare five anomaly detection techniques, univariate z-scores, Mahalanobis distance, Isolation Forest, Local Outlier Factor, and One-Class SVM, and classify a region as a structural anomaly if it is flagged by at least three of the five methods. The findings show that machine learning methods identify a consistent set of regions whose multivariate profiles diverge substantially from the EU-wide pattern. These include both highly developed metropolitan economies (Brussels, Vienna, Berlin, Prague) and regions with persistent socio-economic disadvantages (Central and Western Slovakia, Northern Hungary, Castilla-La Mancha, Extremadura), as well as Istanbul, whose profile differs markedly from EU capital regions. Importantly, these anomalies do not necessarily signal data quality issues; rather, they reflect meaningful structural divergence that warrants analytical or policy attention. The proposed framework is fully reproducible, scalable, and compatible with existing validation workflows, offering a flexible tool for early detection of unusual regional configurations within the European Statistical System.
匹配关键词: AI for science
---

[ACADEMIC - ARXIV]
标题: MolmoAct2: Action Reasoning Models for Real-world Deployment
作者: Haoquan Fang, Jiafei Duan, Donovan Clay, Sam Wang, Shuo Liu, Weikai Huang, Xiang Fan, Wei-Chuan Tsai, Shirui Chen, Yi Ru Wang, Shanli Xing, Jaemin Cho, Jae Sung Park, Ainaz Eftekhar, Peter Sushko, Karen Farley, Angad Wadhwa, Cole Harrison, Winson Han, Ying-Chun Lee, Eli VanderBilt, Rose Hendrix, Suveen Ellawela, Lucas Ngoo, Joyce Chai, Zhongzheng Ren, Ali Farhadi, Dieter Fox, Ranjay Krishna
链接: https://arxiv.org/abs/2605.02881v1
完整摘要: Vision-Language-Action (VLA) models aim to provide a single generalist controller for robots, but today's systems fall short on the criteria that matter for real-world deployment. Frontier models are closed, open-weight alternatives are tied to expensive hardware, reasoning-augmented policies pay prohibitive latency for their grounding, and fine-tuned success rates remain below the threshold for dependable use. We present MolmoAct2, a fully open action reasoning model built for practical deployment, advancing its predecessor along five axes. We introduce MolmoER, a VLM backbone specialized for spatial and embodied reasoning, trained on a 3.3M-sample corpus with a specialize-then-rehearse recipe. We release three new datasets spanning low-to-medium cost platforms, including MolmoAct2-BimanualYAM, 720 hours of teleoperated bimanual trajectories that constitute the largest open bimanual dataset to date, together with quality-filtered Franka (DROID) and SO100/101 subsets. We provide OpenFAST, an open-weight, open-data action tokenizer trained on millions of trajectories across five embodiments. We redesign the architecture to graft a flow-matching continuous-action expert onto a discrete-token VLM via per-layer KV-cache conditioning. Finally, we propose MolmoThink, an adaptive-depth reasoning variant that re-predicts depth tokens only for scene regions that change between timesteps, retaining geometric grounding at a fraction of prior latency. In the most extensive empirical study of any open VLA to date, spanning 7 simulation and real-world benchmarks, MolmoAct2 outperforms strong baselines including Pi-05, while MolmoER surpasses GPT-5 and Gemini Robotics ER-1.5 across 13 embodied-reasoning benchmarks. We release model weights, training code, and complete training data. Project page: https://allenai.org/blog/molmoact2
匹配关键词: AI for science
---

[ACADEMIC - ARXIV]
标题: Multi-fidelity surrogates for mechanics of composites: from co-kriging to multi-fidelity neural networks
作者: Haizhou Wen, Elham Kiyani, Gang Li, Srikanth Pilla, George Em Karniadakis, Zhen Li
链接: https://arxiv.org/abs/2605.02871v1
完整摘要: Composite materials exhibit strongly hierarchical and anisotropic properties governed by coupled mechanisms spanning constituents, plies, laminates, structures, and manufacturing history. This intrinsic complexity makes predictive modeling of composites expensive, because repeated experiments and high-fidelity simulations are needed to cover large design spaces of material, structure, and manufacturing. Multi-fidelity surrogate modeling addresses this challenge by combining abundant, less expensive data with limited high-accuracy data to recover reliable high-fidelity predictions. This review presents a structured overview of multi-fidelity modeling for composite mechanics, covering Gaussian-process or Kriging-based methods, including co-Kriging, coregionalization models, autoregressive formulations, nonlinear autoregressive Gaussian processes, multi-fidelity deep Gaussian processes, and multi-fidelity neural networks. Their distinctions are examined in terms of cross-fidelity correlation, discrepancy representation, uncertainty quantification, and scalability. Selected examples of their applications to composites are introduced according to the roles that multi-fidelity surrogates play in engineering problems, including forward prediction for rapid exploration of material design spaces, inverse optimization for composite parameter identification and design search under limited high-fidelity access, and workflow integration, where heterogeneous data sources, constraints, and validation requirements determine model utility. Open question discussions highlight recurring challenges specific to composites, such as regime-dependent fidelity gaps associated with nonlinear damage and manufacturing history, mismatches between simulations and experiments, and uncertainty propagation across multi-fidelity models.
匹配关键词: AI for science
---

[ACADEMIC - ARXIV]
标题: Differentiable Kernel Ridge Regression for Deep Learning Pipelines
作者: Jean-Marc Mercier, Gabriele Santin
链接: https://arxiv.org/abs/2605.02313v1
完整摘要: Deep neural networks dominate modern machine learning, while alternative function approximators remain comparatively underexplored at scale. In this work, we revisit kernel methods as drop-in components for standard deep learning pipelines. We introduce \emph{Sparse Kernels} (SKs), a differentiable, localized, and lazy variant of kernel ridge regression (KRR) that defers training to inference time and reduces to the solution of small local systems. We integrate SKs into PyTorch as modular layers that preserve end-to-end trainability, and we show that they expose three distinct sets of parameters -- feature representations, target values, and evaluation points -- each of which can be fixed or learned. This decomposition broadens the design space available to practitioners, enabling, in particular, training-free transfer, nonlinear probing, and hybrid kernel-neural models. Across convolutional networks, vision transformers, and reinforcement learning, SK-based modules serve two complementary roles: in some settings, they match the performance of trained neural readouts with substantially less training; in others, they augment existing models and improve their performance when used as additional components. Our results suggest that kernel methods, once made scalable and differentiable, can be readily integrated with deep learning rather than treated as a separate paradigm.
匹配关键词: PyTorch
---

[ACADEMIC - ARXIV]
标题: Unifying Deep Stochastic Processes for Image Enhancement
作者: Wojciech Kozłowski, Radosław Kuczbański, Kamil Adamczewski, Karol Szczypkowski, Maciej Zięba
链接: https://arxiv.org/abs/2605.01568v1
完整摘要: Deep stochastic processes have recently become a central paradigm for image enhancement, with many methods explicitly conditioning the stochastic trajectory on the degraded input. However, the relationship between these conditional processes and standard diffusion models remains unclear. In this work, we introduce a unified perspective on stochastic image enhancement by classifying recent methods into three families of continuous-time processes: unconditional diffusion models, Ornstein-Uhlenbeck (OU) processes, and diffusion bridges. We show that all of these approaches arise from a common stochastic differential equation (SDE) formulation. This framework makes explicit that seemingly disparate methods differ primarily in their drift and diffusion terms, terminal distributions, and boundary conditions, while schedulers and samplers constitute orthogonal design choices. Leveraging this unification, we conduct a controlled empirical study across multiple image enhancement tasks using identical architectures and training protocols. Our results reveal no consistently dominant method; instead, we identify and disentangle the specific design choices that most strongly influence performance. Finally, we release ItoVision, a modular PyTorch library that implements the unified framework and enables rapid prototyping and fair comparison of stochastic image enhancement methods.
匹配关键词: PyTorch
---

[ACADEMIC - ARXIV]
标题: Enhancing Game Review Sentiment Classification on Steam Platform with Attention-Based BiLSTM
作者: Abit Ahmad Oktarian, Fadhil Fitra Wijaya, Dhafin Razaqa Luthfi, Luluk Muthoharoh, Ardika Satria, Martin Clinton Tosima Manullang
链接: https://arxiv.org/abs/2605.01315v1
完整摘要: This paper investigates sentiment classification of Steam game reviews using an attention-based Bidirectional Long Short-Term Memory (BiLSTM) model. Using a dataset of 50,000 reviews sampled from a larger Steam review corpus, the authors compare a traditional machine learning baseline based on TF-IDF and PyCaret AutoML with a deep learning approach implemented in PyTorch. The proposed BiLSTM+Attention model is trained with class-weighted cross-entropy to address class imbalance and achieves 83% accuracy and 85% weighted F1-score on the test set, with 90% recall for negative reviews. The paper also presents attention visualizations to show interpretability by highlighting sentiment-bearing words. The study concludes that the BiLSTM+Attention model is effective for analyzing user sentiment in Steam reviews and useful for helping developers understand player feedback.
匹配关键词: PyTorch
---

[ACADEMIC - ARXIV]
标题: VkSplat: High-Performance 3DGS Training in Vulkan Compute
作者: Jingxiang Chen, Mohamed Ibrahim, Yang Liu
链接: https://arxiv.org/abs/2605.00219v1
完整摘要: We present VkSplat, a high-performance, cross-vendor 3D Gaussian Splatting (3DGS) training pipeline implemented fully in Vulkan compute, addressing performance and compatibility limitation of existing training pipelines. With various optimizations, we achieve $3.3\times$ speed and $33\%$ VRAM reduction over CUDA+PyTorch baseline, maintaining quality, and demonstrating compatibility across GPU vendors. To the best of our knowledge, this is the first fully-Vulkan-based 3DGS training pipeline that achieves state-of-the-art performance. Code: \href{https://github.com/harry7557558/vksplat}{https://github.com/harry7557558/vksplat}
匹配关键词: PyTorch
---

[ACADEMIC - ARXIV]
标题: A Short Note on Batch-efficient Divide-and-Conquer Algorithm for EigenDecomposition
作者: Yue Song
链接: https://arxiv.org/abs/2604.27325v1
完整摘要: EigenDecomposition (ED) is at the heart of many computer vision algorithms and applications. One crucial bottleneck limiting its usage is the expensive computation cost, particularly for a mini-batch of matrices in deep neural networks. Our previous work proposed a dedicated QR-based ED algorithm for batched small matrices (dim${<}32$). This short paper targets the limitation and proposes a batch-efficient Divide-and-Conquer based ED algorithm for larger matrices. The numerical test shows that for a mini-batch of matrices whose dimensions are smaller than $64$, our method can be much faster than the Pytorch SVD function.
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
标题: AlbumFill: Album-Guided Reasoning and Retrieval for Personalized Image Completion
作者: Yu-Ju Tsai, Brian Price, Qing Liu, Luis Figueroa, Daniil Pakhomov, Zhihong Ding, Scott Cohen, Ming-Hsuan Yang
链接: https://arxiv.org/abs/2605.02892v1
完整摘要: Personalized image completion aims to restore occluded regions in personal photos while preserving identity and appearance. Existing methods either rely on generic inpainting models that often fail to maintain identity consistency, or assume that suitable reference images are explicitly provided. In practice, suitable references are often not explicitly provided, requiring the system to search for identity-consistent images within personal photo collections. We present AlbumFill, a training-free framework that retrieves identity-consistent references from personal albums for personalized completion. Given an occluded image and a personal album, a vision-language model infers missing semantic cues to guide composed image retrieval, and the retrieved references are used by reference-based completion models. To facilitate this task, we introduce a dataset containing 54K human-centric samples with associated album images. Experiments across multiple baselines demonstrate the difficulty of personalized completion and highlight the importance of identity-consistent reference retrieval. Project Page: https://liagm.github.io/AlbumFill/
匹配关键词: distributed training
---

[ACADEMIC - ARXIV]
标题: SpecKV: Adaptive Speculative Decoding with Compression-Aware Gamma Selection
作者: Shikhar Shukla
链接: https://arxiv.org/abs/2605.02888v1
完整摘要: Speculative decoding accelerates large language model (LLM) inference by using a small draft model to propose candidate tokens that a larger target model verifies. A critical hyperparameter in this process is the speculation length~$γ$, which determines how many tokens the draft model proposes per step. Nearly all existing systems use a fixed~$γ$ (typically~4), yet empirical evidence suggests that the optimal value varies across task types and, crucially, depends on the compression level applied to the target model. In this paper, we present \textbf{SpecKV}, a lightweight adaptive controller that selects~$γ$ per speculation step using signals extracted from the draft model itself. We profile speculative decoding across 4~task categories, 4~speculation lengths, and 3~compression levels (FP16, INT8, NF4), collecting 5,112 step-level records with per-step acceptance rates, draft entropy, and draft confidence. We demonstrate that the optimal~$γ$ shifts across compression regimes and that draft model confidence and entropy are strong predictors of acceptance rate (correlation~$\approx 0.56$). SpecKV uses a small MLP trained on these signals to maximize expected tokens per speculation step, achieving a 56.0\% improvement over the fixed-$γ$=4 baseline with only 0.34\,ms overhead per decision ($<$0.5\% of step time). The improvement is statistically significant ($p < 0.001$, paired bootstrap test). We release all profiling data, trained models, and notebooks as open-source artifacts.
匹配关键词: distributed training
---

[ACADEMIC - ARXIV]
标题: MolmoAct2: Action Reasoning Models for Real-world Deployment
作者: Haoquan Fang, Jiafei Duan, Donovan Clay, Sam Wang, Shuo Liu, Weikai Huang, Xiang Fan, Wei-Chuan Tsai, Shirui Chen, Yi Ru Wang, Shanli Xing, Jaemin Cho, Jae Sung Park, Ainaz Eftekhar, Peter Sushko, Karen Farley, Angad Wadhwa, Cole Harrison, Winson Han, Ying-Chun Lee, Eli VanderBilt, Rose Hendrix, Suveen Ellawela, Lucas Ngoo, Joyce Chai, Zhongzheng Ren, Ali Farhadi, Dieter Fox, Ranjay Krishna
链接: https://arxiv.org/abs/2605.02881v1
完整摘要: Vision-Language-Action (VLA) models aim to provide a single generalist controller for robots, but today's systems fall short on the criteria that matter for real-world deployment. Frontier models are closed, open-weight alternatives are tied to expensive hardware, reasoning-augmented policies pay prohibitive latency for their grounding, and fine-tuned success rates remain below the threshold for dependable use. We present MolmoAct2, a fully open action reasoning model built for practical deployment, advancing its predecessor along five axes. We introduce MolmoER, a VLM backbone specialized for spatial and embodied reasoning, trained on a 3.3M-sample corpus with a specialize-then-rehearse recipe. We release three new datasets spanning low-to-medium cost platforms, including MolmoAct2-BimanualYAM, 720 hours of teleoperated bimanual trajectories that constitute the largest open bimanual dataset to date, together with quality-filtered Franka (DROID) and SO100/101 subsets. We provide OpenFAST, an open-weight, open-data action tokenizer trained on millions of trajectories across five embodiments. We redesign the architecture to graft a flow-matching continuous-action expert onto a discrete-token VLM via per-layer KV-cache conditioning. Finally, we propose MolmoThink, an adaptive-depth reasoning variant that re-predicts depth tokens only for scene regions that change between timesteps, retaining geometric grounding at a fraction of prior latency. In the most extensive empirical study of any open VLA to date, spanning 7 simulation and real-world benchmarks, MolmoAct2 outperforms strong baselines including Pi-05, while MolmoER surpasses GPT-5 and Gemini Robotics ER-1.5 across 13 embodied-reasoning benchmarks. We release model weights, training code, and complete training data. Project page: https://allenai.org/blog/molmoact2
匹配关键词: distributed training
---

[ACADEMIC - ARXIV]
标题: Pixel Perfect: Relational Image Quality Assessment with Spatially-Aware Distortions
作者: Fadeel Sher Khan, Long N. Le, Abhinau K. Venkataramanan, Seok-Jun Lee, Hamid R. Sheikh
链接: https://arxiv.org/abs/2605.02863v1
完整摘要: Traditional image quality assessment (IQA) methods rely on mean opinion scores (MOS), which are resource-intensive to collect and fail to provide interpretable, localized feedback on specific image distortions. We overcome these limitations by shifting from absolute quality prediction to a relational and directional assessment. Our approach utilizes a self-supervised synthetic distortion engine to generate training data, eliminating the need for manual annotation. A distortion prediction network is trained with an anti-symmetric objective to produce spatially-aware, disentangled maps that identify the type, intensity, and direction of distortions relative to a reference image. Subsequently, a scoring network is trained via contrastive learning on ordinally ranked image sets to predict a relational quality score. Our method provides a more granular and interpretable approach to IQA for the targeted optimization of image processing algorithms without requiring any human-labeled quality scores.
匹配关键词: distributed training
---

[ACADEMIC - ARXIV]
标题: Standing on the Shoulders of Giants: Stabilized Knowledge Distillation for Cross--Language Code Clone Detection
作者: Mohamad Khajezade, Fatemeh H. Fard, Mohamed Sami Shehata
链接: https://arxiv.org/abs/2605.02860v1
完整摘要: Cross-language code clone detection (X-CCD) is challenging because semantically equivalent programs written in different languages often share little surface similarity. Although large language models (LLMs) have shown promise for semantic clone detection, their use as black-box systems raises concerns about cost, reproducibility, privacy, and unreliable output formatting. In particular, compact open-source models often struggle to follow reasoning-oriented prompts and to produce outputs that can be consistently mapped to binary clone labels. To address these limitations, we propose a knowledge distillation framework that transfers reasoning capabilities from DeepSeek-R1 into compact open-source student models for X-CCD. Using cross-language code pairs derived from Project CodeNet, we construct reasoning-oriented synthetic training data and fine-tune Phi3 and Qwen-Coder with LoRA adapters. We further introduce response stabilization methods, including forced conclusion prompting, a binary classification head, and a contrastive classification head, and evaluate model behavior using both predictive metrics and response rate. Experiments on Python--Java, Rust--Java, Rust--Python, and Rust--Ruby show that knowledge distillation consistently improves the reliability of compact models and often improves predictive performance, especially under distribution shift. In addition, classification-head variants substantially reduce inference time compared to generation-based inference. Overall, our results show that reasoning-oriented distillation combined with response stabilization makes compact open-source models more practical and reliable for X-CCD detection.
匹配关键词: distributed training
---

[ACADEMIC - ARXIV]
标题: SpecKV: Adaptive Speculative Decoding with Compression-Aware Gamma Selection
作者: Shikhar Shukla
链接: https://arxiv.org/abs/2605.02888v1
完整摘要: Speculative decoding accelerates large language model (LLM) inference by using a small draft model to propose candidate tokens that a larger target model verifies. A critical hyperparameter in this process is the speculation length~$γ$, which determines how many tokens the draft model proposes per step. Nearly all existing systems use a fixed~$γ$ (typically~4), yet empirical evidence suggests that the optimal value varies across task types and, crucially, depends on the compression level applied to the target model. In this paper, we present \textbf{SpecKV}, a lightweight adaptive controller that selects~$γ$ per speculation step using signals extracted from the draft model itself. We profile speculative decoding across 4~task categories, 4~speculation lengths, and 3~compression levels (FP16, INT8, NF4), collecting 5,112 step-level records with per-step acceptance rates, draft entropy, and draft confidence. We demonstrate that the optimal~$γ$ shifts across compression regimes and that draft model confidence and entropy are strong predictors of acceptance rate (correlation~$\approx 0.56$). SpecKV uses a small MLP trained on these signals to maximize expected tokens per speculation step, achieving a 56.0\% improvement over the fixed-$γ$=4 baseline with only 0.34\,ms overhead per decision ($<$0.5\% of step time). The improvement is statistically significant ($p < 0.001$, paired bootstrap test). We release all profiling data, trained models, and notebooks as open-source artifacts.
匹配关键词: GPU optimization
---

[ACADEMIC - ARXIV]
标题: Multi-fidelity surrogates for mechanics of composites: from co-kriging to multi-fidelity neural networks
作者: Haizhou Wen, Elham Kiyani, Gang Li, Srikanth Pilla, George Em Karniadakis, Zhen Li
链接: https://arxiv.org/abs/2605.02871v1
完整摘要: Composite materials exhibit strongly hierarchical and anisotropic properties governed by coupled mechanisms spanning constituents, plies, laminates, structures, and manufacturing history. This intrinsic complexity makes predictive modeling of composites expensive, because repeated experiments and high-fidelity simulations are needed to cover large design spaces of material, structure, and manufacturing. Multi-fidelity surrogate modeling addresses this challenge by combining abundant, less expensive data with limited high-accuracy data to recover reliable high-fidelity predictions. This review presents a structured overview of multi-fidelity modeling for composite mechanics, covering Gaussian-process or Kriging-based methods, including co-Kriging, coregionalization models, autoregressive formulations, nonlinear autoregressive Gaussian processes, multi-fidelity deep Gaussian processes, and multi-fidelity neural networks. Their distinctions are examined in terms of cross-fidelity correlation, discrepancy representation, uncertainty quantification, and scalability. Selected examples of their applications to composites are introduced according to the roles that multi-fidelity surrogates play in engineering problems, including forward prediction for rapid exploration of material design spaces, inverse optimization for composite parameter identification and design search under limited high-fidelity access, and workflow integration, where heterogeneous data sources, constraints, and validation requirements determine model utility. Open question discussions highlight recurring challenges specific to composites, such as regime-dependent fidelity gaps associated with nonlinear damage and manufacturing history, mismatches between simulations and experiments, and uncertainty propagation across multi-fidelity models.
匹配关键词: GPU optimization
---

[ACADEMIC - ARXIV]
标题: Pixel Perfect: Relational Image Quality Assessment with Spatially-Aware Distortions
作者: Fadeel Sher Khan, Long N. Le, Abhinau K. Venkataramanan, Seok-Jun Lee, Hamid R. Sheikh
链接: https://arxiv.org/abs/2605.02863v1
完整摘要: Traditional image quality assessment (IQA) methods rely on mean opinion scores (MOS), which are resource-intensive to collect and fail to provide interpretable, localized feedback on specific image distortions. We overcome these limitations by shifting from absolute quality prediction to a relational and directional assessment. Our approach utilizes a self-supervised synthetic distortion engine to generate training data, eliminating the need for manual annotation. A distortion prediction network is trained with an anti-symmetric objective to produce spatially-aware, disentangled maps that identify the type, intensity, and direction of distortions relative to a reference image. Subsequently, a scoring network is trained via contrastive learning on ordinally ranked image sets to predict a relational quality score. Our method provides a more granular and interpretable approach to IQA for the targeted optimization of image processing algorithms without requiring any human-labeled quality scores.
匹配关键词: GPU optimization
---

[ACADEMIC - ARXIV]
标题: Trust, but Verify: Peeling Low-Bit Transformer Networks for Training Monitoring
作者: Arian Eamaz, Farhang Yeganegi, Mojtaba Soltanalian
链接: https://arxiv.org/abs/2605.02853v1
完整摘要: Understanding whether deep neural networks are effectively optimized remains challenging, as training occurs in highly nonconvex landscapes and standard metrics provide limited visibility into layer-wise learning quality. This challenge is particularly acute for transformer-based language models, where training is expensive, models are often reused in frozen form, and poorly optimized layers can silently degrade performance. We propose a layer-wise peeling framework for monitoring training dynamics, in which each transformer layer is locally optimized against intermediate representations of the trained model. By constructing lightweight, layer-specific reference solutions and projecting layers onto multiple intermediate outputs via different permutations, we obtain achievable baselines that enable fine-grained diagnosis of under-optimized layers. Experiments on decoder-only transformer models show that these layer-wise reference bounds can match or even surpass the trained model at various stages of training, exposing inefficiencies that remain hidden in aggregate loss curves. We further demonstrate that this analysis remains effective under binarization and quantized settings, where training dynamics are particularly fragile. Across all numerical results, the proposed bounds consistently separate apparent convergence from effective optimality, highlighting optimization opportunities that are invisible when relying on training loss alone.
匹配关键词: GPU optimization
---

[ACADEMIC - ARXIV]
标题: A second-order method on the Stiefel manifold via Newton$\unicode{x2013}$Schulz
作者: Xinhui Xiong, Bin Gao, P. -A. Absil
链接: https://arxiv.org/abs/2605.02838v1
完整摘要: Retraction-free approaches offer attractive low-cost alternatives to Riemannian methods on the Stiefel manifold, but they are often first-order, which may limit the efficiency under high-accuracy requirements. To this end, we propose a second-order method landing on the Stiefel manifold without invoking retractions, which is proved to enjoy local quadratic (or superlinear for its inexact variant) convergence. The update consists of the sum of (i) a component tangent to the level set of the constraint-defining function that aims to reduce the objective and (ii) a component normal to the same level set that reduces the infeasibility. Specifically, we construct the normal component via Newton$\unicode{x2013}$Schulz, a fixed-point iteration for orthogonalization. Moreover, we establish a geometric connection between the Newton$\unicode{x2013}$Schulz iteration and Stiefel manifolds, in which Newton$\unicode{x2013}$Schulz moves along the normal space. For the tangent component, we formulate a modified Newton equation that incorporates Newton$\unicode{x2013}$Schulz. Numerical experiments on the orthogonal Procrustes problem, principal component analysis, and real-data independent component analysis illustrate that the proposed method performs better than the existing methods.
匹配关键词: GPU optimization
---

[ACADEMIC - ARXIV]
标题: Pixel Perfect: Relational Image Quality Assessment with Spatially-Aware Distortions
作者: Fadeel Sher Khan, Long N. Le, Abhinau K. Venkataramanan, Seok-Jun Lee, Hamid R. Sheikh
链接: https://arxiv.org/abs/2605.02863v1
完整摘要: Traditional image quality assessment (IQA) methods rely on mean opinion scores (MOS), which are resource-intensive to collect and fail to provide interpretable, localized feedback on specific image distortions. We overcome these limitations by shifting from absolute quality prediction to a relational and directional assessment. Our approach utilizes a self-supervised synthetic distortion engine to generate training data, eliminating the need for manual annotation. A distortion prediction network is trained with an anti-symmetric objective to produce spatially-aware, disentangled maps that identify the type, intensity, and direction of distortions relative to a reference image. Subsequently, a scoring network is trained via contrastive learning on ordinally ranked image sets to predict a relational quality score. Our method provides a more granular and interpretable approach to IQA for the targeted optimization of image processing algorithms without requiring any human-labeled quality scores.
匹配关键词: self-supervised
---

[ACADEMIC - ARXIV]
标题: Perceptual Flow Network for Visually Grounded Reasoning
作者: Yangfu Li, Yuning Gong, Hongjian Zhan, Teng Li, Yuanhuiyi Lyu, Tianyi Chen, Qi Liu, Ziyuan Huang, Zhihang Zhong, Dandan Zheng, Yue Lu
链接: https://arxiv.org/abs/2605.02730v1
完整摘要: Despite the success of Large-Vision Language Models (LVLMs), general optimization objectives (e.g., standard MLE) fail to constrain visual trajectories, leading to language bias and hallucination. To mitigate this, current methods introduce geometric priors from visual experts as additional supervision. However, we observe that such supervision is typically suboptimal: it is biased toward geometric precision and offers limited reasoning utility. To bridge this gap, we propose Perceptual Flow Network (PFlowNet), which eschews rigid alignment with the expert priors and achieves interpretable yet more effective visual reasoning. Specifically, PFlowNet decouples perception from reasoning to establish a self-conditioned generation process. Based on this, it integrates multi-dimensional rewards with vicinal geometric shaping via variational reinforcement learning, thereby facilitating reasoning-oriented perceptual behaviors while preserving visual reliability. PFlowNet delivers a provable performance guarantee and competitive empirical results, particularly setting new SOTA records on V* Bench (90.6%) and MME-RealWorld-lite (67.0%).
匹配关键词: self-supervised
---

[ACADEMIC - ARXIV]
标题: Dimensionality-Aware Anomaly Detection in Learned Representations of Self-Supervised Speech Models
作者: Sandra Arcos-Holzinger, Sarah M. Erfani, James Bailey, Sanjeev Khudanpur
链接: https://arxiv.org/abs/2605.02715v1
完整摘要: Self-supervised speech models (S3Ms) achieve strong downstream performance, yet their learned representations remain poorly understood under natural and adversarial perturbations. Prior studies rely on representation similarity or global dimensionality, offering limited visibility into local geometric changes. We ask: how do perturbations deform local geometry, and do these shifts track downstream automatic speech recognition (ASR) degradation? To address this, we present GRIDS, a framework using Local Intrinsic Dimensionality (LID) across layer-wise representations in WavLM and wav2vec 2.0. We find that LID increases for all low signal-to noise ratio (SNR) perturbations and diverges at high SNR: benign noise converges toward the clean profile, while adversarial inputs retain early-layer LID elevation. We show LID elevation co-occurs with increased WER, and that layer-wise LID features enable anomaly detection (AUROC 0.78-1.00), opening the door to transcript-free monitoring in S3Ms.
匹配关键词: self-supervised
---

[ACADEMIC - ARXIV]
标题: Representation learning from OCT images
作者: Hedi Tabia, Désiré Sidibé, Nawres Khlifa, Ahmed Tabia, Ines Rahmany, Noura Aboudi, Zainab Haddad, Hajer Khachnaoui, Hsouna Zgolli
链接: https://arxiv.org/abs/2605.02589v1
完整摘要: Optical Coherence Tomography (OCT) has become one of the most used imaging modality in ophthalmology. It provides high-resolution, non-invasive visualization of retinal microarchitecture. The automated analysis of OCT images through representation learning has emerged as a central research frontier. This has mainly been driven by the clinical need to process large acquisition volumes. The objective is to reduce the reliance on expert annotation, and improve diagnostic consistency across devices and populations. This survey provides a comprehensive and structured review of representation learning methods for retinal OCT image analysis. It covers the period from early deep learning approaches to the most recent developments in foundation models and vision-language systems. We organize the literature along a principled taxonomy of learning paradigms, encompassing supervised learning with CNN-based and transformer-based architectures, self-supervised and semi-supervised methods, generative approaches, as well as 3D volumetric modeling, multimodal representation learning, and large-scale pretrained foundation models. For each paradigm, we analyze the core methodological contributions, identify persistent limitations, and trace the connections between successive approaches. We further provide a structured overview of publicly available OCT datasets, discuss evaluation protocol considerations, and present a unified problem formulation that situates each learning paradigm within a common mathematical framework. Building on this analysis, we identify and discuss the most pressing open research directions emerging in the literature. This includes volumetric foundation model pretraining, uncertainty-aware representation learning, federated and privacy-preserving training, fairness and bias mitigation, concept-based interpretability,...
匹配关键词: self-supervised
---

[ACADEMIC - ARXIV]
标题: Self-Supervised Spatial And Zero-Shot Angular Super-Resolution by Spatial-Angular Implicit Representation For Rotating-View SNR-Efficient Diffusion MRI
作者: Yinzhe Wu, Hongyu Rui, Fanwen Wang, Jiahao Huang, Zi Wang, Guang Yang
链接: https://arxiv.org/abs/2605.02575v1
完整摘要: Rotating-view thick-slice acquisition is highly SNR-efficient for mesoscale diffusion MRI (dMRI) but requires numerous rotating views to satisfy Nyquist sampling, resulting in long scan time. We propose a self-supervised Spatial-Angular Implicit Neural Representation (SA-INR) that reconstructs high-resolution dMRI from a single view per diffusion direction, representing a massive acceleration. Our model, an MLP conditioned on a b=0 structural prior and the b-direction via FiLM, is trained end-to-end on the anisotropic input. The framework not only accurately reconstructs the trained b-directions (spatial SR) but also learns a continuous q-space representation, enabling high-fidelity "zero-shot" synthesis of unseen b-directions (angular SR). On simulated data, our method achieved high fidelity for both trained (34.82 dB) and unseen (33.08 dB) directions. Most importantly, the synthesized angular data also improved the quantitative accuracy of downstream DTI model fitting. Our SA-INR framework breaks the classical sampling limits, paving the way for fast, quantitative high-resolution dMRI.
匹配关键词: self-supervised
---

[ACADEMIC - ARXIV]
标题: SpecKV: Adaptive Speculative Decoding with Compression-Aware Gamma Selection
作者: Shikhar Shukla
链接: https://arxiv.org/abs/2605.02888v1
完整摘要: Speculative decoding accelerates large language model (LLM) inference by using a small draft model to propose candidate tokens that a larger target model verifies. A critical hyperparameter in this process is the speculation length~$γ$, which determines how many tokens the draft model proposes per step. Nearly all existing systems use a fixed~$γ$ (typically~4), yet empirical evidence suggests that the optimal value varies across task types and, crucially, depends on the compression level applied to the target model. In this paper, we present \textbf{SpecKV}, a lightweight adaptive controller that selects~$γ$ per speculation step using signals extracted from the draft model itself. We profile speculative decoding across 4~task categories, 4~speculation lengths, and 3~compression levels (FP16, INT8, NF4), collecting 5,112 step-level records with per-step acceptance rates, draft entropy, and draft confidence. We demonstrate that the optimal~$γ$ shifts across compression regimes and that draft model confidence and entropy are strong predictors of acceptance rate (correlation~$\approx 0.56$). SpecKV uses a small MLP trained on these signals to maximize expected tokens per speculation step, achieving a 56.0\% improvement over the fixed-$γ$=4 baseline with only 0.34\,ms overhead per decision ($<$0.5\% of step time). The improvement is statistically significant ($p < 0.001$, paired bootstrap test). We release all profiling data, trained models, and notebooks as open-source artifacts.
匹配关键词: contrastive learning
---

[ACADEMIC - ARXIV]
标题: Unsupervised Machine Learning for Detecting Structural Anomalies in European Regional Statistics
作者: Bogdan Oancea
链接: https://arxiv.org/abs/2605.02884v1
完整摘要: Ensuring the coherence of regional socio-economic statistics is a central task for national statistical institutes. Traditional validation tools, such as range edits, ratio checks, or univariate outlier detection, are effective for identifying extreme values in individual series but are less suited for detecting unusual combinations of indicators in high-dimensional settings. This paper proposes an unsupervised machine learning framework for identifying structurally atypical regional profiles within Europe using publicly available Eurostat data. We construct a cross-sectional dataset of NUTS2 regions (2022) covering four key indicators: GDP per capita in PPS, unemployment rate, tertiary educational attainment, and population density. We apply and compare five anomaly detection techniques, univariate z-scores, Mahalanobis distance, Isolation Forest, Local Outlier Factor, and One-Class SVM, and classify a region as a structural anomaly if it is flagged by at least three of the five methods. The findings show that machine learning methods identify a consistent set of regions whose multivariate profiles diverge substantially from the EU-wide pattern. These include both highly developed metropolitan economies (Brussels, Vienna, Berlin, Prague) and regions with persistent socio-economic disadvantages (Central and Western Slovakia, Northern Hungary, Castilla-La Mancha, Extremadura), as well as Istanbul, whose profile differs markedly from EU capital regions. Importantly, these anomalies do not necessarily signal data quality issues; rather, they reflect meaningful structural divergence that warrants analytical or policy attention. The proposed framework is fully reproducible, scalable, and compatible with existing validation workflows, offering a flexible tool for early detection of unusual regional configurations within the European Statistical System.
匹配关键词: contrastive learning
---

[ACADEMIC - ARXIV]
标题: Multi-fidelity surrogates for mechanics of composites: from co-kriging to multi-fidelity neural networks
作者: Haizhou Wen, Elham Kiyani, Gang Li, Srikanth Pilla, George Em Karniadakis, Zhen Li
链接: https://arxiv.org/abs/2605.02871v1
完整摘要: Composite materials exhibit strongly hierarchical and anisotropic properties governed by coupled mechanisms spanning constituents, plies, laminates, structures, and manufacturing history. This intrinsic complexity makes predictive modeling of composites expensive, because repeated experiments and high-fidelity simulations are needed to cover large design spaces of material, structure, and manufacturing. Multi-fidelity surrogate modeling addresses this challenge by combining abundant, less expensive data with limited high-accuracy data to recover reliable high-fidelity predictions. This review presents a structured overview of multi-fidelity modeling for composite mechanics, covering Gaussian-process or Kriging-based methods, including co-Kriging, coregionalization models, autoregressive formulations, nonlinear autoregressive Gaussian processes, multi-fidelity deep Gaussian processes, and multi-fidelity neural networks. Their distinctions are examined in terms of cross-fidelity correlation, discrepancy representation, uncertainty quantification, and scalability. Selected examples of their applications to composites are introduced according to the roles that multi-fidelity surrogates play in engineering problems, including forward prediction for rapid exploration of material design spaces, inverse optimization for composite parameter identification and design search under limited high-fidelity access, and workflow integration, where heterogeneous data sources, constraints, and validation requirements determine model utility. Open question discussions highlight recurring challenges specific to composites, such as regime-dependent fidelity gaps associated with nonlinear damage and manufacturing history, mismatches between simulations and experiments, and uncertainty propagation across multi-fidelity models.
匹配关键词: contrastive learning
---

[ACADEMIC - ARXIV]
标题: Enhancing RL Generalizability in Robotics through SHAP Analysis of Algorithms and Hyperparameters
作者: Lingxiao Kong, Cong Yang, Oya Deniz Beyan, Zeyd Boukhers
链接: https://arxiv.org/abs/2605.02867v1
完整摘要: Despite significant advances in Reinforcement Learning (RL), model performance remains highly sensitive to algorithm and hyperparameter configurations, while generalization gaps across environments complicate real-world deployment. Although prior work has studied RL generalization, the relative contribution of specific configurations to the generalization gap has not been quantitatively decomposed and systematically leveraged for configuration selection. To address this limitation, we propose an explainable framework that evaluates RL performance across robotic environments using SHapley Additive exPlanations (SHAP) to quantify configuration impacts. We establish a theoretical foundation connecting Shapley values to generalizability, empirically analyze configuration impact patterns, and introduce SHAP-guided configuration selection to enhance generalization. Our results reveal distinct patterns across algorithms and hyperparameters, with consistent configuration impacts across diverse tasks and environments. By applying these insights to configuration selection, we achieve improved RL generalizability and provide actionable guidance for practitioners.
匹配关键词: contrastive learning
---

[ACADEMIC - ARXIV]
标题: Pixel Perfect: Relational Image Quality Assessment with Spatially-Aware Distortions
作者: Fadeel Sher Khan, Long N. Le, Abhinau K. Venkataramanan, Seok-Jun Lee, Hamid R. Sheikh
链接: https://arxiv.org/abs/2605.02863v1
完整摘要: Traditional image quality assessment (IQA) methods rely on mean opinion scores (MOS), which are resource-intensive to collect and fail to provide interpretable, localized feedback on specific image distortions. We overcome these limitations by shifting from absolute quality prediction to a relational and directional assessment. Our approach utilizes a self-supervised synthetic distortion engine to generate training data, eliminating the need for manual annotation. A distortion prediction network is trained with an anti-symmetric objective to produce spatially-aware, disentangled maps that identify the type, intensity, and direction of distortions relative to a reference image. Subsequently, a scoring network is trained via contrastive learning on ordinally ranked image sets to predict a relational quality score. Our method provides a more granular and interpretable approach to IQA for the targeted optimization of image processing algorithms without requiring any human-labeled quality scores.
匹配关键词: contrastive learning
---

[ACADEMIC - ARXIV]
标题: SpecKV: Adaptive Speculative Decoding with Compression-Aware Gamma Selection
作者: Shikhar Shukla
链接: https://arxiv.org/abs/2605.02888v1
完整摘要: Speculative decoding accelerates large language model (LLM) inference by using a small draft model to propose candidate tokens that a larger target model verifies. A critical hyperparameter in this process is the speculation length~$γ$, which determines how many tokens the draft model proposes per step. Nearly all existing systems use a fixed~$γ$ (typically~4), yet empirical evidence suggests that the optimal value varies across task types and, crucially, depends on the compression level applied to the target model. In this paper, we present \textbf{SpecKV}, a lightweight adaptive controller that selects~$γ$ per speculation step using signals extracted from the draft model itself. We profile speculative decoding across 4~task categories, 4~speculation lengths, and 3~compression levels (FP16, INT8, NF4), collecting 5,112 step-level records with per-step acceptance rates, draft entropy, and draft confidence. We demonstrate that the optimal~$γ$ shifts across compression regimes and that draft model confidence and entropy are strong predictors of acceptance rate (correlation~$\approx 0.56$). SpecKV uses a small MLP trained on these signals to maximize expected tokens per speculation step, achieving a 56.0\% improvement over the fixed-$γ$=4 baseline with only 0.34\,ms overhead per decision ($<$0.5\% of step time). The improvement is statistically significant ($p < 0.001$, paired bootstrap test). We release all profiling data, trained models, and notebooks as open-source artifacts.
匹配关键词: representation learning
---

[ACADEMIC - ARXIV]
标题: Unsupervised Machine Learning for Detecting Structural Anomalies in European Regional Statistics
作者: Bogdan Oancea
链接: https://arxiv.org/abs/2605.02884v1
完整摘要: Ensuring the coherence of regional socio-economic statistics is a central task for national statistical institutes. Traditional validation tools, such as range edits, ratio checks, or univariate outlier detection, are effective for identifying extreme values in individual series but are less suited for detecting unusual combinations of indicators in high-dimensional settings. This paper proposes an unsupervised machine learning framework for identifying structurally atypical regional profiles within Europe using publicly available Eurostat data. We construct a cross-sectional dataset of NUTS2 regions (2022) covering four key indicators: GDP per capita in PPS, unemployment rate, tertiary educational attainment, and population density. We apply and compare five anomaly detection techniques, univariate z-scores, Mahalanobis distance, Isolation Forest, Local Outlier Factor, and One-Class SVM, and classify a region as a structural anomaly if it is flagged by at least three of the five methods. The findings show that machine learning methods identify a consistent set of regions whose multivariate profiles diverge substantially from the EU-wide pattern. These include both highly developed metropolitan economies (Brussels, Vienna, Berlin, Prague) and regions with persistent socio-economic disadvantages (Central and Western Slovakia, Northern Hungary, Castilla-La Mancha, Extremadura), as well as Istanbul, whose profile differs markedly from EU capital regions. Importantly, these anomalies do not necessarily signal data quality issues; rather, they reflect meaningful structural divergence that warrants analytical or policy attention. The proposed framework is fully reproducible, scalable, and compatible with existing validation workflows, offering a flexible tool for early detection of unusual regional configurations within the European Statistical System.
匹配关键词: representation learning
---

[ACADEMIC - ARXIV]
标题: Multi-fidelity surrogates for mechanics of composites: from co-kriging to multi-fidelity neural networks
作者: Haizhou Wen, Elham Kiyani, Gang Li, Srikanth Pilla, George Em Karniadakis, Zhen Li
链接: https://arxiv.org/abs/2605.02871v1
完整摘要: Composite materials exhibit strongly hierarchical and anisotropic properties governed by coupled mechanisms spanning constituents, plies, laminates, structures, and manufacturing history. This intrinsic complexity makes predictive modeling of composites expensive, because repeated experiments and high-fidelity simulations are needed to cover large design spaces of material, structure, and manufacturing. Multi-fidelity surrogate modeling addresses this challenge by combining abundant, less expensive data with limited high-accuracy data to recover reliable high-fidelity predictions. This review presents a structured overview of multi-fidelity modeling for composite mechanics, covering Gaussian-process or Kriging-based methods, including co-Kriging, coregionalization models, autoregressive formulations, nonlinear autoregressive Gaussian processes, multi-fidelity deep Gaussian processes, and multi-fidelity neural networks. Their distinctions are examined in terms of cross-fidelity correlation, discrepancy representation, uncertainty quantification, and scalability. Selected examples of their applications to composites are introduced according to the roles that multi-fidelity surrogates play in engineering problems, including forward prediction for rapid exploration of material design spaces, inverse optimization for composite parameter identification and design search under limited high-fidelity access, and workflow integration, where heterogeneous data sources, constraints, and validation requirements determine model utility. Open question discussions highlight recurring challenges specific to composites, such as regime-dependent fidelity gaps associated with nonlinear damage and manufacturing history, mismatches between simulations and experiments, and uncertainty propagation across multi-fidelity models.
匹配关键词: representation learning
---

[ACADEMIC - ARXIV]
标题: Enhancing RL Generalizability in Robotics through SHAP Analysis of Algorithms and Hyperparameters
作者: Lingxiao Kong, Cong Yang, Oya Deniz Beyan, Zeyd Boukhers
链接: https://arxiv.org/abs/2605.02867v1
完整摘要: Despite significant advances in Reinforcement Learning (RL), model performance remains highly sensitive to algorithm and hyperparameter configurations, while generalization gaps across environments complicate real-world deployment. Although prior work has studied RL generalization, the relative contribution of specific configurations to the generalization gap has not been quantitatively decomposed and systematically leveraged for configuration selection. To address this limitation, we propose an explainable framework that evaluates RL performance across robotic environments using SHapley Additive exPlanations (SHAP) to quantify configuration impacts. We establish a theoretical foundation connecting Shapley values to generalizability, empirically analyze configuration impact patterns, and introduce SHAP-guided configuration selection to enhance generalization. Our results reveal distinct patterns across algorithms and hyperparameters, with consistent configuration impacts across diverse tasks and environments. By applying these insights to configuration selection, we achieve improved RL generalizability and provide actionable guidance for practitioners.
匹配关键词: representation learning
---

[ACADEMIC - ARXIV]
标题: Pixel Perfect: Relational Image Quality Assessment with Spatially-Aware Distortions
作者: Fadeel Sher Khan, Long N. Le, Abhinau K. Venkataramanan, Seok-Jun Lee, Hamid R. Sheikh
链接: https://arxiv.org/abs/2605.02863v1
完整摘要: Traditional image quality assessment (IQA) methods rely on mean opinion scores (MOS), which are resource-intensive to collect and fail to provide interpretable, localized feedback on specific image distortions. We overcome these limitations by shifting from absolute quality prediction to a relational and directional assessment. Our approach utilizes a self-supervised synthetic distortion engine to generate training data, eliminating the need for manual annotation. A distortion prediction network is trained with an anti-symmetric objective to produce spatially-aware, disentangled maps that identify the type, intensity, and direction of distortions relative to a reference image. Subsequently, a scoring network is trained via contrastive learning on ordinally ranked image sets to predict a relational quality score. Our method provides a more granular and interpretable approach to IQA for the targeted optimization of image processing algorithms without requiring any human-labeled quality scores.
匹配关键词: representation learning
---

[ACADEMIC - ARXIV]
标题: AlbumFill: Album-Guided Reasoning and Retrieval for Personalized Image Completion
作者: Yu-Ju Tsai, Brian Price, Qing Liu, Luis Figueroa, Daniil Pakhomov, Zhihong Ding, Scott Cohen, Ming-Hsuan Yang
链接: https://arxiv.org/abs/2605.02892v1
完整摘要: Personalized image completion aims to restore occluded regions in personal photos while preserving identity and appearance. Existing methods either rely on generic inpainting models that often fail to maintain identity consistency, or assume that suitable reference images are explicitly provided. In practice, suitable references are often not explicitly provided, requiring the system to search for identity-consistent images within personal photo collections. We present AlbumFill, a training-free framework that retrieves identity-consistent references from personal albums for personalized completion. Given an occluded image and a personal album, a vision-language model infers missing semantic cues to guide composed image retrieval, and the retrieved references are used by reference-based completion models. To facilitate this task, we introduce a dataset containing 54K human-centric samples with associated album images. Experiments across multiple baselines demonstrate the difficulty of personalized completion and highlight the importance of identity-consistent reference retrieval. Project Page: https://liagm.github.io/AlbumFill/
匹配关键词: masked language model
---

[ACADEMIC - ARXIV]
标题: SpecKV: Adaptive Speculative Decoding with Compression-Aware Gamma Selection
作者: Shikhar Shukla
链接: https://arxiv.org/abs/2605.02888v1
完整摘要: Speculative decoding accelerates large language model (LLM) inference by using a small draft model to propose candidate tokens that a larger target model verifies. A critical hyperparameter in this process is the speculation length~$γ$, which determines how many tokens the draft model proposes per step. Nearly all existing systems use a fixed~$γ$ (typically~4), yet empirical evidence suggests that the optimal value varies across task types and, crucially, depends on the compression level applied to the target model. In this paper, we present \textbf{SpecKV}, a lightweight adaptive controller that selects~$γ$ per speculation step using signals extracted from the draft model itself. We profile speculative decoding across 4~task categories, 4~speculation lengths, and 3~compression levels (FP16, INT8, NF4), collecting 5,112 step-level records with per-step acceptance rates, draft entropy, and draft confidence. We demonstrate that the optimal~$γ$ shifts across compression regimes and that draft model confidence and entropy are strong predictors of acceptance rate (correlation~$\approx 0.56$). SpecKV uses a small MLP trained on these signals to maximize expected tokens per speculation step, achieving a 56.0\% improvement over the fixed-$γ$=4 baseline with only 0.34\,ms overhead per decision ($<$0.5\% of step time). The improvement is statistically significant ($p < 0.001$, paired bootstrap test). We release all profiling data, trained models, and notebooks as open-source artifacts.
匹配关键词: masked language model
---

[ACADEMIC - ARXIV]
标题: MolmoAct2: Action Reasoning Models for Real-world Deployment
作者: Haoquan Fang, Jiafei Duan, Donovan Clay, Sam Wang, Shuo Liu, Weikai Huang, Xiang Fan, Wei-Chuan Tsai, Shirui Chen, Yi Ru Wang, Shanli Xing, Jaemin Cho, Jae Sung Park, Ainaz Eftekhar, Peter Sushko, Karen Farley, Angad Wadhwa, Cole Harrison, Winson Han, Ying-Chun Lee, Eli VanderBilt, Rose Hendrix, Suveen Ellawela, Lucas Ngoo, Joyce Chai, Zhongzheng Ren, Ali Farhadi, Dieter Fox, Ranjay Krishna
链接: https://arxiv.org/abs/2605.02881v1
完整摘要: Vision-Language-Action (VLA) models aim to provide a single generalist controller for robots, but today's systems fall short on the criteria that matter for real-world deployment. Frontier models are closed, open-weight alternatives are tied to expensive hardware, reasoning-augmented policies pay prohibitive latency for their grounding, and fine-tuned success rates remain below the threshold for dependable use. We present MolmoAct2, a fully open action reasoning model built for practical deployment, advancing its predecessor along five axes. We introduce MolmoER, a VLM backbone specialized for spatial and embodied reasoning, trained on a 3.3M-sample corpus with a specialize-then-rehearse recipe. We release three new datasets spanning low-to-medium cost platforms, including MolmoAct2-BimanualYAM, 720 hours of teleoperated bimanual trajectories that constitute the largest open bimanual dataset to date, together with quality-filtered Franka (DROID) and SO100/101 subsets. We provide OpenFAST, an open-weight, open-data action tokenizer trained on millions of trajectories across five embodiments. We redesign the architecture to graft a flow-matching continuous-action expert onto a discrete-token VLM via per-layer KV-cache conditioning. Finally, we propose MolmoThink, an adaptive-depth reasoning variant that re-predicts depth tokens only for scene regions that change between timesteps, retaining geometric grounding at a fraction of prior latency. In the most extensive empirical study of any open VLA to date, spanning 7 simulation and real-world benchmarks, MolmoAct2 outperforms strong baselines including Pi-05, while MolmoER surpasses GPT-5 and Gemini Robotics ER-1.5 across 13 embodied-reasoning benchmarks. We release model weights, training code, and complete training data. Project page: https://allenai.org/blog/molmoact2
匹配关键词: masked language model
---

[ACADEMIC - ARXIV]
标题: Multi-fidelity surrogates for mechanics of composites: from co-kriging to multi-fidelity neural networks
作者: Haizhou Wen, Elham Kiyani, Gang Li, Srikanth Pilla, George Em Karniadakis, Zhen Li
链接: https://arxiv.org/abs/2605.02871v1
完整摘要: Composite materials exhibit strongly hierarchical and anisotropic properties governed by coupled mechanisms spanning constituents, plies, laminates, structures, and manufacturing history. This intrinsic complexity makes predictive modeling of composites expensive, because repeated experiments and high-fidelity simulations are needed to cover large design spaces of material, structure, and manufacturing. Multi-fidelity surrogate modeling addresses this challenge by combining abundant, less expensive data with limited high-accuracy data to recover reliable high-fidelity predictions. This review presents a structured overview of multi-fidelity modeling for composite mechanics, covering Gaussian-process or Kriging-based methods, including co-Kriging, coregionalization models, autoregressive formulations, nonlinear autoregressive Gaussian processes, multi-fidelity deep Gaussian processes, and multi-fidelity neural networks. Their distinctions are examined in terms of cross-fidelity correlation, discrepancy representation, uncertainty quantification, and scalability. Selected examples of their applications to composites are introduced according to the roles that multi-fidelity surrogates play in engineering problems, including forward prediction for rapid exploration of material design spaces, inverse optimization for composite parameter identification and design search under limited high-fidelity access, and workflow integration, where heterogeneous data sources, constraints, and validation requirements determine model utility. Open question discussions highlight recurring challenges specific to composites, such as regime-dependent fidelity gaps associated with nonlinear damage and manufacturing history, mismatches between simulations and experiments, and uncertainty propagation across multi-fidelity models.
匹配关键词: masked language model
---

[ACADEMIC - ARXIV]
标题: Enhancing RL Generalizability in Robotics through SHAP Analysis of Algorithms and Hyperparameters
作者: Lingxiao Kong, Cong Yang, Oya Deniz Beyan, Zeyd Boukhers
链接: https://arxiv.org/abs/2605.02867v1
完整摘要: Despite significant advances in Reinforcement Learning (RL), model performance remains highly sensitive to algorithm and hyperparameter configurations, while generalization gaps across environments complicate real-world deployment. Although prior work has studied RL generalization, the relative contribution of specific configurations to the generalization gap has not been quantitatively decomposed and systematically leveraged for configuration selection. To address this limitation, we propose an explainable framework that evaluates RL performance across robotic environments using SHapley Additive exPlanations (SHAP) to quantify configuration impacts. We establish a theoretical foundation connecting Shapley values to generalizability, empirically analyze configuration impact patterns, and introduce SHAP-guided configuration selection to enhance generalization. Our results reveal distinct patterns across algorithms and hyperparameters, with consistent configuration impacts across diverse tasks and environments. By applying these insights to configuration selection, we achieve improved RL generalizability and provide actionable guidance for practitioners.
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
标题: Unified Map Prior Encoder for Mapping and Planning
作者: Zongzheng Zhang, Sizhe Zou, Guantian Zheng, Zhenxin Zhu, Yu Gao, Guoxuan Chi, Shuo Wang, Yuwen Heng, Zhigang Sun, Yiru Wang, Hao Sun, Chao Ma, Zhen Li, Anqing Jiang, Hao Zhao
链接: https://arxiv.org/abs/2605.02762v1
完整摘要: Online mapping and end-to-end (E2E) planning in autonomous driving remain largely sensor-centric, leaving rich map priors, including HD/SD vector maps, rasterized SD maps, and satellite imagery, underused because of heterogeneity, pose drift, and inconsistent availability at test time. We present UMPE, a Unified Map Prior Encoder that can ingest any subset of four priors and fuse them with BEV features for both mapping and planning. UMPE has two branches. The vector encoder pre-aligns HD/SD polylines with a frame-wise SE(2) correction, encodes points via multi-frequency sinusoidal features, and produces polyline tokens with confidence scores. BEV queries then apply cross-attention with confidence bias, followed by normalized channel-wise gating to avoid length imbalance and softly down-weight uncertain sources. The raster encoder shares a ResNet-18 backbone conditioned by FiLM with scaling and shift at every stage, performs SE(2) micro-alignment, and injects priors through zero-initialized residual fusion, so the network starts from a do-no-harm baseline and learns to add only useful prior evidence. A vector-then-raster fusion order reflects the inductive bias of geometry first, appearance second. On nuScenes mapping, UMPE lifts MapTRv2 from 61.5 to 67.4 mAP (+5.9) and MapQR from 66.4 to 71.7 mAP (+5.3). On Argoverse2, UMPE adds +4.1 mAP over strong baselines. UMPE is compositional: when trained with all priors, it outperforms single-prior models even when only one prior is available at test time, demonstrating powerset robustness. For E2E planning with the VAD backbone on nuScenes, UMPE reduces trajectory error from 0.72 to 0.42 m L2 on average (-0.30 m) and collision rate from 0.22% to 0.12% (-0.10%), surpassing recent prior-injection methods. These results show that a unified, alignment-aware treatment of heterogeneous map priors yields better mapping and better planning.
匹配关键词: MAE
---

[ACADEMIC - ARXIV]
标题: Foundation Models to Unlock Real-World Evidence from Nationwide Medical Claims
作者: Fan Ma, Yuntian Liu, Xiang Lan, Weipeng Zhou, Jun Ni, Mauro Giuffrè, Lingfei Qian, Xueqing Peng, Yujia Zhou, Ruey-Ling Weng, Huan He, Lu Li, Qingyu Chen, Andrew Loza, Laila Rasmy, Degui Zhi, Yuan Lu, Chenjie Zeng, Joshua C Denny, Lee Schwamm, Daniella Meeker, Lucila Ohno-Machado, Yong Chen, Hua Xu
链接: https://arxiv.org/abs/2605.02740v1
完整摘要: Evidence derived from large-scale real-world data (RWD) is increasingly informing regulatory evaluation and healthcare decision-making. Administrative claims provide population-scale, longitudinal records of healthcare utilization, expenditure, and detailed coding of diagnoses, procedures, and medications, yet their potential as a substrate for healthcare foundation models remains largely unexplored. Here we present ReClaim, a generative transformer trained from scratch on 43.8 billion medical events from more than 200 million enrollees in the MarketScan claims data spanning 2008-2022. ReClaim models longitudinal trajectories across diagnoses, procedures, medications, and expenditure, and was scaled to 140 million, 700 million, and 1.7 billion parameters. Across over 1,000 disease-onset prediction tasks, ReClaim achieved a mean AUC of 75.6%, substantially outperforming disease-specific LightGBM (66.3%) and the transformer-based Delphi model (69.4%), with the largest gains for rare diseases. These advantages held across retrospective and prospective evaluations and in external validation on two independent datasets. Performance improved monotonically with scale, and post-training added 13.8 percentage points over pre-training alone. Beyond disease prediction, ReClaim captured financial outcomes and improved real-world evidence (RWE) analyses: for healthcare expenditure forecasting it increased explained variance from 0.28 to 0.37 relative to LightGBM, and in a target trial emulation it reduced systematic bias by 72% on average relative to Delphi. Together, these results establish administrative claims as a scalable substrate for healthcare foundation models and show that learned representations generalize across time periods and data sources, supporting disease surveillance, expenditure forecasting, and RWE generation.
匹配关键词: MAE
---

[ACADEMIC - ARXIV]
标题: The 2026 ACII Dyadic Conversations (DaiKon) Workshop & Challenge
作者: Panagiotis Tzirakis, Alice Baird, Jeffrey Brooks, Emilia Parada-Cabaleiro, Lukas Stappen, Sharath Rao, Theo Lebryk, Jakub Piotr Clapa, Jens Madsen
链接: https://arxiv.org/abs/2605.02672v1
完整摘要: The 2026 ACII Dyadic Conversations (ACII-DaiKon) Workshop & Challenge introduces a benchmark for modeling interpersonal affect and social dynamics in dyadic conversations. Although conversational affect modeling has advanced rapidly, most benchmarks remain speaker-centric and underrepresent coupled, time-evolving processes between partners, including directional influence, conversational timing coordination, and rapport development. To address this gap, ACII-DaiKon presents three coordinated sub-challenges built on a shared dataset: (1) directional interpersonal influence prediction, (2) turn-taking prediction (next-speaker and time-to-next-speech), and (3) rapport trajectory prediction across full interactions. The challenge is built on the Hume-DaiKon dataset, comprising 945 dyadic conversations (743.4 hours of audiovisual data) collected under naturalistic conditions across five languages. The benchmark supports multimodal modeling, temporal reasoning, and cross-context generalization through fixed train/validation/test splits, standardized metrics, and released baseline systems. Evaluation uses Concordance Correlation Coefficient (CCC), Pearson correlation, Macro-F1, and Mean Absolute Error (MAE) depending on the sub-challenge. Baseline experiments establish initial reference performance, with best test results of 0.40 CCC and 0.50 Pearson for influence prediction, 0.66 Macro-F1 and 1.50~s MAE for turn-taking, and 0.68 CCC and 0.70 Pearson for rapport trajectory modeling. These results indicate that while current methods capture coarse dyadic patterns, robust modeling of directional dependence and long-horizon interpersonal dynamics remains challenging. The workshop provides a shared platform for rigorous comparison and cross-disciplinary discussion on data validity, evaluation protocols, and culturally aware modeling for dyadic interaction.
匹配关键词: MAE
---

[ACADEMIC - ARXIV]
标题: Mamoda2.5: Enhancing Unified Multimodal Model with DiT-MoE
作者: Yangming Shi, Shixiang Zhu, Tao Shen, Zhimiao Yu, Dengsheng Chen, Taicai Chen, Yunfei Yang, Juan Zhou, Chen Cheng, Liang Ma, Xibin Wu, Benxuan Yan, Ge Li, Tuoyu Zhang, Dan Li, Chang Liu, Zhenbang Sun
链接: https://arxiv.org/abs/2605.02641v1
完整摘要: We present Mamoda2.5, a unified AR-Diffusion framework that seamlessly integrates multimodal understanding and generation within a single architecture. To efficiently enhance the model's generation capability, we equip the Diffusion Transformer backbone with a fine-grained Mixture-of-Experts (MoE) design (128 experts, Top-8 routing), yielding a 25B-parameter model that activates only 3B parameters, significantly reducing training costs while scaling up the model capacity. Mamoda2.5 achieves top-tier generation performance on VBench 2.0 and sets a new record in video editing quality, surpassing evaluated open-source models and matching the performance of current top-tier proprietary models, including the Kling O1 on OpenVE-Bench. Furthermore, we introduce a joint few-step distillation and reinforcement learning framework that compresses the 30-step editing model into a 4-step model and greatly accelerates model inference. Compared to open-source baselines, Mamoda2.5 achieves up to $95.9\times$ faster video editing inference. In real-world applications, Mamoda2.5 has been successfully deployed for content moderation and creative restoration tasks in advertising scenarios, achieving a 98% success rate in internal advertising video editing scenario.
匹配关键词: MAE
---

[ACADEMIC - ARXIV]
标题: Strategy-Aware Optimization Modeling with Reasoning LLMs
作者: Ruiqing Zhao, Fengzhi Li, Yuan Zuo, Rui Liu, Yansong Liu, Yunfei Ma, Fanyu Meng, Junlan Feng
链接: https://arxiv.org/abs/2605.02545v1
完整摘要: Large language models (LLMs) can generate syntactically valid optimization programs, yet often struggle to reliably choose an effective modeling strategy, leading to incorrect formulations and inefficient solver behavior. We propose SAGE, a strategy-aware framework that makes Modeling Strategy explicit in both data construction and post-training. SAGE builds a solver-verified multi-strategy dataset and trains a student model with supervised fine-tuning followed by Segment-Weighted GRPO using a composite reward over format compliance, correctness, and solver efficiency. Across eight benchmarks spanning synthetic and real-world settings, SAGE improves average pass@1 from 72.7 to 80.3 over the strongest open-source baseline. With multiple generations, SAGE discovers more distinct correct formulations and improves component-level diversity at pass@16 by 19-29%. At the largest scale, SAGE produces more compact constraint systems with 14.2% fewer constraints than the baseline, consistent with solver-efficient modeling. Overall, these results show that making Modeling Strategy explicit improves automated optimization modeling. Code is available at https://github.com/rachhhhing/SAGE.
匹配关键词: MAE
---

[ACADEMIC - ARXIV]
标题: AlbumFill: Album-Guided Reasoning and Retrieval for Personalized Image Completion
作者: Yu-Ju Tsai, Brian Price, Qing Liu, Luis Figueroa, Daniil Pakhomov, Zhihong Ding, Scott Cohen, Ming-Hsuan Yang
链接: https://arxiv.org/abs/2605.02892v1
完整摘要: Personalized image completion aims to restore occluded regions in personal photos while preserving identity and appearance. Existing methods either rely on generic inpainting models that often fail to maintain identity consistency, or assume that suitable reference images are explicitly provided. In practice, suitable references are often not explicitly provided, requiring the system to search for identity-consistent images within personal photo collections. We present AlbumFill, a training-free framework that retrieves identity-consistent references from personal albums for personalized completion. Given an occluded image and a personal album, a vision-language model infers missing semantic cues to guide composed image retrieval, and the retrieved references are used by reference-based completion models. To facilitate this task, we introduce a dataset containing 54K human-centric samples with associated album images. Experiments across multiple baselines demonstrate the difficulty of personalized completion and highlight the importance of identity-consistent reference retrieval. Project Page: https://liagm.github.io/AlbumFill/
匹配关键词: generative model
---

[ACADEMIC - ARXIV]
标题: SpecKV: Adaptive Speculative Decoding with Compression-Aware Gamma Selection
作者: Shikhar Shukla
链接: https://arxiv.org/abs/2605.02888v1
完整摘要: Speculative decoding accelerates large language model (LLM) inference by using a small draft model to propose candidate tokens that a larger target model verifies. A critical hyperparameter in this process is the speculation length~$γ$, which determines how many tokens the draft model proposes per step. Nearly all existing systems use a fixed~$γ$ (typically~4), yet empirical evidence suggests that the optimal value varies across task types and, crucially, depends on the compression level applied to the target model. In this paper, we present \textbf{SpecKV}, a lightweight adaptive controller that selects~$γ$ per speculation step using signals extracted from the draft model itself. We profile speculative decoding across 4~task categories, 4~speculation lengths, and 3~compression levels (FP16, INT8, NF4), collecting 5,112 step-level records with per-step acceptance rates, draft entropy, and draft confidence. We demonstrate that the optimal~$γ$ shifts across compression regimes and that draft model confidence and entropy are strong predictors of acceptance rate (correlation~$\approx 0.56$). SpecKV uses a small MLP trained on these signals to maximize expected tokens per speculation step, achieving a 56.0\% improvement over the fixed-$γ$=4 baseline with only 0.34\,ms overhead per decision ($<$0.5\% of step time). The improvement is statistically significant ($p < 0.001$, paired bootstrap test). We release all profiling data, trained models, and notebooks as open-source artifacts.
匹配关键词: generative model
---

[ACADEMIC - ARXIV]
标题: MolmoAct2: Action Reasoning Models for Real-world Deployment
作者: Haoquan Fang, Jiafei Duan, Donovan Clay, Sam Wang, Shuo Liu, Weikai Huang, Xiang Fan, Wei-Chuan Tsai, Shirui Chen, Yi Ru Wang, Shanli Xing, Jaemin Cho, Jae Sung Park, Ainaz Eftekhar, Peter Sushko, Karen Farley, Angad Wadhwa, Cole Harrison, Winson Han, Ying-Chun Lee, Eli VanderBilt, Rose Hendrix, Suveen Ellawela, Lucas Ngoo, Joyce Chai, Zhongzheng Ren, Ali Farhadi, Dieter Fox, Ranjay Krishna
链接: https://arxiv.org/abs/2605.02881v1
完整摘要: Vision-Language-Action (VLA) models aim to provide a single generalist controller for robots, but today's systems fall short on the criteria that matter for real-world deployment. Frontier models are closed, open-weight alternatives are tied to expensive hardware, reasoning-augmented policies pay prohibitive latency for their grounding, and fine-tuned success rates remain below the threshold for dependable use. We present MolmoAct2, a fully open action reasoning model built for practical deployment, advancing its predecessor along five axes. We introduce MolmoER, a VLM backbone specialized for spatial and embodied reasoning, trained on a 3.3M-sample corpus with a specialize-then-rehearse recipe. We release three new datasets spanning low-to-medium cost platforms, including MolmoAct2-BimanualYAM, 720 hours of teleoperated bimanual trajectories that constitute the largest open bimanual dataset to date, together with quality-filtered Franka (DROID) and SO100/101 subsets. We provide OpenFAST, an open-weight, open-data action tokenizer trained on millions of trajectories across five embodiments. We redesign the architecture to graft a flow-matching continuous-action expert onto a discrete-token VLM via per-layer KV-cache conditioning. Finally, we propose MolmoThink, an adaptive-depth reasoning variant that re-predicts depth tokens only for scene regions that change between timesteps, retaining geometric grounding at a fraction of prior latency. In the most extensive empirical study of any open VLA to date, spanning 7 simulation and real-world benchmarks, MolmoAct2 outperforms strong baselines including Pi-05, while MolmoER surpasses GPT-5 and Gemini Robotics ER-1.5 across 13 embodied-reasoning benchmarks. We release model weights, training code, and complete training data. Project page: https://allenai.org/blog/molmoact2
匹配关键词: generative model
---

[ACADEMIC - ARXIV]
标题: Multi-fidelity surrogates for mechanics of composites: from co-kriging to multi-fidelity neural networks
作者: Haizhou Wen, Elham Kiyani, Gang Li, Srikanth Pilla, George Em Karniadakis, Zhen Li
链接: https://arxiv.org/abs/2605.02871v1
完整摘要: Composite materials exhibit strongly hierarchical and anisotropic properties governed by coupled mechanisms spanning constituents, plies, laminates, structures, and manufacturing history. This intrinsic complexity makes predictive modeling of composites expensive, because repeated experiments and high-fidelity simulations are needed to cover large design spaces of material, structure, and manufacturing. Multi-fidelity surrogate modeling addresses this challenge by combining abundant, less expensive data with limited high-accuracy data to recover reliable high-fidelity predictions. This review presents a structured overview of multi-fidelity modeling for composite mechanics, covering Gaussian-process or Kriging-based methods, including co-Kriging, coregionalization models, autoregressive formulations, nonlinear autoregressive Gaussian processes, multi-fidelity deep Gaussian processes, and multi-fidelity neural networks. Their distinctions are examined in terms of cross-fidelity correlation, discrepancy representation, uncertainty quantification, and scalability. Selected examples of their applications to composites are introduced according to the roles that multi-fidelity surrogates play in engineering problems, including forward prediction for rapid exploration of material design spaces, inverse optimization for composite parameter identification and design search under limited high-fidelity access, and workflow integration, where heterogeneous data sources, constraints, and validation requirements determine model utility. Open question discussions highlight recurring challenges specific to composites, such as regime-dependent fidelity gaps associated with nonlinear damage and manufacturing history, mismatches between simulations and experiments, and uncertainty propagation across multi-fidelity models.
匹配关键词: generative model
---

[ACADEMIC - ARXIV]
标题: Enhancing RL Generalizability in Robotics through SHAP Analysis of Algorithms and Hyperparameters
作者: Lingxiao Kong, Cong Yang, Oya Deniz Beyan, Zeyd Boukhers
链接: https://arxiv.org/abs/2605.02867v1
完整摘要: Despite significant advances in Reinforcement Learning (RL), model performance remains highly sensitive to algorithm and hyperparameter configurations, while generalization gaps across environments complicate real-world deployment. Although prior work has studied RL generalization, the relative contribution of specific configurations to the generalization gap has not been quantitatively decomposed and systematically leveraged for configuration selection. To address this limitation, we propose an explainable framework that evaluates RL performance across robotic environments using SHapley Additive exPlanations (SHAP) to quantify configuration impacts. We establish a theoretical foundation connecting Shapley values to generalizability, empirically analyze configuration impact patterns, and introduce SHAP-guided configuration selection to enhance generalization. Our results reveal distinct patterns across algorithms and hyperparameters, with consistent configuration impacts across diverse tasks and environments. By applying these insights to configuration selection, we achieve improved RL generalizability and provide actionable guidance for practitioners.
匹配关键词: generative model
---

[ACADEMIC - ARXIV]
标题: AlbumFill: Album-Guided Reasoning and Retrieval for Personalized Image Completion
作者: Yu-Ju Tsai, Brian Price, Qing Liu, Luis Figueroa, Daniil Pakhomov, Zhihong Ding, Scott Cohen, Ming-Hsuan Yang
链接: https://arxiv.org/abs/2605.02892v1
完整摘要: Personalized image completion aims to restore occluded regions in personal photos while preserving identity and appearance. Existing methods either rely on generic inpainting models that often fail to maintain identity consistency, or assume that suitable reference images are explicitly provided. In practice, suitable references are often not explicitly provided, requiring the system to search for identity-consistent images within personal photo collections. We present AlbumFill, a training-free framework that retrieves identity-consistent references from personal albums for personalized completion. Given an occluded image and a personal album, a vision-language model infers missing semantic cues to guide composed image retrieval, and the retrieved references are used by reference-based completion models. To facilitate this task, we introduce a dataset containing 54K human-centric samples with associated album images. Experiments across multiple baselines demonstrate the difficulty of personalized completion and highlight the importance of identity-consistent reference retrieval. Project Page: https://liagm.github.io/AlbumFill/
匹配关键词: diffusion model
---

[ACADEMIC - ARXIV]
标题: SpecKV: Adaptive Speculative Decoding with Compression-Aware Gamma Selection
作者: Shikhar Shukla
链接: https://arxiv.org/abs/2605.02888v1
完整摘要: Speculative decoding accelerates large language model (LLM) inference by using a small draft model to propose candidate tokens that a larger target model verifies. A critical hyperparameter in this process is the speculation length~$γ$, which determines how many tokens the draft model proposes per step. Nearly all existing systems use a fixed~$γ$ (typically~4), yet empirical evidence suggests that the optimal value varies across task types and, crucially, depends on the compression level applied to the target model. In this paper, we present \textbf{SpecKV}, a lightweight adaptive controller that selects~$γ$ per speculation step using signals extracted from the draft model itself. We profile speculative decoding across 4~task categories, 4~speculation lengths, and 3~compression levels (FP16, INT8, NF4), collecting 5,112 step-level records with per-step acceptance rates, draft entropy, and draft confidence. We demonstrate that the optimal~$γ$ shifts across compression regimes and that draft model confidence and entropy are strong predictors of acceptance rate (correlation~$\approx 0.56$). SpecKV uses a small MLP trained on these signals to maximize expected tokens per speculation step, achieving a 56.0\% improvement over the fixed-$γ$=4 baseline with only 0.34\,ms overhead per decision ($<$0.5\% of step time). The improvement is statistically significant ($p < 0.001$, paired bootstrap test). We release all profiling data, trained models, and notebooks as open-source artifacts.
匹配关键词: diffusion model
---

[ACADEMIC - ARXIV]
标题: MolmoAct2: Action Reasoning Models for Real-world Deployment
作者: Haoquan Fang, Jiafei Duan, Donovan Clay, Sam Wang, Shuo Liu, Weikai Huang, Xiang Fan, Wei-Chuan Tsai, Shirui Chen, Yi Ru Wang, Shanli Xing, Jaemin Cho, Jae Sung Park, Ainaz Eftekhar, Peter Sushko, Karen Farley, Angad Wadhwa, Cole Harrison, Winson Han, Ying-Chun Lee, Eli VanderBilt, Rose Hendrix, Suveen Ellawela, Lucas Ngoo, Joyce Chai, Zhongzheng Ren, Ali Farhadi, Dieter Fox, Ranjay Krishna
链接: https://arxiv.org/abs/2605.02881v1
完整摘要: Vision-Language-Action (VLA) models aim to provide a single generalist controller for robots, but today's systems fall short on the criteria that matter for real-world deployment. Frontier models are closed, open-weight alternatives are tied to expensive hardware, reasoning-augmented policies pay prohibitive latency for their grounding, and fine-tuned success rates remain below the threshold for dependable use. We present MolmoAct2, a fully open action reasoning model built for practical deployment, advancing its predecessor along five axes. We introduce MolmoER, a VLM backbone specialized for spatial and embodied reasoning, trained on a 3.3M-sample corpus with a specialize-then-rehearse recipe. We release three new datasets spanning low-to-medium cost platforms, including MolmoAct2-BimanualYAM, 720 hours of teleoperated bimanual trajectories that constitute the largest open bimanual dataset to date, together with quality-filtered Franka (DROID) and SO100/101 subsets. We provide OpenFAST, an open-weight, open-data action tokenizer trained on millions of trajectories across five embodiments. We redesign the architecture to graft a flow-matching continuous-action expert onto a discrete-token VLM via per-layer KV-cache conditioning. Finally, we propose MolmoThink, an adaptive-depth reasoning variant that re-predicts depth tokens only for scene regions that change between timesteps, retaining geometric grounding at a fraction of prior latency. In the most extensive empirical study of any open VLA to date, spanning 7 simulation and real-world benchmarks, MolmoAct2 outperforms strong baselines including Pi-05, while MolmoER surpasses GPT-5 and Gemini Robotics ER-1.5 across 13 embodied-reasoning benchmarks. We release model weights, training code, and complete training data. Project page: https://allenai.org/blog/molmoact2
匹配关键词: diffusion model
---

[ACADEMIC - ARXIV]
标题: Multi-fidelity surrogates for mechanics of composites: from co-kriging to multi-fidelity neural networks
作者: Haizhou Wen, Elham Kiyani, Gang Li, Srikanth Pilla, George Em Karniadakis, Zhen Li
链接: https://arxiv.org/abs/2605.02871v1
完整摘要: Composite materials exhibit strongly hierarchical and anisotropic properties governed by coupled mechanisms spanning constituents, plies, laminates, structures, and manufacturing history. This intrinsic complexity makes predictive modeling of composites expensive, because repeated experiments and high-fidelity simulations are needed to cover large design spaces of material, structure, and manufacturing. Multi-fidelity surrogate modeling addresses this challenge by combining abundant, less expensive data with limited high-accuracy data to recover reliable high-fidelity predictions. This review presents a structured overview of multi-fidelity modeling for composite mechanics, covering Gaussian-process or Kriging-based methods, including co-Kriging, coregionalization models, autoregressive formulations, nonlinear autoregressive Gaussian processes, multi-fidelity deep Gaussian processes, and multi-fidelity neural networks. Their distinctions are examined in terms of cross-fidelity correlation, discrepancy representation, uncertainty quantification, and scalability. Selected examples of their applications to composites are introduced according to the roles that multi-fidelity surrogates play in engineering problems, including forward prediction for rapid exploration of material design spaces, inverse optimization for composite parameter identification and design search under limited high-fidelity access, and workflow integration, where heterogeneous data sources, constraints, and validation requirements determine model utility. Open question discussions highlight recurring challenges specific to composites, such as regime-dependent fidelity gaps associated with nonlinear damage and manufacturing history, mismatches between simulations and experiments, and uncertainty propagation across multi-fidelity models.
匹配关键词: diffusion model
---

[ACADEMIC - ARXIV]
标题: Enhancing RL Generalizability in Robotics through SHAP Analysis of Algorithms and Hyperparameters
作者: Lingxiao Kong, Cong Yang, Oya Deniz Beyan, Zeyd Boukhers
链接: https://arxiv.org/abs/2605.02867v1
完整摘要: Despite significant advances in Reinforcement Learning (RL), model performance remains highly sensitive to algorithm and hyperparameter configurations, while generalization gaps across environments complicate real-world deployment. Although prior work has studied RL generalization, the relative contribution of specific configurations to the generalization gap has not been quantitatively decomposed and systematically leveraged for configuration selection. To address this limitation, we propose an explainable framework that evaluates RL performance across robotic environments using SHapley Additive exPlanations (SHAP) to quantify configuration impacts. We establish a theoretical foundation connecting Shapley values to generalizability, empirically analyze configuration impact patterns, and introduce SHAP-guided configuration selection to enhance generalization. Our results reveal distinct patterns across algorithms and hyperparameters, with consistent configuration impacts across diverse tasks and environments. By applying these insights to configuration selection, we achieve improved RL generalizability and provide actionable guidance for practitioners.
匹配关键词: diffusion model
---

[ACADEMIC - ARXIV]
标题: Virtual Scanning for NSCLC Histology: Investigating the Discriminatory Power of Synthetic PET
作者: Fatih Aksu, Laura Ciuffetti, Francesco Di Feola, Filippo Ruffini, Giulia Romoli, Fabrizia Gelardi, Arturo Chiti, Valerio Guarrasi, Paolo Soda
链接: https://arxiv.org/abs/2605.02746v1
完整摘要: Accurate histological differentiation between adenocarcinoma (ADC) and squamous cell carcinoma (SCC) is critical for personalized treatment in non-small cell lung cancer (NSCLC). While [$^{18}$F]FDG PET/CT is a standard tool for the clinical evaluation of lung cancer, its utility is often limited by high costs and radiation exposure. In this paper, we investigate the feasibility of "virtual scanning" as a feature-enhancement strategy by evaluating whether synthetic PET data can provide complementary feature representations to supplement anatomical CT scans in histological subtype classification. We propose a framework that leverages a 3D Pix2Pix Generative Adversarial Network (GAN), pretrained on the FDG-PET/CT Lesions dataset, to synthesize pseudo-PET volumes from anatomical CT scans. These synthetic volumes are integrated with structural CT data within the MINT framework, a multi-stage intermediate fusion architecture. Our experiments, conducted on a multi-center dataset of 714 subjects, demonstrate that the inclusion of synthetic metabolic features significantly improves classification performance over a CT-only baseline. The multimodal approach achieved a statistically significant increase in the Area Under the Curve (AUC) from 0.489 to 0.591 and improved the Geometric Mean (GMean) from 0.305 to 0.524. These results suggest that synthetic PET scans provide discriminatory metabolic cues that enable deep learning models to exploit complementary cross-modal information, offering a potential feature-enhancement strategy for clinical scenarios where physical PET scans are unavailable.
匹配关键词: GAN
---

[ACADEMIC - ARXIV]
标题: Video Generation with Predictive Latents
作者: Yian Zhao, Feng Wang, Qiushan Guo, Chang Liu, Xiangyang Ji, Jian Zhang, Jie Chen
链接: https://arxiv.org/abs/2605.02134v1
完整摘要: Video Variational Autoencoder (VAE) enables latent video generative modeling by mapping the visual world into compact spatiotemporal latent spaces, improving training efficiency and stability. While existing video VAEs achieve commendable reconstruction quality, continued optimization of reconstruction does not necessarily translate into improved generative performance. How to enhance the diffusability of video latents remains a critical and unresolved challenge. In this work, inspired by principles of predictive world modeling, we investigate the potential of predictive learning to improve the video generative modeling. To this end, we introduce a simple and effective predictive reconstruction objective that unifies predictive learning with video reconstruction. Specifically, we randomly discard future frames and encode only partial past observations, while training the decoder to reconstruct the observed frames and predict future ones simultaneously. This design encourages the latent space to encode temporally predictive structures and build a more coherent understanding of video dynamics, thereby improving generation quality. Our model, termed Predictive Video VAE (PV-VAE), achieves superior performance on video generation, with 52% faster convergence and a 34.42 FVD improvement over the Wan2.2 VAE on UCF101. Furthermore, comprehensive analyses demonstrate that PV-VAE not only exhibits favorable scalability, with generative performance improving alongside VAE training, but also yields consistent gains in downstream video understanding, underscoring a latent space that effectively captures temporal coherence and motion priors.
匹配关键词: VAE
---

[ACADEMIC - ARXIV]
标题: Learning Multimodal Energy-Based Model with Multimodal Variational Auto-Encoder via MCMC Revision
作者: Jiali Cui, Zhiqiang Lao, Heather Yu
链接: https://arxiv.org/abs/2605.00644v1
完整摘要: Energy-based models (EBMs) are a flexible class of deep generative models and are well-suited to capture complex dependencies in multimodal data. However, learning multimodal EBM by maximum likelihood requires Markov Chain Monte Carlo (MCMC) sampling in the joint data space, where noise-initialized Langevin dynamics often mixes poorly and fails to discover coherent inter-modal relationships. Multimodal VAEs have made progress in capturing such inter-modal dependencies by introducing a shared latent generator and a joint inference model. However, both the shared latent generator and joint inference model are parameterized as unimodal Gaussian (or Laplace), which severely limits their ability to approximate the complex structure induced by multimodal data. In this work, we study the learning problem of the multimodal EBM, shared latent generator, and joint inference model. We present a learning framework that effectively interweaves their MLE updates with corresponding MCMC refinements in both the data and latent spaces. Specifically, the generator is learned to produce coherent multimodal samples that serve as strong initial states for EBM sampling, while the inference model is learned to provide informative latent initializations for generator posterior sampling. Together, these two models serve as complementary models that enable effective EBM sampling and learning, yielding realistic and coherent multimodal EBM samples. Extensive experiments demonstrate superior performance for multimodal synthesis quality and coherence compared to various baselines. We conduct various analyses and ablation studies to validate the effectiveness and scalability of the proposed multimodal framework.
匹配关键词: VAE
---

[ACADEMIC - ARXIV]
标题: Scalable Context-Aware Graph Attention for Unsupervised Anomaly Detection in Large-Scale Mobile Networks
作者: Sara Malacarne, Eirik Hoel-Høiseth, Erlend Aune, David Zsolt Biró, Massimiliano Ruocco
链接: https://arxiv.org/abs/2605.00482v1
完整摘要: Mobile network operators must monitor thousands of heterogeneous network elements across the radio access network and the packet core, each exposing high-dimensional KPI time series. The scale and cost of incident labelling make supervised approaches impractical, motivating unsupervised anomaly detection robust to context shifts and nonstationarity. We propose \textbf{C-MTAD-GAT} (\emph{Context-aware Multivariate Time-series Anomaly Detection with Graph Attention}), an anomaly detection framework designed to operate as a single shared model across large populations of network elements. The model combines temporal and feature-wise graph attention with lightweight static and dynamic context conditioning and a dual-head decoder for reconstruction and multi-step forecasting. It produces per-element, per-feature anomaly scores, converted to alerts via fully unsupervised thresholds calibrated from validation residuals. On the TELCO dataset released with DC-VAE \cite{garcia2023onemodel}, C-MTAD-GAT improves event-level affiliation and pointwise F1 while generating fewer alarms than prior graph-attention and VAE-based baselines. We then apply the same system to nation-scale radio access and evolved packet core control-plane counter data from a mobile network operator, where it is deployed. Operator feedback indicates the alerts are actionable and support daily monitoring, showing scalability across domains without relying on labelled incidents.
匹配关键词: VAE
---

[ACADEMIC - ARXIV]
标题: VQ-SAD: Vector Quantized Structure Aware Diffusion For Molecule Generation
作者: Farshad Noravesh, Reza Haffari, Layki Soon, Arghya Pal
链接: https://arxiv.org/abs/2605.00354v1
完整摘要: Many diffusion based molecule generation methods ignore the symbolic information of molecules and represent the atom and bond type as one hot representation. Methods based on Morgan fingerprints produce hash collisions and are hard to embed into a continuous space without information loss and random fingerprints correspond to no valid molecule. To circumvent this issue we use another paradigm and consider atom and bond codes as latent variables of VQ-VAE. We introduce VQ-SAD which first trains a VQ-VAE and uses the frozen pretrained VQ-VAE model and considers the codebooks for both atom and bond types as tokenizers for the downstream diffusion process. VQ-SAD is a neuro-symbolic model that utilizes both symbolic and neural structural information for a diffusion based model with learnable forward process. The large discrete code space provides a more balanced atom and bond types which enhances the denoising process. VQ-VAE slightly outperforms SOTA models for diffusion based molecule generation on QM9 and ZINC250k datasets.
匹配关键词: VAE
---

[ACADEMIC - ARXIV]
标题: Beyond Gaussian Bottlenecks: Topologically Aligned Encoding of Vision-Transformer Feature Spaces
作者: Andrew Bond, Ilkin Umut Melanlioglu, Erkut Erdem, Aykut Erdem
链接: https://arxiv.org/abs/2604.28122v1
完整摘要: Modern visual world modeling systems increasingly rely on high-capacity architectures and large-scale data to produce plausible motion, yet they often fail to preserve underlying 3D geometry or physically consistent camera dynamics. A key limitation lies not only in model capacity, but in the latent representations used to encode geometric structure. We propose S$^2$VAE, a geometry-first latent learning framework that focuses on compressing and representing the latent 3D state of a scene, including camera motion, depth, and point-level structure, rather than modeling appearance alone. Building on representations from a Visual Geometry Grounded Transformer (VGGT), we introduce a novel type of variational autoencoder using a product of Power Spherical latent distributions, explicitly enforcing hyperspherical structure in the bottleneck to preserve directional and geometric semantics under strong compression. Across depth estimation, camera pose recovery, and point cloud reconstruction, we show that geometry-aligned hyperspherical latents consistently outperform conventional Gaussian bottlenecks, particularly in high-compression regimes. Our results highlight latent geometry as a first-class design choice for physically grounded visual and world models.
匹配关键词: VAE
---

[ACADEMIC - ARXIV]
标题: Multi-fidelity surrogates for mechanics of composites: from co-kriging to multi-fidelity neural networks
作者: Haizhou Wen, Elham Kiyani, Gang Li, Srikanth Pilla, George Em Karniadakis, Zhen Li
链接: https://arxiv.org/abs/2605.02871v1
完整摘要: Composite materials exhibit strongly hierarchical and anisotropic properties governed by coupled mechanisms spanning constituents, plies, laminates, structures, and manufacturing history. This intrinsic complexity makes predictive modeling of composites expensive, because repeated experiments and high-fidelity simulations are needed to cover large design spaces of material, structure, and manufacturing. Multi-fidelity surrogate modeling addresses this challenge by combining abundant, less expensive data with limited high-accuracy data to recover reliable high-fidelity predictions. This review presents a structured overview of multi-fidelity modeling for composite mechanics, covering Gaussian-process or Kriging-based methods, including co-Kriging, coregionalization models, autoregressive formulations, nonlinear autoregressive Gaussian processes, multi-fidelity deep Gaussian processes, and multi-fidelity neural networks. Their distinctions are examined in terms of cross-fidelity correlation, discrepancy representation, uncertainty quantification, and scalability. Selected examples of their applications to composites are introduced according to the roles that multi-fidelity surrogates play in engineering problems, including forward prediction for rapid exploration of material design spaces, inverse optimization for composite parameter identification and design search under limited high-fidelity access, and workflow integration, where heterogeneous data sources, constraints, and validation requirements determine model utility. Open question discussions highlight recurring challenges specific to composites, such as regime-dependent fidelity gaps associated with nonlinear damage and manufacturing history, mismatches between simulations and experiments, and uncertainty propagation across multi-fidelity models.
匹配关键词: autoregressive
---

[ACADEMIC - ARXIV]
标题: Visual Latents Know More Than They Say: Unsilencing Latent Reasoning in MLLMs
作者: Xin Zhang, Qiqi Tao, Jiawei Du, Moyun Liu, Joey Tianyi Zhou
链接: https://arxiv.org/abs/2605.02735v1
完整摘要: Continuous latent-space reasoning offers a compact alternative to textual chain-of-thought for multimodal models, enabling high-dimensional visual evidence to be integrated without explicit reasoning tokens. However, we identify a previously overlooked optimization pathology in existing latent visual reasoning methods: although visual latents become semantically enriched during training, their contribution to final answer prediction is systematically suppressed. Within the shared parameter space, the autoregressive objective favors shortcut reliance on direct visual input, driving latent tokens toward transition-like states rather than informative reasoning content. We term this phenomenon Silenced Visual Latents. To address it, we disentangle the two conflicting objectives by directly optimizing the latent reasoning at inference time, keeping backbone parameters frozen. In Stage I, visual latents are warmed up via query-guided contrastive latent--visual alignment, improving semantic quality while preventing latent collapse. In Stage II, the latent reasoning is further optimized via a confidence-progression reward, which incentivizes predicted token distributions along the latent span to become progressively more concentrated, routing predictions through the latent reasoning rather than bypassing it. Experiments across eight benchmarks and four model backbones show that inference-time latent optimization, without any parameter updates, effectively unleashes the suppressed reasoning capacity of visual latents.
匹配关键词: autoregressive
---

[ACADEMIC - ARXIV]
标题: ParaRNN: An Interpretable and Parallelizable Recurrent Neural Network for Time-Dependent Data
作者: Yuxi Cai, Lan Li, Feiqing Huang, Guodong Li
链接: https://arxiv.org/abs/2605.02692v1
完整摘要: The proliferation of large-scale and structurally complex data has spurred the integration of machine learning methods into statistical modeling. Recurrent neural networks (RNNs), a foundational class of models for time-dependent data, can be viewed as nonlinear extensions of classical autoregressive moving average models. Despite their flexibility and empirical success in machine learning, RNNs often suffer from limited interpretability and slow training, which hinders their use in statistics. This paper proposes the Parallelized RNN (ParaRNN), a novel model composed of multiple small recurrent units. ParaRNN admits an additive representation that decouples recurrent dynamics into interpretable components, whose behavior can be characterized through recurrence features. This interpretability enables its applications in nonparametric regression for time-dependent data, while the design also allows efficient parallelization. The approximation capacity and non-asymptotic prediction error bounds in a nonparametric regression setting are established for ParaRNN. Empirical results on three sequential modeling tasks further demonstrate that ParaRNN achieves performance comparable to vanilla RNNs while offering improved interpretability and efficiency.
匹配关键词: autoregressive
---

[ACADEMIC - ARXIV]
标题: CARD: Coarse-to-fine Autoregressive Modeling with Radix-based Decomposition for Transferable Free Energy Estimation
作者: Ziyang Yu, Yi He, Wenbing Huang, Wen Yan, Yang Liu
链接: https://arxiv.org/abs/2605.02657v1
完整摘要: Estimating free energy differences quantifies thermodynamic preferences in molecular interactions, which is central to chemistry and drug discovery. Despite fruitful progress, existing methods still face key limitations: classical computational approaches remain prohibitively expensive due to their reliance on extensive molecular dynamics simulations, while deep learning-based methods are constrained by either less-expressive generative models or input dimensions tied to a specific system, resulting in negligible generalization. To address these challenges, we propose CARD, a generative framework that employs a novel radix-based decomposition to bijectively convert 3D coordinates into mixed discrete-continuous sequences, enabling coarse-to-fine autoregressive modeling with enhanced expressiveness. Notably, the model corresponds to a distribution with zero free energy, serving as a proposal for absolute free energy computation of arbitrary systems without relying on alchemical pathways. Experiments across diverse tasks demonstrate that CARD matches the accuracy of classical computational methods on unseen systems with diverse topologies, while achieving an approximately 40-fold speedup in inference.
匹配关键词: autoregressive
---

[ACADEMIC - ARXIV]
标题: Active Sampling for Ultra-Low-Bit-Rate Video Compression via Conditional Controlled Diffusion
作者: Amirhosein Javadi, Shirin Saeedi Bidokhti, Tara Javidi
链接: https://arxiv.org/abs/2605.02849v1
完整摘要: Diffusion models provide a powerful generative prior for perceptual reconstruction at ultra-low bitrates, but effective video compression requires controlling the generative process using highly compact conditioning signals. In this work, we present ActDiff-VC, a diffusion-based video compression framework for the ultra-low-bitrate regime. Our method partitions videos into variable-length segments, transmits keyframes only when needed, and summarizes temporal dynamics using a compact set of tracked point trajectories. Conditioned on these sparse signals, a conditional diffusion decoder synthesizes the remaining frames, enabling perceptually realistic reconstruction under severe rate constraints. To support this design, we introduce two mechanisms: content-adaptive keyframe selection and budget-aware sparse trajectory selection, which together enable compact yet effective conditioning for generative reconstruction. Experiments on the UVG and MCL-JCV benchmarks show that ActDiff-VC achieves up to 64.6\% bitrate reduction at matched NIQE, improves KID by up to 64.6\% and FID by up to 37.7\% at comparable bitrates against strong learned codecs, and delivers favorable perceptual rate--distortion trade-offs relative to learned and diffusion-based baselines in the ultra-low-bitrate regime.
匹配关键词: latent diffusion
---

[ACADEMIC - ARXIV]
标题: Fine-Grained Graph Generation through Latent Mixture Scheduling
作者: Nidhi Vakil, Hadi Amiri
链接: https://arxiv.org/abs/2605.02780v1
完整摘要: Structure aware graph generation aims to generate graphs that satisfy given topological properties. It has applications in domains such as drug discovery, social network modeling, and knowledge graph construction. Unlike existing methods that only provide coarse control over graph properties, we introduce a novel conditional variational autoencoder for fine-grained structural control in graph generation. The approach refines the decoder's latent space by dynamically aligning graph- and property-driven representations to improve both graph fidelity and control satisfaction. Specifically, the approach implements a mixture scheduler that progressively integrates graph and control priors. Experiments on five real-world datasets show the efficacy of the proposed model compared to recent baselines, achieving high generation quality while maintaining high controllability.
匹配关键词: latent diffusion
---

[ACADEMIC - ARXIV]
标题: A decoupled diffusion planner that adapts to changing cost limits by using cost-conditioned generation for safety and reward gradients for performance
作者: Rufeng Chen, Zhaofan Zhang, Zhejiang Yang, Hechang Chen, Sihong Xie
链接: https://arxiv.org/abs/2605.02777v1
完整摘要: Offline safe reinforcement learning often requires policies to adapt at deployment time to safety budgets that vary across episodes or change within a single episode. While diffusion-based planners enable flexible trajectory generation, existing guidance schemes often treat reward improvement and constraint satisfaction as competing gradient objectives, which can lead to unreliable safety compliance under cost limits. We reinterpret adaptive safe trajectory generation as sampling from a constrained trajectory distribution, where the budget restricts the trajectory region, and reward shapes preferences within that region. This perspective motivates Safe Decoupled Guidance Diffusion (SDGD), which conditions classifier-free guidance on the cost limit to bias sampling toward trajectories satisfying the specified limit, while using reward-gradient guidance to refine trajectories for higher return. Because direct reward guidance can increase return while also steering samples toward trajectories with higher cumulative cost, we introduce Feasible Trajectory Relabeling (FTR) to reshape reward targets and discourage such directions. We further provide a first-order sampling-time analysis showing that FTR suppresses reward-induced cost drift under a prefix-restorative alignment condition. Extensive evaluations on the DSRL benchmark show that SDGD achieves the strongest safety compliance among baselines, satisfying the constraint on 94.7% of tasks (36/38), while obtaining the highest reward among safe methods on 21 tasks.
匹配关键词: latent diffusion
---

[ACADEMIC - ARXIV]
标题: Linearizing Vision Transformer with Test-Time Training
作者: Yining Li, Dongchen Han, Zeyu Liu, Hanyi Wang, Yulin Wang, Gao Huang
链接: https://arxiv.org/abs/2605.02772v1
完整摘要: While linear-complexity attention mechanisms offer a promising alternative to Softmax attention for overcoming the quadratic bottleneck, training such models from scratch remains prohibitively expensive. Inheriting weights from pretrained Transformers provides an appealing shortcut, yet the fundamental representational gap between Softmax and linear attention prevents effective weight transfer. In this work, we address this conversion challenge from two perspectives: architectural alignment and representational alignment. We identify Test-Time Training (TTT) as a linear-complexity architecture whose two-layer dynamic formulation is structurally aligned with Softmax attention, enabling direct inheritance of pretrained attention weights. To further align representational properties, including key shift-invariance and locality, we introduce key instance normalization and a lightweight locality enhancement module. We validate our approach by linearizing Stable Diffusion 3.5 and introduce SD3.5-T$^5$ (Transformer To Test Time Training). With only 1 hour of fine-tuning on 4$\times$H20 GPUs, SD3.5-T$^5$ achieves comparable text-to-image quality to the fine-tuned Softmax model, while accelerating inference by 1.32$\times$ and 1.47$\times$ at 1K and 2K resolutions.
匹配关键词: latent diffusion
---

[ACADEMIC - ARXIV]
标题: TOC-SR: Task-Optimal Compact diffusion for Image Super Resolution
作者: Sowmya Vajrala, Akshay Bankar, Manjunath Arveti, Shreyas Pandith, Sravanth Kodavanti, Subhajit Sanyal, Amit Unde, Srinivas Soumitri Miriyala
链接: https://arxiv.org/abs/2605.02767v1
完整摘要: Diffusion models have recently demonstrated strong performance for image restoration tasks, including super-resolution. However, their large model size and iterative sampling procedures make them computationally expensive for practical deployment. In this work, we present TOC-SR, a framework for building efficient one-step super-resolution models by first discovering a compact diffusion backbone. Starting from a sixteen-channel latent diffusion model, we construct parameter-efficient surrogate blocks using feature-wise generative distillation and perform architecture discovery using epsilon-constrained Bayesian Optimization to minimize model complexity while preserving generative fidelity. The resulting compact diffusion backbone achieves a 6.6x reduction in parameters and a 2.8x reduction in GMACs compared to the expanded diffusion model. We then adapt this backbone for super-resolution and distill the diffusion process into a single-step generator. Experiments demonstrate that the proposed approach enables efficient super-resolution while maintaining strong reconstruction quality.
匹配关键词: latent diffusion
---

[ACADEMIC - ARXIV]
标题: When Audio-Language Models Fail to Leverage Multimodal Context for Dysarthric Speech Recognition
作者: Pehuén Moure, Niclas Pokel, Bilal Bounajma, Yingqiang Gao, Roman Boehringer, Longbiao Cheng, Shih-Chii Liu
链接: https://arxiv.org/abs/2605.02782v1
完整摘要: Automatic speech recognition (ASR) systems remain brittle on dysarthric and other atypical speech. Recent audio-language models raise the possibility of improving performance by conditioning on additional clinical context at inference time, but it is unclear whether these models can make use of such information. We introduce a benchmark built on the Speech Accessibility Project (SAP) dataset that tests whether diagnosis labels, clinician-derived speech ratings, and progressively richer clinical descriptions improve transcription accuracy for dysarthric speech. Across matched comparisons on nine models, we find that current models do not meaningfully use this context: diagnosis-informed and clinically detailed prompts yield negligible improvements and often degrade word error rate. We complement the prompting analysis with context-dependent fine-tuning, showing that LoRA adaptation with a mixture of clinical prompt formats achieves a WER of 0.066, a 52% relative reduction over the frozen baseline, while preserving performance when context is unavailable. Subgroup analyses reveal significant gains for Down syndrome and mild-severity speakers. These results clarify where current models fall short and provide a testbed for measuring progress toward more inclusive ASR.
匹配关键词: multimodal
---

[ACADEMIC - ARXIV]
标题: DynoSLAM: Dynamic SLAM with Generative Graph Neural Networks for Real-World Social Navigation
作者: Danil Tokhchukov, Veronika Morozova, Gonzalo Ferrer
链接: https://arxiv.org/abs/2605.02759v1
完整摘要: Traditional Simultaneous Localization and Mapping (SLAM) algorithms rely heavily on the static environment assumption, which severely limits their applicability in real-world spaces populated by moving entities, such as pedestrians. In this work, we propose DynoSLAM, a tightly-coupled Dynamic GraphSLAM architecture that integrates socially-aware Graph Neural Networks (GNNs) directly into the factor graph optimization. Unlike conventional approaches that use rigid constant-velocity heuristics or deterministic single-agent neural priors, our framework formulates pedestrian motion forecasting as a stochastic World Model. By utilizing Monte Carlo rollouts from a trained GNN, we capture the multimodal epistemic uncertainty of human interactions and embed it into the SLAM graph via a dynamic Mahalanobis distance factor. We demonstrate through extensive simulated experiments that this stochastic formulation not only maintains highly accurate retrospective tracking but also prevents the optimization failures caused by the deterministic "argmax problem". Ultimately, extracting the empirical mean and covariance matrices of future pedestrian states provides a mathematically rigorous, probabilistic safety envelope for downstream local planners, enabling anticipatory and collision-free robot navigation in densely crowded environments.
匹配关键词: multimodal
---

[ACADEMIC - ARXIV]
标题: Virtual Scanning for NSCLC Histology: Investigating the Discriminatory Power of Synthetic PET
作者: Fatih Aksu, Laura Ciuffetti, Francesco Di Feola, Filippo Ruffini, Giulia Romoli, Fabrizia Gelardi, Arturo Chiti, Valerio Guarrasi, Paolo Soda
链接: https://arxiv.org/abs/2605.02746v1
完整摘要: Accurate histological differentiation between adenocarcinoma (ADC) and squamous cell carcinoma (SCC) is critical for personalized treatment in non-small cell lung cancer (NSCLC). While [$^{18}$F]FDG PET/CT is a standard tool for the clinical evaluation of lung cancer, its utility is often limited by high costs and radiation exposure. In this paper, we investigate the feasibility of "virtual scanning" as a feature-enhancement strategy by evaluating whether synthetic PET data can provide complementary feature representations to supplement anatomical CT scans in histological subtype classification. We propose a framework that leverages a 3D Pix2Pix Generative Adversarial Network (GAN), pretrained on the FDG-PET/CT Lesions dataset, to synthesize pseudo-PET volumes from anatomical CT scans. These synthetic volumes are integrated with structural CT data within the MINT framework, a multi-stage intermediate fusion architecture. Our experiments, conducted on a multi-center dataset of 714 subjects, demonstrate that the inclusion of synthetic metabolic features significantly improves classification performance over a CT-only baseline. The multimodal approach achieved a statistically significant increase in the Area Under the Curve (AUC) from 0.489 to 0.591 and improved the Geometric Mean (GMean) from 0.305 to 0.524. These results suggest that synthetic PET scans provide discriminatory metabolic cues that enable deep learning models to exploit complementary cross-modal information, offering a potential feature-enhancement strategy for clinical scenarios where physical PET scans are unavailable.
匹配关键词: multimodal
---

[ACADEMIC - ARXIV]
标题: Bolek: A Multimodal Language Model for Molecular Reasoning
作者: Frederic Grabowski, Jacek Szczerbiński, Maciej Jaśkowski, Kalina Jasińska-Kobus, Paweł Dąbrowski-Tumański, Tomasz Jetka, Bartosz Topolski
链接: https://arxiv.org/abs/2605.02745v1
完整摘要: Molecular property models increasingly support high-stakes drug-discovery decisions, but their outputs are often difficult to audit: classical predictors return scores without rationale, while language models can produce fluent explanations weakly grounded in the input molecule. We introduce Bolek, a compact multimodal language model that grounds natural-language reasoning in molecular structure by injecting a Morgan fingerprint embedding into an instruction-tuned text decoder. Bolek is fine-tuned on molecular alignment tasks, including molecule description, RDKit descriptor prediction, and substructure detection, and on downstream reasoning over 15 TDC binary classification tasks using synthetic chains-of-thought anchored in concrete molecular features. Across these tasks, Bolek outperforms its Qwen3-4B-Instruct base on all endpoints in yes/no mode and on 13 of 15 in chain-of-thought mode, raising mean ROC/PR AUC from 0.55 to 0.76. It also outperforms TxGemma-9B-Chat on 13 of 15 binary classification tasks despite being less than half its size. Bolek's explanations are more grounded than those of the baseline LLMs: it cites numerical descriptors 10-100x more often per chain-of-thought, and the cited values agree strongly with RDKit for key descriptors such as TPSA, MolLogP, and MolWt (Spearman rho = 0.87-0.91). Generalisation extends beyond the training panel: on 15 unseen TDC classification endpoints, Bolek matches TxGemma on five, and it produces non-trivial rank correlations on three held-out regression endpoints despite never seeing downstream regression during training. These results suggest that targeted modality injection and reasoning supervision tied to verifiable molecular features can yield compact, auditable molecular reasoning models.
匹配关键词: multimodal
---

[ACADEMIC - ARXIV]
标题: Visual Latents Know More Than They Say: Unsilencing Latent Reasoning in MLLMs
作者: Xin Zhang, Qiqi Tao, Jiawei Du, Moyun Liu, Joey Tianyi Zhou
链接: https://arxiv.org/abs/2605.02735v1
完整摘要: Continuous latent-space reasoning offers a compact alternative to textual chain-of-thought for multimodal models, enabling high-dimensional visual evidence to be integrated without explicit reasoning tokens. However, we identify a previously overlooked optimization pathology in existing latent visual reasoning methods: although visual latents become semantically enriched during training, their contribution to final answer prediction is systematically suppressed. Within the shared parameter space, the autoregressive objective favors shortcut reliance on direct visual input, driving latent tokens toward transition-like states rather than informative reasoning content. We term this phenomenon Silenced Visual Latents. To address it, we disentangle the two conflicting objectives by directly optimizing the latent reasoning at inference time, keeping backbone parameters frozen. In Stage I, visual latents are warmed up via query-guided contrastive latent--visual alignment, improving semantic quality while preventing latent collapse. In Stage II, the latent reasoning is further optimized via a confidence-progression reward, which incentivizes predicted token distributions along the latent span to become progressively more concentrated, routing predictions through the latent reasoning rather than bypassing it. Experiments across eight benchmarks and four model backbones show that inference-time latent optimization, without any parameter updates, effectively unleashes the suppressed reasoning capacity of visual latents.
匹配关键词: multimodal
---

[ACADEMIC - ARXIV]
标题: AlbumFill: Album-Guided Reasoning and Retrieval for Personalized Image Completion
作者: Yu-Ju Tsai, Brian Price, Qing Liu, Luis Figueroa, Daniil Pakhomov, Zhihong Ding, Scott Cohen, Ming-Hsuan Yang
链接: https://arxiv.org/abs/2605.02892v1
完整摘要: Personalized image completion aims to restore occluded regions in personal photos while preserving identity and appearance. Existing methods either rely on generic inpainting models that often fail to maintain identity consistency, or assume that suitable reference images are explicitly provided. In practice, suitable references are often not explicitly provided, requiring the system to search for identity-consistent images within personal photo collections. We present AlbumFill, a training-free framework that retrieves identity-consistent references from personal albums for personalized completion. Given an occluded image and a personal album, a vision-language model infers missing semantic cues to guide composed image retrieval, and the retrieved references are used by reference-based completion models. To facilitate this task, we introduce a dataset containing 54K human-centric samples with associated album images. Experiments across multiple baselines demonstrate the difficulty of personalized completion and highlight the importance of identity-consistent reference retrieval. Project Page: https://liagm.github.io/AlbumFill/
匹配关键词: vision language model
---

[ACADEMIC - ARXIV]
标题: SpecKV: Adaptive Speculative Decoding with Compression-Aware Gamma Selection
作者: Shikhar Shukla
链接: https://arxiv.org/abs/2605.02888v1
完整摘要: Speculative decoding accelerates large language model (LLM) inference by using a small draft model to propose candidate tokens that a larger target model verifies. A critical hyperparameter in this process is the speculation length~$γ$, which determines how many tokens the draft model proposes per step. Nearly all existing systems use a fixed~$γ$ (typically~4), yet empirical evidence suggests that the optimal value varies across task types and, crucially, depends on the compression level applied to the target model. In this paper, we present \textbf{SpecKV}, a lightweight adaptive controller that selects~$γ$ per speculation step using signals extracted from the draft model itself. We profile speculative decoding across 4~task categories, 4~speculation lengths, and 3~compression levels (FP16, INT8, NF4), collecting 5,112 step-level records with per-step acceptance rates, draft entropy, and draft confidence. We demonstrate that the optimal~$γ$ shifts across compression regimes and that draft model confidence and entropy are strong predictors of acceptance rate (correlation~$\approx 0.56$). SpecKV uses a small MLP trained on these signals to maximize expected tokens per speculation step, achieving a 56.0\% improvement over the fixed-$γ$=4 baseline with only 0.34\,ms overhead per decision ($<$0.5\% of step time). The improvement is statistically significant ($p < 0.001$, paired bootstrap test). We release all profiling data, trained models, and notebooks as open-source artifacts.
匹配关键词: vision language model
---

[ACADEMIC - ARXIV]
标题: MolmoAct2: Action Reasoning Models for Real-world Deployment
作者: Haoquan Fang, Jiafei Duan, Donovan Clay, Sam Wang, Shuo Liu, Weikai Huang, Xiang Fan, Wei-Chuan Tsai, Shirui Chen, Yi Ru Wang, Shanli Xing, Jaemin Cho, Jae Sung Park, Ainaz Eftekhar, Peter Sushko, Karen Farley, Angad Wadhwa, Cole Harrison, Winson Han, Ying-Chun Lee, Eli VanderBilt, Rose Hendrix, Suveen Ellawela, Lucas Ngoo, Joyce Chai, Zhongzheng Ren, Ali Farhadi, Dieter Fox, Ranjay Krishna
链接: https://arxiv.org/abs/2605.02881v1
完整摘要: Vision-Language-Action (VLA) models aim to provide a single generalist controller for robots, but today's systems fall short on the criteria that matter for real-world deployment. Frontier models are closed, open-weight alternatives are tied to expensive hardware, reasoning-augmented policies pay prohibitive latency for their grounding, and fine-tuned success rates remain below the threshold for dependable use. We present MolmoAct2, a fully open action reasoning model built for practical deployment, advancing its predecessor along five axes. We introduce MolmoER, a VLM backbone specialized for spatial and embodied reasoning, trained on a 3.3M-sample corpus with a specialize-then-rehearse recipe. We release three new datasets spanning low-to-medium cost platforms, including MolmoAct2-BimanualYAM, 720 hours of teleoperated bimanual trajectories that constitute the largest open bimanual dataset to date, together with quality-filtered Franka (DROID) and SO100/101 subsets. We provide OpenFAST, an open-weight, open-data action tokenizer trained on millions of trajectories across five embodiments. We redesign the architecture to graft a flow-matching continuous-action expert onto a discrete-token VLM via per-layer KV-cache conditioning. Finally, we propose MolmoThink, an adaptive-depth reasoning variant that re-predicts depth tokens only for scene regions that change between timesteps, retaining geometric grounding at a fraction of prior latency. In the most extensive empirical study of any open VLA to date, spanning 7 simulation and real-world benchmarks, MolmoAct2 outperforms strong baselines including Pi-05, while MolmoER surpasses GPT-5 and Gemini Robotics ER-1.5 across 13 embodied-reasoning benchmarks. We release model weights, training code, and complete training data. Project page: https://allenai.org/blog/molmoact2
匹配关键词: vision language model
---

[ACADEMIC - ARXIV]
标题: Multi-fidelity surrogates for mechanics of composites: from co-kriging to multi-fidelity neural networks
作者: Haizhou Wen, Elham Kiyani, Gang Li, Srikanth Pilla, George Em Karniadakis, Zhen Li
链接: https://arxiv.org/abs/2605.02871v1
完整摘要: Composite materials exhibit strongly hierarchical and anisotropic properties governed by coupled mechanisms spanning constituents, plies, laminates, structures, and manufacturing history. This intrinsic complexity makes predictive modeling of composites expensive, because repeated experiments and high-fidelity simulations are needed to cover large design spaces of material, structure, and manufacturing. Multi-fidelity surrogate modeling addresses this challenge by combining abundant, less expensive data with limited high-accuracy data to recover reliable high-fidelity predictions. This review presents a structured overview of multi-fidelity modeling for composite mechanics, covering Gaussian-process or Kriging-based methods, including co-Kriging, coregionalization models, autoregressive formulations, nonlinear autoregressive Gaussian processes, multi-fidelity deep Gaussian processes, and multi-fidelity neural networks. Their distinctions are examined in terms of cross-fidelity correlation, discrepancy representation, uncertainty quantification, and scalability. Selected examples of their applications to composites are introduced according to the roles that multi-fidelity surrogates play in engineering problems, including forward prediction for rapid exploration of material design spaces, inverse optimization for composite parameter identification and design search under limited high-fidelity access, and workflow integration, where heterogeneous data sources, constraints, and validation requirements determine model utility. Open question discussions highlight recurring challenges specific to composites, such as regime-dependent fidelity gaps associated with nonlinear damage and manufacturing history, mismatches between simulations and experiments, and uncertainty propagation across multi-fidelity models.
匹配关键词: vision language model
---

[ACADEMIC - ARXIV]
标题: Enhancing RL Generalizability in Robotics through SHAP Analysis of Algorithms and Hyperparameters
作者: Lingxiao Kong, Cong Yang, Oya Deniz Beyan, Zeyd Boukhers
链接: https://arxiv.org/abs/2605.02867v1
完整摘要: Despite significant advances in Reinforcement Learning (RL), model performance remains highly sensitive to algorithm and hyperparameter configurations, while generalization gaps across environments complicate real-world deployment. Although prior work has studied RL generalization, the relative contribution of specific configurations to the generalization gap has not been quantitatively decomposed and systematically leveraged for configuration selection. To address this limitation, we propose an explainable framework that evaluates RL performance across robotic environments using SHapley Additive exPlanations (SHAP) to quantify configuration impacts. We establish a theoretical foundation connecting Shapley values to generalizability, empirically analyze configuration impact patterns, and introduce SHAP-guided configuration selection to enhance generalization. Our results reveal distinct patterns across algorithms and hyperparameters, with consistent configuration impacts across diverse tasks and environments. By applying these insights to configuration selection, we achieve improved RL generalizability and provide actionable guidance for practitioners.
匹配关键词: vision language model
---

[ACADEMIC - ARXIV]
标题: MolmoAct2: Action Reasoning Models for Real-world Deployment
作者: Haoquan Fang, Jiafei Duan, Donovan Clay, Sam Wang, Shuo Liu, Weikai Huang, Xiang Fan, Wei-Chuan Tsai, Shirui Chen, Yi Ru Wang, Shanli Xing, Jaemin Cho, Jae Sung Park, Ainaz Eftekhar, Peter Sushko, Karen Farley, Angad Wadhwa, Cole Harrison, Winson Han, Ying-Chun Lee, Eli VanderBilt, Rose Hendrix, Suveen Ellawela, Lucas Ngoo, Joyce Chai, Zhongzheng Ren, Ali Farhadi, Dieter Fox, Ranjay Krishna
链接: https://arxiv.org/abs/2605.02881v1
完整摘要: Vision-Language-Action (VLA) models aim to provide a single generalist controller for robots, but today's systems fall short on the criteria that matter for real-world deployment. Frontier models are closed, open-weight alternatives are tied to expensive hardware, reasoning-augmented policies pay prohibitive latency for their grounding, and fine-tuned success rates remain below the threshold for dependable use. We present MolmoAct2, a fully open action reasoning model built for practical deployment, advancing its predecessor along five axes. We introduce MolmoER, a VLM backbone specialized for spatial and embodied reasoning, trained on a 3.3M-sample corpus with a specialize-then-rehearse recipe. We release three new datasets spanning low-to-medium cost platforms, including MolmoAct2-BimanualYAM, 720 hours of teleoperated bimanual trajectories that constitute the largest open bimanual dataset to date, together with quality-filtered Franka (DROID) and SO100/101 subsets. We provide OpenFAST, an open-weight, open-data action tokenizer trained on millions of trajectories across five embodiments. We redesign the architecture to graft a flow-matching continuous-action expert onto a discrete-token VLM via per-layer KV-cache conditioning. Finally, we propose MolmoThink, an adaptive-depth reasoning variant that re-predicts depth tokens only for scene regions that change between timesteps, retaining geometric grounding at a fraction of prior latency. In the most extensive empirical study of any open VLA to date, spanning 7 simulation and real-world benchmarks, MolmoAct2 outperforms strong baselines including Pi-05, while MolmoER surpasses GPT-5 and Gemini Robotics ER-1.5 across 13 embodied-reasoning benchmarks. We release model weights, training code, and complete training data. Project page: https://allenai.org/blog/molmoact2
匹配关键词: VLM
---

[ACADEMIC - ARXIV]
标题: VideoNet: A Large-Scale Dataset for Domain-Specific Action Recognition
作者: Tanush Yadav, Mohammadreza Salehi, Jae Sung Park, Vivek Ramanujan, Hannaneh Hajishirzi, Yejin Choi, Ali Farhadi, Rohun Tripathi, Ranjay Krishna
链接: https://arxiv.org/abs/2605.02834v1
完整摘要: Videos are unique in their ability to capture actions which transcend multiple frames. Accordingly, for many years action recognition was the quintessential task for video understanding. Unfortunately, due to a lack of sufficiently diverse and challenging data, modern vision-language models (VLMs) are no longer evaluated on their action recognition capabilities. To revitalize action recognition in the era of VLMs, we advocate for a returned focus on domain-specific actions. To this end, we introduce VideoNet, a domain-specific action recognition benchmark covering 1,000 distinct actions from 37 domains. We begin with a multiple-choice evaluation setting, where the difference between closed and open models is stark: Gemini 3.1 Pro attains 69.9% accuracy while Qwen3-VL-8B gets a mere 45.0%. To understand why VLMs struggle on VideoNet, we relax the questions into a binary setting, where random chance is 50%. Still, Qwen achieves only 59.2% accuracy. Further relaxing the evaluation setup, we provide $k\in\{1,2,3\}$ in-context examples of the action. Some models excel in the few-shot setting, while others falter; Qwen improves $+7.0\%$, while Gemini declines $-4.8\%$. Notably, these gains fall short of the $+13.6\%$ improvement in non-expert humans when given few-shot examples. Finding that VLMs struggle to fully exploit in-context examples, we shift from test-time improvements to the training side. We collect the first large-scale training dataset for domain-specific actions, totaling nearly 500k video question-answer pairs. Fine-tuning a Molmo2-4B model on our data, we surpass all open-weight 8B models on the VideoNet benchmark.
匹配关键词: VLM
---

[ACADEMIC - ARXIV]
标题: Latent Bridge: Feature Delta Prediction for Efficient Dual-System Vision-Language-Action Model Inference
作者: Yudong Liu, Yuan Li, Zijia Tang, Yuxi Zheng, Yueqian Lin, Qinsi Wang, Yi Li, Shuangjun Liu, Shuai Zhang, Taotao Jing, Dashan Gao, Ning Bi, Jingwei Sun, Yiran Chen, Hai Li
链接: https://arxiv.org/abs/2605.02739v1
完整摘要: Dual-system Vision-Language-Action (VLA) models achieve state-of-the-art robotic manipulation but are bottlenecked by the VLM backbone, which must execute at every control step while producing temporally redundant features. We propose Latent Bridge, a lightweight model that predicts VLM output deltas between timesteps, enabling the action head to operate on predicted outputs while the expensive VLM backbone is called only periodically. We instantiate Latent Bridge on two architecturally distinct VLAs: GR00T-N1.6 (feature-space bridge) and π0.5 (KV-cache bridge), demonstrating that the approach generalizes across VLA designs. Our task-agnostic DAgger training pipeline transfers across benchmarks without modification. Across four LIBERO suites, 24 RoboCasa kitchen tasks, and the ALOHA sim transfer-cube task, Latent Bridge achieves 95-100% performance retention while reducing VLM calls by 50-75%, yielding 1.65-1.73x net per-episode speedup.
匹配关键词: VLM
---

[ACADEMIC - ARXIV]
标题: AutoFocus: Uncertainty-Aware Active Visual Search for GUI Grounding
作者: Ruilin Yao, Shegnwu Xiong, Tianyu Zou, Shili Xiong, Yi Rong
链接: https://arxiv.org/abs/2605.02630v1
完整摘要: Vision-Language Models (VLMs) have enabled autonomous GUI agents that translate natural language instructions into executable screen coordinates. However, grounding performance degrades in high-resolution interfaces, where dense layouts and small interactive elements expose a resolution gap between modern displays and model input constraints. Existing zoom-in strategies rely on fixed anchors, heuristic grids, or reinforcement learning, lacking a principled mechanism to adaptively determine where refinement is needed and how much spatial uncertainty should be explored. We propose AutoFocus, a training-free, uncertainty-aware active visual search framework for GUI grounding. Our key insight is that token-level perplexity in coordinate generation naturally reflects spatial uncertainty. Rather than committing to a single prediction, AutoFocus samples multiple coordinate hypotheses and converts their axial perplexities into an anisotropic gaussian spatial probability field, explicitly modeling directional uncertainty. Based on this field, we generate global and local region proposals and introduce Shape-Aware Zooming to balance tight localization with contextual preservation. A visual prompt-based aggregation step then selects the most consistent prediction via structured comparison. Extensive experiments on ScreenSpot-Pro and ScreenSpot-V2 demonstrate consistent improvements across both general-purpose and GUI-specialized VLMs.
匹配关键词: VLM
---

[ACADEMIC - ARXIV]
标题: CoRAL: Contact-Rich Adaptive LLM-based Control for Robotic Manipulation
作者: Berk Çiçek, Mert K. Er, Özgür S. Öğüz
链接: https://arxiv.org/abs/2605.02600v1
完整摘要: While Large Language Models (LLMs) and Vision-Language Models (VLMs) demonstrate remarkable capabilities in high-level reasoning and semantic understanding, applying them directly to contact-rich manipulation remains a challenge due to their lack of explicit physical grounding and inability to perform adaptive control. To bridge this gap, we propose CoRAL (Contact-Rich Adaptive LLM-based control), a modular framework that enables zero-shot planning by decoupling high-level reasoning from low-level control. Unlike black-box policies, CoRAL uses LLMs not as direct controllers, but as cost designers that synthesize context-aware objective functions for a sampling-based motion planner (MPPI). To address the ambiguity of physical parameters in visual data, we introduce a neuro-symbolic adaptation loop: a VLM provides semantic priors for environmental dynamics, such as mass and friction estimates, which are then explicitly refined in real time via online system identification, while the LLM iteratively modulates the cost-function structure to correct strategic errors based on interaction feedback. Furthermore, a retrieval-based memory unit allows the system to reuse successful strategies across recurrent tasks. This hierarchical architecture ensures real-time control stability by decoupling high-level semantic reasoning from reactive execution, effectively bridging the gap between slow LLM inference and dynamic contact requirements. We validate CoRAL on both simulation and real-world hardware across challenging and novel tasks, such as flipping objects against walls by leveraging extrinsic contacts. Experiments demonstrate that CoRAL outperforms state-of-the-art VLA and foundation-model-based planner baselines by boosting success rates over 50% on average in unseen contact-rich scenarios, effectively handling sim-to-real gaps through its adaptive physical understanding.
匹配关键词: VLM
---

[ACADEMIC - ARXIV]
标题: AlbumFill: Album-Guided Reasoning and Retrieval for Personalized Image Completion
作者: Yu-Ju Tsai, Brian Price, Qing Liu, Luis Figueroa, Daniil Pakhomov, Zhihong Ding, Scott Cohen, Ming-Hsuan Yang
链接: https://arxiv.org/abs/2605.02892v1
完整摘要: Personalized image completion aims to restore occluded regions in personal photos while preserving identity and appearance. Existing methods either rely on generic inpainting models that often fail to maintain identity consistency, or assume that suitable reference images are explicitly provided. In practice, suitable references are often not explicitly provided, requiring the system to search for identity-consistent images within personal photo collections. We present AlbumFill, a training-free framework that retrieves identity-consistent references from personal albums for personalized completion. Given an occluded image and a personal album, a vision-language model infers missing semantic cues to guide composed image retrieval, and the retrieved references are used by reference-based completion models. To facilitate this task, we introduce a dataset containing 54K human-centric samples with associated album images. Experiments across multiple baselines demonstrate the difficulty of personalized completion and highlight the importance of identity-consistent reference retrieval. Project Page: https://liagm.github.io/AlbumFill/
匹配关键词: image generation
---

[ACADEMIC - ARXIV]
标题: Enhancing RL Generalizability in Robotics through SHAP Analysis of Algorithms and Hyperparameters
作者: Lingxiao Kong, Cong Yang, Oya Deniz Beyan, Zeyd Boukhers
链接: https://arxiv.org/abs/2605.02867v1
完整摘要: Despite significant advances in Reinforcement Learning (RL), model performance remains highly sensitive to algorithm and hyperparameter configurations, while generalization gaps across environments complicate real-world deployment. Although prior work has studied RL generalization, the relative contribution of specific configurations to the generalization gap has not been quantitatively decomposed and systematically leveraged for configuration selection. To address this limitation, we propose an explainable framework that evaluates RL performance across robotic environments using SHapley Additive exPlanations (SHAP) to quantify configuration impacts. We establish a theoretical foundation connecting Shapley values to generalizability, empirically analyze configuration impact patterns, and introduce SHAP-guided configuration selection to enhance generalization. Our results reveal distinct patterns across algorithms and hyperparameters, with consistent configuration impacts across diverse tasks and environments. By applying these insights to configuration selection, we achieve improved RL generalizability and provide actionable guidance for practitioners.
匹配关键词: image generation
---

[ACADEMIC - ARXIV]
标题: Laplacian Frequency Interaction Network for Rural Thematic Road Extraction
作者: Baiyan Chen, Weixin Zhai
链接: https://arxiv.org/abs/2605.02866v1
完整摘要: Rural thematic road network construction aims to extract topological road structures from movement trajectory images of agricultural machinery. However, this task faces challenges where downsampling methods commonly used in existing studies tend to blur the sparse high-frequency road structures, and the heavy noise from dense field operations often leads to fragmented or redundant topologies in the extracted networks. To address these challenges, we propose LFINet, a Laplacian Frequency Interaction Network. The network begins with a Laplacian Multi-scale Separator (LMS) to decouple the image into low-frequency semantic contexts and high-frequency structural details. These components are then processed by the Cross-Frequency Interaction Block (CFIB) through a dual-pathway architecture in which a High-Frequency Block (HFB) refines local structures while a Spatial Transformer (ST) captures global semantics. Subsequently, a Frequency Gated Modulation (FGM) mechanism integrates the features from pathways by leveraging semantic contexts to calibrate the structural details. Finally, a Progressive Reconstruction Decoder iteratively fuses multi-scale features to ensure topological consistency. Experiments conducted on a real-world agricultural trajectories dataset from Henan Province, China, show that LFINet establishes a new state-of-the-art. Specifically, it achieves an F1-score of 92.54% and an IoU of 86.12%, surpassing the second-ranked method by 0.64% and 1.1%, respectively. This confirms its capability to effectively construct topological road networks from noisy and sparse field data.
匹配关键词: image generation
---

[ACADEMIC - ARXIV]
标题: Pixel Perfect: Relational Image Quality Assessment with Spatially-Aware Distortions
作者: Fadeel Sher Khan, Long N. Le, Abhinau K. Venkataramanan, Seok-Jun Lee, Hamid R. Sheikh
链接: https://arxiv.org/abs/2605.02863v1
完整摘要: Traditional image quality assessment (IQA) methods rely on mean opinion scores (MOS), which are resource-intensive to collect and fail to provide interpretable, localized feedback on specific image distortions. We overcome these limitations by shifting from absolute quality prediction to a relational and directional assessment. Our approach utilizes a self-supervised synthetic distortion engine to generate training data, eliminating the need for manual annotation. A distortion prediction network is trained with an anti-symmetric objective to produce spatially-aware, disentangled maps that identify the type, intensity, and direction of distortions relative to a reference image. Subsequently, a scoring network is trained via contrastive learning on ordinally ranked image sets to predict a relational quality score. Our method provides a more granular and interpretable approach to IQA for the targeted optimization of image processing algorithms without requiring any human-labeled quality scores.
匹配关键词: image generation
---

[ACADEMIC - ARXIV]
标题: Standing on the Shoulders of Giants: Stabilized Knowledge Distillation for Cross--Language Code Clone Detection
作者: Mohamad Khajezade, Fatemeh H. Fard, Mohamed Sami Shehata
链接: https://arxiv.org/abs/2605.02860v1
完整摘要: Cross-language code clone detection (X-CCD) is challenging because semantically equivalent programs written in different languages often share little surface similarity. Although large language models (LLMs) have shown promise for semantic clone detection, their use as black-box systems raises concerns about cost, reproducibility, privacy, and unreliable output formatting. In particular, compact open-source models often struggle to follow reasoning-oriented prompts and to produce outputs that can be consistently mapped to binary clone labels. To address these limitations, we propose a knowledge distillation framework that transfers reasoning capabilities from DeepSeek-R1 into compact open-source student models for X-CCD. Using cross-language code pairs derived from Project CodeNet, we construct reasoning-oriented synthetic training data and fine-tune Phi3 and Qwen-Coder with LoRA adapters. We further introduce response stabilization methods, including forced conclusion prompting, a binary classification head, and a contrastive classification head, and evaluate model behavior using both predictive metrics and response rate. Experiments on Python--Java, Rust--Java, Rust--Python, and Rust--Ruby show that knowledge distillation consistently improves the reliability of compact models and often improves predictive performance, especially under distribution shift. In addition, classification-head variants substantially reduce inference time compared to generation-based inference. Overall, our results show that reasoning-oriented distillation combined with response stabilization makes compact open-source models more practical and reliable for X-CCD detection.
匹配关键词: image generation
---

[ACADEMIC - ARXIV]
标题: AlbumFill: Album-Guided Reasoning and Retrieval for Personalized Image Completion
作者: Yu-Ju Tsai, Brian Price, Qing Liu, Luis Figueroa, Daniil Pakhomov, Zhihong Ding, Scott Cohen, Ming-Hsuan Yang
链接: https://arxiv.org/abs/2605.02892v1
完整摘要: Personalized image completion aims to restore occluded regions in personal photos while preserving identity and appearance. Existing methods either rely on generic inpainting models that often fail to maintain identity consistency, or assume that suitable reference images are explicitly provided. In practice, suitable references are often not explicitly provided, requiring the system to search for identity-consistent images within personal photo collections. We present AlbumFill, a training-free framework that retrieves identity-consistent references from personal albums for personalized completion. Given an occluded image and a personal album, a vision-language model infers missing semantic cues to guide composed image retrieval, and the retrieved references are used by reference-based completion models. To facilitate this task, we introduce a dataset containing 54K human-centric samples with associated album images. Experiments across multiple baselines demonstrate the difficulty of personalized completion and highlight the importance of identity-consistent reference retrieval. Project Page: https://liagm.github.io/AlbumFill/
匹配关键词: video generation
---

[ACADEMIC - ARXIV]
标题: Enhancing RL Generalizability in Robotics through SHAP Analysis of Algorithms and Hyperparameters
作者: Lingxiao Kong, Cong Yang, Oya Deniz Beyan, Zeyd Boukhers
链接: https://arxiv.org/abs/2605.02867v1
完整摘要: Despite significant advances in Reinforcement Learning (RL), model performance remains highly sensitive to algorithm and hyperparameter configurations, while generalization gaps across environments complicate real-world deployment. Although prior work has studied RL generalization, the relative contribution of specific configurations to the generalization gap has not been quantitatively decomposed and systematically leveraged for configuration selection. To address this limitation, we propose an explainable framework that evaluates RL performance across robotic environments using SHapley Additive exPlanations (SHAP) to quantify configuration impacts. We establish a theoretical foundation connecting Shapley values to generalizability, empirically analyze configuration impact patterns, and introduce SHAP-guided configuration selection to enhance generalization. Our results reveal distinct patterns across algorithms and hyperparameters, with consistent configuration impacts across diverse tasks and environments. By applying these insights to configuration selection, we achieve improved RL generalizability and provide actionable guidance for practitioners.
匹配关键词: video generation
---

[ACADEMIC - ARXIV]
标题: Pixel Perfect: Relational Image Quality Assessment with Spatially-Aware Distortions
作者: Fadeel Sher Khan, Long N. Le, Abhinau K. Venkataramanan, Seok-Jun Lee, Hamid R. Sheikh
链接: https://arxiv.org/abs/2605.02863v1
完整摘要: Traditional image quality assessment (IQA) methods rely on mean opinion scores (MOS), which are resource-intensive to collect and fail to provide interpretable, localized feedback on specific image distortions. We overcome these limitations by shifting from absolute quality prediction to a relational and directional assessment. Our approach utilizes a self-supervised synthetic distortion engine to generate training data, eliminating the need for manual annotation. A distortion prediction network is trained with an anti-symmetric objective to produce spatially-aware, disentangled maps that identify the type, intensity, and direction of distortions relative to a reference image. Subsequently, a scoring network is trained via contrastive learning on ordinally ranked image sets to predict a relational quality score. Our method provides a more granular and interpretable approach to IQA for the targeted optimization of image processing algorithms without requiring any human-labeled quality scores.
匹配关键词: video generation
---

[ACADEMIC - ARXIV]
标题: Standing on the Shoulders of Giants: Stabilized Knowledge Distillation for Cross--Language Code Clone Detection
作者: Mohamad Khajezade, Fatemeh H. Fard, Mohamed Sami Shehata
链接: https://arxiv.org/abs/2605.02860v1
完整摘要: Cross-language code clone detection (X-CCD) is challenging because semantically equivalent programs written in different languages often share little surface similarity. Although large language models (LLMs) have shown promise for semantic clone detection, their use as black-box systems raises concerns about cost, reproducibility, privacy, and unreliable output formatting. In particular, compact open-source models often struggle to follow reasoning-oriented prompts and to produce outputs that can be consistently mapped to binary clone labels. To address these limitations, we propose a knowledge distillation framework that transfers reasoning capabilities from DeepSeek-R1 into compact open-source student models for X-CCD. Using cross-language code pairs derived from Project CodeNet, we construct reasoning-oriented synthetic training data and fine-tune Phi3 and Qwen-Coder with LoRA adapters. We further introduce response stabilization methods, including forced conclusion prompting, a binary classification head, and a contrastive classification head, and evaluate model behavior using both predictive metrics and response rate. Experiments on Python--Java, Rust--Java, Rust--Python, and Rust--Ruby show that knowledge distillation consistently improves the reliability of compact models and often improves predictive performance, especially under distribution shift. In addition, classification-head variants substantially reduce inference time compared to generation-based inference. Overall, our results show that reasoning-oriented distillation combined with response stabilization makes compact open-source models more practical and reliable for X-CCD detection.
匹配关键词: video generation
---

[ACADEMIC - ARXIV]
标题: From Sensors to Insight: Rapid, Edge-to-Core Application Development for Sensor-Driven Applications
作者: Komal Thareja, Anirban Mandal, Ewa Deelman
链接: https://arxiv.org/abs/2605.02859v1
完整摘要: Scientists increasingly rely on sensor-based data, yet transforming raw streams into insights across the edge-to-cloud continuum remains difficult. Provisioning heterogeneous infrastructure and managing execution on emerging platforms like Data Processing Units typically requires cross-domain expertise, creating significant barriers to rapid prototyping. This paper introduces an experience-driven methodology for the rapid development of sensor-driven applications. By combining pattern-based workflow engineering with AI-assisted development-implemented via Pegasus on the FABRIC testbed - we utilize an existing Orcasound hydrophone workflow as a reusable template. We introduce a pattern-based engineering methodology to generate and refine workflows for air quality, earthquake, and soil moisture monitoring. Furthermore, we show how these abstract structures are extended to edge resources through modular configuration and placement. Our evaluation focuses on user productivity and practical lessons rather than peak performance. Through these case studies, we illustrate how AI-assisted, pattern-based development lowers the entry barrier for non-experts and enables iterative exploration of sensor-driven applications across distributed infrastructures.
匹配关键词: video generation
---

[ACADEMIC - ARXIV]
标题: AlbumFill: Album-Guided Reasoning and Retrieval for Personalized Image Completion
作者: Yu-Ju Tsai, Brian Price, Qing Liu, Luis Figueroa, Daniil Pakhomov, Zhihong Ding, Scott Cohen, Ming-Hsuan Yang
链接: https://arxiv.org/abs/2605.02892v1
完整摘要: Personalized image completion aims to restore occluded regions in personal photos while preserving identity and appearance. Existing methods either rely on generic inpainting models that often fail to maintain identity consistency, or assume that suitable reference images are explicitly provided. In practice, suitable references are often not explicitly provided, requiring the system to search for identity-consistent images within personal photo collections. We present AlbumFill, a training-free framework that retrieves identity-consistent references from personal albums for personalized completion. Given an occluded image and a personal album, a vision-language model infers missing semantic cues to guide composed image retrieval, and the retrieved references are used by reference-based completion models. To facilitate this task, we introduce a dataset containing 54K human-centric samples with associated album images. Experiments across multiple baselines demonstrate the difficulty of personalized completion and highlight the importance of identity-consistent reference retrieval. Project Page: https://liagm.github.io/AlbumFill/
匹配关键词: visual reasoning
---

[ACADEMIC - ARXIV]
标题: MolmoAct2: Action Reasoning Models for Real-world Deployment
作者: Haoquan Fang, Jiafei Duan, Donovan Clay, Sam Wang, Shuo Liu, Weikai Huang, Xiang Fan, Wei-Chuan Tsai, Shirui Chen, Yi Ru Wang, Shanli Xing, Jaemin Cho, Jae Sung Park, Ainaz Eftekhar, Peter Sushko, Karen Farley, Angad Wadhwa, Cole Harrison, Winson Han, Ying-Chun Lee, Eli VanderBilt, Rose Hendrix, Suveen Ellawela, Lucas Ngoo, Joyce Chai, Zhongzheng Ren, Ali Farhadi, Dieter Fox, Ranjay Krishna
链接: https://arxiv.org/abs/2605.02881v1
完整摘要: Vision-Language-Action (VLA) models aim to provide a single generalist controller for robots, but today's systems fall short on the criteria that matter for real-world deployment. Frontier models are closed, open-weight alternatives are tied to expensive hardware, reasoning-augmented policies pay prohibitive latency for their grounding, and fine-tuned success rates remain below the threshold for dependable use. We present MolmoAct2, a fully open action reasoning model built for practical deployment, advancing its predecessor along five axes. We introduce MolmoER, a VLM backbone specialized for spatial and embodied reasoning, trained on a 3.3M-sample corpus with a specialize-then-rehearse recipe. We release three new datasets spanning low-to-medium cost platforms, including MolmoAct2-BimanualYAM, 720 hours of teleoperated bimanual trajectories that constitute the largest open bimanual dataset to date, together with quality-filtered Franka (DROID) and SO100/101 subsets. We provide OpenFAST, an open-weight, open-data action tokenizer trained on millions of trajectories across five embodiments. We redesign the architecture to graft a flow-matching continuous-action expert onto a discrete-token VLM via per-layer KV-cache conditioning. Finally, we propose MolmoThink, an adaptive-depth reasoning variant that re-predicts depth tokens only for scene regions that change between timesteps, retaining geometric grounding at a fraction of prior latency. In the most extensive empirical study of any open VLA to date, spanning 7 simulation and real-world benchmarks, MolmoAct2 outperforms strong baselines including Pi-05, while MolmoER surpasses GPT-5 and Gemini Robotics ER-1.5 across 13 embodied-reasoning benchmarks. We release model weights, training code, and complete training data. Project page: https://allenai.org/blog/molmoact2
匹配关键词: visual reasoning
---

[ACADEMIC - ARXIV]
标题: Semantic Risk-Aware Heuristic Planning for Robotic Navigation in Dynamic Environments: An LLM-Inspired Approach
作者: Hamza Ahmed Durrani, Rafay Suleman Durrani
链接: https://arxiv.org/abs/2605.02862v1
完整摘要: The integration of Large Language Model (LLM) reasoning principles into classical robot path planning represents a rapidly emerging research direction. In this paper, we propose a Semantic Risk-Aware Heuristic (SRAH) planner that encodes LLM-inspired cost functions penalising geometrically cluttered or high-risk zones into an A$^*$ search framework, augmented with closed-loop replanning upon dynamic obstacle detection. We evaluate SRAH against two established baselines Breadth-First Search (BFS) with replanning and a Greedy heuristic without replanning across 200 randomised trials in a $15{\times}15$ grid-world with 20\% static obstacle density and stochastic dynamic obstacles. SRAH achieves a task success rate of 62.0\%, outperforming BFS (56.5\%) by 9.7\% relative improvement and Greedy (4.0\%) by a large margin. We further analyse the trade-off between planning overhead, path efficiency, and failure-recovery count, and demonstrate via an obstacle-density ablation that semantic cost shaping consistently improves navigation across environments of varying difficulty. Our results suggest that even lightweight, LLM-inspired heuristics provide measurable safety and robustness gains for autonomous robot navigation.
匹配关键词: visual reasoning
---

[ACADEMIC - ARXIV]
标题: Standing on the Shoulders of Giants: Stabilized Knowledge Distillation for Cross--Language Code Clone Detection
作者: Mohamad Khajezade, Fatemeh H. Fard, Mohamed Sami Shehata
链接: https://arxiv.org/abs/2605.02860v1
完整摘要: Cross-language code clone detection (X-CCD) is challenging because semantically equivalent programs written in different languages often share little surface similarity. Although large language models (LLMs) have shown promise for semantic clone detection, their use as black-box systems raises concerns about cost, reproducibility, privacy, and unreliable output formatting. In particular, compact open-source models often struggle to follow reasoning-oriented prompts and to produce outputs that can be consistently mapped to binary clone labels. To address these limitations, we propose a knowledge distillation framework that transfers reasoning capabilities from DeepSeek-R1 into compact open-source student models for X-CCD. Using cross-language code pairs derived from Project CodeNet, we construct reasoning-oriented synthetic training data and fine-tune Phi3 and Qwen-Coder with LoRA adapters. We further introduce response stabilization methods, including forced conclusion prompting, a binary classification head, and a contrastive classification head, and evaluate model behavior using both predictive metrics and response rate. Experiments on Python--Java, Rust--Java, Rust--Python, and Rust--Ruby show that knowledge distillation consistently improves the reliability of compact models and often improves predictive performance, especially under distribution shift. In addition, classification-head variants substantially reduce inference time compared to generation-based inference. Overall, our results show that reasoning-oriented distillation combined with response stabilization makes compact open-source models more practical and reliable for X-CCD detection.
匹配关键词: visual reasoning
---

[ACADEMIC - ARXIV]
标题: SCPRM: A Schema-aware Cumulative Process Reward Model for Knowledge Graph Question Answering
作者: Jiujiu Chen, Yazheng Liu, Sihong Xie, Hui Xiong
链接: https://arxiv.org/abs/2605.02819v1
完整摘要: Large language models excel at complex reasoning, yet evaluating their intermediate steps remains challenging. Although process reward models provide step-wise supervision, they often suffer from a risk compensation effect, where incorrect steps are offset by later correct ones, assigning high rewards to flawed reasoning paths. This issue is further exacerbated in knowledge graph (KG) reasoning, as there may exist multiple paths between the start and end entities in the KGs, and a risky step can make the reasoning path flawed. Those limitations are problematic in risk-sensitive tasks such as medical and legal KG reasoning. To address the issues, we propose a Schema-aware Cumulative Process Reward Model (SCPRM) that evaluates reasoning paths by conditioning on the reasoning prefix , and incorporating schema distance between current reasoning step and the implicit target parsed from the query, which provides cumulative and future rewards to guide the path explorations. We further integrate SCPRM into Monte Carlo Tree Search (MCTS) as SCPRM-MCTS to conduct multi-hop reasoning on KGs for question answering (QA) tasks. Across medical and legal KGQA and CWQ, SCPRM-MCTS improves the performance of Hits@k by an average of 1.18% over strong baselines, demonstrating more accurate and risk-sensitive reasoning evaluation.
匹配关键词: visual reasoning
---

[ACADEMIC - ARXIV]
标题: MolmoAct2: Action Reasoning Models for Real-world Deployment
作者: Haoquan Fang, Jiafei Duan, Donovan Clay, Sam Wang, Shuo Liu, Weikai Huang, Xiang Fan, Wei-Chuan Tsai, Shirui Chen, Yi Ru Wang, Shanli Xing, Jaemin Cho, Jae Sung Park, Ainaz Eftekhar, Peter Sushko, Karen Farley, Angad Wadhwa, Cole Harrison, Winson Han, Ying-Chun Lee, Eli VanderBilt, Rose Hendrix, Suveen Ellawela, Lucas Ngoo, Joyce Chai, Zhongzheng Ren, Ali Farhadi, Dieter Fox, Ranjay Krishna
链接: https://arxiv.org/abs/2605.02881v1
完整摘要: Vision-Language-Action (VLA) models aim to provide a single generalist controller for robots, but today's systems fall short on the criteria that matter for real-world deployment. Frontier models are closed, open-weight alternatives are tied to expensive hardware, reasoning-augmented policies pay prohibitive latency for their grounding, and fine-tuned success rates remain below the threshold for dependable use. We present MolmoAct2, a fully open action reasoning model built for practical deployment, advancing its predecessor along five axes. We introduce MolmoER, a VLM backbone specialized for spatial and embodied reasoning, trained on a 3.3M-sample corpus with a specialize-then-rehearse recipe. We release three new datasets spanning low-to-medium cost platforms, including MolmoAct2-BimanualYAM, 720 hours of teleoperated bimanual trajectories that constitute the largest open bimanual dataset to date, together with quality-filtered Franka (DROID) and SO100/101 subsets. We provide OpenFAST, an open-weight, open-data action tokenizer trained on millions of trajectories across five embodiments. We redesign the architecture to graft a flow-matching continuous-action expert onto a discrete-token VLM via per-layer KV-cache conditioning. Finally, we propose MolmoThink, an adaptive-depth reasoning variant that re-predicts depth tokens only for scene regions that change between timesteps, retaining geometric grounding at a fraction of prior latency. In the most extensive empirical study of any open VLA to date, spanning 7 simulation and real-world benchmarks, MolmoAct2 outperforms strong baselines including Pi-05, while MolmoER surpasses GPT-5 and Gemini Robotics ER-1.5 across 13 embodied-reasoning benchmarks. We release model weights, training code, and complete training data. Project page: https://allenai.org/blog/molmoact2
匹配关键词: embodied AI
---

[ACADEMIC - ARXIV]
标题: From Sensors to Insight: Rapid, Edge-to-Core Application Development for Sensor-Driven Applications
作者: Komal Thareja, Anirban Mandal, Ewa Deelman
链接: https://arxiv.org/abs/2605.02859v1
完整摘要: Scientists increasingly rely on sensor-based data, yet transforming raw streams into insights across the edge-to-cloud continuum remains difficult. Provisioning heterogeneous infrastructure and managing execution on emerging platforms like Data Processing Units typically requires cross-domain expertise, creating significant barriers to rapid prototyping. This paper introduces an experience-driven methodology for the rapid development of sensor-driven applications. By combining pattern-based workflow engineering with AI-assisted development-implemented via Pegasus on the FABRIC testbed - we utilize an existing Orcasound hydrophone workflow as a reusable template. We introduce a pattern-based engineering methodology to generate and refine workflows for air quality, earthquake, and soil moisture monitoring. Furthermore, we show how these abstract structures are extended to edge resources through modular configuration and placement. Our evaluation focuses on user productivity and practical lessons rather than peak performance. Through these case studies, we illustrate how AI-assisted, pattern-based development lowers the entry barrier for non-experts and enables iterative exploration of sensor-driven applications across distributed infrastructures.
匹配关键词: embodied AI
---

[ACADEMIC - ARXIV]
标题: (POSTER) From Sensors to Insight: Rapid, Edge-to-Core Application Development for Sensor-Driven Applications
作者: Komal Thareja, Anirban Mandal, Ewa Deelman
链接: https://arxiv.org/abs/2605.02844v1
完整摘要: Scientists increasingly rely on sensor-based data; however transforming raw streams into insights across the edge-to-cloud continuum remains difficult due to the breadth of expertise required to coordinate the necessary data and computation flow. This paper introduces a pattern-based, AI-assisted methodology for rapid development of sensor-driven applications. Using Pegasus workflows executing on the FABRIC testbed, we demonstrate a 5-step development loop that shifts workflow construction and deployment from code-first to intent-first design. Starting from an existing Orcasound hydrophone workflow as a reusable template, we generate and refine workflows for air quality, earthquake, and soil moisture monitoring applications. We further show how these workflows extend to edge resources-including BlueField-3 DPUs and Raspberry Pis-through configuration and placement rather than workflow redesign. Our evaluation, from the perspective of a novice Pegasus user, shows that AI-assisted pattern reuse compresses multi-stage workflow development to 1-1.5 days per workflow while preserving the rigor and portability of workflow-based execution.
匹配关键词: embodied AI
---

[ACADEMIC - ARXIV]
标题: HAAS: A Policy-Aware Framework for Adaptive Task Allocation Between Humans and Artificial Intelligence Systems
作者: Vicente Pelechanoa, Antoni Mestre, Manoli Albert, Miriam Gil
链接: https://arxiv.org/abs/2605.02832v1
完整摘要: Deciding how to distribute work between humans and AI systems is a central challenge in organisational design. Most approaches treat this as a binary choice, yet the operational reality is richer: humans and AI routinely share tasks or take complementary roles depending on context, fatigue, and the stakes involved. Governing that distribution -- balancing efficiency, oversight, and human capability -- remains an open problem. This paper presents Human-AI Adaptive Symbiosis (HAAS), an implemented framework for adaptive task allocation in software engineering and manufacturing. HAAS combines two coupled components: a rule-based expert system that enforces governance constraints before any learning occurs, and a contextual-bandit learner that selects among feasible collaboration modes from outcome feedback. Task-agent fit is represented through five auditable cognitive dimensions and a five-mode autonomy spectrum -- from human-only to fully autonomous -- embedded in a reproducible benchmark spanning both domains. Three empirical findings emerge. First, governance is not a binary switch but a tunable design variable: tighter constraints predictably convert autonomous AI assignments into supervised collaborations, with domain-specific costs and benefits. Second, in manufacturing, stronger governance can improve operational performance and reduce fatigue simultaneously -- a workload-buffering effect that contradicts the usual framing of governance as pure overhead. Third, no single governance setting dominates across all contexts; moderate governance becomes increasingly competitive as the learner accumulates experience within the governed action space. Together, these findings position HAAS as a pre-deployment workbench for comparing and inspecting human--AI allocation policies before organisational commitment.
匹配关键词: embodied AI
---

[ACADEMIC - ARXIV]
标题: AIs and Humans with Agency
作者: David Mumford
链接: https://arxiv.org/abs/2605.02810v1
完整摘要: This paper compares agency in humans with potential agency in AI programs. Human agency takes many years to develop, as the frontal lobe is activated. Early attempts to endow LLMs agency have met serious obstacles. Progress requires a new architecture where actions and plans are formulated jointly with the human actors in each real world setting.
匹配关键词: embodied AI
---

[ACADEMIC - ARXIV]
标题: MolmoAct2: Action Reasoning Models for Real-world Deployment
作者: Haoquan Fang, Jiafei Duan, Donovan Clay, Sam Wang, Shuo Liu, Weikai Huang, Xiang Fan, Wei-Chuan Tsai, Shirui Chen, Yi Ru Wang, Shanli Xing, Jaemin Cho, Jae Sung Park, Ainaz Eftekhar, Peter Sushko, Karen Farley, Angad Wadhwa, Cole Harrison, Winson Han, Ying-Chun Lee, Eli VanderBilt, Rose Hendrix, Suveen Ellawela, Lucas Ngoo, Joyce Chai, Zhongzheng Ren, Ali Farhadi, Dieter Fox, Ranjay Krishna
链接: https://arxiv.org/abs/2605.02881v1
完整摘要: Vision-Language-Action (VLA) models aim to provide a single generalist controller for robots, but today's systems fall short on the criteria that matter for real-world deployment. Frontier models are closed, open-weight alternatives are tied to expensive hardware, reasoning-augmented policies pay prohibitive latency for their grounding, and fine-tuned success rates remain below the threshold for dependable use. We present MolmoAct2, a fully open action reasoning model built for practical deployment, advancing its predecessor along five axes. We introduce MolmoER, a VLM backbone specialized for spatial and embodied reasoning, trained on a 3.3M-sample corpus with a specialize-then-rehearse recipe. We release three new datasets spanning low-to-medium cost platforms, including MolmoAct2-BimanualYAM, 720 hours of teleoperated bimanual trajectories that constitute the largest open bimanual dataset to date, together with quality-filtered Franka (DROID) and SO100/101 subsets. We provide OpenFAST, an open-weight, open-data action tokenizer trained on millions of trajectories across five embodiments. We redesign the architecture to graft a flow-matching continuous-action expert onto a discrete-token VLM via per-layer KV-cache conditioning. Finally, we propose MolmoThink, an adaptive-depth reasoning variant that re-predicts depth tokens only for scene regions that change between timesteps, retaining geometric grounding at a fraction of prior latency. In the most extensive empirical study of any open VLA to date, spanning 7 simulation and real-world benchmarks, MolmoAct2 outperforms strong baselines including Pi-05, while MolmoER surpasses GPT-5 and Gemini Robotics ER-1.5 across 13 embodied-reasoning benchmarks. We release model weights, training code, and complete training data. Project page: https://allenai.org/blog/molmoact2
匹配关键词: robotics
---

[ACADEMIC - ARXIV]
标题: Enhancing RL Generalizability in Robotics through SHAP Analysis of Algorithms and Hyperparameters
作者: Lingxiao Kong, Cong Yang, Oya Deniz Beyan, Zeyd Boukhers
链接: https://arxiv.org/abs/2605.02867v1
完整摘要: Despite significant advances in Reinforcement Learning (RL), model performance remains highly sensitive to algorithm and hyperparameter configurations, while generalization gaps across environments complicate real-world deployment. Although prior work has studied RL generalization, the relative contribution of specific configurations to the generalization gap has not been quantitatively decomposed and systematically leveraged for configuration selection. To address this limitation, we propose an explainable framework that evaluates RL performance across robotic environments using SHapley Additive exPlanations (SHAP) to quantify configuration impacts. We establish a theoretical foundation connecting Shapley values to generalizability, empirically analyze configuration impact patterns, and introduce SHAP-guided configuration selection to enhance generalization. Our results reveal distinct patterns across algorithms and hyperparameters, with consistent configuration impacts across diverse tasks and environments. By applying these insights to configuration selection, we achieve improved RL generalizability and provide actionable guidance for practitioners.
匹配关键词: robotics
---

[ACADEMIC - ARXIV]
标题: Semantic Risk-Aware Heuristic Planning for Robotic Navigation in Dynamic Environments: An LLM-Inspired Approach
作者: Hamza Ahmed Durrani, Rafay Suleman Durrani
链接: https://arxiv.org/abs/2605.02862v1
完整摘要: The integration of Large Language Model (LLM) reasoning principles into classical robot path planning represents a rapidly emerging research direction. In this paper, we propose a Semantic Risk-Aware Heuristic (SRAH) planner that encodes LLM-inspired cost functions penalising geometrically cluttered or high-risk zones into an A$^*$ search framework, augmented with closed-loop replanning upon dynamic obstacle detection. We evaluate SRAH against two established baselines Breadth-First Search (BFS) with replanning and a Greedy heuristic without replanning across 200 randomised trials in a $15{\times}15$ grid-world with 20\% static obstacle density and stochastic dynamic obstacles. SRAH achieves a task success rate of 62.0\%, outperforming BFS (56.5\%) by 9.7\% relative improvement and Greedy (4.0\%) by a large margin. We further analyse the trade-off between planning overhead, path efficiency, and failure-recovery count, and demonstrate via an obstacle-density ablation that semantic cost shaping consistently improves navigation across environments of varying difficulty. Our results suggest that even lightweight, LLM-inspired heuristics provide measurable safety and robustness gains for autonomous robot navigation.
匹配关键词: robotics
---

[ACADEMIC - ARXIV]
标题: LiDAR Teach, Radar Repeat: Robust Cross-Modal Navigation in Degenerate and Varying Environments
作者: Renxiang Xiao, Yichen Chen, Yuanfan Zhang, Qianyi Shao, Yushuai Chen, Yuxuan Han, Yunjiang Lou, Liang Hu
链接: https://arxiv.org/abs/2605.02809v1
完整摘要: Long-term autonomy requires robust navigation in environments subject to dynamic and static changes, as well as adverse weather conditions. Teach-and-Repeat (T\&R) navigation offers a reliable and cost-effective solution by avoiding the need for consistent global mapping; however, existing T\&R systems lack a systematic solution to tackle various environmental variations such as weather degradation, ephemeral dynamics, and structural changes. This work proposes LTR$^2$, the first cross-modal, cross-platform LiDAR-Teach-and-Radar-Repeat system that systematically addresses these challenges. LTR$^2$ leverages LiDAR during the teaching phase to capture precise structural information under normal conditions and utilizes 4D millimeter-wave radar during the repeating phase for robust operation under environmental degradations. To align sparse and noisy forward-looking 4D radar with dense and accurate omnidirectional 3D LiDAR data, we introduce a Cross-Modal Registration (CMR) network that jointly exploits Doppler-based motion priors and the physical laws governing LiDAR intensity and radar power density. Furthermore, we propose an adaptive fine-tuning strategy that incrementally updates the CMR network based on localization errors, enabling long-term adaptability to static environmental changes without ground-truth labels. We demonstrate that the proposed CMR network achieves state-of-the-art cross-modal registration performance on the open-access dataset. Then we validate LTR$^2$ across three robot platforms over a large-scale, long-term deployment (40+ km over 6 months), including challenging conditions such as nighttime smoke. Experimental results and ablation studies demonstrate centimeter-level accuracy and strong robustness against diverse environmental disturbances, significantly outperforming existing approaches.
匹配关键词: robotics
---

[ACADEMIC - ARXIV]
标题: DynoSLAM: Dynamic SLAM with Generative Graph Neural Networks for Real-World Social Navigation
作者: Danil Tokhchukov, Veronika Morozova, Gonzalo Ferrer
链接: https://arxiv.org/abs/2605.02759v1
完整摘要: Traditional Simultaneous Localization and Mapping (SLAM) algorithms rely heavily on the static environment assumption, which severely limits their applicability in real-world spaces populated by moving entities, such as pedestrians. In this work, we propose DynoSLAM, a tightly-coupled Dynamic GraphSLAM architecture that integrates socially-aware Graph Neural Networks (GNNs) directly into the factor graph optimization. Unlike conventional approaches that use rigid constant-velocity heuristics or deterministic single-agent neural priors, our framework formulates pedestrian motion forecasting as a stochastic World Model. By utilizing Monte Carlo rollouts from a trained GNN, we capture the multimodal epistemic uncertainty of human interactions and embed it into the SLAM graph via a dynamic Mahalanobis distance factor. We demonstrate through extensive simulated experiments that this stochastic formulation not only maintains highly accurate retrospective tracking but also prevents the optimization failures caused by the deterministic "argmax problem". Ultimately, extracting the empirical mean and covariance matrices of future pedestrian states provides a mathematically rigorous, probabilistic safety envelope for downstream local planners, enabling anticipatory and collision-free robot navigation in densely crowded environments.
匹配关键词: robotics
---

[ACADEMIC - ARXIV]
标题: MolmoAct2: Action Reasoning Models for Real-world Deployment
作者: Haoquan Fang, Jiafei Duan, Donovan Clay, Sam Wang, Shuo Liu, Weikai Huang, Xiang Fan, Wei-Chuan Tsai, Shirui Chen, Yi Ru Wang, Shanli Xing, Jaemin Cho, Jae Sung Park, Ainaz Eftekhar, Peter Sushko, Karen Farley, Angad Wadhwa, Cole Harrison, Winson Han, Ying-Chun Lee, Eli VanderBilt, Rose Hendrix, Suveen Ellawela, Lucas Ngoo, Joyce Chai, Zhongzheng Ren, Ali Farhadi, Dieter Fox, Ranjay Krishna
链接: https://arxiv.org/abs/2605.02881v1
完整摘要: Vision-Language-Action (VLA) models aim to provide a single generalist controller for robots, but today's systems fall short on the criteria that matter for real-world deployment. Frontier models are closed, open-weight alternatives are tied to expensive hardware, reasoning-augmented policies pay prohibitive latency for their grounding, and fine-tuned success rates remain below the threshold for dependable use. We present MolmoAct2, a fully open action reasoning model built for practical deployment, advancing its predecessor along five axes. We introduce MolmoER, a VLM backbone specialized for spatial and embodied reasoning, trained on a 3.3M-sample corpus with a specialize-then-rehearse recipe. We release three new datasets spanning low-to-medium cost platforms, including MolmoAct2-BimanualYAM, 720 hours of teleoperated bimanual trajectories that constitute the largest open bimanual dataset to date, together with quality-filtered Franka (DROID) and SO100/101 subsets. We provide OpenFAST, an open-weight, open-data action tokenizer trained on millions of trajectories across five embodiments. We redesign the architecture to graft a flow-matching continuous-action expert onto a discrete-token VLM via per-layer KV-cache conditioning. Finally, we propose MolmoThink, an adaptive-depth reasoning variant that re-predicts depth tokens only for scene regions that change between timesteps, retaining geometric grounding at a fraction of prior latency. In the most extensive empirical study of any open VLA to date, spanning 7 simulation and real-world benchmarks, MolmoAct2 outperforms strong baselines including Pi-05, while MolmoER surpasses GPT-5 and Gemini Robotics ER-1.5 across 13 embodied-reasoning benchmarks. We release model weights, training code, and complete training data. Project page: https://allenai.org/blog/molmoact2
匹配关键词: humanoid robot
---

[ACADEMIC - ARXIV]
标题: Enhancing RL Generalizability in Robotics through SHAP Analysis of Algorithms and Hyperparameters
作者: Lingxiao Kong, Cong Yang, Oya Deniz Beyan, Zeyd Boukhers
链接: https://arxiv.org/abs/2605.02867v1
完整摘要: Despite significant advances in Reinforcement Learning (RL), model performance remains highly sensitive to algorithm and hyperparameter configurations, while generalization gaps across environments complicate real-world deployment. Although prior work has studied RL generalization, the relative contribution of specific configurations to the generalization gap has not been quantitatively decomposed and systematically leveraged for configuration selection. To address this limitation, we propose an explainable framework that evaluates RL performance across robotic environments using SHapley Additive exPlanations (SHAP) to quantify configuration impacts. We establish a theoretical foundation connecting Shapley values to generalizability, empirically analyze configuration impact patterns, and introduce SHAP-guided configuration selection to enhance generalization. Our results reveal distinct patterns across algorithms and hyperparameters, with consistent configuration impacts across diverse tasks and environments. By applying these insights to configuration selection, we achieve improved RL generalizability and provide actionable guidance for practitioners.
匹配关键词: humanoid robot
---

[ACADEMIC - ARXIV]
标题: Semantic Risk-Aware Heuristic Planning for Robotic Navigation in Dynamic Environments: An LLM-Inspired Approach
作者: Hamza Ahmed Durrani, Rafay Suleman Durrani
链接: https://arxiv.org/abs/2605.02862v1
完整摘要: The integration of Large Language Model (LLM) reasoning principles into classical robot path planning represents a rapidly emerging research direction. In this paper, we propose a Semantic Risk-Aware Heuristic (SRAH) planner that encodes LLM-inspired cost functions penalising geometrically cluttered or high-risk zones into an A$^*$ search framework, augmented with closed-loop replanning upon dynamic obstacle detection. We evaluate SRAH against two established baselines Breadth-First Search (BFS) with replanning and a Greedy heuristic without replanning across 200 randomised trials in a $15{\times}15$ grid-world with 20\% static obstacle density and stochastic dynamic obstacles. SRAH achieves a task success rate of 62.0\%, outperforming BFS (56.5\%) by 9.7\% relative improvement and Greedy (4.0\%) by a large margin. We further analyse the trade-off between planning overhead, path efficiency, and failure-recovery count, and demonstrate via an obstacle-density ablation that semantic cost shaping consistently improves navigation across environments of varying difficulty. Our results suggest that even lightweight, LLM-inspired heuristics provide measurable safety and robustness gains for autonomous robot navigation.
匹配关键词: humanoid robot
---

[ACADEMIC - ARXIV]
标题: LiDAR Teach, Radar Repeat: Robust Cross-Modal Navigation in Degenerate and Varying Environments
作者: Renxiang Xiao, Yichen Chen, Yuanfan Zhang, Qianyi Shao, Yushuai Chen, Yuxuan Han, Yunjiang Lou, Liang Hu
链接: https://arxiv.org/abs/2605.02809v1
完整摘要: Long-term autonomy requires robust navigation in environments subject to dynamic and static changes, as well as adverse weather conditions. Teach-and-Repeat (T\&R) navigation offers a reliable and cost-effective solution by avoiding the need for consistent global mapping; however, existing T\&R systems lack a systematic solution to tackle various environmental variations such as weather degradation, ephemeral dynamics, and structural changes. This work proposes LTR$^2$, the first cross-modal, cross-platform LiDAR-Teach-and-Radar-Repeat system that systematically addresses these challenges. LTR$^2$ leverages LiDAR during the teaching phase to capture precise structural information under normal conditions and utilizes 4D millimeter-wave radar during the repeating phase for robust operation under environmental degradations. To align sparse and noisy forward-looking 4D radar with dense and accurate omnidirectional 3D LiDAR data, we introduce a Cross-Modal Registration (CMR) network that jointly exploits Doppler-based motion priors and the physical laws governing LiDAR intensity and radar power density. Furthermore, we propose an adaptive fine-tuning strategy that incrementally updates the CMR network based on localization errors, enabling long-term adaptability to static environmental changes without ground-truth labels. We demonstrate that the proposed CMR network achieves state-of-the-art cross-modal registration performance on the open-access dataset. Then we validate LTR$^2$ across three robot platforms over a large-scale, long-term deployment (40+ km over 6 months), including challenging conditions such as nighttime smoke. Experimental results and ablation studies demonstrate centimeter-level accuracy and strong robustness against diverse environmental disturbances, significantly outperforming existing approaches.
匹配关键词: humanoid robot
---

[ACADEMIC - ARXIV]
标题: DynoSLAM: Dynamic SLAM with Generative Graph Neural Networks for Real-World Social Navigation
作者: Danil Tokhchukov, Veronika Morozova, Gonzalo Ferrer
链接: https://arxiv.org/abs/2605.02759v1
完整摘要: Traditional Simultaneous Localization and Mapping (SLAM) algorithms rely heavily on the static environment assumption, which severely limits their applicability in real-world spaces populated by moving entities, such as pedestrians. In this work, we propose DynoSLAM, a tightly-coupled Dynamic GraphSLAM architecture that integrates socially-aware Graph Neural Networks (GNNs) directly into the factor graph optimization. Unlike conventional approaches that use rigid constant-velocity heuristics or deterministic single-agent neural priors, our framework formulates pedestrian motion forecasting as a stochastic World Model. By utilizing Monte Carlo rollouts from a trained GNN, we capture the multimodal epistemic uncertainty of human interactions and embed it into the SLAM graph via a dynamic Mahalanobis distance factor. We demonstrate through extensive simulated experiments that this stochastic formulation not only maintains highly accurate retrospective tracking but also prevents the optimization failures caused by the deterministic "argmax problem". Ultimately, extracting the empirical mean and covariance matrices of future pedestrian states provides a mathematically rigorous, probabilistic safety envelope for downstream local planners, enabling anticipatory and collision-free robot navigation in densely crowded environments.
匹配关键词: humanoid robot
---

[ACADEMIC - ARXIV]
标题: Latent Bridge: Feature Delta Prediction for Efficient Dual-System Vision-Language-Action Model Inference
作者: Yudong Liu, Yuan Li, Zijia Tang, Yuxi Zheng, Yueqian Lin, Qinsi Wang, Yi Li, Shuangjun Liu, Shuai Zhang, Taotao Jing, Dashan Gao, Ning Bi, Jingwei Sun, Yiran Chen, Hai Li
链接: https://arxiv.org/abs/2605.02739v1
完整摘要: Dual-system Vision-Language-Action (VLA) models achieve state-of-the-art robotic manipulation but are bottlenecked by the VLM backbone, which must execute at every control step while producing temporally redundant features. We propose Latent Bridge, a lightweight model that predicts VLM output deltas between timesteps, enabling the action head to operate on predicted outputs while the expensive VLM backbone is called only periodically. We instantiate Latent Bridge on two architecturally distinct VLAs: GR00T-N1.6 (feature-space bridge) and π0.5 (KV-cache bridge), demonstrating that the approach generalizes across VLA designs. Our task-agnostic DAgger training pipeline transfers across benchmarks without modification. Across four LIBERO suites, 24 RoboCasa kitchen tasks, and the ALOHA sim transfer-cube task, Latent Bridge achieves 95-100% performance retention while reducing VLM calls by 50-75%, yielding 1.65-1.73x net per-episode speedup.
匹配关键词: manipulation
---

[ACADEMIC - ARXIV]
标题: Temporally Consistent Object 6D Pose Estimation for Robot Control
作者: Kateryna Zorina, Vojtech Priban, Mederic Fourmy, Josef Sivic, Vladimir Petrik
链接: https://arxiv.org/abs/2605.02708v1
完整摘要: Single-view RGB object pose estimators have reached a level of precision and efficiency that makes them good candidates for vision-based robot control. However, off-the-shelf methods lack temporal consistency and robustness that are mandatory for a stable feedback control. In this work, we develop a factor graph approach to enforce temporal consistency of the object pose estimates. In particular, the proposed approach: (i) incorporates object motion models, (ii) explicitly estimates the object pose measurement uncertainty, and (iii) integrates the above two components in an online optimization-based estimator. We demonstrate that with appropriate outlier rejection and smoothing using the proposed factor graph approach, we can significantly improve the results on standardized pose estimation benchmarks. We experimentally validate the stability of the proposed approach for a feedback-based robot control task in which the object is tracked by the camera attached to a torque controlled manipulator.
匹配关键词: manipulation
---

[ACADEMIC - ARXIV]
标题: Learning Equivariant Neural-Augmented Object Dynamics From Few Interactions
作者: Sergio Orozco, Tushar Kusnur, Brandon May, George Konidaris, Laura Herlant
链接: https://arxiv.org/abs/2605.02699v1
完整摘要: Learning data-efficient object dynamics models for robotic manipulation remains challenging, especially for deformable objects. A popular approach is to model objects as sets of 3D particles and learn their motion using graph neural networks. In practice, this is not enough to maintain physical feasibility over long horizons and may require large amounts of interaction data to learn. We introduce PIEGraph, a novel approach to combining analytical physics and data-driven models to capture object dynamics for both rigid and deformable bodies using limited real-world interaction data. PIEGraph consists of two components: (1) a \textbf{P}hysically \textbf{I}nformed particle-based analytical model (implemented as a spring--mass system) to enforce physically feasible motion, and (2) an \textbf{E}quivariant \textbf{Graph} Neural Network with a novel action representation that exploits symmetries in particle interactions to guide the analytical model. We evaluate PIEGraph in simulation and on robot hardware for reorientation and repositioning tasks with ropes, cloth, stuffed animals and rigid objects. We show that our method enables accurate dynamics prediction and reliable downstream robotic manipulation planning, which outperforms state of the art baselines.
匹配关键词: manipulation
---

[ACADEMIC - ARXIV]
标题: AnchorD: Metric Grounding of Monocular Depth Using Factor Graphs
作者: Simon Dorer, Martin Büchner, Nick Heppert, Abhinav Valada
链接: https://arxiv.org/abs/2605.02667v1
完整摘要: Dense and accurate depth estimation is essential for robotic manipulation, grasping, and navigation, yet currently available depth sensors are prone to errors on transparent, specular, and general non-Lambertian surfaces. To mitigate these errors, large-scale monocular depth estimation approaches provide strong structural priors, but their predictions can be potentially skewed or mis-scaled in metric units, limiting their direct use in robotics. Thus, in this work, we propose a training-free depth grounding framework that anchors monocular depth estimation priors from a depth foundation model in raw sensor depth through factor graph optimization. Our method performs a patch-wise affine alignment, locally grounding monocular predictions in metric real-world depth while preserving fine-grained geometric structure and discontinuities. To facilitate evaluation in challenging real-world conditions, we introduce a benchmark dataset with dense scene-wide ground truth depth in the presence of non-Lambertian objects. Ground truth is obtained via matte reflection spray and multi-camera fusion, overcoming the reliance on object-only CAD-based annotations used in prior datasets. Extensive evaluations across diverse sensors and domains demonstrate consistent improvements in depth performance without any (re-)training. We make our implementation publicly available at https://anchord.cs.uni-freiburg.de.
匹配关键词: manipulation
---

[ACADEMIC - ARXIV]
标题: ContextualJailbreak: Evolutionary Red-Teaming via Simulated Conversational Priming
作者: Mario Rodríguez Béjar, Francisco J. Cortés-Delgado, S. Braghin, Jose L. Hernández-Ramos
链接: https://arxiv.org/abs/2605.02647v1
完整摘要: Large language models (LLMs) remain vulnerable to jailbreak attacks that bypass safety alignment and elicit harmful responses. A growing body of work shows that contextual priming, where earlier turns covertly bias later replies, constitutes a powerful attack surface, with hand-crafted multi-turn scaffolds consistently outperforming single-turn manipulations on capable models. However, automated optimization-based red-teaming has remained largely limited to the single-turn setting, iterating over static prompts and lacking the ability to reason about which forms of conversational priming induce compliance. While recent multi-turn, search-based approaches have begun to bridge this gap, the mutator design space underlying effective primed dialogues remains largely unexplored. We present ContextualJailbreak, a black-box red-teaming strategy that performs evolutionary search over a simulated multi-turn primed dialogue. The strategy leverages a graded 0-5 harm score from a two-level judge as an in-loop signal, enabling partially harmful responses to guide the search process rather than being discarded. Search is driven by five semantically defined mutation operators: roleplay, scenario, expand, troubleshooting, and mechanistic, of which the last two are novel contributions of this work. Across 50 representative HarmBench behaviors, ContextualJailbreak achieves an ASR of 100% on gpt-oss:20B, 100% on qwen3-8B, 100% on llama3.1:70B, and 90% on gpt-oss:120B, outperforming four single- and multi-turn baselines by 31-96 percentage points on average. The 40 maximally harmful attacks discovered against gpt-oss:120B transfer without adaptation to closed frontier models, achieving 90.0% on gpt-4o-mini, 70.0% on gpt-5, and 70.0% on gemini-3-flash, but only 17.5% on claude-opus-4-7 and 15.0% on claude-sonnet-4-6, revealing a pronounced provider-level asymmetry in alignment robustness.
匹配关键词: manipulation
---

[ACADEMIC - ARXIV]
标题: CoRAL: Contact-Rich Adaptive LLM-based Control for Robotic Manipulation
作者: Berk Çiçek, Mert K. Er, Özgür S. Öğüz
链接: https://arxiv.org/abs/2605.02600v1
完整摘要: While Large Language Models (LLMs) and Vision-Language Models (VLMs) demonstrate remarkable capabilities in high-level reasoning and semantic understanding, applying them directly to contact-rich manipulation remains a challenge due to their lack of explicit physical grounding and inability to perform adaptive control. To bridge this gap, we propose CoRAL (Contact-Rich Adaptive LLM-based control), a modular framework that enables zero-shot planning by decoupling high-level reasoning from low-level control. Unlike black-box policies, CoRAL uses LLMs not as direct controllers, but as cost designers that synthesize context-aware objective functions for a sampling-based motion planner (MPPI). To address the ambiguity of physical parameters in visual data, we introduce a neuro-symbolic adaptation loop: a VLM provides semantic priors for environmental dynamics, such as mass and friction estimates, which are then explicitly refined in real time via online system identification, while the LLM iteratively modulates the cost-function structure to correct strategic errors based on interaction feedback. Furthermore, a retrieval-based memory unit allows the system to reuse successful strategies across recurrent tasks. This hierarchical architecture ensures real-time control stability by decoupling high-level semantic reasoning from reactive execution, effectively bridging the gap between slow LLM inference and dynamic contact requirements. We validate CoRAL on both simulation and real-world hardware across challenging and novel tasks, such as flipping objects against walls by leveraging extrinsic contacts. Experiments demonstrate that CoRAL outperforms state-of-the-art VLA and foundation-model-based planner baselines by boosting success rates over 50% on average in unseen contact-rich scenarios, effectively handling sim-to-real gaps through its adaptive physical understanding.
匹配关键词: sim-to-real
---

[ACADEMIC - ARXIV]
标题: Robotic Affection -- Opportunities of AI-based haptic interactions to improve social robotic touch through a multi-deep-learning approach
作者: Ali Askari, Jens Gerken
链接: https://arxiv.org/abs/2605.02538v1
完整摘要: Despite the advancement in robotic grasping and dexterity through haptic information, affective social touch, such as handshaking or reassuring stroking, remains a major challenge in Human-Robot-Interaction. This position paper examines current progress and limitations across artificial intelligence, haptics and robotics research, and proposes a novel multi-model architecture to address these gaps. Drawing inspiration from neurobiology, we decompose affective touch into distinct, specialized subtasks models. By treating affective touch as a distributed, closed-loop perceptual task rather than a monolithic motoric movement, we aim to overcome the "haptic uncanny valley" through a peer-to-peer, state-sharing framework. Our approach supports scalable and cumulative development within a Sim-to-Real pipeline, fostering interdisciplinary collaboration. By enabling haptics, AI, and robotics researchers to contribute independently yet coherently, we outline a pathway toward a unified, expressive system for social robotics.
匹配关键词: sim-to-real
---

[ACADEMIC - ARXIV]
标题: Sim-to-Real Transfer and Robustness Evaluation of Reinforcement Learning Control with Integrated Perception on an ASV for Floating Waste Capture
作者: Luis F. W. Batista, Stéphanie Aravecchia, Cédric Pradalier
链接: https://arxiv.org/abs/2605.02529v1
完整摘要: Autonomous surface vessels for floating-waste removal operate under varying hydrodynamics, external disturbances, and challenging water-surface perception. We present a field-validated system that combines camera-based polarimetric perception with a lightweight DRL-based controller for floating-waste detection and capture. Camera detections are converted into water-surface target points and tracked by a controller trained entirely in simulation and deployed directly on a retrofitted ASV platform. Our main contribution is a sim-to-real testing methodology that combines a two-stage simulation protocol with a perception abstraction module designed to mimic real camera behavior, enabling reproducible field trials and explicit evaluation of the sim-to-real gap. We apply this framework in matched simulation and field experiments across 14 disturbance regimes to expose failure modes and evaluate robustness. The results show centimeter-level terminal accuracy and indicate robust control performance under the evaluated perturbation regimes. The main source of degradation is insufficient actuation-model fidelity. We also demonstrate the system in a search-and-capture application using real camera detections in real-world conditions over areas of up to $450~m^2$. The study distills practical lessons for reliable transfer, including improved actuation-model fidelity, targeted domain randomization, and careful management of latency and timestamps across modules, while highlighting remaining challenges.
匹配关键词: sim-to-real
---

[ACADEMIC - ARXIV]
标题: Beyond Specialization: Robust Reinforcement Learning Navigation via Procedural Map Generators
作者: Christian Jestel, Nicolas Bach, Marvin Wiedemann, Jan Finke, Peter Detzner
链接: https://arxiv.org/abs/2605.02528v1
完整摘要: Deep reinforcement learning (DRL) navigation policies often overfit to the structure of their training environments, as environmental diversity is typically constrained by the manual effort required to design diverse scenarios. While procedural map generation offers scalable diversity, no prior work systematically compares how different generator types affect policy generalization. We integrate four generators (sparse, maze, graph, and Wave Function Collapse) with guaranteed navigability into MuRoSim, a 2D simulator focusing on training efficiency for LiDAR-based navigation. We cross-evaluate five navigation policies on 1000 seeded maps per generator across three training seeds. Results show a strongly asymmetric cross-generator transfer: a specialist trained on sparse layouts falls to 3.3% success on mazes, whereas a policy trained on the combined generator set achieves 91.5 +/- 1.1% mean success. We further demonstrate that A* path-planner subgoal inputs are the dominant factor for robustness, raising success from the 90.2 +/- 1.4% feedforward baseline to 98.9 +/- 0.4% and outperforming GRU recurrence, which only improves the reactive baseline. The DRL policies outperform a classical Carrot+A* controller, which matches their success only at low speeds (1.0 m/s) but collapses to 24.9% at 2.0 m/s. This highlights learned speed adaptation as the decisive advantage of the learned approach. Real-world experiments on a RoboMaster confirm sim-to-real transfer in a cluttered arena, while a maze-like layout exposes remaining failure modes that recurrence helps mitigate.
匹配关键词: sim-to-real
---

[ACADEMIC - ARXIV]
标题: AlbumFill: Album-Guided Reasoning and Retrieval for Personalized Image Completion
作者: Yu-Ju Tsai, Brian Price, Qing Liu, Luis Figueroa, Daniil Pakhomov, Zhihong Ding, Scott Cohen, Ming-Hsuan Yang
链接: https://arxiv.org/abs/2605.02892v1
完整摘要: Personalized image completion aims to restore occluded regions in personal photos while preserving identity and appearance. Existing methods either rely on generic inpainting models that often fail to maintain identity consistency, or assume that suitable reference images are explicitly provided. In practice, suitable references are often not explicitly provided, requiring the system to search for identity-consistent images within personal photo collections. We present AlbumFill, a training-free framework that retrieves identity-consistent references from personal albums for personalized completion. Given an occluded image and a personal album, a vision-language model infers missing semantic cues to guide composed image retrieval, and the retrieved references are used by reference-based completion models. To facilitate this task, we introduce a dataset containing 54K human-centric samples with associated album images. Experiments across multiple baselines demonstrate the difficulty of personalized completion and highlight the importance of identity-consistent reference retrieval. Project Page: https://liagm.github.io/AlbumFill/
匹配关键词: world model
---

[ACADEMIC - ARXIV]
标题: SpecKV: Adaptive Speculative Decoding with Compression-Aware Gamma Selection
作者: Shikhar Shukla
链接: https://arxiv.org/abs/2605.02888v1
完整摘要: Speculative decoding accelerates large language model (LLM) inference by using a small draft model to propose candidate tokens that a larger target model verifies. A critical hyperparameter in this process is the speculation length~$γ$, which determines how many tokens the draft model proposes per step. Nearly all existing systems use a fixed~$γ$ (typically~4), yet empirical evidence suggests that the optimal value varies across task types and, crucially, depends on the compression level applied to the target model. In this paper, we present \textbf{SpecKV}, a lightweight adaptive controller that selects~$γ$ per speculation step using signals extracted from the draft model itself. We profile speculative decoding across 4~task categories, 4~speculation lengths, and 3~compression levels (FP16, INT8, NF4), collecting 5,112 step-level records with per-step acceptance rates, draft entropy, and draft confidence. We demonstrate that the optimal~$γ$ shifts across compression regimes and that draft model confidence and entropy are strong predictors of acceptance rate (correlation~$\approx 0.56$). SpecKV uses a small MLP trained on these signals to maximize expected tokens per speculation step, achieving a 56.0\% improvement over the fixed-$γ$=4 baseline with only 0.34\,ms overhead per decision ($<$0.5\% of step time). The improvement is statistically significant ($p < 0.001$, paired bootstrap test). We release all profiling data, trained models, and notebooks as open-source artifacts.
匹配关键词: world model
---

[ACADEMIC - ARXIV]
标题: MolmoAct2: Action Reasoning Models for Real-world Deployment
作者: Haoquan Fang, Jiafei Duan, Donovan Clay, Sam Wang, Shuo Liu, Weikai Huang, Xiang Fan, Wei-Chuan Tsai, Shirui Chen, Yi Ru Wang, Shanli Xing, Jaemin Cho, Jae Sung Park, Ainaz Eftekhar, Peter Sushko, Karen Farley, Angad Wadhwa, Cole Harrison, Winson Han, Ying-Chun Lee, Eli VanderBilt, Rose Hendrix, Suveen Ellawela, Lucas Ngoo, Joyce Chai, Zhongzheng Ren, Ali Farhadi, Dieter Fox, Ranjay Krishna
链接: https://arxiv.org/abs/2605.02881v1
完整摘要: Vision-Language-Action (VLA) models aim to provide a single generalist controller for robots, but today's systems fall short on the criteria that matter for real-world deployment. Frontier models are closed, open-weight alternatives are tied to expensive hardware, reasoning-augmented policies pay prohibitive latency for their grounding, and fine-tuned success rates remain below the threshold for dependable use. We present MolmoAct2, a fully open action reasoning model built for practical deployment, advancing its predecessor along five axes. We introduce MolmoER, a VLM backbone specialized for spatial and embodied reasoning, trained on a 3.3M-sample corpus with a specialize-then-rehearse recipe. We release three new datasets spanning low-to-medium cost platforms, including MolmoAct2-BimanualYAM, 720 hours of teleoperated bimanual trajectories that constitute the largest open bimanual dataset to date, together with quality-filtered Franka (DROID) and SO100/101 subsets. We provide OpenFAST, an open-weight, open-data action tokenizer trained on millions of trajectories across five embodiments. We redesign the architecture to graft a flow-matching continuous-action expert onto a discrete-token VLM via per-layer KV-cache conditioning. Finally, we propose MolmoThink, an adaptive-depth reasoning variant that re-predicts depth tokens only for scene regions that change between timesteps, retaining geometric grounding at a fraction of prior latency. In the most extensive empirical study of any open VLA to date, spanning 7 simulation and real-world benchmarks, MolmoAct2 outperforms strong baselines including Pi-05, while MolmoER surpasses GPT-5 and Gemini Robotics ER-1.5 across 13 embodied-reasoning benchmarks. We release model weights, training code, and complete training data. Project page: https://allenai.org/blog/molmoact2
匹配关键词: world model
---

[ACADEMIC - ARXIV]
标题: Multi-fidelity surrogates for mechanics of composites: from co-kriging to multi-fidelity neural networks
作者: Haizhou Wen, Elham Kiyani, Gang Li, Srikanth Pilla, George Em Karniadakis, Zhen Li
链接: https://arxiv.org/abs/2605.02871v1
完整摘要: Composite materials exhibit strongly hierarchical and anisotropic properties governed by coupled mechanisms spanning constituents, plies, laminates, structures, and manufacturing history. This intrinsic complexity makes predictive modeling of composites expensive, because repeated experiments and high-fidelity simulations are needed to cover large design spaces of material, structure, and manufacturing. Multi-fidelity surrogate modeling addresses this challenge by combining abundant, less expensive data with limited high-accuracy data to recover reliable high-fidelity predictions. This review presents a structured overview of multi-fidelity modeling for composite mechanics, covering Gaussian-process or Kriging-based methods, including co-Kriging, coregionalization models, autoregressive formulations, nonlinear autoregressive Gaussian processes, multi-fidelity deep Gaussian processes, and multi-fidelity neural networks. Their distinctions are examined in terms of cross-fidelity correlation, discrepancy representation, uncertainty quantification, and scalability. Selected examples of their applications to composites are introduced according to the roles that multi-fidelity surrogates play in engineering problems, including forward prediction for rapid exploration of material design spaces, inverse optimization for composite parameter identification and design search under limited high-fidelity access, and workflow integration, where heterogeneous data sources, constraints, and validation requirements determine model utility. Open question discussions highlight recurring challenges specific to composites, such as regime-dependent fidelity gaps associated with nonlinear damage and manufacturing history, mismatches between simulations and experiments, and uncertainty propagation across multi-fidelity models.
匹配关键词: world model
---

[ACADEMIC - ARXIV]
标题: Enhancing RL Generalizability in Robotics through SHAP Analysis of Algorithms and Hyperparameters
作者: Lingxiao Kong, Cong Yang, Oya Deniz Beyan, Zeyd Boukhers
链接: https://arxiv.org/abs/2605.02867v1
完整摘要: Despite significant advances in Reinforcement Learning (RL), model performance remains highly sensitive to algorithm and hyperparameter configurations, while generalization gaps across environments complicate real-world deployment. Although prior work has studied RL generalization, the relative contribution of specific configurations to the generalization gap has not been quantitatively decomposed and systematically leveraged for configuration selection. To address this limitation, we propose an explainable framework that evaluates RL performance across robotic environments using SHapley Additive exPlanations (SHAP) to quantify configuration impacts. We establish a theoretical foundation connecting Shapley values to generalizability, empirically analyze configuration impact patterns, and introduce SHAP-guided configuration selection to enhance generalization. Our results reveal distinct patterns across algorithms and hyperparameters, with consistent configuration impacts across diverse tasks and environments. By applying these insights to configuration selection, we achieve improved RL generalizability and provide actionable guidance for practitioners.
匹配关键词: world model
---

[ACADEMIC - ARXIV]
标题: Multi-Axis Speech Similarity via Factor-Partitioned Embeddings
作者: Jim O'Regan, Jens Edlund
链接: https://arxiv.org/abs/2605.02804v1
完整摘要: Speech encodes multiple simultaneous attributes--linguistic content, speaker identity, dialect, gender--that conventional single-vector embeddings conflate. We present a factor-partitioned embedding framework that maps each utterance into a single vector whose subspaces correspond to distinct axes of variation. A shared acoustic encoder feeds per-axis linear projection heads, each trained via distillation from a specialist teacher or a contrastive objective over shared-label pairs. The resulting embeddings support attribute-conditioned retrieval: similarity is computed as a signed weighted sum over per-axis cosine scores, allowing retrieval that jointly considers what was said and how --or explicitly suppresses one attribute to surface another. We evaluate on cross-corpus retrieval over corpora sharing the Harvard sentence prompts, demonstrating that signed axis weighting can suppress same-speaker bias and surface semantically matched utterances across recording conditions.
匹配关键词: speech synthesis
---

[ACADEMIC - ARXIV]
标题: HumanSplatHMR: Closing the Loop Between Human Mesh Recovery and Gaussian Splatting Avatar
作者: Yeheng Zong, Pou-Chun Kung, Yike Pan, Seth Isaacson, Yizhou Chen, Ram Vasudevan, Katherine A. Skinner
链接: https://arxiv.org/abs/2605.02784v1
完整摘要: Accurately recovering human pose and appearance from video is an essential component of scene reconstruction, with applications to motion capture, motion prediction, virtual reality, and digital twinning. Despite significant interest in building realistic human avatars from video, this paper demonstrates that existing methods do not accurately recover the 3D geometry of humans. ViT-based approaches are not consistently reliable and can overfit to 2D views, while NeRF- and Gaussian Splatting-based avatars treat pose and appearance separately, limiting rendering generalization to new poses. To resolve these shortcomings, this paper proposes HumanSplatHMR, a joint optimization framework that refines 3D human poses while simultaneously learning a high-fidelity avatar for novel-view and novel-pose synthesis. Our key insight is to close the loop between geometric pose estimation and differentiable rendering. Unlike prior human avatar methods that rely on accurate human pose obtained through motion capture systems or offline refinement, which are impractical in in-the-wild scenarios, our approach uses only human mesh estimates from a state-of-the-art human pose estimator to better reflect real-world conditions. Therefore, instead of using the human pose only as a deformation prior, HumanSplatHMR backpropagates photometric, segmentation, and depth losses through a differentiable renderer to the pose parameters and global position. This coupling refines the global 3D pose over time, improving accuracy and alignment while producing better renderings from novel views. Experiments show consistent improvements over pose recovery baselines that omit image-level refinement and avatar baselines that decouple pose estimation from avatar reconstruction.
匹配关键词: speech synthesis
---

[ACADEMIC - ARXIV]
标题: When Audio-Language Models Fail to Leverage Multimodal Context for Dysarthric Speech Recognition
作者: Pehuén Moure, Niclas Pokel, Bilal Bounajma, Yingqiang Gao, Roman Boehringer, Longbiao Cheng, Shih-Chii Liu
链接: https://arxiv.org/abs/2605.02782v1
完整摘要: Automatic speech recognition (ASR) systems remain brittle on dysarthric and other atypical speech. Recent audio-language models raise the possibility of improving performance by conditioning on additional clinical context at inference time, but it is unclear whether these models can make use of such information. We introduce a benchmark built on the Speech Accessibility Project (SAP) dataset that tests whether diagnosis labels, clinician-derived speech ratings, and progressively richer clinical descriptions improve transcription accuracy for dysarthric speech. Across matched comparisons on nine models, we find that current models do not meaningfully use this context: diagnosis-informed and clinically detailed prompts yield negligible improvements and often degrade word error rate. We complement the prompting analysis with context-dependent fine-tuning, showing that LoRA adaptation with a mixture of clinical prompt formats achieves a WER of 0.066, a 52% relative reduction over the frozen baseline, while preserving performance when context is unavailable. Subgroup analyses reveal significant gains for Down syndrome and mild-severity speakers. These results clarify where current models fall short and provide a testbed for measuring progress toward more inclusive ASR.
匹配关键词: speech synthesis
---

[ACADEMIC - ARXIV]
标题: Adaptive Interpolation-Synthesis for Motion In-Betweening on Keyframe-Based Animation
作者: Anton Raël, Julien Boucher, Antoine Lhermitte
链接: https://arxiv.org/abs/2605.02742v1
完整摘要: Motion in-betweening is one of the most artistically demanding and time consuming stages of 3D animation, where the expressivity and rhythm of motion are defined. The level of creative control it requires makes it a major production bottleneck, underscoring the need for intelligent tools that assist animators in this process. Although recent deep learning approaches have achieved strong results in motion synthesis and in-betweening, they assume data characteristics, motion styles, and problem formulations that diverge from professional animation workflows. To bridge this gap, we propose a method explicitly aligned with the constraints of motion in-betweening for keyframe-based animation in production environments. At its core, the Adaptive Interpolation-Synthesis (AIS) layer mirrors the animator's creative process by dynamically balancing learned interpolation and direct pose synthesis. In addition, a domain-based input keypose schedule reflects the distribution of production data, improving stylistic consistency and alignment between training and real-world usage. Our method achieves state-of-the-art performance on production data; when integrated into Autodesk Maya, it enables animators to complete in-betweening tasks with a 3.5x speedup.
匹配关键词: speech synthesis
---

[ACADEMIC - ARXIV]
标题: Dimensionality-Aware Anomaly Detection in Learned Representations of Self-Supervised Speech Models
作者: Sandra Arcos-Holzinger, Sarah M. Erfani, James Bailey, Sanjeev Khudanpur
链接: https://arxiv.org/abs/2605.02715v1
完整摘要: Self-supervised speech models (S3Ms) achieve strong downstream performance, yet their learned representations remain poorly understood under natural and adversarial perturbations. Prior studies rely on representation similarity or global dimensionality, offering limited visibility into local geometric changes. We ask: how do perturbations deform local geometry, and do these shifts track downstream automatic speech recognition (ASR) degradation? To address this, we present GRIDS, a framework using Local Intrinsic Dimensionality (LID) across layer-wise representations in WavLM and wav2vec 2.0. We find that LID increases for all low signal-to noise ratio (SNR) perturbations and diverges at high SNR: benign noise converges toward the clean profile, while adversarial inputs retain early-layer LID elevation. We show LID elevation co-occurs with increased WER, and that layer-wise LID features enable anomaly detection (AUROC 0.78-1.00), opening the door to transcript-free monitoring in S3Ms.
匹配关键词: speech synthesis
---

[ACADEMIC - ARXIV]
标题: Tibetan-TTS:Low-Resource Tibetan Speech Synthesis with Large Model Adaptation
作者: Jiaxu He, Chao Wang, Jie Lian, Yuqing Cai, Yongxiang Li, Renzeg Duojie, Jie Li
链接: https://arxiv.org/abs/2605.02496v1
完整摘要: Tibetan text-to-speech (TTS) has long been challenged by scarce speech resources, significant dialectal variation, and the complex mapping between written text and spoken pronunciation. To address these issues, this work presents, to the best of our knowledge, the first large-model-based Tibetan TTS system in the industry, built upon a large speech synthesis model developed by Xingchen AGI Lab. The proposed system integrates data quality enhancement, Tibetan-oriented text representation and tokenizer adaptation, and cross-lingual adaptive training for low-resource Tibetan speech synthesis. Experimental results show that the system can generate stable, natural, and intelligible Tibetan speech under low-resource conditions. In subjective evaluation, the MOS scores of the syllable-level and BPE-based systems reach 4.28 and 4.35, while their pronunciation accuracies reach 97.6% and 96.6%, respectively, outperforming an external commercial Tibetan TTS interface. These results demonstrate that combining a large-model backbone with Tibetan-oriented text representation adaptation and cross-lingual adaptive training enables highly usable low-resource Tibetan speech synthesis, and also provides a technical foundation for future unified multi-dialect Tibetan speech synthesis.
匹配关键词: TTS
---

[ACADEMIC - ARXIV]
标题: When Audio-Language Models Fail to Leverage Multimodal Context for Dysarthric Speech Recognition
作者: Pehuén Moure, Niclas Pokel, Bilal Bounajma, Yingqiang Gao, Roman Boehringer, Longbiao Cheng, Shih-Chii Liu
链接: https://arxiv.org/abs/2605.02782v1
完整摘要: Automatic speech recognition (ASR) systems remain brittle on dysarthric and other atypical speech. Recent audio-language models raise the possibility of improving performance by conditioning on additional clinical context at inference time, but it is unclear whether these models can make use of such information. We introduce a benchmark built on the Speech Accessibility Project (SAP) dataset that tests whether diagnosis labels, clinician-derived speech ratings, and progressively richer clinical descriptions improve transcription accuracy for dysarthric speech. Across matched comparisons on nine models, we find that current models do not meaningfully use this context: diagnosis-informed and clinically detailed prompts yield negligible improvements and often degrade word error rate. We complement the prompting analysis with context-dependent fine-tuning, showing that LoRA adaptation with a mixture of clinical prompt formats achieves a WER of 0.066, a 52% relative reduction over the frozen baseline, while preserving performance when context is unavailable. Subgroup analyses reveal significant gains for Down syndrome and mild-severity speakers. These results clarify where current models fall short and provide a testbed for measuring progress toward more inclusive ASR.
匹配关键词: ASR
---

[ACADEMIC - ARXIV]
标题: Dimensionality-Aware Anomaly Detection in Learned Representations of Self-Supervised Speech Models
作者: Sandra Arcos-Holzinger, Sarah M. Erfani, James Bailey, Sanjeev Khudanpur
链接: https://arxiv.org/abs/2605.02715v1
完整摘要: Self-supervised speech models (S3Ms) achieve strong downstream performance, yet their learned representations remain poorly understood under natural and adversarial perturbations. Prior studies rely on representation similarity or global dimensionality, offering limited visibility into local geometric changes. We ask: how do perturbations deform local geometry, and do these shifts track downstream automatic speech recognition (ASR) degradation? To address this, we present GRIDS, a framework using Local Intrinsic Dimensionality (LID) across layer-wise representations in WavLM and wav2vec 2.0. We find that LID increases for all low signal-to noise ratio (SNR) perturbations and diverges at high SNR: benign noise converges toward the clean profile, while adversarial inputs retain early-layer LID elevation. We show LID elevation co-occurs with increased WER, and that layer-wise LID features enable anomaly detection (AUROC 0.78-1.00), opening the door to transcript-free monitoring in S3Ms.
匹配关键词: ASR
---

[ACADEMIC - ARXIV]
标题: ContextualJailbreak: Evolutionary Red-Teaming via Simulated Conversational Priming
作者: Mario Rodríguez Béjar, Francisco J. Cortés-Delgado, S. Braghin, Jose L. Hernández-Ramos
链接: https://arxiv.org/abs/2605.02647v1
完整摘要: Large language models (LLMs) remain vulnerable to jailbreak attacks that bypass safety alignment and elicit harmful responses. A growing body of work shows that contextual priming, where earlier turns covertly bias later replies, constitutes a powerful attack surface, with hand-crafted multi-turn scaffolds consistently outperforming single-turn manipulations on capable models. However, automated optimization-based red-teaming has remained largely limited to the single-turn setting, iterating over static prompts and lacking the ability to reason about which forms of conversational priming induce compliance. While recent multi-turn, search-based approaches have begun to bridge this gap, the mutator design space underlying effective primed dialogues remains largely unexplored. We present ContextualJailbreak, a black-box red-teaming strategy that performs evolutionary search over a simulated multi-turn primed dialogue. The strategy leverages a graded 0-5 harm score from a two-level judge as an in-loop signal, enabling partially harmful responses to guide the search process rather than being discarded. Search is driven by five semantically defined mutation operators: roleplay, scenario, expand, troubleshooting, and mechanistic, of which the last two are novel contributions of this work. Across 50 representative HarmBench behaviors, ContextualJailbreak achieves an ASR of 100% on gpt-oss:20B, 100% on qwen3-8B, 100% on llama3.1:70B, and 90% on gpt-oss:120B, outperforming four single- and multi-turn baselines by 31-96 percentage points on average. The 40 maximally harmful attacks discovered against gpt-oss:120B transfer without adaptation to closed frontier models, achieving 90.0% on gpt-4o-mini, 70.0% on gpt-5, and 70.0% on gemini-3-flash, but only 17.5% on claude-opus-4-7 and 15.0% on claude-sonnet-4-6, revealing a pronounced provider-level asymmetry in alignment robustness.
匹配关键词: ASR
---

[ACADEMIC - ARXIV]
标题: AlbumFill: Album-Guided Reasoning and Retrieval for Personalized Image Completion
作者: Yu-Ju Tsai, Brian Price, Qing Liu, Luis Figueroa, Daniil Pakhomov, Zhihong Ding, Scott Cohen, Ming-Hsuan Yang
链接: https://arxiv.org/abs/2605.02892v1
完整摘要: Personalized image completion aims to restore occluded regions in personal photos while preserving identity and appearance. Existing methods either rely on generic inpainting models that often fail to maintain identity consistency, or assume that suitable reference images are explicitly provided. In practice, suitable references are often not explicitly provided, requiring the system to search for identity-consistent images within personal photo collections. We present AlbumFill, a training-free framework that retrieves identity-consistent references from personal albums for personalized completion. Given an occluded image and a personal album, a vision-language model infers missing semantic cues to guide composed image retrieval, and the retrieved references are used by reference-based completion models. To facilitate this task, we introduce a dataset containing 54K human-centric samples with associated album images. Experiments across multiple baselines demonstrate the difficulty of personalized completion and highlight the importance of identity-consistent reference retrieval. Project Page: https://liagm.github.io/AlbumFill/
匹配关键词: audio language model
---

[ACADEMIC - ARXIV]
标题: SpecKV: Adaptive Speculative Decoding with Compression-Aware Gamma Selection
作者: Shikhar Shukla
链接: https://arxiv.org/abs/2605.02888v1
完整摘要: Speculative decoding accelerates large language model (LLM) inference by using a small draft model to propose candidate tokens that a larger target model verifies. A critical hyperparameter in this process is the speculation length~$γ$, which determines how many tokens the draft model proposes per step. Nearly all existing systems use a fixed~$γ$ (typically~4), yet empirical evidence suggests that the optimal value varies across task types and, crucially, depends on the compression level applied to the target model. In this paper, we present \textbf{SpecKV}, a lightweight adaptive controller that selects~$γ$ per speculation step using signals extracted from the draft model itself. We profile speculative decoding across 4~task categories, 4~speculation lengths, and 3~compression levels (FP16, INT8, NF4), collecting 5,112 step-level records with per-step acceptance rates, draft entropy, and draft confidence. We demonstrate that the optimal~$γ$ shifts across compression regimes and that draft model confidence and entropy are strong predictors of acceptance rate (correlation~$\approx 0.56$). SpecKV uses a small MLP trained on these signals to maximize expected tokens per speculation step, achieving a 56.0\% improvement over the fixed-$γ$=4 baseline with only 0.34\,ms overhead per decision ($<$0.5\% of step time). The improvement is statistically significant ($p < 0.001$, paired bootstrap test). We release all profiling data, trained models, and notebooks as open-source artifacts.
匹配关键词: audio language model
---

[ACADEMIC - ARXIV]
标题: MolmoAct2: Action Reasoning Models for Real-world Deployment
作者: Haoquan Fang, Jiafei Duan, Donovan Clay, Sam Wang, Shuo Liu, Weikai Huang, Xiang Fan, Wei-Chuan Tsai, Shirui Chen, Yi Ru Wang, Shanli Xing, Jaemin Cho, Jae Sung Park, Ainaz Eftekhar, Peter Sushko, Karen Farley, Angad Wadhwa, Cole Harrison, Winson Han, Ying-Chun Lee, Eli VanderBilt, Rose Hendrix, Suveen Ellawela, Lucas Ngoo, Joyce Chai, Zhongzheng Ren, Ali Farhadi, Dieter Fox, Ranjay Krishna
链接: https://arxiv.org/abs/2605.02881v1
完整摘要: Vision-Language-Action (VLA) models aim to provide a single generalist controller for robots, but today's systems fall short on the criteria that matter for real-world deployment. Frontier models are closed, open-weight alternatives are tied to expensive hardware, reasoning-augmented policies pay prohibitive latency for their grounding, and fine-tuned success rates remain below the threshold for dependable use. We present MolmoAct2, a fully open action reasoning model built for practical deployment, advancing its predecessor along five axes. We introduce MolmoER, a VLM backbone specialized for spatial and embodied reasoning, trained on a 3.3M-sample corpus with a specialize-then-rehearse recipe. We release three new datasets spanning low-to-medium cost platforms, including MolmoAct2-BimanualYAM, 720 hours of teleoperated bimanual trajectories that constitute the largest open bimanual dataset to date, together with quality-filtered Franka (DROID) and SO100/101 subsets. We provide OpenFAST, an open-weight, open-data action tokenizer trained on millions of trajectories across five embodiments. We redesign the architecture to graft a flow-matching continuous-action expert onto a discrete-token VLM via per-layer KV-cache conditioning. Finally, we propose MolmoThink, an adaptive-depth reasoning variant that re-predicts depth tokens only for scene regions that change between timesteps, retaining geometric grounding at a fraction of prior latency. In the most extensive empirical study of any open VLA to date, spanning 7 simulation and real-world benchmarks, MolmoAct2 outperforms strong baselines including Pi-05, while MolmoER surpasses GPT-5 and Gemini Robotics ER-1.5 across 13 embodied-reasoning benchmarks. We release model weights, training code, and complete training data. Project page: https://allenai.org/blog/molmoact2
匹配关键词: audio language model
---

[ACADEMIC - ARXIV]
标题: Multi-fidelity surrogates for mechanics of composites: from co-kriging to multi-fidelity neural networks
作者: Haizhou Wen, Elham Kiyani, Gang Li, Srikanth Pilla, George Em Karniadakis, Zhen Li
链接: https://arxiv.org/abs/2605.02871v1
完整摘要: Composite materials exhibit strongly hierarchical and anisotropic properties governed by coupled mechanisms spanning constituents, plies, laminates, structures, and manufacturing history. This intrinsic complexity makes predictive modeling of composites expensive, because repeated experiments and high-fidelity simulations are needed to cover large design spaces of material, structure, and manufacturing. Multi-fidelity surrogate modeling addresses this challenge by combining abundant, less expensive data with limited high-accuracy data to recover reliable high-fidelity predictions. This review presents a structured overview of multi-fidelity modeling for composite mechanics, covering Gaussian-process or Kriging-based methods, including co-Kriging, coregionalization models, autoregressive formulations, nonlinear autoregressive Gaussian processes, multi-fidelity deep Gaussian processes, and multi-fidelity neural networks. Their distinctions are examined in terms of cross-fidelity correlation, discrepancy representation, uncertainty quantification, and scalability. Selected examples of their applications to composites are introduced according to the roles that multi-fidelity surrogates play in engineering problems, including forward prediction for rapid exploration of material design spaces, inverse optimization for composite parameter identification and design search under limited high-fidelity access, and workflow integration, where heterogeneous data sources, constraints, and validation requirements determine model utility. Open question discussions highlight recurring challenges specific to composites, such as regime-dependent fidelity gaps associated with nonlinear damage and manufacturing history, mismatches between simulations and experiments, and uncertainty propagation across multi-fidelity models.
匹配关键词: audio language model
---

[ACADEMIC - ARXIV]
标题: Enhancing RL Generalizability in Robotics through SHAP Analysis of Algorithms and Hyperparameters
作者: Lingxiao Kong, Cong Yang, Oya Deniz Beyan, Zeyd Boukhers
链接: https://arxiv.org/abs/2605.02867v1
完整摘要: Despite significant advances in Reinforcement Learning (RL), model performance remains highly sensitive to algorithm and hyperparameter configurations, while generalization gaps across environments complicate real-world deployment. Although prior work has studied RL generalization, the relative contribution of specific configurations to the generalization gap has not been quantitatively decomposed and systematically leveraged for configuration selection. To address this limitation, we propose an explainable framework that evaluates RL performance across robotic environments using SHapley Additive exPlanations (SHAP) to quantify configuration impacts. We establish a theoretical foundation connecting Shapley values to generalizability, empirically analyze configuration impact patterns, and introduce SHAP-guided configuration selection to enhance generalization. Our results reveal distinct patterns across algorithms and hyperparameters, with consistent configuration impacts across diverse tasks and environments. By applying these insights to configuration selection, we achieve improved RL generalizability and provide actionable guidance for practitioners.
匹配关键词: audio language model
---

[ACADEMIC - ARXIV]
标题: MolmoAct2: Action Reasoning Models for Real-world Deployment
作者: Haoquan Fang, Jiafei Duan, Donovan Clay, Sam Wang, Shuo Liu, Weikai Huang, Xiang Fan, Wei-Chuan Tsai, Shirui Chen, Yi Ru Wang, Shanli Xing, Jaemin Cho, Jae Sung Park, Ainaz Eftekhar, Peter Sushko, Karen Farley, Angad Wadhwa, Cole Harrison, Winson Han, Ying-Chun Lee, Eli VanderBilt, Rose Hendrix, Suveen Ellawela, Lucas Ngoo, Joyce Chai, Zhongzheng Ren, Ali Farhadi, Dieter Fox, Ranjay Krishna
链接: https://arxiv.org/abs/2605.02881v1
完整摘要: Vision-Language-Action (VLA) models aim to provide a single generalist controller for robots, but today's systems fall short on the criteria that matter for real-world deployment. Frontier models are closed, open-weight alternatives are tied to expensive hardware, reasoning-augmented policies pay prohibitive latency for their grounding, and fine-tuned success rates remain below the threshold for dependable use. We present MolmoAct2, a fully open action reasoning model built for practical deployment, advancing its predecessor along five axes. We introduce MolmoER, a VLM backbone specialized for spatial and embodied reasoning, trained on a 3.3M-sample corpus with a specialize-then-rehearse recipe. We release three new datasets spanning low-to-medium cost platforms, including MolmoAct2-BimanualYAM, 720 hours of teleoperated bimanual trajectories that constitute the largest open bimanual dataset to date, together with quality-filtered Franka (DROID) and SO100/101 subsets. We provide OpenFAST, an open-weight, open-data action tokenizer trained on millions of trajectories across five embodiments. We redesign the architecture to graft a flow-matching continuous-action expert onto a discrete-token VLM via per-layer KV-cache conditioning. Finally, we propose MolmoThink, an adaptive-depth reasoning variant that re-predicts depth tokens only for scene regions that change between timesteps, retaining geometric grounding at a fraction of prior latency. In the most extensive empirical study of any open VLA to date, spanning 7 simulation and real-world benchmarks, MolmoAct2 outperforms strong baselines including Pi-05, while MolmoER surpasses GPT-5 and Gemini Robotics ER-1.5 across 13 embodied-reasoning benchmarks. We release model weights, training code, and complete training data. Project page: https://allenai.org/blog/molmoact2
匹配关键词: KV cache
---

[ACADEMIC - ARXIV]
标题: Latent Bridge: Feature Delta Prediction for Efficient Dual-System Vision-Language-Action Model Inference
作者: Yudong Liu, Yuan Li, Zijia Tang, Yuxi Zheng, Yueqian Lin, Qinsi Wang, Yi Li, Shuangjun Liu, Shuai Zhang, Taotao Jing, Dashan Gao, Ning Bi, Jingwei Sun, Yiran Chen, Hai Li
链接: https://arxiv.org/abs/2605.02739v1
完整摘要: Dual-system Vision-Language-Action (VLA) models achieve state-of-the-art robotic manipulation but are bottlenecked by the VLM backbone, which must execute at every control step while producing temporally redundant features. We propose Latent Bridge, a lightweight model that predicts VLM output deltas between timesteps, enabling the action head to operate on predicted outputs while the expensive VLM backbone is called only periodically. We instantiate Latent Bridge on two architecturally distinct VLAs: GR00T-N1.6 (feature-space bridge) and π0.5 (KV-cache bridge), demonstrating that the approach generalizes across VLA designs. Our task-agnostic DAgger training pipeline transfers across benchmarks without modification. Across four LIBERO suites, 24 RoboCasa kitchen tasks, and the ALOHA sim transfer-cube task, Latent Bridge achieves 95-100% performance retention while reducing VLM calls by 50-75%, yielding 1.65-1.73x net per-episode speedup.
匹配关键词: KV cache
---

[ACADEMIC - ARXIV]
标题: Trust, but Verify: Peeling Low-Bit Transformer Networks for Training Monitoring
作者: Arian Eamaz, Farhang Yeganegi, Mojtaba Soltanalian
链接: https://arxiv.org/abs/2605.02853v1
完整摘要: Understanding whether deep neural networks are effectively optimized remains challenging, as training occurs in highly nonconvex landscapes and standard metrics provide limited visibility into layer-wise learning quality. This challenge is particularly acute for transformer-based language models, where training is expensive, models are often reused in frozen form, and poorly optimized layers can silently degrade performance. We propose a layer-wise peeling framework for monitoring training dynamics, in which each transformer layer is locally optimized against intermediate representations of the trained model. By constructing lightweight, layer-specific reference solutions and projecting layers onto multiple intermediate outputs via different permutations, we obtain achievable baselines that enable fine-grained diagnosis of under-optimized layers. Experiments on decoder-only transformer models show that these layer-wise reference bounds can match or even surpass the trained model at various stages of training, exposing inefficiencies that remain hidden in aggregate loss curves. We further demonstrate that this analysis remains effective under binarization and quantized settings, where training dynamics are particularly fragile. Across all numerical results, the proposed bounds consistently separate apparent convergence from effective optimality, highlighting optimization opportunities that are invisible when relying on training loss alone.
匹配关键词: quantization
---

[ACADEMIC - ARXIV]
标题: Statistically-Lossless Quantization of Large Language Models
作者: Michael Helcig, Eldar Kurtic, Dan Alistarh
链接: https://arxiv.org/abs/2605.02404v1
完整摘要: Model quantization has become essential for efficient large language model deployment, yet existing approaches involve clear trade-offs: methods such as GPTQ and AWQ achieve practical compression but are lossy, while lossless techniques preserve fidelity but typically do not accelerate inference. This paper explores the middle ground of statistically-lossless compression through three complementary notions of losslessness for quantized LLMs. First, task-lossless compression preserves zero-shot benchmark accuracy within natural sampling variance and remains achievable at aggressive bitwidths. Second, we formalize the stricter notion of distribution-lossless compression, requiring the quantized model's next-token distribution to be practically indistinguishable from the original, and propose the Expected Acceptance Rate (EAR), the maximum token-agreement probability under optimal coupling, as a directly interpretable fidelity metric (for example, EAR >= 0.99 indicates 99% agreement). Third, we prove a gamma-squared variance law showing that symmetric quantization inflates noise variance by gamma squared relative to asymmetric quantization, making asymmetry necessary for distribution-lossless fidelity but not for task-level preservation. Using SLQ, a layer-wise non-uniform method with asymmetric quantization and wide bitwidth search, we achieve task-lossless compression at well below 4 bits per parameter (as low as 3.3 bits depending on the model), distribution-lossless compression at 5 to 6 bits per parameter on average, and inference speedups of 1.7 to 3.6x relative to FP16 with optimized kernels. Source code is available at https://github.com/IST-DASLab/SLQ.
匹配关键词: quantization
---

[ACADEMIC - ARXIV]
标题: SpecKV: Adaptive Speculative Decoding with Compression-Aware Gamma Selection
作者: Shikhar Shukla
链接: https://arxiv.org/abs/2605.02888v1
完整摘要: Speculative decoding accelerates large language model (LLM) inference by using a small draft model to propose candidate tokens that a larger target model verifies. A critical hyperparameter in this process is the speculation length~$γ$, which determines how many tokens the draft model proposes per step. Nearly all existing systems use a fixed~$γ$ (typically~4), yet empirical evidence suggests that the optimal value varies across task types and, crucially, depends on the compression level applied to the target model. In this paper, we present \textbf{SpecKV}, a lightweight adaptive controller that selects~$γ$ per speculation step using signals extracted from the draft model itself. We profile speculative decoding across 4~task categories, 4~speculation lengths, and 3~compression levels (FP16, INT8, NF4), collecting 5,112 step-level records with per-step acceptance rates, draft entropy, and draft confidence. We demonstrate that the optimal~$γ$ shifts across compression regimes and that draft model confidence and entropy are strong predictors of acceptance rate (correlation~$\approx 0.56$). SpecKV uses a small MLP trained on these signals to maximize expected tokens per speculation step, achieving a 56.0\% improvement over the fixed-$γ$=4 baseline with only 0.34\,ms overhead per decision ($<$0.5\% of step time). The improvement is statistically significant ($p < 0.001$, paired bootstrap test). We release all profiling data, trained models, and notebooks as open-source artifacts.
匹配关键词: speculative decoding
---

[ACADEMIC - ARXIV]
标题: Laplacian Frequency Interaction Network for Rural Thematic Road Extraction
作者: Baiyan Chen, Weixin Zhai
链接: https://arxiv.org/abs/2605.02866v1
完整摘要: Rural thematic road network construction aims to extract topological road structures from movement trajectory images of agricultural machinery. However, this task faces challenges where downsampling methods commonly used in existing studies tend to blur the sparse high-frequency road structures, and the heavy noise from dense field operations often leads to fragmented or redundant topologies in the extracted networks. To address these challenges, we propose LFINet, a Laplacian Frequency Interaction Network. The network begins with a Laplacian Multi-scale Separator (LMS) to decouple the image into low-frequency semantic contexts and high-frequency structural details. These components are then processed by the Cross-Frequency Interaction Block (CFIB) through a dual-pathway architecture in which a High-Frequency Block (HFB) refines local structures while a Spatial Transformer (ST) captures global semantics. Subsequently, a Frequency Gated Modulation (FGM) mechanism integrates the features from pathways by leveraging semantic contexts to calibrate the structural details. Finally, a Progressive Reconstruction Decoder iteratively fuses multi-scale features to ensure topological consistency. Experiments conducted on a real-world agricultural trajectories dataset from Henan Province, China, show that LFINet establishes a new state-of-the-art. Specifically, it achieves an F1-score of 92.54% and an IoU of 86.12%, surpassing the second-ranked method by 0.64% and 1.1%, respectively. This confirms its capability to effectively construct topological road networks from noisy and sparse field data.
匹配关键词: speculative decoding
---

[ACADEMIC - ARXIV]
标题: Trust, but Verify: Peeling Low-Bit Transformer Networks for Training Monitoring
作者: Arian Eamaz, Farhang Yeganegi, Mojtaba Soltanalian
链接: https://arxiv.org/abs/2605.02853v1
完整摘要: Understanding whether deep neural networks are effectively optimized remains challenging, as training occurs in highly nonconvex landscapes and standard metrics provide limited visibility into layer-wise learning quality. This challenge is particularly acute for transformer-based language models, where training is expensive, models are often reused in frozen form, and poorly optimized layers can silently degrade performance. We propose a layer-wise peeling framework for monitoring training dynamics, in which each transformer layer is locally optimized against intermediate representations of the trained model. By constructing lightweight, layer-specific reference solutions and projecting layers onto multiple intermediate outputs via different permutations, we obtain achievable baselines that enable fine-grained diagnosis of under-optimized layers. Experiments on decoder-only transformer models show that these layer-wise reference bounds can match or even surpass the trained model at various stages of training, exposing inefficiencies that remain hidden in aggregate loss curves. We further demonstrate that this analysis remains effective under binarization and quantized settings, where training dynamics are particularly fragile. Across all numerical results, the proposed bounds consistently separate apparent convergence from effective optimality, highlighting optimization opportunities that are invisible when relying on training loss alone.
匹配关键词: speculative decoding
---

[ACADEMIC - ARXIV]
标题: Active Sampling for Ultra-Low-Bit-Rate Video Compression via Conditional Controlled Diffusion
作者: Amirhosein Javadi, Shirin Saeedi Bidokhti, Tara Javidi
链接: https://arxiv.org/abs/2605.02849v1
完整摘要: Diffusion models provide a powerful generative prior for perceptual reconstruction at ultra-low bitrates, but effective video compression requires controlling the generative process using highly compact conditioning signals. In this work, we present ActDiff-VC, a diffusion-based video compression framework for the ultra-low-bitrate regime. Our method partitions videos into variable-length segments, transmits keyframes only when needed, and summarizes temporal dynamics using a compact set of tracked point trajectories. Conditioned on these sparse signals, a conditional diffusion decoder synthesizes the remaining frames, enabling perceptually realistic reconstruction under severe rate constraints. To support this design, we introduce two mechanisms: content-adaptive keyframe selection and budget-aware sparse trajectory selection, which together enable compact yet effective conditioning for generative reconstruction. Experiments on the UVG and MCL-JCV benchmarks show that ActDiff-VC achieves up to 64.6\% bitrate reduction at matched NIQE, improves KID by up to 64.6\% and FID by up to 37.7\% at comparable bitrates against strong learned codecs, and delivers favorable perceptual rate--distortion trade-offs relative to learned and diffusion-based baselines in the ultra-low-bitrate regime.
匹配关键词: speculative decoding
---

[ACADEMIC - ARXIV]
标题: Fine-Grained Graph Generation through Latent Mixture Scheduling
作者: Nidhi Vakil, Hadi Amiri
链接: https://arxiv.org/abs/2605.02780v1
完整摘要: Structure aware graph generation aims to generate graphs that satisfy given topological properties. It has applications in domains such as drug discovery, social network modeling, and knowledge graph construction. Unlike existing methods that only provide coarse control over graph properties, we introduce a novel conditional variational autoencoder for fine-grained structural control in graph generation. The approach refines the decoder's latent space by dynamically aligning graph- and property-driven representations to improve both graph fidelity and control satisfaction. Specifically, the approach implements a mixture scheduler that progressively integrates graph and control priors. Experiments on five real-world datasets show the efficacy of the proposed model compared to recent baselines, achieving high generation quality while maintaining high controllability.
匹配关键词: speculative decoding
---

[ACADEMIC - ARXIV]
标题: SpecKV: Adaptive Speculative Decoding with Compression-Aware Gamma Selection
作者: Shikhar Shukla
链接: https://arxiv.org/abs/2605.02888v1
完整摘要: Speculative decoding accelerates large language model (LLM) inference by using a small draft model to propose candidate tokens that a larger target model verifies. A critical hyperparameter in this process is the speculation length~$γ$, which determines how many tokens the draft model proposes per step. Nearly all existing systems use a fixed~$γ$ (typically~4), yet empirical evidence suggests that the optimal value varies across task types and, crucially, depends on the compression level applied to the target model. In this paper, we present \textbf{SpecKV}, a lightweight adaptive controller that selects~$γ$ per speculation step using signals extracted from the draft model itself. We profile speculative decoding across 4~task categories, 4~speculation lengths, and 3~compression levels (FP16, INT8, NF4), collecting 5,112 step-level records with per-step acceptance rates, draft entropy, and draft confidence. We demonstrate that the optimal~$γ$ shifts across compression regimes and that draft model confidence and entropy are strong predictors of acceptance rate (correlation~$\approx 0.56$). SpecKV uses a small MLP trained on these signals to maximize expected tokens per speculation step, achieving a 56.0\% improvement over the fixed-$γ$=4 baseline with only 0.34\,ms overhead per decision ($<$0.5\% of step time). The improvement is statistically significant ($p < 0.001$, paired bootstrap test). We release all profiling data, trained models, and notebooks as open-source artifacts.
匹配关键词: kernel optimization
---

[ACADEMIC - ARXIV]
标题: Multi-fidelity surrogates for mechanics of composites: from co-kriging to multi-fidelity neural networks
作者: Haizhou Wen, Elham Kiyani, Gang Li, Srikanth Pilla, George Em Karniadakis, Zhen Li
链接: https://arxiv.org/abs/2605.02871v1
完整摘要: Composite materials exhibit strongly hierarchical and anisotropic properties governed by coupled mechanisms spanning constituents, plies, laminates, structures, and manufacturing history. This intrinsic complexity makes predictive modeling of composites expensive, because repeated experiments and high-fidelity simulations are needed to cover large design spaces of material, structure, and manufacturing. Multi-fidelity surrogate modeling addresses this challenge by combining abundant, less expensive data with limited high-accuracy data to recover reliable high-fidelity predictions. This review presents a structured overview of multi-fidelity modeling for composite mechanics, covering Gaussian-process or Kriging-based methods, including co-Kriging, coregionalization models, autoregressive formulations, nonlinear autoregressive Gaussian processes, multi-fidelity deep Gaussian processes, and multi-fidelity neural networks. Their distinctions are examined in terms of cross-fidelity correlation, discrepancy representation, uncertainty quantification, and scalability. Selected examples of their applications to composites are introduced according to the roles that multi-fidelity surrogates play in engineering problems, including forward prediction for rapid exploration of material design spaces, inverse optimization for composite parameter identification and design search under limited high-fidelity access, and workflow integration, where heterogeneous data sources, constraints, and validation requirements determine model utility. Open question discussions highlight recurring challenges specific to composites, such as regime-dependent fidelity gaps associated with nonlinear damage and manufacturing history, mismatches between simulations and experiments, and uncertainty propagation across multi-fidelity models.
匹配关键词: kernel optimization
---

[ACADEMIC - ARXIV]
标题: Pixel Perfect: Relational Image Quality Assessment with Spatially-Aware Distortions
作者: Fadeel Sher Khan, Long N. Le, Abhinau K. Venkataramanan, Seok-Jun Lee, Hamid R. Sheikh
链接: https://arxiv.org/abs/2605.02863v1
完整摘要: Traditional image quality assessment (IQA) methods rely on mean opinion scores (MOS), which are resource-intensive to collect and fail to provide interpretable, localized feedback on specific image distortions. We overcome these limitations by shifting from absolute quality prediction to a relational and directional assessment. Our approach utilizes a self-supervised synthetic distortion engine to generate training data, eliminating the need for manual annotation. A distortion prediction network is trained with an anti-symmetric objective to produce spatially-aware, disentangled maps that identify the type, intensity, and direction of distortions relative to a reference image. Subsequently, a scoring network is trained via contrastive learning on ordinally ranked image sets to predict a relational quality score. Our method provides a more granular and interpretable approach to IQA for the targeted optimization of image processing algorithms without requiring any human-labeled quality scores.
匹配关键词: kernel optimization
---

[ACADEMIC - ARXIV]
标题: Trust, but Verify: Peeling Low-Bit Transformer Networks for Training Monitoring
作者: Arian Eamaz, Farhang Yeganegi, Mojtaba Soltanalian
链接: https://arxiv.org/abs/2605.02853v1
完整摘要: Understanding whether deep neural networks are effectively optimized remains challenging, as training occurs in highly nonconvex landscapes and standard metrics provide limited visibility into layer-wise learning quality. This challenge is particularly acute for transformer-based language models, where training is expensive, models are often reused in frozen form, and poorly optimized layers can silently degrade performance. We propose a layer-wise peeling framework for monitoring training dynamics, in which each transformer layer is locally optimized against intermediate representations of the trained model. By constructing lightweight, layer-specific reference solutions and projecting layers onto multiple intermediate outputs via different permutations, we obtain achievable baselines that enable fine-grained diagnosis of under-optimized layers. Experiments on decoder-only transformer models show that these layer-wise reference bounds can match or even surpass the trained model at various stages of training, exposing inefficiencies that remain hidden in aggregate loss curves. We further demonstrate that this analysis remains effective under binarization and quantized settings, where training dynamics are particularly fragile. Across all numerical results, the proposed bounds consistently separate apparent convergence from effective optimality, highlighting optimization opportunities that are invisible when relying on training loss alone.
匹配关键词: kernel optimization
---

[ACADEMIC - ARXIV]
标题: A second-order method on the Stiefel manifold via Newton$\unicode{x2013}$Schulz
作者: Xinhui Xiong, Bin Gao, P. -A. Absil
链接: https://arxiv.org/abs/2605.02838v1
完整摘要: Retraction-free approaches offer attractive low-cost alternatives to Riemannian methods on the Stiefel manifold, but they are often first-order, which may limit the efficiency under high-accuracy requirements. To this end, we propose a second-order method landing on the Stiefel manifold without invoking retractions, which is proved to enjoy local quadratic (or superlinear for its inexact variant) convergence. The update consists of the sum of (i) a component tangent to the level set of the constraint-defining function that aims to reduce the objective and (ii) a component normal to the same level set that reduces the infeasibility. Specifically, we construct the normal component via Newton$\unicode{x2013}$Schulz, a fixed-point iteration for orthogonalization. Moreover, we establish a geometric connection between the Newton$\unicode{x2013}$Schulz iteration and Stiefel manifolds, in which Newton$\unicode{x2013}$Schulz moves along the normal space. For the tangent component, we formulate a modified Newton equation that incorporates Newton$\unicode{x2013}$Schulz. Numerical experiments on the orthogonal Procrustes problem, principal component analysis, and real-data independent component analysis illustrate that the proposed method performs better than the existing methods.
匹配关键词: kernel optimization
---

[ACADEMIC - ARXIV]
标题: SpecKV: Adaptive Speculative Decoding with Compression-Aware Gamma Selection
作者: Shikhar Shukla
链接: https://arxiv.org/abs/2605.02888v1
完整摘要: Speculative decoding accelerates large language model (LLM) inference by using a small draft model to propose candidate tokens that a larger target model verifies. A critical hyperparameter in this process is the speculation length~$γ$, which determines how many tokens the draft model proposes per step. Nearly all existing systems use a fixed~$γ$ (typically~4), yet empirical evidence suggests that the optimal value varies across task types and, crucially, depends on the compression level applied to the target model. In this paper, we present \textbf{SpecKV}, a lightweight adaptive controller that selects~$γ$ per speculation step using signals extracted from the draft model itself. We profile speculative decoding across 4~task categories, 4~speculation lengths, and 3~compression levels (FP16, INT8, NF4), collecting 5,112 step-level records with per-step acceptance rates, draft entropy, and draft confidence. We demonstrate that the optimal~$γ$ shifts across compression regimes and that draft model confidence and entropy are strong predictors of acceptance rate (correlation~$\approx 0.56$). SpecKV uses a small MLP trained on these signals to maximize expected tokens per speculation step, achieving a 56.0\% improvement over the fixed-$γ$=4 baseline with only 0.34\,ms overhead per decision ($<$0.5\% of step time). The improvement is statistically significant ($p < 0.001$, paired bootstrap test). We release all profiling data, trained models, and notebooks as open-source artifacts.
匹配关键词: preference learning
---

[ACADEMIC - ARXIV]
标题: Unsupervised Machine Learning for Detecting Structural Anomalies in European Regional Statistics
作者: Bogdan Oancea
链接: https://arxiv.org/abs/2605.02884v1
完整摘要: Ensuring the coherence of regional socio-economic statistics is a central task for national statistical institutes. Traditional validation tools, such as range edits, ratio checks, or univariate outlier detection, are effective for identifying extreme values in individual series but are less suited for detecting unusual combinations of indicators in high-dimensional settings. This paper proposes an unsupervised machine learning framework for identifying structurally atypical regional profiles within Europe using publicly available Eurostat data. We construct a cross-sectional dataset of NUTS2 regions (2022) covering four key indicators: GDP per capita in PPS, unemployment rate, tertiary educational attainment, and population density. We apply and compare five anomaly detection techniques, univariate z-scores, Mahalanobis distance, Isolation Forest, Local Outlier Factor, and One-Class SVM, and classify a region as a structural anomaly if it is flagged by at least three of the five methods. The findings show that machine learning methods identify a consistent set of regions whose multivariate profiles diverge substantially from the EU-wide pattern. These include both highly developed metropolitan economies (Brussels, Vienna, Berlin, Prague) and regions with persistent socio-economic disadvantages (Central and Western Slovakia, Northern Hungary, Castilla-La Mancha, Extremadura), as well as Istanbul, whose profile differs markedly from EU capital regions. Importantly, these anomalies do not necessarily signal data quality issues; rather, they reflect meaningful structural divergence that warrants analytical or policy attention. The proposed framework is fully reproducible, scalable, and compatible with existing validation workflows, offering a flexible tool for early detection of unusual regional configurations within the European Statistical System.
匹配关键词: preference learning
---

[ACADEMIC - ARXIV]
标题: Multi-fidelity surrogates for mechanics of composites: from co-kriging to multi-fidelity neural networks
作者: Haizhou Wen, Elham Kiyani, Gang Li, Srikanth Pilla, George Em Karniadakis, Zhen Li
链接: https://arxiv.org/abs/2605.02871v1
完整摘要: Composite materials exhibit strongly hierarchical and anisotropic properties governed by coupled mechanisms spanning constituents, plies, laminates, structures, and manufacturing history. This intrinsic complexity makes predictive modeling of composites expensive, because repeated experiments and high-fidelity simulations are needed to cover large design spaces of material, structure, and manufacturing. Multi-fidelity surrogate modeling addresses this challenge by combining abundant, less expensive data with limited high-accuracy data to recover reliable high-fidelity predictions. This review presents a structured overview of multi-fidelity modeling for composite mechanics, covering Gaussian-process or Kriging-based methods, including co-Kriging, coregionalization models, autoregressive formulations, nonlinear autoregressive Gaussian processes, multi-fidelity deep Gaussian processes, and multi-fidelity neural networks. Their distinctions are examined in terms of cross-fidelity correlation, discrepancy representation, uncertainty quantification, and scalability. Selected examples of their applications to composites are introduced according to the roles that multi-fidelity surrogates play in engineering problems, including forward prediction for rapid exploration of material design spaces, inverse optimization for composite parameter identification and design search under limited high-fidelity access, and workflow integration, where heterogeneous data sources, constraints, and validation requirements determine model utility. Open question discussions highlight recurring challenges specific to composites, such as regime-dependent fidelity gaps associated with nonlinear damage and manufacturing history, mismatches between simulations and experiments, and uncertainty propagation across multi-fidelity models.
匹配关键词: preference learning
---

[ACADEMIC - ARXIV]
标题: Enhancing RL Generalizability in Robotics through SHAP Analysis of Algorithms and Hyperparameters
作者: Lingxiao Kong, Cong Yang, Oya Deniz Beyan, Zeyd Boukhers
链接: https://arxiv.org/abs/2605.02867v1
完整摘要: Despite significant advances in Reinforcement Learning (RL), model performance remains highly sensitive to algorithm and hyperparameter configurations, while generalization gaps across environments complicate real-world deployment. Although prior work has studied RL generalization, the relative contribution of specific configurations to the generalization gap has not been quantitatively decomposed and systematically leveraged for configuration selection. To address this limitation, we propose an explainable framework that evaluates RL performance across robotic environments using SHapley Additive exPlanations (SHAP) to quantify configuration impacts. We establish a theoretical foundation connecting Shapley values to generalizability, empirically analyze configuration impact patterns, and introduce SHAP-guided configuration selection to enhance generalization. Our results reveal distinct patterns across algorithms and hyperparameters, with consistent configuration impacts across diverse tasks and environments. By applying these insights to configuration selection, we achieve improved RL generalizability and provide actionable guidance for practitioners.
匹配关键词: preference learning
---

[ACADEMIC - ARXIV]
标题: Pixel Perfect: Relational Image Quality Assessment with Spatially-Aware Distortions
作者: Fadeel Sher Khan, Long N. Le, Abhinau K. Venkataramanan, Seok-Jun Lee, Hamid R. Sheikh
链接: https://arxiv.org/abs/2605.02863v1
完整摘要: Traditional image quality assessment (IQA) methods rely on mean opinion scores (MOS), which are resource-intensive to collect and fail to provide interpretable, localized feedback on specific image distortions. We overcome these limitations by shifting from absolute quality prediction to a relational and directional assessment. Our approach utilizes a self-supervised synthetic distortion engine to generate training data, eliminating the need for manual annotation. A distortion prediction network is trained with an anti-symmetric objective to produce spatially-aware, disentangled maps that identify the type, intensity, and direction of distortions relative to a reference image. Subsequently, a scoring network is trained via contrastive learning on ordinally ranked image sets to predict a relational quality score. Our method provides a more granular and interpretable approach to IQA for the targeted optimization of image processing algorithms without requiring any human-labeled quality scores.
匹配关键词: preference learning
---

[ACADEMIC - ARXIV]
标题: MolmoAct2: Action Reasoning Models for Real-world Deployment
作者: Haoquan Fang, Jiafei Duan, Donovan Clay, Sam Wang, Shuo Liu, Weikai Huang, Xiang Fan, Wei-Chuan Tsai, Shirui Chen, Yi Ru Wang, Shanli Xing, Jaemin Cho, Jae Sung Park, Ainaz Eftekhar, Peter Sushko, Karen Farley, Angad Wadhwa, Cole Harrison, Winson Han, Ying-Chun Lee, Eli VanderBilt, Rose Hendrix, Suveen Ellawela, Lucas Ngoo, Joyce Chai, Zhongzheng Ren, Ali Farhadi, Dieter Fox, Ranjay Krishna
链接: https://arxiv.org/abs/2605.02881v1
完整摘要: Vision-Language-Action (VLA) models aim to provide a single generalist controller for robots, but today's systems fall short on the criteria that matter for real-world deployment. Frontier models are closed, open-weight alternatives are tied to expensive hardware, reasoning-augmented policies pay prohibitive latency for their grounding, and fine-tuned success rates remain below the threshold for dependable use. We present MolmoAct2, a fully open action reasoning model built for practical deployment, advancing its predecessor along five axes. We introduce MolmoER, a VLM backbone specialized for spatial and embodied reasoning, trained on a 3.3M-sample corpus with a specialize-then-rehearse recipe. We release three new datasets spanning low-to-medium cost platforms, including MolmoAct2-BimanualYAM, 720 hours of teleoperated bimanual trajectories that constitute the largest open bimanual dataset to date, together with quality-filtered Franka (DROID) and SO100/101 subsets. We provide OpenFAST, an open-weight, open-data action tokenizer trained on millions of trajectories across five embodiments. We redesign the architecture to graft a flow-matching continuous-action expert onto a discrete-token VLM via per-layer KV-cache conditioning. Finally, we propose MolmoThink, an adaptive-depth reasoning variant that re-predicts depth tokens only for scene regions that change between timesteps, retaining geometric grounding at a fraction of prior latency. In the most extensive empirical study of any open VLA to date, spanning 7 simulation and real-world benchmarks, MolmoAct2 outperforms strong baselines including Pi-05, while MolmoER surpasses GPT-5 and Gemini Robotics ER-1.5 across 13 embodied-reasoning benchmarks. We release model weights, training code, and complete training data. Project page: https://allenai.org/blog/molmoact2
匹配关键词: benchmark
---

[ACADEMIC - ARXIV]
标题: Active Sampling for Ultra-Low-Bit-Rate Video Compression via Conditional Controlled Diffusion
作者: Amirhosein Javadi, Shirin Saeedi Bidokhti, Tara Javidi
链接: https://arxiv.org/abs/2605.02849v1
完整摘要: Diffusion models provide a powerful generative prior for perceptual reconstruction at ultra-low bitrates, but effective video compression requires controlling the generative process using highly compact conditioning signals. In this work, we present ActDiff-VC, a diffusion-based video compression framework for the ultra-low-bitrate regime. Our method partitions videos into variable-length segments, transmits keyframes only when needed, and summarizes temporal dynamics using a compact set of tracked point trajectories. Conditioned on these sparse signals, a conditional diffusion decoder synthesizes the remaining frames, enabling perceptually realistic reconstruction under severe rate constraints. To support this design, we introduce two mechanisms: content-adaptive keyframe selection and budget-aware sparse trajectory selection, which together enable compact yet effective conditioning for generative reconstruction. Experiments on the UVG and MCL-JCV benchmarks show that ActDiff-VC achieves up to 64.6\% bitrate reduction at matched NIQE, improves KID by up to 64.6\% and FID by up to 37.7\% at comparable bitrates against strong learned codecs, and delivers favorable perceptual rate--distortion trade-offs relative to learned and diffusion-based baselines in the ultra-low-bitrate regime.
匹配关键词: benchmark
---

[ACADEMIC - ARXIV]
标题: A Closed-Form Persistence-Landmark Pipeline for Certified Point-Cloud and Graph Classification
作者: Sushovan Majhi, Atish Mitra, Žiga Virk, Pramita Bagchi
链接: https://arxiv.org/abs/2605.02836v1
完整摘要: We introduce PLACE (Persistence-Landmark Analytic Classification Engine), a closed-form pipeline for classifying point clouds and graphs through their persistent-homology signatures. Three quantitative guarantees -- a margin-based excess-risk rate, a closed-form descriptor-selection rule, and a per-prediction certificate -- are derived from training labels alone, with no learned weights or held-out calibration. The embedding sums Mitra-Virk single-point coordinate functions over a sparse landmark grid; closed-form weights maximize a structural distortion constant $λ(ν)$ (a Lipschitz lower bound on $\mathcal{D}_n$ under non-interference). (i) An $O(kR/(Δ\sqrt{m_{\min}}))$ margin bound, driven by class-mean separation $Δ$ and embedding radius $R$, matched by a sample-starved minimax lower bound. (ii) The Mahalanobis margin under Ledoit-Wolf-shrunk covariance is the strongest closed-form descriptor selector on a heterogeneous 64-descriptor chemical-graph pool (mean Spearman $ρ\approx +0.54$ across 10 benchmarks, positive on 9 of 10); the isotropic surrogate $Δ/\sqrt\ell$ admits a closed-form selection-consistency rate on homogeneous (14-15 descriptor) protein/social pools. (iii) A training-time-decided certificate with no per-prediction overhead, in non-asymptotic Pinelis and asymptotic Gaussian plug-in forms. Empirically, PLACE is the strongest diagram-based method on Orbit5k and matches the strongest topology-based baseline within statistical noise on MUTAG and COX2. The remaining gaps fall into two diagnosable regimes: descriptor blindness on NCI1/NCI109, and pool-coverage limits elsewhere. Both radii exceed the firing threshold $\hatΔ/2$ on every benchmark at our training-set sizes, dominated by the $\sqrt\ell$ scaling of the multivariate-norm bound; the per-prediction certificate is constructive but not yet operational at these sizes.
匹配关键词: benchmark
---

[ACADEMIC - ARXIV]
标题: VideoNet: A Large-Scale Dataset for Domain-Specific Action Recognition
作者: Tanush Yadav, Mohammadreza Salehi, Jae Sung Park, Vivek Ramanujan, Hannaneh Hajishirzi, Yejin Choi, Ali Farhadi, Rohun Tripathi, Ranjay Krishna
链接: https://arxiv.org/abs/2605.02834v1
完整摘要: Videos are unique in their ability to capture actions which transcend multiple frames. Accordingly, for many years action recognition was the quintessential task for video understanding. Unfortunately, due to a lack of sufficiently diverse and challenging data, modern vision-language models (VLMs) are no longer evaluated on their action recognition capabilities. To revitalize action recognition in the era of VLMs, we advocate for a returned focus on domain-specific actions. To this end, we introduce VideoNet, a domain-specific action recognition benchmark covering 1,000 distinct actions from 37 domains. We begin with a multiple-choice evaluation setting, where the difference between closed and open models is stark: Gemini 3.1 Pro attains 69.9% accuracy while Qwen3-VL-8B gets a mere 45.0%. To understand why VLMs struggle on VideoNet, we relax the questions into a binary setting, where random chance is 50%. Still, Qwen achieves only 59.2% accuracy. Further relaxing the evaluation setup, we provide $k\in\{1,2,3\}$ in-context examples of the action. Some models excel in the few-shot setting, while others falter; Qwen improves $+7.0\%$, while Gemini declines $-4.8\%$. Notably, these gains fall short of the $+13.6\%$ improvement in non-expert humans when given few-shot examples. Finding that VLMs struggle to fully exploit in-context examples, we shift from test-time improvements to the training side. We collect the first large-scale training dataset for domain-specific actions, totaling nearly 500k video question-answer pairs. Fine-tuning a Molmo2-4B model on our data, we surpass all open-weight 8B models on the VideoNet benchmark.
匹配关键词: benchmark
---

[ACADEMIC - ARXIV]
标题: HAAS: A Policy-Aware Framework for Adaptive Task Allocation Between Humans and Artificial Intelligence Systems
作者: Vicente Pelechanoa, Antoni Mestre, Manoli Albert, Miriam Gil
链接: https://arxiv.org/abs/2605.02832v1
完整摘要: Deciding how to distribute work between humans and AI systems is a central challenge in organisational design. Most approaches treat this as a binary choice, yet the operational reality is richer: humans and AI routinely share tasks or take complementary roles depending on context, fatigue, and the stakes involved. Governing that distribution -- balancing efficiency, oversight, and human capability -- remains an open problem. This paper presents Human-AI Adaptive Symbiosis (HAAS), an implemented framework for adaptive task allocation in software engineering and manufacturing. HAAS combines two coupled components: a rule-based expert system that enforces governance constraints before any learning occurs, and a contextual-bandit learner that selects among feasible collaboration modes from outcome feedback. Task-agent fit is represented through five auditable cognitive dimensions and a five-mode autonomy spectrum -- from human-only to fully autonomous -- embedded in a reproducible benchmark spanning both domains. Three empirical findings emerge. First, governance is not a binary switch but a tunable design variable: tighter constraints predictably convert autonomous AI assignments into supervised collaborations, with domain-specific costs and benefits. Second, in manufacturing, stronger governance can improve operational performance and reduce fatigue simultaneously -- a workload-buffering effect that contradicts the usual framing of governance as pure overhead. Third, no single governance setting dominates across all contexts; moderate governance becomes increasingly competitive as the learner accumulates experience within the governed action space. Together, these findings position HAAS as a pre-deployment workbench for comparing and inspecting human--AI allocation policies before organisational commitment.
匹配关键词: benchmark
---

[ACADEMIC - ARXIV]
标题: Semantic Risk-Aware Heuristic Planning for Robotic Navigation in Dynamic Environments: An LLM-Inspired Approach
作者: Hamza Ahmed Durrani, Rafay Suleman Durrani
链接: https://arxiv.org/abs/2605.02862v1
完整摘要: The integration of Large Language Model (LLM) reasoning principles into classical robot path planning represents a rapidly emerging research direction. In this paper, we propose a Semantic Risk-Aware Heuristic (SRAH) planner that encodes LLM-inspired cost functions penalising geometrically cluttered or high-risk zones into an A$^*$ search framework, augmented with closed-loop replanning upon dynamic obstacle detection. We evaluate SRAH against two established baselines Breadth-First Search (BFS) with replanning and a Greedy heuristic without replanning across 200 randomised trials in a $15{\times}15$ grid-world with 20\% static obstacle density and stochastic dynamic obstacles. SRAH achieves a task success rate of 62.0\%, outperforming BFS (56.5\%) by 9.7\% relative improvement and Greedy (4.0\%) by a large margin. We further analyse the trade-off between planning overhead, path efficiency, and failure-recovery count, and demonstrate via an obstacle-density ablation that semantic cost shaping consistently improves navigation across environments of varying difficulty. Our results suggest that even lightweight, LLM-inspired heuristics provide measurable safety and robustness gains for autonomous robot navigation.
匹配关键词: safety
---

[ACADEMIC - ARXIV]
标题: A decoupled diffusion planner that adapts to changing cost limits by using cost-conditioned generation for safety and reward gradients for performance
作者: Rufeng Chen, Zhaofan Zhang, Zhejiang Yang, Hechang Chen, Sihong Xie
链接: https://arxiv.org/abs/2605.02777v1
完整摘要: Offline safe reinforcement learning often requires policies to adapt at deployment time to safety budgets that vary across episodes or change within a single episode. While diffusion-based planners enable flexible trajectory generation, existing guidance schemes often treat reward improvement and constraint satisfaction as competing gradient objectives, which can lead to unreliable safety compliance under cost limits. We reinterpret adaptive safe trajectory generation as sampling from a constrained trajectory distribution, where the budget restricts the trajectory region, and reward shapes preferences within that region. This perspective motivates Safe Decoupled Guidance Diffusion (SDGD), which conditions classifier-free guidance on the cost limit to bias sampling toward trajectories satisfying the specified limit, while using reward-gradient guidance to refine trajectories for higher return. Because direct reward guidance can increase return while also steering samples toward trajectories with higher cumulative cost, we introduce Feasible Trajectory Relabeling (FTR) to reshape reward targets and discourage such directions. We further provide a first-order sampling-time analysis showing that FTR suppresses reward-induced cost drift under a prefix-restorative alignment condition. Extensive evaluations on the DSRL benchmark show that SDGD achieves the strongest safety compliance among baselines, satisfying the constraint on 94.7% of tasks (36/38), while obtaining the highest reward among safe methods on 21 tasks.
匹配关键词: safety
---

[ACADEMIC - ARXIV]
标题: DynoSLAM: Dynamic SLAM with Generative Graph Neural Networks for Real-World Social Navigation
作者: Danil Tokhchukov, Veronika Morozova, Gonzalo Ferrer
链接: https://arxiv.org/abs/2605.02759v1
完整摘要: Traditional Simultaneous Localization and Mapping (SLAM) algorithms rely heavily on the static environment assumption, which severely limits their applicability in real-world spaces populated by moving entities, such as pedestrians. In this work, we propose DynoSLAM, a tightly-coupled Dynamic GraphSLAM architecture that integrates socially-aware Graph Neural Networks (GNNs) directly into the factor graph optimization. Unlike conventional approaches that use rigid constant-velocity heuristics or deterministic single-agent neural priors, our framework formulates pedestrian motion forecasting as a stochastic World Model. By utilizing Monte Carlo rollouts from a trained GNN, we capture the multimodal epistemic uncertainty of human interactions and embed it into the SLAM graph via a dynamic Mahalanobis distance factor. We demonstrate through extensive simulated experiments that this stochastic formulation not only maintains highly accurate retrospective tracking but also prevents the optimization failures caused by the deterministic "argmax problem". Ultimately, extracting the empirical mean and covariance matrices of future pedestrian states provides a mathematically rigorous, probabilistic safety envelope for downstream local planners, enabling anticipatory and collision-free robot navigation in densely crowded environments.
匹配关键词: safety
---

[ACADEMIC - ARXIV]
标题: Parking Assistance for Trailer-Truck Transport Vehicles Using Sensor Fusion and Motion Planning
作者: George Alenchery, Thomas Jeske, Tova Quinones, Lentz Fortune, Tristan Lindo-Slones, Amber Jones, Jordan Fletcher
链接: https://arxiv.org/abs/2605.02716v1
完整摘要: Autonomous driving technology has rapidly evolved over the past decade, offering significant improvements in transportation efficiency, safety, and cost reduction. While much of the progress has focused on highway driving and obstacle avoidance, low-speed maneuvers such as parking remain among the most difficult challenges for autonomous systems. This challenge is especially pronounced in trailer-truck transport vehicles due to their articulated motion and environmental constraints. This paper presents a proposed framework for autonomous truck parking that integrates perception, motion planning, control systems, and infrastructure awareness. By combining sensor fusion, Hybrid A* path planning, nonlinear model predictive control (NMPC), and data-driven parking systems, this work highlights the importance of system-level coordination for reliable and scalable autonomous parking solutions. As a proof-of-concept implementation, we adapted an open-source A* path planning simulation to incorporate a tractor-trailer kinematic model, demonstrating articulated vehicle path planning within a command-line simulation environment, with jackknife prevention identified as an area requiring further development.
匹配关键词: safety
---

[ACADEMIC - ARXIV]
标题: An Empirical Study of Agent Skills for Healthcare: Practice, Gaps, and Governance
作者: Gelei Xu, Ningzhi Tang, Xueyang Li, Toby Jia-Jun Li, Zhi Zheng, Wei Jin, Yiyu Shi
链接: https://arxiv.org/abs/2605.02709v1
完整摘要: Healthcare automation is shaped by local procedures and organizational constraints, so agent capabilities rarely transfer unchanged across settings. Agent skills, self-contained directories that package reusable procedures for AI agents, are emerging as a procedural layer for adapting healthcare agents across diverse healthcare settings. We present the first empirical analysis of healthcare agent skills, drawing on 557 healthcare-related skills filtered from 58,159 public skills on ClawHub and annotated along ten dimensions covering function, deployment context, autonomy, and safety. We find that public healthcare skills emphasize patient-facing workflow automation and monitoring rather than the diagnostic and treatment-oriented tasks foregrounded in healthcare-agent research; coverage of the healthcare lifecycle and specialized clinical inputs remains uneven; and general technical risk does not reliably capture clinical risk. These findings position healthcare skills as a procedural layer not yet addressed by current benchmarks and risk frameworks.
匹配关键词: safety
---

