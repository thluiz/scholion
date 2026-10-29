---
title: "Implementing Video Chat in a Phoenix Application with WebRTC"
date: '2016-03-11T17:51:57-03:00'
category: webclip
summary: 'The post explains how to add video chat to a Phoenix app by using Phoenix channels to exchange signaling data, then creating a direct WebRTC peer connection with local and remote video streams.'
tags: ["phoenix", "webrtc", "phoenix-channels", "video-chat"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Implementing Video Chat in a Phoenix Application with WebRTC"
    url: "https://hashrocket.com/blog/posts/implementing-video-chat-in-a-phoenix-application-with-webrtc"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2016-03/hashrocket-com--implementing-video-chat-in-phoenix-application-webrtc.md"
    kind: repo
---

The article walks through a basic WebRTC video chat setup in a Phoenix app. Phoenix channels handle the signaling needed before two clients can open a direct peer-to-peer connection, while the browser side uses getUserMedia, RTCPeerConnection, and ICE candidates to move from local stream capture to a working video call.

## Reading notes

- Create a new Phoenix app and route the root path to a call controller that renders a page with local and remote video elements plus Connect, Call, and Hangup buttons.
- Add a call channel with join and message handling, then register that channel in the user socket so clients can join it.
- Include adapter.js in the layout so the WebRTC methods work across browsers.
- In app.js, import the socket, join the call channel, and wire the buttons to connect, call, and hang up.
- The connect action requests local media with getUserMedia and passes the stream to gotStream.
- gotStream stores the local stream, assigns it to the local video element, and calls setupPeerConnection.
- setupPeerConnection creates an RTCPeerConnection, sets callbacks for ICE candidates and remote streams, and adds the local stream to the connection.
- call triggers createOffer, and gotLocalDescription stores the local description and sends it through the channel as signaling data.
- When a remote description arrives, gotRemoteDescription sets it on the peer connection and creates an answer.
- Remote streams are assigned to the remote video element in gotRemoteStream.
- Local ICE candidates are sent through the channel, and incoming ICE candidates are added to the peer connection in gotRemoteIceCandidate.
- The channel message handler parses incoming payloads and decides whether to pass them to gotRemoteDescription or gotRemoteIceCandidate.
- hangup closes the peer connection and resets the page state.
- The post ends by saying that opening two tabs, connecting in both, and calling from one tab should produce a video chat session.
