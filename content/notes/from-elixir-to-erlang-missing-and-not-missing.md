---
title: "From Elixir to Erlang"
date: '2026-11-16T20:09:02+00:00'
category: webclip
summary: 'Author reflects on moving from Elixir to full‑time Erlang work, listing tools and features they miss (ExUnit, Ecto, Unicode) and those they expected to miss but do not (syntax, Phoenix, mix).'
tags: ["elixir", "erlang", "testing", "tooling"]
has_commentary: false
generated_by: "openai/gpt-5.1"
sources:
  - title: "From Elixir to Erlang"
    url: "https://devonestes.com/elixir-erlang"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/devonestes-com--from-elixir-to-erlang-missing-and-not-missing.md"
    kind: repo
---

The author describes working full-time in Erlang for a new client after primarily using Elixir, and reflects on which Elixir features they actually miss and which they expected to miss but do not. They clarify that “not missing” something only means they are coping without it, not that they are glad it is gone, and they remain open to better Erlang techniques they might not yet know.

## Reading notes

- The author has been away from writing due to childcare responsibilities and a new client where they are now writing Erlang full-time, alongside some operations work.
- They outline that when they say they do not miss something from Elixir, it means they expected to miss it strongly but are not really feeling that in practice, even though they would still gladly have it back.
- They note that for some things they do miss, the gap might be due to not yet knowing good Erlang approaches, and they invite readers to share resources.
- Regarding syntax, they argue that while Erlang’s Prolog-style syntax seems unfamiliar at first and often gets complaints, after a few days it becomes comfortable to read and write.
- They report being just as fast now in reading and writing Erlang as Elixir and suggest that Erlang syntax is fine once it is practiced, despite many newcomers preferring Elixir because it resembles languages they already know.
- They say they miss ExUnit compared to Erlang’s built-in EUnit and Common Test, which initially felt odd as two frameworks but are now accepted.
- They highlight ExUnit’s conveniences such as colored diffs when comparing terms and very helpful error messages, which make TDD feel smoother than with EUnit or Common Test.
- They also miss ExUnit’s SQL Sandbox feature, which lets them write safe unit tests that interact with a database.
- They describe missing Ecto as a “truly wonderful” query builder, contrasting it with the current project’s hand-rolled query builder that is less flexible and harder to work with.
- They explain that the custom query builder functions adequately but does not reach Ecto’s ease of use, and they dislike manually handling the connection pool and transactions in that library.
- They remark that Ecto hides connection and transaction concerns so effectively that they temporarily forgot Ecto was responsible for managing them.
- They mention that they do not miss Phoenix on the current project, even though a previous project with heavy streaming and websockets would have been difficult to imagine in Erlang without it.
- For the present, simpler service, which does not need streaming or websockets, using Cowboy directly has been sufficient and has not made them long for Phoenix.
- They still regard Phoenix as a solid library and say they would use it in Elixir almost all the time, but in this narrow case they have been fine without it.
- They miss strong Unicode support in their current Erlang environment, noting that the app is over 10 years old and predates Erlang’s improved Unicode capabilities.
- The system is still on OTP 19, and although modern Erlang has better Unicode support, legacy code from before those improvements remains, which is problematic for a user base spread across much of Europe where UTF-8 is essential.
- They note that with Elixir they did not even have to think about Unicode support, and in the current project they repeatedly find themselves thinking that certain tasks would be much easier in Elixir.
- They say they do not miss mix because Rebar3 has become a strong tool, and while there are a few small mix features they miss, they have not yet encountered a task where mix would have unblocked them.
- They add that this shift has led them back to using Makefiles, which they enjoy, and they express enthusiasm for Makefiles and bash as tools for automating tasks, even if that preference might seem unusual.
