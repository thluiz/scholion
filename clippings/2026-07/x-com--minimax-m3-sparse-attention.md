---
url: "https://x.com/omarsar0/article/2074494774292148726"
captured_at: "2026-07-08T22:31:40+01:00"
title: "GLM 5.2 has taken over much of the AI timeline lately..."
domain: "x-com"
---

elvis@omarsar0 · Jul 7

GLM 5.2 has taken over much of the AI timeline lately, and most of the conversation has centered on how it stacks up against Opus. That is the headline. The workload tells a quieter story: the builders I work with have kept running MiniMax M3 at scale, because it delivers comparable long-horizon capability at a fraction of the cost. In fact, MiniMax M3 still leads GLM 5.2 in token usage on Open Router by more than 50%.

The main constraint on long-horizon agents has not been intelligence; it has been the cost of attention over a growing context.

M3 is built to remove that constraint. Its 500K-token context window is one of the longest available in an open-weight model, but the capability that matters is the ability to stay on a single task for hours while the context keeps growing. M3 is multimodal with native image and video understanding, so the same agent can work across text, code, and visual inputs in one run.

Fireworks makes the same point from the infrastructure side. It frames M3 as the first open-weight model on Fireworks to combine frontier coding, native image and video understanding, and a 500K-token context window in one system. The practical claims that matter for this piece are the ones Fireworks reports in that launch post. M3 reaches up to 15x faster long-context decoding than M2.7, per-token compute drops to 1/20th at long context, and Fireworks cites 12- to 24-hour autonomous runs on paper reproduction and CUDA kernel optimization tasks.

Long-horizon tasks are demanding because the context never stops growing. A multi-hour agent run accumulates code, logs, tool outputs, and intermediate reasoning, and with standard dense attention, every new token effectively re-reads all of it. Cost grows with the square of the length, so the longer an agent works, the more expensive each step becomes. That is the practical reason most long-running agents get cut short.

The mechanism that changes this is MiniMax Sparse Attention (MSA), documented in MiniMax's recent report. MSA changes what the model reads at each step. Before attending, it runs a lightweight pre-filtering pass: an Index Branch scores the context in blocks, selects the blocks most relevant to the current token, and the model attends only to those. It reads the index rather than the whole library, which keeps the cost of each step roughly flat even as the context grows into the hundreds of thousands of tokens.

MiniMax Sparse Attention: a lightweight Index Branch scores key-value blocks and selects the top-k per query group, and the main branch attends only to those blocks.

What this means if you are building with M3:

- Predictable cost at any length. The paper sets Bk = 128 and k = 16, so each query and GQA group selects 16 blocks, or 2,048 key-value tokens. An extended run still has indexing overhead, but the main attention budget stays fixed.
- Cheap long context. In the paper's model configuration, they report a 28.4x per-token attention FLOPs reduction at extreme sequence lengths versus dense GQA under the same head setup.
- Fast in production. On H800 at long sequence lengths, they report 14.2x prefill and 7.6x decoding wall-clock speedups. The separate top-k benchmark says MiniMax's specialized kernel is fastest against torch.topk and TileLang in all tested settings.
- Minimal quality cost. In the 109B MoE experiments, the paper reports 6B active parameters per token and says MSA-CPT remains close to the full-attention baseline after long-context extension. It evaluates MMLU, GSM8K, HumanEval, RULER, HELMET, and many other benchmarks while each query attends to 2,048 tokens.

Per-token attention FLOPs and latency stay nearly flat for MSA as sequence length grows, while dense GQA (grouped-query attention) climbs sharply: 28.4x less compute, 14.2x faster prefill, and 7.6x faster decoding at extreme sequence lengths.

## What This Unlocks

The interesting part is not just that M3 can hold more tokens. It is that long context becomes cheap enough and fast enough to sit inside iterative systems that need to keep state over time.

- Self-improving agents. This is the first application I would watch. A self-improving agent needs to keep the current code, prior failed edits, evaluation logs, benchmark results, and its own hypotheses in view while it proposes the next change. Sparse attention does not solve evaluation, but it makes the long-running propose, validate, and revise loop much less likely to collapse under context cost.
- Repository-scale engineering. Fireworks highlights full-repository code understanding and strong agentic coding. That matters because real engineering work rarely fits into a neat prompt. Debugging across a codebase, tracking regressions, and making multi-file changes all benefit from an agent that can keep the repository, test output, and edit history alive in one session.
- Scientific and systems research. Fireworks points to long autonomous runs on paper reproduction and CUDA kernel optimization. Those are useful examples because the work is not a single answer. It is a sequence of experiments, logs, failures, fixes, and measurements where continuity is the product feature.
- Multimodal long-context workflows. M3 is natively multimodal, not text-only with vision bolted on. It combines long context with native image and video understanding, so a single run can reason across text, code, screenshots, diagrams, and video frames together. That opens up visual-to-code from a mockup or screenshot, video analysis, multimodal document review, and agents that keep visual context alive alongside their code and tool traces across a long session.

This is why the model is interesting for builders. It moves long context from a document-reading feature toward an execution substrate for agents that need memory, iteration, and verification.

It is worth noting why this is arriving now. MiniMax introduced sparse attention during the M2 generation and set it aside because the infrastructure was not yet mature. For M3, the focus was on the kernels. MSA partitions the context into blocks, reads each block once with contiguous memory access, and attends only to the relevant blocks, which lets it run several times faster than other open sparse-attention methods while holding quality.

This connects directly to the context engineering work I have focused on. For years, I have encouraged developers to curate what goes into the context window. MSA is the model learning to curate what it attends to within the window; the same principle moves one layer down into the architecture.

For developers and researchers, this is the difference between a short demo and a tool you can depend on. It means an agent that reads an entire repository in one pass, debugs across a full codebase in a single sustained session, or carries a research task through hours of experiments, logs, and revisions without losing context. In MiniMax's own long-horizon runs, the strongest result often emerged deep into a multi-hour session, long after most models would plateau and stop. Affordable long context is what gives an agent that kind of persistence.

This is the part I find most compelling. The agents I build usually fail not because the model is weak but because they cannot sustain a long task, and a reliable long context is the foundational infrastructure that finally addresses it.

## Where To Get Started With MiniMax M3

For a technical team, the Fireworks point is operational. M3's sparse-attention design only becomes useful if the serving layer can keep latency, throughput, and cost stable at long context. Fireworks says it powers MiniMax's first-party API inference, offers the fastest endpoint in the MiniMax model series, and prices M3 from $0.60 per 1M input tokens with serverless and on-demand deployment options. At that rate, M3 lands at roughly 75% less than GLM 5.2 for comparable usage, which makes the story less about a larger context window and more about whether long-horizon agents can run economically in production.

The pricing is useful because it reframes M3 as an upgrade path from M2.7, not just a new frontier model. Fireworks says open-weight launch pricing has dropped to parity with M2.7 for standard serverless usage, so teams get M3's long context and native multimodal understanding without paying a premium over the previous generation.

To test M3, use the same Fireworks chat completions endpoint you would use for other Fireworks models. The model id is accounts/fireworks/models/minimax-m3, and because the model is multimodal, a single request can include text plus image URLs in the same message.

For harder agentic or reasoning tasks, add "thinking": {"type": "enabled"} to the payload. For production workloads, Fireworks positions serverless as the fastest path to evaluation and on-demand deployments as the option for predictable throughput.
