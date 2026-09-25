---
title: "My Evolving Approach to Learning Programming Languages"
date: "2026-09-23T18:52:34+01:00"
category: webclip
has_commentary: false
summary: "Dan Lew returns to Python after 15 years and tracks how the questions he asks of a language changed: from 'does it run on my machine' to reproducibility, testing, typing, API privacy, and immutability."
tags:
  - python
  - programming-languages
  - software-craft
  - career-growth
sources:
  - title: "My Evolving Approach to Learning Programming Languages"
    url: "https://blog.danlew.net/2024/09/24/my-evolving-approach-to-learning-programming-languages/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/blog-danlew-net--my-evolving-approach-to-learning-programming-languages.md"
    kind: repo
---

Dan Lew picks Python back up for a new job after 15 years away from it and notices that the questions he now asks of the language have changed more than the language itself. He lists five, each contrasted against how he thought as a novice developer.

The five: how many steps does it take to run this code on another machine (a novice used whatever Python came preinstalled and never updated dependencies), how to run unit tests (a novice saw testing as a waste of time), how to get type checking (a novice knew a small codebase well enough not to need it), how to hide implementation details behind a public API, and how to make an immutable structured collection of data.

## Reading notes

- Reproducible environment: as a novice he relied on whatever Python version came preinstalled on his machine and the server, avoided libraries, and never updated the ones he used. Now he wants a small, deterministic number of steps to run checked-out code on another machine.
- Unit testing: he used to see automated tests as a waste of time. Test-driven development is now his default, both as a faster way to verify his own code and as protection when he refactors later.
- Typing: on small codebases he could hold in his head, he saw no need for types. Larger codebases push him to want a function's inputs and outputs visible without reading its implementation, and to catch mistakes at type-check time instead of in production.
- Privacy: he had no concept of an "implementation detail" as a novice. Tightly defined public APIs that hide internals are now how he keeps accidental complexity out of a codebase.
- Immutability: mutable dicts were his default. Leaning functional now, he values immutable data classes because they stop a subroutine from changing an input unexpectedly.
- The concerns aren't Python-specific. He'd ask the same five questions of any language today, and part of the shift is personal experience while part is the tooling: Python didn't have type hints or dataclasses 15 years ago.
