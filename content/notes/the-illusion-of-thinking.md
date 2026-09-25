---
title: "The Illusion of Thinking"
date: '2025-06-06T13:28:16-03:00'
category: webclip
summary: 'Apple argues that frontier large reasoning models improve on some reasoning benchmarks, but their accuracy collapses past certain problem complexities, their reasoning effort can fall as complexity rises, and they show limits in exact computation.'
tags: ["large-reasoning-models", "problem-complexity", "reasoning-benchmarks", "llm-reasoning"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "The Illusion of Thinking: Understanding the Strengths and Limitations of Reasoning Models via the Lens of Problem Complexity - Apple Machine Learning Research"
    url: "https://machinelearning.apple.com/research/illusion-of-thinking?utm_source=tldrai"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2025-06/machinelearning-apple-com--the-illusion-of-thinking.md"
    kind: repo
---

Apple studies large reasoning models with controllable puzzle environments to examine final answers and internal reasoning traces under varying compositional complexity. The paper says this setup avoids some limits of standard benchmarks and helps reveal how these models behave across different levels of difficulty.

## Reading notes

- Frontier LRMs improve on reasoning benchmarks, but their core capabilities, scaling properties, and limits are still not well understood.
- Standard evaluations focus on final-answer accuracy in math and coding, and this can suffer from data contamination while revealing little about reasoning trace quality.
- The paper uses controllable puzzle environments with consistent logical structure and adjustable compositional complexity.
- Across many puzzles, frontier LRMs show a complete accuracy collapse beyond certain complexity levels.
- Their reasoning effort rises with complexity up to a point, then declines even when token budget remains available.
- Under equivalent inference compute, the paper separates three regimes: low-complexity tasks where standard models outperform LRMs, medium-complexity tasks where LRMs benefit from extra thinking, and high-complexity tasks where both collapse.
- The paper says LRMs have limits in exact computation, do not use explicit algorithms reliably, and reason inconsistently across puzzles.
- The analysis of reasoning traces examines explored solution patterns and computational behavior to better characterize their strengths and limits.
