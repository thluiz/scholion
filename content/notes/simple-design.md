---
title: "Simple Design"
date: '2026-11-16T04:46:22+00:00'
category: webclip
summary: 'Kent Beck’s Simple Design rules prioritize working code first, then clarity, then avoiding duplication, and only after that reducing the number of classes, methods, and modules.'
tags: ["simple-design", "kent-beck", "xp", "dry"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Simple Design"
    url: "https://deviq.com/practices/simple-design"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/deviq-com--simple-design.md"
    kind: repo
---

Simple Design is presented as a priority order for code. First, code should pass all tests. After that, it should express the author’s ideas clearly enough for future developers to understand it.

The text treats duplication and small size as lower-priority concerns. DRY applies only when it does not break working code or readability, and reducing classes, methods, and modules comes last if the first three rules are already satisfied.

## Reading notes

- Kent Beck’s four rules are also called The Four Commandments or the XP Simplicity Rules.
- The highest priority is that the code works, which XP developers verify through automated unit tests.
- Code should be clear, consistent, and expressive so future developers can understand the author’s intent.
- DRY is described as the third rule, but it can be set aside if it would harm working code or clarity.
- Minimizing classes, methods, and modules is the lowest-priority rule and should only be pursued after the first three are met.
- JB Rainsberger offers a similar view with the four elements of simple design.
