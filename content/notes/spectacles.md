---
title: "Spectacles"
date: '2016-01-02T12:40:38-03:00'
category: webclip
summary: 'Spectacles adds database view support to ActiveRecord, with migrations, an abstract view class, and support for several database drivers. It also offers PostgreSQL materialized views with refresh and creation options.'
tags: ["activerecord", "database-views", "postgresql", "materialized-views"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "liveh2o/spectacles"
    url: "https://github.com/liveh2o/spectacles"
    kind: repo
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2016-01/github-com--spectacles.md"
    kind: repo
---

Spectacles adds database view functionality to ActiveRecord and is built to work with Rails 3.2+. It lets you create views in migrations in a format similar to tables and defines an abstract view class for view-backed models.

It supports SQLite, MySQL, MySQL2, PostgreSQL, and Vertica drivers. For PostgreSQL, it also supports materialized views, including refreshes and options such as force, data, columns, tablespace, and storage.

## Reading notes

- Adds database view support to ActiveRecord
- Is built for Rails 3.2+
- Creates views in migrations with a table-like format
- Provides an abstract view class for models backed by views
- Works with SQLite, MySQL, MySQL2, PostgreSQL, and Vertica drivers
- Supports materialized views only on PostgreSQL
- Materialized views cache results and need manual refresh after source data changes
- `create_materialized_view` accepts `force`, `data`, `columns`, `tablespace`, and `storage` options
