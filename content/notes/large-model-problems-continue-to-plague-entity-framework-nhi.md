---
title: "Large Model Problems Continue to Plague Entity Framework, NHibernate"
date: '2016-01-11T09:06:15-03:00'
category: webclip
summary: 'The page says Entity Framework gets much slower as EDMX models grow, and that NHibernate shows similar slowdowns when change tracking and relationships are involved. AsNoTracking is mentioned as a workaround with limits.'
tags: ["entity-framework", "nhibernate", "performance", "orm"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Large Model Problems Continue to Plague Entity Framework, NHibernate"
    url: "http://www.infoq.com/news/2013/12/EF-Large-Models"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2016-01/infoq-com--large-model-problems-continue-to-plague-entity-framework-nhi.md"
    kind: repo
---

The page says that model size affects Entity Framework performance. In the cited bug report, materializing one entity is much faster than materializing from a richer EDMX with many entity types and associations. It also says the same issue appears in EF 5 and EF 6.

It then describes a workaround using AsNoTracking, while noting that this disables change tracking. Frans Bouma’s comparison is used to show that Entity Framework and NHibernate can take much longer to materialize entities when change tracking is on, and that the slowdown comes from model complexity rather than the size of the result set.

## Reading notes

- Entity Framework gets slower as the EDMX model grows larger.
- A bug report compares one entity type with a richer model containing 67 entity types and 92 associations.
- The same performance issue is said to occur in EF 5 and EF 6.
- AsNoTracking is presented as a workaround, but it makes entities read-only for change tracking purposes.
- Frans Bouma’s benchmark says Entity Framework and NHibernate can be much slower when change tracking is enabled.
- The slowdown is described as coming from the size of the model, especially its relationships, not from the size of the fetched set.
