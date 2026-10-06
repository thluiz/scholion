---
url: "https://www.christian-schneider.net/CrossSiteWebSocketHijacking.html"
captured_at: "2015-04-22T16:24:21-03:00"
title: "Cross-Site WebSocket Hijacking (CSWSH)"
domain: "christian-schneider-net"
---

# Cross-Site WebSocket Hijacking (CSWSH)

![db65e419ca72a20e418bb8b040baa920.jpg](christian-schneider-net--cross-site-websocket-hijacking-cswsh/db65e419ca72a20e418bb8b040baa920.jpg)

The relatively new **HTML5 WebSocket** technique to enable full-duplex communication channels between browsers and servers is retrieving more and more attention from developers
as well as security analysts. Using WebSockets developers can exchange text and binary messages pushed from the server to the browser as well as vice versa.

During some experiments and pentests with WebSocket backed applications in the last few months I came across a scenario where developers might use WebSockets in a way
to open up their applications to a vulnerability I call **Cross-Site WebSocket Hijacking (CSWSH)**, which I will present in this short blog post.

### The protocol upgrade

In order to create the full-duplex communication channel the WebSocket protocol requires a handshake (carried out over `http://` or `https://`) to switch towards
a WebSocket protocol. This handshake effectively upgrades the communication protocol to `ws://` (or `wss://` for SSL protected channels).
But this upgrade phase is also a potential target to attack and Achilles' heel of using
WebSockets inside an application that deals with non-public data, because it kind of *bridges/transfers* the HTTP(S)-based communication towards the WS(S)-based WebSocket protocol.

The typical lifecycle of a WebSocket interaction between client & server goes as follows:

1. Client initiates a connection by sending an HTTP(S) WebSocket handshake request.
2. Server replies with a handshake response (all handled by the web application server transparently to the application) and sends a response status code of *101 Switching Protocols*.

From that point on both browser and server communicate using WebSocket API with a completely symmetrical connection (each party can send and retrieve text and binary messages).
On the browser level this is defined by W3's HTML5 WebSocket API specification and at protocol level via RFC 6455 "The WebSocket Protocol".

Let's take a closer look at this handshake request and inspect the **request headers** of such a handshake to upgrade the protocol to WebSockets
*(of an imaginary stock portfolio management application, which uses WebSockets to quickly push new stock quotes to logged-in users as well as retrieve stock orders from them)*:

```
"GET /trading/ws/stockPortfolio HTTP/1.1"
Host: www.some-trading-application.com
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:23.0) Firefox/23.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: de-de,de;q=0.8,en-us;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
DNT: 1
Sec-WebSocket-Version: 13
Origin: https://www.some-trading-application.com
Sec-WebSocket-Key: x7nPlaiHMGDBuJeD6l7y/Q==
Cookie: JSESSIONID=1A9431CF043F851E0356F5837845B2EC
Connection: keep-alive, Upgrade
Pragma: no-cache
Cache-Control: no-cache
Upgrade: websocket
```

As you can see from the request headers of the HTTP(S) handshake request, the authentication data (in this example the **Cookie** header) is sent along with the upgrade handshake.
The same would be true for HTTP-Authentication data. Both is correct behaviour of the browsers according to the aforementioned specification and RFC.

Upon successful
WebSocket handshake the server replies with the *101 Switching Protocols* status code and from then on the `ws://` or `wss://` based connection is
established between browser and server. The header `Sec-WebSocket-Key` is part of the browser/server handshake internals (to verify that the server has read and
understood the request) and is automatically created by and taken care of the browser
initiating the WebSocket request.

Regarding client authentication during this handshake/upgrade phase the RFC 6455 reads as follows:

> This protocol doesn't prescribe any particular way that servers can authenticate clients during the WebSocket handshake.
> The WebSocket server can use any client authentication mechanism available to a generic HTTP server, such as cookies, HTTP authentication, or TLS authentication.

RFC 6455 "The WebSocket Protocol", chapter 10.5 WebSocket Client Authentication

This means to developers that they can use for example cookies or HTTP-Authentication to authenticate the WebSocket handshake request, as if it was a regular HTTP(S) web application request.

### Hijacking it cross-site

Now let's consider what happens when a developer follows this well-known style of using session cookies to authenticate the WebSocket handshake/upgrade request
within a logged-in (sensitive) part of a web application:

Because WebSockets are **not restrained by the same-origin policy**, an attacker can easily initiate a WebSocket
request (i.e. the handshake/upgrade process) from a malicious webpage targeting the `ws://` or `wss://` endpoint URL of the attacked application (the
stock service in our example). Due to the fact that this request is a regular HTTP(S) request, browsers send the cookies and HTTP-Authentication headers along, even cross-site.

Take a look at the WebSocket handshake/upgrade request when issued from a malicious webpage cross-site (visited by the victim while logged-in with our stock trading application).
Here the WebSocket endpoint `wss://www.some-trading-application.com/trading/ws/stockPortfolio` is accessed from a malicious webpage at
`https://www.some-evil-attacker-application.com`

```
"GET /trading/ws/stockPortfolio HTTP/1.1"
Host: www.some-trading-application.com
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:23.0) Firefox/23.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: de-de,de;q=0.8,en-us;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
DNT: 1
Sec-WebSocket-Version: 13
Origin: https://www.some-evil-attacker-application.com
Sec-WebSocket-Key: hP+ghc+KuZT2wQgRRikjBw==
Cookie: JSESSIONID=1A9431CF043F851E0356F5837845B2EC
Connection: keep-alive, Upgrade
Pragma: no-cache
Cache-Control: no-cache
Upgrade: websocket
```

As you can see, the browser sends the authentication information (in this example the session cookie) along with the WebSocket handshake/upgrade request.
This is very similar to a **Cross-Site Request Forgery (CSRF)** attack scenario. But in the WebSocket scenario this attack can be extended from a write-only CSRF attack
to a full read/write communication with a WebSocket service by physically establishing a new WebSocket connection with the service under the *same authentication data as the victim*.
Therefore I call this attack vector **Cross-Site WebSocket Hijacking (CSWSH)**.

Effectively this allows the attacker in our scenario to read the victim's stock portfolio updates pushed via the WebSocket connection and update the protfolio
by issuing write requests via the WebSocket connection. This is possible due to the fact that the server's WebSocket code relies on the session authentication data
(cookies or HTTP-Authentication) sent along from the browser during the WebSocket handshake/upgrade phase.

Another interesting observation is the `Origin` header that is sent along the WebSocket handshake/upgrade request. This is like in a regular CORS request utilizing
*Cross-Origin Resource Sharing*: If this was a regular HTTP(S) CORS request, the browser would not let the JavaScript on the malicious webpage see the response,
when the server does not explicitly allow it (via a matching `Access-Control-Allow-Origin` response header). But when it comes to WebSockets this "fail close"
style of defaulting to "restrict response access" when the server does not explicitly allow cross-origin requests is inverted: In our example the server *did not* send
any CORS response headers along, but the cross-site WebSocket request's response is still handled by the browser by properly establishing the full-duplex WebSocket connection.
This demonstrates that WebSockets are not protected by the same-origin policy (SOP), so developers must not rely on SOP protection when it comes to developing WebSocket based applications.
Clearly the CORS stuff has nothing to do with the WebSockets stuff, but they both utilize the same request header (`Origin`) and the server-side code should check that header!

### Securing it

As you've already noticed, securing an application against **Cross-Site WebSocket Hijacking** attacks can be performed using two countermeasures:

1. Check the `Origin` header of the WebSocket handshake request on the server, since that header was designed to
   protect the server against attacker-initiated cross-site connections of victim browsers!
2. Use session-individual random tokens (like CSRF-Tokens) on the handshake request and verify them on the server.

These simple but effective protections must be used as soon as you're using WebSockets inside an application which access the web session on the server-side
to communicate and/or accept private data via the WebSocket channel.

If you don't need to access the web session from the server-side WebSocket counterpart, just separately handle authentication and/or authorization
using custom tokens or similar techniques *within* your WebSocket protocol and avoid relating to the web session via cookies or HTTP-Authentication
during the handshake request.

### Conclusion

As a Pentester
:   Check for *Cross-Site WebSocket Hijacking* attacks as soon as you notice any WebSocket based communication in the application you're analysing.
    As a side note, in case you already find *Origin* header verification present in the application, try to bypass it from victim's browser: When the server expects *https://www.some-trading-application.com*
    as the Origin, mount your attacks on *https://www.some-trading-application.com.some-evil-attacker-application.com* to test for obviously broken *Origin* header verifications.

As a Security Consultant
:   Make your clients aware of the requirement to always check *Origin* headers. Educate them to secure all WebSocket handshakes using
    random tokens (like protecting against CSRF attacks) or let them embed the authentication and/or authorization *into* the WebSocket protocol (avoid web session access).

As a Developer
:   Make sure you are aware of this attack scenario and know how to employ the countermeasures securely
    into your application (at least when you need to access the web session from the application part that uses WebSockets or when you otherwise
    try to transfer non-public data over that channel). Better try to avoid accessing the web session from the server-side WebSocket counterpart
    and separately handle authentication and/or authorization using tokens or similar techniques *within* your WebSocket protocol.

by [Christian Schneider](https://www.christian-schneider.net/contact.html#main)
on August 31st, 2013

[Feedback](https://www.christian-schneider.net/CrossSiteWebSocketHijacking.html#comment)
