---
title: "AI-assisted development needs automated tests"
date: "2026-09-23T16:27:50+01:00"
category: webclip
summary: "Simon Willison argues that comprehensive test coverage is what makes LLM-assisted coding trustworthy: tests let you prove convoluted AI-written code actually works."
tags:
  - ai-coding
  - testing
  - llm
has_commentary: false
sources:
  - title: "AI-assisted development needs automated tests"
    url: "https://simonwillison.net/2025/May/28/automated-tests/?utm_source=tldrnewsletter"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2025-05/simonwillison-net--ai-assisted-development-needs-automated-tests.md"
    kind: repo
---

Simon Willison suggests the gap between people who find LLMs genuinely useful for coding and people who find them a hindrance comes down to automated tests. He has followed the "Perfect Commit" discipline for over five years, bundling implementation, tests and documentation into a single unit. As a result, nearly everything he works on already has solid coverage before an LLM ever touches it.

## Fichamento

- Comprehensive tests derisk LLM-generated code. If a model produces something weird or convoluted that still solves the problem, tests prove it works, and the model can then refactor until the code looks right while staying green throughout.
- LLMs also help write the tests themselves. Willison calls this having a pair programmer who reliably remembers how to use `unittest.mock`.
- His closing challenge to anyone who says LLMs hurt more than they help is to ask about the health of their test suite first.
