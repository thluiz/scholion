---
title: "Constructors or Static Factory Methods?"
date: '2020-06-11T12:04:55-03:00'
category: webclip
summary: 'The page argues that static factory methods only look better when the design is already wrong. It favors constructors, polymorphism, and separate objects over static creation helpers.'
tags: ["static-factory-methods", "constructors", "object-oriented-design"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Constructors or Static Factory Methods?"
    url: "https://www.yegor256.com/2017/11/14/static-factory-methods.html"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2020-06/yegor256-com--constructors-or-static-factory-methods.md"
    kind: repo
---

The page argues against Joshua Bloch’s preference for static factory methods over constructors. It says their advantages, such as names, caching, and subtype selection, are workarounds for a design that should instead use polymorphism, encapsulation, or separate objects.

## Reading notes

- A constructor is presented as the natural way to create an object in object-oriented software.
- Named static factories are said to signal that the design should be split into more specific classes, such as `HexColor` and `RGBColor`.
- Caching through a static factory is treated as a storage concern that belongs in a separate object like `Palette`.
- Choosing a subtype from a static factory is described as taking decision-making away from the object itself.
- The preferred alternative is to keep the relevant logic inside the class or move management concerns to dedicated objects, not to static methods.
