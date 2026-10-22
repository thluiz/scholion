---
title: "How to Make an Awesome Horizontal Parallax Animation"
date: '2020-11-25T05:03:49-03:00'
category: webclip
summary: 'The article explains how parallax depth comes from differences in scale and speed, then shows how to build a horizontal scene by separating foreground, midground, and background and animating each layer differently.'
tags: ["parallax", "css-animation", "transform", "svg"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "How to Make an Awesome Horizontal Parallax Animation - DEV Community 👩‍💻👨‍💻"
    url: "https://dev.to/robole/how-to-make-an-awesome-horizontal-parallax-animation-3o6a"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2020-11/dev-to--how-to-make-an-awesome-horizontal-parallax-animation.md"
    kind: repo
---

The article explains the parallax effect as a way to create a stronger sense of depth in motion, using a train scene to show how nearby elements should move faster and distant ones slower. It breaks the scene into foreground, midground, and background, then animates each layer with different offsets or durations to create the effect.

It also compares PNG layers with inline SVG. SVG avoids extra image requests, scales better, and works well for a repeating animation when the first and last frames stay very similar. The article recommends animating with `transform` instead of `left` for better performance.

## Reading notes

- Parallax increases perceived depth and is used for slick scrolling animations.
- The visual cue for depth depends on scale, light, and speed.
- In motion, nearer elements should move faster and farther ones slower.
- The train example adapts a CodePen scene into a layered animation.
- The scene is grouped into foreground, midground, and background.
- Each group can be exported as a separate PNG or combined in one SVG with grouped elements.
- The image should be prepared with the scale already baked in so the animation only needs horizontal movement.
- The viewport must always show a complete frame for the foreground and background.
- Using widths that are multiples of the viewport makes the animation easier to adjust.
- A looping animation needs a first frame and a last frame that are very similar.
- The HTML uses one container and three layered child divs.
- The layers are stacked with absolute positioning and clipped with overflow hidden.
- The initial scene is built with horizontal `transform: translateX(...)` offsets.
- Layer speed can be controlled by different distances or by different animation durations.
- The article recommends `transform` over `left` for better animation performance.
- Inline SVG reduces requests and stays responsive when resized.
- For an infinite loop, the SVG design keeps the first and last frames almost identical.
- A warning is given about combined SVG and CSS transforms affecting positioning.
