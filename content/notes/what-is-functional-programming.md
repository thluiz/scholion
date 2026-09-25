---
title: "What is Functional Programming?"
date: '2026-09-25T20:43:30+01:00'
category: webclip
summary: 'The article defines functional programming as building programs mainly by composing functions, supported by higher-order functions, first-class values, immutable data, ADTs, and limited effects. It also distinguishes casual from pure FP and argues most value comes from the casual form.'
tags: ["functional-programming", "higher-order-functions", "immutable-data", "algebraic-data-types"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "What is Functional Programming?"
    url: "https://softwaremill.com/what-is-functional-programming/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/softwaremill-com--what-is-functional-programming.md"
    kind: repo
---

Functional programming is presented as a style where program logic is expressed primarily through function application and composition. The article argues that this usually depends on higher-order functions, functions as first-class values, expressions instead of statements, immutable data, and a reduced use of effects.

## Reading notes

- A strict definition of FP as programming with pure, side-effect-free functions is described as too narrow for common usage.
- In collection processing, FP is shown through declarative operations such as map, filter, and reduce.
- Functions can be treated as values, which avoids duplication and makes composition easier.
- Immutable data structures support updating by creating new values instead of mutating existing ones.
- Effects can be represented as values, separating the description of a computation from its evaluation.
- Errors can also be modeled as values, such as Result or Either, instead of being handled through exceptions.
- FP often separates data from behavior, while OO tends to combine them through encapsulation.
- Algebraic data types and pattern matching are presented as core building blocks of functional programs.
- The article distinguishes casual FP, where functions may have effects, from pure FP, where all functions are effect-free.
- Purity is described as valuable but not something most mainstream languages can fully verify.
- The practical value of FP is said to come mostly from moving away from imperative style toward casual FP.
- Languages differ in how well they support FP ergonomically, with Java and C# on one end, Haskell on the other, and Kotlin or Rust in between.
- The article concludes that FP is useful as a set of techniques, not as an end in itself.
