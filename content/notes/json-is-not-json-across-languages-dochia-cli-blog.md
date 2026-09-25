---
title: "JSON is not JSON Across Languages | Dochia CLI Blog"
date: '2025-09-26T19:24:58+01:00'
category: webclip
summary: 'JSON is simple on paper, but different languages and libraries interpret numbers, strings, dates, key order, and nulls differently, creating interoperability bugs across systems.'
tags: ["json", "interoperability", "cross-language", "data-serialization"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "JSON is not JSON Across Languages | <span class=\"text-terminal-purple\">Dochia</span> CLI Blog"
    url: "https://blog.dochia.dev/blog/json-isnt-json/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2025-09/blog-dochia-dev--json-is-not-json-across-languages-dochia-cli-blog.md"
    kind: repo
---

JSON looks uniform, but the article argues that its behavior changes across languages and libraries. The main risks are precision loss in large numbers and decimals, Unicode normalization differences, key-order assumptions, null and missing-field handling, and date parsing mismatches. These gaps matter most when data crosses service boundaries, especially in APIs, hashing, signatures, and financial workflows.

The article also stresses that parsers differ in how they accept malformed input and how they preserve or normalize values. Its practical guidance is to validate schemas, normalize data types, choose parsers carefully, and test cross-language compatibility with real payloads and edge cases.

## Reading notes

- JSON is defined simply, but implementations leave room for different interpretations across languages and libraries.
- Large integers can lose precision in JavaScript, while other languages may preserve them or depend on the target type used during parsing.
- Decimal values can also become problematic when arithmetic is done with floating-point types instead of dedicated decimal types.
- Unicode strings may compare differently unless they are normalized to the same form.
- Object key order is not guaranteed by the specification, yet some applications rely on it for hashing and signatures.
- Null, undefined, and missing fields are handled differently depending on the language and data structure.
- JSON has no native date type, so timestamps and date strings are represented and parsed in multiple incompatible ways.
- Parsers differ on duplicate keys, trailing commas, leading zeros, and single quotes.
- Cross-language compatibility testing is presented as necessary for catching these mismatches before production.
- The article recommends schema validation, canonical serialization for cryptographic use, and careful library selection.
