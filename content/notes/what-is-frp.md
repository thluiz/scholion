---
title: "What is FRP?"
date: '2012-11-05T13:44:55-03:00'
category: webclip
summary: 'Explains FRP as a way to handle user input and GUI updates functionally by treating time-varying values as signals that update automatically, and shows how this simplifies interactive interfaces.'
tags: ["functional-reactive-programming", "signals", "gui", "elm"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "What is FRP?"
    url: "http://elm-lang.org/learn/What-is-FRP.elm"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2012-11/elm-lang-org--what-is-frp.md"
    kind: repo
---

FRP is presented as a functional way to handle user input and GUI updates. Its core idea is that some values change over time, and these time-varying values are called signals. In Elm, signals update automatically and can be combined to build interactive behavior.

## Reading notes

- FRP is described as a functional setting for rich interaction, especially for handling user input and updating a GUI.
- The text says FRP makes it easier to create interactive GUIs and work with sequences of synchronous and asynchronous events.
- A signal is a value that changes over time, and FRP treats such values as updating automatically.
- `Mouse.position` is used as an example of a signal that changes when the mouse moves.
- `Window.dimensions` is another signal example that changes when the window is resized.
- `count` is shown counting how many times a signal updates, here used for mouse clicks.
- `lift` is used to apply a normal function to a signal so it runs automatically when the signal updates.
- The text says lifting a function that produces static graphics onto a signal produces animation.
- FRP becomes more powerful when paired with a graphics library, enabling interactive pages and purely functional games.
- FRP can combine multiple signals, such as using `lift2` to relate mouse position to window width.
- `sampleOn` is described as sampling one signal whenever another signal updates.
- `keepWhen` keeps a signal’s value only when a boolean signal is true, and uses a default value so the result always has a value.
- The text describes FRP as declarative because it focuses on what is displayed rather than how the computer performs the updates.
- It contrasts FRP with traditional GUI frameworks that require event handlers, callbacks, and DOM manipulations.
- The page says FRP leaves many irrelevant details to the compiler, reducing the work needed for GUI programming.
