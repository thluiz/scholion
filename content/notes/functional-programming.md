---
title: Functional Programming
date: '2026-04-04T08:23:52+01:00'
summary: 'Functional programming is a paradigm where programs are constructed by applying and composing functions. It is declarative: function definitions are expressions that map values to other values,…'
tags: ["software-engineering", "programming-paradigms", "functional"]
has_commentary: true
sources:
- title: Functional programming — Wikipedia
  url: https://en.wikipedia.org/wiki/Functional_programming
  kind: wiki
---

Functional programming is a paradigm where programs are constructed by applying and composing functions. It is declarative: function definitions are expressions that map values to other values, rather than sequences of statements that mutate state.

Three core ideas:

- **Pure functions** — given the same inputs, always return the same output, with no side effects (no mutation, no I/O). This makes them predictable and easy to test.
- **Immutability** — data structures are not modified after creation. Instead of changing an object, you create a new one with the desired changes.
- **First-class functions** — functions can be assigned to variables, passed as arguments, and returned from other functions, just like any other value.

Languages like Haskell and Erlang are purely or primarily functional. Others like JavaScript, Python, Scala, and F# are multi-paradigm but support functional patterns. Even in object-oriented codebases, applying functional principles — pure functions, immutability, composition — tends to produce more predictable, testable code.
