---
title: "On-Policy Distillation"
date: '2025-10-28T18:19:12+00:00'
category: webclip
summary: 'The post argues that on-policy distillation combines on-policy sampling with dense teacher scoring, improving reasoning, personalization, and continual learning while using less compute than RL.'
tags: ["on-policy-distillation", "distillation", "reinforcement-learning", "continual-learning"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "On-Policy Distillation - Thinking Machines Lab"
    url: "https://thinkingmachines.ai/blog/on-policy-distillation/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2025-10/thinkingmachines-ai--on-policy-distillation-thinking-machines-lab.md"
    kind: repo
---

On-policy distillation samples trajectories from the student and uses a teacher to score each token, aiming to combine the on-policy relevance of RL with the dense supervision of distillation. The post presents it as a cheap post-training method for reasoning and personalization, and as a useful tool for continual learning.

## Reading notes

- LLMs are described as stacking capabilities from pre-training, mid-training, and post-training, with smaller specialized models often being better in trained domains and cheaper to deploy.
- The post contrasts on-policy training, which samples from the student, with off-policy training, which learns from external targets.
- RL is presented as on-policy but sparse, since it gives feedback only at the episode level and not at the token level.
- Distillation is presented as off-policy supervision from teacher trajectories, including intermediate thinking steps, and can use teacher log probabilities or sampled sequences.
- On-policy distillation is defined as sampling from the student and grading each token with a strong teacher.
- The method is compared with SFT and RL in a table, with on-policy distillation combining on-policy sampling and dense reward.
- The implementation uses per-token reverse KL between student and teacher distributions, with zero discounting and no separate reward model.
- The post says reverse KL is useful because low KL corresponds to high teacher probability, and because it is mode seeking.
- In the reasoning experiments, a Qwen3-8B-Base student is trained with Qwen3-32B as teacher, starting from off-policy distillation on OpenThoughts-3 prompts.
- Off-policy distillation improves AIME’24 scores, but the text says extending it to reach higher scores would require much more data.
- RL on top of the same initialization reaches higher benchmark scores, but at much higher compute cost.
- On-policy distillation reaches strong benchmark performance after about 150 steps from the SFT checkpoint, with lower compute than RL.
- The post reports that on-policy distillation gives a large compute-efficiency gain and can reduce cost relative to SFT extrapolation.
- For personalization, the post uses an internal assistant example combining internal document knowledge with instruction following.
- Mid-training on internal documents improves knowledge but degrades instruction-following behavior, even when background chat data is mixed in.
- LoRA reduces forgetting somewhat, but the post says it still does not preserve the original post-trained behavior.
- On-policy distillation with an earlier Qwen3-8B model as teacher restores most instruction-following performance after mid-training, while keeping the gained knowledge.
- The discussion says dense supervision can make learning much more compute-efficient than RL.
- The post also says distillation can reuse the same prompts across multiple epochs without collapsing into simple answer memorization in the way RL may.
- RL is framed as search over semantic strategies, while distillation is presented as a shortcut for learning the final strategy.
- For continual learning, the post argues that on-policy distillation avoids the regressions seen when SFT is run on a model’s own samples.
- The conclusion says on-policy distillation combines reliable on-policy learning with the cost efficiency of dense rewards, and is useful for frontier capabilities, adaptability, and personalization.
