---
title: "Code Smell: No AND in Function name"
date: '2019-06-25T21:05:58+00:00'
category: webclip
summary: 'The page says function names with “AND” usually signal too much responsibility. Split the work into separate functions so each one does one thing and stays easier to maintain.'
tags: ["single-responsibility-principle", "function-naming", "maintainability"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Code Smell: No AND in Function name"
    url: "https://dev.to/samanthaming/code-smell-no-and-in-function-name-1g10"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/dev-to--code-smell-no-and-in-function-name.md"
    kind: repo
---

The page argues that a function should follow the Single Responsibility Principle and do one thing only. If a name includes “AND”, it usually means the function is handling more than one concern, so the better fix is to split it into separate functions.

## Reading notes

- A function name with “AND” suggests the function is doing too much.
- The recommended solution is to remove “AND” and split the work into separate functions.
- The Single Responsibility Principle says each module should have one responsibility, with separate concerns kept in separate modules.
- Following SRP makes a code base more flexible and modular.
- The article says the same idea applies in non-dev terms, using examples of ingredients sold separately versus pre-mixed.
- Separate functions are easier to maintain as requirements change.
- A single function that does multiple things can become bloated and difficult to maintain over time.
- One community suggestion is to start function names with a verb.
- Another comment recommends using specific names instead of generic ones like `getData()`.
