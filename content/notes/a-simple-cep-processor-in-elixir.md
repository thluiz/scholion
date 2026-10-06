---
title: "A Simple CEP Processor in Elixir"
date: '2015-05-26T10:51:14-03:00'
category: webclip
summary: 'The post shows a simple CEP setup in Elixir that simulates stock ticks, routes them through a broker and worker factory, keeps a timed window per symbol, and prints hourly averages through a sink.'
tags: ["elixir", "cep", "genevent", "erlang"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "A Simple CEP Processor in Elixir"
    url: "http://blog.jonharrington.org/a-simple-cep-processor-in-elixir/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-05/blog-jonharrington-org--a-simple-cep-processor-in-elixir.md"
    kind: repo
---

The post sketches a CEP processor in Elixir built from GenEvent servers, GenServer processes, and a timed window data structure from an earlier post. It simulates stock quotes, routes each tick by symbol, and has workers compute and emit hourly averages.

## Reading notes

- CEP is presented as systems that process streams of events.
- The application simulates real-time stock feed data with random ticks instead of using a live feed.
- One GenEvent server handles input ticks and another handles output average events.
- The broker looks up the process registered for a stock symbol and forwards the tick to that worker when it exists.
- If no worker is registered for a symbol, the broker sends the event to the worker factory.
- The worker factory starts a new worker process for a tick event and registers it under the symbol.
- Each worker keeps a timed window, updates it on every tick, and sends the 60 minute average to the output GenEvent server.
- The source module sends a tick event after each interval period.
- The sink module prints the symbol, timestamp, and average, and the post says a real sink could store data in a database or file.
- The application module wires the processes together with two GenEvent servers, the factory, the broker, and three source processes.
- The post says the setup lets producers and consumers be decoupled and makes it easier to add more tick consumers later.
