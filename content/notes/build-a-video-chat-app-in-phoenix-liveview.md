---
title: "Build a Video Chat App in Phoenix LiveView"
date: '2026-11-16T08:17:52+00:00'
category: webclip
summary: 'The article walks through building a multi-user video chat app with Phoenix LiveView, Presence, PubSub, and WebRTC, including room creation, presence tracking, signaling, and a STUN server.'
tags: ["phoenix-liveview", "webrtc", "presence", "pubsub"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Build a Video Chat App in Phoenix LiveView | Littlelines"
    url: "https://web.archive.org/web/20200823145045id_/https://littlelines.com/blog/2020/07/06/building-a-video-chat-app-in-phoenix-liveview"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/web-archive-org--build-a-video-chat-app-in-phoenix-liveview.md"
    kind: repo
---

The article shows how to build a real-time video chat app in Phoenix LiveView. It starts with room creation and room lookup, then adds Phoenix Presence to track who is connected in each room. From there, it wires LiveView hooks and JavaScript to access the camera, create peer connections, and pass signaling data between clients through PubSub-backed LiveView events.

## Reading notes

- Creates a room model with title and slug, with a unique slug index and slug normalization.
- Uses LiveView to create rooms and to show a room by slug, redirecting if the room does not exist.
- Uses Phoenix Presence to track ephemeral connected users in a room topic.
- Adds a local video stream through a LiveView hook and browser media access.
- Explains WebRTC signaling, SDP offers and answers, ICE candidates, and STUN servers.
- Uses a mesh architecture so each user creates a peer connection with every other connected user.
- Sends offer requests, SDP offers, answers, and ICE candidates through LiveView events and PubSub broadcasts.
- Uses hidden DOM elements with hooks to pass server-side state into JavaScript.
- Adds a STUN server to the Phoenix application with a GenServer and starts it in the supervision tree.
