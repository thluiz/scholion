---
title: "Node.js + MySQL Example: Handling 100's of GigaBytes of Data"
date: '2017-06-08T15:45:39-03:00'
category: webclip
summary: 'The post explains how Node.js and MySQL can handle billions of rows and hundreds of gigabytes by using indexing, user-based tables, and table partitioning to manage retention and deletions.'
tags: ["nodejs", "mysql", "table-partitioning", "large-data"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Node.js + MySQL Example: Handling 100's of GigaBytes of Data | @RisingStack"
    url: "http://blog.risingstack.com/node-js-mysql-example-handling-hundred-gigabytes-of-data/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2017-06/blog-risingstack-com--nodejs-mysql-example-handling-hundred-gigabytes-data.md"
    kind: repo
---

The article argues that MySQL can still fit large-scale workloads if the schema and cleanup strategy are planned well. It discusses when to split data into user-specific tables, when to delete in chunks, and when MySQL table partitioning becomes the better option for time-based retention.

## Reading notes

- The post uses a Node.js and MySQL example to show how to handle billions of rows and hundreds of gigabytes of data.
- The author says the goal is also to help decide whether Node.js and MySQL fit a given use case and how to implement that choice.
- MySQL was chosen for Trace’s distributed tracing data because Postgres was not good at updating rows at the time.
- With good indexing and planning, MySQL can be suitable for problems often associated with NoSQL alternatives.
- InnoDB tables are immutable, so every ALTER TABLE copies data into a new table.
- When each nominal value has a lot of associated data, separate tables named like <user_id>_<entity_name> can reduce individual table size.
- Creating tables per user can also make account removal an O(1) operation.
- If data still needs time-based cleanup after partitioning by users, the article suggests MySQL table partitioning.
- Partitioned tables behave like multiple tables but keep the same interface from the application side.
- The example uses RANGE partitioning on TO_DAYS(created_at), with start and future partitions as safety nets.
- The partition key must be part of the primary key or a unique index.
- The article notes limitations of partitioned tables, including no query cache, no foreign keys for partitioned InnoDB tables, and no FULLTEXT indexes or searches.
- New partitions are created by reorganizing the future partition.
- Old partitions are dropped with ALTER TABLE ... DROP PARTITION.
- The Node.js example uses knex, lodash, dedent, and moment to build partition definitions dynamically.
- Partition creation and removal are based on the current partitions read from information_schema.partitions.
- The script runs hourly so cleanup can happen at least once a day.
- The partition logic also checks that newly created partitions are not older than the current oldest partition.
- The conclusion says MySQL can be used for large data if the system is planned carefully, but partitioning reduces access to some InnoDB features.
