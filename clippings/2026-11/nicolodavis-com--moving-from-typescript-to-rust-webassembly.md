---
url: "https://nicolodavis.com/blog/typescript-to-rust"
captured_at: "2026-11-16T04:41:43+00:00"
title: "Moving from TypeScript to Rust / WebAssembly"
domain: "nicolodavis-com"
---

I recently decided to switch the engine of [Boardgame Lab](https://boardgamelab.app/) from TypeScript to Rust. The application itself is an SPA written in Svelte. I only switched the logic that updates the game state to Rust. Here is a summary of my experience with the transition:

## Isomorphic Architecture

One of the advantages of using JavaScript or TypeScript is that you can run the same code on both client and server. For [Boardgame Lab](https://boardgamelab.app/), this means that the game state can be updated independently on both sides. This results in a lag-free experience on the client while still using the server as the authoritative source of data.

With [WebAssembly](https://webassembly.org/) taking off, you can get the same advantage writing Rust. Instead of pushing client-side code to the server, we push server-side code to the client by compiling Rust to WebAssembly.

This [Rollup](https://github.com/wasm-tool/rollup-plugin-rust) plugin allows you to import a _Cargo.toml_ file into your TypeScript codebase, allowing a seamless integration between Rust and TypeScript code. The dev experience is almost as smooth as writing TypeScript itself (for example, the browser refreshes automatically when you change a line of Rust code).

[wasm-bindgen](https://github.com/rustwasm/wasm-bindgen) facilitates serialization of Rust structs into JSON objects and vice-versa.

## Limitations of TypeScript

Coding in TypeScript has been a largely pleasant experience, but switching to Rust immediately brought to light some of the limitations of TypeScript.

#### Strict Typing

TypeScript is more of a type-hinter than a type-checker. It primarily ensures that you’re not accessing fields that you aren’t declaring via the type system (which is quite expressive). It also enables nicer autocomplete for your IDE.

However, it does not actually ensure that the data you are manipulating corresponds to the type that you have declared to represent it. For example, the data might contain **additional fields** or even **incorrect** values for declared types.

#### Data Validation

You have to write data validation code to ensure that you’re operating on correct data in TypeScript. You get this for free in Rust, which will throw an error if you parse data that doesn’t line up with the struct that is to hold it in memory.

#### Error Handling

Rust’s [pattern matching](https://doc.rust-lang.org/book/ch06-02-match.html) and [error handling](https://doc.rust-lang.org/book/ch09-02-recoverable-errors-with-result.html) make it easy to handle every code path that could result in an error, leading to very robust code.

This leads to a great degree of confidence that if it compiles, it’s probably not going to throw an error at runtime.

## Performance

#### WebAssembly is faster than JavaScript

The initial rewrite without any performance optimizations is already faster than the previous TypeScript codebase. This doesn’t matter too much yet, but [Boardgame Lab](https://boardgamelab.app/) will eventually ship with bots, so the performance will matter once game trees need to be searched.

#### The Rust server is leaner

The multiplayer server receives updates from clients via WebSockets and then:

*   Updates its copy of the game state.
*   Broadcasts the client update to other clients.

The previous server used [ws](https://github.com/websockets/ws), a popular library for NodeJS. The new version uses [Warp](https://github.com/seanmonstar/warp) (Rust), which uses less memory under the same load.

## Conclusion

Overall, I’m pretty happy with the switch. I haven’t really encountered much resistance from the borrow checker despite being fairly new to Rust (I come from a C++ background, so maybe that helps).

discussion on [Hacker News](https://news.ycombinator.com/item?id=23776514) | [Twitter](https://twitter.com/search?q=https%3A%2F%2Fnicolodavis.com%2Fblog%2Ftypescript-to-rust%2F)
