---
title: "5 ways to center a div vertically and horizontally using CSS"
date: '2020-07-05T14:10:38+00:00'
category: webclip
summary: 'The article collects five CSS ways to center a div both horizontally and vertically, comparing Flexbox, Grid, positioning, margin, and table-based layouts, plus a bonus table approach.'
tags: ["css", "layout", "flexbox", "grid"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "5 ways to center a div vertically and horizontally using CSS"
    url: "https://dev.to/ruphaa/5-ways-to-center-a-div-vertically-and-horizontally-using-css-3i60"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/dev-to--5-ways-to-center-a-div-vertically-and-horizontally-using-css.md"
    kind: repo
---

The article gathers several CSS techniques for centering a div on a page. It frames the task as a common one and points to different layout tools that can place an element in the middle both horizontally and vertically.

## Reading notes

- Flex can center the child by setting the parent to `display: flex` and using `justify-content: center` with `align-items: center`, with fixed width and height on the parent.
- Grid can center content with `display: grid` and `place-items: center` on the parent.
- Grid can also center through the child by setting `display: grid` on the parent and using `align-self: center` and `justify-self: center` on the child.
- A positioning approach sets the child to `position: absolute` and moves it to 50% from the top and left of the parent.
- A margin approach uses `margin: 0 auto` on the child, though the author notes that this can be inconsistent and may need extra properties.
- Another positioning method sets the child to `position: absolute`, uses `top`, `left`, `right`, and `bottom` as `0`, and adds `margin: auto`.
- The note on `inset` says it is shorthand for `top`, `left`, `right`, and `bottom`, and mentions Firefox support.
- A bonus method uses CSS table layouts by setting `display: table` on a wrapper and `display: table-cell` on the parent.
- In the table approach, the child can be centered either with `margin` or with `display: inline-block`.
