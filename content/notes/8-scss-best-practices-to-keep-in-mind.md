---
title: "8 SCSS Best Practices to Keep in Mind"
date: '2026-11-16T00:27:35+00:00'
category: webclip
summary: 'The post gathers eight SCSS guidelines that aim to make styles easier to read, maintain, and scale, from mobile-first structure and variables to naming, comments, and media query placement.'
tags: ["scss", "css", "best-practices"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "8 SCSS Best Practices to Keep in Mind"
    url: "https://dev.to/liaowow/8-css-best-practices-to-keep-in-mind-4n5h"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/dev-to--8-scss-best-practices-to-keep-in-mind.md"
    kind: repo
---

The post presents eight SCSS guidelines taken from a company coding guideline and frames them as useful for both collaborative work and personal projects. It focuses on writing CSS that stays readable, maintainable, and easier to scale.

## Reading notes

- Mobile-first styling is preferred so responsive design starts from mobile and expands upward with `min-width` media queries.
- Variables and mixins should be set early, especially for values like border radius, colors, fonts, margins, and transition timing.
- `#id` selectors and `!important` are treated as overly specific and discouraged because they can complicate CSS order in collaborative work.
- Magic numbers should be avoided in favor of relative values that explain why a number is needed.
- Selector names should describe hierarchy or purpose rather than only visual appearance.
- Zero values should follow the project’s consistency rules, including units for zero-duration times, no units for zero-length values, and a leading zero for decimals.
- Comments should be placed above the property they describe, and inline `//` comments are preferred over block comments.
- Media queries should stay at the root of the declaration instead of being nested inside each selector, so they are easier to find.
