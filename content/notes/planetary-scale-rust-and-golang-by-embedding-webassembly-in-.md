---
title: "Planetary Scale Rust and Golang by embedding WebAssembly in Elixir"
date: '2020-12-10T10:26:08-03:00'
category: webclip
summary: 'The post describes Assemblex, a toy Elixir platform for deploying and running WebAssembly binaries across nodes, with hot reloads, supervision, and benchmarked execution overhead.'
tags: ["webassembly", "elixir", "distributed-systems", "benchmarking"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Planetary Scale Rust and Golang by embedding WebAssembly in Elixir - DEV Community 👩‍💻👨‍💻"
    url: "https://dev.to/hansonkd/planetary-scale-rust-and-golang-by-embedding-webassembly-in-elixir-45cm"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2020-12/dev-to--planetary-scale-rust-and-golang-by-embedding-webassembly-in-.md"
    kind: repo
---

The post presents Assemblex, a toy serverless platform built in Elixir for deploying WebAssembly binaries across multiple nodes and calling guest functions through URLs. It combines WebAssembly sandboxing with Elixir’s fault tolerance, supervision, and distributed messaging, and it uses Lasp for eventually consistent deployment state and Phoenix for HTTP access.

## Reading notes

- The project investigates the overhead of embedding WebAssembly inside Elixir by letting users upload a .wasm file and call a function from it.
- Assemblex supports Rust, Golang, AssemblyScript, and Zig through the WaPC protocol.
- The runtime was changed from synchronous execution to an asynchronous scheduler so it could fit Elixir’s concurrent request model better.
- Lasp provides an eventually consistent in-memory CRDT store, node auto-configuration, and network composition through partisan.
- Deployment works by storing the wasm binary and version in Lasp, then using a supervisor task to hot swap the running executor when the version changes.
- Execution pulls a process from a registry and starts a new WebAssembly VM to run the guest function and return bytes.
- A bounded sync channel keeps a pool of warmed VMs ready, creating new ones on demand and discarding extras when idle.
- A GenServer handles host callbacks so wasm code can call back into Elixir functions.
- Benchmarks compare Elixir native calls with WebAssembly calls that read from Redis three times and concatenate the results.
- The benchmarks use two pool sizes, 100 and 1, to compare the effect of pre-warmed instances.
- The results suggest WebAssembly can compete with Elixir when the pool is sized well, though memory use remains a concern.
- The next steps mentioned are WASI support, preemptive yields, memory limits for guest VMs, and distributed supervision with hord.
