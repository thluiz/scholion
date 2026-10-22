---
title: "Functional Reactive Programming in JavaScript"
date: '2013-10-06T23:28:00-03:00'
category: webclip
summary: 'The post introduces FRP as a way to reduce complexity in user input and asynchronous work, then shows Bacon.js streams and properties in a simple Wikipedia search example.'
tags: ["functional-reactive-programming", "javascript", "bacon-js", "event-streams", "reactive-programming"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "If you are a front-end developer – that is, someone who builds user interfaces f"
    url: "http://flippinawesome.org/2013/09/30/functional-reactive-programming-in-javascript/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2013-10/flippinawesome-org--functional-reactive-programming-in-javascript.md"
    kind: repo
---

The post presents Functional Reactive Programming as a way to simplify user input and asynchronous operations. It explains reactive programming through a changing relationship between values, then shows how Bacon.js uses event streams and properties to build a small Wikipedia search example.

## Reading notes

- FRP is presented as useful for dealing with user input and asynchronous operations, especially where callback chains become hard to manage.
- Reactive programming is explained as treating value relationships as time-based rather than as one-time assignments.
- Functional Reactive Programming is described as reactive programming implemented with functional style and side-effect-free code.
- Bacon.js is used as the example implementation for a simple Wikipedia search tool.
- An input field and search button are wired into event streams.
- Event streams are described as time-based series of discrete events that can be merged, filtered, or mapped before handling.
- A search can be triggered either by clicking the button or pressing Enter in the input field.
- In Bacon.js, the button stream and enter-key stream are merged, mapped to the input value, and passed through `flatMapLatest(doSearch)`.
- `doSearch` builds a Wikipedia API URL and returns `Bacon.fromPromise($.ajax(...))`.
- `flatMapLatest` keeps only events from the latest spawned stream.
- Properties are described as values that always have a current value and can change over time.
- `scan(0, ...)` is used to count searches by incrementing a value whenever `searchStream` emits.
- `toProperty()` is used to turn mapped search results into a property containing the number of results.
- The post says this avoids global variables and manual updates in the UI.
- The conclusion says the post only covers the surface of FRP libraries and mentions RxJS as another option.
