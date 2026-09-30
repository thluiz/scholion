---
title: "Refactoring: My 6 favorite patterns"
date: '2020-03-10T09:17:08-03:00'
category: webclip
summary: 'The post outlines six refactoring patterns that improve readability, maintainability, and parameter handling, and shows how extracting logic into objects or methods makes code easier to change.'
tags: ["refactoring", "javascript", "object-oriented-programming"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Refactoring: My 6 favorite patterns"
    url: "https://dev.to/brycedooley/refactoring-my-6-favorite-patterns-p13"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2020-03/dev-to--refactoring-my-6-favorite-patterns.md"
    kind: repo
---

The post presents six refactoring patterns the author finds useful in JavaScript, with the claim that they improve code cleanliness, readability, and maintainability. It also notes that good test coverage is crucial for refactoring, and that the patterns should apply to any programming language.

## Reading notes

- Introduce Object Parameter turns several function arguments into one object so parameter order matters less and naming stays consistent.
- Replace Anonymous Function with Expression extracts complex anonymous callbacks into named function expressions, which makes intent easier to read.
- Replace Primitive with Object wraps values like status, phone, or price in classes so validation and access rules are easier to control.
- Decompose Conditional moves conditional logic into descriptive expressions before the `if` statement so the code is easier to follow.
- Encapsulate Record adds a layer between a component and an external data shape or API so the component can use its own API.
- Replace Conditional with Polymorphism moves branching logic into type-specific objects that each implement the same method in their own way.
