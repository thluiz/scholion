---
title: "What the hell is <!DOCTYPE html>?"
date: '2022-07-08T15:54:00-03:00'
category: webclip
summary: 'The page explains that HTML5 no longer needs a DTD reference, but the doctype still tells browsers to use standard mode instead of quirks mode.'
tags: ["doctype", "html5", "quirks-mode", "standards-mode"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "What the hell is <!DOCTYPE html>? - DEV Community"
    url: "https://dev.to/aman894/what-the-hell-is-doctype-html-32om"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2022-07/dev-to--what-the-hell-is-doctype-html.md"
    kind: repo
---

The page says that older HTML documents used a doctype declaration with a reference to a DTD, which described the document structure and the valid elements it could contain. It then explains that HTML5 no longer needs that SGML-based reference, but the doctype still matters because it tells browsers to run the page in standard mode.

## Reading notes

- A DTD describes the structure of an XML document and the legal elements it can contain.
- Before HTML5, HTML documents used a doctype declaration with a DTD reference on the first line.
- That declaration provided the list of valid elements and identified whether the DTD was strict, transitional, or frameset.
- HTML5 no longer needs a DTD reference because it is not SGML based.
- In HTML5, `<!DOCTYPE html>` tells the browser to use standard mode.
- Without a valid doctype on the first line, the browser may switch to quirks mode.
- The page links quirks mode to older browsers and to legacy code that broke when standards-based behavior became common.
