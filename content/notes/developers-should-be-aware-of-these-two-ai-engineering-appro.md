---
title: "Developers should be aware of these two AI engineering approaches"
date: '2026-10-26T12:30:42+00:00'
category: webclip
summary: 'The page argues that reliable agentic systems depend on Graph Engineering and Harness Engineering: one structures work into explicit steps, and the other provides the environment, rules, and verification needed for agent reliability.'
tags: ["graph-engineering", "harness-engineering", "agentic-systems"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Developers should be aware of these two AI engineering approaches"
    url: "https://daily.dev/posts/LgFVrktej"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-10/daily-dev--developers-should-be-aware-of-these-two-ai-engineering-appro.md"
    kind: repo
---

The page says developers should know two practices for building reliable agentic systems: Graph Engineering and Harness Engineering. Graph Engineering breaks work into smaller explicit tasks with inputs, outputs, and routes to the next step, which helps structure AI work and makes decisions easier to inspect. Harness Engineering focuses on the broader environment around the coding agent, including the service, ownership, dependencies, rules, allowed changes, and verification.

## Reading notes

- Graph Engineering organizes work as connected smaller tasks instead of one large prompt.
- Each task has a purpose, a defined input, an output, and a route to the next step.
- This structure makes agent decisions easier to inspect and allows independent work in parallel.
- Harness Engineering matters because code generation is only one part of software engineering.
- A useful agent also needs to understand the service, its team, its dependencies, the rules it must follow, what it may change, and how to verify its work.
- The page presents Harness Engineering through two practical implementations: a controlled payment bug fix and a scorecard-based deployment gate.
