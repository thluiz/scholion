---
title: "Real Time Multiplayer in HTML5 - Build New Games"
date: '2013-01-11T11:39:06-03:00'
category: webclip
summary: 'The article outlines how browser multiplayer works for real-time games, using socket.io, Node.js, Express, and canvas, then explains client prediction, interpolation, and fixed-rate server and client loops.'
tags: ["real-time-multiplayer", "socket-io", "node-js", "html5-canvas"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Real Time Multiplayer in HTML5 - Build New Games"
    url: "http://buildnewgames.com/real-time-multiplayer/?utm_source=javascriptweekly&utm_medium=email"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2013-01/buildnewgames-com--real-time-multiplayer-in-html5-build-new-games.md"
    kind: repo
---

The article explains why HTTP is enough for turn-based or asynchronous browser games but too slow for real-time play, then shows a browser stack built with socket.io, Node.js, Express, and HTML5 canvas. It also frames the demo around a simple two-player lobby and a shared game world that runs on both server and client.

## Reading notes

- HTTP POST and GET work for semi real-time and asynchronous games, but real-time games need messages sent and received many times per second.
- socket.io is presented as the main networking layer because it supports web sockets and falls back to other transports when needed.
- Node.js and Express are used together to serve files, route requests, and host the socket.io server cleanly.
- The client side connects with a small HTML file, loads the socket.io script, and listens for the connection event.
- The demo focuses on two blocks moving in the same space so the multiplayer logic stays visible.
- Frame-rate independence is handled with delta time so movement stays consistent across devices and browsers.
- The article recommends exposing tweakable values, and the demo uses Dat.GUI for live changes.
- The networking model uses a simple lobby where a client joins an existing game or creates a new one.
- The server keeps authority over game state, while the client also runs local logic to stay responsive.
- The server uses a fast physics loop and a slower state-update loop to process input and broadcast state.
- The client uses prediction so local input changes position immediately instead of waiting for the server reply.
- Other players are smoothed with interpolation by storing server messages and drawing positions slightly behind server time.
- The shared game code lives in game.core.js so the same functions and data structures can run on both server and client.
- The demo also stores input sequences so the client can drop acknowledged inputs and reapply the remaining ones.
- The article ends by pointing to the demo, the source code, and further reading on multiplayer networking and real-time game programming.
