---
title: "Building a WebAssembly-powered serverless platform"
date: '2022-06-02T09:57:55-03:00'
category: webclip
summary: 'The post shows how to embed Wasmtime in a Rust HTTP service, route requests to WebAssembly modules, return strings through WASI stdout, and pass parameters via environment variables.'
tags: ["webassembly", "wasmtime", "wasi", "serverless"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Building a WebAssembly-powered serverless platform"
    url: "https://blog.scottlogic.com/2022/04/16/wasm-faas.html"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2022-06/blog-scottlogic-com--building-a-webassembly-powered-serverless-platform.md"
    kind: repo
---

The article builds a bare-bones serverless platform around WebAssembly. It uses Wasmtime inside a Rust app, with Actix Web handling HTTP routing to `.wasm` modules. The first version returns integers from a `run` export, then the platform is extended to use WASI so modules can write strings to stdout and receive parameters through environment variables.

## Reading notes

- WebAssembly is presented as more useful outside the browser, as a standalone runtime used in projects such as Kubernetes, Istio, and Red Panda.
- Wasmtime is chosen because of its WASI support, and Rust is used because Wasmtime itself is written in Rust.
- A simple module exports `run` and returns `42`, and the Rust host loads the module, finds the export, and executes it.
- The serverless platform uses Actix Web to listen on `127.0.0.1:8080` and map the request path to a module name.
- Returning strings requires shared memory or another interface, because WebAssembly only passes integers directly.
- WASI is used as the language-agnostic way to handle output, with stdout serving as the response channel.
- The host builds a WASI context with stdout wired to a buffer, instantiates the module through a Wasmtime linker, and calls `_start`.
- The compiled module imports WASI functions such as `fd_write`, `proc_exit`, `environ_sizes_get`, and `environ_get`, which the linker resolves.
- For input parameters, the example uses query-string values as environment variables passed into the WASI context.
- A Rust Sudoku solver reads a `puzzle` environment variable, solves the grid, and prints the result line by line.
- The final platform is described as multi-language, lightweight, secure, and fast, with the sample Hello World function taking 19 ms end to end and Wasmtime accounting for 6 ms.
