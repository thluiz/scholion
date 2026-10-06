---
title: "Ruby concurrency explained"
date: '2012-06-04T12:56:46-03:00'
category: webclip
summary: 'The article explains concurrency in Ruby through threads, multiple processes, fibers, and non-blocking I/O, and argues that each approach trades simplicity, safety, memory use, and throughput.'
tags: ["ruby", "concurrency", "threads", "non-blocking-io"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Ruby concurrency explainined | Matt Aimonetti"
    url: "http://merbist.com/2011/02/22/concurrency-in-ruby-explained/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2012-06/merbist-com--ruby-concurrency-explained-matt-aimonetti.md"
    kind: repo
---

The article frames concurrency as a throughput problem: getting code to do more work in less time. It contrasts different ways to achieve that in Ruby and shows why the choice depends on the runtime, the workload, and the tradeoffs between shared state, memory use, and blocking operations.

## Reading notes

- Concurrency is described as multitasking, with the goal of letting code handle multiple different things at the same time.
- The article uses a Twitter client and a web server to show why blocking the main loop hurts user interaction and request handling.
- It compares language-level approaches such as Java-style threads, PHP-style process-per-request, and the actor model used by Erlang and Scala.
- In Ruby 1.9, native threads exist, but the Global Interpreter Lock limits true parallel execution in MRI while still helping with data integrity and some C extensions.
- Other Ruby implementations such as JRuby, Rubinius, and MacRuby are mentioned as alternatives without a GIL.
- Multiple processes and forking are presented as a common Ruby solution, especially for Rails servers, because copy-on-write can reduce memory overhead.
- The article notes that forking is useful for background jobs such as Resque, where process isolation helps when jobs leak memory or hang.
- Fibers are described as lightweight, programmer-scheduled units that can pause and resume, but they still do not bypass blocking I/O inside a thread.
- The reactor pattern is presented as the way to avoid blocking I/O by delegating work to an external service and resuming code through callbacks.
- EventMachine, Thin, and Node.js are cited as examples of this non-blocking approach in practice.
- The article closes by saying high concurrency in Ruby is possible, but easier tools and simpler APIs would make it less painful to write concurrent code.
