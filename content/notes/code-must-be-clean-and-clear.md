---
title: "Code Must Be Clean. And Clear."
date: '2026-11-16T03:02:55+00:00'
category: webclip
summary: 'The page argues that clean code is only the first step. Maintainability also depends on code being clear enough for strangers to understand, modify, and fix bugs quickly.'
tags: ["clean-code", "maintainability", "readability"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Code Must Be Clean. And Clear."
    url: "https://yegor256.com/2018/09/12/clear-code.html"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/yegor256-com--code-must-be-clean-and-clear.md"
    kind: repo
---

The page argues that code should be both clean and clear. Clean code removes anti-patterns and other sources of dirt, but that is not enough if other people cannot understand how to use or modify it.

## Reading notes

- Clean code is compared to a clean kitchen: free of dirt, but still unusable if the controls are not understandable.
- Cleaning code removes problems such as large methods, non-descriptive variable names, tight coupling, and weak SOLID or SRP compliance.
- Cleanliness is important, but the page says it is not the most important goal.
- Code can be clean and still be difficult for others to understand.
- “Others” includes current teammates and future contributors who were not involved in writing it.
- The code should speak the language of the people who need to use it, not only the language of its designer.
- A practical test is to ask someone outside the project to inspect the code or fix a bug in about 30 minutes.
- Maintainability is defined by whether a stranger can modify the code and fix a bug in less than an hour.
- Cleanliness helps maintainability, but the page says that strangers repeatedly seeing the code, trying to contribute, and reporting unclear parts is what improves it most.
