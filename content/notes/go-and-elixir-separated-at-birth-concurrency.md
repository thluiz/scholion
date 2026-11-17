---
title: "Go and Elixir - Separated at Birth?"
date: '2026-11-17T15:05:41+00:00'
category: webclip
summary: 'The text compares Elixir’s actor-based concurrency with Go’s goroutines, links this model to hardware limits after Moore’s law, and questions Ruby’s future without strong concurrency support.'
tags: ["concurrency", "elixir", "go", "ruby"]
has_commentary: false
generated_by: "openai/gpt-5.1"
sources:
  - title: "Go and Elixir - Separated at Birth?"
    url: "https://devonestes.com/go-and-elixir-separated-at-birth"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/devonestes-com--go-and-elixir-separated-at-birth-concurrency.md"
    kind: repo
---

The author compares Elixir (and Erlang) to Go in how they handle concurrency, noting that both use patterns where isolated processes communicate via messages, akin to the Actor model. After reflecting on an article about the end of performance gains from Moore’s law and the shift to multi-core processors, they argue that efficient algorithms and good resource management are becoming crucial. In this context, they express doubts about Ruby’s long-term viability because it is interpreted and lacks strong support for true concurrency, suggesting compiled languages and more robust concurrency primitives as a better path.

## Reading notes

- Elixir and Erlang handle concurrency with many small processes that each have a single responsibility, following the Actor model.
- The author finds process communication in Elixir and Erlang particularly easy compared to other environments.
- Go also makes inter-process (goroutine) communication relatively easy, though the author finds it less straightforward than in Elixir.
- In Go, concurrency is based on goroutines, and communication between them or with the main process happens via channels.
- Go’s concurrency philosophy is summarized as sharing state by communicating instead of communicating through shared state.
- The author realizes that Go’s approach is essentially the same pattern used in Elixir for concurrency.
- They mention having heard that Scala and Clojure use similar patterns to manage concurrency effectively.
- The author wonders if there is a growing consensus in the programming community around this kind of concurrency model.
- After reading a Nature article, the author notes that CPU clock speeds have plateaued due to heat and power constraints.
- Processor performance has been improved recently by adding more cores instead of making individual cores faster.
- The author describes this multi-core shift as a workaround that is also approaching its limits.
- They argue that future software must rely on efficient algorithms and careful resource management rather than expecting ever-faster hardware.
- The author questions Ruby’s place in this future, given performance and concurrency demands.
- They point out that Ruby, as an interpreted language, is significantly slower than compiled languages from the start.
- The author sees Ruby’s lack of true concurrency support as a more serious long-term problem than interpretation overhead.
- They consider that MRI Ruby might be replaced in practice by JRuby, which offers true threading.
- Threaded programs are described as prone to difficult and subtle bugs, which complicates relying on threads alone.
- The author suggests that using a compiled language is likely more efficient over time than sticking with JRuby in its current form.
- They express pessimism about Ruby’s future unless it gains much stronger concurrency primitives.
