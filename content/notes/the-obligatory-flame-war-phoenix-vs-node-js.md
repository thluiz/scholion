---
title: "The Obligatory “Flame War” Phoenix vs Node.js"
date: '2016-01-10T07:39:41-03:00'
category: webclip
summary: 'The post compares Node.js and Phoenix with simple Siege benchmarks, showing Node doing fine on I/O-bound requests but collapsing when each request blocks for one second, while Phoenix keeps handling the load.'
tags: ["node-js", "phoenix", "benchmark", "elixir"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "The Obligatory &quot;Flame War&quot; Phoenix vs Node.js | AkitaOnRails.com"
    url: "http://www.akitaonrails.com/2015/12/03/the-obligatory-flame-war-phoenix-vs-node-js"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2016-01/akitaonrails-com--the-obligatory-flame-war-phoenix-vs-node-js.md"
    kind: repo
---

The post compares a tiny Node.js + Express app with a small Phoenix app using Siege. In the first test, Node finishes faster on an I/O-bound workload, but the author says that result is not a fair trial and mainly shows that Node’s async model handles that kind of case well.

## Reading notes

- Node.js + Express is set up as a simple hello world with one title and one paragraph.
- Phoenix is bootstrapped as a bare-bones project with one extra router endpoint that renders the same content.
- The first benchmark uses 200 concurrent connections and 8 requests each, for 1,600 requests total.
- In that I/O-bound test, Node.js has the lower total time.
- The author says a single Node.js process uses one real OS thread, while Elixir can reach all 8 CPU cores on the machine.
- Phoenix logs show processing times in microseconds instead of milliseconds.
- The second benchmark adds a blocking one-second sleep to both projects.
- The post says Node.js is easy to block because JavaScript runs in a single-threaded event loop until it yields control.
- With 10 requests that each sleep for 1 second, Node.js takes about 10 seconds overall because the requests run one after another.
- Phoenix handles the blocking workload more easily because its schedulers can suspend processes and share resources across cores.
- The author says adding more requests and connections still stays fast in Phoenix.
- A side note says Node is not easy to scale across multiple nodes, and that running several Node processes only helps by splitting the blocking work.
- The post points to Erlang as the basis for distributed systems such as ejabberd and RabbitMQ.
- It says Elixir makes it simple for one node to discover other nodes and exchange messages with them.
