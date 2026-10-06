---
title: "Create a transparent TabbedBar for Titanium Mobile"
date: '2012-06-11T14:14:26-03:00'
category: webclip
summary: 'The snippet builds a semi-transparent Titanium Mobile TabbedBar by layering a bar background, an empty TabbedBar, and visible labels inside one reusable view.'
tags: ["titanium-mobile", "javascript", "ios", "tabbed-bar"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Create a transparent TabbedBar for Titanium Mobile - JavaScript - Snipplr Social Snippet Repository"
    url: "http://snipplr.com/view/54338/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2012-06/snipplr-com--create-transparent-tabbedbar-for-titanium-mobile.md"
    kind: repo
---

The snippet creates a reusable Titanium Mobile view that combines a background layer, a semi-transparent iOS TabbedBar with empty button labels, and a text overlay placed on top. The result is a transparent tabbed bar that can be added to another view or window.

## Reading notes

- It wraps all parts in one view so the component can be reused elsewhere.
- The background color of the bar should match a color from the view's background image.
- The TabbedBar uses empty labels, while a separate overlay supplies the visible button text.
- The overlay labels are centered, bold, white, and given a black shadow.
- The function accepts backgroundColor, buttonNames, height, and opacity properties.
- If opacity is not provided, it defaults to 0.4.
- The example creates a window, builds the transparent tabbed bar with three buttons, adds it to the window, and opens the window.
