---
title: "How to build a self-healing system using supervision tree in Elixir"
date: '2020-11-01T21:46:34-03:00'
category: webclip
summary: 'Explains how Elixir supervision trees make systems reliable by restarting failed processes, using workers, supervisors, restart strategies, and self-termination to recover from repeated crashes.'
tags: ["elixir", "supervision-tree", "supervisor", "fault-tolerance"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "How to build a self-healing system using supervision tree in Elixir"
    url: "https://kodius.com/blog/elixir-supervision-tree/?utm_source=elixirdigest&utm_medium=email&utm_campaign=279"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2020-11/kodius-com--how-to-build-a-self-healing-system-using-supervision-tree-in.md"
    kind: repo
---

The post explains that Elixir supervision trees help build reliable, fault-tolerant, self-healing systems. It shows how supervisors restart failed workers, when they escalate restarts to a parent, and how different restart strategies change the outcome.

## Reading notes

- Supervision trees are presented as a way to keep services available by restarting the part of the system that failed.
- The tree has two process types, workers and supervisors, and supervisors manage direct children only.
- A supervisor can restart children when they terminate and can also terminate itself and its children if failures keep happening.
- The three restart strategies are `:one_for_one`, `:one_for_all`, and `:rest_for_one`.
- The default restart tolerance is 3 restarts in 5 seconds.
- A simple tree is built with one supervisor and two worker processes started through `Supervisor.start_link/2`.
- Each child defines `child_spec/1`, which returns the `:id` and `:start` fields needed by the supervisor.
- `Task.start_link/1` is used in the example workers to create long-running processes.
- With `:one_for_one`, killing one worker restarts only that worker.
- With `:one_for_all`, killing one worker restarts all children.
- With `:rest_for_one`, killing a process restarts it and the children listed after it.
- When a child exceeds the restart limit, the supervisor exits and the parent supervisor restarts it.
- In the more complex example, process C is itself a supervisor with children D and E.
- Killing process C restarts C and then its children D and E.
- Repeated crashes of D or E eventually cause C to terminate and be restarted by the parent supervisor.
