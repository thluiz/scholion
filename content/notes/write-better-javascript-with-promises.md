---
title: "Write Better JavaScript with Promises"
date: '2014-04-22T10:27:26-03:00'
category: webclip
summary: 'The article shows how promises make jQuery code easier to read, let APIs return values instead of callbacks, support chaining, and combine multiple requests with `when`.'
tags: ["javascript", "promises", "jquery", "async"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Write Better JavaScript with Promises"
    url: "http://davidwalsh.name/write-javascript-promises?utm_source=javascriptweekly&utm_medium=email"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2014-04/davidwalsh-name--write-better-javascript-with-promises.md"
    kind: repo
---

Promises make jQuery code easier to read because you can attach `done`, `fail`, and `always` handlers to the returned object, and the callbacks run in order. The article also shows that an API can return a promise instead of taking a handler, which makes it easier to pass the result around and transform it with `then`.

## Reading notes

- A callback example appends `data.text` to the page after a `getJSON` request succeeds.
- The promise version attaches `done` and `fail` handlers directly to the object returned by `getJSON`.
- jQuery also provides `always`, which runs whether the request succeeds or fails.
- The callback order is preserved, with `done` first, `fail` second, and `always` last.
- A wrapper around the HipsterJesus API can return a promise from `html` instead of accepting a handler.
- `then` can change the resolved value before passing it to the next handler in the chain.
- AngularJS once allowed templates to bind directly to promises, and the article says this feature was later deprecated.
- Promises can be chained to build small methods such as `html`, `paragraphs`, and `sentences`.
- Multiple API calls become simpler with `$.when`, which waits for both requests before running one handler.
