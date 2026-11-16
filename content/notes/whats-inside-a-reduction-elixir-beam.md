---
title: "What's Inside a Reduction?"
date: '2026-11-16T20:08:28+00:00'
category: webclip
summary: 'Examines how BEAM reductions are counted, showing that many non-reduction instructions and BIFs affect runtime, so reduction counts poorly track performance.'
tags: ["elixir", "beam", "performance", "benchmarking"]
has_commentary: false
generated_by: "openai/gpt-5.1"
sources:
  - title: "What's Inside a Reduction?"
    url: "https://devonestes.com/inside-a-reduction"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/devonestes-com--whats-inside-a-reduction-elixir-beam.md"
    kind: repo
---

The author describes adding reduction counting to Benchee and initially expecting reductions to give a stable, architecture-specific performance metric that would enable reliable tests for performance‑sensitive functions. Benchmarks comparing `Enum.flat_map/2` with `Enum.map/2 |> List.flatten/1` showed a much larger difference in reduction counts than in wall‑clock time, which broke that assumption. Investigating BEAM assembly with the `decompile` package revealed that many instructions (`move`, `test`, `get_map_elements`, `bif`, `jump`, `allocate`, `make_fun2`, etc.) are not counted as reductions but still consume time, and that BIFs run in C are also outside the reduction count.

Using small Elixir examples, the post shows two functions that each cost one reduction but have very different numbers of BEAM instructions and runtimes, and then a third function that takes two reductions yet runs faster than the original one‑reduction version. From this, the author concludes that reduction counts do not correlate reliably with runtime and are therefore not suitable as a primary tool for performance testing. Reduction data can still guide very low‑level optimization work (for example, replacing reductions with BIFs in hot paths), but such tuning largely belongs to language or, at most, library authors. The feature will likely be documented and released to see how others might use it, and the exploration underscores how BEAM’s compile‑time and runtime optimizations can produce surprising performance characteristics.

## Reading notes

- The author added a reduction‑counting feature to Benchee and initially ran into confusing benchmark results that turned out to be correct and exposed flawed assumptions about reductions as a performance metric.
- The original hope was that reductions would offer a stable, architecture‑specific measure for precise performance tests, unlike noisy wall‑clock timing, because deterministic functions should use a constant number of reductions.
- A benchmark comparing `Enum.flat_map/2` with `Enum.map/2 |> List.flatten/1` showed the slower version having 2.10× the reductions but only 1.36× the runtime, contradicting the expectation of a tight correlation.
- The author had implicitly modeled things like lambda calculus with only functions, assuming most work was function calls of roughly similar cost and that BIF usage would be similarly distributed.
- Using Michał Muskała’s `decompile` package, the BEAM assembly for `Enum.flat_map/2` showed many operations that are not `call` or `call_ext`, such as `move`, `test`, `get_map_elements`, `bif`, `jump`, `allocate`, `make_fun2`, and `kill`.
- These non‑call instructions are not counted as reductions but still contribute to wall‑clock time, so functions that do lots of such work can be slower while still consuming only one reduction.
- A simple `Test` module example defines `a_from_map/1` and `a_from_map2/4`, both counted as one reduction per call, to illustrate that they differ significantly in instruction count and runtime.
- The BEAM assembly for `a_from_map/1` has four main instructions (map check, element extraction, move, return), while `a_from_map2/4` has multiple repeated `test` and `get_map_elements` operations plus heap and list construction instructions.
- Benchmarking these functions with Benchee shows `a_from_map/1` running around 3.26× faster than `a_from_map2/4`, while both still register a reduction count of 1.
- The author ties the ~3.5× runtime difference to the roughly 3.5× increase in the number of BEAM instructions between the two functions rather than to reduction counts.
- From these experiments, the author infers that using reduction counts as the main basis for performance testing can give misleading results and false positives where reduction numbers match but timings differ greatly.
- The code that is most performance‑critical is also likely to rely on BIFs and other non‑reduction operations implemented in C, which further weakens the usefulness of reduction counts in testing such functions.
- Reduction information can still be useful for low‑level optimization of extremely hot paths, for instance by guiding the replacement of reductions with BIFs or other faster constructs.
- This style of optimization is framed as appropriate mostly at the language level and perhaps in a limited way in libraries, rather than typical production application code.
- The author leans toward documenting the behavior and releasing the feature despite its limits, to see if others find valuable uses that have not been considered.
- A postscript example extends the `Test` module with `a_from_map3/1`, which delegates to a private `do_a_from_map3/1`, resulting in two reductions for a call.
- The BEAM assembly for `a_from_map3/1` shows it essentially just performing a `call_only` to `do_a_from_map3/1`, where the actual map pattern match and extraction occurs.
- A benchmark of `a_from_map/1`, `a_from_map2/4`, and `a_from_map3/1` finds that `a_from_map3/1` (two reductions) runs faster than `a_from_map/1` (one reduction) and much faster than `a_from_map2/4`.
- Reduction statistics for that benchmark show `a_from_map3/1` at 2 reductions versus 1 for the other two functions, yet its wall‑clock performance is best.
- The author closes by noting that the BEAM has many compile‑time and runtime optimizations and stresses that performance work on BEAM should rely on measurement instead of guesses because optimizations can lead to surprising results.
