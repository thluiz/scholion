---
title: "Continuous AI in software engineering"
date: "2026-09-23T18:11:00+01:00"
category: webclip
has_commentary: false
summary: "Sean Goedecke argues AI should be used like tests and types, continuously and automatically, not as an on-demand oracle a developer has to remember to consult."
tags:
  - continuous-ai
  - github-actions
  - code-review
sources:
  - title: "Continuous AI in software engineering"
    url: "https://www.seangoedecke.com/continuous-ai/?utm_source=tldrnewsletter"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2025-07/seangoedecke-com--continuous-ai-in-software-engineering.md"
    kind: repo
---

Goedecke compares AI to tests and type checks. Nobody decides to run those manually each time; they run continuously through CI, pre-push hooks and IDE highlighting, and a developer benefits from them even without consciously triggering them. He argues AI in the software development lifecycle should work the same way, a pattern he calls "continuous AI," a term he attributes to GitHub. Having Copilot PR reviews turned on by default changed his mind. One in five or ten catches something he missed; skimming past the rest costs him almost nothing.

## Fichamento

- Draws the core analogy explicitly: using AI "on tap" (going to get it when there's a problem) is like manually running unit tests or a type checker instead of having CI and IDE highlighting do it continuously.
- Defines continuous AI as any way AI tooling gets automatically integrated into existing development flows, running via CI, hooks or a schedule on its own. Tools like Claude Code or Devin still need a developer to actively invoke them each time.
- Examples given: automated AI-driven PR reviews, AI-driven issue/PR labeling, automated daily or weekly summary rollups, and Copilot/Cursor-style autocomplete.
- Copilot PR reviews turned on by default is what converted him: most individual reviews don't add value, but one in five or ten catches something real, and skimming four low-value reviews to reach the useful one is a cheap trade.
- He extends the same logic to internal reporting: weekly rollups that summarize project status for the management chain are, in his view, safe to delegate to AI most of the time, reserving human attention for when a project is actually going badly.
- Describes adding the GitHub Models permission to the native GitHub Actions access token as one of his most satisfying small wins: free inference plus Actions' triggers (PR/issue events, pushes, cron) makes continuous AI cheap to experiment with, without anyone needing to approve a subscription first.
- His closing position: even in a future where agentic models handle most or all coding, he expects layers of automated checks and organizational AI tasks to persist as ambient infrastructure regardless.
