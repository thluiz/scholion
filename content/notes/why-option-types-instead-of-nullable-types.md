---
title: "Why F#, Rust and others use Option type instead of nullable types like C# 8 or TypeScript?"
date: '2026-11-16T05:28:34+00:00'
category: webclip
summary: 'The answers explain that option types model absence as a value with strong composability, while nullable types depend on compiler tracking. They also note that performance differences are language-dependent.'
tags: ["option-types", "nullable-types", "language-design"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "language design - Why F#, Rust and others use Option type instead of nullable types like C# 8 or TypeScript? - Software Engineering Stack Exchange"
    url: "https://softwareengineering.stackexchange.com/questions/410724/why-f-rust-and-others-use-option-type-instead-of-nullable-types-like-c-8-or-t"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/softwareengineering-stackexchange-com--why-option-types-instead-of-nullable-types.md"
    kind: repo
---

The answers frame Option as a way to represent absence with a regular type that works well with collections, mapping, flattening, and defaulting. They also stress that null handling is often easier to keep safe when the type system and standard library are designed around option values from the start.

## Reading notes

- Option is treated as a zero-or-one-element collection, so it fits with common collection operations like foreach, map, flatten, and getOrElse.
- Several answers say null references are a language problem that option types avoid, especially in languages that can eliminate null altogether.
- Some answers argue that option types are more composable than nullable unions when values can nest or when a lookup may need to preserve more than one kind of absence.
- One answer says nullable types need compiler support to track three states safely, including when a value has been checked and is known non-null.
- Another answer says the choice is tied to language design and history, since C# and TypeScript keep null for compatibility, while Rust, Scala, F#, and Haskell lean toward option-style modeling.
- One answer states that runtime overhead is not inherently worse for Option, and that in some languages the compiler can optimize optional values down to a null pointer or a packed representation.
- One answer warns that Option can make later API changes harder when a function that used to accept a plain value is changed to accept an optional one.
