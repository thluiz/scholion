---
title: "Keeping it simple: coding a carousel"
date: '2015-04-16T17:25:58-03:00'
category: webclip
summary: 'The article argues for a carousel built with minimal HTML, CSS and JavaScript, using one active container class, one current item, and progressive enhancement instead of layered complexity.'
tags: ["carousel", "progressive-enhancement", "javascript", "css"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Keeping it simple: coding a carousel | Christian Heilmann"
    url: "http://christianheilmann.com/2015/04/08/keeping-it-simple-coding-a-carousel/?utm_source=BrazilJS+Weekly&utm_campaign=bb3ff78761-BrazilJS_Weekly_303_22_2013&utm_medium=email&utm_term=0_e6beed4270-bb3ff78761-64537241&ct=t(BrazilJS_Weekly_468_9_2013)"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-04/christianheilmann-com--keeping-it-simple-coding-a-carousel.md"
    kind: repo
---

The article argues that carousels should stay simple and work even when JavaScript is unavailable. It uses an ordered list as the core structure, adds a container class to activate the behavior, and keeps the visible state on a single current item.

## Reading notes

- A carousel can start as an ordered list inside a container.
- The basic CSS positions the box relatively and hides overflow so only one item is visible at a time.
- One class on the container activates the carousel behavior, and one class marks the current item.
- The JavaScript keeps state with a counter, updates the current element by moving the class, and uses buttons for navigation.
- The code relies on querySelector and classList, so it checks for support before proceeding.
- Transition, opacity, and transform can add visual polish without changing the core structure.
- pointer-events: none is used in the stacked version so hidden items do not capture links.
- The article closes by questioning whether every widget needs to be made generic and highly configurable.
