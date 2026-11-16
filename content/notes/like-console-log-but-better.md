---
title: "Like `console.log` But Better"
date: '2026-11-16T00:30:36+00:00'
category: webclip
summary: 'The page shows console methods and log styling that make debugging clearer, including `console.table()`, `console.count()`, `console.assert()`, labels, and CSS styling with `%c`.'
tags: ["javascript", "console", "debugging"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Like `console.log` But Better"
    url: "https://dev.to/leirasanchez/like-console-log-but-better-nhm"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/dev-to--like-console-log-but-better.md"
    kind: repo
---

The page says the console offers more than `log` and that these methods can make debugging less confusing. It highlights ways to display data more clearly, count calls, check assertions, and style log output.

## Reading notes

- `console.table()` shows arrays and objects in a table, with rows for elements or properties and optional column names.
- `console.count()` keeps track of how many times it has been called, and a string label can be provided.
- `console.assert()` only writes to the console when the assertion is false, using the second argument as the error message.
- Labels can be added to `console.log()` by passing a string first, which helps organize the output.
- `%c` can be added to the first string in `console.log()` and CSS styles can be passed as the next argument to color and style the message.
