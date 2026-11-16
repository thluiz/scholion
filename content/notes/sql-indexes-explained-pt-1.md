---
title: "SQL Indexes Explained, Pt. 1"
date: '2026-11-16T06:12:46+00:00'
category: webclip
summary: 'The article uses spreadsheet-style exercises to show why sorted access is faster, when sorting helps or hurts, and how these patterns lead to the idea of a database index.'
tags: ["sql", "database-indexes", "query-performance"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "SQL Index Tutorial—Everything Developers Need to Know, Pt. 1 | Toptal®"
    url: "https://toptal.com/database/sql-indexes-explained-pt-1"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/toptal-com--sql-indexes-explained-pt-1.md"
    kind: repo
---

Properly used, SQL indexes can make data retrieval much faster. The article explains this by comparing unsorted reads, sorted reads, and different column orderings in exercises based on hotel reservations, then linking those patterns to how indexes help an RDBMS stop sooner and read less data.

## Reading notes

- The series aims to explain why indexes are used, how modern RDBMSs design them, and which algorithms they use for specific query patterns.
- The exercises only require basic SQL knowledge and basic programming knowledge.
- The first exercise compares scanning all rows with reading a table sorted by ClientID for a query on one client.
- Sorting helps only if the data is already in the needed order; if the data must be sorted first, that cost can outweigh the gain.
- The second exercise counts reservations on one date and shows how a sorted table lets the reader find the first matching row and then count consecutive matches.
- The third exercise looks for guests arriving on two dates at one hotel and compares different sort orders for DateFrom and HotelID.
- Sorting by HotelID and DateFrom lets the reader skip to the hotel, then to the date, and then copy a consecutive block of matching rows.
- Sorting by HotelID only is less efficient because every row for that hotel still needs a date check.
- Sorting by DateFrom and HotelID changes where the skips and matches occur, but still creates blocks of partially matched and fully matched rows.
- The article concludes that the best approach in the exercises is the one that keeps the target rows in one consecutive block.
- The closing points connect these observations to database indexes: a sorted copy of data can speed reads, jumping to the first matching row saves work, and keeping sorted copies for frequent queries is useful.
- It defines an index as an auxiliary data structure that reduces the amount of data accessed during query execution.
- It describes the main use case as finding a range of values on an indexed column, then reading consecutive matching rows and stopping early.
- It notes that indexes may differ by structure, clustering, and partitioning, and that they can store full rows, derived values, or column copies.
- It says a balanced tree is a typical index implementation with sorted leaf levels.
- It states that an appropriate index can significantly improve SELECT performance by reducing data access.
