---
title: "Iteration: A Gentle Introduction to Functional Programming"
date: '2020-07-12T10:33:39-03:00'
category: webclip
summary: 'The page shows how to move from loops to reusable functional tools like forEach, map, prop, curry, and compose, making dependencies explicit and code easier to test and combine.'
tags: ["functional-programming", "javascript", "iteration", "composition"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Iteration: A Gentle Introduction to Functional Programming | by Tim Roberts | Medium"
    url: "https://medium.com/@BeardedTim/iteration-a-gentle-introduction-to-functional-programming-c59fcb0ab58d"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2020-07/medium-com--iteration-gentle-introduction-to-functional-programming.md"
    kind: repo
---

The article uses simple JavaScript examples to show how functional programming turns repeated loop logic into small reusable functions. It starts with printing names from a list, then generalizes the idea with forEach and map, and then makes property access and transformations more explicit with prop, curry, and compose.

## Reading notes

- A loop that prints names can be wrapped in a function so the iteration details stay hidden and the caller only needs to know what the function does.
- The same iteration pattern can print ages instead of names by changing only the action applied to each item, not the loop structure.
- forEach expresses the idea of iterating over a list and performing a function on each item.
- map expresses the idea of building a new list by transforming each value, instead of changing the original list.
- prop is introduced to read a given property from an object, and then rewritten as a curried function so it can be partially applied.
- currying lets map receive a transformation function created earlier, which makes dependencies more explicit.
- compose is described as a helper that takes several functions and returns one function that applies them in reverse order to an initial value.
- Small functions such as prop, curry, and uppercase are presented as reusable pieces that can be combined to solve domain-specific tasks.
- The article links functional style to simpler unit testing because each function depends only on its input and output.
- It also argues that this style improves productivity by making code easier to reuse across problems.
