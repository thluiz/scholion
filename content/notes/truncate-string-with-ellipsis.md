---
title: "Truncate string with ellipsis"
date: '2026-11-16T01:55:23+00:00'
category: webclip
summary: 'The page shows how to truncate long one-line text with CSS using width, white-space, overflow, and text-overflow, and how to expose the full string with the title attribute.'
tags: ["css", "text-overflow", "overflow", "white-space"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Truncate string with ellipsis"
    url: "https://dev.to/ip127001/truncate-string-with-ellipsis-26l5"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/dev-to--truncate-string-with-ellipsis.md"
    kind: repo
---

The page explains how to adjust long strings in one line and show ellipsis at the end. It uses CSS properties together, and suggests the title attribute to show the full string on hover.

## Reading notes

- text-overflow is used to show how hidden content appears when text is clipped
- white-space: nowrap keeps the text from wrapping
- overflow: hidden clips content inside a fixed width
- width sets the space available for the content
- title can show the full long string when the element is hovered
- in an input element, text-overflow: ellipsis can be used directly
