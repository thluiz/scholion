---
title: "Death By a Thousand Microservices"
date: '2026-09-25T20:33:02+01:00'
category: webclip
summary: 'The article argues that microservices often add complexity, tooling, coordination, and testing costs without matching scale needs, while monoliths and simpler service boundaries often work better.'
tags: ["microservices", "monolith", "distributed-systems", "software-architecture"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Death By a Thousand Microservices"
    url: "https://renegadeotter.com/2023/09/10/death-by-a-thousand-microservices.html"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/renegadeotter-com--death-by-a-thousand-microservices.md"
    kind: repo
---

The article argues that microservices became a default choice in tech culture even when the problem does not justify distributed complexity. It connects that trend to JavaScript server-side enthusiasm, FAANG influence, venture capital pressure, and the prestige attached to building for “web scale.”

It says that most companies do not need a true distributed system, and that the costs show up in development, debugging, deployment, testing, resilience, tooling, observability, and team coordination. It also points to examples of companies that started or still run on monoliths, and suggests simpler alternatives such as a modular monolith or a few clearly justified services.

## Reading notes

- Microservices are presented as a cultural habit that often replaces the real question of what problem is being solved.
- Early JavaScript server-side development and the rise of “full-stack” identities helped normalize dogmatic thinking about backend architecture.
- Venture funding encouraged hiring and visible complexity instead of profitability or simpler systems.
- Distributed systems are described as inherently harder to build, test, deploy, debug, and keep resilient.
- The article cites startup audits that favored simple engineering and warned against premature microservices and messaging-heavy designs.
- Many successful companies began with monoliths, and several still rely on them at the core.
- Microservices often create heavy coordination costs, repeated boilerplate, and poor developer ergonomics.
- Tooling, observability, and integration testing become separate burdens that consume time and money.
- The article argues that a monolith is not the same as good code, but distributed systems are less forgiving of mistakes.
- It recommends starting with a monolith or using a small number of services only when a separate load is clearly justified.
