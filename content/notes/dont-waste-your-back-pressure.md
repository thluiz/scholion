---
title: "Don't Waste Your Back Pressure"
date: "2026-09-23T18:16:43+01:00"
category: webclip
has_commentary: false
summary: "Argues that agent leverage scales with the automated feedback ('back pressure') around them, like build systems, type checkers, and browser tools, not with the model alone."
tags:
  - ai-agents
  - software-engineering
  - developer-tools
sources:
  - title: "Don't waste your back pressure ·"
    url: "https://banay.me/dont-waste-your-backpressure/?utm_source=tldrnewsletter"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/banay-me--dont-waste-your-back-pressure.md"
    kind: repo
---

Moss names a pattern behind the projects that get real mileage out of coding agents: they build structure around the agent that gives it automated feedback on its own work. He calls this feedback "back pressure," borrowing the term for a system throttling upstream flow based on what it can absorb. An agent that can run a build, read a type error, or compare a rendered page against an expectation corrects itself; an agent limited to editing files depends on a human to catch every missed import.

The argument is about where an engineer's attention goes. Without back pressure, the engineer spends their own time on trivial corrections instead of the larger problem. With it, they can hand off progressively harder tasks and trust the loop to catch mistakes before the result reaches them.

## Fichamento

- Agents given only file-editing tools rely on a human for every piece of feedback, which limits delegation to simple, closely supervised tasks.
- Giving an agent a bash tool to run a build lets it read the failure and correct itself, freeing the engineer from checking syntactic correctness line by line.
- Expressive type systems act as a form of back pressure: they can make invalid states unrepresentable and surface edge cases, and languages with clear error messages (the author names Rust, Elm, and Python) feed that signal straight back to the model.
- MCP servers for Playwright or Chrome DevTools give an agent a way to compare a rendered UI against an expectation, removing the need for a human to describe layout problems manually; for non-UI work, MCP bridges to LSPs serve the same function through lints.
- Outside conventional engineering, the author cites proof assistants like Lean paired with AI (referencing the Erdős Problems work by Kevin Barreto and Liam Price, using Aristotle to formalize a GPT-5.2 Pro proof into Lean) and randomized fuzzing for CUDA kernel correctness as other domains where an automated correctness loop lets an agent keep iterating until the result is trustworthy.
- For spec-driven development, the suggested technique is generating documentation from an OpenAPI schema automatically, so the agent can compare what it produced against what it intended to build.
