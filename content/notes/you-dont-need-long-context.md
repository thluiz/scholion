---
title: "You don’t need long context"
date: '2026-11-11T20:11:20+00:00'
category: webclip
summary: 'The paper argues that frontier models can keep contexts short without losing much accuracy on long-horizon and long-input tasks, and that selective reading plus compaction can replace long contexts.'
tags: ["long-context", "llm-agents", "context-compaction"]
has_commentary: true
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "You don’t need long context"
    url: "https://arxiv.org/html/2611.05306v1"
    kind: paper
  - title: "Full paper PDF (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/arxiv-org--you-dont-need-long-context.pdf"
    kind: repo
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/arxiv-org--you-dont-need-long-context.md"
    kind: repo
---

The paper claims that long contexts are often unnecessary for the tasks that seem to require them. Across long-horizon workflows and long-input benchmarks, the authors report that frequent compaction or selective reading usually preserves accuracy while reducing latency, memory use, and cost.

## Reading notes

- Later tokens cost more to generate than earlier ones, and the cost gap can be large on frontier models.
- Shorter contexts improve cloud cost, local latency, throughput, and memory use.
- The paper asks whether long contexts are necessary for long-horizon tasks, long-input tasks, and single-action operation.
- Long-horizon tasks are tested with end-of-conversation compaction.
- Long-input tasks are tested with selective input reading from files plus compaction as fallback.
- The benchmarks cover software engineering, terminal use, retrieval, multi-hop QA, and multi-document reasoning.
- On long-horizon tasks, frequent compaction usually keeps accuracy close to the full-history baseline.
- On long-input tasks, selective reading usually matches or improves baseline performance while keeping live context short.
- On some tasks, the model can work with no more than one action per context and still preserve most of the baseline accuracy.
- The paper proposes Semantic State Space Models as a post-training direction where a model keeps an explainable semantic state between turns.
- The conclusion is that the tested evidence does not justify keeping long contexts by default for the workloads studied.

## Commentary

The paper splits long context into two sources: history that grows with every agent action, and inputs too big for the prompt. The second becomes the first once the document sits in a file and the model reads it in slices with `sed` and `head`. From there everything is a long-horizon task, and compaction handles it.

The numbers support the thesis on the benchmarks chosen. On the six long-horizon ones (SWE-bench Verified, Terminal-Bench and four others), accuracy moves between −3.7 and +5.6 points for Opus 4.5 and between −3.3 and +4.4 for GPT 5.6 Sol. On the seven long-input ones the gain reaches 40 points, but the baseline dumps the whole document into the prompt, and four of the seven are needle-in-a-haystack tasks.

The savings are estimated, not measured. The cost factor comes from throughput on GLM 5.2, Kimi K2.6 and Qwen 3 Coder Next on H100s (3.6× to 7× between 256K and 16K windows), applied to closed-model prices. In the nominal cost tables, GPT 5.6 Sol gets more expensive with compaction on SWE-bench Verified: from $167.68 to between $184 and $203. New input tokens and output tokens both grow with every restart.

Per Appendix A, the briefing that preserves accuracy describes the work still to do: the task nearly verbatim, the plan, the completion criteria and pointers to artifacts. A narrative of what already happened doesn't help.

The conclusion about long-context models goes past the experiment. Getting from "it works on these benchmarks" to "training models that accumulate history makes no sense" takes more than the Turing analogy at the end. The authors themselves admit the evidence doesn't rule out tasks where long context helps.
