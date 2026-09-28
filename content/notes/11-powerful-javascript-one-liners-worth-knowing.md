---
title: "11 Powerful JavaScript One-Liners Worth Knowing"
date: '2022-07-26T19:06:53-03:00'
category: webclip
summary: 'A set of 11 JavaScript one-liners for counting characters, checking empty objects, waiting, comparing dates, redirecting, handling touch support, DOM insertion, shuffling arrays, reading selected text, random booleans, and averaging arrays.'
tags: ["javascript", "one-liners", "dom", "arrays"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "11 Powerful JavaScript One-Liners Worth Knowing | by chao huang | Jul, 2022 | Bits and Pieces"
    url: "https://blog.bitsrc.io/javascript-shock-you-just-one-line-of-code-8a8587d7a07c"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2022-07/blog-bitsrc-io--11-powerful-javascript-one-liners-worth-knowing.md"
    kind: repo
---

The page collects 11 short JavaScript utilities and shows the single-line code for each one. The examples cover string counting, object emptiness, async waiting, date differences, redirects, touch support, DOM insertion, shuffling, selected text, random booleans, and array averages.

## Reading notes

- `characterCount` splits a string by a given character and uses the array length minus one.
- `isEmpty` checks that an object has no own keys and that its constructor is `Object`.
- `wait` creates a promise and resolves it with `setTimeout` after a given time.
- `daysBetween` converts the absolute difference between two dates from milliseconds into days.
- `redirect` sets `location.href` to send the browser to another URL.
- `touchSupported` checks whether the document supports `touchstart`.
- `insertHTMLAfter` uses `insertAdjacentHTML('afterend', html)` to place HTML after an element.
- `shuffle` uses `arr.sort(() => Math.random() > 0.5)` to randomize array order.
- `getSelectedText` returns the browser selection as a string.
- `getRandomBoolean` returns `true` or `false` with equal probability.
- `average` sums array values with `reduce` and divides by `arr.length`.
