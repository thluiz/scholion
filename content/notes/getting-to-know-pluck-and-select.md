---
title: "Getting to Know Pluck and Select"
date: '2013-11-30T23:12:53-03:00'
category: webclip
summary: 'The post compares `pluck` and `select` in ActiveRecord, showing that `pluck` avoids model instantiation overhead, is faster for raw values, and `select` still matters when you need model objects and methods.'
tags: ["activerecord", "performance", "rails"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Getting to Know Pluck and Select - Gavin Miller"
    url: "http://gavinmiller.io/2013/getting-to-know-pluck-and-select/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2013-11/gavinmiller-io--getting-to-know-pluck-and-select.md"
    kind: repo
---

The post explains that `select` returns ActiveRecord model objects, while `pluck` returns plain values and skips the overhead of building models. It argues that this difference matters for performance even when query time looks similar.

## Reading notes

- `select` was the standard way to query a single field before `pluck` existed.
- `User.select(:id).to_a` returns an array of `User` models with only `id` loaded.
- `pluck` was introduced in Rails 3.2 to skip ActiveRecord object construction.
- `User.pluck(:id)` returns an array of integers instead of model instances.
- The database query time can be similar, but object creation makes `select` slower.
- A benchmark over 10,000 users showed `select` was 91% slower than `pluck`.
- `pluck` was created to remove the overhead seen in patterns like `User.select(:id).map(&:id)`.
- As of Rails 4.0, `pluck` can take multiple columns.
- `select` accepts multiple columns as separate arguments or as an array, but `pluck` does not accept an array.
- `select` is useful when the returned records need model methods.
- The post summarizes the distinction as `pluck` for model values and `select` for model objects.
