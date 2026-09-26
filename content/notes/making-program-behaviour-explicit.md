---
title: "Making program behaviour explicit | Pirrmann's train of thought"
date: '2026-09-27T00:43:56+01:00'
category: webclip
summary: 'The post uses F# computation expressions to show how quoted expressions can be mutated before evaluation, producing unpredictable runtime behavior and even supporting mutation-testing-style replacements.'
tags: ["fsharp", "computation-expressions", "mutation-testing"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Making program behaviour explicit | Pirrmann's train of thought"
    url: "http://www.pirrmann.net/making-program-behaviour-explicit/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/pirrmann-net--making-program-behaviour-explicit.md"
    kind: repo
---

The post shows F# computation expressions being used to capture an expression, mutate it, and then evaluate the altered result. The examples are built to produce unpredictable runtime behavior, with mutations that can cause subtle bugs and difficult debugging.

It also sketches a builder that quotes an expression in `Run`, passes it through a mutation step, and evaluates the result. The author notes that the same approach can be used for mutation testing, and closes by saying that computation expressions remain a powerful way to build DSLs.

## Reading notes

- Computation expressions are presented as a way to make runtime behavior unpredictable by mutating quoted expressions before evaluation.
- The examples use custom syntax such as `usually`, `mostProbably`, and `pray` to show how mutations can change results.
- The text describes different states for the mutation process, including a default chance of mutation, a safe state, and an angry state with more mutations.
- The implementation sketch centers on a `ChaosBuilder` with `Return`, `Quote`, and `Run`, where `Run` mutates the quoted expression and evaluates it.
- An `IMutationSitePicker` chooses where to mutate, and an `IExpressionReplacer` performs the replacement.
- A sample `MutateWithProbability` implementation uses `System.Random` and a mutable last-random value to decide whether to pick the next site.
- The author says the actual expression manipulation code is not included, but the current work is available as a Gist.
- The post connects the idea to mutation testing and mentions numeric constant mutation, operator replacement, reordering pattern matching, and type-aware function replacement.
- The conclusion says computation expressions are a powerful F# feature and can be used to write DSLs.
