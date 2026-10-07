---
title: "Elixir vs Ruby Showdown - Phoenix vs Rails"
date: '2015-01-16T20:25:58-03:00'
category: webclip
summary: 'The post compares Phoenix and Rails on the same routed, rendered request and reports much higher throughput for Phoenix, with lower CPU load and steadier latency in localhost and Heroku benchmarks.'
tags: ["phoenix", "rails", "benchmarking", "web-frameworks"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Elixir vs Ruby Showdown - Phoenix vs Rails"
    url: "http://www.littlelines.com/blog/2014/07/08/elixir-vs-ruby-showdown-phoenix-vs-rails/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-01/littlelines-com--elixir-vs-ruby-showdown-phoenix-vs-rails.md"
    kind: repo
---

The post compares Phoenix and Rails on the same web task: route matching, controller rendering, view rendering with partials, and returning the response. It says the setup isolates these pieces so throughput and latency can be compared on a more realistic framework workload.

The reported results favor Phoenix in both localhost and Heroku tests. On localhost, Phoenix reaches 10.63x more throughput and lower latency variation; on Heroku, it reaches 8.94x more throughput with 3.74x less CPU load, while Rails shows much higher latency and less consistent response times.

## Reading notes

- The comparison uses Phoenix 0.3.1 with Cowboy and Erlang 17.1 against Rails 4.0.4 with Puma and MRI Ruby 2.1.0.
- The benchmark measures request routing, controller action rendering, layout and view rendering, partial rendering, and response delivery.
- No view caching was used, and request logging was disabled in both apps.
- The localhost test reports 12,120.00 req/s for Phoenix and 1,140.53 req/s for Rails.
- The Heroku test reports 2,691.03 req/s for Phoenix and 301.36 req/s for Rails.
- The author says benchmarks are only a good idea of performance and should be measured against your own system.
- The conclusion claims Elixir combines Ruby-like productivity with Erlang concurrency and fault tolerance, while Phoenix still needs a stronger ecosystem to match Rails.
