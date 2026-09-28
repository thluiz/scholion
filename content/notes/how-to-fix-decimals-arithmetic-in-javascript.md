---
title: "How to fix decimals arithmetic in JavaScript"
date: '2022-04-27T15:34:18-03:00'
category: webclip
summary: 'Explains why decimal sums and subtractions can produce unexpected results in JavaScript, and shows two fixes: decimal libraries or scaling values before computing.'
tags: ["javascript", "decimal-arithmetic", "floating-point", "math"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "How to fix decimals arithmetic in JavaScript"
    url: "https://flaviocopes.com/javascript-decimal-arithmetics/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2022-04/flaviocopes-com--how-to-fix-decimals-arithmetic-in-javascript.md"
    kind: repo
---

JavaScript can return unexpected results when adding or subtracting decimal numbers, such as `0.1 + 0.2` becoming `0.30000000000000004` or `1.4 - 1` becoming `0.3999999999999999`. The page says this is not unique to JavaScript, because computers store data in binary and some decimal values cannot be represented exactly.

It suggests using libraries such as `decimal.js`, `bignumber.js`, or `big.js`. It also shows a workaround that multiplies values by a power of 10, performs the calculation, and divides back, including a reusable `sum(a, b, positions)` function.

## Reading notes

- Decimal arithmetic can produce long repeating results instead of the expected rounded value.
- The problem comes from binary storage and the limited precision of decimal values in that format.
- Libraries like `decimal.js`, `bignumber.js`, and `big.js` are listed as options.
- A workaround is to scale numbers by a factor such as 100, compute the sum, and then divide again.
- The example function uses `toFixed(positions)` and `Math.pow(10, positions)` to handle a chosen number of decimal places.
