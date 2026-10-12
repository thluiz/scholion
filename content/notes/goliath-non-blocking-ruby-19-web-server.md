---
title: "Goliath: Non-blocking, Ruby 1.9 Web Server"
date: '2014-07-07T15:23:20-03:00'
category: webclip
summary: 'Goliath is presented as an asynchronous Ruby 1.9 app server and lightweight framework built on Rack, fibers, and EventMachine, with a synchronous-looking API, middleware support, and performance benchmarks across Ruby runtimes.'
tags: ["ruby", "asynchronous-processing", "web-server", "eventmachine"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Goliath: Non-blocking, Ruby 1.9 Web Server - igvita.com"
    url: "https://www.igvita.com/2011/03/08/goliath-non-blocking-ruby-19-web-server/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2014-07/igvita-com--goliath-non-blocking-ruby-19-web-server.md"
    kind: repo
---

Goliath is introduced as a fully asynchronous Ruby 1.9 app server and lightweight framework built on Rack. The post says it aims to combine asynchronous processing, middleware support, simple configuration, high performance, and readable, maintainable code.

It explains that fibers let asynchronous code pause and resume while keeping a synchronous-looking API, so no callbacks are needed in the example. The post also gives performance numbers for MRI, JRuby, and Rubinius, notes production use at PostRank, and points to streaming, uploads, proxying, and other examples.

## Reading notes

- Goliath is described as both an app server and a lightweight framework, not a direct substitute for every other server.
- It is built around Rack and is designed for fully asynchronous processing.
- Fibers are used to keep asynchronous code readable while preserving a synchronous API feel.
- The example shows a GitHub proxy using middleware for params, JSON formatting, response negotiation, and validation.
- The post says asynchronous HTTP requests are paused and resumed automatically, without callbacks.
- It reports MRI Ruby 1.9.2 as the fastest current runtime in the benchmarks shown.
- JRuby is said to be slower at the time because fibers map to native Java threads.
- Rubinius performance is described as variable and still open to optimization.
- Goliath is said to have run in production at PostRank for over a year with sustained traffic and no memory leaks or restarts.
- The post says it supports HTTP keep-alive, request pipelining, and real-time streaming APIs.
