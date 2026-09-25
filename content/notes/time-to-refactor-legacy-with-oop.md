---
title: "Time to refactor legacy with OOP"
date: '2026-09-25T20:16:44+01:00'
category: webclip
summary: 'The article shows a legacy stats method that mixes tuple fields and is hard to read, then refactors it with OOP, iterators, and a builder-based workflow.'
tags: ["oop", "refactoring", "builder-pattern", "legacy-code"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Time to refactor legacy with OOP"
    url: "https://pvs-studio.com/en/blog/posts/csharp/1159/?ref=dailydev"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/pvs-studio-com--time-to-refactor-legacy-with-oop.md"
    kind: repo
---

The article starts from a legacy statistics method that is hard to inspect and easy to get wrong. A tuple-based UTM counter swaps Answered and Activated, which produces wrong final data without a compilation error. The author then argues for removing tuples, splitting the monolithic logic, and restructuring the code with OOP.

## Reading notes

- A 500-line static method returns many dictionaries and nested tuple structures, which makes the code hard to follow and debug.
- The reported bug comes from mixing up Answered and Activated inside a tuple, and the mistake only appears in the data output.
- The first refactoring goal is to replace tuples with classes to avoid that kind of field mix-up.
- A naïve split into several smaller methods still leaves large loops and can hurt performance by repeating passes over the same dataset.
- The proposed direction is to combine the builder pattern with iterators so the data is traversed by date in a controlled way.
- A chart builder example is used to explain the pattern before applying the same idea to mail statistics.
- In the final design, date iterators group data by month or year, and a statistics builder collects counts through actions attached to the processing flow.
- The builder uses out parameters to return the series that will later be passed into charts.
- Separate methods are used for request counts and trial activations, and the builder is chained before Process runs the accumulated logic.
- The refactoring aims to improve modularity, readability, compile-time safety, and performance while keeping the counting logic flexible.
