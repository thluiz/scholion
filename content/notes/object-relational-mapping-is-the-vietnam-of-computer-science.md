---
title: "Object-Relational Mapping is the Vietnam of Computer Science"
date: '2020-02-22T12:11:52+00:00'
category: webclip
summary: 'Jeff Atwood agrees with Ted Neward that ORM has no clean solution. Every workaround involves painful trade-offs, and the costs often show up only later in development.'
tags: ["orm", "object-relational-mapping", "databases", "software-design"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Object-Relational Mapping is the Vietnam of Computer Science"
    url: "https://blog.codinghorror.com/object-relational-mapping-is-the-vietnam-of-computer-science"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/blog-codinghorror-com--object-relational-mapping-is-the-vietnam-of-computer-science.md"
    kind: repo
---

Atwood accepts Ted Neward’s argument that the object/relational mismatch has no good solution. He says developers keep running into the gap between relational databases and object models, and that every proposed fix adds serious trade-offs that may only become clear much later in the project.

## Reading notes

- He describes ORM as a long-standing mismatch between relational models and traditional object models.
- He says there is no good solution to the problem, only approaches with painful trade-offs.
- He lists several possible responses: abandoning objects, embracing object storage, writing manual mapping code, using ORM only for part of the problem, integrating relational ideas into languages, and building frameworks around relational constructs.
- He notes that raw relational access can bypass ORM caching.
- He concludes that the workable choice is to pick one side, either objects or relational databases, so the mapping problem disappears.
