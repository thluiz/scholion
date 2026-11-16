---
title: "A Mental Model to think in TypeScript"
date: '2020-08-26T19:31:16+00:00'
category: webclip
summary: 'The post argues that developers already think in types, and TypeScript makes that mental model explicit with annotations, narrowing, structural typing, and tooling that catches errors before runtime.'
tags: ["typescript", "type-system", "compile-time", "tooling"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "A Mental Model to think in TypeScript"
    url: "https://web.archive.org/web/20200928174351id_/https://leandrotk.github.io/tk/2020/07/a-mental-model-to-think-in-typescript/index.html"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/web-archive-org--a-mental-model-to-think-in-typescript.md"
    kind: repo
---

The post argues that developers already reason in types when handling data, and TypeScript makes that reasoning explicit with annotations, compiler checks, and better editor support. It contrasts runtime behavior with compile-time checks, shows how the type system catches invalid inputs, and explains that types disappear after compilation.

## Reading notes

- JavaScript code is valid TypeScript syntax, so migration can be gradual by renaming files from `.js` to `.ts`.
- People already think in types when they decide how to handle arrays, objects, and function inputs.
- Type annotations make constraints explicit and let the compiler catch invalid values before runtime.
- Basic types such as `number`, `string`, and `boolean` can be added directly with `:` annotations.
- Object types can be written inline or extracted into type aliases like `Product` for reuse and clarity.
- TypeScript uses structural typing, so compatibility depends on shape and properties rather than type names.
- Compile time is when TypeScript checks types; runtime is when the program actually executes.
- Types live in type space, while variables, functions, and object values live in value space.
- Type-only names cannot be used as runtime values, so `instanceof` does not work with plain type aliases.
- Narrowing with `typeof`, `if`, `in`, `Array.isArray`, and `instanceof` helps the compiler understand specific cases.
- Optional properties need checks before using methods like `length` or `endsWith`.
- `Readonly` and `ReadonlyArray` help prevent mutation in compile time, including on nested arrays when applied explicitly.
- Type inference can remove redundant annotations while still preserving documentation through editor hover information.
- Enums can group related constant values, such as media types or UI state labels, into a named block.
- Union types combine alternatives, while intersection types combine required properties from multiple types.
- Utility types like `Pick`, `Readonly`, and `Required` help compose and reuse existing types.
- The TypeScript tooling provides autocomplete, hover types, and error messages that often point to the exact mistake.
- Strict compiler settings like `strictNullChecks` and `noImplicitAny` help surface bugs earlier.
- The article recommends reading type errors carefully and treating the compiler as a helper rather than an obstacle.
