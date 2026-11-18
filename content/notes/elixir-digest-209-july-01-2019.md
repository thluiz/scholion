---
title: "Elixir Digest #209 for July 01, 2019"
date: '2019-07-06T09:27:09+00:00'
category: webclip
summary: 'Digest edition with Elixir v1.9 releases feature, Phoenix Universal/App Links, BEAM–Rust integration, Phoenix LiveView live_link, and property-based testing for stats.'
tags: ["elixir", "phoenix", "beam", "testing"]
has_commentary: false
generated_by: "openai/gpt-5.1"
sources:
  - title: "Elixir Digest #209 for July 01, 2019"
    url: "https://web.archive.org/web/20190716230130id_/https://elixirdigest.net/digests/209"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/web-archive-org--elixir-digest-209-july-01-2019.md"
    kind: repo
---

This Elixir Digest issue highlights a Manning promotion on Elixir books and several posts from the community. Topics range from serving iOS Universal Links and Android App Links with Phoenix, to the new releases feature in Elixir v1.9, to combining BEAM with Rust for performance and hardware access, Phoenix LiveView URL handling, and applying property-based testing to a statistics calculation.

## Reading notes

- Manning Publications offers 40% off all orders, including Elixir books, aiming to support developers from varied backgrounds in improving with Phoenix, Elixir syntax, and overall Elixir skills.
- One article explains that hosting server-side files for iOS Universal Links and Android App Links can be handled straightforwardly in Phoenix, even though deep links themselves can be complex.
- Elixir v1.9 introduces releases as its main new feature, described as a self-contained directory bundling application code, dependencies, and the Erlang VM and runtime for deployment.
- The description of releases notes they can be packaged and deployed as long as the target system matches the OS distribution and version used when running the mix release command.
- A post on BEAM and Rust states that BEAM is known for fault tolerance, solid performance, and memory efficiency, while acknowledging that some use cases require going beyond BEAM’s limits.
- That same piece raises scenarios such as interfacing directly with hardware or making specific parts of an application as fast as possible as motivations for combining BEAM with Rust.
- Another article about Phoenix LiveView discusses using live_link after previously covering live_redirect, focusing on changing the URL without changing the location or refreshing the page.
- The LiveView article notes that keeping the URL in sync with the page state helps users bookmark or share the current state more easily.
- A post on property-based testing recalls the author’s excitement on first encountering the idea in Clojure but notes difficulty applying it beyond simple reversible operations like encode–decode equality.
- The same piece mentions that the properties the author previously devised often felt too weak to reveal bugs, motivating the example based on a statistics calculation.
