---
title: "The Mythical Agent-Month — Wes McKinney"
date: '2026-09-25T21:43:28+01:00'
category: webclip
summary: 'Wes McKinney argues that coding agents reduce accidental complexity and speed up code generation, but they also amplify scope creep, coordination problems, and bloated codebases. Design, taste, and expert human judgment remain the bottlenecks.'
tags: ["software-engineering", "coding-agents", "brooks-law", "design-taste"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "The Mythical Agent-Month – Wes McKinney"
    url: "https://wesmckinney.com/blog/mythical-agent-month/?utm_source=tldrnewsletter"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/wesmckinney-com--the-mythical-agent-month-wes-mckinney.md"
    kind: repo
---

McKinney says AI has disrupted his sleep and changed his workflow, because he now gets up early to feed ideas to coding agents. He thinks the real question is how long human edge will last once agents can produce better software with less human input.

## Reading notes

- He compares agentic development with _The Mythical Man-Month_ and Brooks’s Law, asking whether teams of humans directing AI agents will avoid the old software bottlenecks.
- He argues that agents make it easier to produce a working program, but the move from prototype to production still requires testing, documentation, hardening, and maintainability.
- He links this to Conway’s Law and the coordination problem, since multiple agent sessions can generate conflicting plans that humans must reconcile.
- In the discussion of _No Silver Bullet_, he says agents are very good at reducing accidental complexity, but they cannot reliably distinguish it from essential complexity.
- He says agents often create new accidental complexity through defensive boilerplate, larger codebases, and systems that become harder to reason about as they grow.
- He describes a “brownfield barrier” where large agent-built codebases begin to collapse under their own size, with each new change hacking through earlier output.
- He says near-zero code generation cost encourages scope creep, because adding features feels cheap even though every feature adds future maintenance, debugging, and reasoning cost.
- He says open source projects can be hurt by large, “helpful” pull requests when contributors are more hands-off and less accountable for design decisions.
- He concludes that design, product scoping, and taste are now the main constraints, and that the people who thrive will be the ones who can judge what to build and what to leave out.
