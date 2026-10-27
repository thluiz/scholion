---
title: "MySQL is done. It's the Postgres Age."
date: '2012-05-23T18:34:07-03:00'
category: webclip
summary: 'The post argues that Postgres has absorbed many jobs once split across several tools, from schemaless data and queues to search and geo indexing, while MySQL offers no clear advantage.'
tags: ["postgres", "database", "mysql"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "MySQL is done. It's the Postgres Age. by Jeff Dickey"
    url: "http://dickey.xxx/mysql-is-done-it-s-the-postgres-age"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2012-05/dickey-xxx--mysql-is-done-postgres-age-jeff-dickey.md"
    kind: repo
---

Jeff Dickey argues that Postgres has become the default database choice for many web teams because it now covers features that used to require separate systems. He says this reduces operational complexity and makes Postgres the tool people are praising most in web development.

## Reading notes

- Postgres is described as a relational(-ish) database that is becoming a one-size-fits-all option for databases.
- The post says Postgres can handle schemaless data, array columns, queueing, full-text searching, and geo-spatial indexing.
- Dickey says conversations with users at Rapportive suggest Postgres works well at large scale and would be chosen again from scratch.
- He claims Postgres is the database tool most widely praised in web development.
- The post contrasts the old “right tool for the job” NoSQL view with Postgres absorbing features from other tools inside one platform.
- He says this can remove the need for separate Mongo, RabbitMQ, and Solr systems.
- The downside he notes is that this approach centers the system on one box, which limits scaling and makes the architecture harder to distribute.
- He also says backup is simpler with one box than with multiple data systems.
- The post points out that Postgres supports schema changes inside transactions, concurrent indexing, and window functions.
- Dickey says these features let Postgres do things MySQL cannot.
- He ends by saying MySQL has no reason to be used anymore and asks for a feature MySQL has over Postgres.
