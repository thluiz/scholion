---
url: "https://muratbuffalo.blogspot.com/2024/08/designing-data-intensive-applications.html?ref=dailydev"
captured_at: "2026-09-25T17:59:27+01:00"
title: "Designing Data Intensive Applications (DDIA) Book"
domain: "muratbuffalo-blogspot-com"
---

We started reading this book as part of [Alex Petrov's book club](http://databass.dev/discord). We just got started, so you can join us, by joining the discord channel above. We meet Wednesday's 11am Eastern Time. 

Previously we had read transaction processing book by Grey and Reuters. [This page links to my summaries of that book.](https://muratbuffalo.blogspot.com/2024/08/index-for-transaction-processing-book.html)

## Chp 1. Reliable, Scalable, and Maintainable Applications

I love the diagrams opening each chapter. Beautiful!

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiydFgFMoNlmW2nI8DYWY2lYzd8EaBUfKh0A1puG7NHL9txcdjnpi2BLcZWV2orSFZHX0GaNeBvhCBAWQifPzVXD9r4T5J-pYfRacGpMZqmF6r8AuQ6tsIiCxSCgGT75DLkwrzv5DX-tUH_ge_1XA5qiqL9vlSyyZYGjZTxexydGW1pMQmeD_we-GNdZ4A/s320/Screenshot%202024-08-06%20at%2012.40.58%E2%80%AFPM.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiydFgFMoNlmW2nI8DYWY2lYzd8EaBUfKh0A1puG7NHL9txcdjnpi2BLcZWV2orSFZHX0GaNeBvhCBAWQifPzVXD9r4T5J-pYfRacGpMZqmF6r8AuQ6tsIiCxSCgGT75DLkwrzv5DX-tUH_ge_1XA5qiqL9vlSyyZYGjZTxexydGW1pMQmeD_we-GNdZ4A/s1552/Screenshot%202024-08-06%20at%2012.40.58%E2%80%AFPM.png)

The first chapter consists of warm up stuff. It talks about the definitions of reliabilty, scalability, and maintainability. It is still engaging, because  it is written with an educator and technical blogger voice, rather than a dry academic voice.

This book came out on 2017. Martin is working on the new version. So if you have comments for things to focus on for the new version, it would be helpful to collect them in a document and email it to Martin. For example, I am curious about how the below paragraph from the Preface will get revised with 8 more years of hindsight:

"Sometimes, when discussing scalable data systems, people make comments along the lines of, “You’re not Google or Amazon. Stop worrying about scale and just use a relational database.” There is truth in that statement: building for scale that you don’t need is wasted effort and may lock you into an inflexible design. In effect, it is a form of premature optimization. However, it’s also important to choose the right tool for the job, and different technologies each have their own strengths and weaknesses. As we shall see, relational databases are important but not the final word on dealing with data."

## Chp 2. Data Models and Query Languages

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhSC6uLe9PGszNkYuc1Vp87IgN4FzUnVdcjZilKiTQmlJNdXfa3eTYn8KIXVRdhaZID-JMBfOsDQgNwsh5Ox5CeXgRv-UR6B-CHBKGNpkhX6_wRyRm4G9DT0QSBuW1wJgM4OfGjOPF87pdc-46G2Gjt-cFF1gasc1-y6nMwfirecVCKsvVdSLKsGoM0Yjc/w400-h266/Screenshot%202024-08-06%20at%2012.42.43%E2%80%AFPM.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhSC6uLe9PGszNkYuc1Vp87IgN4FzUnVdcjZilKiTQmlJNdXfa3eTYn8KIXVRdhaZID-JMBfOsDQgNwsh5Ox5CeXgRv-UR6B-CHBKGNpkhX6_wRyRm4G9DT0QSBuW1wJgM4OfGjOPF87pdc-46G2Gjt-cFF1gasc1-y6nMwfirecVCKsvVdSLKsGoM0Yjc/s1494/Screenshot%202024-08-06%20at%2012.42.43%E2%80%AFPM.png)

The choice of data model significantly impacts the capabilities of software above it. This chapter provides a really nice and objective review of the landscape. 

### Relational Model and SQL

The relational model, proposed by Edgar Codd in 1970, forms the basis of SQL. It organizes data into relations (tables) containing tuples (rows). Relational databases were first deployed for business data processing on 1960s-70s mainframes. They simplified data management by hiding implementation details behind a clean interface. By the mid-1980s, relational database management systems (RDBMSes) and SQL became the defacto tools for data storage and querying.

Various models challenged the relational model's dominance:

*   Network and hierarchical models (1970s-early 1980s)
*   Object databases (late 1980s-early 1990s)
*   XML databases (early 2000s)
*   NoSQL/Document databases (2010s)

## Document Databases and NoSQL

NoSQL arose from the need for greater scalability, usability (especially programmability by developers), and desire for more flexible schemas.

Let's double-click on usability/programmability. If data is stored in relational tables, an awkward translation layer is required between the objects in the application code and the database model of tables, rows, and columns. Object-relational mapping (ORM) frameworks try to alleviate this impedance mismatch, and reduce the amount of boilerplate code required for this translation layer, but they can’t completely hide the differences between the two models.

To address this issues, document databases store data in a JSON-like format, and provide:

*   Reduced "impedance mismatch" between application code and storage layer
*   Better data locality
*   Schema flexibility

However, they face challenges with complex joins and many-to-many relationships.

## Relational vs. Document Model

The choice between relational and document models depends on the application's needs:

*   Document model excels for one-to-many relationships and tree-like structures
*   Relational model is better for complex joins and many-to-many relationships

Or, dually, Document databases might lead to data duplication, while relational databases may require "shredding" document-like structures across multiple tables.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEixid-_d1KGUinrmSZZtgIRX1NiIQIeq0F088Q3KiNldfJ8_K9M7KeP-CGM3NNHcY8HD3OGh319vJXqyD9XNARYOGxv0ZCYpuxjvOAbZSGmJMmNxT3DDPqPKwE7klxcyPocAKJ6_PGuT-j-583tpPnCbQYLgCy5Pcvs9R2wEFgn0IFDyNfy-RkbugYC7So/w640-h614/Screenshot%202024-08-06%20at%2012.46.07%E2%80%AFPM.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEixid-_d1KGUinrmSZZtgIRX1NiIQIeq0F088Q3KiNldfJ8_K9M7KeP-CGM3NNHcY8HD3OGh319vJXqyD9XNARYOGxv0ZCYpuxjvOAbZSGmJMmNxT3DDPqPKwE7klxcyPocAKJ6_PGuT-j-583tpPnCbQYLgCy5Pcvs9R2wEFgn0IFDyNfy-RkbugYC7So/s1686/Screenshot%202024-08-06%20at%2012.46.07%E2%80%AFPM.png)

The JSON representation has better locality than the multi-table schema in Figure 2-1. If you want to fetch a profile in the relational example, you need to either perform multiple queries (query each table by user\_id) or perform a messy multi-way join between the users table and its subordinate tables. In the JSON representation, all the relevant information is in one place, and one query is sufficient.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjyEm6uGVkpPNEFWTUkCRoJ-5wOtlnUX9CmEHPIhTPdFJ9O2vt_YsXszHdSnkgq-IdJ3B4aSh7BShy68Zoj_3InbqE2FY0H4XtizucC0V_HXOmLUUD6BfIsejPQHuIDKQkC_PxJdxd0bmLnKrm9eIIza73C25nSeDjg2C_59xSrQgNMglan-bKlIxRMp8o/w400-h301/Screenshot%202024-08-06%20at%2012.46.25%E2%80%AFPM.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjyEm6uGVkpPNEFWTUkCRoJ-5wOtlnUX9CmEHPIhTPdFJ9O2vt_YsXszHdSnkgq-IdJ3B4aSh7BShy68Zoj_3InbqE2FY0H4XtizucC0V_HXOmLUUD6BfIsejPQHuIDKQkC_PxJdxd0bmLnKrm9eIIza73C25nSeDjg2C_59xSrQgNMglan-bKlIxRMp8o/s1710/Screenshot%202024-08-06%20at%2012.46.25%E2%80%AFPM.png)

While document databases are known for data locality, some relational databases also offer this feature. For example, Google Spanner's tables allow nesting of related data and the column-family concept in the Bigtable data model (used in Cassandra and HBase) also aim to improve locality.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj7Iumwjh-BfnnPYG4LLLZGu-DGBzlKrBD7fT1IDWuz615Tw1_3rL5fV0PDDcZe6xLf6BHI3o42ZnwQiTAgS5apqzN1f6t3gh-rIUszZnin23OZ8gwq43BoWI7-ulcAJ_enaOrgO53EUPFir0RPfBX3Us0goDMoFCcdPVeo-gd28bbiPHsioAjD6ru-2yU/w400-h198/Screenshot%202024-08-06%20at%2012.46.52%E2%80%AFPM.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj7Iumwjh-BfnnPYG4LLLZGu-DGBzlKrBD7fT1IDWuz615Tw1_3rL5fV0PDDcZe6xLf6BHI3o42ZnwQiTAgS5apqzN1f6t3gh-rIUszZnin23OZ8gwq43BoWI7-ulcAJ_enaOrgO53EUPFir0RPfBX3Us0goDMoFCcdPVeo-gd28bbiPHsioAjD6ru-2yU/s1666/Screenshot%202024-08-06%20at%2012.46.52%E2%80%AFPM.png)

Query languages also vary between models. SQL uses an English-sentence-style syntax, while document databases often use JSON-based query languages. For instance, MongoDB's aggregation pipeline language is similar in expressiveness to a subset of SQL but uses a JSON-based syntax.

UPDATE (December 2024): [Here is the index for the DDIA chapters](https://muratbuffalo.blogspot.com/2024/12/index-for-designing-data-intensive.html) after having gone through the book!
