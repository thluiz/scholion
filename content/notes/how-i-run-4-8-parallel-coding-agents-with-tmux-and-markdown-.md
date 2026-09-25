---
title: "How I run 4–8 parallel coding agents with tmux and Markdown specs"
date: '2026-09-25T20:36:27+01:00'
category: webclip
summary: 'The author describes a manual system for coordinating 4–8 coding agents with tmux, Markdown feature designs, and slash commands that track planning, implementation, verification, and archive stages.'
tags: ["tmux", "coding-agents", "markdown-specs", "workflow"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "How I run 4–8 parallel coding agents with tmux and Markdown specs"
    url: "https://schipper.ai/posts/parallel-coding-agents/?utm_source=weeklyfoo&utm_medium=email&utm_campaign=weeklyfoo"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/schipper-ai--how-i-run-4-8-parallel-coding-agents-with-tmux-and-markdown-.md"
    kind: repo
---

The author describes a lightweight workflow for running parallel coding agents with tmux, Markdown files, bash aliases, and slash commands. The core unit is the Feature Design, a spec that captures the problem, considered solutions, the chosen implementation plan, file changes, and verification steps. He says this setup lets him work with 4 to 8 agents, while more than that becomes hard to manage and hurts decision quality.

## Reading notes

- Uses role-based tmux windows for Planner, Worker, and PM work.
- Stores each Feature Design as a numbered file in docs/features/ and tracks it through eight stages.
- Uses slash commands for creating, exploring, deep-diving, verifying, and closing feature designs.
- Ties every commit back to a specific Feature Design and updates the changelog when work is closed.
- Keeps a feature index that shows active, pending verification, and completed items.
- Bootstraps new repositories with /fd-init, which creates directories, templates, commands, and project conventions.
- Planning starts with /fd-explore so agents load codebase context before designing.
- Complex design work can use inline notes in the FD file and a /fd-deep command that launches four parallel agents.
- Worker agents start fresh from a ready FD, then implement, verify, and close the work in sequence.
- The author treats FD files as decision traces that help agents rediscover prior work and help him remember past choices.
- A separate dev guide keeps long-form guidance out of CLAUDE.md and lets agents open only the entries they need.
- The setup relies on multiple terminals, tmux window management, path aliases, and idle notifications to handle context switching.
- The main limits are cognitive load, sequential dependencies, context window pressure, permission-system friction, and the manual effort of translating business context into FDs.
