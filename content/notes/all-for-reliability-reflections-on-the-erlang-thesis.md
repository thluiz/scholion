---
title: "All For Reliability: Reflections on the Erlang Thesis"
date: '2026-11-16T03:51:37+00:00'
category: webclip
summary: 'The article argues that Erlang’s process model, messaging, supervision, and scheduling were designed first for reliability, and that these choices also make concurrent programs scale well.'
tags: ["erlang", "elixir", "reliability", "concurrency"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "All For Reliability: Reflections on the Erlang Thesis - DockYard"
    url: "https://dockyard.com/blog/2018/07/18/all-for-reliability-reflections-on-the-erlang-thesis"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/dockyard-com--all-for-reliability-reflections-on-the-erlang-thesis.md"
    kind: repo
---

The article reads Joe Armstrong’s Erlang thesis as a defense of reliability, not speed, as the original goal. It shows how Erlang turns hardware failure, process failure, and recovery into one uniform model, and how that model later became useful for Elixir and Phoenix.

## Reading notes

- Armstrong’s thesis frames the problem as building reliable systems from programs that can contain errors.
- Erlang treats hardware failure as software failure so one process can react to another process’s death in a uniform way.
- Processes are isolated, share no memory, and communicate only by asynchronous message passing.
- This isolation is meant to limit failure spread, like firewalls between parts of a system.
- The VM makes processes lightweight so many of them can be created quickly and on demand.
- Preemptive scheduling prevents one CPU-bound process from blocking others that are ready to run.
- The same mechanisms that support reliability also support consistent performance under load.
- Small processes, asynchronous messaging, and concurrent garbage collection help the system avoid stop-the-world pauses.
- Armstrong’s evidence from Erlang systems suggests very high reliability, even when software errors still occurred.
- The article concludes that concurrency-oriented programming is both a reliability strategy and a performance strategy.
