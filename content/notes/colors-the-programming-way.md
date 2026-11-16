---
title: "Colors, the Programming Way"
date: '2020-04-20T21:22:38+00:00'
category: webclip
summary: 'The article explains how to choose workable color schemes by using hue, saturation, and lightness instead of RGB, then checks contrast and color-blind accessibility before applying the result.'
tags: ["color-schemes", "hue", "contrast", "accessibility"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Colors, the Programming Way"
    url: "https://dev.to/jcolag/colors-the-programming-way-5bf2"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/dev-to--colors-the-programming-way.md"
    kind: repo
---

The article argues that RGB is a poor model for choosing related colors, because it reflects display hardware more than how people perceive color. It suggests working in terms of hue, saturation, and lightness, then using geometry on the color wheel to build adjacent, complementary, triadic, and tetradic schemes.

It also recommends checking contrast with WCAG-style luminance calculations and testing schemes against several kinds of color blindness by applying matrices to each color channel. The same approach can be automated, but the author still recommends visual inspection and, in existing work, following a company’s branding guidelines.

## Reading notes

- RGB is useful for displays, but it makes relationships between colors hard to see.
- Hue, saturation, and lightness give a more intuitive way to describe colors.
- Adjacent, complementary, triadic, and tetradic schemes come from angles on the hue circle.
- A closest named color can be found by comparing an input color against a list of named colors in HSL or HSV space.
- Contrast can be calculated from luminance values and used to check whether colors are readable together.
- Color schemes should also be tested against multiple kinds of color blindness.
- The process can be automated, but the result still needs visual inspection.
- For existing company work, branding guidelines should take priority over new color choices.
