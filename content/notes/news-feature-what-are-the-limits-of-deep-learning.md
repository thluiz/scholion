---
title: "News Feature: What are the limits of deep learning?"
date: "2026-09-23T15:38:15+01:00"
category: webclip
summary: "PNAS profile of 2019 surveys where deep learning breaks: adversarial spoofing, data inefficiency, opacity, and the missing common sense that symbolic AI once tried to hand-code."
tags:
  - deep-learning
  - ai
  - neural-networks
  - llms
has_commentary: false
sources:
  - title: "News Feature: What are the limits of deep learning?"
    url: "https://pmc.ncbi.nlm.nih.gov/articles/PMC6347705/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/pmc-ncbi-nlm-nih-gov--news-feature-what-are-the-limits-of-deep-learning.md"
    kind: repo
---

M Mitchell Waldrop's 2019 PNAS piece opens with a deep-learning image classifier that mistakes a banana for a toaster the moment a sticker gets pasted in the corner. Geoffrey Hinton calls that kind of adversarial spoofing "probably quite profound," a sign the field is "doing something wrong." Waldrop adds three more weaknesses researchers cite alongside it: the labeled-example count a network needs versus the one or two examples a child needs, the opacity of a trained network's decisions, and its lack of common sense about what the patterns it recognizes mean.

The piece traces deep learning's roots to the 1980s "brain wars" between symbolic AI (rule-based, good at structured reasoning) and connectionist neural networks (better with noisy input, worse at fluid real-world reasoning). Three 2018-era attempts at fixing the gaps close the piece: DeepMind's multi-task training experiments, its two-network Generative Query Network architecture, and graph networks that represent objects and relations instead of raw pixels.

## Reading notes

- Adversarial attacks (a sticker that flips a banana into a toaster in the AI's output) show how far pattern recognition is from human-level robustness, per Hinton and the Google Brain team that documented the effect.
- Deep learning is data-inefficient by comparison to a child: a system often needs a concept repeated thousands of times where a child needs one or two.
- Opacity is a practical problem: David Cox (MIT-IBM Watson AI Lab) points to lending decisions, where regulation already requires an explanation the network cannot easily give.
- Gary Marcus frames the shift in public perception: deep learning had a period of looking like magic; now the limitations are visible enough that "people are realizing that it's not magic."
- The field traces back to a 1980s standoff between symbolic AI (rule-based, good at structured reasoning, bad at fluid real-world input) and connectionist neural networks (better with noisy input, but limited by the computing power of the era).
- Hinton's 2009 speech-recognition and 2012 image-recognition results, both improving on prior state of the art, triggered the deep-learning boom; DeepMind's 2015 Atari and 2016 AlphaGo results extended it into reinforcement learning.
- None of those milestones solved the underlying gaps: the Atari system needed thousands of rounds to learn what a human masters in minutes, with no understanding of what an on-screen paddle is.
- Proposed paths forward researchers were pursuing as of 2019: multi-task training that produces early "meta-learning," networks that cooperate instead of one model doing everything (DeepMind's Generative Query Network), inductive biases inspired by how infants learn intuitive physics and psychology, and graph networks that represent objects and relations instead of raw pixels.
- The essay closes on Matthew Botvinick's read: the shortcomings are real, and he still expects the technique to keep advancing past them.

Related: [I don't like LLMs](/notes/i-dont-like-llms/) registers a parallel, more contemporary discomfort with where these systems' behavior comes from.
