---
title: "The Philosophy of Ramda"
date: '2015-02-27T20:20:11-03:00'
category: webclip
summary: 'Ramda says it is a practical functional library for JavaScript programmers, built around small composable functions, immutable data, a shallow API, and parameter order that supports currying.'
tags: ["ramda", "functional-programming", "javascript", "immutability"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "The Philosophy of Ramda"
    url: "http://fr.umio.us/the-philosophy-of-ramda/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-02/fr-umio-us--the-philosophy-of-ramda.md"
    kind: repo
---

Ramda presents itself as a library for JavaScript programmers who want functional pipelines made from small composable functions. Its API is shaped around practical use, not academic purity, and it keeps user data immutable while aiming for simple, consistent calls.

## Reading notes

- Ramda is built to make a functional pipeline style easier in JavaScript.
- The functions are modular, composable, and each takes a single parameter in the example.
- None of the functions mutates its input.
- The library is guided by simplicity, understood as keeping separate concerns from becoming entangled.
- Ramda is for programmers building systems, not for academic exercise.
- Some Ramda behavior may surprise academic users, but it is meant to work well for working programmers.
- Ramda does not try to implement its functions in a functional way internally; it uses imperative `while` loops when needed.
- The library does not try to mirror native JavaScript APIs or other functional languages exactly.
- Ramda is a library or toolbelt, not a framework that dictates application structure.
- It is not a drop-in replacement for Underscore or lodash.
- A key design choice is to put function parameters first and data parameters last.
- Every function is curried so that passing only the function arguments can return a new function.
- This parameter order is presented as essential for automatic currying and composable code.
- Ramda keeps its API shallow and avoids broad multi-behavior functions.
- If one function needs to work on different kinds of values, Ramda prefers separate functions.
- The library tries to avoid becoming an inconsistent and unmaintainable API.
- Consistency rules include using `*By` for single-property comparisons and `*With` for general functions.
- Ramda is meant to support functional programming in JavaScript as a practical day-to-day library.
- JavaScript already has first-class functions, higher-order functions, and lexical closures.
- Ramda helps with immutable data and referential transparency by not storing application state or mutating inputs.
- Lazy evaluation and some pattern matching are under consideration.
- Efficient recursion and homoiconicity are outside Ramda's scope.
- Ramda works mainly with lists implemented as arrays.
- Many functions return lists, which makes composition straightforward.
- `pipe` is included as a reversed form of `compose` because it can express intent more clearly.
- Ramda's implementation favors practicality over elegant recursion because current JavaScript engines handle recursion poorly.
- The API includes functions that seem useful, fit the functional model, and are simple enough to implement.
- The conclusion says Ramda was created because no other library worked the way its authors wanted, and it aims to combine composable functions, immutable data, and simple pipelines.
