---
title: "How I use Claude Code"
date: '2026-09-25T21:35:42+01:00'
category: webclip
summary: 'Boris Cherny describes a largely vanilla Claude Code setup built around parallel sessions, shared instructions, slash commands, subagents, hooks, and strong verification loops.'
tags: ["claude-code", "ai-coding", "developer-workflows"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Thread by @bcherny on Thread Reader App"
    url: "https://threadreaderapp.com/thread/2007179832300581177.html?utm_source=tldrnewsletter"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/threadreaderapp-com--how-i-use-claude-code.md"
    kind: repo
---

Boris Cherny says he keeps his Claude Code setup mostly vanilla because the tool works well out of the box and is meant to be customized in different ways by different people. He describes a workflow built around many parallel sessions, shared repo instructions, automation for repetitive tasks, and verification before landing changes.

## Reading notes

- Runs five Claudes in parallel in the terminal, with tab numbering and system notifications to track when input is needed.
- Also runs five to ten Claudes on claude.ai/code alongside local sessions, and sometimes starts sessions from the phone app.
- Uses Opus 4.5 with thinking for everything, saying it is the best coding model he has used.
- Shares one CLAUDE.md across the team, checks it into git, and updates it whenever Claude does something wrong.
- Tags @.claude on coworkers’ PRs during code review and uses the Claude Code GitHub action to add work to the PR.
- Starts most sessions in Plan mode, then switches to auto-accept edits mode after agreeing on a plan.
- Uses slash commands for inner-loop workflows, especially /commit-push-pr, with inline bash to precompute information and reduce back-and-forth.
- Uses subagents such as code-simplifier and verify-app to automate common PR workflows.
- Uses a PostToolUse hook to format code and avoid later CI formatting errors.
- Avoids --dangerously-skip-permissions and instead pre-allows safe bash commands with /permissions and shared settings.
- Uses Claude Code with tools like Slack through MCP, BigQuery, and Sentry.
- For long-running tasks, uses background verification, Stop hooks, or the ralph-wiggum plugin, often with permission modes that avoid interruption.
- Says the most important tip is to give Claude a way to verify its work, because that feedback loop improves the final result by two to three times.
