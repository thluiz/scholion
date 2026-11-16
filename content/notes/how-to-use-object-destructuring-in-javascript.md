---
title: "How to Use Object Destructuring in JavaScript"
date: '2026-11-16T04:01:58+00:00'
category: webclip
summary: 'Explains how object destructuring assigns object properties to variables, supports multiple properties, default values, aliases, nested objects, dynamic property names, rest, and common usage in loops and function parameters.'
tags: ["javascript", "object-destructuring", "es2015", "rest-syntax"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "How to Use Object Destructuring in JavaScript"
    url: "https://dmitripavlutin.com/javascript-object-destructuring"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/dmitripavlutin-com--how-to-use-object-destructuring-in-javascript.md"
    kind: repo
---

Object destructuring in JavaScript lets you extract properties from an object and bind them to variables without repeating the object name each time. The post shows how that syntax replaces several separate property-access assignments with one statement, and how it can also handle multiple properties at once.

## Reading notes

- Extracting properties with destructuring avoids boilerplate by binding `hero.name` and `hero.realName` directly to variables in one statement.
- The basic pattern is `const { identifier } = expression`, which assigns the object property value to a variable with the same name.
- Multiple properties can be extracted at once by listing them inside the braces, separated by commas.
- If a property is missing, the variable becomes `undefined` unless a default value is provided in the pattern.
- Aliases let you create a variable name different from the property name, as in `realName: secretName`.
- Nested object destructuring can reach into inner objects, and the nesting can be extended as far as needed.
- Dynamic property names can be destructured with bracket notation, using a runtime value to choose the property.
- The rest syntax collects the remaining properties into a separate object after one or more properties have been extracted.
- Destructuring works with `const`, `let`, and `var`, and it can also assign to an already declared variable.
- The post shows destructuring inside a `for..of` loop and inside a function parameter, where the parameter is destructured before the function body uses it.
