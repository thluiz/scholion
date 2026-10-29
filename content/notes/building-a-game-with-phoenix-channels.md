---
title: "Building a Game with Phoenix Channels"
date: '2016-05-09T13:59:58-03:00'
category: webclip
summary: 'Tutorial that builds a simple browser game with Phoenix Channels, using an Agent for shared state, channel events for movement, collision detection, Gravatar avatars, and score tracking.'
tags: ["phoenix-channels", "elixir", "browser-game"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Building a Game with Phoenix Channels — Medium"
    url: "https://medium.com/@miguel.coba/building-a-game-with-phoenix-channels-a3e6b390cfcc"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2016-05/medium-com--building-a-game-with-phoenix-channels.md"
    kind: repo
---

The article walks through building a simple multiplayer game with Phoenix Channels. Players join through their email, move with the arrow keys, and share the same game state through an Agent rather than the database. The browser draws the board with canvas and listens for channel events to keep every client synchronized.

## Reading notes

- The game is a browser-based board where players move with the arrow keys and score points by hitting other players.
- The interface uses HTML canvas for the board, a message area, and an email input for the player identifier.
- Game state is stored in an Elixir Agent as a map keyed by player email.
- The supervision tree starts the Agent together with the application.
- The socket defines a `players:*` channel and assigns the player id from the incoming connection params.
- Joining `players:lobby` returns the current players list and then broadcasts a `player:joined` event.
- The browser stores the players list, draws the board, and handles `player:joined` and `player:position` events.
- Player movement is sent as `player:move` messages from arrow-key handlers in the browser.
- The server updates positions, keeps them inside the board limits, and broadcasts the new position to all clients.
- Gravatar support adds an avatar URL to each player and caches loaded images in the browser.
- Collision detection compares player coordinates, respawns the killed player at the center, and increments the killer’s score.
- The browser shows a red background briefly when the local player is killed and renders the kills counter next to each sprite.
