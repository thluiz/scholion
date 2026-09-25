---
title: "A high-velocity style of software development"
date: '2026-09-25T17:57:35+01:00'
category: webclip
summary: 'The article argues for coding as a fast, iterative experiment: write code early, keep mock data nearby, restart often, favor consistency, and use composable functions and clean workspaces to shorten feedback loops.'
tags: ["software-development", "iterative-workflow", "functional-programming", "coding-practice"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "A high-velocity style of software development"
    url: "https://mihaiolteanu.me/interactive-dev?ref=dailydev"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/mihaiolteanu-me--a-high-velocity-style-of-software-development.md"
    kind: repo
---

The article argues for a development style built around direct experimentation in code instead of heavy planning and documentation. It favors keeping mock data, temporary scaffolding, and executable code close together, restarting often, and using hot reloading or print-based inspection to shorten feedback loops.

## Reading notes

- Write code and experiment instead of talking and planning.
- Iterating in actual code exposes corner cases, rewrites requirements, and keeps the feedback loop tight.
- Keep experimental and mock data alongside production code, even if some of it stays commented out or uncommitted.
- Minimize restart times and restart the project often so code changes stay cheap.
- Keep the entry point and the most important code at the top of the file so the file reveals itself quickly.
- Use one coding style across the project, even if another style seems better in isolation.
- Prefer functions that are either pure or clearly side-effecting, so their behavior is easy to predict and test.
- Compose functions and flow data through pipes when the whole project supports that style.
- Treat small functions as general-purpose utilities, not just short wrappers around specific cases.
- Keep the work environment clean, with only the code and a few essential tools visible.
- Use consistent naming so reading code becomes easier and less surprising.
- Keep separate playground projects for highly experimental work before bringing ideas into the main project.
- The article presents this as a high-velocity, laboratory-like way of working with software.
