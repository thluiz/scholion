---
title: "Confreaks TV | ElixirConf 2016"
date: '2016-09-29T10:04:59+00:00'
category: webclip
summary: 'Archived Confreaks TV page listing 14 ElixirConf 2016 talks with short abstracts, covering Elixir tooling, OTP, Phoenix, metrics, distributed systems, and learning paths.'
tags: ["elixir", "phoenix", "otp", "conference-talks"]
has_commentary: false
generated_by: "openai/gpt-5.1"
sources:
  - title: "Confreaks TV | elixirconf2016"
    url: "https://web.archive.org/web/20160927192401id_/http://confreaks.tv:80/events/elixirconf2016?"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/web-archive-org--confreaks-tv-elixirconf2016-schedule-overview.md"
    kind: repo
---

Archived Confreaks TV event page for ElixirConf 2016, held August 31–September 2, 2016, listing 14 recorded presentations with dates, times, ratings, view counts, and abstracts. The talks span binary protocols, distributed process groups, debugging, production systems with Phoenix and OTP, real‑time mobile and hardware integrations, metrics and dashboards, distributed graph processing, strings and iolists, collaborative music tools, learning Elixir from a front‑end background, and new calendar types in Elixir 1.3.

## Reading notes

- Event page for ElixirConf 2016, dated August 31–September 2, 2016, with 14 available presentations and navigation to all events and other conference events.
- Session "Implementing Binary Protocols with Elixir" presents binary protocols like HTTP/2, HPACK, and DNS as efficient but complex, and proposes learning to implement them in Elixir using binary pattern matching, string and integer (de)encoding, binary data frames, tests extracted from RFCs, and an HPACK implementation.
- Talk "pg2 and You: Getting Distributed with Elixir" focuses on Erlang's pg2 module for distributed process groups, used by Phoenix's default PubSub adapter behind Channels, offering a tour of pg2 features, internals, and how similar functionality and other distributed Erlang primitives can be used from Elixir.
- "Code Spelunking for Knowledge and Profit" argues that reading others' code is key to improving as a programmer and frames Elixir as especially suited to code reading, with examples from popular libraries to show expert practices.
- "Debugging Techniques in Elixir" starts from printing to standard output as a first debugging step, then moves to using observer and other tools; it promises coverage of debugging and profiling, inspecting crash dumps, handling common failure causes, and understanding the concepts behind reports and observer.
- "Selling Food with Elixir" describes building a Phoenix‑powered API for online food orders and restaurant delivery over six months, using OTP services that tolerate flaky third‑party APIs and store outages, isolate failures, and scale with a growing restaurant chain.
- The food‑ordering talk also covers overall system architecture and OTP applications, using ETS and process state instead of only a database for real‑time restaurant availability, batched processing without external job queues using OTP concepts, and practical pitfalls discovered before production.
- "Phoenix Beyond the Browser: Realtime Applications with Phoenix and Swift" explores Elixir and Phoenix as a concurrent, fast, reliable backend for mobile apps, focusing on WebSockets and Phoenix Channels to build real‑time iOS apps and games in Swift with features like Presence.
- That real‑time mobile session includes a basic introduction to Swift, setting up an iOS app to communicate with Phoenix over WebSockets, and using Phoenix features (including Presence) to improve applications.
- "Building 'Learn to Touch Type' Glove with Elixir and Arduino" shares the process of creating a touch‑typing glove, from research and tool selection to designing flexible pressure sensors, wiring them to Arduino, reading sensor data into an Elixir server, and rendering the results in a browser.
- "Measuring Your Elixir Application" argues that applications cannot be optimized without measurement and notes that the Elixir/Erlang ecosystem already offers many options for metrics collection.
- The metrics talk describes building a metrics dashboard at Xerpa using InfluxDB for storage and Grafana for visualization, with non‑intrusive metrics collection in code using Elixir metaprogramming to simplify instrumentation.
- It outlines benefits of this setup, including analyzing application evolution over time with InfluxDB’s query language and tricks to derive business value, and claims teams can operate without New Relic when using such tooling.
- "Edgelixir: Distributed Graph Processing in Elixir" introduces distributed graph processing systems as important tools, presents graph structures as a way to solve many problems, and shows how Elixir features like OTP, macros, and functional programming can simplify writing a distributed Pregel‑style graph framework.
- The keynote entry is listed with time, date, rating "Everyone", and posting date but has no abstract text on this page.
- "String Theory" addresses Elixir strings and iolists, asking why strings are binaries, how binary contents relate to Unicode support, and what iolists are and how they help efficient template rendering.
- The string talk promises to teach the relationship between bitstrings, binaries, and strings; correct comparison and dissection of UTF‑8 strings; and efficient construction of string output for files or sockets, framed as a journey into the bits and bytes behind these structures.
- "Collaborative Music with Elm and Phoenix" walks through designing a collaborative music composition environment with an Elm frontend and a Phoenix Channels backend, showing how Phoenix building blocks enable collaboration and persistence.
- That collaborative music session explains how to map Elm frontend data structures and actions into Elixir for persistence and data transfer.
- "From Front End to Full Stack with Elixir and Phoenix" recounts the speaker's path from self‑taught designer to front‑end developer, then to full‑stack development using a well‑tested Phoenix API, and describes learning to think in the "Elixir Way".
- This beginner‑oriented talk discusses resisting the urge to carry over OOP habits into Elixir, leveraging Plugs, approaches to testing, and other lessons learned.
- "The New Calendar Types in Elixir 1.3" presents the new built‑in date and time types added in Elixir 1.3, explaining design considerations and how they improve data and software quality.
- The calendar talk addresses when to choose NaiveDateTime versus DateTime, and suggests best practices for using the new types with Ecto, Phoenix, and Elixir in general.
