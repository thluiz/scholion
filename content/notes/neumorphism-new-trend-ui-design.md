---
title: "Neumorphic design: What it is and how to use it effectively"
date: "2026-09-23T19:22:29+01:00"
category: webclip
has_commentary: false
summary: "Traces neumorphism from skeuomorphism and flat design, its three defining principles, and the accessibility trade-off that comes with its low-contrast look."
tags:
  - ui-design
  - neumorphism
  - accessibility
sources:
  - title: "Neumorphic design: What it is and how to use it effectively - LogRocket Blog"
    url: "https://blog.logrocket.com/ux-design/neumorphism-new-trend-ui-design/?ref=dailydev"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/blog-logrocket-com--neumorphism-new-trend-ui-design.md"
    kind: repo
---

Allie Paschal places neumorphism as the third step in a design lineage: skeuomorphism imitated physical objects (a trash can icon, a notepad texture) to make early digital interfaces feel familiar, then flat design stripped all of that away for speed and usability, then neumorphism, arriving around 2019, brought back just enough shadow and gradient to restore a sense of depth without reintroducing skeuomorphism's clutter. Buttons and cards in a neumorphic interface look like they're rising or sinking into the background rather than sitting flat on top of it.

Three principles define the look. A near-monochrome palette built on off-white or off-black rather than pure white or black, so shadows and gradients read clearly against it. Soft, diffused shadows and highlights that all share one consistent light-source direction, so an element lit from the top-left always casts its shadow toward the bottom-right. And uniformly high corner radii across every component, since a sharp corner would reintroduce the contrast the style is built to avoid.

## Fichamento

- The trade-off is direct: the low contrast that makes neumorphism look soft is the same low contrast that tends to fail WCAG's three-to-one color contrast requirement for non-decorative elements, and can make interactive components indistinguishable from the background they sit on.
- A gray border on a low-contrast element is offered as a minimal fix that preserves the neumorphic look while meeting contrast requirements.
- Real products cited as using partial neumorphism rather than a full commitment to it: Momentum Dash (monochrome palette with a lime-green accent, shadows, rounded corners), Bose's music app (grayscale palette, shadow on the active/selected component), and an older Tesla app (dark, monochromatic, but explicitly without the shadows and highlights that would make it fully neumorphic).
- The piece places neumorphism alongside three sibling trends from the same flat-design lineage: glassmorphism (translucent, blurred "frosted glass" panels, popularized by macOS Big Sur in 2020), neubrutalism (bold colors, hard outlines, popularized around 2022, exemplified by Figma's own site), and dark mode (trending since roughly 2017, adopted exclusively by Netflix, Hulu, and Max).
- Multiple layered drop shadows and gradients are named as a performance cost, not just a visual one, since they add render time that matters more on mobile devices or low-bandwidth connections.
