---
title: "5 functions of the Console object you didn’t know"
date: '2014-11-07T11:45:34-03:00'
category: webclip
summary: 'The page highlights five lesser-known Console methods for debugging in Chrome: assert, table, profile, group, and time, and briefly explains what each one does.'
tags: ["console", "javascript", "debugging", "chrome-devtools"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "5 functions of the Console object you didn’t know - Blog - Shelly Cloud"
    url: "https://shellycloud.com/blog/2014/11/five-functions-of-the-console-object-you-didnt-know?utm_source=javascriptweekly&utm_medium=email"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2014-11/shellycloud-com--five-functions-of-the-console-object-you-didnt-know.md"
    kind: repo
---

The page points out that the Console object offers more than `console.log()`. It presents five methods that the author describes as useful in everyday work and says they were tested in Google Chrome 38.

## Reading notes

- `console.assert(expression, message)` logs the given message when the first argument is false, and logs nothing when the expression is true.
- `console.table(object)` displays an object or array as a table.
- `console.profile(name)` starts a CPU profiler in the console, saves each run as a separate tab, and should be paired with `console.profileEnd()`.
- `console.group(message)` groups following logs into a dropdown list until `console.groupEnd()` is called, and groups can be nested.
- `console.groupCollapsed(message)` works like `console.group(message)` but starts collapsed.
- `console.time(name)` starts a timer in milliseconds and is stopped with `console.timeEnd(name)` using the same name.
