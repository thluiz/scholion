---
title: "Why Erlang?"
date: '2015-05-14T21:01:51-03:00'
category: webclip
summary: 'The post argues that Erlang fits concurrent network applications better than Ruby runtimes and libraries because its actor model avoids shared state and makes fault-tolerant systems easier to build.'
tags: ["erlang", "actor-model", "concurrency", "ruby"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Why Erlang? | SMYCK"
    url: "http://smyck.net/2012/04/22/why-erlang/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-05/smyck-net--why-erlang-smyck.md"
    kind: repo
---

The post argues that Erlang is a better choice for concurrent network applications because it implements the actor model natively. It presents Wooga as a case where an Erlang backend handled similar game complexity with far fewer application servers than a Ruby backend.

## Reading notes

- Concurrency for web applications and API backends becomes more important as multicore CPUs become more common.
- Ruby developers discuss concurrency through threads, multiple runtimes, more processes, actor-model libraries like Celluloid, or Akka through JRuby.
- Actor-based approaches in Ruby, Python, and Java still depend on runtimes that do not natively support the model.
- In the actor model, actors run at the same time, communicate by messages, and do not share global state or shared memory.
- Because each actor owns its internal state, it can serialize access to that state and reduce deadlocks and race conditions.
- The actor model fits functional languages because they embrace immutable data.
- Erlang is described as a functional language that implements the actor model for concurrency.
- Erlang was developed by Ericsson for carrier-grade telecom switches, with goals of fault tolerance, high availability, and concurrent execution.
- The author says he had long been a Ruby developer but kept hitting limits in network applications such as web apps, web servers, and proxies.
- At Wooga, one Ruby backend for a large game ran on about 80 to 200 application servers and handled about 5000 to 7000 requests per second.
- A new backend for a similarly complex game was built in Erlang by Paolo and Knut and now uses about 1 application server, with 2 or 3 servers for redundancy.
- The backend uses a stateful design where each player is represented by an actor inside the Erlang VM.
- Requests for a player go directly to that actor, so many requests are answered quickly without hitting the database.
- If one actor crashes, the others are not affected because there is no shared or global state.
- When a player stops playing, the actor saves the game state to persistent storage and terminates.
- The author says Erlang spread to more backends and smaller services at Wooga after that success.
- He recommends learning Erlang by starting a small project and using learnyousomeerlang.com rather than only reading books.
