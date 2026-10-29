---
title: "[C#] Remove diacritics (accents) from a string"
date: '2015-10-08T19:11:01-03:00'
category: webclip
summary: 'The post shows a C# extension method that removes diacritics by normalizing to Form D, filtering out non-spacing marks, then normalizing back to Form C.'
tags: ["csharp", "unicode", "string-normalization"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "[C#] Remove diacritics (accents) from a string"
    url: "http://www.levibotelho.com/development/c-remove-diacritics-accents-from-a-string/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-10/levibotelho-com--csharp-remove-diacritics-from-a-string.md"
    kind: repo
---

Removing diacritics from a string is a common task, and the post shows a simple extension method for doing it in .NET. The method first checks for null or whitespace, then normalizes the text, removes characters classified as non-spacing marks, and normalizes the result again.

## Reading notes

- The .NET framework does not have a built-in method for removing diacritics from a string.
- Normalization Form D decomposes precomposed characters into their component code points.
- After normalization, the method filters out code points whose Unicode category is NonSpacingMark.
- The rebuilt string is normalized again with Normalization Form C before being returned.
- The post explains that normalization is used here to separate accents from the input string, not to compare strings for equality.
