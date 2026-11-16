---
title: "Highlander, there can be only one"
date: '2026-11-16T08:07:41+00:00'
category: webclip
summary: 'The post shows how to start a globally unique process in an Erlang cluster with `:global` and a small `Highlander` module that registers, monitors, and restarts the chosen child spec.'
tags: ["erlang", "global-process-registry", "supervisor-child-spec"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Highlander, there can be only one"
    url: "https://web.archive.org/web/20200808150316id_/https://moosecode.nl/blog/highlander_there_can_be_only_one"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/web-archive-org--highlander-there-can-be-only-one.md"
    kind: repo
---

The post explains a small way to run one globally unique process in an Erlang cluster. It uses `:global` and a `Highlander` wrapper around an existing child spec so a supervisor can start only one instance across the cluster.

## Reading notes

- The goal is to make one child in an existing supervision tree globally unique without changing the whole tree.
- `Highlander` is inserted as `{Highlander, child_spec}` and uses `child_spec.id` as the global name.
- `:global.register_name(name, pid)` is used to claim the name, and `:global.whereis_name(name)` is used to look up an existing process.
- If registration succeeds, Highlander starts the wrapped child under its own supervisor.
- If registration fails, Highlander monitors the already registered process and retries if that process goes down.
- When the monitored process dies, Highlander handles `:DOWN` by trying to register again.
- On termination, Highlander stops the child process so shutdown stays orderly.
- The wrapper accepts any child spec, including another supervisor, because it uses `Supervisor.child_spec/1`.
