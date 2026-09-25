---
title: "The efficient frontier of LLM inference"
date: '2026-09-25T21:48:18+01:00'
category: webclip
summary: 'The article distinguishes techniques that trade latency for throughput or quality for speed from those that expand the whole serving frontier, then situates quantization, parallelism, kernels, speculative decoding, and disaggregation on that map.'
tags: ["llm-inference", "latency-throughput", "quantization", "speculative-decoding"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "The efficient frontier of LLM inference"
    url: "https://www.baseten.co/blog/the-efficient-frontier-of-llm-inference/#quantization?utm_source=tldrai"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/baseten-co--the-efficient-frontier-of-llm-inference.md"
    kind: repo
---

The article uses the idea of an efficient frontier to describe LLM inference engineering as a set of tradeoffs between latency, throughput, cost, quality, and speed. It separates methods that move a deployment to a different point on the frontier from methods that expand the frontier itself.

## Reading notes

- Batch size changes the latency-throughput balance: smaller batches improve per-user latency but raise cost per token, while larger batches increase throughput and lower cost.
- Parallelism choices across multiple GPUs can favor either lower latency or higher throughput, depending on how Tensor Parallelism, Expert Parallelism, and Attention Data Parallelism are used.
- Quantization lowers precision in weights, activations, or KV cache values and improves both latency and throughput, while introducing a new quality-versus-efficiency tradeoff.
- Kernel optimization and runtime improvements reduce the resources needed per token and push the serving frontier outward.
- Speculative decoding guesses tokens and validates them, and current methods such as EAGLE-3, DSpark, and DFlash can improve tokens per second, especially for code generation.
- Disaggregation separates prefill and decode onto dedicated workers so each phase can be optimized separately and throughput can increase while latency stays the same or slightly better.
