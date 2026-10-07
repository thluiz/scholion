---
title: "Building a 3D Multiplayer Game with Pusher"
date: '2014-11-27T10:13:24-03:00'
category: webclip
summary: 'Tutorial showing how to build a simple 3D multiplayer game with Three.js and Pusher, using event-driven updates, presence channels, and synced player movement across browser tabs.'
tags: ["threejs", "pusher", "multiplayer-games", "realtime-web"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Building a 3D Multiplayer Game with Pusher - Pusher Blog"
    url: "http://blog.pusher.com/building-3d-multiplayer-game-pusher/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2014-11/blog-pusher-com--building-a-3d-multiplayer-game-with-pusher.md"
    kind: repo
---

The tutorial explains how to make a simple 3D multiplayer game that uses Three.js for the scene and Pusher for real-time communication. It starts with a floor, a cube player, click-based movement, and then adds presence channels so multiple browser tabs can join the same game, see who is online, and keep player state in sync.

It also shows how to move from instant position changes to smoother movement by storing rotation, distance, direction, and facing state on each player object, then updating those values through Pusher events.

## Reading notes

- The author uses Pusher to avoid inefficient game-loop calls and switches to event-driven communication for player updates.
- ID-named events are used to address specific clients without creating separate private channels for each member.
- Presence channels provide member lists plus member-added and member-removed events.
- A PHP auth endpoint is used to authenticate the presence channel.
- Each player is stored in an associative array keyed by member ID.
- On subscription, cubes are created for existing members and the local player is assigned to `me`.
- When a member joins or leaves, the corresponding cube is created or removed.
- Player positions are synced by triggering client events that send the player ID and position.
- For smooth movement, each player also stores `mesh`, `rotation`, `angle_diff`, `direction`, `distance`, and `facing_destination`.
- The render loop rotates players toward their destination before translating them forward.
- The tutorial ends by syncing these movement variables so all tabs animate the same way.
