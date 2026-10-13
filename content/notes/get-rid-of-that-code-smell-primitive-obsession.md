---
title: "Get Rid of That Code Smell – Primitive Obsession"
date: '2012-06-26T10:30:46-03:00'
category: webclip
summary: 'Primitive Obsession happens when primitive Ruby objects are used in places where they do not fit the domain. The post recommends replacing them with rich objects that carry the right semantics and API.'
tags: ["primitive-obsession", "ruby", "oop", "rich-objects"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Get Rid of That Code Smell – Primitive Obsession | solnic.eu"
    url: "http://solnic.eu/2012/06/25/get-rid-of-that-code-smell-primitive-obsession.html"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2012-06/solnic-eu--get-rid-of-that-code-smell-primitive-obsession.md"
    kind: repo
---

Primitive Obsession is described as a common Ruby code smell that appears when Array, String, Fixnum, or Float are used in domain-specific places where they do not fit semantically. The post uses examples such as a string for a URI, a float for money, and a hash for a set of objects, and says the problem is using convenient primitives where a domain object would be more accurate.

## Reading notes

- Primitive Obsession appears when primitive Ruby objects are used intensively in places where their semantics do not match the domain.
- The post says there are no tools it knows of that can reliably detect this smell, so the reader has to rely on domain understanding and manual analysis.
- Monkey patching primitive classes is mentioned as a possible smell indicator.
- The Virtus example shows a Hash being used to represent a set of attributes because it gives easy `#[]` access.
- The post says that approach is a mistake because the real need is set semantics plus methods to add and merge attributes.
- The replacement in Virtus is `Virtus::AttributeSet`, a richer object built for attributes.
- `AttributeSet` exposes a smaller API than Hash and also handles attributes inherited from a parent.
- The closing advice is to use rich domain objects such as `Money`, `Configuration`, or `GeoLocation` instead of spreading primitive values through the code.
