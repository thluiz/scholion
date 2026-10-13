---
title: "Building Multiplayer Games with Node.js and Socket.IO"
date: '2013-10-06T23:29:40-03:00'
category: webclip
summary: 'The article explains how Anagrammatix uses Node.js, Express, and Socket.IO to run a real-time multiplayer word game across a host screen and mobile controllers, with server-managed rooms and events.'
tags: ["node-js", "socket-io", "multiplayer-games", "real-time-web", "javascript", "nodejs"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Building Multiplayer Games with Node.js and Socket.IO | Flippin' Awesome"
    url: "http://flippinawesome.org/2013/09/30/building-multiplayer-games-with-node-js-and-socket-io/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2013-10/flippinawesome-org--building-multiplayer-games-with-node-js-and-socket-io.md"
    kind: repo
---

The article walks through Anagrammatix, a multiplayer word game built with HTML, CSS, JavaScript, Node.js, Express, and Socket.IO. A large browser screen acts as the host, mobile browsers act as controllers, and the server relays events and data between them in real time.

## Reading notes

- The game is an anagram challenge where the host screen shows a word, players see a list of options, and the first correct tap earns points while wrong taps lose points.
- To run it locally, Node.js must be installed, the repository cloned, dependencies installed with npm, and the server started with node index.js.
- The setup uses Node.js for the backend, Express for serving static files and handling HTTP requests, and Socket.IO for real-time browser-server communication.
- Socket.IO falls back to other transport methods when websockets are not supported.
- Client-side code uses jQuery, TextFit, FastClick.js, and CSS for DOM handling, responsive text, faster taps, and styling.
- The architecture uses Express on the same port as Socket.IO, and each websocket connection gets a unique identifier.
- Server-side game code lives in agxgame.js, while index.js loads the modules and starts the server.
- Socket.IO event listeners connect browser events to server functions and server events to client functions.
- The browser loads index.html and templates from the public folder, then app.js initializes Socket.IO and the initial screen.
- The host creates a game by emitting hostCreateNewGame, and the server creates a room, returns the game ID, and joins the host to that room.
- Players join by sending a game ID and name; the server checks whether the room exists, adds the player, and notifies everyone in the room.
- When the room has two players, the host triggers hostRoomFull, and the server emits beginNewGame to everyone in that room.
- The host shows a five-second countdown while players see Get Ready.
- When the countdown ends, the host emits hostCountdownFinished and the server sends the first word.
- Word data contains a displayed word, the correct answer, and a list of decoys; the answer is inserted into the player list at a random position.
- The host displays the word, and the player screens render the answer list as buttons.
- When a player taps a word, the client sends the answer, game ID, player ID, and round to the server, which forwards it to the host as hostCheckAnswer.
- The host checks whether the answer belongs to the current round, updates the score, and advances the game only for the correct current-round answer.
- When the word pool is exhausted, the server emits gameOver and the host displays the winner.
- After game over, the host resets its waiting state so players can start another game.
- The article recommends Chrome developer tools, especially the Network tab and WebSockets frames, for tracking websocket traffic and debugging events.
