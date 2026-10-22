---
title: "Styling scrollbars with CSS"
date: '2021-02-23T09:13:29-03:00'
category: webclip
summary: 'The page shows how to style scrollbars with CSS by combining the newer scrollbar-width and scrollbar-color properties with WebKit scrollbar pseudo-elements for wider browser support.'
tags: ["css", "scrollbar", "webkit"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Styling scrollbars with CSS"
    url: "https://h.daily-dev-tips.com/styling-scrollbars-with-css"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2021-02/h-daily-dev-tips-com--styling-scrollbars-with-css.md"
    kind: repo
---

The page explains that styled scrollbars are still uncommon, but they can improve a design. It recommends using both the newer scrollbar properties and the WebKit pseudo-elements so the result works in more browsers.

## Reading notes

- The article says scrollbars have traditionally been hard to style, but CSS now includes `scrollbar-color` and `scrollbar-width`.
- It defines CSS variables for scrollbar width, background color, and thumb color so the values can be reused.
- It uses `scrollbar-width` and `scrollbar-color` on the container as the newer scrollbar styling approach.
- It notes that Chrome support needs settings enabled, and Firefox needs `layout.css.scrollbar-color.enabled` set to `true`.
- It says `scrollbar-color` takes thumb color first and background second, and that `dark` and `light` are not supported by browsers yet.
- It uses `::-webkit-scrollbar` to set the width, `::-webkit-scrollbar-track` for the track background, and `::-webkit-scrollbar-thumb` for the thumb styling.
- It says the WebKit prefix is more widely supported, so combining it with the newer properties gives broader browser coverage.
