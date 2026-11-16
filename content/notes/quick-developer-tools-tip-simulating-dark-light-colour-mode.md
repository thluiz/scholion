---
title: "Quick developer tools tip: simulating dark/light colour mode"
date: '2020-02-22T12:11:49+00:00'
category: webclip
summary: 'The post shows how to use browser developer tools to emulate dark mode, light mode, reduced motion, and high contrast so products can be tested without changing the whole OS.'
tags: ["developer-tools", "dark-mode", "accessibility"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Quick developer tools tip: simulating dark/light colour mode"
    url: "https://christianheilmann.com/2020/01/30/quick-developer-tools-tip-simulating-dark-light-colour-mode"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/christianheilmann-com--quick-developer-tools-tip-simulating-dark-light-colour-mode.md"
    kind: repo
---

The post explains that newer operating systems include dark/light mode, prefers-reduced-motion, and high contrast mode, and that products should be tested in those settings to catch obvious problems. It says browser developer tools include simulators for these modes, so you do not need to change the entire operating system.

## Reading notes

- Newer operating systems offer dark/light mode and prefers-reduced-motion, and products should be tested in those modes.
- Windows high contrast mode is an accessibility feature that should also be tested.
- In Microsoft Edge, the simulator is under More tools, then Rendering, then Emulate CSS media feature prefers-color-scheme.
- The same can be reached with Ctrl/Cmd + Shift + P by typing dark or light and choosing the rendering options, not the devtools theme.
- The functionality is available in any Chromium-based browser.
- The author says the controls are hidden and asks readers to report issues through the devtools feedback tool or contact them on Twitter.
