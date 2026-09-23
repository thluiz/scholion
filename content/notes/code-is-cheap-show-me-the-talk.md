---
title: "Code is cheap. Show me the talk."
date: 2026-09-23T13:52:07+01:00
category: webclip
summary: "Kailash Nadh argues LLMs made code abundant and cheap, so accountability, provenance, and the ability to think and articulate now matter more than the code itself."
tags: ["llms", "vibe-coding", "software-development", "foss"]
has_commentary: false
sources:
  - title: "Code is cheap. Show me the talk. - nadh.in"
    url: "https://nadh.in/blog/code-is-cheap/?utm_source=tldrnewsletter"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/nadh-in--code-is-cheap-show-me-the-talk.md"
    kind: repo
---

Kailash Nadh flips Linus Torvalds's famous line from 2000. Talk used to be cheap and code was the proof; twenty-five years later, watching Torvalds himself merge AI-generated code into his own project, Nadh argues the ratio has reversed. Code is now abundant and nearly free to produce.

The reversal changes what counts as evidence of a good developer, a good codebase, and even what FOSS collaboration is for. It also has a cost: juniors who lean on LLMs before building their own fundamentals risk becoming dependent on a tool they don't understand, with fewer seniors around who still have a reason to teach them.

## Fichamento

- The old rule-of-thumb signals for judging a codebase or a FOSS project (tidy documentation, a clear README, consistent style and comments) no longer say much about quality, since LLMs can produce all of that instantly regardless of who's behind the keyboard.
- Work that used to take weeks or months now takes hours; the physiological and cognitive cost of producing software has dropped by orders of magnitude, freeing time for architecture and thinking instead of typing.
- AI-written code reads as "slop" because provenance is lost: without a visible human cost behind it, there's no one to hold accountable, and code generated infinitely and without effort is hard to value.
- FOSS's social contract rested on software being scarce and hard to make. When anyone can vibe-code what they need for themselves, that incentive to share and collaborate weakens, and curation, governance, and trust become more valuable than the code itself.
- Nadh separates two failure modes: manic "vibe coding" advocates who mistake infinite output for value, and denouncers stuck on an argument from incredulity. Both miss that experienced developers who can articulate problems well get disproportionately better results from the same tools.
- The people most exposed are juniors without fundamentals yet. Depending on an LLM before developing an independent understanding of systems leaves them stuck maintaining code they don't grasp, and reduces the incentive for seniors to mentor them when output is already fast.
- Nadh argues that syntax and framework knowledge are no longer the bottleneck; what matters now is thinking clearly, articulating the problem, and steering the tools.
