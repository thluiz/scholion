---
title: "Good programmers worry about data structures and their relationships"
date: '2026-09-25T20:23:20+01:00'
category: webclip
summary: 'The piece argues that good software starts with the data model, because clear data structures make code easier to design, maintain, and extend, and can replace complexity in logic.'
tags: ["data-structures", "software-design", "code-maintenance"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Good programmers worry about data structures and their relationships"
    url: "https://read.engineerscodex.com/p/good-programmers-worry-about-data?ref=dailydev"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/read-engineerscodex-com--good-programmers-worry-about-data-structures-and-their-relat.md"
    kind: repo
---

The article argues, using a Linus Torvalds quote, that good programmers focus on data structures and their relationships rather than only on code. It says software becomes easier to design, maintain, read, and extend when the data model is treated as the starting point.

It gives an example of replacing a 500-line function with a 50-line function plus a better data structure, which improved speed, understanding, and maintenance. It also cites _The Art of Unix Programming_ on folding knowledge into data so program logic can stay simple and robust.

## Reading notes

- Start with the data model before diving into code details.
- Good data structures make software more reliable, understandable, and readable.
- Treating the data model as an afterthought creates more work later.
- A well-thought-out data model makes migrations and building on complex systems easier.
- Restructuring data can remove whole classes of problems and shrink code significantly.
- The article recommends reducing code complexity with stricter interface or database types.
- It also notes that higher-level design thinking matters before detailed implementation.
