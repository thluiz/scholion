---
title: "The key points of Working Effectively with Legacy Code - Change Messy Software Without Breaking It"
date: '2020-07-05T14:11:20+00:00'
category: webclip
summary: 'The book argues that the safest way to change legacy code is to add fast automated tests first, then refactor. It introduces seams, characterization tests, and Sprout/Wrap techniques for risky code.'
tags: ["legacy-code", "testing", "refactoring", "seams"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "The key points of Working Effectively with Legacy Code - Change Messy Software Without Breaking It"
    url: "https://understandlegacycode.com/blog/key-points-of-working-effectively-with-legacy-code"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/understandlegacycode-com--the-key-points-of-working-effectively-with-legacy-code.md"
    kind: repo
---

The post summarizes Michael Feathers’ book as a practical guide for changing legacy code without breaking behavior. Its core advice is to create automated feedback first, because tests make later changes and refactoring safer.

## Reading notes

- Add tests before changing existing code, so you can preserve current behavior.
- When tests are hard to add, change as little code as possible and use minimal, safe refactorings.
- Identify seams as places where behavior can be altered without changing source code.
- Break dependencies first, because external services, databases, and complex setup often block testing.
- Prefer fast tests that do not talk to infrastructure.
- Characterization tests capture the current behavior of hard-to-understand code and keep it stable during refactoring.
- Use the Sprout technique to build new tested code elsewhere, then call it from legacy code.
- Use the Wrap technique when the new logic should happen before or after an existing method call.
- Scratch refactoring can help you understand opaque code if you revert the changes afterward.
- Avoid depending directly on library implementations, since those dependencies spread through the codebase and make upgrades harder.
- The book is presented as still useful because its advice stays relevant for legacy code work.
