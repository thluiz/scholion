---
title: "Callback Hell"
date: '2013-08-21T10:16:25-03:00'
category: webclip
summary: 'The page explains how callback-heavy JavaScript becomes hard to read when functions stay anonymous and deeply nested, and it recommends naming functions, keeping code shallow, and splitting code into modules.'
tags: ["javascript", "callbacks", "modules"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Callback Hell"
    url: "http://callbackhell.com/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2013-08/callbackhell-com--callback-hell.md"
    kind: repo
---

The page describes “callback hell” as the tangled look that asynchronous JavaScript can take when callbacks are nested deeply and function names are missing. It argues that the problem can be reduced with a few habits: name functions, keep the structure shallow, and move repeated code into modules.

## Reading notes

- Asynchronous JavaScript with callbacks is hard to write intuitively, and the result often shows many nested `function` blocks and closing brackets.
- Naming functions makes code easier to read, improves stack traces, and helps avoid deep nesting.
- Keeping code shallow makes it less intimidating and easier to edit, refactor, and work on later.
- Modularizing code is presented as the most important step, with small modules that do one thing and can be assembled into larger ones.
- The example `formuploader.js` exports one function through CommonJS, and the application code then requires that module and uses it in two lines.
- The page says browserify can be used in the browser to load CommonJS modules.
- Promises are described as a more abstract pattern, but the document stays focused on vanilla JavaScript and notes that different developers may prefer different approaches.
