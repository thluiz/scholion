---
title: "Efficient Pagination Using Deferred Joins"
date: '2022-07-26T13:25:07-03:00'
category: webclip
summary: 'The article compares offset/limit and cursor pagination, then shows how deferred joins and covering indexes can make offset/limit fast enough for deep paging in MySQL and Laravel.'
tags: ["pagination", "mysql", "laravel", "covering-indexes"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Efficient Pagination Using Deferred Joins - Aaron Francis"
    url: "https://aaronfrancis.com/2022/efficient-pagination-using-deferred-joins"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2022-07/aaronfrancis-com--efficient-pagination-using-deferred-joins.md"
    kind: repo
---

The article explains why offset/limit pagination gets slower on deep pages, since the database still reads rows it later discards. It contrasts that with cursor pagination, which only moves forward from the last seen record but does not allow direct page access.

It then proposes deferred joins, where the first query fetches only the primary keys with offset and limit, and a second query retrieves the full rows for those keys. The article also shows how covering indexes, multi-column indexes, primary-key behavior in InnoDB, and descending indexes can reduce the work needed for pagination. It includes a Laravel macro example for `fastPaginate` and notes that the technique is not original, but drawn from High Performance MySQL.

## Reading notes

- Offset/limit is easy to use and supports direct access to page numbers, but it becomes slower as the offset grows because the database still has to fetch and discard earlier rows.
- Cursor pagination uses the last seen record as state, so each next query starts after that point and stays fast across many pages, but pages are not directly addressable.
- Deferred joins delay fetching full rows until after the offset and limit have reduced the result set to the current page.
- The pattern uses an inner query that can rely on indexes for pagination, then joins back to the table to retrieve the full records.
- In the Laravel example, the query is simplified to the primary key, paginated normally, and then a second query loads the full rows for the returned keys.
- The article says this approach should preserve the benefits of Laravel's LengthAwarePaginator while using deferred joins.
- Covering indexes let MySQL satisfy a query from the index alone, without reading the underlying rows.
- For pagination, the indexed columns must match the query needs, or the database may fall back to reading rows.
- Multi-column indexes can help pagination, and the `order by` column should be placed at the end of the composite index.
- InnoDB appends the primary key to indexes, which can make some queries fully covered by a single index.
- Descending indexes can help when users mostly sort by newest items, and MySQL 8 supports them.
- The article says the method is not a silver bullet and depends on the data and index design.
- It also notes that the idea comes from High Performance MySQL rather than being a new invention.
