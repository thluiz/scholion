---
title: "The Complete Guide to Building Agents with the Claude Agent SDK"
date: '2026-09-25T18:01:12+01:00'
category: webclip
summary: 'The guide shows how the Claude Agent SDK wraps the agent loop, built-in tools, permissions, subagents, hooks, structured output, and MCP so you can build a code review agent and other agents with less manual orchestration.'
tags: ["claude-agent-sdk", "ai-agents", "typescript", "mcp"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "The Complete Guide to Building Agents with the Claude Agent SDK"
    url: "https://nader.substack.com/p/the-complete-guide-to-building-agents?utm_source=tldrai"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/nader-substack-com--the-complete-guide-to-building-agents-with-the-claude-agent-.md"
    kind: repo
---

The post explains that the Claude Agent SDK is the engine behind Claude Code, exposed as a library for building agents that can read files, run commands, edit code, manage context, and keep working through tasks. It walks through a code review agent that analyzes a codebase for bugs, security issues, performance problems, and code quality, then returns structured feedback.

## Reading notes

- The SDK replaces the manual tool loop you would otherwise manage with the raw API.
- Built-in tools include Read, Write, Edit, Bash, Glob, Grep, WebSearch, and WebFetch.
- The guide uses Claude Code CLI as the runtime, TypeScript as the language, and Claude Opus 4.5 as the model.
- Query returns an async generator that streams system, assistant, and result messages.
- The review agent can inspect files, search code, and report issues with file names and line numbers.
- The SDK supports JSON Schema output for structured review results.
- Permission modes include default, acceptEdits, and bypassPermissions.
- canUseTool lets you approve or deny tools with custom logic.
- Subagents can be registered with Task for specialized analysis.
- Sessions can be resumed using a session ID.
- Hooks such as PreToolUse can audit tool calls or block dangerous commands.
- Custom tools can be exposed through MCP servers.
- The guide also covers cost tracking, file checkpointing, skills, hosting, secure deployment, and TypeScript and Python references.
