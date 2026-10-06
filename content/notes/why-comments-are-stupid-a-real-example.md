---
title: "Why Comments Are Stupid, a Real Example"
date: '2015-04-14T12:27:43-03:00'
category: webclip
summary: 'The post argues that comments often signal unclear naming or oversized methods, and shows a .NET refactor where better names and structure remove comments without reducing clarity.'
tags: ["comments", "refactoring", "clean-code", "dotnet"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Making the Complex Simple"
    url: "http://simpleprogrammer.com/2015/04/13/why-comments-are-stupid-a-real-example/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-04/simpleprogrammer-com--why-comments-are-stupid-a-real-example.md"
    kind: repo
---

The author argues that comments often appear because code is not naming things clearly enough or because methods are too large. After reading Code Complete and Clean Code, he came to see comments as a sign that code should express intent better on its own.

He uses a .NET Framework method, SplitDirectoryFile, to show how comments can be replaced by clearer variable names, smaller methods, and a class that encapsulates the logic. The refactor removes comments while keeping the code understandable, and the author says code that communicates intent directly is easier to maintain.

## Reading notes

- Comments often cover for weak naming or methods that are too large.
- Better naming can communicate assumptions that were previously written as comments.
- A method can sometimes be replaced by a clearer helper or a boolean or value that makes the intent explicit.
- Refactoring the example into a class helps express the logic more clearly.
- The author treats the refactor as a net gain because code changes, while comments often do not.
