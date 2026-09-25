---
title: "Implementing rod-cutting"
date: '2025-03-14T16:03:23-03:00'
category: webclip
summary: 'The article compares how the bottom-up rod-cutting algorithm translates from pseudocode into Python, Java, and F#, and argues that ceremony depends on the language and style, not just dynamic versus static typing.'
tags: ["rod-cutting", "python", "java", "fsharp"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Implementing rod-cutting"
    url: "https://blog.ploeh.dk/2024/12/23/implementing-rod-cutting/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2025-03/blog-ploeh-dk--implementing-rod-cutting.md"
    kind: repo
---

The article compares the bottom-up rod-cutting algorithm from *Introduction to Algorithms* across Python, Java, and F#. It shows that the pseudocode maps directly to each language, but the amount of ceremony differs, with Python and F# feeling lighter than Java in this example.

## Reading notes

- The article continues the discussion from *Implementation and usage mindsets* and uses the rod-cutting algorithm as the example.
- The price table is treated as one-indexed, so a leading zero is added when using zero-indexed arrays.
- For a rod of length 10, the best revenue is 30 with no cut.
- For a rod of length 7, there are two optimal solutions: 1 + 6 and 2 + 2 + 3, both with revenue 18.
- The pseudocode returns two arrays, `r` for maximum revenues and `s` for best cut positions.
- Python implements the algorithm directly, with the main hurdles being array initialization and negative infinity.
- Java needs more ceremony, including explicit types, a custom result class, and a more verbose setup.
- The article notes that Java’s static typing is not the only source of ceremony; tooling and data modeling also matter.
- F# also translates the algorithm closely, despite requiring an annotation for the array parameter and `mutable` values for the loop variables.
- The interactive F# session prints cuts at positions 1 and 6 for the sample rod of length 7.
- The conclusion is that F# can be as implementation-friendly as Python in this kind of task, while Java introduces more friction here.
