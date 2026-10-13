---
title: "When To Comment Your Code"
date: '2013-09-27T10:19:14-03:00'
category: webclip
summary: 'The post argues that code should usually explain itself, and comments should be reserved for what the code cannot say, especially why something is done or why a choice was avoided.'
tags: ["comments", "self-documenting-code", "clean-code"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Ardalis - When To Comment Your Code"
    url: "http://ardalis.com/when-to-comment-your-code"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2013-09/ardalis-com--when-to-comment-your-code.md"
    kind: repo
---

The post says comments should be used sparingly because code should be simple enough to explain itself. When comments are needed, they should explain why something was chosen, describe hazards, or document public APIs.

## Reading notes

- Early in programming, comments were useful for assignments and for describing intent in English when the code was simple.
- In college, comments were needed mainly to help understand unfamiliar Scheme syntax.
- Self-documenting code is presented as code that is easier to read and understand.
- Comments should explain the why instead of the how or what.
- Code should be improved before adding comments when the code is hard to understand.
- Comments that repeat what the code already says add noise and violate the Don’t Repeat Yourself principle.
- Comments can be wrong, and if code and comments disagree, both are probably wrong.
- Simple, descriptive names and small, single-purpose methods reduce the need for comments.
- Comments can be useful during design to organize steps, but those step comments should often become method names.
- Comments should express what code cannot say, not what it already says.
- Comments should also warn about dangers, unusual constraints, or reasons not to optimize or change something.
- Tests with expressive names can document behavior and reduce the need for comments.
- Generated documentation from comments can be useful for public APIs, but often adds little beyond obvious information.
- Clean code and source control are better places than comments for many kinds of boilerplate or history.
- The overall conclusion is that comments are mainly a fallback when code cannot express something clearly enough.
