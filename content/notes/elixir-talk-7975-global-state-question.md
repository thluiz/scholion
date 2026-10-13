---
title: "[elixir-talk:7975] A question about global state"
date: '2015-04-10T10:04:44-03:00'
category: webclip
summary: 'The thread explains that Elixir libraries can keep startup-derived state in a supervised process or ETS, and that users should start it through the application rather than manually.'
tags: ["elixir", "global-state", "agent", "supervision"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "[elixir-talk:7975] A question about global state - th.luiz@gmail.com - Gmail"
    url: "https://mail.google.com/mail/u/0/?pli=1#inbox/14ca02f0d6fe1860"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-04/mail-google-com--elixir-talk-7975-global-state-question.md"
    kind: repo
---

The thread asks how to keep startup-derived terminal capability state in an Elixir library without checking environment variables on every call. The answers say processes are cheap, so an Agent is fine, and the process can be started by the library's application instead of by users.

José Valim describes creating a Mix application with a supervisor, starting the Agent as a child, and storing the state behind explicit functions. Robert Virding adds that ETS can hold static data at startup or be managed by a process if the data changes.

## Reading notes

- The original question is about saving terminal capability information after checking environment variables once.
- One reply says processes are cheap enough that using one here should not be a problem.
- Another reply says the library's agent should be supervised and started by the application's supervisor.
- José Valim says a Mix application started with `mix new my_app --sup` already gives an application callback for startup.
- His example starts an Agent as a child and exposes a `get/1` function for reading the stored map.
- He says this makes global state explicit and easier to control, inspect, debug, and understand.
- Robert Virding says static data can be initialized at startup and stored in ETS.
- He says more dynamic data can also live in ETS, with a process managing updates.
