---
title: "Every Layer of Review Makes You 10x Slower"
date: "2026-09-23T17:55:07+01:00"
category: webclip
has_commentary: false
summary: "Avery Pennarun argues AI coding speed doesn't fix engineering velocity because review layers, not typing speed, are the bottleneck, and draws on Deming's quality theory to argue for eliminating review stages, not stacking more of them."
tags:
  - engineering-management
  - code-review
  - ai-coding
  - deming
sources:
  - title: "Every layer of review makes you 10x slower"
    url: "https://apenwarr.ca/log/20260316-every-layer-of-review-makes-you-10x-slower?utm_source=weeklyfoo&utm_medium=email&utm_campaign=weeklyfoo"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/apenwarr-ca--every-layer-of-review-makes-you-10x-slower.md"
    kind: repo
---

Avery Pennarun (CEO of Tailscale) opens with a rule of thumb he can't find a theoretical basis for but keeps observing empirically: every layer of approval in a process multiplies its wall-clock time by roughly 10x. A 30-minute bug fix becomes a half-day once a peer reviews it, a week once an architecture team approves the design, a fiscal quarter once another team has to schedule the work, and multiple years once it needs executive sign-off. His point about AI coding follows directly from that: making the first step (writing the code) faster doesn't touch the actual bottleneck, which is time spent waiting in review queues, not time spent typing.

He works through why simply skipping review isn't the answer either, using W. E. Deming's critique of stacked QA passes in manufacturing. Adding more inspection stages looks like it should multiply quality (two 90%-effective QA passes should catch 99% of defects), but in practice each team downstream relies on the one before it to catch mistakes, so nobody upstream works as carefully as they would without a safety net. His prescription borrows Deming's actual fix, the one that worked at Toyota and didn't transfer cleanly to the US auto industry: trust. Build small teams that own quality end-to-end, replace review layers with an actual culture where anyone can "stop the line," and only then remove the review stages, because removing reviews without replacing the trust structure just produces slop faster.

## Fichamento

- Central claim, stated as a rule of thumb with no theory behind it but consistent empirical support: each layer of approval in a process multiplies its wall-clock duration roughly 10x (30 min → half a day with peer review → a week with architecture approval → a quarter with cross-team scheduling → years at the executive level).
- His argument for why AI coding speed doesn't solve this: making code generation faster (Claude writes in 3 minutes what took 30) doesn't remove the review bottleneck, it just produces more code for the same slow review pipeline to choke on, whether that means a human re-reviewing unverified AI output or a "monstrosity" project needing to be sliced into review-sized chunks anyway.
- He names a failure spiral he calls the "AI Developer's Descent Into Madness": fast prototype, mounting bugs from AI-driven fixes, delegating review to another AI agent, then building an agent framework to manage the agents, then starting over. He says he's watched several peers get stuck in it.
- Applying Deming's manufacturing critique: stacking QA passes doesn't compound quality the way a simple percentage model suggests, because each downstream team's incentive is to catch what the upstream team missed rather than work carefully themselves, since "that's what the next step is for."
- The Toyota Production System eliminated the QA phase and replaced it with an "stop the line" button anyone could press; the same button, installed at US manufacturers without the accompanying trust culture, went unused because workers feared being fired for pressing it.
- His diagnostic reframe of code review's actual job: a reviewer catching a mistake means the root cause already happened and it's too late to prevent it; the reviewer's real job is to obsolete their own class of review comment permanently (his example: gofmt eliminating whitespace review comments for good), not to keep catching the same category of error indefinitely.
- His proposed path forward is bottom-up, not a single policy change: build small teams that can be trusted to own quality without external review, let bigger systems compose from those trusted small components (drawing an analogy to a manufacturer sourcing reliable parts and removing its own QA steps as a result), and expect small startups, with naturally fewer review layers already, to have an advantage in this shift over larger companies whose slow review systems are structurally embedded.
