---
title: "The Codeless Code: Case 15 Immutable"
date: '2020-04-19T06:29:13+00:00'
category: webclip
summary: 'A novice learns why Strings are immutable, then overgeneralizes the lesson and makes every class immutable, forcing large constructors and awkward object creation.'
tags: ["java", "immutability", "object-design"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "The Codeless Code: Case 15 Immutable"
    url: "http://thecodelesscode.com/case/15"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/thecodelesscode-com--the-codeless-code-case-15-immutable.md"
    kind: repo
---

A novice from the Temple of Three Stones asks why Java Strings are immutable, since converting a field to mixed case seems to require extra objects and copied characters. A sister answers with a comparison between a brass coin and an egg, and he takes the lesson to heart.

He then makes all his classes immutable, so every change requires a new instance. The result is that his constructors become very large and complex, and the Java master assigns the nun to correct him.

## Reading notes

- The novice is new to Java and is bothered by the cost of changing a String.
- The sister explains immutability through the contrast between something that can be exchanged again and something that cannot.
- He applies immutability to all classes, not only Strings.
- This choice makes constructors large and complex.
- The master responds by having the nun correct the novice.
