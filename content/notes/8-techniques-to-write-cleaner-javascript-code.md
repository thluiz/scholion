---
title: "8 techniques to write cleaner JavaScript code"
date: '2022-03-17T11:21:59-03:00'
category: webclip
summary: 'The article lists eight ways to make JavaScript easier to read and maintain: pure functions, named or object parameters, destructuring, constants for hard-coded values, method chaining, promises, and async/await.'
tags: ["javascript", "clean-code", "webdev", "promises"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "8 techniques to write cleaner JavaScript code - DEV Community 👩‍💻👨‍💻"
    url: "https://dev.to/codewithahsan/8-techniques-to-write-cleaner-javascript-code-369e"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2022-03/dev-to--8-techniques-to-write-cleaner-javascript-code.md"
    kind: repo
---

The article argues that cleaner JavaScript comes from code that is easier to read, test, and understand. It illustrates each technique with small examples, then rewrites them to reduce hidden dependencies, unclear parameters, repeated property access, and nested async callbacks.

## Reading notes

- Pure functions always return the same output for the same inputs and do not change outside variables.
- When a function has many arguments, passing an object with named properties is clearer than relying on positional parameters.
- Object and array destructuring reduce repeated property and index access.
- Hard-coded values should be replaced with named constants so their meaning is visible.
- Short variable names like `t` make code harder to trace when the context is not obvious.
- `Object.assign()` can help build a new object while applying default values from a config object.
- Method chaining becomes useful when several methods are meant to be called in sequence on the same object.
- Promises and `async`/`await` make asynchronous code easier to read than nested callbacks.
