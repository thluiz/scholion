---
title: Proxy Pattern
date: '2026-04-04T08:24:50+01:00'
summary: '"Provide a surrogate or placeholder for another object to control access to it."'
tags:
- software-engineering
- design-patterns
- gang-of-four
has_commentary: false
sources:
- title: Proxy pattern — Wikipedia
  url: https://en.wikipedia.org/wiki/Proxy_pattern
  kind: wiki
---

"Provide a surrogate or placeholder for another object to control access to it."

The Proxy pattern (GoF, 1994) interposes a wrapper object between the client and the real object. The proxy implements the same interface as the real object, so the client doesn't know the difference.

Common variants: a virtual proxy delays expensive object creation until actually needed (lazy loading), a protection proxy controls access based on permissions, and a remote proxy represents an object in a different address space. The proxy can add caching, logging, or access checks without modifying the real object.
