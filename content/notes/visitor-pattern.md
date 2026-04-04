---
title: Visitor Pattern
date: '2026-04-04T08:29:50+01:00'
summary: '"Represent an operation to be performed on the elements of an object structure."'
tags:
- software-engineering
- design-patterns
- gang-of-four
has_commentary: false
sources:
- title: Visitor pattern — Wikipedia
  url: https://en.wikipedia.org/wiki/Visitor_pattern
  kind: wiki
---

"Represent an operation to be performed on the elements of an object structure."

The Visitor pattern (GoF, 1994) separates algorithms from the objects on which they operate. It lets you add new operations to existing object structures without modifying the structures themselves — following the Open/Closed Principle.

The mechanism is double dispatch: each element in the structure accepts a visitor and calls the visitor's method corresponding to its own type. The visitor implements one method per element type, containing the operation logic.

The tradeoff: adding new element types is harder, because every visitor needs a new method. The pattern works best when the object structure is stable but operations on it change frequently.
