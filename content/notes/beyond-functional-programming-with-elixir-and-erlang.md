---
title: "Beyond Functional Programming with Elixir and Erlang"
date: "2026-09-23T16:42:36+01:00"
category: webclip
has_commentary: false
summary: "José Valim argues that functional programming was never the goal of the Erlang VM, only the means to fault-tolerant, concurrent, maintainable distributed systems."
tags:
  - elixir
  - erlang
  - functional-programming
  - concurrency
sources:
  - title: "Beyond Functional Programming with Elixir and Erlang « Plataformatec Blog"
    url: "http://blog.plataformatec.com.br/2016/05/beyond-functional-programming-with-elixir-and-erlang/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/blog-plataformatec-com-br--beyond-functional-programming-with-elixir-and-erlang.md"
    kind: repo
---

The Erlang VM was designed as a runtime for distributed, fault-tolerant systems; functional programming principles provided the foundation that got it there.

## Fichamento

- Fault-tolerance requires isolating entities that touch the same data into separate processes with no shared state, so one failing doesn't corrupt what another depends on.
- Concurrency bugs in object-oriented and imperative languages mostly come from shared mutable state; making immutability the default narrows down where race conditions can actually occur.
- Maintainability follows from the same root: data that can't change under you, pattern-matching for terseness, protocols for polymorphism backed by explicit contracts.
- Concurrency and fault-tolerance aren't just infrastructure concerns. Slow compilation, slow boot times, and slow test suites are daily productivity hurdles that a concurrent runtime can address directly, since almost everything now needs to use all available cores.
- A CPU-bound test suite parallelized at 80% doesn't get the naive 4x speedup on 4 cores. It gets roughly 2.5x, since the sequential 20% still has to run alone.
