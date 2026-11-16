---
title: "Printers Instead of Getters"
date: '2020-02-22T12:11:52+00:00'
category: webclip
summary: 'The page argues that objects should not expose state through getters. Instead, they should print themselves to a format, or accept a media object that receives the data.'
tags: ["getters", "object-oriented-design", "serialization", "media"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Printers Instead of Getters"
    url: "https://yegor256.com/2016/04/05/printers-instead-of-getters.html"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/yegor256-com--printers-instead-of-getters.md"
    kind: repo
---

The page argues that getters turn objects into public bags of data and reflect a procedural habit of trusting data instead of the object. It proposes printers as an alternative, so an object produces XML, JSON, or other output itself.

## Reading notes

- Getters and setters are treated as an anti-pattern, and the text says there is no need to keep arguing about that.
- Instead of exposing data through getters, an object should have the ability to print itself to some media.
- A `Book` example shows the traditional getter approach used with JAXB to produce XML.
- The text says this exposes the object’s internals and turns it into a bag of data.
- The convenience of getters is attributed to procedural thinking and to not trusting objects.
- The proposed alternative is a `toXML()` printer method on the object itself.
- The same idea is extended to `toJSON()` when another format is needed.
- If many formats are required, the text says the object can become too large.
- To avoid that, it proposes a `Media` object that accepts data through a `print(Media media)` method.
- A `JsonMedia` example shows the media accumulating fields and later producing a JSON object.
- The final point is that different media can handle different formats while the `Book` class stays small.
