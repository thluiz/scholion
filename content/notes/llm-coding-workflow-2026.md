---
title: "My LLM coding workflow going into 2026"
date: "2026-09-23T15:59:28+01:00"
category: webclip
summary: "Addy Osmani lays out the workflow he converged on after a year of AI-assisted coding: spec before code, small chunks, heavy context packing, and treating every AI commit as his own responsibility."
tags:
  - ai-coding
  - claude-code
  - software-engineering-workflow
  - llms
has_commentary: false
sources:
  - title: "AddyOsmani.com - My LLM coding workflow going into 2026"
    url: "https://addyosmani.com/blog/ai-coding-workflow/?utm_source=tldrnewsletter"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-01/addyosmani-com--my-llm-coding-workflow-going-into-2026.md"
    kind: repo
---

Addy Osmani calls his approach "AI-assisted engineering," a label chosen to separate it from letting an agent run unattended. The workflow starts before any code gets written: a spec.md built by having the LLM iteratively ask questions until requirements and edge cases are settled, then a plan.md that breaks the work into small tasks. He credits Les Orchard for the framing that stuck with him, a "waterfall in 15 minutes."

The throughline across every step is that Osmani treats AI output the way he'd treat a junior developer's pull request: useful, fast, and never trusted without review. [Code is cheap. Show me the talk.](/notes/code-is-cheap-show-me-the-talk/) argues a version of the same shift from a different angle, that LLMs made code abundant enough that accountability and articulation now carry the weight code used to carry.

## Fichamento

- He avoids monolithic prompts entirely, breaking projects into tickets tackled one at a time, since large asks tend to produce what one developer called "10 devs worked on it without talking to each other."
- Context packing means dumping goals, invariants, examples of good solutions, and explicit warnings about approaches to avoid into the prompt before coding starts, sometimes automated with tools like gitingest or repo2txt.
- He switches models mid-task when one stalls, calling it "model musical chairs," and defaults to Gemini for most coding work because it tends to understand his requests on the first try.
- Async agents like Google's Jules and GitHub's Copilot Agent clone the repo into a cloud VM, work in the background, and open a pull request, distinct from CLI tools like Claude Code that operate in real time inside the project directory.
- Version control becomes ultra-granular: commits after every small task, one practitioner's "save points in a game" framing, plus git worktrees to isolate parallel AI experiments without risking the main branch.
- A CLAUDE.md file (and GEMINI.md for Gemini CLI) carries persistent style rules, lint preferences, and an explicit instruction to ask for clarification rather than fabricate an answer when context is missing.
- His closing claim is that AI rewards existing engineering discipline rather than replacing it: spec-writing, testing, and version control matter more, not less, once an AI is writing half the code.
