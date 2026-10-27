---
title: "WebSockets in Rails 4"
date: '2013-11-13T11:45:34-03:00'
category: webclip
summary: 'The post explains how Rails 4 concurrency and Rack Hijack make WebSockets practical in Rails controllers, and introduces Tubesock as a small gem that wraps this approach.'
tags: ["rails-4", "websockets", "rack-hijack", "concurrency"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "WebSockets in Rails 4"
    url: "http://ngauthier.com/2013/03/websockets-in-rails-4.html"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2013-11/ngauthier-com--websockets-in-rails-4.md"
    kind: repo
---

The post says Rails 4’s concurrent request handling makes it possible to keep WebSocket connections open in a single process with a concurrent server like Puma. It also says this approach avoids EventMachine and any reactor model.

## Reading notes

- Rails 4 is described as fully concurrent, so there is no full-stack lock on a request.
- With a concurrent server like Puma, one process can handle many requests at the same time.
- Ruby threads inside a Rails app can hold WebSocket connections open without bogging down the server.
- Rack Hijack, available since Rack 1.5.0, gives access to the underlying socket for bidirectional communication with the client.
- Because Rails is built on Rack, the client socket can be grabbed directly from a Rails controller.
- Tubesock is presented as a small, new, untested gem that packages this functionality.
- Tubesock provides a Rails controller module and a wrapper method to hijack the Rack connection.
- It also wraps the `websocket` gem to handle WebSocket handshakes and frames.
- The example controller shows a `chat` action that hijacks the connection, sends a greeting on open, and echoes received data back to the client.
- The post links to the Tubesock GitHub repository and to an example chat application.
