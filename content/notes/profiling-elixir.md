---
title: "Profiling Elixir"
date: '2015-04-10T11:08:29-03:00'
category: webclip
summary: 'The author profiles an Elixir Game of Life implementation with ExProf and fprof, compares their outputs, and concludes that most time is spent in map lookups through Access.Map.get/2.'
tags: ["elixir", "profiling", "fprof", "exprof"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Profiling Elixir"
    url: "http://learningelixir.joekain.com/profiling-elixir/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-04/learningelixir-joekain-com--profiling-elixir.md"
    kind: repo
---

The post describes an Elixir Game of Life project used to experiment with profiling tools after the program ran much more slowly than expected. ExProf and then fprof are used to inspect the code, and both point away from the inner Life functions the author expected to dominate.

The profiling output leads the author to inspect Elixir.Access.Map.get/2 in access.ex and infer that much of the runtime is spent looking up values in the Map that stores the game board. The post ends with the author still looking for more information and planning to keep testing other tools.

## Reading notes

- The author returns to Elixir after time away and builds Conway’s Game of Life as a test project.
- Two test layers are used, with end-to-end tests in bash and unit tests in ExUnit.
- A glider pattern is used to measure performance in a board sized 100x83 cells.
- The program runs at about 5 to 6 seconds per generation, slower than the desired 0.5 to 1 second.
- ExProf is introduced as a simple profiler and wrapped around the test run.
- The first profile output shows time in ensure_compiled/1, code_server:call/2, impl_for/1, and maps:find/2.
- The author expected more time in Life.list_of_neighbors/3 and Life.count_live_neighbors/3, but the report does not show that.
- fprof is then used because it gives more detail and call chains.
- The first fprof analysis is sorted by ACC, which the author finds less useful than OWN.
- The analysis is changed to sort by OWN through options passed to :fprof.analyse().
- The adjusted output is easier to read and still points to map-related lookup work.
- The author inspects Elixir.Access.Map.get/2 in access.ex and treats it as the protocol implementation for [] on a Map.
- The conclusion is that the program likely spends most of its time doing Map lookups for the game board.
- The post closes by saying more tools still need to be explored.
