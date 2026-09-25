---
title: "Clean Code: The Good, the Bad and the Ugly"
date: '2026-09-25T08:50:01+01:00'
category: webclip
summary: 'The article praises Clean Code for naming, readability and code-smell awareness, but criticizes its outdated Java focus, dogmatic advice and verbose examples, especially the prime generator.'
tags: ["clean-code", "software-engineering", "code-quality", "refactoring"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Clean Code: The Good, the Bad and the Ugly"
    url: "https://gerlacdt.github.io/blog/posts/clean_code/?ref=dailydev"
    kind: repo
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/gerlacdt-github-io--clean-code-the-good-the-bad-and-the-ugly.md"
    kind: repo
---

The article says _Clean Code_ had a major impact on developers by making code quality, readability and maintainability central concerns. It highlights advice on naming, tests, SRP, DRY, CQS, boundaries, data abstractions and code smells, while also arguing that some recommendations are outdated or too dogmatic.

## Reading notes

- The book helped create awareness around code quality and made readability and maintainability a larger focus in programming.
- It gives lasting advice on naming, exception handling, unit tests, SRP, pure functions, CQS, DRY, boundaries and data abstractions.
- The author values the code-smells compendium because it teaches how to detect bad code as well as write good code.
- A main criticism is that parts of the book are obsolete, especially the heavy Java focus, the reliance on EJBs and AspectJ, and the shallow treatment of concurrency.
- The article says the book does not cover functional programming enough, including immutability, referential transparency, higher-order functions and avoiding side effects.
- Its presentation of principles is described as dogmatic, which can encourage cargo-cult programming when rules are applied without context.
- The article argues that duplication can sometimes be acceptable and that higher design concerns like coupling, cohesion and information hiding should come first.
- The code examples are presented as the ugly part of the book because they are verbose, Java-specific and often harder to understand than the lessons they are meant to teach.
- The prime generator example is used to show excessive function granularity, long names, many side effects, violation of CQS and problematic use of static state.
- The conclusion recommends Clean Code for new programmers, but not as the first software engineering book, and suggests other books that explain practices, trade-offs and reasons more openly.
