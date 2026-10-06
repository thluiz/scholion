---
title: "What are the different OTP supervisor restart strategies useful for?"
date: '2015-05-22T11:17:49-03:00'
category: webclip
summary: 'The post summarizes the four OTP supervisor restart strategies and the situations they fit: fixed hierarchies, same-type process pools, dependent pipelines or registries, and tightly related groups that must restart together.'
tags: ["otp", "supervisors", "restart-strategies", "elixir"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "What are the different OTP supervisor restart strategies useful for? – Chris McGrath"
    url: "http://chrismcg.com/2015/04/28/what-are-the-different-otp-supervisor-restart-strategies-useful-for/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-05/chrismcg-com--what-are-the-different-otp-supervisor-restart-strategies-use.md"
    kind: repo
---

The post explains the four OTP supervisor restart strategies by linking each one to a common process structure. It says `one_for_one` is used for fixed supervisor hierarchies with independent children, `simple_one_for_one` for creating many processes of the same type, `rest_for_one` for pipelines or registry-like dependencies, and `one_for_all` for related processes that must restart together.

## Reading notes

- `one_for_one` is used for supervisor hierarchies and workers or supervisors that do not need to be pooled or started dynamically.
- `simple_one_for_one` is used to create and supervise processes of the same type, either as a pool at startup or when something happens later.
- In the cache example, `Mapper` calls `start_child(url)` and stores the returned pid so it can avoid a database lookup next time the shortcode is requested.
- `simple_one_for_one` and `one_for_one` are described as the most common strategies.
- `rest_for_one` fits one-way dependencies, such as a chain of processes in a pipeline.
- If an earlier process in that chain dies, the later processes that depend on it must be restarted.
- The post also uses a registry process that maps external input to the pid of the process that handles it as another `rest_for_one` example.
- In the cache supervisor example, if `Mapper` dies, the supervisor terminates the children caching the urls because the mapping is lost.
- `one_for_all` is used when several processes depend on each other to get work done and one failure means the rest should restart too.
- The Riak Core example is a sync setup for two-way synchronization where restarting all related processes brings the system back to a known state.
- The summary says `one_for_one` and `simple_one_for_one` are used most often, `rest_for_one` occasionally, and `one_for_all` rarely.
