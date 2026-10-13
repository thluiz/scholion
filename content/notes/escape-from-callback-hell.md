---
title: "Escape from Callback Hell"
date: '2012-11-05T13:45:34-03:00'
category: webclip
summary: 'The page argues that callbacks create non-linear, hard-to-maintain code, and that Functional Reactive Programming in Elm gives a linear way to express time-dependent and asynchronous behavior.'
tags: ["callbacks", "functional-reactive-programming", "elm"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Escape from Callback Hell"
    url: "http://elm-lang.org/learn/Escape-from-Callback-Hell.elm"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2012-11/elm-lang-org--escape-from-callback-hell.md"
    kind: repo
---

Callbacks are described as a modern `goto` because they make programs jump across the codebase, which makes them difficult to read, maintain, and change. The page frames the real issue as time-dependent relationships, such as waiting for a value or letting things happen concurrently.

It contrasts three approaches with the Flickr API example: synchronous code is readable but freezes the app, callback-based code is responsive but tangled, and FRP with signals and `lift` keeps the flow linear while still handling asynchrony. The result is presented as readable, responsive code that stays concise.

## Reading notes

- Callbacks structure programs by passing control to another function when a value is ready.
- In callback-heavy code, the whole application can become a tangled mess of nested functions.
- The page compares callbacks to `goto` because both force hard-to-follow jumps through the codebase.
- The deeper problem is time dependence: some actions depend on values that change over time, and some computations happen concurrently.
- FRP is presented as a higher-level way to describe those time-dependent relationships.
- In the Flickr example, synchronous requests are easy to read but block the app.
- The callback version avoids blocking but becomes deeply nested and hard to maintain.
- FRP uses signals to represent values that change over time, such as text input.
- `lift` transforms signals, and `send` handles asynchronous requests without leaving the signal-based model.
- The final Elm version keeps a linear control flow while remaining responsive.
- The page concludes that signals can express several kinds of time relationships, including asynchrony and filtering.
