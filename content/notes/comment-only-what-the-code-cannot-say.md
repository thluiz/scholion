---
title: "Comment Only What the Code Cannot Say"
date: '2020-07-05T14:11:25+00:00'
category: webclip
summary: 'Henney argues that comments should add information code cannot express. Wrong, redundant, and stale comments create noise, so code should be rewritten or renamed when it can speak for itself.'
tags: ["comments", "code-quality", "readability"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Comment Only What the Code Cannot Say | by Kevlin Henney | Medium"
    url: "https://medium.com/@kevlinhenney/comment-only-what-the-code-cannot-say-dfdb7b8595ac"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/medium-com--comment-only-what-the-code-cannot-say.md"
    kind: repo
---

Henney says comments are useful only when they add something code cannot say. Comments that repeat code, preserve commented-out code, or replace a better name or structure create noise and distraction, so they should be removed or rewritten.

## Reading notes

- Good comments require judgment about what not to write, just like good writing in general.
- Comments that are wrong are harmful, and incorrect comments can survive in a codebase longer than code errors.
- Comments that restate code add no value, because they repeat knowledge already expressed in code.
- Commented-out code has no useful effect and becomes stale quickly; version control handles history better.
- Noisy and wrong comments can make programmers ignore comments altogether.
- Comments should be treated like code and kept only when they add value for the reader.
- If a comment explains something the code should already make clear, the code should change instead.
- Better variable, method, class, and test names can remove the need for explanatory comments.
- Long functions should often be split into smaller functions so the code structure carries the intent.
- The useful comment is the one that fills the gap between what code can express and what the reader still needs to know.
