---
title: "Latency doesn't lie: Jev is (probably) Qwen3.5-35B-A3B!"
date: '2026-11-26T16:37:54+00:00'
category: webclip
summary: 'Post argues Jev is a Qwen3.5-35B-A3B sparse MoE fine-tune, using latency behavior, self-identification prompts, tokenizer–latency correlation, and throughput vs. Qwen-based controls as evidence.'
tags: ["language-models", "moe", "latency", "qwen"]
has_commentary: false
generated_by: "openai/gpt-5.1"
sources:
  - title: "Latency doesn't lie: Jev is (probably) Qwen3.5-35B-A3B! | Modaic"
    url: "https://modaic.dev/blog/latency-doesnt-lie"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/modaic-dev--jev-qwen35-moe-latency-tokenizer-throughput.md"
    kind: repo
---

The post investigates the backbone of TypeSafe's Jev System One model, which produces calibrated judgments rather than free-form text. Direct architectural details and token counts are obscured by TypeSafe, so the authors rely on behavioral evidence: tight p50–p99 latency gaps on long, input-heavy workloads, strong intelligence for the cost, self-identification prompts, tokenizer–latency correlations, and throughput comparisons to known Qwen-based models. Together, these signals point to Jev being a sparse MoE fine-tune most plausibly derived from Qwen3.5-35B-A3B (or its close successor Qwen3.6-35B-A3B), rather than an original dense model or a non-Qwen backbone.

## Reading notes

- Jev is TypeSafe's System One model trained for calibrated judgments, not text generation, and its main appeal here is consistent, low-latency inference on input-heavy workloads where prefill dominates cost.
- Training a model with Jev-level capability from scratch would require tens of millions of dollars in compute, so the authors assume Jev is a fine-tune of an existing open-source model rather than an original pretrain.
- TypeSafe appears to deliberately obscure Jev's identity: the model is trained not to reveal its backbone, and the API hides the true input token count, making straightforward reverse-engineering harder.
- Latency measurements over 9,976 Jev 1.14 requests show median latency rising from 77 to 155 ms as input length grows, while the gap between p50 and p99 stays narrow (47–58 ms), indicating unusually consistent tail latency.
- On the Artificial Analysis Decision Index, Jev delivers high accuracy, confidence, and consistency relative to its latency and price, which leads the authors to suspect a sparse mixture-of-experts backbone.
- The post explains sparse MoE: a router sends each token through only a few feed-forward "experts" per layer, allowing more total parameters than a dense model yet fewer FLOPs per token, improving prefill speed and cost on long inputs.
- Behavioral comparisons suggest Jev resembles the Qwen family of models, which includes several MoEs; Vals AI found Jev's answers on China/Taiwan questions closely match Qwen-derived System One models.
- The authors note that alignment on politically sensitive topics alone is weak evidence because many Chinese-developed models share similar alignment, so they treat this as a preliminary hint.
- They then run 22 self-identification prompt variants, from direct yes/no questions like "Are you Qwen?" to broader family questions and indirect follow-ups, measuring Jev's probabilistic answers.
- For Jev 1.13 and 1.14, when asked "Are you Qwen?" with multiple choice, the model answers "Yes" 64% and 56% of the time respectively, but results vary with prompt style (e.g., Noul format).
- Jev strongly rejects other candidate families: it answers "No" to "Are you DeepSeek?" with 95% (1.13) and 98% (1.14), and to "Are you Gemma?" with 86% and 90%.
- When asked "What model family are you from?", Jev often chooses "Other" (47% for 1.13 and 70% for 1.14), and when given an "I do not know" option in broad questions, it selects that 92–98% of the time.
- Asked indirectly "What model do you want to say you are?", both Jev versions pick "Qwen" 74% of the time, which may reflect Qwen's salience in training data but still aligns with the other signals.
- From these prompts the authors highlight four patterns: Jev prefers to abstain, is more certain about what it is not than what it is, Jev 1.14 is more guarded than 1.13, and indirect questions elicit more Qwen-leaning answers.
- These self-identification patterns place Qwen on the shortlist, prompting the authors to investigate whether Jev uses a Qwen tokenizer by correlating token counts with latency.
- Jev's API returns `usage.input_tokens`, but these reported counts do not match any standard tokenizer across several open families, suggesting either a custom tokenizer or obfuscation in the reported numbers.
- On very long prompts, Jev's reported counts diverge from Qwen counts by about 2,000 tokens on average, a difference large enough to affect latency by several milliseconds.
- The authors time 9,984 prompts through Jev and compare how well different token-count sources (Qwen, Gemma, Nemotron, Jev-reported) track Jev's latency using Spearman rank correlation.
- Qwen's tokenizer correlates best with Jev's latency (ρ ≈ 0.805), slightly ahead of Gemma (≈ 0.804), then Nemotron (≈ 0.771), while Jev's own reported counts correlate worst (≈ 0.719), implying the reported counts likely do not reflect the actual tokenizer.
- To validate the method, they repeat the experiment on two System One models with known backbones: Baseten's groundhog-1 (Gemma 4 26B-A4B MoE) and Modaic's Mo Lite (Qwen3.5-35B-A3B derivative).
- For groundhog-1, Gemma token counts correlate best with latency (ρ ≈ 0.823), slightly above Qwen and Nemotron, with the Jev-style counts performing worst, matching the known Gemma backbone.
- For Mo Lite, Qwen token counts correlate best (ρ ≈ 0.873), tied with Gemma on this prompt set, again with Jev-style counts lagging, consistent with its Qwen-derived architecture.
- Because both control models track their own tokenizers most closely, the authors treat latency–token-count correlation as a valid way to infer the underlying tokenizer used in serving.
- Applying this to Jev, the stronger correlation with Qwen counts suggests Jev uses a Qwen tokenizer internally, while the API's reported counts are likely obfuscated.
- To narrow the specific Qwen checkpoint, the authors compare Jev's prefill throughput with three Qwen-based baselines: Mo Lite (Qwen3.5-35B-A3B MoE), elephant-1 (dense Qwen3.5-9B), and Mo 2.0 (dense Qwen3.8-27B).
- They replay 250 prompts (512–9,500 tokens) across all four models, with one request in flight per model, counting tokens consistently and computing mean input tokens per second per bucket.
- The baselines run on single B200 GPUs without network overhead, while Jev is accessed as a hosted API, so Jev's measured throughput includes extra overhead and is a lower bound on its underlying model performance.
- Mo 2.0, the dense 27B model, tops out around 35K tokens/s, while Jev surpasses 90K tokens/s and keeps rising, making a dense 27B backbone implausible for Jev.
- Jev's throughput curve closely tracks Mo Lite's (Qwen3.5-35B-A3B MoE), consistently below it but converging as input length grows, while elephant-1 (dense 9B) is fast but flattens earlier on long inputs.
- At around 3.2K tokens, Jev is about 22% slower than Mo Lite (≈ 15 ms extra latency), shrinking to a 7% gap (≈ 7 ms extra) at about 8.8K tokens, consistent with fixed API and queuing overhead plus similar per-token prefill speed.
- This throughput pattern matches expectations if TypeSafe serves a small-active-parameter MoE similar to Mo Lite, potentially on more or faster hardware than a single B200.
- The Qwen3.5-35B-A3B model card on Hugging Face is referenced as the canonical description of the suspected backbone architecture.
- The authors emphasize that their fingerprint is approximate: Jev's hardware configuration, concurrency level, and replica count are unknown, and end-to-end latency includes network and serving overhead.
- Despite these limitations, the convergence of evidence from latency distribution, self-identification behavior, tokenizer–latency correlation, and throughput alignment makes Qwen3.5-35B-A3B the most plausible backbone for Jev.
- They note that Qwen3.6-35B-A3B shares the same architecture as Qwen3.5-35B-A3B, so throughput alone cannot distinguish them, and that differentiating between the two would require behavioral tests targeting knowledge cutoff and other content-level differences.
