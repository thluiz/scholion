---
title: "CSS-Only Full-Width Responsive Images 2 Ways"
date: '2026-11-16T19:40:51+00:00'
category: webclip
summary: 'The post compares two CSS ways to make full-width responsive images: `background-size: cover` for background containers and `object-fit: cover` for `img` elements, with notes on support and use cases.'
tags: ["css", "responsive-images", "background-size", "object-fit"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "CSS-Only Full-Width Responsive Images 2 Ways"
    url: "https://dev.to/5t3ph/css-only-full-width-responsive-images-2-ways-2njm"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/dev-to--css-only-full-width-responsive-images-2-ways.md"
    kind: repo
---

The post compares two ways to build full-width responsive images with CSS. One uses `background-size: cover` on a container with a background image and a set aspect ratio. The other uses `object-fit: cover` on a standard `img`, with height used to constrain the image.

## Reading notes

- `background-size: cover` is presented as the older option, widely used before broad support for newer CSS image handling.
- The background-image version places the image in the element's style attribute and uses `aria-label` in place of `alt`.
- The container uses `padding-bottom` to create a 16:9 ratio.
- `object-fit: cover` is described as the newer option and is not available for older IE versions without a polyfill.
- The `img` version keeps standard image semantics and uses `alt` instead of `aria-label`.
- The `img` is constrained with `height`, and `object-fit: cover` centers and crops it within the container.
- Use `background-size` when the image is decorative, when the container needs extra content, or when pseudo-elements and other background effects are needed.
- Use `object-fit` when a normal `img` fits the context and its semantics should be preserved.
