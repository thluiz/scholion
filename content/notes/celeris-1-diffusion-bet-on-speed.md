---
title: "Celeris-1's Diffusion Bet on Speed"
date: 2026-09-23T13:13:29+01:00
category: webclip
summary: "Celeris-1 swaps autoregressive generation for diffusion, claiming 15x faster responses than GPT-5-mini at a slightly lower MMLU-Pro score."
tags: ["celeris-1", "diffusion-models", "llm-inference", "benchmarks"]
has_commentary: false
sources:
  - title: "Celeris on X: Introducing celeris-1"
    url: "https://x.com/celeris_ai/status/2080442996403933630?s=12&utm_source=tldrai"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-07/x-com--celeris-1-diffusion-bet-on-speed.md"
    kind: repo
---

Celeris.ai's launch announcement for celeris-1: diffusion-based inference instead of autoregressive decoding, a 157ms p50 response latency (about 15x faster than GPT-5-mini, 17x faster than GPT-5), and a 76% score on MMLU-Pro against 78% for GPT-5-mini and 81% for GPT-5.

On raw throughput, celeris-1 reaches 1,280 tokens per second against 144 for Gemini 3.5 Flash-Light, measured on a reconstructed version of Artificial Analysis's benchmark dataset. Replies on X pushed back quickly on the "near-GPT-5" framing, given that gap on the same benchmark.

## Reading notes

- Celeris-1 replaces autoregressive generation with a diffusion-based inference architecture, which the company presents as the source of its speed gains without losing ground on the MMLU-Pro score cited alongside it.
- Its p50 response latency is 157ms, about 15x faster than GPT-5-mini and 17x faster than GPT-5.
- On MMLU-Pro it scores 76%, against 78% for GPT-5-mini and 81% for GPT-5.
- Throughput reaches 1,280 tokens per second, compared with 144 for Gemini 3.5 Flash-Light, on a reconstructed version of Artificial Analysis's benchmark dataset.
- The company frames its mission as maximizing useful intelligence delivered per unit of time, and points to celeris.ai/blog for build details and the full benchmark set.
- Replies on X questioned the "near-GPT-5" label given the actual MMLU-Pro gap, and several commenters asked whether the model would ship as open weights.
