---
title: "Why Hot Deploys are Cool"
date: '2026-11-16T03:52:20+00:00'
category: webclip
summary: 'Greg Vaughn argues that hot deploys are useful in many Elixir systems because most changes are to plain modules, while full restarts handle rarer supervision-tree changes and state updates. He says context should decide whether to rely on them.'
tags: ["elixir", "deployment", "hot-deploys"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Why Hot Deploys are Cool"
    url: "https://gvaughn.github.io/2020/05/17/why_hot_deploys_are_cool.html"
    kind: repo
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/gvaughn-github-io--why-hot-deploys-are-cool.md"
    kind: repo
---

Greg Vaughn says he values hot deploys in Elixir because most of his releases only change plain modules, not supervision trees or long-running process state. In that setup, Distillery can generate relup files for most deploys, while full restarts handle the harder cases.

## Reading notes

- He links hot code loading to Erlang’s original zero-downtime requirement and treats it as part of the platform’s history.
- He distinguishes between relying on hot deploys and simply benefiting from them.
- Relying on them means designing the system to stay up continuously and handling appup, relup, and code_changed cases carefully.
- He says most of his deploys do not need changes to the supervision tree or long-running GenServer state.
- Distillery lets him hot deploy plain modules for more than 90% of cases without extra work.
- For the remaining cases, he uses a full restart release and depends on durable storage and cache refresh at startup.
- He says hot deploys let background tasks keep running without interruption.
- He notes that Docker and orchestration can make hot deploys less relevant in some organizations.
- He says his current startup context fits Elixir and BEAM well because the system is mostly periodic background work with a smaller Phoenix UI.
- He advises newcomers not to dismiss hot deploys outright and to test them in a side project to understand where they fit.
