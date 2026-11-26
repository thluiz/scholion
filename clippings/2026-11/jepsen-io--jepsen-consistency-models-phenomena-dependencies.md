---
url: "https://jepsen.io/consistency"
captured_at: "2026-11-25T16:19:18+00:00"
title: "Consistency"
domain: "jepsen-io"
---

Jepsen analyzes the safety properties of distributed systems–most notably, identifying violations of consistency models. But what are consistency models? What phenomena do they allow? What kind of consistency does a given program really need?

In this reference guide, we provide basic definitions, intuitive explanations, and theoretical underpinnings of various consistency models, as well as links to the literature. We aim to make consistency properties accessible for industry practitioners, academics, and enthusiasts.

## [](#models)[Models](https://jepsen.io/consistency/models)

A [consistency model](https://jepsen.io/consistency/models) is a safety property which declares what a system can do. Formally, a consistency model defines a set of _histories_ that a system can legally execute. For instance, the model known as [Serializability](https://jepsen.io/consistency/models/serializable) guarantees that every legal history must be equivalent to a totally ordered execution.

## [](#phenomena)[Phenomena](https://jepsen.io/consistency/phenomena)

Consistency models are often defined in terms of proscribed [phenomena](https://jepsen.io/consistency/phenomena): specific patterns of operations. For example, [G1a (Aborted Read)](https://jepsen.io/consistency/phenomena/g1a) occurs when a transaction observes a write performed by a different, aborted transaction.

## [](#dependencies)[Dependencies](https://jepsen.io/consistency/dependencies)

Consistency models and phenomena are often defined in terms of [dependencies](https://jepsen.io/consistency/dependencies) between different operations. For example, we say that transaction T2 write-read depends on transaction T1 if T2 reads some value that T1 wrote. These dependencies form a graph. Preventing specific cycles in that graph gives rise to different consistency models.
