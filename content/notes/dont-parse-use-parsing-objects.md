---
title: "Don't Parse, Use Parsing Objects"
date: '2020-02-22T12:11:52+00:00'
category: webclip
summary: 'The article argues that deserialization should move from DTO-based parsing into objects like JsonBook or RqUser, so HTTP handling, validation, and parsing stay reusable and less procedural.'
tags: ["parsing-objects", "deserialization", "object-oriented-design"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Don't Parse, Use Parsing Objects"
    url: "https://yegor256.com/2018/02/27/parsing-objects.html"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/yegor256-com--dont-parse-use-parsing-objects.md"
    kind: repo
---

The article argues that deserialization should be handled by objects rather than by DTOs that are parsed in an entry point. In the example, the library receives a JSON request for a book, and the parsing logic is moved into a `JsonBook` object that implements `Book`.

## Reading notes

- The traditional DTO approach serializes objects to JSON on the way out and deserializes them on the way back, but the article says this is the wrong pattern.
- Serialization should be replaced by printers, and deserialization should be done by objects.
- In the first example, the HTTP entry point reads multipart form data, parses JSON, creates a `BookDTO`, sets the ISBN, and calls `library.register(book)`.
- That approach is not reusable, because the same HTTP processing and JSON parsing would need to be rewritten elsewhere.
- Error handling and validation are not reusable there either, so adding them to that method would force duplication.
- The code is also procedural and has temporal coupling between method calls.
- A better design hides parsing inside a `JsonBook` class that stores the JSON body and returns the ISBN through its `isbn()` method.
- With that design, the REST entry point only constructs `new JsonBook(...)` and passes it to `library.register(...)`.
- The article gives `RqUser` as another example from the author’s projects.
- When a primitive like `String` is a `final` class rather than an interface, the article uses a class that implements `Scalar<String>` and returns the parsed value from `value()`.
- These examples are presented as support for the principle of parsing objects.
