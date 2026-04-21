---
title: Four Rules of Simple Design
date: '2026-04-04T08:15:26+01:00'
summary: 'Kent Beck formulated four rules of simple design while developing Extreme Programming in the late 1990s. A design is simple, in priority order, when it:'
tags: ["software-engineering", "design-principles", "extreme-programming"]
has_commentary: true
sources:
- title: Beck Design Rules — Martin Fowler
  url: https://martinfowler.com/bliki/BeckDesignRules.html
  kind: article
---

Kent Beck formulated four rules of simple design while developing Extreme Programming in the late 1990s. A design is simple, in priority order, when it:

1. **Passes the tests** — the software works as intended. Testing is a first-class activity, not an afterthought.
2. **Reveals intention** — the code is easy to understand. Readers can grasp the purpose behind each decision.
3. **No duplication** — every piece of knowledge has a single, unambiguous representation.
4. **Fewest elements** — minimize the number of classes, methods, and moving parts. Remove anything that doesn't serve the first three rules.

The order matters: passing tests comes first, then clarity, then removing duplication, and finally minimizing structure. Each rule only applies after the ones above it are satisfied.

The fourth rule is a corollary of [Occam's razor](/notes/occam-razor/) applied to software design: entities should not be multiplied beyond necessity.
