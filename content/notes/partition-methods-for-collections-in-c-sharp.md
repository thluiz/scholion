---
title: "Partition methods for collections in C#"
date: '2026-09-25T21:38:52+01:00'
category: webclip
summary: 'The article defines partitioning as splitting a collection into fixed-size parts and shows extension methods for IList<T>, IDictionary<TKey, TValue>, and ConcurrentDictionary<TKey, TValue> to support parallel processing.'
tags: ["c-sharp", "collections", "parallel-processing"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Partition methods for collections in C#"
    url: "https://toreaurstad.blogspot.com/2024/10/partition-methods-for-collections-in-c.html?m=1&utm_source=newsletter.csharpdigest.net&utm_medium=newsletter&utm_campaign=using-windows-error-reporting-in-net&_bhlid=f27099d53236b8833e46834f463dd985bcc3801d"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/toreaurstad-blogspot-com--partition-methods-for-collections-in-c-sharp.md"
    kind: repo
---

The article explains partitioning as splitting a collection into chunks of a fixed size, with the last chunk possibly smaller than the others. It gives an example of a 100-item list split into partitions of 30 items, producing four parts.

## Reading notes

- Partitioning is defined as splitting a collection into partitions of size C, where C is a positive constant integer.
- A list of 100 elements partitioned by 30 yields four partitions, and the last partition contains only 9 elements.
- The article shows extension methods named Partition for IList<T>, IDictionary<TKey, TValue>, and ConcurrentDictionary<TKey, TValue>.
- Each method uses Skip and Take inside a loop based on the collection count divided by the partition size.
- The example partitions a ConcurrentDictionary with 200,000 key-value pairs into four parts of 50,000 items each.
- The resulting partitions are processed in parallel.
- The article notes that the simpler Parallel.ForEach approach tested faster than partitioning into multiple concurrent dictionaries.
- The main point is that partitioning can support a divide-and-conquer approach for distributing collection work across several threads.
