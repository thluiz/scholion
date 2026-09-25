---
title: "Everything You Want to Know About the Record Type in .NET… But Were Afraid to Ask"
date: '2026-09-25T08:24:53+01:00'
category: webclip
summary: 'O texto explica como record types reduzem boilerplate em DTOs, usam init e with para imutabilidade e contam com igualdade, hash e ToString gerados. Também compara desempenho com classes e structs.'
tags: ["dotnet-5", "record-types", "immutabilidade", "performance"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Everything You Want to Know About the Record Type in .NET… But Were Afraid to Ask"
    url: "https://dotnettips.wordpress.com/2021/02/26/everything-you-want-to-know-about-the-record-type-in-net-5-but-were-afraid-to-ask/?utm_source=newsletter.csharpdigest.net&utm_medium=newsletter&utm_campaign=10-lessons-i-learned-from-using-aspire-in-production&_bhlid=02b275dc8f7af750ddde9a88efe8c83efdcd1cbe"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/dotnettips-wordpress-com--record-type-dotnet-5-immutability-performance.md"
    kind: repo
---

The article presents record types in .NET 5 as a fit for model types such as DTOs and POCOs, with less boilerplate and built-in support for immutability. It also notes that records generate equality members, GetHashCode(), and a useful ToString(), while mentioning a custom PropertiesToString() for collection properties.

## Fichamento

- Record types were introduced in .NET 5 to reduce boilerplate code.
- The author uses record types mainly for model types such as DTOs and POCOs.
- Record declarations use the record keyword instead of class.
- Init accessors replace set for values that should be set in constructors or object initialization.
- After object creation, record data cannot be modified, which preserves immutability.
- The with keyword creates a new object when a record needs updated values.
- Record types automatically generate equality operators and related comparison members.
- Record types also generate GetHashCode(), reducing maintenance work.
- Record types generate a ToString() result that is more meaningful than the default type name.
- The author created PropertiesToString() in IDataRecord to serialize collection properties more accurately.
- Benchmarking in the article compares records with value types and reference types.
- The article says cloning a record is faster than cloning value types and reference types.
- The article says hashing reference types is slightly faster than hashing value types and record types.
- JSON serialization and deserialization are shown as common operations for these types.
- Iterating over records is described as slower than reference types but faster than value types.
- Sorting records is described as slightly faster than reference types and faster than value types.
- The article concludes that records can reduce coding effort and maintenance costs, especially for DTOs.
- The author lists immutability, inheritance support, generated equality and hash members, and performance as reasons to adopt record types.
