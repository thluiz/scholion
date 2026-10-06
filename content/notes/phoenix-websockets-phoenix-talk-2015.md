---
title: "Phoenix & WebSockets"
date: '2015-06-02T17:37:57-03:00'
category: webclip
summary: 'The thread says Phoenix could not support raw WebSockets directly at the time, because its websocket support for Channels was tied to a private Cowboy API. The recommended path was Plug dispatch options with a raw Cowboy websocket handler.'
tags: ["phoenix", "websockets", "cowboy", "plug"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Phoenix & WebSockets - th.luiz@gmail.com - Gmail"
    url: "https://mail.google.com/mail/u/0/?pli=1#inbox/14dab96b92a57e17"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-06/mail-google-com--phoenix-websockets-phoenix-talk-2015.md"
    kind: repo
---

The discussion centers on raw WebSockets in Phoenix. Jakub says he needs direct access to the WebSocket, not Channels, and that Plug has no WebSocket API either. Chris McCord replies that Phoenix cannot support raw WebSockets directly yet, because its websocket support for Channels uses a private Cowboy API, and that the best option is a raw Cowboy websocket handler with Plug dispatch options.

## Reading notes

- Jakub needs raw WebSockets, not Channels, for a system he is building.
- He is already using Cowboy for WebSockets and wants a small API in Phoenix for other requests.
- He says Phoenix docs do not mention WebSockets.
- He says Plug also has no WebSocket API.
- He notes Phoenix runs on top of Cowboy, so he is currently running one Cowboy instance for WebSockets and another for Phoenix.
- Steve Domin points to Phoenix websocket code in `phoenix/endpoint/cowboy_websocket.ex`.
- Chris McCord says Phoenix cannot support raw WebSockets directly until Plug has a WebSocket API.
- Chris says Phoenix supports websocket transport for Channels through a private API coupled to Cowboy.
- Chris recommends Plug dispatch options and a raw Cowboy websocket handler for raw WebSockets.
- Chris explains that Channels abstract the transport layer, support websockets and longpolling, and add pubsub and channel callbacks on top of the transport.
- Chris says Channels also provide reconnects, backoff, error handling, authorization, and multiplexing over a single connection.
- Ivan Miranda asks for the difference between Channels and WebSockets and thanks Chris for the clarification.
- Josh Adams says he is working on a websockets proxy and would like to see common abstractions overlap.
