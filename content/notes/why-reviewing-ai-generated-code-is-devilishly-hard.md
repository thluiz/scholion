---
title: "Why reviewing AI-generated code is devilishly hard"
date: '2026-11-16T10:42:43+00:00'
category: webclip
summary: 'The post argues that reviewing AI-generated code is harder because the usual control gate is missing, metacognitive limits are weaker, LLM fluency increases trust, and automation bias raises the chance of missed faults.'
tags: ["ai-code-review", "metacognition", "automation-bias", "large-language-models"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "2026-05-23 — Why reviewing AI-generated code is devilishly hard"
    url: "https://www.spinellis.gr/blog/20260523/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/spinellis-gr--why-reviewing-ai-generated-code-is-devilishly-hard.md"
    kind: repo
---

The post argues that reviewing AI-generated code is harder than reviewing human-written code because the reviewer must not only understand the change but also judge how well they understand it. Without the usual control gate, people can accept code while believing they understand it when they do not.

It links that problem to metacognition, the Dunning-Kruger effect, the illusion of explanatory depth, and automation bias. LLM fluency makes faulty code look plausible, which can lead reviewers to trust incorrect suggestions and miss omitted fixes or tests.

## Reading notes

- Human-only development forces a reader to understand non-trivial code before contributing to it, so lack of understanding blocks progress.
- With AI-assisted changes that already passed continuous integration, that objective control gate is absent.
- Metacognition here means both understanding code and assessing that understanding.
- Metacognitive monitoring includes tracking what you know, how well you understand a change, confidence in comments, and confusion.
- Metacognitive judgment includes judgment of learning, feeling of knowing, confidence judgment, and ease-of-processing judgments.
- The Dunning-Kruger effect makes low-competence people overestimate their competence, which raises the risk for junior programmers accepting faulty AI-generated code.
- The illusion of explanatory depth suggests that people think they understand mechanisms more deeply than they do, and this can apply to code, algorithms, data structures, designs, interactions, and architecture.
- In programming, explanatory knowledge matters more than facts, procedures, or narratives because it supports reasoning across the software development lifecycle.
- LLM output can look trustworthy even when faulty because it is generated as the next most probable tokens.
- Automation bias makes people trust automated systems too much and reduce independent verification.
- Automation can increase acceptance of incorrect suggestions and reduce detection of omitted handlers or tests.
- The closing advice is to be more vigilant when reviewing AI-generated code.
