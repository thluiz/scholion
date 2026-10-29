---
title: "What's coming in Elixir 1.3"
date: '2016-05-09T13:59:32-03:00'
category: webclip
summary: 'The post surveys Elixir 1.3 changes, including stricter scoping, richer `with` support, calendar types, new Mix tasks, and deprecations that will raise warnings.'
tags: ["elixir", "release-notes", "mix-tasks", "scoping"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "What's coming in Elixir 1.3"
    url: "http://tuvistavie.com/2016/elixir-1-3/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2016-05/tuvistavie-com--whats-coming-in-elixir-1-3.md"
    kind: repo
---

Elixir 1.3 adds several language and tooling changes that aim to make code more consistent, easier to refactor, and easier to inspect. The post also notes a few deprecations that may produce warnings in existing projects.

## Reading notes

- Imperative assignment is being deprecated so all special forms can move toward simpler, more consistent scoping rules, even if that means a little extra verbosity in some cases.
- `with` gains `else` for handling error cases and guards, which makes nested control flow and error processing easier to express.
- New date and time types are added to the standard library, improving interoperability between libraries that previously used different date packages.
- `escript` can now be installed from a URL, and Mix gets tasks for listing and uninstalling installed escripts.
- ExUnit gets a readable diff for failed tests, and `String.myers_difference/2` supports that feature.
- A `make` compiler is added for projects that need it, especially libraries that distribute NIFs.
- `defdelegate` deprecates list usage and `:append_first`, while allowing optional parameters in delegates.
- `Process.sleep/1` is added, but the post recommends using it mainly for retry delays rather than waiting on tasks or monitoring processes.
- OTP `optional_callbacks` is supported so behaviour modules can define defaults and implementations can keep only the required callbacks.
- New Mix tasks `deps.tree` and `app.tree` show dependency and application trees.
- The post ends by encouraging regular compilation against Elixir master to catch deprecations early.
