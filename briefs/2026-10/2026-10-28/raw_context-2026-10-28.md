# 破晓 PoXiao 数据快照 · 2026-10-28
# 生成时间: 2026-10-28 07:10:17
# 说明: vibe_fetch 未运行（arXiv 429 限流），本文件为 gen_brief.sh + HF API 的数据存档

## [HF DAILY PAPERS] 共 15 篇 (完整摘要)

### Trajectory2Gym: Decision-Grounded Compositional Interaction Synthesis for Tool-Use Agents
- arxiv: https://arxiv.org/abs/2610.33568
- authors: Yihao Hu, Zhihao Wen, Yitong Lin, Siyuan Lu, Pan Wang, Wei Wu
- summary: Successful tool-use trajectories are not necessarily useful supervision. Even successful interactions may underrepresent multi-step dependencies or contain actions that are unjustified by the information visible to the agent at decision time. We identify two coupled requirements for effective trajectory supervision: compositional coverage, so that important observation-action dependencies are represented, and decision grounding, so that each supervised action is supported by the learner-visible interaction history. We introduce Trajectory2Gym, which constructs executable interactions around under-supported compositional structures and derives supervision only from grounded decisions in their realized executions. Structural-support selection allocates the resulting experience, while parent-normalized supervised fine-tuning preserves the semantic interaction as the unit of training weight. This reframes trajectory generation as the deliberate construction of learnable interaction experience, rather than the collection of successful trajectories. Across five Qwen3 scales, Trajectory2Gym improves Tau1, Tau2, and BFCL at every tested scale, increasing the equal-weight three-benchmark mean by 16.9-29.8 percentage points. The gains are strongest in stateful and multi-turn interaction, where later decisions depend on earlier observations and feedback. Our results suggest that scaling tool-use agents depends not only on collecting more successful trajectories, but on constructing interactions whose dependencies are represented and whose decisions are learnable from the agent's visible history.

### StreamVibe: Proactive Video Agents for Evolving User Intent
- arxiv: https://arxiv.org/abs/2610.34662
- authors: Chengzhi Liu, Yuxiang Lai, Yuzhe Yang, Yanqing Liu, Jiheng Hou, Yue Cao
- summary: Vision-language models are shifting from offline passive understanding toward online proactive interaction. However, prevailing methods largely rely on explicit requests while miss the implicit user intent (e.g., "where should I click next?" while a user navigate a website), meanwhile fail to update the state simultaneously as user requests might update continuously. These limitations make them less suited to intent-aware interaction in practical. To address these challenges, we introduce StreamVibe-Bench, a new benchmark serving as testbed for user intent interaction, with 4.1K evaluation samples and 85K training samples spanning explicit, implicit, and dynamic intents. Building on this benchmark, we develop StreamVibe-VL, a streaming proactive model that infers implicit user intents from continuous observations and dynamically tailors its interactions as these intents evolve. We further introduce StreamVibe-Harness, which maintains user intents as persistent states with a fleixble lifecycles via a hierarchical memory to track the latest user intent and environmental state. Our experiments reveal three key findings: (i) StreamVibe-VL preserves strong general video understanding while improving response timing and answer quality by 10.7% over other baselines; (ii) existing proactive models remain limited in understanding user intent and deciding when to respond, especially under implicit and dynamic intents; and (iii) StreamVibe-Harness further improves response consistency and adaptation over sustained interaction, resulting in a 12.3% gain in proactive interaction.

### Trial by Trace: Benchmarking AI Agent Harnesses for Reliability and Failure Attribution
- arxiv: https://arxiv.org/abs/2610.32285
- authors: Zhiyong Cao, Hengjie Zhu, Yongxin Wang, Xuchen Li, Jintao Li, Shuxia Liu
- summary: LLM agents are increasingly used to solve real-world problems, and their effectiveness depends on both the underlying models and the harnesses that support their operation. However, most existing benchmarks focus on model capabilities and overall agent performance, with limited attention to the evaluation of agent harnesses. To address this gap, we introduce TraceTrial-Bench, which organizes harness reliability into seven components covering context, execution, governance, lifecycle, observability, tools, and verification. We construct 95 expert-level, mechanism-oriented tasks with executable or state-based ground truth to support semantically equivalent comparisons while preserving the native behavior of each harness. We design a Trajectory Tracing (TT) module to capture agent execution traces and introduce a two-layer evaluation framework that separately assesses agent performance and harness reliability. In addition, we design a Multi-source Evidence Acquisition (MEA) module to provide evidence from the agent context, harness, and execution environment for LLM-based evaluation, and develop a Failure Attribution (FA) module that uses explicit mechanism chains to support attribution at the run level. Across 4 harnesses, 9 models, and 95 tasks, our evaluation of 3,420 runs yields macro-averaged harness scores ranging from 59.8% to 72.0%, while 31.1% of runs achieve task success despite failing at least one harness criterion. TraceTrial-Bench provides an auditable and reproducible foundation for comparing agent harnesses, diagnosing their failures, and studying how harness design interacts with model behavior.

### DynaFlow: Learning Free-Form Multi-Agent Orchestration
- arxiv: https://arxiv.org/abs/2610.34467
- authors: Ruhao Liu, Qi Li, Shizun Wang, Xinchao Wang
- summary: Multi-agent systems often rely on predefined collaboration structures, limiting their ability to adapt to diverse task requirements. We introduce DynaFlow, a framework that integrates free-form executable workflow synthesis into the action space of the main agent. The agent decides when collaboration is needed and generates task-specific programs that coordinate sub-agents through sequential or parallel execution, structured information exchange, and verification. Execution results and traces inform subsequent actions, enabling the agent to adapt collaboration as reasoning progresses. We train only the main agent through supervised fine-tuning on distilled trajectories, followed by refinement on examples filtered for unsupported premises, biased verification, and information-flow defects. All sub-agents remain fixed, separating orchestration learning from executor capability improvement. Across six benchmarks spanning mathematical reasoning, scientific question answering, and multi-hop retrieval, DynaFlow achieves 88.08% overall accuracy in Forced mode, outperforming the strongest evaluated baseline by 10.90 percentage points with the same Qwen3.5-27B backbone. Workflow analysis finds more explicit use, verification, and refinement of upstream outputs after training, highlighting cross-stage information flow as a key dimension of multi-agent orchestration.

### InteractiveWorld: A Verifiable Human-Centric Environment for Building Better Interactive MLLM Assistants
- arxiv: https://arxiv.org/abs/2610.33966
- authors: Qinsi Wang, Wei Wen, Chong Zhou, Saksham Suri, Zechun Liu, Lemeng Wu
- summary: People have long dreamed of an assistant that is always there to guide them and remind what they forget, from new dishes to lost keys. Powered by multimodal large language models (MLLMs), egocentric AI assistants on wearable devices are bringing this dream within reach: they see what the user sees and give instructions for user's physical work when necessary. However, testing such assistance is challenging and usually requires real people. The expensive and rare real interaction data leaves a key question unanswered: Can today's MLLMs truly help people in physical world? To answer this question, we propose InteractiveWorld, the first verifiable environment for closed-loop interaction between human and AI assistant. Unlike existing robot-centric simulators, InteractiveWorld lets the assistant guide a human agent who observes the scene, understands instructions, and acts independently. It thus realistically simulates how AI assistant collaborates with human: the assistant instructs, the human acts, and the environment executes actions and updates what they see next. Building on it, we introduce InteractiveBench, the first dynamic benchmark for egocentric AI assistants, with 120 multi-turn tasks across six categories. In each task, the assistant guides the human in real time, and every instruction shapes the outcome, which is scored by verifiable, state-based rewards. Experiments with 12 frontier MLLMs show they are still far from reliable assistants. Even the strongest model, Claude Fable 5.1, achieves at most 20% and 25% on long-horizon Guidance and Planning tasks, respectively. Overall, our work offers a verifiable platform and a rigorous evaluation set, laying a solid foundation for research on interactive MLLM assistants that truly help people in the physical world.

### Work Agents: Systems, Capabilities, and Optimization
- arxiv: https://arxiv.org/abs/2610.35845
- authors: Zishan Xu, Enjun Du, Mingqi Gao, Cheng Yang, Junhao Shen, Zirong Chen
- summary: As foundation models evolve from information generation to digital work execution, agents are increasingly capable of completing complex tasks across tools, applications, and workflows. However, existing research lacks a unified perspective on how agents reliably accomplish delegated work. To address this gap, we present a work-centric, system-level perspective that views work agents as systems combining foundation models and runtime harnesses to execute tasks in stateful workspaces and deliver verifiable outcomes. We introduce two complementary dimensions, work persistence and work openness, to characterize working conditions, and classify digital work into five forms according to task scope and organization. Building on this framework, we identify five core capability families required for reliable work execution and examine approaches to model optimization, harness optimization, and their joint optimization. We further analyze existing evaluation methods and metrics from the perspective of work outcomes. Finally, we discuss future research directions, including sustained work delegation, adaptation to open environments, and the interaction between work execution and capability improvement. This paper provides a unified framework for understanding, optimizing, and evaluating work agents, supporting the development of systems capable of delivering reliable, verifiable, and practically valuable work outcomes.

### Continual Learning Exam: Benchmarking Long-Horizon RSI and Experiential Learning in LLM Agents
- arxiv: https://arxiv.org/abs/2610.33956
- authors: Haoyu Zhao, Sitian Tu, Yuxuan Huang, Huichi Zhou, Zhangyue Yin, Jiahao Huang
- summary: Continual learning is the ability of LLM agents to improve over time by acquiring, refining, and applying knowledge from experience while retaining useful prior knowledge. It is essential for agents learning over long time horizons, yet current evaluations largely assess individual task performance rather than improvement through accumulated experience. We introduce Continual Learning Exam (CLE), a large-scale benchmark developed by 50+ domain experts to measure experience-driven improvement in realistic professional workflows. CLE comprises 120 human-authored tasks, each organised as a five-level ladder, yielding 600 levels spanning 89 professional roles across 12 occupational domains. Agents must pass each level to unlock the next, with later levels building on experience accumulated during earlier assignments. An evaluation agent assesses each submission against human-authored rubrics. We compare a single-submission setting with one that provides diagnostic feedback after failure and allows one revision. Across 17 harness-model configurations using frontier LLMs, feedback and revision yield a median completion gain of 5.3 percentage points. Yet the best-performing system clears only 47.7% of levels and completes all five levels in just 23.3% of tasks, highlighting the difficulty of sustained learning from experience for existing frontier LLMs. As such, the dataset can also be used to post-train LLMs to strengthen their continual learning capabilities.

### WorldCast: World-Consistent Character Video Generation with Large-Angle Camera Control
- arxiv: https://arxiv.org/abs/2610.33135
- authors: Lei Cao, Yu Liu, Wenhua Liao, Peng Zhang, Fei Wang, Hao Zhang
- summary: Precise camera control is essential for cinematic character video generation, yet existing methods struggle to follow large-angle trajectories with combined rotation, translation, and radius variation from arbitrary initial azimuths. Such viewpoint changes also reveal character regions unseen in the initial frame, causing geometric distortions, appearance degradation, and identity drift. To systematically study these coupled challenges, we introduce CLACT, a large-scale Character-centric dataset and benchmark covering diverse Large-Angle Camera Trajectories, with accurate camera geometry and multi-view character observations for training and evaluation. We further propose WorldCast, a framework for world-consistent character video generation under diverse large-angle camera motions. Specifically, we back-project the initial frame into a 3D point cloud using estimated depth, align the point-cloud scale with the target camera trajectory, and render it along the trajectory to obtain explicit geometric guidance and coverage masks. To complement the incomplete character information, we introduce Geometry-Aligned Memory Attention (GAMA). Using relative camera poses estimated jointly from the initial frame and multi-view character anchors, we express anchor and target-view geometry in a common coordinate frame. GAMA uses this geometric alignment to guide the retrieval and injection of view-relevant character features during generation. Evaluations across diverse large-angle camera trajectories demonstrate accurate trajectory following while preserving character geometry, appearance, and identity.

### Spatial Audio Generation and Editing with Executable Plans and Self-Distilling Transfusion
- arxiv: https://arxiv.org/abs/2610.34415
- authors: Kam Man Wu, Yu Zhang, Pengjun Fang, Mingfei Chen, Weijia Chen, Zeyue Tian
- summary: Spatial audio authoring coordinates source decisions with soundfield synthesis. For editing, plans specify what to change and retain, while reference audio supplies further acoustic detail. We present AMBIT, a unified framework for native First-Order Ambisonics (FOA) generation and editing with three connected contributions. First, a shared Transfusion backbone couples autoregressive planning with rectified-flow rendering through executable ScenePlans that specify source content, activity, and 3D trajectories. For editing, the plan describes the full target scene, including retained sources; contrastive features ground the requested change, while full reference latents supply residual acoustic detail for preservation. Second, an FOA-aware continuous VAE combines shared-decoder omnidirectional recovery, asymmetric grouped KL, and spatial covariance matching to preserve content and inter-channel structure. Third, joint Transfusion on-policy self-distillation (OPSD) refines planning on student-generated prefixes and rendering at sampling states reached under student plans, with target-conditioned teachers supervising both modes of the shared student. Evaluations across speech, music, and sound show improved generation content and spatial quality, acoustic fidelity during instruction-guided editing, and unedited-source preservation over the compared baselines. Project page: https://wjm-george.github.io/AMBIT/

### AV-FABLE: Audio-Visual Manipulation Forensics in Long-Form Videos
- arxiv: https://arxiv.org/abs/2610.33413
- authors: Yuesheng Huang, Hoi Fan Au, Jiaqi Hou, Ruicheng Zhang, Jiarui He, Haocheng Yang
- summary: Localized AI manipulations in long-form videos often affect brief events within otherwise authentic content, making video-level classification insufficient for forensic analysis. Existing audio-visual deepfake benchmarks largely focus on short talking-head clips, while long-form temporal forensics remains predominantly visual. We introduce AV-FABLE, a dual-timeline benchmark for sparse manipulations in open-scene long-form audio-visual videos. AV-FABLE contains 16,650 pristine--manipulated twin pairs (998 hours) created with 27 editing configurations, with separate audio and visual timelines that enable modality-specific temporal localization and expose errors hidden by joint-timeline evaluation. On AV-FABLE, zero-shot prompting of audio-visual large language models (AV-LLMs) yields near-chance detection and poor temporal localization. In contrast, supervised readouts of their frozen perception features recover strong forensic signals, suggesting manipulation evidence is encoded in these representations but not effectively exposed through language outputs. Motivated by this observation, we propose NFSR(Native Forensics via Separated Readouts), which reads frozen AV-LLM features with separate audio and visual temporal decoders. NFSR achieves the best audio-visual localization performance in-domain and across all three out-of-distribution settings, including transfer to held-out videos from an external long-video forensic benchmark. AV-FABLE, code, and model weights will be publicly released.

### Eat Your Precision: Precision Objective Mitigates Reward Hacking in Rubric-based RL
- arxiv: https://arxiv.org/abs/2610.33512
- authors: Hyun Ryu, Jong-Heon Kim, Yiqing Xie, Seungone Kim, Carolyn Rose, Eunho Yang
- summary: Rubric-based rewards enable effective reinforcement learning on non-verifiable tasks. However, because these rewards are typically defined as a weighted measure of rubric coverage, models are trained primarily to maximize a recall objective. As a result, RL-trained models produce responses that are more complete but also more verbose and contain more unnecessary or factually incorrect content, leading them to be less preferred than responses from the base model. To address this issue, we present the FORK reward, which jointly optimizes recall and a novel precision objective, which requires each unit of a model response to be both necessary and factually correct, as measured by rubric-driven necessity credits and a factual-correctness grader, respectively. Our experimental results show that FORK outperforms existing rubric-based RL methods and achieves Pareto-optimal performance that balances rubric coverage and overall response quality. Compared to the original recall-based reward, FORK substantially improves precision and reduces response length while achieving similar rubric coverage, which leads to significantly higher win rate compared to the base policy (e.g., from 10.6% to 68.0% on RubricHub-Medical and from 22.1% to 74.1% on HealthBench).

### Principia: Test-Time Hypotheses to Principle Construction for Scientific Discovery
- arxiv: https://arxiv.org/abs/2610.32195
- authors: Dongki Kim, Sangwoo Park, Jinheon Baek, Soyeong Jeong, Sung Ju Hwang
- summary: Scientific discovery requires identifying the scientific principles underlying observed phenomena to guide further investigation. As these empirical principles are often unknown in complex discovery processes, they are constructed via a hypotheses-to-principle pipeline to obtain recurring causalities from progressively accumulated observations during test-time discovery. However, constructing this knowledge requires substantial domain expertise, time, and effort, making this translation stage a bottleneck for scientific discovery. To address this limitation, we propose Principia, an LLM-based framework that constructs and continually refines scientific principles at test time. Drawing on how human researchers develop principles, Principia forms comparative causal hypotheses from related inputs and their observed outcomes, then synthesizes recurring relationships across these hypotheses into inductive principles. By applying the constructed hypotheses and inductive principles to the task, it obtains new observations, revises the hypotheses used based on these new observations, and reconstructs principles from the updated hypotheses, allowing scientific knowledge to continuously evolve throughout test-time discovery. Across benchmarks spanning molecular optimization, protein engineering, gene perturbation, and molecular property prediction, Principia outperforms baselines relying on internal knowledge, external sources, or experience summaries, while generating principles that are plausible and consistent with the scientific literature, demonstrating its effectiveness in constructing and refining task-specific hypotheses and principles at test time for scientific discovery. Our code is available at https://github.com/DongkiKim95/Principia.

### Δτ-Bench: Pushing Agents Toward a Moving Capability
- arxiv: https://arxiv.org/abs/2610.34238
- authors: Shuofei Qiao, Xuanguang Pan, Yijun Chen, Wendi Feng, Bin Wu, Runnan Fang
- summary: In this paper, we introduce Δτ-Bench, an executable agent benchmark that models the structural evolution of large tool ecosystems. In Δτ-Bench, independently evolving services continually reshape how tasks can be accomplished: familiar tools may disappear or be replaced, while more efficient alternatives emerge amid overlapping functionality and noisy documentation. Against this moving capability frontier, we evaluate whether agents can proactively discover efficient tool-use paths and promptly revise their accumulated procedural knowledge, bringing together demands that existing benchmarks fail to examine. Δτ-Bench comprises 1,588 validated multi-turn tasks across 42 domains and six successive ecosystem states generated through capability-preserving transformations. Our evaluation shows that even the strongest evaluated model or harness achieves only 42.3% task success, while initial gains from existing skill-learning methods can not consistently translate into better adaptation as the ecosystem evolves. These findings motivate Steward, an ecosystem manager that jointly manages tools and procedural knowledge through incremental skill maintenance and dynamic provisioning during task execution. Experiments show that Steward sustains higher task success across ecosystem changes with lower skill-maintenance overhead, while improving both recovery from disrupted workflows and adoption of more efficient alternatives.

### Qwen-Image-PE: Learning Visual Design for Text-to-Image Prompt Enhancement
- arxiv: https://arxiv.org/abs/2610.33472
- authors: Zekai Zhang, Yanran Zhang, Shengming Yin, Yan Shu, Zhening Liu, Bingxuan Zhao
- summary: Learning visual design is essential for prompt enhancement (PE) to turn underspecified user requests into coherent visual specifications for text-to-image (T2I) generation. Existing methods preserve user intent and improve overall visual appeal, with less explicit emphasis on fine-grained design dimensions. To address this gap, we introduce Qwen-Image-PE, which learns visual design through two-stage training. Supervised fine-tuning with Caption-Based Reverse Distillation (CRD) uses dense captions of well-designed images as design supervision. Reinforcement learning with Groupwise Design Reward (GDR) jointly compares all candidate images for the same request to refine lighting, composition, layout, and detail. On Qwen-Image-Bench with Qwen-Image-2.1, Qwen-Image-PE-397B improves over original requests by 7.81 points, while Qwen-Image-PE-9B outperforms all evaluated PE baselines. Further evaluations show gains in visual design, aesthetics, image quality, and human preference. We find that PE scales along three axes: training data, model size, and information density, with sufficient information density as a prerequisite for effective enhancement. Moreover, we demonstrate that Qwen-Image-PE generalizes to four additional T2I backbones, even surpassing native prompt enhancers on HunyuanImage-2.1 and FLUX 3 Image Klein. We release Qwen-Image-PE-9B at https://huggingface.co/Qwen/Qwen-Image-2.1-PE-T2I.

### HiP3R: Hierarchical Pose Graphs for Long-Horizon 3D Reconstruction
- arxiv: https://arxiv.org/abs/2610.31635
- authors: Zunnan Xu, Shangchen Zhou, Yihang Luo, Chen Change Loy
- summary: Feed-forward models accurately estimate camera motion and 3D geometry from short video windows. However, computational and memory costs prevent direct inference on sequences containing thousands of frames. Long videos must therefore be processed as overlapping chunks. This division produces independent local reconstructions with inconsistent coordinate frames and duplicate estimates of shared cameras. Achieving global consistency requires propagating constraints from adjacent overlaps and distant revisits across the sequence. This requirement naturally motivates pose graph optimization. However, the choice of graph level creates a trade-off. Chunk-level graphs efficiently resolve scale drift and close large loops. Yet, their rigid transformations cannot correct internal errors or conflicting frame predictions. Conversely, frame-level optimization offers local flexibility, but scaling it globally is computationally expensive and can break metric scale. HiP3R resolves this trade-off using a hierarchical pose graph. HiP3R first optimizes a robust chunk-level Sim(3) graph to establish the global layout and scale. It then holds this layout fixed and estimates one shared SE(3) camera per frame, turning overlapping window predictions into a single trajectory. Experiments across multiple benchmarks demonstrate the effectiveness of HiP3R in improving camera trajectories and 3D reconstruction. Our method applies to both chunk-based and streaming backends without additional training or fine-tuning. The codes are available at https://kkakkkka.github.io/HiP3R.

## [HACKERNEWS] 共 20 条

[1] score=708 | US Government is hiding a secret court ruling about how it spies on Americans
    url: https://www.wired.com/story/the-us-government-is-hiding-a-secret-court-ruling-about-how-it-spies-on-americans/

[2] score=636 | Genie 4
    url: https://deepmind.google/blog/genie-4-a-new-generation-of-world-simulation/

[3] score=617 | Ghostty 1.4
    url: https://ghostty.org/docs/install/release-notes/1-4-0

[4] score=424 | Wikipedia's Cleanup of AI-Generated Content
    url: https://spectrum.ieee.org/wikipedia-wikiproject-ai-writing-cleanup

[5] score=418 | Python's experimental JIT to be removed
    url: https://lwn.net/SubscriberLink/1102102/0c00e4d550f25f8c/

[6] score=400 | Anthropic trained Claude on illegally obtained Stanford professors' books
    url: https://stanforddaily.com/2026/10/27/professors-books-pirated-to-train-claude/

[7] score=288 | New iMac with M6
    url: https://www.apple.com/imac/

[8] score=241 | New 14‑inch MacBook Pro with M6
    url: https://www.apple.com/in/newsroom/2026/10/apple-introduces-the-new-14-inch-macbook-pro-with-m6/

[9] score=193 | Amazon Is Gutting Its AI Division After Sustained Failure
    url: https://futurism.com/artificial-intelligence/amazon-ai-division-failure-nova

[10] score=181 | Discord will soon let anyone find public server messages through Google
    url: https://discord.com/blog/making-content-from-discoverable-servers-easier-to-discover

[11] score=149 | Classification of Finite Simple Groups Formalized in Lean
    url: https://cfsg.axiommath.ai/

[12] score=140 | Tailscale SSH: Investigation and remediation update
    url: https://tailscale.com/ssh-investigation-update

[13] score=139 | Here be monsters: What do you still need to know when agents do the work?
    url: https://blog.adrq.dev/here-be-monsters-what-do-you-still-need-to-know-when-agents-do-the-work

[14] score=127 | Why Micron Is Suddenly Ditching 4F² DRAM as Rivals Double Down
    url: https://hothardware.com/news/why-micron-is-suddenly-ditching-4f-dram

[15] score=120 | Survival LLM: AI assistant and emergency library that runs on your own computer
    url: https://www.brangus.io/survival-llm

[16] score=100 | Introducing LFM3: Every Modality for Specialized Intelligence
    url: https://www.liquid.ai/blog/lfm3

[17] score=80 | OpenLDK: Bringing the Java World into Common Lisp
    url: https://atgreen.github.io/repl-yell/posts/openldk-java-in-common-lisp/

[18] score=69 | Early progress on accelerating drug development with Claude
    url: https://www.anthropic.com/research/early-progress-drug-development

[19] score=64 | An examination of lost firefly species of the US and Canada
    url: https://journaloflostspecies.org/index.php/jls/article/view/37/33

[20] score=54 | Raspberry Pi Zero 3W and Pi 4 Model A spotted in device trees
    url: https://bret.dk/raspberry-pi-zero-3-w-pi-4-model-a/

## [REDDIT LocalLLaMA] 共 20 条

[1] [Bi-Weekly Megathread] Project Showcase
    link: https://www.reddit.com/r/LocalLLaMA/comments/1x9yg86/biweekly_megathread_project_showcase/

[2] I am a King, but local 😂
    link: https://www.reddit.com/r/LocalLLaMA/comments/1xgy5ic/i_am_a_king_but_local/

[3] The reason why 5090's are $10k now...
    link: https://www.reddit.com/r/LocalLLaMA/comments/1xh3iek/the_reason_why_5090s_are_10k_now/

[4] LiquidAI/LFM3-1.7B · Hugging Face
    link: https://www.reddit.com/r/LocalLLaMA/comments/1xgy8s3/liquidailfm317b_hugging_face/

[5] Debunking Cohere's claim of Qwen 3.8 Flash Next uploading to Alibaba remote URL
    link: https://www.reddit.com/r/LocalLLaMA/comments/1xgopmj/debunking_coheres_claim_of_qwen_38_flash_next/

[6] Real-time video captioning with LFM3-VL-2B running locally in-browser on WebGPU
    link: https://www.reddit.com/r/LocalLLaMA/comments/1xh0otf/realtime_video_captioning_with_lfm3vl2b_running/

[7] Statistically Lossless Qwen3.8 27B GGUFs
    link: https://www.reddit.com/r/LocalLLaMA/comments/1xh17tk/statistically_lossless_qwen38_27b_ggufs/

[8] New audio model: LFM3-Audio-2B
    link: https://www.reddit.com/r/LocalLLaMA/comments/1xh50at/new_audio_model_lfm3audio2b/

[9] Ling-3.1-flash-1019 weights are out, and they released the base model too
    link: https://www.reddit.com/r/LocalLLaMA/comments/1xgrr8n/ling31flash1019_weights_are_out_and_they_released/

[10] LiquidAI/LFM3-Omni-2B-GGUF
    link: https://www.reddit.com/r/LocalLLaMA/comments/1xh1rwn/liquidailfm3omni2bgguf/

[11] 8x R9700 System Upgrade
    link: https://www.reddit.com/r/LocalLLaMA/comments/1xgwyx9/8x_r9700_system_upgrade/

[12] OpenAI's major results over the last 3 months came from scaling test-time compute with agent swarms. I've been building an open-source equivalent for the past year, and I'd love for you guys to try it.
    link: https://www.reddit.com/r/LocalLLaMA/comments/1xh4bnd/openais_major_results_over_the_last_3_months_came/

[13] Spark-X2.6-1.7B, almost the same perf as 4b
    link: https://www.reddit.com/r/LocalLLaMA/comments/1xgw2qm/sparkx2617b_almost_the_same_perf_as_4b/

[14] inclusionAI/Ling-3.1-flash-1019 · Hugging Face
    link: https://www.reddit.com/r/LocalLLaMA/comments/1xgpo4q/inclusionailing31flash1019_hugging_face/

[15] A 1.3B OCR model just hit 93.68 on real-world document parsing and there's now an AI judge for OCR errors
    link: https://www.reddit.com/r/LocalLLaMA/comments/1xgx26j/a_13b_ocr_model_just_hit_9368_on_realworld/

[16] SenseNova 6.8 Code2Video: an open-sourced model that writes and revises code to make videos
    link: https://www.reddit.com/r/LocalLLaMA/comments/1xgvcnu/sensenova_68_code2video_an_opensourced_model_that/

[17] baidu/Unlimited-OCR-2 · Hugging Face
    link: https://www.reddit.com/r/LocalLLaMA/comments/1xgnbtq/baiduunlimitedocr2_hugging_face/

[18] I now have definitive proofs that my Qwen Flash Next is trying to send something to a remote Chinese server
    link: https://www.reddit.com/r/LocalLLaMA/comments/1xg78oq/i_now_have_definitive_proofs_that_my_qwen_flash/

[19] 4 coding agents on one RTX 3090: ~290 tok/s total from a custom CUDA engine for Qwen3.8-27B (3-4x llama-server --parallel)
    link: https://www.reddit.com/r/LocalLLaMA/comments/1xgs8hp/4_coding_agents_on_one_rtx_3090_290_toks_total/

[20] Update: My 4B coding model is getting better at generating 3D scenes
    link: https://www.reddit.com/r/LocalLLaMA/comments/1xgc7uv/update_my_4b_coding_model_is_getting_better_at/
