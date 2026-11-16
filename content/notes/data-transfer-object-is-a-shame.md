---
title: "Data Transfer Object Is a Shame"
date: '2020-02-22T12:11:52+00:00'
category: webclip
summary: 'The page argues that DTOs violate encapsulation by exposing data across procedures, turning object-oriented code into procedural code. It prefers objects that keep data inside and save or print themselves.'
tags: ["dto", "encapsulation", "object-oriented-programming", "procedural-code"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Data Transfer Object Is a Shame"
    url: "https://yegor256.com/2016/07/06/data-transfer-object.html"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/yegor256-com--data-transfer-object-is-a-shame.md"
    kind: repo
---

The page argues that a DTO goes against object-oriented programming because it makes data visible outside the object. In the example, a book is loaded from a REST API, passed through code that reads its fields, and then saved with JDBC, which turns the object into a passive data holder.

The alternative presented is to keep the data inside the object and let it act on itself, such as saving itself to a database or printing itself to some medium. The main claim is that DTOs make object-oriented code behave like procedural code.

## Reading notes

- DTO is presented as a design choice that conflicts with encapsulation.
- In OOP, data should stay hidden behind objects, and objects should not access other objects’ internal data.
- The example shows a book loaded from a REST API and later written to a database through field access.
- That book is described as a passive data structure that only transfers data between procedures.
- A better design shown in the page calls a method on the book itself, such as `save(database)`.
- Another variant keeps the object in control by using a fluent database API inside `save()`.
- The page says the data should never escape the `book` object.
- Objects may save themselves or print themselves, but the page rejects getting data out of them.
- DTO is described as turning object-oriented code into procedural code.
- The page also lists other names often used for DTOs, including business objects, domain objects, entity objects, and JavaBeans.
