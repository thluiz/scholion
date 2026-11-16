---
title: "Each Private Static Method Is a Candidate for a New Class"
date: '2026-11-16T02:43:27+00:00'
category: webclip
summary: 'The article argues that private static methods should usually become classes instead, because classes can be reused and tested while private static methods cannot.'
tags: ["private-static-methods", "reusability", "testability", "oop"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Each Private Static Method Is a Candidate for a New Class"
    url: "https://yegor256.com/2017/02/07/private-method-is-new-class.html"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/yegor256-com--each-private-static-method-is-a-candidate-for-a-new-class.md"
    kind: repo
---

The article argues that when a private static method appears to factor out logic, it is often a sign that the logic should live in a separate class. The key difference is that a class can be reused and tested, while a private static method cannot.

## Reading notes

- A private static method may make code shorter, but it stays confined to one class.
- If the same logic is needed elsewhere, the method has to be copied and pasted.
- A separate class makes the shared behavior reusable.
- The example refactors URL encoding into an `Encoded` class.
- That class can be used in multiple places and covered by a unit test.
- The author treats each private static method as a candidate for a new class.
- The note also says this reasoning may apply to all private methods, not only static ones.
