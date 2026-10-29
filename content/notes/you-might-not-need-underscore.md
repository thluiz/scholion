---
title: "You Might Not Need Underscore"
date: '2015-07-13T15:28:37-03:00'
category: webclip
summary: 'The post argues that many tasks once covered by Underscore or lodash are now easier with standard JavaScript, so simpler code can avoid extra library knowledge and still stay maintainable.'
tags: ["javascript", "standard-library", "underscore", "lodash"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "You Might Not Need Underscore | Reindex"
    url: "https://www.reindex.io/blog/you-might-not-need-underscore/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-07/reindex-io--you-might-not-need-underscore.md"
    kind: repo
---

The post argues that utility libraries can make code easier to write, but not necessarily simpler to read or maintain. Using standard library functions reduces the need to know a separate abstraction, and modern JavaScript features cover many patterns that older utility libraries used to provide.

## Reading notes

- Utility libraries such as Underscore and lodash became common in JavaScript toolchains.
- Code that relies on the standard library is easier for future readers and maintainers to understand.
- Writing speed is presented as less important than maintainable code.
- It is easier to recover from no abstraction than from the wrong abstraction.
- Repeated patterns in code are the point at which abstraction becomes useful.
- ES2015 and ES2016 add features that replace several utility-library functions.
- Babel makes those newer features usable in current tooling.
- Learning the language itself is described as a transferable skill that outlasts a utility library.
- The post says utility libraries and npm functions still have a place, but many functions once essential in ES3 are no longer needed.
- Examples cover arrays, objects, functions, and utility helpers that can now be done with plain JavaScript.
