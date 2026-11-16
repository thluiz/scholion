---
title: "Moving from TypeScript to Rust / WebAssembly"
date: '2026-11-16T04:41:43+00:00'
category: webclip
summary: 'The author moved Boardgame Lab’s game-state logic from TypeScript to Rust and WebAssembly, citing shared client-server code, stronger validation and error handling, faster execution, and leaner server memory use.'
tags: ["typescript", "rust", "webassembly", "performance"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Moving from TypeScript to Rust / WebAssembly"
    url: "https://nicolodavis.com/blog/typescript-to-rust"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/nicolodavis-com--moving-from-typescript-to-rust-webassembly.md"
    kind: repo
---

The author switched only the game-state update logic in Boardgame Lab from TypeScript to Rust, while the app itself remains a Svelte SPA. He describes the change as a way to keep client and server logic aligned and to compile Rust to WebAssembly for client-side use.

## Reading notes

- Boardgame Lab moved its game-state update logic from TypeScript to Rust, while the application itself stayed a Svelte single-page app.
- JavaScript and TypeScript let the same code run on client and server, which gives Boardgame Lab a low-latency client and a server that remains the authoritative data source.
- WebAssembly lets the same advantage be reached with Rust by compiling server-side code for the client.
- A Rollup Rust plugin can import a Cargo.toml file into a TypeScript codebase, and the development flow stays close to TypeScript, including automatic browser refresh after Rust changes.
- wasm-bindgen helps serialize Rust structs to JSON and back.
- TypeScript is described as a strong type-hinter, but it does not ensure that the runtime data really matches the declared type.
- In TypeScript, data validation must be written manually to guard against extra fields or incorrect values.
- Rust is presented as handling validation through parsing, with errors raised when data does not match the struct in memory.
- Rust pattern matching and error handling make it easier to cover error paths and compile with more confidence that runtime errors will not appear.
- The first WebAssembly rewrite was already faster than the previous TypeScript version.
- The author expects performance to matter more later when bots need to search game trees.
- The Rust multiplayer server uses Warp instead of ws and uses less memory under the same load.
- The author says the switch felt good overall and reports little resistance from the borrow checker, possibly helped by a C++ background.
