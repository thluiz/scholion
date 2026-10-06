---
title: "We're Doing It Wrong"
date: '2012-05-30T10:56:55-03:00'
category: webclip
summary: 'The page explains how Array#sort behaves across browsers, why stable sorting and locale-aware string comparison matter, and how mapping values first can reduce comparison cost.'
tags: ["javascript", "array-sort", "localecompare", "performance"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Sorting - We're Doing It Wrong | Rodney Rehm"
    url: "http://blog.rodneyrehm.de/archives/14-Sorting-Were-Doing-It-Wrong.html"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2012-05/blog-rodneyrehm-de--sorting-were-doing-it-wrong.md"
    kind: repo
---

The page argues that sorting in JavaScript is easy to use but easy to misuse. It shows that browser engines may use different algorithms, that stable sorting matters when the comparison returns the same value, and that comparing different data types or strings with plain `a > b ? 1 : -1` can produce inconsistent results.

It also describes ways to improve sorting of DOM elements and arrays by reducing repeated work in the comparison function, using `localeCompare` for strings, and mapping values before sorting. A detached-DOM approach is presented, but the benchmark in the text shows that it helps Chrome only and is skipped in the final plugin.

## Reading notes

- `Array#sort` depends on a callback for custom ordering, and ECMAScript expects stable sorting, but browser engines may use different algorithms.
- A sort is stable when equal items keep their relative order; the text contrasts stable engines with Chrome’s unstable QuickSort behavior.
- Comparing mixed types with the default pattern `a > b ? 1 : -1` can yield different results across browsers, especially with `NaN` and `Infinity`.
- For strings, plain Unicode comparison fails for many languages, including German umlauts and French accents.
- `String#localeCompare` is recommended for string sorting because it follows the user’s operating-system locale.
- Sorting DOM children with jQuery can be made faster by avoiding `append`, using direct `appendChild`, and reducing extra DOM work.
- A comparison function may run many times for the same element, so repeated text extraction and lowercasing can become expensive.
- Mapping each item to a reduced value before sorting cuts repeated evaluation and improves performance.
- Detaching DOM nodes before sorting can reduce reflows, but the benchmark in the text says the technique only benefits Chrome enough to justify skipping it.
