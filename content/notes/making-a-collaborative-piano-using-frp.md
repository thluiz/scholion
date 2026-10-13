---
title: "Making a Collaborative Piano Using Functional Reactive Programming (FRP)"
date: '2013-10-07T10:03:34-03:00'
category: webclip
summary: 'The post explains FRP through a collaborative piano built in CoffeeScript, where clicks, keypresses, and WebSocket messages are merged into one event flow and mirrored across clients.'
tags: ["functional-reactive-programming", "bacon-js", "websockets", "javascript"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Making a Collaborative Piano Using Functional Reactive Programming (FRP)"
    url: "http://open.bekk.no/making-a-collaborative-piano-using-functional-reactive-programming-frp"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2013-10/open-bekk-no--making-a-collaborative-piano-using-frp.md"
    kind: repo
---

The post uses a collaborative piano to show how Functional Reactive Programming handles multiple inputs in a clear way. It explains FRP as a mix of functional and reactive programming, with behaviours for values that vary over time and events for discrete values such as clicks, keypresses, and socket messages.

## Reading notes

- FRP is presented as a way to merge and transform multiple event inputs into one sequence of interactions in a declarative style.
- Behaviours vary over continuous time, while events are discrete streams with values only when they occur.
- In the piano example, the client is written in CoffeeScript and the server uses Node.js, ExpressJS, and Socket.io.
- Clicks on piano keys are turned into an event stream, mapped to note names, and sent to a player function.
- Keypresses are turned into another stream, translated through a mapping from key codes to piano keys, and filtered to keep only mapped keys.
- The click and keypress streams are merged so the same sound action runs for both.
- A server event stream is created from WebSocket messages so notes played by other clients can also be heard.
- The local note stream is merged with the server stream, and local notes are emitted before merging so they can be broadcast to other clients.
- The same key streams are reused to add an active class to the corresponding piano key, then remove it after 200 ms.
- Bacon.js is used for the example because it distinguishes between behaviours and events, unlike RxJS, which is described here as using observables.
