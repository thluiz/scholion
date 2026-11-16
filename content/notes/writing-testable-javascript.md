---
title: "Writing Testable JavaScript"
date: '2026-11-16T02:28:32+00:00'
category: webclip
summary: 'The article argues that unit testing becomes practical when JavaScript is split into small, testable pieces with clear responsibilities, simple methods, and configurable objects.'
tags: ["javascript", "unit-testing", "testable-code"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Writing Testable JavaScript"
    url: "https://alistapart.com/article/writing-testable-javascript"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/alistapart-com--writing-testable-javascript.md"
    kind: repo
---

The article argues that client-side code becomes easier to test when it is reorganized into separate objects for presentation, data, application state, and glue code. It contrasts integration tests with unit tests and shows that testable JavaScript reduces coupling and hidden state.

## Reading notes

- Integration tests check how an app behaves from the user’s point of view, while unit tests focus on a small piece of functionality and its input and output.
- Traditional procedural JavaScript is hard to unit test because responsibilities are mixed together, functions grow large, state is hidden in closures, and DOM access is tightly coupled to behavior.
- The article recommends separating code into distinct objects that do not need to know about one another, keeping methods short, supporting configurability, and using constructor functions.
- The Likes Box is refactored into a `Likes` object with an `.add()` method that removes the empty state and appends a liked name to the list.
- The Search Results piece is turned into a `SearchResults` object that can render results and trigger a `like` event on the document when a result is liked.
- The Search Data piece is turned into a `SearchData` object whose `fetch()` method returns a promise, resolves to an empty array for no query, and returns only the `results` property from the server response.
- The article suggests mocking server interaction in tests with Sinon rather than making real requests.
- The final application code wires together `SearchForm`, `SearchResults`, `Likes`, and `SearchData`, while the document acts as a message bus for search and like events.
- Testing is presented as a way to catch bugs earlier and make later refactoring and extension safer.
