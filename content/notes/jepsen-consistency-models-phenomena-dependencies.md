---
title: "Consistency"
date: '2026-11-25T16:19:18+00:00'
category: webclip
summary: 'Reference guide outlining what consistency models are, how they relate to phenomena and dependencies, and how these structures define legal histories in distributed systems.'
tags: ["distributed-systems", "consistency-models", "concurrency"]
has_commentary: false
generated_by: "openai/gpt-5.1"
sources:
  - title: "Consistency"
    url: "https://jepsen.io/consistency"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/jepsen-io--jepsen-consistency-models-phenomena-dependencies.md"
    kind: repo
---

Jepsen focuses on analyzing safety properties in distributed systems, especially by detecting violations of consistency models. This reference guide explains what consistency models are, which kinds of behaviors they allow or forbid, and how to reason about what consistency guarantees a particular program requires. It introduces basic definitions, gives intuitive explanations and theoretical background, and points to relevant literature for practitioners, academics, and enthusiasts.

## Reading notes

- A consistency model is presented as a safety property that constrains what a system is allowed to do.
- Formally, a consistency model specifies a set of histories that the system may execute legally.
- Serializability is given as an example model where every permitted history must correspond to some totally ordered execution.
- Consistency models can also be characterized by which specific phenomena (patterns of operations) they forbid.
- Phenomena such as G1a (Aborted Read) involve situations like a transaction reading data written by another transaction that later aborts.
- Both models and phenomena can be described via dependencies between operations, such as one transaction reading a value previously written by another.
- These dependencies form a graph whose structure reflects how transactions influence one another.
- Different consistency guarantees arise from preventing certain types of cycles in the dependency graph.
