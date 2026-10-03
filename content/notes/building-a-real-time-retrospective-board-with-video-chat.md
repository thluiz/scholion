---
title: "Building A Real-Time Retrospective Board With Video Chat"
date: '2016-03-21T08:31:43-03:00'
category: webclip
summary: 'The article shows how to build a virtual retrospective board with deepstream, using records and lists for sticky notes, real-time sync, password login, and WebRTC video chat.'
tags: ["deepstream", "webrtc", "real-time-sync", "agile"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Building A Real-Time Retrospective Board With Video Chat – Smashing Magazine"
    url: "https://www.smashingmagazine.com/2016/03/building-a-real-time-retrospective-board-with-video-chat/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2016-03/smashingmagazine-com--building-a-real-time-retrospective-board-with-video-chat.md"
    kind: repo
---

The article outlines a virtual retrospective board for distributed agile teams. It uses deepstream for real-time state sync, login with a shared password, and WebRTC for video chat so team members can hold the meeting from different locations.

## Reading notes

- The board needs to let users create, edit, and move sticky notes, keep the board state in sync in real time, talk through video chat, and require the right password at login.
- The setup uses jQuery and deepstream, with deepstream providing pub-sub, RPC, data sync, and WebRTC support.
- The server is started with deepstream.io, then restricted with a permissionHandler that checks for a username and the password `sesame`.
- On the client side, the app connects to `localhost:6020`, shows a login form, and only starts the board and video chat after `ds.login()` succeeds.
- Deepstream records store individual sticky notes, and lists store collections of record names. The board itself is represented as a list, and each sticky note is a record.
- Sticky note text is synced by subscribing to record changes and writing user edits back to the same record field.
- Dragging is handled by using the record position as the single source of truth, so the DOM updates from the record and drag events update the record.
- Adding a note works by adding a new record ID to the board list, and list events are used to render notes when they appear.
- WebRTC is described as a browser-to-browser media system that still needs a server for coordination, and deepstream reduces it to a phonebook and a call.
- Local audio and video are obtained with `getUserMedia`, then inserted into a video element with `srcObject`.
- The app registers the logged-in user as a callee, listens for other callees, and uses that phonebook to build a room-like many-to-many connection model.
- When callees are received, the client calls every other user except itself, and incoming calls are accepted with the local stream.
- The article closes by noting that production RTC apps still rely on workarounds and evolving standards, while libraries like adapter.js and deepstream help bridge the gap.
