---
title: "Design Patterns Are Temporary, Language Features Are Forever"
date: '2026-09-25T20:16:10+01:00'
category: webclip
summary: 'The post argues that visitor starts to make more sense once you know pattern matching, and that newer Java features like sealed types and switch pattern matching can replace some old OO patterns.'
tags: ["design-patterns", "java", "pattern-matching", "visitor-pattern"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Design Patterns Are Temporary, Language Features Are Forever"
    url: "https://ptrtojoel.dev/posts/design-patterns-are-temporary/?ref=dailydev"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/ptrtojoel-dev--design-patterns-are-temporary-language-features-are-forever.md"
    kind: repo
---

The post treats design patterns as useful when they make a problem easier, but also easy to overuse or learn through weak examples. The author says visitor was hard to grasp until learning pattern matching in Rust, and then seeing it as an OO way to do something similar.

With Java 21, sealed types and switch pattern matching make the language feel closer to that style of direct data matching. In the filesystem example, the visitor version works, but the newer Java version feels shorter and clearer, with the logic focused more on the data than on OO indirection.

## Reading notes

- Design patterns can help with real problems, but they are also often overused or explained with unrealistic examples.
- Visitor was hard to understand before the author learned pattern matching in Rust.
- Pattern matching made visitor feel like an OO version of matching on data.
- Java 21 adds sealed types and pattern matching for switch, which the author sees as a strong improvement.
- The filesystem example shows visitor working for add and delete operations on tree nodes.
- The modern Java version is shorter and easier to follow, with logic centered on the data structure.
- Visitor still has drawbacks like indirection, double dispatch, and more visit methods for new use cases.
- The author now has more appreciation for visitor, even if newer language features feel like a better fit.
