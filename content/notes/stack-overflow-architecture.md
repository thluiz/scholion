---
title: "Stack Overflow Architecture"
date: '2015-05-07T22:18:37-03:00'
category: webclip
summary: 'The page argues that Stack Overflow shows how a scale-up strategy can work well for a two-tier CRUD application on a Microsoft stack, while also noting the limits of that choice, the cost of licensing, and the difficulties of NoSQL and multitenancy.'
tags: ["stack-overflow", "scale-up", "microsoft-stack", "multitenancy"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Stack Overflow Architecture - High Scalability -"
    url: "http://highscalability.com/stack-overflow-architecture"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-05/highscalability-com--stack-overflow-architecture.md"
    kind: repo
---

Stack Overflow is presented as a case where scale up remains a practical choice. The page says the site uses a Microsoft stack, keeps the web and database tiers separate, and adds larger machines and more memory when it needs more capacity. It also frames the site as a useful example for comparing scale up, scale out, and NoSQL tradeoffs.

## Reading notes

- Stack Overflow is described as a two-tier site with direct database access from the web server code.
- The platform listed includes ASP.NET MVC, SQL Server 2008, Visual Studio 2008 Team Suite, jQuery, LINQ to SQL, and Subversion.
- The web tier and database tier run on Lenovo ThinkServer machines, with a QNAP NAS used for backups.
- The site search relies heavily on SQL Server full-text search.
- The article says the bottleneck is the database most of the time.
- It argues that buying hardware can be better than renting when you can manage servers yourself.
- It says memory is cheap and should be maxed out for near-free performance gains.
- It says CPU speed matters a lot for the database server, with query times improving as clocks rise.
- It notes that network equipment can become the main cost driver at low server volumes.
- It recommends separating application and database duties so they can scale independently.
- It says applications should keep state in the database so they can scale horizontally.
- It warns that scale up has limited redundancy and that clusters become expensive when machines are already expensive.
- It says few applications scale linearly with processor count because locks reduce the benefit of big iron.
- It describes NoSQL as hard because many common database features have to be built manually.
- It explains that transactions in many NoSQL systems do not span arbitrary boundaries.
- It raises multitenancy as a harder problem than it first appears, especially for customization and upgrades.
- It uses Salesforce as an example of a wide, sparse table design for multitenancy.
