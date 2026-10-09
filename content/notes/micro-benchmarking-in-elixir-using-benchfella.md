---
title: "Micro Benchmarking in Elixir using Benchfella"
date: '2015-06-07T07:17:10-03:00'
category: webclip
summary: 'The post compares file-hashing approaches in Elixir with Benchfella, showing that larger chunk sizes perform better, while reading a whole file at once can be faster than a single oversized chunk.'
tags: ["elixir", "benchmarking", "benchfella", "hashing"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Curse the Darkness: Micro Benchmarking in Elixir using Benchfella"
    url: "http://www.cursingthedarkness.com/2015/06/micro-benchmarking-in-elixir-using.html"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-06/cursingthedarkness-com--micro-benchmarking-in-elixir-using-benchfella.md"
    kind: repo
---

The post introduces Benchfella as a micro-benchmarking framework for Elixir that works similarly to ExUnit. It then uses it to compare different chunk sizes for hashing files, and also compares chunked hashing with reading the whole file at once.

## Reading notes

- Benchfella is presented as a micro-benchmarking framework for Elixir that behaves much like ExUnit.
- The code shown defines many benchmarks by iterating over a list of chunk sizes.
- The hashing test streams a file in chunks and folds the data through SHA-256 hash functions.
- Benchfella runs each test as many times as possible in a given interval, with one second as the default, and stores results on the filesystem for later comparison.
- The benchmark results show a significant advantage for large chunk sizes when hashing files of size 2**24, 2**26, and 2**28.
- The author notes an odd bump at 2**23 in the plot.
- The test was run on a MacBook Pro with 16 GB of memory and an SSD disk drive.
- The post says that large binaries are generally the fastest way to handle large data sets in Elixir and Erlang, while memory limits still matter.
- A second benchmark compares chunked hashing with a chunk size larger than the file to reading the whole file into a string and hashing it.
- The simple read method is consistently twice as fast as the single-chunk method.
- The final application chooses a chunk size that allows multiple files to be processed at the same time and switches hashing methods based on file size.
