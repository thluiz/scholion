---
title: "Pure CSS Parallax Websites"
date: '2014-10-31T09:23:05-03:00'
category: webclip
summary: 'The article shows how CSS transforms, perspective, and scaling can create parallax scrolling without JavaScript, improving smoothness and letting the browser handle rendering more efficiently.'
tags: ["css-transforms", "parallax", "hardware-acceleration", "progressive-enhancement"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Pure CSS Parallax Websites"
    url: "http://keithclark.co.uk/articles/pure-css-parallax-websites/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2014-10/keithclark-co-uk--pure-css-parallax-websites.md"
    kind: repo
---

The article explains how to build a parallax scrolling site with CSS alone. It argues that moving the effect out of JavaScript avoids the reflows, paints, and frame drops caused by scroll handlers, while letting the browser handle more of the work through hardware acceleration.

## Reading notes

- The effect uses a container with `perspective` and `overflow-y: auto` so scrolling happens inside the element while descendants are rendered against a fixed 3D viewpoint.
- Layers are taken out of normal flow and assigned different `translateZ()` values to control scrolling speed.
- Because Z translation changes apparent size, the article adds `scale()` to correct the depth effect and keep layers at their original size.
- The amount of parallax depends on both `perspective` and the Z distance; more negative values scroll more slowly.
- For multi-section layouts, the article groups layers inside `parallax__group` elements with `transform-style: preserve-3d` and `height: 100vh`.
- Groups should not be clipped with `overflow: hidden`, because that breaks the effect.
- Debugging is easier when transforms are applied directly to the groups to make the 3D structure visible.
- Firefox, Safari, Opera, and Chrome support the effect, while IE does not support `preserve-3d` yet.
- The content should still work without parallax, following progressive enhancement.
