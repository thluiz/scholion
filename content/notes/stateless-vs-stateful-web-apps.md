---
title: "Stateless vs stateful web apps"
date: '2016-02-07T22:04:15-03:00'
category: webclip
summary: 'The post contrasts stateless HTTP with stateful WebSocket apps, arguing that stateful systems demand long-lived connections, careful concurrency, and efficient broadcast handling to keep latency and costs down.'
tags: ["stateless", "stateful", "websockets", "concurrency"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Stateless vs stateful web apps"
    url: "http://blog.plataformatec.com.br/2016/02/stateless-vs-stateful-web-apps/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2016-02/blog-plataformatec-com-br--stateless-vs-stateful-web-apps.md"
    kind: repo
---

The post contrasts HTTP’s stateless request model with WebSocket-based stateful apps. In HTTP, each request carries the needed data and can be handled by any server. With WebSockets, clients keep a long-lived conversation with one machine, so deployment, connection handling, and broadcast costs change.

It argues that stateful apps need infrastructure that can hold many concurrent connections and multiplex CPU and IO efficiently. The text compares Rails and Phoenix, saying Rails often pushes work into queues and external pubsub systems, while Phoenix channels can use all cores, broadcast directly, and scale across nodes without Redis.

## Reading notes

- HTTP scales more easily because each request is self-contained and can be served by any machine or process.
- WebSockets keep clients connected to one machine for a long time, so the number of open connections grows with time spent in the app.
- A stateful deployment must support many concurrent long-running connections from proxy to web server.
- Broadcasting to connected clients becomes more expensive as the number of open connections rises.
- Efficient stateful infrastructure depends on using memory, IO, and CPU as efficiently as possible.
- CPU blocking can increase latency quickly when many channel events arrive at once.
- In Ruby, the Global Virtual Machine Lock limits parallel execution in a way that affects channel work.
- In Rails, a common workaround is to queue background jobs for rendering and publishing events.
- The post warns against running CPU-intensive workers in the same process as channels because they compete for CPU.
- Platforms with proper multi-core concurrency can handle CPU and IO events across cores without locking.
- The Rails workflow described passes events through a channel, a job queue, a worker, pubsub, and then the server before reaching clients.
- Phoenix channels run on the Erlang VM and broadcast through pubsub with a shorter flow.
- Phoenix does not require an external job queue for channel broadcasts in the described setup.
- Phoenix can broadcast locally without Redis and can also broadcast across nodes in distributed mode.
- The post concludes that multi-core concurrency simplifies stateful applications and improves user experience through lower latency.
- The errata says Rails master can deploy stateful and stateless load on the same machine with a proper web server.
- The errata also clarifies that CPU use is not Ruby-specific and that Action Cable does not block on IO.
