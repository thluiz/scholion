---
url: "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/normalize"
captured_at: "2026-11-16T02:20:22+00:00"
title: "String.prototype.normalize() - JavaScript | MDN"
domain: "developer-mozilla-org"
---

## [Try it](#try_it)

## [Syntax](#syntax)

### [Parameters](#parameters)

[`form` Optional](#form)

One of `"NFC"`, `"NFD"`, `"NFKC"`, or `"NFKD"`, specifying the Unicode Normalization Form. If omitted or [`undefined`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined), `"NFC"` is used.

These values have the following meanings:

[`"NFC"`](#nfc)

Canonical Decomposition, followed by Canonical Composition.

[`"NFD"`](#nfd)

Canonical Decomposition.

[`"NFKC"`](#nfkc)

Compatibility Decomposition, followed by Canonical Composition.

[`"NFKD"`](#nfkd)

Compatibility Decomposition.

### [Return value](#return_value)

A string containing the Unicode Normalization Form of the given string.

### [Exceptions](#exceptions)

[`RangeError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RangeError)

Thrown if `form` isn't one of the values specified above.

## [Description](#description)

Unicode assigns a unique numerical value, called a _code point_, to each character. For example, the code point for `"A"` is given as U+0041. However, sometimes more than one code point, or sequence of code points, can represent the same abstract character — the character `"ñ"` for example can be represented by either of:

*   The single code point U+00F1.
*   The code point for `"n"` (U+006E) followed by the code point for the combining tilde (U+0303).

However, since the code points are different, string comparison will not treat them as equal. And since the number of code points in each version is different, they even have different lengths.

The `normalize()` method helps solve this problem by converting a string into a normalized form common for all sequences of code points that represent the same characters. There are two main normalization forms, one based on **canonical equivalence** and the other based on **compatibility**.

### [Canonical equivalence normalization](#canonical_equivalence_normalization)

In Unicode, two sequences of code points have canonical equivalence if they represent the same abstract characters, and should always have the same visual appearance and behavior (for example, they should always be sorted in the same way).

You can use `normalize()` using the `"NFD"` or `"NFC"` arguments to produce a form of the string that will be the same for all canonically equivalent strings. In the example below we normalize two representations of the character `"ñ"`:

#### Composed and decomposed forms

Note that the length of the normalized form under `"NFD"` is `2`. That's because `"NFD"` gives you the **decomposed** version of the canonical form, in which single code points are split into multiple combining ones. The decomposed canonical form for `"ñ"` is `"\u006E\u0303"`.

You can specify `"NFC"` to get the **composed** canonical form, in which multiple code points are replaced with single code points where possible. The composed canonical form for `"ñ"` is `"\u00F1"`:

### [Compatibility normalization](#compatibility_normalization)

In Unicode, two sequences of code points are compatible if they represent the same abstract characters, and should be treated alike in some — but not necessarily all — applications.

All canonically equivalent sequences are also compatible, but not vice versa.

For example:

*   the code point U+FB00 represents the [ligature](https://developer.mozilla.org/en-US/docs/Glossary/Ligature) `"ﬀ"`. It is compatible with two consecutive U+0066 code points (`"ff"`).
*   the code point U+24B9 represents the symbol `"Ⓓ"`. It is compatible with the U+0044 code point (`"D"`).

In some respects (such as sorting) they should be treated as equivalent—and in some (such as visual appearance) they should not, so they are not canonically equivalent.

You can use `normalize()` using the `"NFKD"` or `"NFKC"` arguments to produce a form of the string that will be the same for all compatible strings:

When applying compatibility normalization it's important to consider what you intend to do with the strings, since the normalized form may not be appropriate for all applications. In the example above the normalization is appropriate for search, because it enables a user to find the string by searching for `"f"`. But it may not be appropriate for display, because the visual representation is different.

As with canonical normalization, you can ask for decomposed or composed compatible forms by passing `"NFKD"` or `"NFKC"`, respectively.

## [Examples](#examples)

### [Using normalize()](#using_normalize)

## [Specifications](#specifications)

Specification

[ECMAScript® 2027 Language Specification  
\# sec-string.prototype.normalize](https://tc39.es/ecma262/multipage/text-processing.html#sec-string.prototype.normalize)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

*   [Unicode Standard Annex #15, Unicode Normalization Forms](https://www.unicode.org/reports/tr15/ "External link (opens in new tab)")
*   [Unicode equivalence](https://en.wikipedia.org/wiki/Unicode_equivalence "External link (opens in new tab)") on Wikipedia
