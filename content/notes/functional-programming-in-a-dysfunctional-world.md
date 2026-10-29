---
title: "Functional Programming in a Dysfunctional World"
date: '2015-07-24T08:45:59-03:00'
category: webclip
summary: 'The article argues that functional programming improves correctness and testability through immutability, pure functions, algebraic data types, and strong type systems, with property-based testing as a key complement.'
tags: ["functional-programming", "immutability", "type-systems", "property-based-testing"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Functional Programming in a Dysfunctional World"
    url: "https://underthehood.myob.com/functional-programming-in-a-dysfunctional-world/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-07/underthehood-myob-com--functional-programming-in-a-dysfunctional-world.md"
    kind: repo
---

The article argues that functional programming is valuable mainly because it improves correctness and testability. It links that claim to immutability, pure functions, algebraic data types, and stronger type systems, and it presents property-based testing as a natural fit for code written this way.

## Reading notes

- The article focuses on two benefits of functional programming: correctness and testability.
- Immutability makes code easier to reason about because values are not modified in place.
- The author contrasts mutable Ruby code with equivalent Haskell code that returns new lists instead of changing existing ones.
- The article says copying data can be acceptable in many systems, and that performance concerns should be measured rather than assumed.
- Immutable values are presented as thread-safe, which helps with parallel computation.
- The text claims that lazy evaluation in functional data structures can keep performance competitive with imperative approaches.
- Algebraic data types are described as a way to express disjunction more clearly than typical mainstream type systems.
- The Maybe type is used as an example of representing the possible absence of a value.
- The article says this helps avoid null pointer exceptions because the compiler forces explicit handling of both cases.
- It presents recursive data structures, such as trees, as a natural use for algebraic data types.
- Hindley–Milner type inference is described as a system that can infer types from usage and serve as documentation through type annotations.
- The article claims that stronger type systems can catch errors at compile time and reduce the need for tests aimed only at checking correctness.
- Pure functions are described as functions whose output depends only on their input.
- Pure functions are said to be easier to test because there is nothing to mock in their dependencies.
- Monads are mentioned as a way to separate I/O from pure code.
- Property-based testing is presented as a way to define properties of a function and generate many random test cases.
- The quicksort example is used to show how properties can describe ordering, idempotence, minimum, maximum, and permutation behavior.
- The closing advice is to start with immutable variables and a separation between pure and side-effecting code if adopting a full functional language feels too radical.
