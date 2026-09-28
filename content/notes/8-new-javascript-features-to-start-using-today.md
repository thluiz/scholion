---
title: "8 new JavaScript features to start using today"
date: '2022-07-07T17:15:37-03:00'
category: webclip
summary: 'The article reviews eight ECMAScript 2022 features, including class fields, regexp match indices, top-level await, negative indexing with .at(), hasOwn, static blocks, and Error cause.'
tags: ["javascript", "ecmascript-2022", "class-fields", "regexp"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "8 new JavaScript features to start using today | InfoWorld"
    url: "https://www.infoworld.com/article/3665748/8-new-javascript-features-to-start-using-today.html#tk.rss_all"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2022-07/infoworld-com--8-new-javascript-features-to-start-using-today.md"
    kind: repo
---

ECMAScript 2022 adds eight JavaScript features the article presents as usable now. It groups them around class fields, regular expressions, module loading, object property checks, array indexing, static initialization, and error chaining.

## Reading notes

- Public and private instance fields can be declared in the class body instead of only in the constructor.
- Private instance methods and accessors also use the hash prefix and have the same visibility rules as private fields.
- Static members belong to the class, not to instances, and can also be private.
- RegExp match indices are available when the `/d` flag is used, and `exec` results then include start and end positions for matches and named groups.
- Top-level await lets a module wait on dependent asynchronous work before the importing module runs.
- Ergonomic brand checks let code test for a private field with `#fieldName in object`.
- `.at()` supports negative indices on built-in indexable values.
- `Object.hasOwn` works as a static alternative to `hasOwnProperty`, including cases such as objects created with `Object.create(null)`.
- Static class blocks run when the class is loaded and can initialize static values.
- `Error` now accepts a `cause` option for chained error information.
