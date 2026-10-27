---
title: "Elixir Application Design"
date: '2015-05-29T09:12:53-03:00'
category: webclip
summary: 'The post uses Cowboy and Mix to explore OTP application design, emphasizing process structure, supervisor setup, and the state kept by Mix.TasksServer and Mix.ProjectStack.'
tags: ["otp-application-design", "mix", "supervisor", "process-structure"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Elixir Application Design"
    url: "http://learningelixir.joekain.com/elixir-application-design/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-05/learningelixir-joekain-com--elixir-application-design.md"
    kind: repo
---

The post says the main challenge in learning OTP application design is understanding overall process structure. It points to talks from ElixirConf and to learnyousomeerlang.com as starting points, then uses Cowboy and Mix as examples for looking at real application trees.

## Reading notes

- The author had been finding basics of OTP, but not much introductory material on how to design an overall OTP application.
- Two ElixirConf talks convinced the author that process structure is the most important part of OTP application design.
- The author began reading Learn You Some Erlang chapters on OTP application design and also started reading Elixir and Erlang application code.
- Cowboy was chosen first because it is an Erlang project that has been around for years, and a simple sample app was run and inspected with the Erlang observer.
- The observer showed several running applications with their own process trees, including cowboy, cowboy_elixir_example, elixr, inets, kernel, and ranch.
- The author then focused on Mix because it had a smaller application structure that seemed easier to study.
- Mix’s process tree showed two leaf processes, Elixir.Mix.ProjectStack and Elixir.Mix.TaskServer, supervised by Elixir.Mix.Supervisor.
- Two unnamed processes at the root were identified through observer details as application_master:main_loop/2 and application_master:loop_it/4, which the author associates with starting the application and running its main loop.
- The Elixir.Mix.Supervisor process was seen running gen_server:loop/6, and the author notes that supervisor is implemented on top of gen_server.
- The Mix application structure in mix.exs defines Mix.Supervisor with a one-for-one restart strategy and two children.
- Mix.TasksServer is described as an Agent that maintains a HashSet of tasks.
- Mix.ProjectStack is described as an Agent that maintains a stack with push, pop, and peek operations.
- Peeking at the stack from iex showed configuration data for the sample app, and the author says these Agents keep useful state for Mix so it can look it up or update it as needed.
