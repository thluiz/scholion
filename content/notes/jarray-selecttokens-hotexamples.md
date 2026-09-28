---
title: "JArray.SelectTokens Examples"
date: '2022-05-10T09:58:42-03:00'
category: webclip
summary: 'The page shows C# examples of JArray.SelectTokens with JSONPath queries for nested properties, scans, wildcards, slices, index lists, and value filters over arrays.'
tags: ["csharp", "jsonpath", "newtonsoft-json", "jarray"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "JArray.SelectTokens, Newtonsoft.Json.Linq C# (CSharp) Code Examples - HotExamples"
    url: "https://csharp.hotexamples.com/examples/Newtonsoft.Json.Linq/JArray/SelectTokens/php-jarray-selecttokens-method-examples.html"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2022-05/csharp-hotexamples-com--jarray-selecttokens-hotexamples.md"
    kind: repo
---

The page collects 12 C# examples of `Newtonsoft.Json.Linq.JArray.SelectTokens`. The examples show how the method returns matching tokens from arrays when the query uses nested conditions, recursive scans, wildcards, slices, multiple indexes, and comparisons on numeric and string values.

## Reading notes

- Uses a nested filter to find array items whose `cast` contains `Will Smith`, then selects their `name` values.
- Filters arrays by comparing `hi` to numeric values, including `> 1` and `>= 1`.
- Filters a plain numeric array with `@ > 1` when no path is present.
- Shows that chained JSONPath filters can return no results when the first filter reduces items to scalars.
- Uses `$..*` to scan and return the array, objects, nested objects, arrays, and primitive values in traversal order.
- Uses `$..Name` to collect every `Name` value in the array.
- Uses `[*]` to return all array elements.
- Uses `[1,2,0]` to return selected array items in the listed order.
- Uses slices such as `[-3:]`, `[-1:-2:-1]`, `[-2:-1]`, `[1:1]`, `[1:2]`, `[::-1]`, and `[::-2]` to select ranges and reverse order.
