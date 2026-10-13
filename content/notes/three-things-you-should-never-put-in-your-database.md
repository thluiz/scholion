---
title: "Three things you should never put in your database"
date: '2014-06-19T10:01:37-03:00'
category: webclip
summary: 'The article argues that databases should not store files, ephemeral data, or production logs, because these uses slow reads and writes, bloat backups, and waste resources better handled by other tools.'
tags: ["databases", "performance", "logs", "ephemeral-data"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Three things you should never put in your database"
    url: "http://www.revsys.com/blog/2012/may/01/three-things-you-should-never-put-your-database/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2014-06/revsys-com--three-things-you-should-never-put-in-your-database.md"
    kind: repo
---

The article argues that the best way to improve systems is to avoid decisions that hurt maintainability and scaling. It says databases are the wrong place for files, short-lived data, and logs, because those uses make backups larger, slow access, and waste resources that should serve application traffic.

## Reading notes

- Storing images, files, and binary data in the database is slower than using a filesystem and makes backups larger and access more layered.
- For files on disk, the article recommends storing a relative path in the database or using S3 or a CDN.
- Ephemeral data like usage statistics, metrics, GPS locations, session data, and frequent aggregates should use tools better suited to short-lived workloads.
- If a table is routinely deleted by time range with a cron job, the article says the wrong tool is being used.
- For ephemeral workloads, it suggests redis, statsd/graphite, or Riak.
- Logs in a database are described as risky when they share the same production database as other data.
- Even modest logging adds insert load, and verbose logging can overwhelm the production database.
- The article suggests Splunk, Loggly, or rotating flat files for logs.
