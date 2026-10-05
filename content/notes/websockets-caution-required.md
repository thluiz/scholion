---
title: "WebSockets, caution required!"
date: '2015-12-30T09:10:00-03:00'
category: webclip
summary: 'The article argues that WebSockets are an implementation detail, not a feature, and that most realtime web apps need reliable client updates more than a new server backchannel.'
tags: ["websockets", "realtime-web", "http2", "messaging-reliability"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "WebSockets, caution required!"
    url: "https://samsaffron.com/archive/2015/12/29/websockets-caution-required"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-12/samsaffron-com--websockets-caution-required.md"
    kind: repo
---

The article argues that WebSockets are not the best default for realtime web apps. Users want live apps, developers want them to be easy to build, and operations want them to be easy to deploy and manage. The server-to-client side is useful, but the browser-to-server backchannel adds debugging, logging, rate-limiting, load, and connection-management problems that many apps do not need.

It lists several drawbacks: proxy issues on unsecured HTTP, many open connections per browser, a lack of unity with HTTP/2, server-side complexity, load-balancing complications, the tendency to re-create HTTP semantics, and the fact that WebSockets still need reliable messaging because the network is unreliable. The article concludes that reliable messaging is more important than WebSockets and that transport-agnostic systems like MessageBus can support polling, streaming, EventSource, and other mechanisms.

## Reading notes

- WebSockets help only if they deliver realtime apps that are easy to build, deploy, scale, and manage.
- A new browser-to-server backchannel creates extra choices and operational concerns for developers.
- Many web applications are mostly read-oriented, so the server-to-client direction matters more than client-to-server transport.
- WebSockets have had spec instability and compatibility fallout, including support gaps in older browsers.
- Unsecured HTTP can break WebSockets because proxy behavior is unreliable.
- Browsers allow many open WebSocket connections, which can multiply server load across tabs.
- HTTP/2 handles multiple tabs more efficiently, but it does not unify with WebSockets.
- Efficient WebSocket servers in Ruby require low-level event mechanisms such as epoll or kqueue.
- Load balancing becomes harder when connections stay open indefinitely.
- Sophisticated WebSocket setups end up resembling HTTP with channels, routing, and payloads.
- WebSockets still need reliable delivery, ordering, and catch-up logic because connections can fail.
- Reliable messaging infrastructure can support multiple transports, including polling and streaming.
- Discourse does not use WebSockets and relies on MessageBus and HTTP/2 templates instead.
