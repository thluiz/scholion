---
title: "Stranger Things, JavaScript Edition"
date: '2020-06-04T19:45:25-03:00'
category: webclip
summary: 'The post explains several surprising JavaScript behaviors, including map with parseInt, string coercion that produces ''banana'', truthy and falsy values, loose array equality, and arithmetic coercion rules.'
tags: ["javascript", "type-coercion", "equality", "truthy-falsy"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Stranger Things, JavaScript Edition"
    url: "https://livecodestream.dev/post/2020-06-03-stranger-things-javascript-edition/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2020-06/livecodestream-dev--stranger-things-javascript-edition.md"
    kind: repo
---

The post walks through a set of JavaScript expressions that produce unexpected results and explains them by pointing to how the language handles callback arguments, coercion, equality, and arithmetic. It shows that the odd outputs are not random, but follow JavaScript’s built-in rules.

## Reading notes

- `['1', '7', '11'].map(parseInt)` returns `[1, NaN, 3]` because `map()` passes the value, the index, and the array to the callback, and `parseInt()` treats the index as the radix.
- The expected result can be restored by passing only the current value to `parseInt`.
- The expression `('b'+'a'+ + 'a' + 'a').toLowerCase()` becomes `banana` because `+ 'a'` produces `NaN`, which is then concatenated into the string.
- The `fail` example is built from expressions that produce `false` and `falseundefined`, then selects letters from those strings.
- JavaScript uses truthy and falsy values when a boolean is needed, and falsy values listed in the post are `0`, `-0`, `0n`, empty strings, `null`, `undefined`, and `NaN`.
- Loose equality on arrays can return `true` in many cases because JS applies coercion, such as `[] == ''`, `[] == 0`, and nested arrays compared to `0` or `''`.
- In arithmetic, subtraction and addition can behave differently with strings, numbers, arrays, and objects because JS applies coercion rules before evaluating the operation.
- `{} + []` is treated differently from `[] + {}` when written without parentheses because the first form is parsed as a code block followed by unary plus.
