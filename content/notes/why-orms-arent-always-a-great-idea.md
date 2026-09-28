---
title: "Why ORMs Aren't Always a Great Idea"
date: '2022-07-19T17:48:08-03:00'
category: webclip
summary: 'The post argues that ORMs can speed up development and help beginners, but they also hide database behavior, limit control, and can hurt performance and maintenance as systems grow.'
tags: ["orms", "sql", "database-performance", "software-development"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Why ORMs Aren't Always a Great Idea - DEV Community"
    url: "https://dev.to/harshhhdev/why-orms-arent-always-a-great-idea-41kg"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2022-07/dev-to--why-orms-arent-always-a-great-idea.md"
    kind: repo
---

The post argues that ORMs are useful in some situations, especially for quick development and for beginners, but that they are not always the best choice for relational databases. It says SQL already gives a direct way to work with databases, while ORMs add an abstraction that can hide database features, reduce control over queries, and create maintenance costs later.

It also says ORMs can make simple CRUD work easier and can reduce the risk of SQL injection for beginners, but they may cause performance problems such as extra queries, weak joins, and the N+1 selects issue. The conclusion is that ORMs should be used carefully and not treated as a silver bullet.

## Reading notes

- ORMs are presented as an abstraction layer between relational databases and applications.
- The post says ORMs reduce database features to a lowest common denominator across systems.
- It argues that relational databases are not arbitrarily interchangeable and have different strengths and weaknesses.
- It says ORMs are decent for simple CRUD operations, but many real applications need more than that.
- It claims the time saved early with ORMs can become maintenance cost later as a startup grows.
- It says ORMs can lead to extra queries, weaker performance, and sub-par JOINs.
- It describes the N+1 selects problem as a common ORM issue.
- It argues that ORMs obscure how the underlying database works and can limit learning.
- It notes that raw SQL access exists in some ORMs, but says that using SQL directly can still be just as practical.
- It says ORMs can save development time in hackathons and similar short-term projects.
- It says beginners may use ORMs to avoid SQL complexity and reduce the risk of SQL injection.
- It concludes that ORMs are useful tools in the right context, but not a silver bullet.
