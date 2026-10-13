---
title: "Protecting against XML Entity Expansion attacks"
date: '2013-12-05T11:01:05-03:00'
category: webclip
summary: 'The post explains that untrusted XML can trigger entity expansion during parsing and consume huge CPU resources. It recommends using XmlReader first, disabling resolvers, and limiting document size before parsing into XmlDocument.'
tags: ["xml-security", "entity-expansion", "xmldocument", "xmlreader"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Protecting against XML Entity Expansion attacks - Tom Hollander's blog - Site Home - MSDN Blogs"
    url: "http://blogs.msdn.com/b/tomholl/archive/2009/05/21/protecting-against-xml-entity-expansion-attacks.aspx"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2013-12/blogs-msdn-com--protecting-against-xml-entity-expansion-attacks.md"
    kind: repo
---

The post argues that input validation is a basic defense and that untrusted XML should be treated as malicious unless proven otherwise. It describes how a document that looks small and well formed can expand into an enormous amount of text during parsing and cause denial of service.

## Reading notes

- Input validation is presented as the basic defense against security attacks, and all uncontrolled input should be treated as malicious unless proven otherwise.
- The author describes an XML file received from the Internet that was checked with schema validation and a digital signature, yet still exposed a missed attack class.
- Untrusted XML should never be loaded into XmlDocument as the first step, because parsing alone can trigger a meltdown.
- The example shows nested custom entities that expand repeatedly until a small XML document becomes extremely large.
- The impact described is denial of service through heavy CPU consumption rather than data theft.
- The suggested defense is to use XmlReader before XmlDocument, or instead of it when a fully parsed document is not needed.
- The sample configuration sets XmlResolver to null and MaxCharactersInDocument to 10000.
- If parsing with XmlReader finishes without XmlException, the document is treated as safe to parse further, but normal validation and encoding still remain necessary.
