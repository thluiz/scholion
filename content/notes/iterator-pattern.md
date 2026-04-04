---
title: Iterator Pattern
date: '2026-04-04T08:26:50+01:00'
summary: '"Provide a way to access the elements of an aggregate object sequentially without exposing its underlying representation."'
tags:
- software-engineering
- design-patterns
- gang-of-four
has_commentary: false
sources:
- title: Iterator pattern — Wikipedia
  url: https://en.wikipedia.org/wiki/Iterator_pattern
  kind: wiki
---

"Provide a way to access the elements of an aggregate object sequentially without exposing its underlying representation."

The Iterator pattern (GoF, 1994) decouples traversal logic from the collection itself. The collection provides an iterator object; the client uses `next()` and `hasNext()` without knowing whether the underlying structure is an array, a tree, a hash map, or something else.

This pattern is so fundamental that most modern languages have built it into the language: `for...of` in JavaScript, `for...in` in Python, `foreach` in C#, `Iterator` trait in Rust. You use it every day, even if you don't call it by name.
