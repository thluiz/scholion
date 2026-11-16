---
title: "Spreading, Destructuring and Rest Parameters in Javascript"
date: '2026-11-16T01:27:38+00:00'
category: webclip
summary: 'The article explains how spread syntax, destructuring, and rest parameters help work with arrays and objects, reduce code length, and make assignments, copies, and function arguments easier to handle.'
tags: ["javascript", "spread-syntax", "destructuring", "rest-parameters"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Spreading, Destructuring and Rest Parameters in Javascript"
    url: "https://dev.to/puf17640/spreading-destructuring-and-rest-parameters-in-javascript-1haf"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/dev-to--spreading-destructuring-and-rest-parameters-in-javascript.md"
    kind: repo
---

The article introduces three ECMAScript 2015 features for arrays and objects. Spread syntax is used to unpack values, make shallow copies, update objects, concatenate arrays, and split strings into character arrays. Destructuring is used to assign object and array values to variables, including nested values, renamed variables, defaults, and primitive properties. Rest parameters collect an arbitrary number of function arguments into an array and can also be used in object and array destructuring.

## Reading notes

- Spread syntax (`...`) can unpack arrays and objects and create shallow copies.
- Spreading can copy an object, similar to `Object.assign()`, and can also update object properties.
- Nested objects must also be spread when updating them, or they are overwritten.
- Spreading can duplicate arrays, concatenate arrays, and turn a string into an array of characters.
- Object destructuring can map properties to variables in one assignment, including renamed variables.
- Destructuring also works with nested object properties and primitive values such as `String.length`.
- Array destructuring assigns values by position, can skip entries, and can handle nested arrays.
- Object and array destructuring can be combined, and defaults can be used while destructuring.
- Rest parameters gather remaining function arguments into an array.
- Rest syntax can also be used to collect remaining properties from an object or remaining items from an array.
