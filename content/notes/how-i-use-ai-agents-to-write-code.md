---
title: "How I use AI agents to write code"
date: '2026-09-25T18:25:55+01:00'
category: webclip
summary: 'The author says AI agents are useful when paired with project guidance, tests, plan mode, and repeated review loops, even if they still make common mistakes and feel frustrating.'
tags: ["ai-agents", "coding", "software-development"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "How I use AI agents to write code"
    url: "https://nolanlawson.com/2025/12/22/how-i-use-ai-agents-to-write-code/?ref=dailydev"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/nolanlawson-com--how-i-use-ai-agents-to-write-code.md"
    kind: repo
---

The author says he no longer dismisses AI coding tools, because colleagues use them productively and the tools often write code better than he can. He argues that they only work well when given clear project context, a feedback loop, and repeated review, and he still finds them unreliable for subtle or novel work.

## Reading notes

- He uses Claude Code as his main tool, mainly because it is enough for his needs.
- He recommends a project `CLAUDE.md` or `AGENTS.md` plus a personal one for local habits and quirks.
- He says the project file should explain architecture, stable parts, work in progress, and risky areas.
- He says automated tests help agents check their work and converge on a solution.
- He says plan mode is useful for more complicated tasks.
- He gives a SQL performance example where a benchmark and `EXPLAIN` showed the first solution was slower.
- He says coding agents are not very good at UI work because inspection and screenshots cost time and tokens.
- He says AI mistakes often include deleting useful comments, duplicating code, and making subtle refactor changes that break intent.
- He suggests restarting with a fresh session and asking the agent to diff against `origin/main` and check for functional bugs.
- He says repeating the same review prompt can shake out more errors.
- He likes that Claude Code can keep working while he is away, but sometimes the work goes off track and he resets it.
- He says the biggest practical problem is that the tool asks permission for every little thing, which makes him skim and say yes too quickly.
- He experiments with running it in a Podman container in yolo mode, but only for side projects.
- He says he still feels ambivalent toward AI agents, but they let him write far more code in far less time.
- He says he does not use LLMs for everything and still writes code himself for subtle, novel, or sprawling tasks.
- He compares his current role more to a software architect who writes specs, reviews code, and sometimes still writes code.
- He does not use AI for his open-source work because it feels strange to publish code he did not truly write.
- He says he liked writing all the code himself more, but he also sees AI use as a kind of optimal strategy he keeps choosing.
