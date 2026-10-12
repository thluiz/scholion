---
title: "CSS Anti-patterns"
date: '2014-07-06T12:14:31-03:00'
category: webclip
summary: 'Mark Daggett lists common CSS anti-patterns from a large Rails site, including unclear naming, invalid declarations, verbose code, over-specific classes, browser hacks, duplication, unused classes, and over-namespacing.'
tags: ["css", "anti-patterns", "web-development"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "CSS Anti-patterns - Mark Daggett's Blog"
    url: "http://markdaggett.com/blog/2011/12/04/css-anti-patterns/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2014-07/markdaggett-com--css-anti-patterns.md"
    kind: repo
---

Mark Daggett describes CSS problems he kept seeing while refactoring views in a large enterprise Rails site. He says the examples came from that site, but he had seen the same patterns on other projects too, and he groups them as maintainability problems in the CSS and HTML.

## Reading notes

- unclear class names that describe color or appearance instead of the class’s job
- invalid CSS declarations that can break later rules in the cascade
- verbose declarations that can be compacted into one line
- classes that try to do too many jobs instead of one
- browser-specific hacks kept out of the master stylesheet and moved to overrides
- duplicated CSS that should be abstracted into a shared class
- overuse of `!important` as a last-resort override
- copy-pasted blocks that are not adapted into more general code
- unused classes that should be removed during development
- excessive namespacing tied to specific HTML tags that makes CSS brittle
