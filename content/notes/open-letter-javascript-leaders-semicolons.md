---
title: "An Open Letter to JavaScript Leaders Regarding Semicolons"
date: '2014-07-06T13:03:27-03:00'
category: webclip
summary: 'The post argues that JavaScript semicolon rules are understandable, that minimal-semicolon and comma-first style is safe, and that leaders should stop spreading fear about ASI.'
tags: ["javascript", "semicolons", "asi", "style"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "blog.izs.me: An Open Letter to JavaScript Leaders Regarding Semicolons"
    url: "http://blog.izs.me/post/2353458699/an-open-letter-to-javascript-leaders-regarding"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2014-07/blog-izs-me--open-letter-javascript-leaders-semicolons.md"
    kind: repo
---

The post argues that minimal semicolons and comma-first formatting are valid JavaScript and safe in browsers and tools. It says the real issue is understanding how JavaScript statements end, especially automatic semicolon insertion and restricted productions.

It also claims that lining important tokens up on the left makes code easier to scan, while semicolons everywhere are mainly justified by aesthetics, consistency, or linter rules. The author says people who guide others in JavaScript should know these rules and avoid repeating claims that semicolons make code safer.

## Reading notes

- Comma-first formatting and minimal semicolons are presented as valid and safe in browser code and common minifiers.
- The rules for statement termination are summarized through four cases: unclosed constructs, `++` and `--`, control structures without blocks, and lines that begin with continuation-like tokens.
- Prefixing continuation lines with semicolons is described as a simple way to avoid ambiguity.
- `return`, `throw`, `break`, `continue`, and postfix `++` or `--` are described as restricted productions where a newline ends the statement.
- The post argues that these cases become easier to spot when statements are not always forced to end with semicolons.
- The left edge is described as easier for humans to scan than a missing token on the right edge.
- Semicolons everywhere are defended mainly for aesthetics, politics, or linter consistency.
- The author rejects the claim that semicolons make code safer, saying they do not fix ASI problems and do not remove the need to understand statement termination.
- People who give JavaScript guidance are told to know the rules, admit limits, and avoid spreading uncertainty.
- In the addenda, the author answers objections about naming leaders, punctuation in English, and accusations of pedantry by restating that code style is a choice but false claims are not.
