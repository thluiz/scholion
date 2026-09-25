---
title: "The Illusion of the Illusion of Thinking"
date: "2026-09-23T18:12:05+01:00"
category: webclip
has_commentary: false
summary: "Anthropic and Open Philanthropy researchers argue that a widely cited 'reasoning collapse' study measured token limits and broken benchmarks, not a failure of model reasoning."
tags:
  - llm-reasoning
  - benchmarks
  - ai-evaluation
sources:
  - title: "The Illusion of the Illusion of Thinking — A Comment on Shojaee et al. (2025)"
    url: "https://arxiv.org/html/2506.09250v1"
    kind: paper
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/arxiv-org--the-illusion-of-the-illusion-of-thinking.md"
    kind: repo
---

C. Opus and A. Lawsen respond to Shojaee et al.'s "The Illusion of Thinking," a paper that reported large reasoning models collapsing to zero accuracy on planning puzzles past a certain complexity. Their reply argues the collapse is an artifact of the experiment, not of the models: Tower of Hanoi tests ran past the models' output token budget, and models were penalized for truncating an answer they clearly understood how to continue.

The sharper problem sits in the River Crossing benchmark. Shojaee et al. tested configurations with six or more agents and boat capacity three, a combination with no valid solution at all. Models that correctly recognized the puzzle as unsolvable were scored as failures anyway.

## Reading notes

- Models solving Tower of Hanoi explicitly stated they were stopping early to avoid excessive output length, which the original study's automated grading counted as a reasoning failure rather than a practical constraint.
- Given the token budgets used (64,000 for Claude 3.7 Sonnet and DeepSeek-R1, 100,000 for o3-mini) and roughly 5 tokens per move, the math predicts collapse right around N=7–8, matching the reported failure points.
- River Crossing instances with N≥6 actors and boat capacity 3 are mathematically unsolvable; models were still scored as wrong for not producing an answer.
- When models were asked to output a generating function (for example, a Lua function producing the solution) instead of an exhaustive move list, they solved Tower of Hanoi with N=15 accurately in under 5,000 tokens.
- The authors argue solution length is a poor proxy for problem difficulty: Tower of Hanoi needs exponentially many moves but each move is a trivial decision, while River Crossing needs far fewer moves but real constraint search, which explains why models can execute 100+ Hanoi moves and still fail a 5-move River Crossing case.
- Their conclusion: the original study shows models can't exceed their context limits and that automated grading can miscount both practical constraints and impossible puzzles as reasoning failures, not that reasoning itself collapses.
