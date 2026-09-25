---
title: "Anatomy of the .NET dictionary"
date: '2026-09-25T08:26:24+01:00'
category: webclip
summary: 'Explains how .NET Dictionary stores entries in buckets and arrays, handles collisions with chaining, reuses freed slots, and grows or trims capacity.'
tags: ["csharp","dotnet","collections","anatomy"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Anatomy of the .NET dictionary"
    url: "https://dunnhq.com/posts/2024/anatomy-of-the-dotnet-dictionary/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/dunnhq-com--anatomy-of-the-dotnet-dictionary.md"
    kind: repo
---

The post explains that .NET `Dictionary<TKey, TValue>` does not store key/value pairs directly. It uses two arrays, one for buckets and one for entries, and the bucket points into a chain of entries through encoded indices. Collisions are resolved by comparing hash codes and then equality, and removed entries are kept for reuse through a free list.

It also shows that dictionary capacity starts at a prime number, grows by resizing to the next prime when needed, and can be reduced with `TrimExcess`. `KeyValuePair` is described as part of the API rather than the internal storage format.

## Reading notes

- A `.NET Dictionary<TKey, TValue>` uses two internal arrays, one for buckets and one for entries, instead of storing the data as key/value pairs.
- The buckets point to entries by encoded indices; `0` marks an empty bucket and the values are 1-based.
- When adding an item, the key passes through `GetHashCode`, the bucket is calculated by modulo, and the entry is placed at the available index.
- When there is a collision, the dictionary walks the chain of entries in the same bucket and compares hash code and `Equals`.
- If the key already exists, the insert operation updates the value or throws an exception, depending on the insert mode.
- The chain between entries is maintained by the `next` field, which also serves to link free slots.
- Removing an item does not physically delete the entry; it is marked as free, enters the free list, and can be reused later.
- `_freeList` points to the next free slot and `_freeCount` counts how many free slots exist.
- The initial capacity used in the example is 3, chosen from an internal list of prime numbers.
- When capacity is exhausted, the dictionary resizes to a larger prime number, typically doubling and rounding up.
- Public `Count` is calculated as `_count - _freeCount`, so the external total can be smaller than the internal total.
- `TrimExcess` is mentioned as a way to free memory in a large dictionary with a lot of churn.
- `KeyValuePair` is the interface for input and output of data, but it is not how the dictionary stores the values internally.
