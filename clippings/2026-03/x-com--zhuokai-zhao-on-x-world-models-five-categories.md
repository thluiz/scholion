---
url: "https://x.com/zhuokaiz/status/2032201769053212682?utm_source=tldrai"
captured_at: "2026-03-12T21:07:12+00:00"
title: "Zhuokai Zhao (@zhuokaiz) on X"
domain: "x-com"
---

AMI Labs just raised $1.03B. World Labs raised $1B a few weeks earlier. Both are betting on world models.

But almost nobody means the same thing by that term.

Here are, in my view, five categories of world models.

---

1. Joint Embedding Predictive Architecture (JEPA)
Representatives: AMI Labs (@ylecun), V-JEPA 2

The central bet here is that pixel reconstruction alone is an inefficient objective for learning the abstractions needed for physical understanding. LeCun has been saying this for years — predicting every pixel of the future is intractable in any stochastic environment. JEPA sidesteps this by predicting in a learned latent space instead.

Concretely, JEPA trains an encoder that maps video patches to representations, then a predictor that forecasts masked regions in that representation space — not in pixel space. 

This is a crucial design choice. 

A generative model that reconstructs pixels is forced to commit to low-level details (exact texture, lighting, leaf position) that are inherently unpredictable. By operating on abstract embeddings, JEPA can capture "the ball will fall off the table" without having to hallucinate every frame of it falling.

V-JEPA 2 is the clearest large-scale proof point so far. It's a 1.2B-parameter model pre-trained on 1M+ hours of video via self-supervised masked prediction — no labels, no text. The second training stage is where it gets interesting: just 62 hours of robot data from the DROID dataset is enough to produce an action-conditioned world model that supports zero-shot planning. The robot generates candidate action sequences, rolls them forward through the world model, and picks the one whose predicted outcome best matches a goal image. This works on objects and environments never seen during training.

The data efficiency is the real technical headline. 62 hours is almost nothing. It suggests that self-supervised pre-training on diverse video can bootstrap enough physical prior knowledge that very little domain-specific data is needed downstream. That's a strong argument for the JEPA design — if your representations are good enough, you don't need to brute-force every task from scratch.

AMI Labs is LeCun's effort to push this beyond research. They're targeting healthcare and robotics first, which makes sense given JEPA's strength in physical reasoning with limited data. But this is a long-horizon bet — their CEO has openly said commercial products could be years away.

---

2. Spatial Intelligence (3D World Models)
Representative: World Labs (@drfeifei)

Where JEPA asks "what will happen next," Fei-Fei Li's approach asks "what does the world look like in 3D, and how can I build it?" 

The thesis is that true understanding requires explicit spatial structure — geometry, depth, persistence, and the ability to re-observe a scene from novel viewpoints — not just temporal prediction. 

This is a different bet from JEPA: rather than learning abstract dynamics, you learn a structured 3D representation of the environment that you can manipulate directly.

Their product Marble generates persistent 3D environments from images, text, video, or 3D layouts. "Persistent" is the key word — unlike a video generation model that produces a linear sequence of frames, Marble's outputs are actual 3D scenes with spatial coherence. You can orbit the camera, edit objects, export meshes. This puts it closer to a 3D creation tool than to a predictive model, which is deliberate.

For context, this builds on a lineage of neural 3D representation work (NeRFs, 3D Gaussian Splatting) but pushes toward generation rather than reconstruction. Instead of capturing a real scene from multi-view photos, Marble synthesizes plausible new scenes from sparse inputs. The challenge is maintaining physical plausibility — consistent geometry, reasonable lighting, sensible occlusion — across a generated world that never existed.

---

3. Learned Simulation (Generative Video + Latent-Space RL)
Representatives: Google DeepMind (Genie 3, Dreamer V3/V4), Runway GWM-1

This category groups two lineages that are rapidly converging: generative video models that learn to simulate interactive worlds, and RL agents that learn world models to train policies in imagination.

The video generation lineage. DeepMind's Genie 3 is the purest version — text prompt in, navigable environment out, 24 fps at 720p, with consistency for a few minutes. Rather than relying on an explicit hand-built simulator, it learns interactive dynamics from data. The key architectural property is autoregressive generation conditioned on user actions: each frame is generated based on all previous frames plus the current input (move left, look up, etc.). This means the model must maintain an implicit spatial memory — turn away from a tree and turn back, and it needs to still be there. DeepMind reports consistency up to about a minute, which is impressive but still far from what you'd need for sustained agent training.

Runway's GWM-1 takes a similar foundation — autoregressive frame prediction built on Gen-4.5 — but splits into three products: Worlds, Robotics, and Avatars. The split into Worlds / Avatars / Robotics suggests the practical generality problem is still being decomposed by action space and use case.

The RL lineage. The Dreamer series has the longer intellectual history. The core idea is clean: learn a latent dynamics model from observations, then roll out imagined trajectories in latent space and optimize a policy via backpropagation through the model's predictions. The agent never needs to interact with the real environment during policy learning.

Dreamer V3 was the first AI to get diamonds in Minecraft without human data. Dreamer 4 did the same purely offline — no environment interaction at all. Architecturally, Dreamer 4 moves from Dreamer’s earlier recurrent-style lineage to a more scalable transformer-based world-model recipe, and introduced "shortcut forcing" — a training objective that lets the model jump from noisy to clean predictions in just 4 steps instead of the 64 typical in diffusion models. This is what makes real-time inference on a single H100 possible. 

These two sub-lineages used to feel distinct: video generation produces visual environments, while RL world models produce trained policies. 

But Dreamer 4 blurred the line — humans can now play inside its world model interactively, and Genie 3 is being used to train DeepMind's SIMA agents. 

The convergence point is that both need the same thing: a model that can accurately simulate how actions affect environments over extended horizons.

The open question for this whole category is one LeCun keeps raising: does learning to generate pixels that look physically correct actually mean the model understands physics? Or is it pattern-matching appearance? Dreamer 4's ability to get diamonds in Minecraft from pure imagination is a strong empirical counterpoint, but it's also a game with discrete, learnable mechanics — the real world is messier.

---

4. Physical AI Infrastructure (Simulation Platform)
Representative: NVIDIA Cosmos

NVIDIA's play is don't build the world model, build the platform everyone else uses to build theirs. 

Cosmos launched at CES January 2025 and covers the full stack — data curation pipeline (process 20M hours of video in 14 days on Blackwell, vs. 3+ years on CPU), a visual tokenizer with 8x better compression than prior SOTA, model training via NeMo, and deployment through NIM microservices.

The pre-trained world foundation models are trained on 9,000 trillion tokens from 20M hours of real-world video spanning driving, industrial, robotics, and human activity data. 

They come in two architecture families: diffusion-based (operating on continuous latent tokens) and autoregressive transformer-based (next-token prediction on discretized tokens). Both can be fine-tuned for specific domains.

Three model families sit on top of this. 
Predict generates future video states from text, image, or video inputs — essentially video forecasting that can be post-trained for specific robot or driving scenarios. 
Transfer handles sim-to-real domain adaptation, which is one of the persistent headaches in physical AI — your model works great in simulation but breaks in the real world due to visual and dynamics gaps. 
Reason (added at GTC 2025) brings chain-of-thought reasoning over physical scenes — spatiotemporal awareness, causal understanding of interactions, video Q&A.

---

5. Active Inference
Representative: VERSES AI (Karl Friston)

This is the outlier on the list — not from the deep learning tradition at all, but from computational neuroscience.

Karl Friston's Free Energy Principle says intelligent systems continuously generate predictions about their environment and act to minimize surprise (technically: variational free energy, an upper bound on surprise).

Where standard RL is usually framed around reward maximization, active inference frames behavior as minimizing variational / expected free energy, which blends goal-directed preferences with epistemic value. This leads to natural exploration behavior: the agent is drawn to situations where it's uncertain, because resolving uncertainty reduces free energy.

VERSES built AXIOM (Active eXpanding Inference with Object-centric Models) on this foundation. 

The architecture is fundamentally different from neural network world models. Instead of learning a monolithic function approximator, AXIOM maintains a structured generative model where each entity in the environment is a discrete object with typed attributes and relations. 

Inference is Bayesian — beliefs are probability distributions that get updated via message passing, not gradient descent. This makes it interpretable (you can inspect what the agent believes about each object), compositional (add a new object type without retraining), and extremely data-efficient.

In their robotics work, they've shown a hierarchical multi-agent setup where each joint of a robot arm is its own active inference agent. The joint-level agents handle local motor control while higher-level agents handle task planning, all coordinating through shared beliefs in a hierarchy. The whole system adapts in real time to unfamiliar environments without retraining — you move the target object and the agent re-plans immediately, because it's doing online inference, not executing a fixed policy.

They shipped a commercial product (Genius) in April 2025, and the AXIOM benchmarks against RL baselines are competitive on standard control tasks while using orders of magnitude less data.

---

imo, these five categories aren't really competing — they're solving different sub-problems.

JEPA compresses physical understanding.
Spatial intelligence reconstructs 3D structure. 
Learned simulation trains agents through generated experience. 
NVIDIA provides the picks and shovels. 
Active inference offers a fundamentally different computational theory of intelligence.

My guess is the lines between them blur fast.
