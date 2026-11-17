---
title: "Measuring memory consumption on the BEAM"
date: '2026-11-17T15:03:06+00:00'
category: webclip
summary: 'Explains Benchee’s new feature for benchmarking memory usage of Elixir/Erlang functions, how it works on the BEAM, and its current limitations and requirements.'
tags: ["elixir", "beam", "performance", "memory-usage"]
has_commentary: false
generated_by: "openai/gpt-5.1"
sources:
  - title: "Measuring memory consumption on the BEAM"
    url: "https://devonestes.com/measuring-memory-consumption-on-the-beam"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/devonestes-com--measuring-memory-consumption-on-the-beam.md"
    kind: repo
---

The text introduces a new Benchee 0.13 feature that allows benchmarking memory usage in Elixir and Erlang functions, emphasizing that performance also depends on memory consumption. It shows how to enable memory measurements with a `memory_time` option, explains that most functions will need short measurement periods, and notes that randomness in a function can cause memory usage to vary. The author then details current limitations: measurements only cover the single process running the function and count all memory used, including garbage collected data, and the feature requires OTP 19 or higher. Finally, it outlines the tracing-based approach used for measuring memory on the BEAM, since garbage collection cannot be disabled, and points to the Benchee source code for implementation details.

## Reading notes

- Benchee 0.13 adds support for benchmarking memory usage of functions in Elixir or Erlang, expanding focus beyond just run time.
- To measure memory, Benchee is used as usual, but a `memory_time` option must be set to define how long memory usage is recorded.
- The example compares memory usage between `Enum.flat_map` and a combination of `Enum.map` with `List.flatten` over a range of integers.
- For most benchmarked functions, short measurement durations are sufficient because they typically use a consistent amount of memory on each run.
- Memory usage variation is expected mainly in functions that involve some randomness.
- Current implementation measures memory usage only for the single process executing the benchmarked function, not the overall BEAM VM.
- Memory used by additional processes spawned for parallel work is not reflected in the current measurements.
- The author mentions a desire to eventually capture wider VM effects, but this is outside the current scope.
- What is reported is the total memory used by the function, including all data that is later garbage collected.
- Every byte that is garbage collected during the function’s execution contributes to the reported total memory usage.
- The memory measurement feature depends on a tracing capability introduced in OTP 19, so it only works on OTP 19 or newer.
- Unlike some other garbage collected runtimes, the BEAM does not allow disabling garbage collection without risking crashing the VM.
- In other runtimes, a common memory measurement pattern is to disable GC, measure VM size before and after running a function, and take the difference.
- Because disabling GC is not an option on the BEAM, another strategy is required for memory measurement.
- The approach used in Benchee spawns a process that listens for messages from `:erlang.trace/3`.
- The tracer listens specifically for garbage collection messages to observe heap sizes.
- By examining heap size before and after each garbage collection, the code calculates how much data was collected.
- The implementation accumulates garbage collected data size throughout the function’s execution.
- At the end of the benchmark run, the remaining data on the heap is added to the accumulated collected data to obtain total memory usage.
- The author notes that the actual implementation code for memory measurement is relatively small and provides a link to the file in the Benchee repository.
