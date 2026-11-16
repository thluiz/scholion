---
title: "Introduction to Akka.Streams"
date: '2020-02-22T12:11:49+00:00'
category: webclip
summary: 'Akka.Streams is a type-safe, resource-safe streaming library on top of Akka.NET. The post explains declarative stages, batching, backpressure, materialization, graphs, and how it compares with Rx.NET and TPL Dataflow.'
tags: ["akka-streams", "backpressure", "materialization", "tpl-dataflow"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Introduction to Akka.Streams"
    url: "https://petabridge.com/blog/introduction-akkadotnet-streams"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/petabridge-com--introduction-to-akka-streams.md"
    kind: repo
---

Akka.Streams is presented as a library on top of Akka.NET for consuming and processing potentially infinite data streams in a type-safe and resource-safe way. The post shows how declarative stages can parse messages, write them to a database, and switch to batching with GroupedWithin when one-by-one persistence becomes a bottleneck.

## Reading notes

- Akka.Streams is built on Akka.NET and is meant for consuming and processing potentially infinite streams of data in a type-safe and resource-safe way.
- A simple pipeline can read documents from a queue, parse them, insert them into a database, and print each inserted item.
- One advantage of the API is its declarative syntax, which makes it easy to change a stream from single-item inserts to batched inserts.
- GroupedWithin collects items until it reaches a size limit or a time limit, whichever comes first.
- The library borrows ideas from Rx.NET but adapts them to graph-based workflows and server-side systems.
- Backpressure is central to Akka.Streams, letting consumers control the rate at which producers send more data.
- Akka.Streams can interoperate with Rx.NET through the integration with observables.
- Streams are described as higher-level Akka.NET programs made from modular sources, flows, and sinks.
- The post says this lowers the amount of code needed for many routine streaming problems and fits common connectors such as Kafka, Azure Queues, and RabbitMQ.
- Materialization is required to run a stream because the graph is only a blueprint until a materializer evaluates it.
- Materializers can support different execution tradeoffs, and they enable optimizations before graph execution.
- Fusing is described as an optimization that combines sequential synchronous stages to reduce overhead.
- The author compares materializers to the Free Monad pattern and to an Interpreter, and notes a similarity with IQueryable.
- Graphs have materialized values, so the result of a stream can be something other than a collection, such as a queue or an awaitable.
- Source<T, TValue> carries both the element type and the materialized value type, and NotUsed is used when a stage has no meaningful materialized value.
- Keep combinators let you preserve one or both materialized values from connected stages.
- Akka.Streams can model full graphs, including cycles, not only linear pipelines.
- Every shape has a fixed number of inlets and outlets, and all ports must be connected before materialization.
- A source has only outlets, a sink has only inlets, a flow has both, and a closed shape has neither exposed.
- The Graph DSL is used to wire stages together into more complex workflows.
- The example graph partitions cached and uncached items, sends duplicates to one sink, and sends uncached items through a cache update path to another sink.
- The post says this structure could represent systems such as fraud detection, alerting, or batched downstream processing.
- Akka.Streams is presented as useful for Akka.Persistence journals, TCP servers, and third-party integrations through Alpakka.
- The appendix contrasts Akka.Streams with TPL Dataflow, describing Akka.Streams as more declarative while TPL Dataflow is more imperative.
- It also notes that some stream operations, such as sliding windows, are easier in Akka.Streams, and that the library includes many stages and connectors.
- The post ends by mentioning StreamRefs for propagating streams across node boundaries.
