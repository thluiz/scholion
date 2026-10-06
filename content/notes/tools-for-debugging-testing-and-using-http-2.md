---
title: "Tools for debugging, testing and using HTTP/2"
date: '2015-12-23T15:01:19-03:00'
category: webclip
summary: 'The post lists browser add-ons, command-line tools, load-testing tools, conformance checks, libraries, packet decoding setup, and Chrome developer features for working with HTTP/2.'
tags: ["http-2", "debugging-tools", "load-testing", "wireshark"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Tools for debugging, testing and using HTTP/2"
    url: "http://blog.cloudflare.com/tools-for-debugging-testing-and-using-http-2/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-12/blog-cloudflare-com--tools-for-debugging-testing-and-using-http-2.md"
    kind: repo
---

The post gathers tools for checking, testing, and debugging HTTP/2. It begins with browser indicators and online checks, then moves to command-line clients, load testing, conformance testing, development libraries, packet analysis, and Chrome developer features for seeing which resources were loaded with HTTP/2.

## Reading notes

- Chrome and Firefox add-ons can show whether a page used HTTP/2, SPDY, or HTTP/1.1.
- Online tools can test whether a site supports HTTP/2.
- Claire reports how a page was loaded, including IPv6, Railgun, and HTTP/2.
- `is-http2` checks a site from the command line and reports the protocols a server advertises.
- `curl` gained HTTP/2 support in version 7.43.0 when linked with `nghttp`, and `--http2` makes it use HTTP/2 when possible.
- `nghttp` can show the HTTP/2 frames sent and received.
- `h2c` can keep connections alive, run in the background, and dump HTTP/2 frames for debugging.
- `openssl s_client -nextprotoneg ''` can show which protocols a site advertises.
- `h2i` lets you connect to an HTTP/2 site and send individual frames interactively.
- `h2load` is the load-testing tool included with `nghttp2`.
- `h2spec` runs conformance tests against a real HTTP/2 server and reports results with RFC7540 references.
- `h2scan` checks a list of sites for HTTPS, SPDY/3.1, and HTTP/2 support.
- `nghttp2`, Go’s `x/net/http2`, a Ruby implementation, and Haskell’s `http2` package are listed as useful libraries.
- Wireshark decodes HTTP/2, and Chrome can write TLS session keys to `SSLKEYLOGFILE` so Wireshark can decrypt traffic.
- Chrome Developer Tools can add a Protocol column to sort page resources by protocol.
- The post ends with links to an HTTP/2 introduction, `http2 explained`, and the HTTP/2 working group site.
