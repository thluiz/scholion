---
title: "Notes on \"Engineering Principles for Building Financial Systems\""
date: "2026-09-23T17:31:11+01:00"
category: webclip
has_commentary: false
tags:
  - financial-systems
  - accounting-bugs
  - distributed-systems
summary: "A one-cent summation error across ten million transactions becomes a $100k discrepancy, and the same drift pattern shows up in any system that keeps a running counter."
sources:
  - title: "Notes on \"Engineering Principles for Building Financial Systems\""
    url: "https://advancedweb.hu/shorts/notes-on-engineering-principles-for-building-financial-systems/?ref=dailydev"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/advancedweb-hu--notes-on-engineering-principles-for-building-financial-systems.md"
    kind: repo
---

Tamás Sallai's notes reduce financial systems to three goals: accurate, auditable, timely. Most of the piece dwells on the first one, and on how small bugs break it. A summation error that looks like nothing at the scale of one transaction can pass every check, because everything appears to work, and only becomes visible once it has been added enough times to matter.

The pattern extends past finance. Any system carrying a running counter can drift the same way. A reference count enforcing a foreign key in DynamoDB, for instance, can go out of sync until it blocks deletion of the parent entity, and someone fixes it by hand.

## Fichamento

- The three goals of an accounting system: accurate, auditable, timely.
- Summation bugs are dangerous because they're invisible at the single-transaction scale; everything "works" until the error has compounded enough to show.
- Ten million transactions off by one cent adds up to a $100k discrepancy, material enough to draw tax authorities' attention.
- The later a summation bug is caught, the harder it is to attribute: you can see something is off, not where the discrepancy originated.
- The same failure mode appears outside finance. A counter enforcing foreign keys in DynamoDB can drift out of sync, block deletion of the parent entity, and get patched by hand-editing data.
