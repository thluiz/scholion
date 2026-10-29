---
title: "Domain-Driven Design (DDD) With F# and EventStore"
date: '2016-04-11T09:12:42-03:00'
category: webclip
summary: 'The post presents a DDD implementation in F# with EventStore, using functional constructs, discriminated unions, and fold-based event application to keep domain logic explicit and isolated from infrastructure.'
tags: ["domain-driven-design", "fsharp", "eventstore", "event-sourcing"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Domain-Driven Design (DDD) with F# and EventStore - Lev Gorodinski"
    url: "http://gorodinski.com/blog/2013/02/17/domain-driven-design-with-fsharp-and-eventstore/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2016-04/gorodinski-com--domain-driven-design-ddd-with-f-sharp-and-eventstore.md"
    kind: repo
---

The post describes a methodology for implementing Domain-Driven Design with F# and EventStore. It argues that functional programming and DDD share the same aim of making domain knowledge explicit, and it uses event sourcing to show that alignment.

## Reading notes

- The example is a spike in early progress and uses F# and EventStore to explore a more idiomatic functional approach.
- The author contrasts functional and object-oriented paradigms and says F# changed his view of language value.
- DDD and functional programming are presented as sharing the goal of formalizing domain knowledge for automation and integration.
- The sample is based on SimpleCQRS and related F# implementations, but tries to move further away from object-oriented habits.
- The use of classes is limited to serialization and EventStore integration, and the choice is justified as a way to avoid technology for its own sake.
- The InventoryItem module contains state, commands, events, assertions, and command execution in a single F# source file.
- Discriminated unions are used so that all commands and events are explicitly handled with static verification.
- The identity value is kept outside the domain module because the domain logic does not need it.
- The Aggregate module defines an abstraction for aggregates and a persistent command handler.
- Persisted events are applied with fold.
- The IntegrationTests module wires the aggregate module to EventStore and serialization.
- The EventStore module is specific to InventoryItem in this version, but the author says it could be generalized by generalizing the serializer.
- The summary claims the F# version is more concise, more encapsulated, more declarative, more statically verified, and more readable.
- The author says explicit factoring by functions replaces class hierarchies and keeps the informational core at the center with infrastructure around it.
- Future work mentioned includes projections, read models, a service layer, more complex domains, domain services, complex invariants, and types for domain state.
- The author also wants to test the approach outside event sourcing and explore computation expressions for persistent workflows.
