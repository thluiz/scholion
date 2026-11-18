---
title: "Elixir and Rust is a good mix"
date: '2025-04-21T19:36:37+00:00'
category: webclip
summary: 'Guide to using Rust with Elixir via Rustler: creating NIFs, adding an image processing function, being BEAM-friendly with Dirty NIFs, and deploying on Fly.io with Docker.'
tags: ["elixir", "rust", "nif", "deployment"]
has_commentary: false
generated_by: "openai/gpt-5.1"
sources:
  - title: "Elixir and Rust is a good mix"
    url: "https://fly.io/phoenix-files/elixir-and-rust-is-a-good-mix"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/fly-io--elixir-and-rust-is-a-good-mix.md"
    kind: repo
---

This post explains how to integrate Rust into an existing Elixir application using Rustler, focusing on creating NIFs, wiring them into Elixir, extending them for image processing, handling CPU-heavy work safely on the BEAM, and deploying the result with Docker on Fly.io.

## Reading notes

- The motivating problem is a CPU‑intensive or system‑level task, such as image processing, where suitable Elixir/Hex libraries may not exist but there is a strong Rust ecosystem.
- The example assumes a Rust `image` crate is available while the application codebase is already written in Elixir and the team is not very familiar with Rust.
- Rustler is introduced as a library that makes using Rust and its package ecosystem from Elixir straightforward.
- To get started, Rustler is added to `mix.exs` as `{:rustler, "~> 0.38.0"}` and fetched with `mix deps.get`.
- Running `mix rustler.new` generates an empty Rust project under `native/`, including Cargo configuration, source file, and a README with setup instructions.
- An Elixir module `MyApp.RustImage` is created using `use Rustler, otp_app: :my_app, crate: "rust_image"`, with a stub `add/2` function that raises `:nif_not_loaded` until the NIF is loaded.
- The Rust side defines an `add/2` function annotated with `#[rustler::nif]` and initializes Rustler with `rustler::init!("Elixir.MyApp.RustImage");` so the BEAM can attach the NIFs to the Elixir module.
- NIFs (Native Implemented Functions) are described as the BEAM’s way to call native code directly, usually requiring extensive boilerplate, manual memory management, and careful error handling when implemented via C.
- Rustler hides most of the usual NIF boilerplate, relying on Rust’s safety guarantees, in contrast to the more complex steps shown in the Erlang NIF tutorial.
- Running `iex -S mix` and calling `MyApp.RustImage.add(100, 20)` demonstrates that the Rust NIF is compiled by Cargo and invoked successfully from Elixir.
- If Rust is missing on the machine, an error appears and the reader is directed to install Rust via the standard `rustup` process.
- Rustler integrates with the Elixir workflow by automatically recompiling when Rust source changes; editing `lib.rs`, saving, then calling `r(MyApp.RustImage)` in `iex` triggers a rebuild and reload.
- The dynamic reload example modifies `add/2` to add one extra to the sum, and a subsequent call in `iex` shows the updated behavior.
- To move from a toy example to image processing, the Rust crate `image = "0.25.10"` is added to `Cargo.toml` alongside `rustler`.
- A new Rust NIF `jpg/3` is implemented that takes input and output paths plus a quality integer, opens the input image via `ImageReader`, decodes it, and writes a JPEG using `JpegEncoder`.
- The `jpg/3` function returns a `Result<String, String>` and on success returns the output path wrapped in `Ok`, providing a success value to Elixir.
- The Elixir module should be updated to include a stub for `jpg/3` similar to the earlier `add/2` stub, though the exact code is left to the reader.
- Calling `MyApp.RustImage.jpg("input.png", "output.jpeg", 75)` from `iex` yields a successful `{:ok, "output.jpeg"}` result and converts the image to JPEG with the given quality.
- The post highlights that CPU‑heavy work might run quickly in development but can behave differently in production environments with shared CPU and RAM.
- It explains that BEAM runs NIF code directly and cannot preempt Rust code in the middle of execution, which can interfere with the scheduler’s ability to manage millions of processes.
- To avoid blocking the scheduler with long‑running NIFs, the Rustler macro is updated from `#[rustler::nif]` to `#[rustler::nif(schedule = "DirtyCpu")]`.
- Using `schedule = "DirtyCpu"` marks the function as a Dirty NIF, letting BEAM and Rustler schedule it in a way that avoids blocking the rest of the system.
- The post notes that Dirty NIFs are more difficult to manage when working directly with C NIFs, and Rustler simplifies this significantly.
- For deployment on Fly.io with Docker, additional steps are needed so that the Docker build environment can compile the Rust code.
- A new Docker build stage based on `rust:1.97.1` is added, which installs build dependencies like `build-essential` and `git`, sets the working directory to `/app`, copies the `native/rust_images` directory, and runs `cargo rustc --release`.
- After the Rust build stage, the Elixir build stage compiles assets with `mix assets.deploy` and then copies the compiled Rust shared library into `priv/native` using `COPY --from=rust /app/target/release/librust_images.so priv/native/librust_images.so`.
- The Elixir release is compiled after the Rust library is in place, ensuring the NIF binary is available at build time.
- In `config/prod.exs`, configuration is added for `MyApp.RustImage` specifying the crate name, setting `skip_compilation?: true`, and telling Rustler to load the library from `{:my_app, "priv/native/librust_image"}`.
- This setup builds the Rust library in its own Docker builder context, allowing it to run in parallel with other steps and benefit from Docker build caching.
- Skipping compilation at runtime and loading the prebuilt shared object ensures deployment uses the binary produced during the Docker build.
- Once the Dockerfile and configuration are in place, deployment proceeds with `fly deploy`.
- The post closes noting that NIFs plus Rust open access to the broader Rust ecosystem from Elixir, citing examples like scientific data handling with `explorer` and WebRTC integration with `specter`.
- A note explains that the post was updated in August 2026 to keep Elixir and JS dependencies current so that examples remain compatible and to reduce the influence of outdated blog posts on automated tooling.
- The article ends by reiterating that Fly.io provides an easy way to run Phoenix LiveView applications near users and links to documentation for deploying a Phoenix app.
