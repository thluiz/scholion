---
title: "Cross-Site WebSocket Hijacking (CSWSH)"
date: '2015-04-22T16:24:21-03:00'
category: webclip
summary: 'The article describes how WebSocket handshakes can carry cookies or HTTP authentication cross-site, allowing an attacker to open an authenticated connection, read data, and send messages unless the server checks Origin or uses tokens.'
tags: ["websockets", "csrf", "same-origin-policy", "origin-header"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Cross-Site WebSocket Hijacking (CSWSH)"
    url: "https://www.christian-schneider.net/CrossSiteWebSocketHijacking.html"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-04/christian-schneider-net--cross-site-websocket-hijacking-cswsh.md"
    kind: repo
---

The article explains that a WebSocket connection starts with an HTTP or HTTPS handshake that upgrades to `ws://` or `wss://`. During that handshake, browsers send session cookies or HTTP authentication data, and the server can use those credentials to authenticate the connection.

It then shows how this becomes Cross-Site WebSocket Hijacking when a malicious page opens a WebSocket to a logged-in application. Because WebSockets are not restrained by the same-origin policy, the browser still sends the victim’s authentication data, which can give the attacker read and write access to private WebSocket traffic. The article recommends checking the `Origin` header on the server and using session-specific random tokens during the handshake. If the application does not need the web session on the WebSocket side, it suggests handling authentication and authorization separately inside the WebSocket protocol.

## Reading notes

- WebSocket communication begins with an HTTP(S) handshake that upgrades the connection to `ws://` or `wss://`.
- Browsers send cookies and HTTP authentication data with the handshake request.
- RFC 6455 allows servers to authenticate the handshake with cookies, HTTP authentication, or TLS authentication.
- A malicious webpage can start a cross-site WebSocket handshake to an application endpoint.
- The browser still sends the victim’s authentication data during that cross-site request.
- This can turn a write-only CSRF-style action into a read/write WebSocket connection.
- The article names this attack Cross-Site WebSocket Hijacking, or CSWSH.
- The `Origin` header is present in the WebSocket handshake and should be checked on the server.
- Session-specific random tokens can also protect the handshake.
- If the WebSocket side does not need the web session, authentication and authorization can be handled separately inside the WebSocket protocol.
