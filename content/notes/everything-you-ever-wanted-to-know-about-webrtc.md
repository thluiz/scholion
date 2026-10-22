---
title: "Everything You Ever Wanted to Know About WebRTC"
date: '2021-07-28T10:07:42-03:00'
category: webclip
summary: 'The post explains WebRTC as direct peer-to-peer real-time communication, with signaling still handled by a server, and walks through MediaStream, RTCPeerConnection, and RTCDataChannel basics.'
tags: ["webrtc", "media-stream", "rtcpeerconnection", "rtcdatachannel"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Everything You Ever Wanted to Know About WebRTC"
    url: "https://blog.openreplay.com/everything-you-ever-wanted-to-know-about-webrtc"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2021-07/blog-openreplay-com--everything-you-ever-wanted-to-know-about-webrtc.md"
    kind: repo
---

The post presents WebRTC as a direct real-time communication approach for the web, contrasting it with WebSocket’s server-mediated transfer. It says WebRTC still needs a server for signaling, but once peers are connected, media and data move directly and encrypted between them.

It then breaks WebRTC into three core pieces and shows the main use cases for each one: capturing camera and microphone input with MediaStream, establishing peer connections with RTCPeerConnection, and sending arbitrary data with RTCDataChannel. It also mentions browser support, screen capture, and the role of OpenReplay Assist as a WebRTC-based example.

## Reading notes

- WebRTC stands for Web Real-Time Communication and is meant for direct connection after signaling is complete.
- A server is still needed for signaling, and it can also act as an always-online peer for transfer or backup.
- WebRTC is supported by more than 94% of reported browsers, but not by IE and older browsers.
- The core parts covered are MediaStream API, RTCPeerConnection, and RTCDataChannel.
- getUserMedia() is available in HTTPS contexts and returns a MediaStream built from one or more MediaStreamTrack objects.
- The constraints object can request audio and video and can be extended with device-specific settings such as width, height, and deviceId.
- enumerateDevices() can be used to inspect available input devices.
- getDisplayMedia() is the Screen Capture API method for accessing the device screen and, in newer browsers, sound.
- Streams can be attached to video and audio elements through srcObject.
- OpenReplay Assist is described as a WebRTC-based way to see a user’s live screen and start a quick call while debugging.
- RTCPeerConnection handles encoding, encryption, and connection setup through signaling and ICE candidates.
- The article shows offer/answer exchange with createOffer(), setLocalDescription(), setRemoteDescription(), and createAnswer().
- For media streaming, addTrack() is used to send individual tracks, while addStream() is described as obsolete.
- On the receiving side, a new MediaStream collects incoming track events and is attached to a video element.
- RTCDataChannel is used for arbitrary data transfer, created with createDataChannel() and received through the datachannel event.
- The channel is used after the open event, and send() transmits data while message receives it.
