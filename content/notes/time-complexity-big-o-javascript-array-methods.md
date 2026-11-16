---
title: "Time complexity Big O for Javascript Array methods and examples"
date: '2020-06-03T22:00:14+00:00'
category: webclip
summary: 'The post lists common JavaScript Array methods, groups them by mutator, accessor, iteration, and bonus methods, and gives each one’s Big O time complexity with short examples.'
tags: ["javascript", "array-methods", "big-o", "time-complexity"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Time complexity Big 0 for Javascript Array methods and examples."
    url: "https://dev.to/lukocastillo/time-complexity-big-0-for-javascript-array-methods-and-examples-mlg"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/dev-to--time-complexity-big-o-javascript-array-methods.md"
    kind: repo
---

The post groups common JavaScript array methods by what they do and gives each one’s Big O time complexity. It covers mutator, accessor, and iteration methods, then adds `some()` and `every()` as bonus cases.

## Reading notes

- `push()` and `pop()` are O(1) because they add or remove an element at the end of the array.
- `shift()`, `unshift()`, and `splice()` are O(n) because they can move elements in the array.
- `sort()` is O(n log(n)) and can use a compare function for custom ordering.
- `concat()`, `slice()`, and `indexOf()` are O(n).
- `forEach()`, `map()`, `filter()`, and `reduce()` are O(n) because they process each element in the array.
- `some()` returns true when it finds one or more matching items, and false otherwise.
- `every()` returns true only when all items match the given condition.
- The conclusion says understanding these methods helps calculate the time complexity of larger algorithms built from arrays.
