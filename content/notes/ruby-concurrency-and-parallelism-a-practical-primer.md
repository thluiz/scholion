---
title: "Ruby Concurrency and Parallelism: A Practical Primer"
date: '2015-02-10T10:22:35-03:00'
category: webclip
summary: 'The article explains the difference between concurrency and parallelism in Ruby and compares forking, threading, thread pools, and background jobs, with performance and resource tradeoffs.'
tags: ["ruby", "concurrency", "parallelism", "background-jobs"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Ruby Concurrency and Parallelism: A Practical Primer"
    url: "http://www.toptal.com/ruby/ruby-concurrency-and-parallelism-a-practical-primer"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-02/toptal-com--ruby-concurrency-and-parallelism-a-practical-primer.md"
    kind: repo
---

The article separates concurrency from parallelism and uses a mailer example to compare Ruby approaches for handling many tasks. It shows that forking can speed up CPU-heavy work, while MRI threads offer little benefit because of the GIL, though they still help with IO-heavy tasks. It also notes that JRuby and Rubinius can support real parallel threading.

## Reading notes

- Concurrency means tasks overlap in time; parallelism means tasks run at the same time.
- The article uses a Mailer example with a Fibonacci function to make each request CPU-intensive.
- A benchmark of 100 synchronous deliveries is used as the baseline.
- Forking multiple processes makes the example much faster, but it can consume a lot of memory and adds process-communication complexity.
- In MRI, threads do not improve CPU-bound performance much because of the Global Interpreter Lock.
- Threads can still be useful for IO-heavy work.
- JRuby and Rubinius are presented as alternatives that support real parallel threading.
- Creating too many threads can exhaust resources.
- Thread pools reuse a fixed set of threads and use a Queue to hand out jobs.
- Celluloid is presented as a simpler way to build concurrent Ruby programs with pooling.
- Background jobs are another option, with Sidekiq, Resque, Delayed Job, Beanstalkd, and Sucker Punch mentioned as examples.
- The conclusion says the right choice depends on the application, operating environment, and requirements.
