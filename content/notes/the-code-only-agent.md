---
title: "The Code-Only Agent"
date: '2026-09-25T20:34:03+01:00'
category: webclip
summary: 'The article argues that an agent should have only one tool, code execution. By forcing every task into executable code, it produces repeatable witnesses, clearer semantics, and more trustworthy computation.'
tags: ["code-execution", "agent-design", "formal-verification", "claude-code"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "The Code-Only Agent"
    url: "https://rijnard.com/blog/the-code-only-agent?utm_source=tldrai"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/rijnard-com--the-code-only-agent.md"
    kind: repo
---

The article argues for a Code-Only agent that can do nothing productive without writing and running code. Instead of tool calls like `ls` or `grep`, the agent must generate executable code, so the work becomes a code witness whose output can be rerun and reasoned about.

## Reading notes

- The post starts from frustration with agent ecosystems full of tools, MCP, subagents, and skills, and proposes simplifying the assumptions to a single tool: `execute_code`.
- In this setup, the agent cannot use `bash`, `ls`, or `grep`; it must write code in a chosen runtime such as Python and execute it.
- The point is to shift attention from what tools the agent will use to what code it will produce.
- The agent does not answer with a result directly; it produces a code witness, and the answer comes from running that code.
- This makes the work repeatable and more explicit, because the code is governed by the semantics of the runtime language.
- The author treats this as useful for computable tasks where guarantees matter, and connects it to formal verification and the idea that programs are proofs.
- The article describes practical design choices for a Code-Only harness, including how to return outputs, handle large results, and manage `stdout` and `stderr`.
- It also discusses enforcement, saying that a plugin hook can block banned tool uses and push the agent back toward code generation.
- The runtime choice matters, with Python, TypeScript, Rust, and Bash all presented as possible options depending on the domain.
- The post suggests that reusable building blocks for Code-Only agents may emerge as executable patterns, with functions, loops, and APIs composed programmatically.
- The closing outlook combines Code-Only execution with broader agent orchestration and hybrid tooling, where natural language handles coordination and code handles computation.
