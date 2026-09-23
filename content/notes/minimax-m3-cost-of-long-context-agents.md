---
title: "MiniMax M3 and the Cost of Long-Context Agents"
date: 2026-09-23T13:07:06+01:00
category: webclip
summary: "MiniMax M3's sparse attention keeps per-step cost flat as context grows, making multi-hour autonomous agents affordable in production."
tags: ["minimax-m3", "sparse-attention", "long-context", "ai-agents"]
has_commentary: false
sources:
  - title: "GLM 5.2 has taken over much of the AI timeline lately..."
    url: "https://x.com/omarsar0/article/2074494774292148726"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-07/x-com--minimax-m3-sparse-attention.md"
    kind: repo
---

Elvis (omarsar0) argues that MiniMax M3 is now the real destination for long-horizon agent workloads, holding capability comparable to GLM 5.2 at a much lower cost. The mechanism behind that gap is MiniMax Sparse Attention (MSA): instead of reading the whole context at every step, the model pre-filters it into blocks and attends only to the most relevant ones, which keeps cost roughly flat as the context window grows past 500K tokens.

With MSA holding the attention budget fixed at 16 blocks per query regardless of context length, an agent's per-step cost stops climbing as it accumulates hours of code, logs, and tool output on a single task.

## Fichamento

- Despite GLM 5.2 dominating the AI conversation, MiniMax M3 leads it in real Open Router token usage by more than 50%. It delivers comparable long-horizon capability at a fraction of the cost.
- The real bottleneck for long-horizon agents is the cost of attention over a growing context. Cost scales with the square of context length under standard dense attention, so every additional hour of agent work gets more expensive.
- MiniMax Sparse Attention pre-filters context before attending. An Index Branch scores key-value blocks, and each query selects only the top 16 blocks (2,048 tokens), which keeps the attention budget roughly flat regardless of context length.
- MiniMax's own benchmarks report a 28.4x reduction in per-token attention FLOPs, 14.2x faster prefill, and 7.6x faster decoding than dense attention at long sequence lengths, with quality staying close to the full-attention baseline.
- Fireworks prices M3 at $0.60 per 1M input tokens, about 75% cheaper than GLM 5.2 for comparable usage, at price parity with the earlier M2.7 generation despite the added context and multimodal capability.
- The source names four concrete cases this unlocks: a self-improving agent that keeps its current code, failed edits, evaluation logs, and hypotheses in view across a multi-hour loop; a coding agent that keeps a full repository, test output, and edit history alive in one session; autonomous runs of 12 to 24 hours on paper reproduction and CUDA kernel optimization; and multimodal runs that reason over text, code, screenshots, diagrams, and video frames together.
