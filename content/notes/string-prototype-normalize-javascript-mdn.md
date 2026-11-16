---
title: "String.prototype.normalize() - JavaScript | MDN"
date: '2020-04-20T21:22:46+00:00'
category: webclip
summary: 'Describes String.prototype.normalize(), which returns a string in a Unicode normalization form. It explains NFC, NFD, NFKC, and NFKD, and how normalization affects comparison, length, search, and display.'
tags: ["javascript", "unicode", "string-normalization"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "String.prototype.normalize() - JavaScript | MDN"
    url: "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/normalize"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/developer-mozilla-org--string-prototype-normalize-javascript-mdn.md"
    kind: repo
---

String.prototype.normalize() returns a string in a Unicode normalization form. If form is omitted or undefined, NFC is used. The page distinguishes canonical normalization from compatibility normalization and shows how different code point sequences can represent the same character.

## Reading notes

- form can be "NFC", "NFD", "NFKC", or "NFKD"
- NFC means Canonical Decomposition, followed by Canonical Composition
- NFD means Canonical Decomposition
- NFKC means Compatibility Decomposition, followed by Canonical Composition
- NFKD means Compatibility Decomposition
- the return value is a string containing the Unicode Normalization Form of the given string
- a RangeError is thrown if form is not one of the specified values
- Unicode assigns a code point to each character, but the same abstract character can be represented by more than one code point sequence
- the character "ñ" can be represented by U+00F1 or by "n" plus the combining tilde U+0303
- string comparison does not treat different code point sequences as equal, and their lengths can differ
- normalize() converts a string into a common normalized form for sequences that represent the same characters
- NFD and NFC produce the same form for canonically equivalent strings
- NFD gives the decomposed form, splitting single code points into multiple combining ones
- NFC gives the composed form, replacing multiple code points with single code points where possible
- canonically equivalent sequences should always have the same visual appearance and behavior
- NFKD and NFKC produce the same form for compatible strings
- compatibility includes cases such as the ligature U+FB00 for "ﬀ" and the symbol U+24B9 for "Ⓓ"
- compatibility normalization should be chosen with care because the result may suit search but not display
