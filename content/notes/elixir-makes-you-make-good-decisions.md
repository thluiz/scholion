---
title: "Elixir Makes You Make Good Decisions"
date: '2026-09-25T17:12:19+01:00'
category: webclip
summary: 'The author argues that Elixir, Phoenix, Ecto, and the BEAM helped screen.garden make cleaner architecture, easier authorization, faster file sync, and tests that are pleasant to write.'
tags: ["elixir", "phoenix", "testing", "software-architecture"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Elixir Makes You Make Good Decisions"
    url: "https://kevinbarrett.org/elixir-makes-you-make-good-decisions/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/kevinbarrett-org--elixir-makes-you-make-good-decisions.md"
    kind: repo
---

The author says that building screen.garden with Elixir and Phoenix led to early architectural choices that held up well, made dependencies dependable, and kept new features easy to ship. He also says the stack shaped better decisions around authorization, file sync, and testing.

## Reading notes

- The project was built as a nights-and-weekends effort with Elixir and Phoenix, and the author says the stack has supported solid early architectural and structural decisions.
- He describes screen.garden as a sync and multiplayer collaboration backend for Obsidian that also lets users access a vault from the web.
- For authorization, the team used let_me to turn ad hoc checks into a policy DSL, then changed the access model without changing their contexts.
- Private collections were added by creating Ecto schemas and let_me checks, without spreading spaghetti code through the codebase.
- The author pushes back on the idea that Elixir’s smaller community means weak tooling, saying Broadway, an SQS adapter, and Oban Web enabled fast file sync with retries, backpressure, and sequencing.
- He says Elixir makes testing feel worthwhile because ExUnit, mix generators, fixtures, setup hooks, assert, and refute make tests quick to write and easy to design.
- He compares solving problems in Elixir to finding Koroks in Breath of the Wild and Tears of the Kingdom, as a small puzzle that makes the world feel a little more repaired.
