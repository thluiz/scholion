---
title: "You don’t need long context"
date: '2026-11-11T20:11:20+00:00'
category: webclip
summary: 'The paper argues that frontier models can keep contexts short without losing much accuracy on long-horizon and long-input tasks, and that selective reading plus compaction can replace long contexts.'
tags: ["long-context", "llm-agents", "context-compaction"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "You don’t need long context"
    url: "https://arxiv.org/html/2611.05306v1"
    kind: paper
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
