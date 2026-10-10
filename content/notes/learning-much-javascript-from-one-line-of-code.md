---
title: "Learning much javascript from one line of code"
date: '2014-10-12T11:34:20-03:00'
category: webclip
summary: 'The post breaks down a one-line snippet that outlines every page element in a random color, using it to explain selector APIs, array-like objects, outlines, and bitwise tricks.'
tags: ["javascript", "browser-console", "bitwise-operators"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Learning much javascript from one line of code - arqex"
    url: "http://arqex.com/939/learning-much-javascript-one-line-code?utm_source=javascriptweekly&utm_medium=email"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2014-10/arqex-com--learning-much-javascript-from-one-line-of-code.md"
    kind: repo
---

The post dissects a one-line JavaScript snippet shared by Addy Osmani that outlines every element on a page in a random color. It uses that example to show how browser-console selectors, array-like iteration, CSS outline, and number conversion work together.

## Reading notes

- The snippet is presented as a compact way to debug CSS layers by applying a 1 px outline with a random color to all page elements.
- `$$` is described as a browser console helper equivalent to `document.querySelectorAll`, and `document.all` is also mentioned as another way to select everything.
- The selected elements are treated as a `NodeList`, then iterated with `[].forEach.call` because `NodeList` does not implement every `Array` method.
- The text notes that using `for(i=0;A=$$('*');)` can make the code shorter, but it leaks global variables.
- `outline` is used because it does not affect element size or layout position.
- The color value is built from a random number converted to hexadecimal with `toString(16)`.
- `parseInt` is used to convert hexadecimal text to decimal, and `1<<24` is explained as `2^24`.
- The post explains that bitwise operations drop the decimal part of a float, so `~~` can act as a short way to get an integer result.
- It also mentions that `|0` can be used to discard the decimal part after the random number is produced.
- The closing section says programming requires a lot of accumulated knowledge and encourages readers who understood the one-liner, or who kept reading even if they did not.
