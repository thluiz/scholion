---
title: "WebSockets in Ruby"
date: '2014-03-05T11:04:25-03:00'
category: webclip
summary: 'The post describes moving a geocoding service in Ruby from HTTP to WebSockets, compares Ruby WebSocket options, and settles on webmachine-ruby with Celluloid actors for per-client CPU-heavy work.'
tags: ["websockets", "ruby", "webmachine-ruby", "celluloid"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "WebSockets in Ruby - Troika Tech"
    url: "http://www.troikatech.com/blog/2014/02/26/websocket-webmachine/?utm_source=rubyweekly&utm_medium=email"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2014-03/troikatech-com--websockets-in-ruby-troika-tech.md"
    kind: repo
---

The post says the service had to keep instant coordinate conversion feedback while avoiding a growing data download and heavy client-side loading. Because Ruby WebSocket options were limited, the author tested several approaches and settled on webmachine-ruby.

## Reading notes

- The original geocoding service was built in Ruby as a library plus a simple Sinatra webservice.
- The client later required a conversion on every mouse move, which led to a JavaScript version.
- Support for multiple Roads per User made larger downloads and client-side loading impractical.
- The author looked for a Ruby WebSocket solution and briefly considered using node.js instead.
- sinatra-websocket did not upgrade the connection to a WebSocket.
- faye-websocket was skipped.
- Rails-based options used too much memory on a small Heroku dyno and could crash during startup.
- webmachine-ruby was the remaining option.
- The author migrated the HTTP service to webmachine resources before adding WebSockets.
- webmachine-ruby uses a callable websocket handler through Reel.
- A handler can read from the socket and act on the message.
- The docs do not explain that the handler should loop on reads to avoid hanging.
- Celluloid::IO provides non-blocking socket reads.
- The author assigned each client to a Celluloid Actor to isolate CPU-intensive operations.
- The solution does not yet handle non-WebSocket clients.
- The author notes missing socket events and says the actor is allowed to crash in the current use case.
- The author mentions faye and websocket-rails as options when a pub/sub system is needed.
