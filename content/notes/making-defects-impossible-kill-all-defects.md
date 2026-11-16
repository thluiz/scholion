---
title: "Making Defects Impossible"
date: '2020-02-22T12:11:45+00:00'
category: webclip
summary: 'The article argues that recurring bugs can often be reduced by moving checks into the compiler, using immutable objects, modeling valid states in types, and making null handling explicit.'
tags: ["software-defects", "type-safety", "immutability", "null-handling"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Making Defects Impossible - Kill All Defects"
    url: "https://web.archive.org/web/20191206190723id_/https://killalldefects.com/2019/08/29/making-defects-impossible/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/web-archive-org--making-defects-impossible-kill-all-defects.md"
    kind: repo
---

The article says repeated defects are especially frustrating and argues for finding ways to make common errors impossible to hide. It recommends choosing techniques carefully, since some trade readability or other benefits for stronger guarantees.

## Reading notes

- Catch run-time errors at compile time when the language or tooling can detect bad calls and type mismatches early.
- Use immutability to ensure an object stays in a valid state once created, as with `DateTime`.
- Encode valid states in types with discriminated unions so validation becomes part of the type system.
- Treat null as an explicit case with options, so code must handle both present and absent values.
