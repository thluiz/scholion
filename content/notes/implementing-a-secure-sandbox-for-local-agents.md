---
title: "Implementing a secure sandbox for local agents"
date: '2026-09-24T23:26:51+01:00'
category: webclip
summary: 'Cursor describes a sandbox for coding agents that cuts approval interruptions, preserves security, and adapts to macOS, Linux, and Windows limits while teaching agents when escalation is needed.'
tags: ["agent-sandboxing","coding-agents","security"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Implementing a secure sandbox for local agents"
    url: "https://cursor.com/blog/agent-sandboxing?utm_source=tldrai"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/cursor-com--implementing-a-secure-sandbox-for-local-agents.md"
    kind: repo
---

Cursor says coding agents gain power when they can run terminal commands automatically, but that also raises the risk of deleted databases, broken code, and leaked secrets. Requiring approval for every command leads to approval fatigue, especially when several agents run at once. The team rolled out agent sandboxing on macOS, Linux, and Windows so agents can work inside a controlled environment and ask for approval mainly when they need to go outside it, often for internet access. They report 40% fewer stops than unsandboxed agents.

## Reading notes

- The text presents the sandbox as a way to reduce interruptions without giving up the security of local agents.
- It describes the problem of accumulated manual approvals, which make users stop reviewing each request carefully.
- The implementation uses a uniform API, but with different mechanisms on each operating system.
- On macOS, the team evaluated App Sandbox, containers, virtual machines, and Seatbelt, and settled on Seatbelt via sandbox-exec.
- On Linux, the solution combines Landlock and seccomp, with ignored files becoming inaccessible to the sandboxed process.
- On Windows, Cursor runs the Linux sandbox inside WSL2 while working with Microsoft on more suitable native primitives.
- The text also says the agent harness had to be adjusted to explain the sandbox's restrictions and indicate when permission escalation is necessary.
- After these changes, recovery behavior improved and the offline evaluation also improved.
- The gradual rollout in production confirmed use of the feature, and the company says it sees one third of requests on supported platforms running with the sandbox.
