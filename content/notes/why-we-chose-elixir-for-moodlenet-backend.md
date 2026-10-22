---
title: "Why did we choose Elixir for the backend development of MoodleNet?"
date: '2020-09-07T16:48:24-03:00'
category: webclip
summary: 'The post says MoodleNet chose Elixir and Phoenix for backend development because of performance, scalability, concurrency, reliability, simplicity, flexibility, correctness, and developer productivity.'
tags: ["elixir", "phoenix-framework", "backend-development"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Why did we choose Elixir for the backend development of MoodleNet? – MoodleNet"
    url: "https://blog.moodle.net/2018/elixir-choice/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2020-09/blog-moodle-net--why-we-chose-elixir-for-moodlenet-backend.md"
    kind: repo
---

MoodleNet says it chose Elixir for backend development after research into frontend and backend languages. The post points to a detailed wiki page and summarizes the main benefits of Elixir and Phoenix for the project.

## Reading notes

- The team decided to use Elixir for backend development after Mayel researched languages and compared options.
- Phoenix is presented as faster than Rails, PHP, and Python in one benchmark and more consistent under load.
- The Erlang VM is described as a good fit for scaling by adding servers and for concurrency on multi-core CPUs.
- The post says developer time matters as much as server performance, so productivity and programmer wellbeing were part of the choice.
- Elixir is described as reliable because it runs on the Erlang VM, which has long been used in highly reliable systems.
- The language is presented as simple for running many processes, flexible for building applications other frameworks cannot support, and correct because Ecto works with database constraints and user-facing error messages.
- The downsides mentioned are Elixir’s relative newness and the difficulty of finding developers, though the team says that second problem is already solved for MoodleNet.
