---
title: "10 New JavaScript Features in ES2020 That You Should Know"
date: '2026-11-16T19:35:36+00:00'
category: webclip
summary: 'The article presents the finalized ES2020 changes and explains features like BigInt, dynamic import, nullish coalescing, optional chaining, Promise.allSettled, globalThis, and module namespace exports.'
tags: ["javascript", "es2020", "programming", "ecmascript"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "10 New JavaScript Features in ES2020 That You Should Know"
    url: "https://www.freecodecamp.org/news/javascript-new-features-es2020/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/freecodecamp-org--10-new-javascript-features-in-es2020-that-you-should-know.md"
    kind: repo
---

The post says ES2020 is now finalized and gives a tour of the main changes in the JavaScript specification. It focuses on features for larger integers, cleaner module loading, safer property access, and more consistent behavior across runtimes.

## Reading notes

- BigInt lets JavaScript represent integers beyond the current `2^53 - 1` limit, and values use an `n` suffix to mark them as BigInts.
- Dynamic import lets applications load modules on demand, including conditional loading, without relying on bundlers like Webpack or Babel.
- Nullish coalescing checks only `undefined` and `null`, instead of all falsey values, so empty strings and `0` can still be kept.
- Optional chaining reads deeply nested properties, function calls, or array access without throwing when an intermediate value is missing.
- Promise.allSettled waits until every promise is settled, whether resolved or rejected.
- String#matchAll returns an iterator with all regex matches and captured groups.
- globalThis provides one global object name that works in browsers, Node, web workers, and other runtimes.
- Module namespace exports add symmetric syntax such as `export * as utils from './utils.mjs'`.
- The order of `for...in` loops is now formally defined in ES2020.
- `import.meta` gives module metadata, including a `url` property for the module base URL.
