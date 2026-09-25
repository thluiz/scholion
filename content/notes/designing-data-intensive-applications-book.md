---
title: "Designing Data-Intensive Applications (DDIA) Book"
date: '2026-09-25T17:59:27+01:00'
category: webclip
summary: 'Chapter 1 introduces reliability, scalability, and maintainability as the book’s starting terms, and Chapter 2 compares relational and document models, stressing how data model choice shapes application capabilities.'
tags: ["data-models", "sql", "document-databases", "data-intensive-applications"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Designing Data Intensive Applications (DDIA) Book"
    url: "https://muratbuffalo.blogspot.com/2024/08/designing-data-intensive-applications.html?ref=dailydev"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/muratbuffalo-blogspot-com--designing-data-intensive-applications-book.md"
    kind: repo
---

The post is a reading log for the opening chapters of *Designing Data-Intensive Applications*. Chapter 1 defines reliability, scalability, and maintainability and is described as a warm-up chapter written in an educator’s voice. The author also notes that the book is being revised and quotes the preface’s warning against premature optimization while still choosing the right tool for the job.

Chapter 2 reviews relational and document models. It says the data model strongly affects what software above it can do, explains how SQL and RDBMSes became the default, and outlines why NoSQL and document databases were adopted for scalability, programmer usability, flexible schemas, and better locality. It also notes the tradeoff between document and relational designs, especially around joins, many-to-many relationships, and data duplication.

## Reading notes

- Chapter 1 defines reliability, scalability, and maintainability.
- The chapter is described as engaging because it uses an educator and technical blogger voice.
- The post quotes the preface on avoiding scale you do not need while still choosing the right tool for the job.
- Chapter 2 says the choice of data model strongly affects the capabilities of software above it.
- The relational model is presented as the basis of SQL and as the default by the mid-1980s.
- The post lists network, hierarchical, object, XML, and NoSQL/document databases as challenges to relational dominance.
- NoSQL is tied to scalability, usability for developers, and flexible schemas.
- Document databases reduce impedance mismatch, improve locality, and support schema flexibility.
- Relational databases are better for complex joins and many-to-many relationships.
- Document models fit one-to-many and tree-like structures, but can lead to duplication.
- Relational schemas may require shredding document-like data across multiple tables.
- The post notes that some relational and distributed systems also support locality, including Spanner and Bigtable-like column families.
- SQL is contrasted with JSON-based query languages such as MongoDB’s aggregation pipeline.
