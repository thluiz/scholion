---
title: "ES2019 new features"
date: '2019-11-19T10:28:36+00:00'
category: webclip
summary: 'Overview of ES2019 additions to JavaScript, including Object.fromEntries, new string and array methods, Symbol description, optional catch binding, and safer JSON.stringify.'
tags: ["javascript", "ecmascript", "es2019"]
has_commentary: false
generated_by: "openai/gpt-5.1"
sources:
  - title: "ES2019 new features"
    url: "https://web.archive.org/web/20191119080207id_/https://dev.to/duomly/what-s-new-es2019-brings-48d7"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/web-archive-org--es2019-new-features-overview-object-flat-trim.md"
    kind: repo
---

The article presents the main ES2019 (ECMAScript 2019) features available in modern browsers like Chrome 72. It walks through new methods and language tweaks that simplify data conversion, string and array handling, working with Symbols, error handling, and JSON serialization.

## Reading notes

- ES2019 follows the regular ECMAScript release process, where proposals move through stages 0–4 and stage 4 means they are finalized.
- New Object.fromEntries() complements Object.entries() by turning an array of key–value pairs back into an object with a single method.
- The example shows Object.entries() converting a `car` object into an array, and Object.fromEntries() rebuilding the original object from that key–value array.
- New string methods trimStart() and trimEnd() remove whitespace from the beginning and end of a string, respectively, making front-end string manipulation easier.
- A code sample demonstrates that trimStart() leaves trailing spaces in place and trimEnd() leaves leading spaces in place.
- Array.prototype.flat() creates a new array by recursively concatenating elements of sub-arrays up to a given depth, which defaults to one.
- The example with nested arrays shows flat() with default depth 1, with depth 2, and with depth set to Infinity to fully flatten all nested levels.
- Array.prototype.flatMap() combines map() and flat() by applying a mapping function and then flattening the result one level in a single step.
- The provided flatMap() example adds 2 to each array item and shows the result as a flattened array of numbers.
- ES6 introduced Symbol, and ES2019 adds a direct description property on Symbol instances to make debugging easier without converting symbols to strings first.
- The Symbol example shows creating a symbol with a description string and then reading that description via the description property.
- Before ES2019, a catch clause in try…catch required a binding identifier even when the caught error value was unused, otherwise a SyntaxError occurred.
- ES2019 allows an optional catch binding so developers can write catch blocks without naming an error variable when they do not need it.
- JSON.stringify() in ES2019 is adjusted to avoid returning ill-formed Unicode strings by representing surrogate code points as escape sequences.
- When such JSON is parsed back with JSON.parse(), the surrogate code point sequences are restored to their original representation.
- The JSON.stringify() examples show how individual surrogate code units like `\uDF06\uD834` and `\uDEAD` are serialized as escaped sequences in the resulting JSON string.
- The conclusion lists the covered ES2019 features: Object.fromEntries(), trimStart() and trimEnd(), flat() and flatMap(), the Symbol description property, optional catch binding, and the updated JSON.stringify() behavior.
- The author suggests reading a previous article about useful JavaScript features since ES6 for readers who are unfamiliar with earlier ECMAScript updates.
