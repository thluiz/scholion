---
title: "Eight CSS Tips for Advanced Layouts and Effects"
date: '2017-06-09T15:13:36-03:00'
category: webclip
summary: 'The article presents eight CSS techniques for advanced layouts and effects, showing how selectors, sizing rules, padding, tables, Flexbox, transforms, and filters can solve common front-end layout problems.'
tags: ["css", "layout", "flexbox", "css-filters"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Eight CSS Tips for Advanced Layouts and Effects"
    url: "https://www.toptal.com/front-end/eight-expert-css-tips"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2017-06/toptal-com--eight-css-tips-for-advanced-layouts-and-effects.md"
    kind: repo
---

The article collects eight CSS techniques for handling layout and visual effects with less reliance on extra scripting. It focuses on features such as sibling selectors, `box-sizing: border-box`, vertical padding for proportional height, `font-size` for proportional width, CSS tables, Flexbox, transforms, `border-radius`, and CSS filters.

## Reading notes

- Sibling selectors can replace some first/last-item logic and support patterns such as showing only active cards and the items after them.
- Setting `box-sizing: border-box` keeps element sizing consistent across browsers.
- Vertical padding can be used to give an element a height tied to its width, which also helps preserve video aspect ratios.
- `font-size` can serve as the basis for width and height when an element’s dimensions are expressed in `em`.
- Vertical centering of dynamic content can use `display: table` and `display: table-cell`, or Flexbox when browser support allows it.
- Same-height columns can be built with large negative `margin-bottom` values and matching `padding-bottom`, with CSS tables and Flexbox as alternatives.
- `transform: rotate(x)` and `border-radius` can turn boxy shapes into angled panes, circles, or ovals without altering the original content.
- CSS filters, including `invert` and `hue-rotate`, can create a night mode without a separate stylesheet.
