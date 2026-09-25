---
title: "After two years of vibecoding, I'm back to writing by hand"
date: "2026-09-23T14:35:35+01:00"
category: webclip
summary: "Mo Bitar traces two years of AI coding through excitement, spec docs, and what he calls slop, and explains why he went back to writing most of his code by hand."
tags:
  - llms
  - vibe-coding
  - ai-agents
  - software-development
has_commentary: false
sources:
  - title: "After two years of vibecoding, I'm back to writing by hand"
    url: "https://atmoio.substack.com/p/after-two-years-of-vibecoding-im?utm_source=weeklyfoo&utm_medium=email&utm_campaign=weeklyfoo"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/atmoio-substack-com--after-two-years-of-vibecoding-im-back-to-writing-by-hand.md"
    kind: repo
---

Mo Bitar traces a common arc for engineers who take AI coding seriously: a small task impresses, a bigger one impresses more, and eventually someone hands the agent the refactor nobody wants to touch. When results disappoint, the instinct is to blame the prompt, so the next move is a beefy spec document meant to remove all ambiguity. That doesn't hold either. Reading his own codebase cover to cover after months of carefully specified agentic work, he found what he calls slop: changes that look plausible and pass review one at a time, but show no respect for the whole, for structural integrity, or for the patterns around them.

That's why he went back to writing most of his code by hand, and says he's faster, more accurate, and more creative once the full cost of the process is priced in, not just tokens per hour. [Code is cheap. Show me the talk.](/notes/code-is-cheap-show-me-the-talk/) makes a related argument: AI-written code reads as slop once there's no visible human cost, and no one to hold accountable for it.

## Reading notes

- Serious engineers using AI for real work follow a predictable arc: amazement at small tasks, then bigger ones, then an attempt at the one big refactor nobody wants to touch.
- When output disappoints, the instinct is to blame the prompt as under-specified, which pushes toward writing exhaustive spec documents before building anything.
- Spec-driven development fails too: real design docs evolve through discovery and implementation, but an agent commits to early decisions and doesn't revise them as understanding changes.
- Agent-written code looks convincing in isolation and even in pull request review, because both the engineer and the agent are trained to recognize what a "good" PR looks like.
- Reading his full codebase cover to cover, after months of carefully specified agentic work, he found slop: units of change that are internally consistent but disregard the whole, structural integrity, and neighboring patterns.
- He compares it to a novel where individual paragraphs read fine and stay consistent with the characters, yet the chapter as a whole doesn't cohere with what comes before or after.
- He decided not to ship, charge users for, or promise to protect user data with code he judged as slop.
- Writing by hand again, he reports being faster, more accurate, more creative, and more productive than with AI, once the full cost is priced in and not just code tokens per hour.
