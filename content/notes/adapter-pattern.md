---
title: Adapter Pattern
date: '2026-04-04T08:21:50+01:00'
summary: '"Convert the interface of a class into another interface clients expect."'
tags:
- software-engineering
- design-patterns
- gang-of-four
has_commentary: false
sources:
- title: Adapter pattern — Wikipedia
  url: https://en.wikipedia.org/wiki/Adapter_pattern
  kind: wiki
---

"Convert the interface of a class into another interface clients expect."

The Adapter pattern (GoF, 1994), also known as Wrapper, allows incompatible interfaces to work together. It wraps an existing class with a new interface so that it becomes compatible with what the client code expects — without modifying the original source code.

A real-world analogy: a power plug adapter lets a European device plug into a British socket. The device and the socket don't change — the adapter bridges the gap.
