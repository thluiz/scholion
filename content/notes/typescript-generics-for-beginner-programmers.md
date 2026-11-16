---
title: "TypeScript Generics for People Who Gave Up on Understanding Generics"
date: '2020-02-22T12:11:59+00:00'
category: webclip
summary: 'The tutorial explains generics through `makeState()` and `makePair()`, showing type parameters, constraints, default types, reusable generic interfaces, type aliases, and generic classes.'
tags: ["typescript", "generics", "beginner-programming"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "TypeScript Generics for People Who Gave Up on Understanding Generics"
    url: "https://ts.chibicode.com/generics"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/ts-chibicode-com--typescript-generics-for-beginner-programmers.md"
    kind: repo
---

The tutorial is aimed at beginner programmers and uses small examples to make TypeScript generics easier to understand. It starts with a `makeState()` function, then shows how a generic type parameter lets the same function create number-only or string-only states, while `extends` can restrict allowed types and default type parameters can remove repetitive annotations.

## Reading notes

- The article is written for beginner programmers and is meant as a friendlier alternative to existing TypeScript tutorials.
- `makeState()` first stores a single `number`, then is changed to `string` to show the basic type-checking problem.
- Using `number | string` alone does not solve the need for separate number-only and string-only states.
- `makeState<S>()` introduces a type parameter so callers can choose the stored type.
- `S extends number | string` restricts the generic argument to allowed types.
- A default type parameter like `S = number` lets `makeState()` be called without spelling out `<number>` every time.
- The article compares generic parameters to regular function parameters, but with types instead of values.
- `makePair()` extends the same idea to two type parameters, `F` and `S`, for a pair with `first` and `second` fields.
- The same pair shape can be extracted into a generic interface or a generic type alias and reused.
- The last section turns `makeState()` into a generic class `State<S>` and notes that type parameters are passed when instantiating the class.
