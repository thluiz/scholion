---
title: "The Simplest Case for Unit Tests: Pure Functions"
date: '2022-08-04T09:07:05-03:00'
category: webclip
summary: 'Pure functions are easy to cover with unit tests because their output depends only on inputs. The article shows how tests expose edge cases in strings, money calculations, and math operations.'
tags: ["unit-tests", "pure-functions", "edge-cases", "javascript"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "The Simplest Case for Unit Tests: Pure Functions"
    url: "https://how-to.dev/the-simplest-case-for-unit-tests-pure-functions"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2022-08/how-to-dev--the-simplest-case-for-unit-tests-pure-functions.md"
    kind: repo
---

Pure functions are the clearest place to start with unit tests because their results depend only on arguments. The article uses simple JavaScript examples to show how tests make behavior explicit, expose edge cases, and encourage more careful thinking about inputs and outputs.

## Reading notes

- Unit tests check small pieces of code against explicit expectations and give automatic feedback while working on a codebase.
- Pure functions depend only on their arguments, keep no internal state, and do not read external values besides those arguments.
- A greeting function can be tested by checking the full returned string for a given name and surname.
- Tests also surface edge cases, such as calling the greeting function with only one argument or with missing name parts, which may require changing the implementation.
- Discount calculations can fail because of floating-point rounding in JavaScript, especially when dealing with money.
- Rounding the result to two decimal places can fix cases where the raw number is slightly off or has more decimal places than needed.
- Even mathematical functions can need tests for unexpected inputs, such as missing arguments, strings, or objects.
- For those invalid inputs, the article suggests deciding whether to return NaN, throw an error, or fall back to a default value, and making that choice explicit in tests.
- The article concludes that pure functions are the most straightforward functions to cover with unit tests and that writing those tests trains a precise way of thinking.
