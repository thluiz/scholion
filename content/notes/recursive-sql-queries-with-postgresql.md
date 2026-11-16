---
title: "Recursive SQL Queries with PostgreSQL"
date: '2020-04-20T21:22:37+00:00'
category: webclip
summary: 'The article explains recursive CTEs in PostgreSQL, shows how they traverse employee hierarchies and graphs, and notes that recursive queries can also generate infinite streams and recursive views.'
tags: ["postgresql", "recursive-cte", "sql", "graphs"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Recursive SQL Queries with PostgreSQL"
    url: "https://dev.to/martinheinz/recursive-sql-queries-with-postgresql-1i6h"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/dev-to--recursive-sql-queries-with-postgresql.md"
    kind: repo
---

Recursive CTEs are presented as a way to handle self-referential data and tree-like or graph-like structures in SQL. The article first shows the formal `WITH RECURSIVE` pattern, then uses employee hierarchies and graph edges to demonstrate how recursion can build paths, levels, and repeated expansions.

## Reading notes

- Recursive queries are useful for self-referential data and tree-like data structures, such as manager-subordinate relationships, category hierarchies, flight maps, taxonomies, article links, and comment threads.
- Recursive queries use a CTE, or common table expression, introduced with the SQL `WITH` clause to make complex queries more readable.
- A recursive SQL query has a non-recursive part and a recursive part joined with `UNION` or `UNION ALL`.
- In the simple numeric example, the base case selects `1`, and the recursive part adds `1` until the `WHERE` clause stops the recursion.
- An employee table with a self-referencing `manager_id` column is used to model a manager-subordinate hierarchy.
- A recursive query can return the subtree under a given employee, using a `level` column to show depth in the hierarchy.
- The same hierarchy can be used to compute degrees of separation between two employees.
- A recursive query can also work from the bottom up, producing a job progression path such as `Developer > Manager > VP > CEO`.
- For graphs, the article uses an `edges` table with `src` and `dest` columns.
- PostgreSQL arrays are used to store paths, concatenate visited nodes, and avoid cycles by checking that a new destination is not already in the path.
- Recursive queries can generate infinite streams of rows, and `LIMIT` can safely return only the first rows from such a query.
- PostgreSQL can also create recursive views, which the article describes as syntax sugar for recursive queries.
