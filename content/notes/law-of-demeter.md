---
title: Law of Demeter
date: '2026-04-04T08:13:31+01:00'
summary: '"Only talk to your immediate friends; don''t talk to strangers."'
tags:
- software-engineering
- object-oriented
- design-principles
has_commentary: true
sources:
- title: Law of Demeter — Wikipedia
  url: https://en.wikipedia.org/wiki/Law_of_Demeter
  kind: wiki
---

"Only talk to your immediate friends; don't talk to strangers."

The Law of Demeter (LoD), also known as the principle of least knowledge, was proposed by Ian Holland at Northeastern University in 1987. It states that a given object should assume as little as possible about the structure of other objects, including its subcomponents.

In practice, for languages that use dot notation, it can be summarized as "use only one dot": `a.m()` is fine, `a.m().n()` is not. The chain `A.B.C.Name` violates the law — your object shouldn't need to know about the internal structure of objects two or three levels deep.

The advantage is more maintainable and adaptable software — since objects are less dependent on the internal structure of others, implementations can change without breaking callers. The tradeoff is that it may require writing wrapper methods to propagate calls, adding some verbosity.
