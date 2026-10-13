---
title: "Introducing Transproc - functional data transformations for Ruby"
date: '2015-04-20T09:18:02-03:00'
category: webclip
summary: 'The post presents Transproc as ROM’s data-transformation backend, built around stateless functions that compose left to right. It argues this fits data pipelines better than typical OO Ruby for handling hashes and nested transformations.'
tags: ["ruby", "data-transformation", "rom", "functional-programming"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "solnic.eu - Introducing Transproc - functional data transformations for Ruby"
    url: "http://solnic.eu/2015/04/16/introducing-transproc-functional-data-transformations-for-ruby.html"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-04/solnic-eu--introducing-transproc-functional-data-transformations-for-ru.md"
    kind: repo
---

The post introduces Transproc as a backend for data transformations in ROM. It says Transproc treats transformations as stateless functions that compose left to right, so data can move through a pipeline without needing to refer to the data object directly.

It contrasts this with typical OO Ruby approaches, which it says are awkward for data processing, often relying on monkey patches or more complex abstractions. It also says custom transformations are easy to add by naming a proc or defining a module, and invites readers to try it and report missing transformations.

## Reading notes

- Transproc is presented as ROM’s first data transformation backend.
- Its core properties are stateless transformation functions and left-to-right composition.
- The post says this approach makes it easier to encapsulate transformations in a pipeline.
- It criticizes idiomatic OO Ruby for data transformation, especially monkey patches and manual hash mutation.
- It shows composing transformations with `>>` or `+`.
- It says custom transformation functions can be added by providing a name and a proc.
- It mentions creating a module with custom transformations.
- It encourages readers to check the docs and report missing transformations.
