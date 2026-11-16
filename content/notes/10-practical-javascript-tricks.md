---
title: "10 Practical JavaScript Tricks"
date: '2020-07-05T14:11:24+00:00'
category: webclip
summary: 'The post collects small JavaScript shortcuts for arrays, conditionals, swapping values, dynamic properties, and unique filtering, while warning that code still needs to work across browsers.'
tags: ["javascript", "arrays", "es6", "browser-compatibility"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "10 Practical JavaScript Tricks"
    url: "https://dev.to/zandershirley/10-practical-javascript-tricks-2b7h"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/dev-to--10-practical-javascript-tricks.md"
    kind: repo
---

The post lists small JavaScript shortcuts for working with arrays, conditionals, and objects. It shows how to turn `arguments` into an array, sum array values with `reduce`, use short-circuit conditionals and `||` defaults, resize arrays through `length`, swap values with destructuring, build dynamic property names, and filter unique values with `Set`.

It also notes that efficiency matters less than responsibility, and says a website needs to work in all browsers. The closing point recommends using Endtest or similar tools to check that behavior.

## Reading notes

- Convert the `arguments` object into a regular array with `Array.prototype.slice.call(arguments)`.
- Sum array values with `reduce` instead of using a loop.
- Use `hungry && goToFridge()` to replace a simple `if` block.
- Assign a fallback value with `arg1 = arg1 || 32`.
- Use the comma operator to evaluate expressions from left to right and return the last value.
- Change `array.length` to shorten an array or empty it.
- Swap two values with array destructuring.
- Use `sort(function() { return Math.random() - 0.5 })` to shuffle an array.
- Create dynamic object property names with computed bracket syntax.
- Remove duplicates by wrapping an array in `Set` and spreading the result.
- The closing note says responsibility matters more than efficiency.
- The post says a website needs to work in all browsers and mentions Endtest as a way to check that.
