---
title: "Extract Functions Arguments using Destructure in JavaScript"
date: '2020-09-07T16:47:30-03:00'
category: webclip
summary: 'The page shows how to collect function arguments with rest parameters and unpack them with array destructuring, while distinguishing parameters, arguments, and the `arguments` object.'
tags: ["javascript", "destructuring", "rest-parameters", "function-arguments"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Extract Functions Arguments using Destructure in JavaScript - DEV Community 👩‍💻👨‍💻"
    url: "https://dev.to/samanthaming/extract-functions-arguments-using-destructure-in-javascript-169k"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2020-09/dev-to--extract-functions-arguments-using-destructure-in-javascript.md"
    kind: repo
---

The page explains a simple pattern for handling function inputs in JavaScript: collect the passed values with a rest parameter, then unpack them with array destructuring. It also separates the idea of a parameter from the actual argument value and contrasts both with the built-in `arguments` object.

## Reading notes

- Use `...args` to collect passed values into a real array, then assign them with `[egg, cheese] = args`
- The `arguments` object exists in every non-arrow function, but it is array-like rather than an array
- A parameter is the variable in the function declaration, while an argument is the value passed at call time
- The page recommends rest parameters over `arguments` because they are explicit and return a real array
- AirBnB style guidance says not to name a parameter `arguments`
- The page shows that defaults can be set directly in the header with `...[egg = '', cheese = '']`
- It also shows that rest parameters can be destructured directly as `...[egg, cheese]`
