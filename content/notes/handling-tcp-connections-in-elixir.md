---
title: "Handling TCP connections in Elixir"
date: '2015-07-19T10:40:45-03:00'
category: webclip
summary: 'The article shows how to wrap a TCP client in a GenServer, avoid blocking with queued replies, use active sockets carefully, and add reconnect backoff with Connection.'
tags: ["elixir", "tcp", "genserver", "connection"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Handling TCP connections in Elixir"
    url: "http://andrealeopardi.com/posts/handling-tcp-connections-in-elixir/?utm_campaign=elixir_radar_13&utm_medium=email&utm_source=RD+Station"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-07/andrealeopardi-com--handling-tcp-connections-in-elixir.md"
    kind: repo
---

The article explains a pattern for handling TCP connections in Elixir by keeping the socket inside a GenServer and using it as the single interface to the server. It starts with a simple Redis client example, then shows why blocking on `:gen_tcp.recv/2` becomes a problem when multiple processes use the same GenServer.

## Reading notes

- TCP connections in Erlang and Elixir are handled with `:gen_tcp`, and the article focuses on clients that connect to an external TCP server.
- A GenServer is used to keep the TCP socket in its state and reuse it for all communication.
- The first version connects in `init/1`, uses `:binary`, and sets `active: false` so messages are not delivered automatically.
- Sending a command with `:gen_tcp.send/2` and then reading with `:gen_tcp.recv/2` works, but it blocks the GenServer while waiting for a response.
- To avoid blocking, `handle_call/3` can return `{:noreply, state}` and later reply with `GenServer.reply/2`.
- The article switches to `active: true` so TCP messages arrive as Erlang messages in `handle_info/2`.
- Because Redis replies sequentially, the GenServer keeps a queue of waiting clients and matches each response to the next client in line.
- `active: :once` is presented as a safer option than `active: true` because it delivers one TCP message at a time and reduces mailbox flooding.
- The socket is reactivated with `:inet.setopts/2` after a `{:tcp, ...}` message is handled.
- The same pattern is described as common in database drivers and similar libraries, with examples such as eredis, postgrex, and mongodb.
- The article then introduces the `Connection` behaviour to improve startup handling and reconnection support.
- With `Connection`, `init/1` can return `{:connect, info, state}` so `start_link/0` returns quickly while the connection is established in the background.
- `connect/2` can return `{:backoff, timeout, state}` when `:gen_tcp.connect/3` fails, allowing retries after a delay.
- The article ends by noting that the GenServer can be used with poolboy to form a pool of workers that checkout, use, and check in Redis clients.
