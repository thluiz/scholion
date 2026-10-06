---
title: "HTML5 WebSocket Security is Strong"
date: '2015-04-22T16:25:04-03:00'
category: webclip
summary: 'The post argues that WebSocket inherits several HTTP security mechanisms because it starts as an HTTP handshake, and it also adds native protections like subprotocol validation and client-to-server masking.'
tags: ["websocket", "security", "http-compatible", "html5"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "HTML5 WebSocket Security is Strong"
    url: "http://blog.kaazing.com/2012/02/28/html5-websocket-security-is-strong/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-04/blog-kaazing-com--html5-websocket-security-is-strong.md"
    kind: repo
---

The post says WebSocket security benefits from its HTTP-compatible design and from protections defined by the standard itself. It also says security features must be implemented by each gateway or server, and that fallback paths need to preserve the same protections.

## Reading notes

- WebSocket starts as an HTTP handshake and then upgrades to the WebSocket wire protocol, so many HTTP security mechanisms can also apply.
- HTTP compatibility is presented as a deliberate choice, including support for standard ports 80 and 443.
- TLS or SSL can secure WebSocket traffic the same way it secures HTTPS, with WebSocket Secure using TLS before the handshake and upgrade.
- Origin-based security can be applied because a WebSocket endpoint is defined by a URL, and WebSocket uses the origin security model from RFC 6454.
- Cross-origin WebSocket connections can be made securely when the gateway or server supports origin-based access control.
- Cookie-based session handling can be reused for WebSocket applications when the gateway or server reads the same cookies.
- Subprotocol validation is a native WebSocket security feature because the Sec-WebSocket-Protocol header negotiates the application-level protocol.
- Protocol-level inspection can be used to check that traffic matches the expected subprotocol and to enforce security policies.
- Client-to-server masking prevents intermediaries from relying on predictable payload bytes, and WebSocket-aware intermediaries can unmask frames for inspection.
- Fallback matters because many users will depend on it when WebSocket cannot be established.
- Security features used for WebSocket should also apply to fallback methods such as Comet, Ajax, or Flash Sockets.
- The post says Flash Sockets are a potential security risk because they can allow raw cross-origin TCP connections to the target origin’s HTTP port.
- The article ends by saying enterprise WebSocket applications should choose gateways or servers with the security features they need and plan for security early.
