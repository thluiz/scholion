---
title: "Untangle Spaghetti Code with Context Objects"
date: '2020-02-22T12:11:49+00:00'
category: webclip
summary: 'The article argues that context objects can reduce parameter explosion in spaghetti code, localize changes, and cut merge conflicts, while warning against turning them into oversized objects with application logic.'
tags: ["spaghetti-code", "context-objects", "parameter-explosion", "maintainability"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Untangle Spaghetti Code with Context Objects - Kill All Defects"
    url: "https://web.archive.org/web/20200923054153id_/https://killalldefects.com/2020/01/15/untangle-spaghetti-code-with-context-objects/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/web-archive-org--untangle-spaghetti-code-with-context-objects.md"
    kind: repo
---

Context objects are presented as a way to bundle commonly used state into one place instead of passing many parameters through multiple methods. The article says this can make it easier to add new state, speed up development, and keep changes closer to the problem being solved. It also notes that lazy loading can avoid paying for expensive data fetches when the data is never needed.

## Reading notes

- Spaghetti code is described as code that must be traced file to file, has methods with growing parameter lists, and is only comprehensible to its creator.
- Adding a new parameter to support a change can force updates in many upstream methods.
- If the new data requires a database call or external API, every upstream caller may need to handle that operation.
- This kind of change increases merge conflicts and can lead to methods with too many parameters.
- A context object wraps commonly used values into a single object instead of passing each one separately.
- New fields can be added to the context object directly, either when it is created or through lazy loading.
- Lazy loading performs expensive work only when the value is first needed.
- The main benefits are easier state growth, faster new development, and fewer unrelated connecting changes.
- The article warns that context objects can become overly large god objects.
- It also warns against putting application logic in context objects.
- Small pieces of state should be grouped into more appropriate objects, such as a `Person` object for first name, last name, and age.
- The article recommends immutable state in context objects, with no setters except for lazy-loaded values.
- It also recommends avoiding methods in context objects except private helpers for lazy loading.
- Properly used, context objects can reduce code churn, merge conflicts, and review noise in larger web applications, especially without formal dependency injection support.
