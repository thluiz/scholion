---
title: "Builders and Manipulators"
date: '2020-02-22T12:12:01+00:00'
category: webclip
summary: 'The article proposes a naming rule for OOP methods: builders return an object and should be nouns, while manipulators change state and should be verbs that return void.'
tags: ["oop", "method-naming", "queries-and-commands"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Builders and Manipulators"
    url: "https://yegor256.com/2018/08/22/builders-and-manipulators.html"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/yegor256-com--builders-and-manipulators.md"
    kind: repo
---

The article argues for a strict split in OOP method names. If a method returns a value, it should be a noun that names what it returns. If it changes state, it should be a verb and return void. The point is to keep queries and commands separate and make the code easier to understand.

## Reading notes

- Builders create or find an object and return it.
- A builder name should describe the returned result, so `book()` is preferred over `find()`, `getTitle()`, or `calculateSpeed()`.
- Builders should not modify the encapsulated entities and should have no side effects.
- Manipulators change the entities the object encapsulates.
- Manipulators should return `void`, as in `add(Book book)` or `save()`.
- The rule aims to separate declarative code from imperative code.
- Following the rule is said to make methods smaller, names shorter, and design simpler.
- The author links the idea to Bertrand Meyer’s distinction between queries and commands.
- The author rejects the noun/verb naming principle because it does not separate builders from manipulators.
