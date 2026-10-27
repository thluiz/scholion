---
title: "Functions Explained"
date: '2013-02-23T22:02:55-03:00'
category: webclip
summary: 'The post explains JavaScript functions as named blocks, then shows how arguments, hoisting, declaration versus expression, scope, and naming affect behavior and debugging.'
tags: ["javascript", "functions", "hoisting", "debugging"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Functions Explained - Mark Daggett's Blog"
    url: "http://markdaggett.com/blog/2013/02/15/functions-explained/?utm_source=javascriptweekly&utm_medium=email"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2013-02/markdaggett-com--functions-explained.md"
    kind: repo
---

The post treats JavaScript functions as named blocks that can be invoked on demand. It explains how arguments behave differently for complex and primitive values, how declarations and expressions are evaluated at different times, and how function scope differs from block scope.

## Reading notes

- Functions are presented as named blocks that developers can call when needed.
- Complex values are passed by reference, so changes inside the function can affect the original object.
- Primitive values are passed by value, so reassignment inside the function does not change the original variable.
- Function declarations are parsed and hoisted before execution, so they can be called before they appear in the source.
- Function expressions are assigned at runtime, so calling them before assignment results in an error.
- A function expression with the same name as a declaration is treated as a separate entity because it belongs to the assignment expression.
- Function declarations cannot be conditionally defined, and the post advises against placing them inside control flow statements.
- JavaScript scope is described as function-scoped rather than block-scoped, unlike the Ruby example shown in the post.
- A for loop uses the enclosing scope, so variables remain accessible after the loop ends.
- Naming function expressions helps debugging because the name appears in the function's own scope and in stack traces.
