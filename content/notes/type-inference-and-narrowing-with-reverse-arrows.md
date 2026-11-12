---
title: "Type inference and narrowing with reverse arrows"
date: '2026-11-12T12:03:46+00:00'
category: webclip
summary: 'Elixir infers and narrows types by refining dynamic values and propagating constraints through function arrows in reverse, which improves bug finding and will support more precise signatures in v1.21.'
tags: ["type-inference", "type-narrowing", "reverse-arrows", "elixir"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Type inference and narrowing with reverse arrows"
    url: "https://elixir-lang.org/blog/2026/11/10/inference-narrowing-reverse-arrows/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/elixir-lang-org--type-inference-and-narrowing-with-reverse-arrows.md"
    kind: repo
---

Elixir infers types by refining `dynamic()` as values are used. Instead of treating the dynamic type as a black box, it intersects it with the types expected by the functions a variable reaches, which can expose violations such as using the same value as both a number and a bitstring.

## Reading notes

- `dynamic()` in Elixir means `dynamic(term())`, and `term()` is the top type, so inference starts broad and becomes more specific as code uses the value.
- Multiple arrows make function types precise when a function has several clauses, as in `integer() -> integer()` and `float() -> float()` for `negate/1`.
- Elixir propagates arrows in reverse, starting from the expected result and walking back to the arguments, which can narrow `x` in `rem(negate(x), 2)` to `integer()`.
- Guards are inferred the same way: if a guard must succeed, Elixir reverses the arrows of `and`, `is_integer/1`, and `is_bitstring/1` to infer the variable types that make the guard true.
- Occurrence typing narrows variables differently in each branch of `if` and `case`, using the return value of the tested expression to recover the input types that could have produced it.
- In v1.20, narrowing could fail after assigning a guard expression to a variable, because the connection between the variable and the original expression was lost.
- Elixir v1.21 keeps track of the expression assigned to each variable, so narrowing can continue through assignments such as `y = is_integer(x)` and even across more than one assignment.
- The implementation is lazy: it only narrows when the variables involved are actually used in the branch.
- Reverse arrows also let Elixir refine expressions such as map values and other data constructors, so narrowing can flow back from `map.foo` to the original variable `foo`.
- The article links this approach to the If-T benchmark and says v1.21 passes all its tests, improving bug detection and reducing false positives once type signatures are added.

## Related notes

- [Data evolution with set-theoretic types](/notes/data-evolution-with-set-theoretic-types/)
- [In defense of TypeScript](/notes/in-defense-of-typescript/)
