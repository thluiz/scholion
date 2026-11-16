---
title: "Code Smells in JavaScript. We look at feature envy and intimate…"
date: '2026-11-16T05:49:16+00:00'
category: webclip
summary: 'The article defines code smells and explains feature envy in JavaScript: one class relies too much on another class’s fields, which breaks encapsulation.'
tags: ["javascript", "code-smells", "encapsulation"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Code Smells in JavaScript. We look at feature envy and intimate… | by John Au-Yeung | Better Programming"
    url: "https://medium.com/better-programming/more-code-smells-in-javascript-113067dbd89f"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/medium-com--code-smells-in-javascript-feature-envy-intimate-classes.md"
    kind: repo
---

The article defines a code smell as a characteristic of code that may point to deeper problems, and says code quality can be judged by looking for these signs. It then focuses on feature envy and classes that are too intimate.

## Reading notes

- A code smell is a characteristic of code that suggests deeper problems.
- Feature envy happens when one class uses too many features of another class.
- The article says this often shows up when one class references another class’s fields excessively.
- The ShapeCalculator example uses many fields from Rectangle.
- This use exposes Rectangle fields such as height and width and breaks encapsulation.
