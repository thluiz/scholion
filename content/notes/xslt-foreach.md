---
title: "XSLT ForEach"
date: '2015-02-13T18:21:45-03:00'
category: webclip
summary: 'An XSLT 1.0 stylesheet uses a recursive named template to print a numeric range, splitting the interval at the midpoint and recursing on each half until start and end match.'
tags: ["xslt", "recursion", "xml-transformation"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "XSLT ForEach"
    url: "http://stackoverflow.com/questions/9076323/xslt-looping-from-1-to-60"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-02/stackoverflow-com--xslt-foreach.md"
    kind: repo
---

The stylesheet matches the document root, switches output to text, and starts a named template with start and end parameters. The template checks whether the start is within the end, prints the number when both are equal, and otherwise splits the range at the midpoint and calls itself twice.

## Reading notes

- The root template calls `displayNumbers` with `pStart` set to 1 and `pEnd` set to 1000000.
- `displayNumbers` takes two parameters, `pStart` and `pEnd`.
- When `pStart` is not greater than `pEnd`, the template continues.
- If `pStart` equals `pEnd`, it outputs the current number followed by a line break.
- Otherwise, it computes `vMid` as `floor(($pStart + $pEnd) div 2)`.
- It then calls `displayNumbers` for the left half from `pStart` to `vMid`.
- It calls `displayNumbers` again for the right half from `vMid+1` to `pEnd`.
