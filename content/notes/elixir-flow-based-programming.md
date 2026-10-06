---
title: "Elixir Flow-Based Programming"
date: '2015-06-05T09:34:48-03:00'
category: webclip
summary: 'The author explores implementing flow-based programming in Elixir by using GenServer and Erlang digraphs, then adds initial values, component ports, and multiple processes per component to exploit concurrency.'
tags: ["elixir", "flow-based-programming", "genserver", "concurrency"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Elixir Flow-Based Programming"
    url: "http://www.elixirfbp.org/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-06/elixirfbp-org--elixir-flow-based-programming.md"
    kind: repo
---

The post series describes an Elixir implementation of flow-based programming built around a GenServer-backed graph. The graph stores component metadata, ports, edges, and initial values, and later supports starting networks that run components as Elixir processes.

## Reading notes

- The graph is modeled as a persistent process using GenServer and Erlang digraph.
- The graph structure stores id, name, library, main, description, and digraph.
- External API functions call the GenServer, and callback functions handle graph operations.
- Clearing a graph deletes its vertices and edges from the internal digraph.
- Nodes and edges can be added and removed through graph callbacks.
- The node label was expanded to store component, inports, outports, and metadata.
- Component port definitions are read at runtime from the component module.
- Initial values are attached to target ports and later sent to target processes.
- Components are modeled as Elixir processes that receive messages on input ports.
- The author sketches an Elixir version of Math.Add with receive-based looping.
- The implementation uses a graph protocol inspired by NoFlo.
- A Citibike example wires ticker, map, HTTP fetch, unpack, filter, and output components.
- Streamtools-style JSON responses are converted into Elixir maps and lists.
- A multi-process component mode is added by specifying number_of_processes in node metadata.
- IPs are dispatched round-robin across spawned processes, with no guarantee of order.
- The timing test shows faster execution as more faker processes are assigned.
