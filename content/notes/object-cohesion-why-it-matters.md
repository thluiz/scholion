---
title: "Object Cohesion: Why It Matters"
date: '2026-11-16T02:21:31+00:00'
category: webclip
summary: 'The post argues that cohesion can be measured empirically and used to test Elegant Objects claims. With jPeek, the author compares Java classes and says features like static methods, mutability, annotations, and DTOs tend to correlate with lower cohesion.'
tags: ["object-cohesion", "java", "elegant-objects", "jpeek"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Object Cohesion: Why It Matters"
    url: "https://yegor256.com/2020/02/11/object-cohesion.html"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/yegor256-com--object-cohesion-why-it-matters.md"
    kind: repo
---

Object cohesion is presented as a measurable property of software modules that can support the claims of Elegant Objects. The post argues that if classes with certain features consistently show lower cohesion, those claims gain empirical backing.

## Reading notes

- The author says cohesion can help EO adepts prove some of their assumptions.
- A class is low in cohesion when its attributes and methods are unrelated and can be split without loss.
- A highly cohesive class cannot be broken into smaller pieces because its attributes and methods belong together.
- The post cites earlier research saying more cohesive classes tend to be less error-prone.
- The author proposes comparing random Java classes with and without static methods and checking which group has higher average cohesion.
- The post presents jPeek as an open source tool for calculating cohesion metrics in Java code.
- It says many cohesion metrics have been published, but only a few were properly implemented.
- The author says jPeek can be used to test EO claims about mutable classes, annotations, and DTOs.
