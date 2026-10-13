---
title: "Essential JavaScript Interview Questions"
date: '2016-04-11T13:15:39-03:00'
category: webclip
summary: 'A list of JavaScript interview prompts covering scope, hoisting, strict mode, coercion, closures, recursion, async timing, and DOM traversal, with no answers shown in the captured text.'
tags: ["javascript", "interview-questions", "scope", "closures"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Essential JavaScript Interview Questions"
    url: "https://www.toptal.com/javascript/interview-questions"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2016-04/toptal-com--essential-javascript-interview-questions.md"
    kind: repo
---

A collection of 25 JavaScript interview questions. The page focuses on language behavior, including object checks, variable scope, `this`, strict mode, return parsing, `NaN`, floating-point precision, integer tests, closures, recursion, event loop timing, logical operators, type coercion, object property keys, and DOM traversal.

## Reading notes

- The page lists questions about `typeof` checks on objects and a possible pitfall with `typeof bar === "object"`.
- It asks about the output of code that assigns `var a = b = 3` inside an IIFE.
- It includes a question about `this` and `self` in nested functions.
- It asks why a whole JavaScript source file might be wrapped in a function block.
- It asks for the significance and benefits of `'use strict'` at the top of a source file.
- It compares two functions where one return statement is followed by a newline before an object literal.
- It asks what `NaN` is, its type, and how to test for it reliably.
- It includes a question about `0.1 + 0.2` and equality with `0.3`.
- It asks for possible ways to write `isInteger(x)`.
- It asks about console logging order with `setTimeout` delays of `1000` and `0`.
- It asks for a short palindrome function.
- It asks for a `sum` method that works as both `sum(2,3)` and `sum(2)(3)`.
- It asks about a loop creating buttons with click handlers that reference `i`.
- It asks about array mutation after `reverse()` and `push()`.
- It asks about string and number coercion in several `console.log` expressions.
- It asks how to avoid stack overflow in a recursive list processor while keeping the recursive pattern.
- It asks what a closure is and requests an example.
- It asks about delayed logging in a loop and how closures can help.
- It asks how `||` and `&&` evaluate and what values they return.
- It asks about `false == '0'` and `false === '0'`.
- It asks what happens when objects are used as property keys.
- It includes a recursive factorial-style function call.
- It includes a nested immediately invoked function expression that logs a captured variable.
- It asks about losing `this` when a method is assigned to another variable.
- It asks for a function that visits a DOM element and all of its descendants and passes each to a callback.
