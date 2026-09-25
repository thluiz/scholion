---
title: "I Vibe-Coded a Triton Kernel"
date: '2025-08-18T15:24:53+01:00'
category: webclip
summary: 'The author describes trying to make GPT-OSS attention trainable by replacing a forward-only Triton kernel with a working backward pass, using Modal, ChatGPT, Claude Code, and Codex CLI to fix test failures until the harness passed.'
tags: ["triton", "kernel-writing", "ai-agents", "gpt-oss"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "I Vibe-Coded a Triton Kernel"
    url: "https://benanderson.work/blog/vibe-coded-kernel/?utm_source=tldrai"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2025-08/benanderson-work--i-vibe-coded-a-triton-kernel.md"
    kind: repo
---

The author says GPT-OSS is hard to fine-tune because the recommended setup de-quantizes MXFP4 weights to BF16 and the attention design rules out Flash Attention and PyTorch SDPA, leaving eager attention as the fallback. He then tries to turn the release’s forward-only Triton attention kernel into one that works for training.

## Reading notes

- He says his kernel experience is limited, but he still managed to produce a correct-looking Triton kernel for GPT-OSS attention.
- He treats correctness as the main goal and builds tests around the kernel and a PyTorch reference.
- Cursor CLI generated a backward kernel and some tests, which he then used as a starting point.
- A notebook-based test setup failed because running hundreds of tests produced too much console output.
- He switched to a Modal app that loads the kernel and tests, runs them on an H100, and saves results as JSON.
- The tests failed immediately, including some forward tests, and the first issue was invalid memory accesses.
- He used a loop of pasting failing tests into ChatGPT, pasting rewritten kernels back into the IDE, and rerunning tests.
- That approach fixed the simple memory-access problems, but the backward pass still disagreed with the PyTorch reference.
- He then let Claude Code work autonomously on the repo with a prompt that pointed it to the Modal test command and the failing test case.
- Claude improved the implementation but still failed on query-padding cases.
- He handed the same task to GPT-5 through Codex CLI after Claude summarized the remaining issues in BUG.md.
- GPT-5 eventually got the tests to pass after some back-and-forth about running Modal tests.
- He ends by suggesting the episode makes recursive self-improvement feel more plausible, while saying he has doubts about that broader narrative.
