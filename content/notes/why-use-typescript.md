---
title: "Why use TypeScript?"
date: '2026-11-16T19:25:24+00:00'
category: webclip
summary: 'The post argues that TypeScript helps build code that is easier to maintain and share over time by making data shapes, expected types, and connected changes visible to the compiler and linter.'
tags: ["typescript", "types", "interfaces", "generics"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Why use TypeScript?"
    url: "https://dev.to/peacefullatom/why-use-typescript-4nej"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/dev-to--why-use-typescript.md"
    kind: repo
---

The post presents TypeScript as a way to write code that is easier to maintain and share over time. It says TypeScript does not make code bug-free or remove runtime errors, but it helps reveal expected data, track changes across related code, and support collaboration.

## Reading notes

- TypeScript is presented as a way to develop code with fewer bugs that is easier to maintain and share over a long time.
- The article says TypeScript does not write bug-free code, avoid runtime errors, or guarantee returned data types at runtime.
- It says TypeScript can reduce the time needed to understand a new codebase and make expected input and output types clearer.
- It says real-time linting and compiler checks force updates across connected code when something changes.
- Built-in types listed in the article include boolean, number, string, array, tuple, enum, any, void, null, undefined, never, and object.
- A tuple is described as an array with a fixed length and known element types.
- The article uses React hooks as an example of tuple usage.
- An enum is described as a way to give friendlier names to numeric values.
- The any type is shown as useful when data types cannot be defined early or come from external sources, but the article warns against using it in production.
- The void type is described as the return type for functions that do not return a value.
- The never type is used for something that will never happen, such as a function that throws and stops execution.
- TypeScript defaults to let and const instead of var, and declarations without assignment must have a type definition.
- let is described as block-scoped, unlike var.
- const prevents reassignment, but arrays and objects can still be modified inside.
- Type inference means an explicit type is not needed when the value or function call already has a known type.
- Class fields and methods can be typed, and the article uses a User class to show typed properties and return values.
- Interfaces are described as a way to define object structure, including required, readonly, and optional fields.
- The article says interface names are often prefixed with I.
- Function signatures can define required and optional parameters and a return type.
- Generics are shown as a way to reuse the same function across different types without duplicating code.
- The article also shows type aliases, including union types, as a way to combine function types and primitive values.
