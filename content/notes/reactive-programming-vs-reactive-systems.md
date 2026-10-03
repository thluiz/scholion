---
title: "Reactive programming vs. Reactive systems"
date: '2017-06-11T09:46:32-03:00'
category: webclip
summary: 'The article distinguishes reactive programming from reactive systems: the first improves local asynchronous dataflow, while the second is an architectural style for resilient, elastic, message-driven distributed systems.'
tags: ["reactive-programming", "reactive-systems", "distributed-systems", "architecture"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Reactive programming vs. Reactive systems"
    url: "https://www.oreilly.com/ideas/reactive-programming-vs-reactive-systems"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2017-06/oreilly-com--reactive-programming-vs-reactive-systems.md"
    kind: repo
---

The article separates reactive programming from reactive systems and treats reactive as a set of design principles. It says reactive programming helps with asynchronous, non-blocking dataflow inside components, while reactive systems address the architecture of distributed systems as a whole.

## Reading notes

- Reactive is presented as a set of design principles for systems architecture and design in a distributed environment.
- Reactive programming is described as a subset of asynchronous programming and is generally event-driven.
- Functional reactive programming is excluded from the rest of the discussion because the term is often used incorrectly.
- Reactive programming supports breaking work into discrete asynchronous, non-blocking steps and composing them into workflows.
- Its APIs are generally callback-based, declarative, or a mix of both, often with stream operators.
- The main benefits of reactive programming are better use of multicore and multi-CPU hardware, improved performance, and developer productivity.
- Back-pressure is presented as crucial to avoid unbounded resource consumption.
- Reactive systems are described as message-driven, unlike reactive programming, which is event-driven.
- Messages have a clear destination, while events are facts for others to observe.
- Reactive systems use message-passing to decouple components in time and space, enabling concurrency, distribution, and mobility.
- The foundation of a reactive system is said to be message-passing, which supports isolation, resilience, and elasticity.
- Resilience is defined as responsiveness under failure and includes self-healing through isolation and supervision.
- Elasticity is defined as responsiveness under load and includes scaling up or down automatically.
- Location transparency lets a system scale with the same abstractions across cores, machines, and data centers.
- Reactive systems are presented as productive because they reduce cascading failures, improve recovery, and lower operational cost.
- Reactive programming is framed as useful inside components, but not sufficient by itself for system-level resilience and elasticity.
- The article concludes that reactive programming should be used as one tool within the broader design of a reactive system.
