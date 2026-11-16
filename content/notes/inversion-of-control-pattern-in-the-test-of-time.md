---
title: "The Inversion of Control pattern in the test of time"
date: '2026-11-16T02:29:09+00:00'
category: webclip
summary: 'The post argues that IoC and containers help with composition, testing, and lifetime management, but also add complexity, scattered changes, and hidden dependencies. RavenDB uses IoC selectively, not everywhere.'
tags: ["inversion-of-control", "dependency-injection", "software-architecture", "testing"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "The Inversion of Control pattern in the test of time"
    url: "https://ayende.com/blog/189697-C/the-inversion-of-control-pattern-in-the-test-of-time?Key=7e553416-64f4-433d-998e-deb0008c0b3c"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/ayende-com--inversion-of-control-pattern-in-the-test-of-time.md"
    kind: repo
---

The post argues that IoC and containers can make business software easier to compose, test in isolation, and manage by lifetime, but they also create interface sprawl, harder-to-follow control flow, and change costs when the system needs to evolve. For RavenDB, the author prefers to keep some core parts explicit and only use container-like automation where the code changes often.

## Reading notes

- The author describes years of working with DI and IoC, and says the topic is too broad for a Twitter-length discussion.
- A composable system adds functionality by adding code rather than modifying existing code.
- RavenDB does not use a container for its main database structure.
- Container-driven systems can become convention-heavy, so working within the convention feels automatic while breaking it requires debugging.
- The RavenDB Cloud backend uses a container, IoC, interfaces, and multiple dispatch to handle storage, machine allocation, failure recovery, billing, and monitoring.
- That backend can adapt quickly across multiple cloud providers, but the approach also adds complexity.
- IoC can let developers postpone understanding wiring details until later, while still getting work done.
- Containers are useful not only for auto-wiring, but also for decomposition and lifetime management.
- The author is wary of decomposed systems because they tend to produce many single-implementation interfaces and make code flow harder to understand.
- A system split into many independent pieces may be easier to unit test, but harder to change globally because changes must be applied across many interfaces.
- A cross-cutting change, such as passing a correlation token for distributed tracing, can require touching most of the system.
- Independent components are easy to test in isolation, but the important behavior often lives in the assembled bundle and its container configuration.
- System tests should therefore be easy, fast, and obvious.
- The container’s lifetime management matters because applications typically use singleton, transient, and scoped lifetimes.
- Matching lifetimes helps avoid wiring mistakes, but injected dependencies can still hide where state is actually being carried.
- The author says non-trivial software is inherently complex, so the choice is to rearrange complexity or hide it, not eliminate it.
- RavenDB still uses constructor injection in core classes such as DocumentDatabase.
- DocumentDatabase has complex async initialization, recovery work, disk loading, and an idle-based lifetime that does not fit a standard container well.
- For that kind of core structure, manual control keeps dependencies, lifetime, and behavior explicit.
- RavenDB has many endpoints, and for that frequently repeated structure the author built a small internal container-like mechanism.
- Adding an endpoint means creating a class based on a known base class, and the routing infrastructure handles discovery, wiring, request context injection, and execution.
- This reduces the amount of magic in the parts that rarely change while automating the parts that change often.
- The author says RavenDB can measure performance costs of abstraction, and in some places interface method calls are forbidden because they are too expensive.
- Making new endpoints the easiest thing in the codebase encourages open/closed design and makes maintenance, code review, and new code simpler.
