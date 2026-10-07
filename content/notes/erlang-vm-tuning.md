---
title: "Erlang VM Tuning"
date: '2015-02-19T22:43:32-03:00'
category: webclip
summary: 'Riak exposes Erlang VM settings in riak.conf, while older versions used vm.args. The page lists tuning options for SMP, schedulers, ports, buffers, ETS, crash dumps, tick time, and shutdown time.'
tags: ["erlang", "riak", "vm-tuning"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Erlang VM Tuning"
    url: "http://docs.basho.com/riak/latest/ops/tuning/erlang/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-02/docs-basho-com--erlang-vm-tuning.md"
    kind: repo
---

Riak runs on Erlang VM, so tuning VM parameters is part of performance optimization. The page maps Erlang flags and environment values to Riak configuration names, then explains which settings affect multiprocessing, scheduler behavior, port usage, buffering, storage limits, crash dumps, network tick checks, and shutdown timing.

## Reading notes

- Riak is written almost entirely in Erlang and exposes only a subset of Erlang VM parameters through node configuration files.
- In Riak versions before 2.0, VM parameters were set in `vm.args`; in 2.0 and later, they are set in `riak.conf`, and `vm.args` values override `riak.conf` when both are present.
- SMP can be enabled, disabled, or set to `auto`; `auto` enables it only when the OS supports SMP and more than one logical processor is detected.
- The scheduler settings include total and online thread counts, wakeup interval, compaction of load, and utilization balancing.
- `+sfwi` is recommended at `500` and `+scl` at `false` when using the older `vm.args` system.
- Only one of compaction of load or utilization balancing can be active at a time; if both are false, Riak uses compaction of load.
- Port settings cover the Erlang distribution port range, the maximum number of concurrent ports or sockets, and the `nodename` used for cluster node identifiers.
- The asynchronous thread pool can be sized with `erlang.async_threads`, and each async thread has a configurable stack size.
- Kernel polling is on by default and can be turned off with `erlang.K = off`.
- Warning messages from `error_logger` can be mapped to warnings, errors, or info reports with `erlang.W`.
- `erlang.process_limit` sets the maximum number of system processes, and `erlang.distribution_buffer_size` controls the distribution buffer busy limit.
- `erlang.max_ets_tables` sets the ETS table limit, and higher values increase quick-access storage at the cost of RAM.
- `erlang.crash_dump` changes the crash dump location, and `erlang.distribution.net_ticktime` sets the interval for node liveness checks.
- `erlang.shutdown_time` sets how long the VM spends shutting down before killing existing processes.
