---
title: "Flexibility Equates to Lower Quality"
date: '2020-02-22T12:12:01+00:00'
category: webclip
summary: 'The post argues that flexible languages and many syntax choices raise code ambiguity and hurt maintainability. Simpler, more restricted languages and stricter rules are presented as a path to higher quality.'
tags: ["software-development", "programming-languages", "maintainability"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Flexibility Equates to Lower Quality"
    url: "https://yegor256.com/2017/04/11/flexibility-equates-lower-quality.html"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/yegor256-com--flexibility-equates-to-lower-quality.md"
    kind: repo
---

The post contrasts “if it works, it’s good” with “if it’s good, it works” and applies that tension to software source code. It uses Ruby and Java examples to show that multiple valid forms can make code easier to write but harder to read and maintain.

## Reading notes

- The argument centers on source code, not just OOP in general.
- Perl is described as a language that can do the same thing in three different ways, leaving no single “right” form.
- Ruby examples show several ways to write the same conditional assignment.
- Java is presented as stricter and closer to “make it right and it will work.”
- The difference matters depending on whether programmers are writing code or reading it.
- The post distinguishes between code owners and designers, linking the first to a hacker mentality and the second to a designer mentality.
- Too much syntactic sugar is framed as useful for self-expression and showing off, but annoying to read.
- Ruby’s philosophy is summarized as accepting many forms as long as they work.
- Java’s strong and static typing are treated as supporting the opposite view.
- The main claim is that more flexible languages tend to produce lower maintainability.
- The same logic is extended to software development in general: fewer options and more restrictions can improve quality.
- Tools like Checkstyle and Rubocop are mentioned as attempts to restrict language features, though they are said to lag behind programmer creativity.
- The post concludes that modern OOP languages such as Java, Ruby, and C++ have too many features and that this reduces maintainability.
