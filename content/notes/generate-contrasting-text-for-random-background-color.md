---
title: "Generate Contrasting Text For Your Random Background Color"
date: '2020-02-22T12:12:01+00:00'
category: webclip
summary: 'The article shows how to choose black or white text for a user-selected background by converting hex colors to RGB, calculating YIQ brightness, and applying a threshold in JavaScript.'
tags: ["javascript", "color-contrast", "web-components"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Generate Contrasting Text For Your Random Background Color"
    url: "https://web.archive.org/web/20191224090229id_/https://dev.to/daviddalbusco/generate-contrasting-text-for-your-random-background-color-g0m"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/web-archive-org--generate-contrasting-text-for-random-background-color.md"
    kind: repo
---

The article explains a simple way to keep text readable on a user-chosen background color. It converts a hexadecimal color to RGB, then uses the W3C YIQ brightness formula to decide whether the contrasting text should be black or white.

It also shows a Vanilla JavaScript demo with a color picker, where the selected hex value updates the page background and the text color. The implementation reuses an open-source color component from DeckDeckGo and notes that the component can be used in modern frameworks or plain JavaScript.

## Reading notes

- The project needs a way to show contrasted text because users can assign their own background colors.
- The solution is based on the Ionic Color Generator implementation.
- The code includes a hex-to-RGB conversion.
- The contrast calculation uses the W3C YIQ brightness formula.
- The brightness result is compared with a threshold to return either black or white text.
- The demo uses a color picker in an HTML page.
- The selected color is applied to the page background and to the text color.
- The `@deckdeckgo/color` web component is open source.
- The component works in Vanilla JavaScript and modern frameworks.
- The component is described as lightweight according to Bundlephobia.
