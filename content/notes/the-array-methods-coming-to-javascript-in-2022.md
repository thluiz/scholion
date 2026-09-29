---
title: "The Array Methods Coming to JavaScript in 2022"
date: '2022-05-04T14:52:05-03:00'
category: webclip
summary: 'The article explains a Stage 3 proposal that adds non-destructive array methods to JavaScript so code can copy an array and then reverse, sort, splice, or replace one item without mutating the original.'
tags: ["javascript", "arrays", "proposal-change-array-by-copy"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "The Array Methods Coming to JavaScript in 2022 | HackerNoon"
    url: "https://hackernoon.com/the-array-methods-coming-to-javascript-in-2022?source=rss"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2022-05/hackernoon-com--the-array-methods-coming-to-javascript-in-2022.md"
    kind: repo
---

The page says JavaScript arrays are often copied before changes because updates affect the original array. It presents the “Change Array by Copy” proposal as a way to reduce that pattern with built-in methods that return modified copies instead of mutating the source.

## Reading notes

- JavaScript stores arrays in heap storage, so assigning one array to another keeps the same underlying array.
- Copying with the spread operator is a common workaround before changing an array.
- The “Change Array by Copy” proposal has reached Stage 3.
- The proposal adds four methods: `toReversed()`, `toSorted(compareFn)`, `toSpliced(start, deleteCount, ...items)`, and `with(index, value)`.
- `toReversed()` returns a reversed copy of the array.
- `toSorted()` returns a sorted copy and accepts a comparison function.
- `toSpliced()` returns a copied array with items removed or inserted.
- `with()` returns a copied array with one element replaced.
- The methods also work on `TypedArray` values such as `Int8Array`.
- The page says these methods are not yet supported in major browsers or Node.js, but a polyfill exists.
