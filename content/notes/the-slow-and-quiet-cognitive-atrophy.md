---
title: "The Slow and Quiet Cognitive Atrophy of a Modern Software Engineer"
date: "2026-09-23T13:51:08+01:00"
category: webclip
has_commentary: false
summary: "AI-generated code looks clean and its own tests pass, but skipping the review step quietly erodes an engineer's own skill. Elmar Chavez traces the decay and argues discipline is what keeps understanding intact."
tags:
  - ai
  - software-engineering
  - skill-decay
  - code-review
sources:
  - title: "The Slow and Quiet Cognitive Atrophy of a Modern Software Engineer - DEV Community"
    url: "https://dev.to/codingwithjiro/the-slow-and-quiet-cognitive-atrophy-of-a-modern-software-engineer-3lbh"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/dev-to--the-slow-and-quiet-cognitive-atrophy-of-a-modern-software-engineer.md"
    kind: repo
---

Elmar Chavez names the danger after Pieter Bruegel's The Blind Leading the Blind. He describes the prompt-accept-repeat workflow of AI-assisted coding as something that quietly removes the review step that used to catch mistakes and build understanding. The UI looks right and the AI-generated tests pass. In his account, that's enough for engineers to accept a change without reading it. The same habit moves through the code review chain. A junior's trust in AI output cascades into a senior's trust in the junior, all the way to production.

## Reading notes

- Skill decay from over-reliance on AI isn't unique to software, but the "prompt, accept, repeat" workflow removes the review step that used to catch small mistakes before they accumulate.
- Doing a task yourself, rather than just directing an AI to do it, is what forces attention to edge cases, UX decisions, and which tests actually matter.
- Human-written code carries an owner. Someone who built it can fix it, and solves the same problem faster the next time because of that ownership.
- Unreviewed AI code moving through a PR chain, junior trusting the AI and senior trusting the junior, creates a false sense of trust that reaches production.
- His daily practice against atrophy is solving one coding challenge a day, recording himself explaining the solution out loud, then reviewing the recording for where he struggles or pauses.
- He caught AI recommending a deprecated method once, something his own prior study of the subject let him notice. A fully AI-directed workflow would have missed it.
- A debugging attempt handled entirely through AI prompting produced repeated lists of three to five pre-check steps that didn't fix anything; doing the fix himself instead took 15-30 minutes and left him with an understanding that stuck.

Connects with [I don't like LLMs](/notes/i-dont-like-llms/), where Martin Fowler names a related but different discomfort: an aversion to the Silicon Valley culture that shaped these models, distinct from the skill-decay argument here.
