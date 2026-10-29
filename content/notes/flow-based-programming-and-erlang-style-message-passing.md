---
title: "Flow-based programming and Erlang style message passing - A Biology-inspired idea of how they fit together"
date: '2015-06-26T17:50:34-03:00'
category: webclip
summary: 'The post compares Flow-based programming and Erlang/Elixir messaging, arguing that FBP suits heavy computation inside services, while Erlang fits control-plane communication across services and distributed systems.'
tags: ["flow-based-programming", "erlang", "elixir", "distributed-computing"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Flow-based programming and Erlang style message passing - A Biology-inspired idea of how they fit together | Bionics IT"
    url: "http://bionics.it/posts/flowbased-vs-erlang-message-passing?utm_campaign=elixir_radar_12&utm_medium=email&utm_source=RD+Station"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-06/bionics-it--flow-based-programming-and-erlang-style-message-passing.md"
    kind: repo
---

The author argues that Erlang/Elixir and Flow-based programming overlap, but are better at different tasks. He says Erlang/Elixir works well as a control plane or service-to-service messaging layer, while FBP fits the heavy computation side better.

## Reading notes

- Erlang and Elixir are presented as especially interesting because of the Erlang VM’s ability to use multiple CPUs and multiple computers for distributed computing.
- Flow-based programming is described as attractive for the same broad reason, since it runs things in parallel.
- The author notes that FBP and Erlang/Elixir seem similar at first because both involve separate processes communicating with each other.
- He points to challenges in mapping FBP onto Erlang/Elixir, including back-pressure, bounded buffers, mailbox routing, and extra copying.
- He says these differences make a direct implementation of FBP in Erlang/Elixir less straightforward.
- He also says Erlang can be slow for some computations, including a string-processing example in Elixir that he found slower than unoptimized Python.
- At the same time, he credits the Erlang VM with process isolation, fault tolerance, inspectability, and hot code reloading.
- From this, he suggests using Erlang for the control plane of a distributed system, while faster languages handle the actual computation.
- He uses biology as a model and compares the DNA-to-RNA-to-Protein chain to Flow-based programming.
- He compares cell-to-cell signaling to Erlang-style message passing.
- In his view, DNA-to-RNA-to-Protein is a high-performance internal processing chain, while cell-to-cell signaling is a looser signaling system between cells.
- He concludes that FBP is well suited for heavy lifting inside a microservice, while Erlang-style message passing is suited for communication between services.
- He suggests this combination might help with Erlang’s performance limits and FBP’s distributed robustness issues.
