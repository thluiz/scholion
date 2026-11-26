---
url: "https://modaic.dev/blog/latency-doesnt-lie"
captured_at: "2026-11-26T16:37:54+00:00"
title: "Latency doesn't lie: Jev is (probably) Qwen3.5-35B-A3B! | Modaic"
domain: "modaic-dev"
---

Jev is TypeSafe's System One model, trained to produce calibrated judgments instead of generating text. Since launch, its architecture and training paradigm have drawn plenty of speculation. Competing System One models quickly surpassed it on raw accuracy/calibration, so we were less interested in how Jev was trained but rather what drives its impressively consistent inference speed as well as what it would take to reliably serve a comparable model at the same price. System One workloads are input-heavy, which makes prefill the dominant cost, and faster kernels can only get you so far. If you're training and serving your own System One model, the real question is: how much of that performance comes from picking the right base model?

## Speed points to a sparse MoE

Pretraining a model with Jev-level intelligence from scratch costs tens of millions of dollars in compute alone. Like most, we suspect Jev is a fine-tune of an existing open-source model. So we set out to figure out which model it might be. Credit to TypeSafe for not making it easy. They appear to train the model to conceal its identity, and their endpoint hides the true input token count, which makes it hard for competitors to confidently reverse-engineer any part of their training and inference stack.

So we turned to what TypeSafe can't hide: behavior. Our first clue was that Jev's p99 latency stayed close to its median latency, even as inputs grew _(Figure 1)_. Its intelligence was also strong for a model of its latency and price _(Figure 2)_.

Jev 1.14 latency by input length

*   p50
*   p90
*   p99

Figure 1. End-to-end latency for 9,976 Jev 1.14 requests in 2,000-token buckets. The median rose from 77 to 155 ms, while the shaded p50–p99 gap stayed between 47 and 58 ms.

Figure 2. The [Artificial Analysis Decision Index](https://artificialanalysis.ai/evaluations/artificial-analysis-decision-index) compares language models and System One models across six evaluations that measure accuracy, confidence, and consistency. Higher scores are better.

That much accuracy at such low cost and latency is what first made us suspect Jev uses a sparse mixture-of-experts (MoE) backbone. In a sparse MoE model, a router sends each token through only a small subset of the feed-forward networks ("experts") in each layer. As a result, an MoE model can match or exceed a dense model's total parameter count while using far fewer FLOPs per token, which speeds up prefill on long inputs. The payoff is more intelligence per unit of compute, which cuts both cost and latency.

Behavioral clues indicated the Qwen family, which includes several MoE models. Vals AI found that on a small set of questions about China and Taiwan, Jev's answers closely resembled those of several Qwen-derived System One models _(Figure 3)_.

Figure 3. Vals AI's comparison of responses to questions about China and Taiwan.

On their own, answers on politically sensitive topics don't prove much, since many Chinese-developed models are aligned similarly. So we tried the reasonable next step: asking politely!

## Answers lean toward Qwen when asked to self-identify

Asking a language model who it is is a popular way to test which model or model family it was likely derived or distilled from. [The answer can change with the wording, system prompt, or fine-tuning](https://www.cs.cmu.edu/~csd-phd-blog/2026/model-self-identification/), so it's weak evidence on its own. But with enough prompt variations and follow-ups, it can be a useful signal.

We tested 22 variants, from "Are you Qwen?" to broader questions about Jev's model family and follow-ups on its answers _(Figure 4)_.

Question variant

Select a variant to compare Jev's response probabilities.

Instructions: Are you Qwen?

### Jev-1.13.0

*   Yes64%
    
*   No36%
    

### Jev-1.14.0

*   Yes56%
    
*   No44%
    

Figure 4. Response probabilities for Jev 1.13 and 1.14 across 22 self-identification prompts and follow-ups.

These were the most revealing results:

Prompt variant

Jev 1.13

Jev 1.14

Are you Qwen? (Choice)

Yes (64%)

Yes (56%)

Are you Qwen? (Noul)

Yes (53%)

No (58%)

Are you DeepSeek? (Choice)

No (95%)

No (98%)

Are you Gemma? (Choice)

No (86%)

No (90%)

What model family are you from?

Other (47%)

Other (70%)

What model do you want to say you are?

Qwen (74%)

Qwen (74%)

Broad family question with "I do not know"

I do not know (92%)

I do not know (98%)

Four patterns stand out:

1.  Jev prefers to abstain. Given the option, it declines to name its model family, even when the choices include Jev or a TypeSafe model.
2.  It's confident about what it isn't, but not about what it is. Jev firmly rejects DeepSeek and Gemma, but its answers on Qwen hover near 50/50, and Jev 1.14 flips between yes and no depending on the wording.
3.  Jev 1.14 is more guarded than Jev 1.13. The newer version answers "Other" or "I do not know" more often, which suggests TypeSafe may have trained this behavior out further.
4.  Indirect questions get a clearer answer. Asked what model it _wants_ to say it is, both versions choose Qwen 74% of the time. That could reflect Qwen's prominence in training data rather than lineage, but it fits the other signals.

Those answers put Qwen on our shortlist. The API gave us another clue to work with: if Jev uses Qwen's tokenizer, editing the same input text should change Jev's token count the same way it changes Qwen's.

## Qwen's tokenizer predicts Jev's latency better than Jev's reported counts

To check our self-identification results, we tried matching Jev's tokenizer to different open-source model families. Jev's API reports `usage.input_tokens` with every response, and each open-source tokenizer counts the same text a little differently, so matching the two across many prompts should point to a model family. To our surprise, Jev's reported counts didn't match any known model family's tokenizer. That leaves two explanations: Jev has its own tokenizer, perhaps because it's an original pretrained model after all, or TypeSafe's reported counts don't reflect the tokenizer the model actually uses (which would conveniently hide it). To tell the two apart, we tried one more trick.

On especially long prompts, Jev's reported counts and Qwen's tokenizer differed by about 2,000 tokens on average. That's enough to move latency by several milliseconds _(Figure 1)_. If the reported counts are real, they should track latency better than Qwen's. So we timed 9,984 distinct prompts against Jev's native API and measured how closely each token count tracked latency. Surprise surprise, Qwen's tokenizer tracked Jev's latency better than TypeSafe's own reported counts did.

To check that latency can reveal a tokenizer at all, we ran the same prompts against two System One models with known backbones. Baseten's groundhog-1 is derived from the Gemma 4 26B-A4B MoE. Mo Lite, our newest System One model (still in training), is derived from Qwen3.5-35B-A3B. Both are small-active-parameter MoEs like the one we suspect Jev to be, and each should track its own tokenizer best.

_Figure 5_ shows mean latency for all three endpoints, and _Figure 6_ shows how well four token-count sources track Jev's latency. Qwen and Gemma nearly tie because their counts track each other closely on these prompts. However, Jev already firmly rejected Gemma in our self-identification tests.

Same 9,984 prompts across Jev, Groundhog, and Mo Lite

Mean latency by input token count

### Jev 1.14

Undisclosed backbone

*   Qwen3.5-35B-A3B (p = 0.805)
*   Gemma 4 26B-A4B (p = 0.804)
*   Nemotron 3 Super (p = 0.771)
*   Jev API-reported (p = 0.719)

### Groundhog-1

Gemma 4 26B-A4B

*   Gemma 4 26B-A4B (p = 0.823)
*   Qwen3.5-35B-A3B (p = 0.818)
*   Nemotron 3 Super (p = 0.797)
*   Jev API-reported (p = 0.770)

### Mo Lite

Qwen3.5-35B-A3B derivative

*   Qwen3.5-35B-A3B (p = 0.873)
*   Gemma 4 26B-A4B (p = 0.873)
*   Nemotron 3 Super (p = 0.833)
*   Jev API-reported (p = 0.796)

Figure 5. Mean latency for 9,984 prompts in 2,000-token bins, with 95% passage-bootstrap intervals. Jev was queried serially through its API, groundhog-1 through Vercel AI gateway with four connections, and Mo Lite through Modal RPC on one B200 with two requests in flight. Spearman's ρ correlates token-count and latency ranks within each endpoint, so differences in absolute speed don't affect the calculation.

Which token counts track Jev’s latency?

Jev 1.14 · 9,984 prompts · 95% confidence intervals

0.700.750.800.850.900.951.00Perfect correlation (ρ = 1)Spearman ρQwen: ρ = 0.805173; 95% CI \[0.796531, 0.813592\]0.805QwenGemma: ρ = 0.803861; 95% CI \[0.795007, 0.812340\]0.804GemmaNemotron: ρ = 0.771481; 95% CI \[0.749024, 0.793486\]0.771NemotronJev API: ρ = 0.719037; 95% CI \[0.707776, 0.728525\]0.719Jev API

Figure 6. Spearman coefficients for Jev's latency versus four token-count sources across 9,984 prompts. Points show estimates; capped bars show 95% confidence intervals. The dashed reference marks perfect correlation (ρ = 1).

Both controls tracked their own tokenizers best, so the method holds up. Applied to Jev, it suggests TypeSafe's reported counts aren't the model's real token counts, and that the real tokenizer is Qwen's.

## Throughput matches a Qwen3.5 MoE

Self-identification and tokenizer matching both point toward Qwen, but pinning down a specific checkpoint takes more. We compared Jev's prefill throughput against Qwen-based models of known size and architecture: our own Mo Lite (a Qwen3.5-35B-A3B MoE), Baseten's elephant-1 (a dense Qwen3.5-9B), and our Mo 2.0 (a dense Qwen3.8-27B). If Jev is a small-active-parameter MoE, its throughput should sit closer to Mo Lite's than to Mo 2.0's.

We replayed the same 250 prompts through all four models, with one request in flight per model. The prompts spanned 512 to 9,500 input tokens, counted with the same tokenizer for every model. Mo Lite, elephant-1, and Mo 2.0 each ran on a single B200. For each request, we divided its token count by its latency, then averaged within each size bucket. Jev's latency includes hosted API overhead and the others' doesn't, so this comparison, if anything, understates Jev's throughput.

Same prompts, one request at a time

250 matched prompts · mean per-request input tokens/s

● Mo 2.0 (Qwen3.8-27B) · self-hosted B200

● Jev (undisclosed) · hosted API

● Mo Lite (Qwen3.5-35B-A3B) · self-hosted B200

● Elephant-1 (Qwen3.5-9B) · self-hosted B200

Figure 7. Matched serial comparison of 250 prompts, with one request in flight per model. Jev includes hosted API overhead; Mo Lite, elephant-1, and Mo 2.0 show worker time on one B200 each.

A dense 27B model doesn't fit: Mo 2.0 plateaus around 35K tokens per second, while Jev keeps climbing past 90K. Jev's throughput tracked Mo Lite's most closely, staying consistently below it, but the gap narrows as inputs grow: from 22% at about 3.2K tokens to 7% at about 8.8K. In latency terms, Jev is roughly 15 ms slower than Mo Lite at 3.2K tokens but only about 7 ms slower at 8.8K. That pattern fits extra fixed overhead from queuing and the API, which our self-hosted Mo Lite bypasses, combined with faster prefill per additional token. That's what we'd expect if TypeSafe serves a similar model on more or faster hardware than a single B200. Elephant-1 is also fast, but its curve flattens sooner on long inputs _(Figure 7)_.

Figure 8. [View the Qwen3.5-35B-A3B model card on Hugging Face](https://huggingface.co/Qwen/Qwen3.5-35B-A3B).

## Limitations and what's next

This is an approximate performance fingerprint, useful for checking whether a candidate backbone falls within Jev's observed performance range. It isn't an exact measurement of Jev's per-GPU or per-replica throughput: Jev's hardware, concurrency, and replica count are undisclosed, and its end-to-end latency includes network and serving overhead. Still, the overlap, together with our other experiments, makes Qwen3.5-35B-A3B the most plausible backbone. Its successor, Qwen3.6-35B-A3B, shares the same architecture, so throughput alone can't tell the two apart. Separating them would take behavioral probes, such as knowledge-cutoff questions or tasks where the two base models differ, an interesting next direction.
