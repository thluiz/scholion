---
title: "TypeScript: Type vs Interface"
date: 2026-09-23T13:10:55+01:00
category: webclip
summary: "Interfaces merge and extend; types cover unions and tuples but can't be redeclared. Nevzorov's rule: interface for growth, type for flexibility."
tags: ["typescript", "interface", "type-alias", "type-system"]
has_commentary: false
sources:
  - title: "What's the difference between Type and Interface in TypeScript?"
    url: "https://app.daily.dev/posts/k7yR5YBI5?utm_source=notification&utm_medium=email&utm_campaign=digest"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2025-08/app-daily-dev--typescript-type-vs-interface.md"
    kind: repo
---

Anatoly Nevzorov's distinction: `interface` can be reopened and merged across declarations, which suits public APIs and object shapes that might grow. `type` is declared once, cannot be redeclared, and only combines through intersections (`&`). In exchange, `type` handles unions, tuples, and conditional types, forms `interface` can't represent at all.

In his own account, on large codebases interfaces compile faster and give smoother autocomplete, while complex union types can slow the TypeScript server down.

## Reading notes

- Declaring the same `interface` twice merges the members into one type (`interface Cat { meow }` plus a later `interface Cat { purr }` gives a `Cat` with both). Declaring the same `type` twice throws a compiler error instead.
- Type aliases cover unions (`'loading' | 'success' | 'error'`), tuples (`[number, number]`), and conditional types (`T | null | undefined`), none of which an interface can express.
- Interface merging is automatic; getting the same combined shape from types takes a manual intersection, as in `type User = Id & Name`.
- On large codebases, interfaces compile faster and give smoother autocomplete and refactoring; heavy union types can slow the TypeScript server down.
- His rule of thumb: interface for public APIs, object shapes, and anything expected to grow; type for unions, tuples, function overloads, and anything that needs `&` or `|`.
- An interface can extend an object-like type (`interface Dog extends Animal`), but not one built from unions or primitives. A type can mimic an interface through `&`, though the result is more manual to maintain.
