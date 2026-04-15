---
title: Proximate vs Ultimate Cause in Systems
date: '2026-04-07T19:45:31+01:00'
category: podcast
summary: 00:27:33 — Address Proximate Causes, Understand Ultimate Ones
tags:
- systems-thinking
- complex-systems
- developer-mindset
has_commentary: false
sources:
- title: Systems Thinking
  url: https://vox.thluiz.com/2022/06/W24/systems-thinking
  kind: podcast
---

**00:27:33** — Address Proximate Causes, Understand Ultimate Ones

In distributed systems, the root problem is often several applications away from where it manifests. It is tempting to fix things at the source, but the practical approach is to understand the ultimate cause while directly addressing the proximate cause, for example by rate-limiting or adding a queue. Fixing only at the source leads to whack-a-mole: you change one thing, which shifts load patterns, which breaks something else. In effect, you are moving emergent behavior around the system, making unpredictable situations appear even more unpredictably. System boundaries are abstract tools for thinking, not real walls.
