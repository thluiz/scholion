---
title: "GitHub - dtanzer/babystepstimer: A timer for the \"baby steps\" exercise/technique for doing TDD"
date: '2026-11-16T03:08:36+00:00'
category: webclip
summary: 'A timer for the baby steps TDD exercise, deliberately built as hard-to-change legacy code for refactoring practice, with multiple language versions and notes on its structure.'
tags: ["tdd", "refactoring-kata", "legacy-code", "baby-steps"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "GitHub - dtanzer/babystepstimer: A timer for the \"baby steps\" exercise/technique for doing TDD"
    url: "https://github.com/dtanzer/babystepstimer"
    kind: repo
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/github-com--babystepstimer-refactoring-kata-legacy-code.md"
    kind: repo
---

A timer for the baby steps TDD exercise, but also a deliberately awkward legacy codebase for refactoring practice. The page says the code is meant to be easy to understand while still being hard to change, and points to variants in several languages.

## Reading notes

- The project is presented as a timer for the "Taking baby steps" TDD exercise.
- It is also described as bad legacy code that can be used for refactoring exercises.
- The author says the code was created for a refactoring screen cast and for practice with legacy code sessions.
- The listed characteristics include single responsibility violations, high coupling, low cohesion, and direct use of low-level APIs.
- The code has reasonably clear names, so it is meant to be understandable even when it is difficult to change.
- The UI is described as complicated because it renders HTML inside a Swing application.
- The timer window can be moved with the mouse and stays on top once started.
- When the timer reaches zero, it turns red and the text says to throw away everything written in the last two minutes.
- When the red/green/refactoring cycle finishes before zero, the instruction is to commit changes and press Reset.
- The project includes contributed versions in C#, C++, Swift iOS, Objective-C iOS, TypeScript, and JavaScript.
- The project uses CC-licensed sounds from freesound.org.
- The code is licensed under Apache License 2.0.
