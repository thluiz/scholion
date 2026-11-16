---
title: "LINQ GroupBy in Depth"
date: '2020-02-22T12:11:49+00:00'
category: webclip
summary: 'The page explains how LINQ GroupBy groups collections by a key, how element and result selectors change the output, and how an equality comparer affects grouping and key choice.'
tags: ["linq", "groupby", "csharp", "dotnet"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "LINQ GroupBy in Depth - Kill All Defects"
    url: "https://web.archive.org/web/20200808061719id_/https://killalldefects.com/2020/01/21/dotnet-linq-groupby-in-depth/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/web-archive-org--linq-groupby-in-depth-kill-all-defects.md"
    kind: repo
---

The page walks through LINQ GroupBy in C# from basic grouping to advanced overloads. It shows how a key selector splits a collection into sub-collections, how an element selector limits what each group contains, and how a result selector projects groups into a custom shape.

## Reading notes

- GroupBy groups related data by a chosen property and returns groups that can be iterated as collections.
- With a key selector like `books.GroupBy(b => b.Author)`, the result is an `IEnumerable<IGrouping<string, Book>>`.
- An element selector can keep only part of each item, such as titles instead of full book objects.
- A result selector can project each group into a custom anonymous object with an author field and a collection of titles.
- With a result selector, the return type becomes `IEnumerable<TProjected>` instead of `IEnumerable<IGrouping<TKey, TValue>>`.
- An equality comparer can control how keys are matched when grouping, such as ignoring casing differences with `StringComparer.CurrentCultureIgnoreCase`.
- When multiple values compare to the same group, LINQ uses the first encountered key as the group key.
- The page suggests cleaning and normalizing the data source when possible, and using a custom comparer only when grouping needs criteria other than reference equality.
