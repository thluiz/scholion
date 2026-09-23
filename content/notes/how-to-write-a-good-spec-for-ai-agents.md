---
title: "How to Write a Good Spec for AI Agents"
date: "2026-09-23T17:30:51+01:00"
category: webclip
has_commentary: false
summary: "A framework for specs that keep AI coding agents focused: start high-level, structure like a PRD around six core areas, work in modular prompts, and iterate continuously."
tags:
  - ai-agents
  - spec-writing
  - claude-code
  - prompt-engineering
sources:
  - title: "How to write a good spec for AI agents - by Addy Osmani"
    url: "https://addyo.substack.com/p/how-to-write-a-good-spec-for-ai-agents"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/addyo-substack-com--how-to-write-a-good-spec-for-ai-agents.md"
    kind: repo
---

Addy Osmani lays out a framework for writing specs that keep AI coding agents like Claude Code and Gemini CLI focused, built from five principles. A spec should start as a short, high-level brief and let the agent expand it into a fuller document rather than trying to write an RFC from scratch. It should follow PRD/SRS structure covering commands, testing, project structure, code style, git workflow, and boundaries, the six areas GitHub found most common across an analysis of 2,500+ agent configuration files. Work gets broken into modular, sequential prompts instead of one large context dump, since piling on instructions makes models satisfy fewer of them. Guardrails come from a three-tier boundary system (always do / ask first / never do) plus self-verification steps built into the prompt. The spec itself stays a living document, updated and re-synced with the agent as the project evolves.

Osmani closes with failure modes drawn from the same GitHub study: vague prompts, context dumped without summarization, skipped human review, and treating exploratory "vibe coding" the same as production engineering. He also cites Simon Willison's "lethal trifecta" of speed, non-determinism, and cost as the combination that makes unreviewed agent output dangerous.

## Fichamento

- Throwing a massive, RFC-sized spec at an agent in one shot doesn't work: context window limits and the model's "attention budget" get in the way.
- Principle 1: start with a concise goal statement and let the agent draft the detailed spec.md from it. Claude Code's Plan Mode (Shift+Tab) keeps the agent read-only while it explores the codebase and drafts.
- Principle 2: structure the spec like a PRD/SRS. GitHub's analysis of 2,500+ agent config files found six recurring areas: commands, testing, project structure, code style, git workflow, and boundaries. "Never commit secrets" was the single most common constraint found.
- Principle 3: break large specs into modular prompts instead of one giant context dump. Research on the "curse of instructions" shows model adherence dropping as more requirements pile into a single prompt.
- Modularity techniques: hierarchical table-of-contents summaries of large specs, dedicated subagents scoped to one section of the spec, and refreshing context per task instead of keeping the whole spec loaded at once.
- Principle 4: use a three-tier boundary system (always do / ask first / never do) instead of a flat list of prohibitions, plus self-verification steps ("compare the result with the spec and confirm all requirements are met").
- Principle 5: treat the spec as a living, version-controlled document. Test continuously against it, update it when the agent misunderstands something, and explicitly re-sync the agent with the revised version.
- Common pitfalls: vague prompts ("build me something cool"), overlong context dumped without summarization, skipping human review of agent output, and conflating exploratory "vibe coding" with production engineering.
- Simon Willison's "lethal trifecta" for agent risk: speed (agents work faster than you can review), non-determinism (same input, different outputs), and cost (which encourages corner-cutting on verification).
