---
title: "Parallel Elixir Run"
date: '2016-02-29T11:02:45-03:00'
category: webclip
summary: 'The post shows how to distribute letter-frequency work across several Elixir processes with Task.async and Task.await, then merge the partial results. It reports faster runtimes with multiple workers than with one.'
tags: ["elixir", "task", "parallel-processing"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Parallel Elixir Run"
    url: "https://shcatula.wordpress.com/2016/02/09/parallel-elixir-run/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2016-02/shcatula-wordpress-com--parallel-elixir-run.md"
    kind: repo
---

The post uses Task to split a letter-frequency job across several processes. The work is divided into groups, each group is sent to a worker with Task.async, and the results are gathered with Task.await before they are merged.

## Reading notes

- The problem is to calculate letter occurrences in a list of texts, and the goal is to distribute the load rather than share state.
- Agent is not needed for this case, because the task only needs async execution and later collection of results.
- Task.async starts a job and Task.await waits for it to finish and return its result.
- The processes are linked, so a crash on either side makes the other fail too.
- The code first groups the texts by workers, then uses Enum.map to start one task per group.
- A second Enum.map waits for each task and collects the returned values.
- The complete example is available on Github.
- An informal benchmark with ten thousand short poems gives 12 seconds with 1 worker and about 5 seconds with 4, 16, 32, or 128 workers.
- The author says the speedup is significant compared with a single process and comes with little more code than usual.
