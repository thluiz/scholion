---
url: "https://www.toptal.com/database/sql-indexes-explained-pt-3?utm_campaign=Toptal%20Engineering%20Blog&utm_medium=email&_hsmi=126740665&_hsenc=p2ANqtz-9sS4sxGELfMUlRjNSgmtXMXH8FExvKOAQPwnRqCPjUk1Y_p4P7LiYeMwsSmiKIbx6Ocs7MQ43xErIaSfXjdA6pHjrtlA&utm_content=126740665&utm_source=hs_email"
captured_at: "2021-06-14T09:27:08-03:00"
title: "Solving SQL Bottlenecks (SQL Indexes Explained, Pt. 3) | Toptal"
domain: "toptal-com"
---

# Solving Bottlenecks With SQL Indexes and Partitions

[Mirko Marović](https://www.toptal.com/resume/mirko-marovic)

Mirko designs and develops massive, extreme-workload databases. He also trains software developers on databases and SQL.

In [the first lesson](https://www.toptal.com/database/sql-indexes-explained-pt-1) of SQL Indexes Explained, we learned that `SELECT` queries are faster when the data is already ordered by values of specific columns.

In [the second lesson](https://www.toptal.com/database/sql-indexes-explained-pt-2), we learned the basic structure of B-tree indexes and how to use them to reduce the volume of data we access while executing a query. We also figured out how to implement queries joining multiple tables and how indexes can speed up such queries.

We also highlighted two scenarios where the use of indexes in SQL is helpful. When indexes are covering indexes, containing all columns from the query—from `WHERE` conditions, `JOIN` conditions, and the `SELECT` list—we avoid reading the corresponding table entirely. Alternatively, indexes can help when they reduce the number of data blocks accessed to a small fraction of the table size.

Otherwise, it’s more efficient to scan the whole table than to read from an index and jump randomly back and forth to the corresponding table rows.

## SQL Range Queries

The queries that can take advantage of indexes typically include conditions that significantly reduce the range of possible values one or more columns can take. Range queries restrict data based on conditions like “the value of Column A must be between X and Y.”

A good example of this is the query from Exercise 4 of the second lesson:

```
SELECT c.ClientName
FROM Reservations r
JOIN Clients c ON r.ClientID = c.ClientID
WHERE r.DateFrom BETWEEN (
    TO_DATE('2020-08-13', 'YYYY-MM-DD') AND
    TO_DATE('2020-08-14', 'YYYY-MM-DD')
  ) AND
  r.HotelID = 3;
```

Here we have two ranges. The first one is the range of dates, the period between August 13, 2020, and August 14, 2020. The second one is the smallest possible numeric range. The condition is equivalent to `r.HotelID BETWEEN 3 AND 3`.

## Exercise 1: Periods (Date and Time Range Queries)

Let’s add a column called `CheckInTime` to the `Reservations` table. You can see sample data in [this spreadsheet](https://docs.google.com/spreadsheets/d/1k4fVxH5BDM3dzYiaDSFHZYyx9KrzJiD4G0uih6U8heU/edit#gid=0). Notice there’s a single index covering both `CheckInTime` and `ClientId`.

Write a query that would return the names of clients who checked in on August 15, 2020.

Inexperienced SQL developers usually write the following query:

```
SELECT c.ClientName
FROM Reservations r
JOIN Clients c ON r.ClientID = c.ClientID
WHERE TO_DATE(r.CheckInTime, 'YYYY-MM-DD') = '2020-08-15';
```

They assume that query execution would look like this:

```
Get first row from IX_CheckInTime_ClientID where
  TO_DATE(CheckInTime, 'YYYY-MM-DD') = '2020-08-15'

While found and TO_DATE(CheckInTime, 'YYYY-MM-DD') = '2020-08-15' 
  Fetch Clients.* where ClientID = IX_CheckInTime_ClientID.ClientID
  Write down Clients.ClientName
  Get next row from IX_CheckInTime_ClientID
```

The problem is that not a single RDBMS at the time of this writing is capable of generating such an execution plan. They see `TO_DATE` (Oracle syntax) as a function that transforms the value of the column `CheckInTime` into something unindexed. So, the execution plans they tend to generate look like this:

```
For each row from IX_CheckInTime_ClientID
  If TO_DATE(CheckInTime, 'YYYY-MM-DD') = '2020-08-15' then
    Fetch Clients.* where ClientID = IX_CheckInTime_ClientID.ClientID
    Write down Clients.ClientName
```

Executing this would be faster than reading all rows from the `Reservations` table because the index row is narrower than the table row. A smaller row means that fewer blocks would need to be accessed from the disk.

However, we know that the first execution plan would be much more efficient. To persuade our RDBMS to use that approach, we need to rewrite the query:

```
SELECT c.ClientName
FROM Reservations r
JOIN Clients c ON r.ClientID = c.ClientID
WHERE r.CheckInTime >= TO_DATE('2020-08-15 00:00:00', 'YYYY-MM-DD HH:MI:SS')
  AND r.CheckInTime < TO_DATE('2020-08-16 00:00:00', 'YYYY-MM-DD HH:MI:SS');
```

This is a proper range query, one that every good RDBMS understands. Our RDBMS figures out that we want data from the `Reservations` table where the value of `CheckInTime`—not something derived from it—belongs to the well-defined range. The execution plan it generates would be more like:

```
Get first row from IX_CheckInTime_ClientID where
  CheckInTime >= '2020-08-15 00:00:00'

While found and CheckInTime < '2020-08-16 00:00:00' 
  Fetch Clients.* where ClientID = IX_CheckInTime_ClientID.ClientID
  Write down Clients.ClientName
  Get next row from IX_CheckInTime_ClientID
```

That’s what we really want: to leverage not only the index itself but also the fact that it’s sorted.

## Exercise 2: `LIKE` With a Wildcard at the Start

This time our detective comes to the hotel with vague information about the suspect: just that the last name ends with “-son.” The detective wants the first and last names of all such guests:

```
SELECT FirstName, LastName
FROM Clients
WHERE LastName LIKE '%son';
```

For the `Clients` table and an index on `LastName`, we’ll use [this spreadsheet](https://docs.google.com/spreadsheets/d/1EJlK2DJ3Za_6NiXJjkNfp3imLy2-B4ju2C874BG8OIE/edit#gid=0). Write down the results the query would return. Think about different approaches you can apply.

### Table Scan Approach

The simplest strategy is to read all data from the table and write down names for guests when their last name ends with “-son”:

```
For each row from Clients
  If LastName like '%son' then write down FirstName, LastName
```

Here, we would have to read the entire table sequentially.

### Using an Index

Let’s try to take advantage of the index on the `LastName` column. Go to the IX\_LastName sheet, use it to find all clients satisfying the given criterion, and write down their names.

It turns out that you have to read the entire index to find all the Andersons, Robinsons, and Thompsons from the table. Is that any better than using a table scan? In addition to reading the entire index, you also had to find, for every matching entry, the corresponding row from the table using the `rowAddress` value, then write down the `FirstName` from there:

```
For each row from IX_LastName
  If LastName like '%son' then
    Fetch Clients.* where RowAddress = IX_LastName.RowAddress
    Write down FirstName, LastName
```

For us, it was simpler and faster to read the table sequentially. For our RDBMS, it would depend on the percentage of rows satisfying the criteria. If there are just a handful of Andersons, Robinsons, and Thompsons in a large table, an RDBMS would read fewer data blocks from much narrower index entries even if it has to read a few blocks from the table when a match is found. Otherwise, the table scan takes less time.

Ordering the data in the index does not provide any help with such a query. The smaller size of the index row can be helpful—but only sometimes.

## Exercise 3: `LIKE` With a Wildcard at the End

The next time our detective comes, we need to find all clients whose last names start with “Rob-.”

```
SELECT FirstName, LastName
FROM Clients
WHERE LastName LIKE 'Rob%';
```

Try to extract data matching the query from the same spreadsheet.

If you used the table scan approach, you missed the opportunity to take full advantage of the index `IX_LastName`. It’s much faster to locate the first entry from the index starting with “Rob-” (Roberts), read subsequent rows (both Robertses and Robinsons), and stop when the `LastName` no longer matches the criterion:

```
Get first row from IX_LastName where LastName <= 'Rob'

While found and LastName < 'Roc' 
  Fetch Clients.* where rowAddress = IX_LastName.rowAddress
  Write down FirstName, LastName
  Get next from IX_LastName
```

In this case, after the B-tree lookup for the first entry, we only read entries satisfying the criterion. We stop reading as soon as we read a name that does not match the criterion.

## Addressing B-tree Scaling Woes

Typically when we deploy a new database, there are a few populated lookup tables and empty transactional tables. The system runs smoothly from the get-go, especially if we respected good practices of database design by normalizing tables; creating primary, foreign, and unique keys; and supporting foreign keys with corresponding indexes.

After a few months or years, when data volume has significantly increased system and database complexity, we start to notice performance degradation. Opinions arise about why the system has been slowing down and what to do about it.

The popular opinion is often that the size of the database is the primary culprit. The solution seems to be to remove historical data we don’t need daily and place it in a separate database for reporting and analytics.

Let’s explore the main assumption first.

### SQL Range Queries: Does Execution Time Depend on Table Size?

Consider a typical range query from a single table:

```
SELECT Column1, …, ColumnN
FROM Table
WHERE Column BETWEEN X AND Y;
```

Assuming there is an index on `Column`, the optimal execution plan is:

```
Get first row from IX_Column where Column between X and Y

While found and Column <= Y
  Fetch Table.* where rowAddress = IX_Column.rowAddress
  Write down Column1, …, ColumnN
  Get next row from IX_Column
```

Let’s count the blocks an RDBMS will have to read to return this data.

The `Get first row` part is implemented by the B-tree lookup we [introduced](https://www.toptal.com/database/sql-indexes-explained-pt-2#balanced-tree-b-tree-indexes) in the second lesson. The number of blocks it has to read is equal to the depth of the B-tree. After that, we read subsequent items from the leaf level of the index.

With OLTP queries, typically all results will be found within one index block (sometimes two but rarely more). In addition to that, for each index entry, we have access to a block in the table to find the corresponding row based on its address. Some table rows might be within the same table block we already loaded, but to simplify estimation, let’s assume that we load a new block every time.

So the formula is:

**B = D + 1 + R**

B is the total number of blocks read, D is the B-tree depth, and R is the number of rows returned by the query.

The only parameter that depends on the number of rows in the table is D, the B-tree depth.

To simplify calculations and make a point, assume that 1,000 index entries fit into one block. D = 1 as long as there are less than 1,000 rows in the table. For tables holding business transactions, that might be the case the first business day after system deployment. Soon enough, the B-tree depth will increase. As long as there are less than 1 million rows in the table, the index will consist of two levels.

If we’re bothered by slow database response times and blame data volume for this, note that transaction tables often have mere millions of rows. Since only 1 million rows fit a two-level B-tree index, the depth must be at least three. The depth will not grow to four unless there are more than 1 billion rows in the table. Now we have a more precise estimate:

**B = 4 + R**

If R is small, lowering the B-tree depth back to two would speed up the query significantly. When we search by a primary or unique key value, the system will read four blocks instead of five, which is a 20% improvement. If the query returns more rows, the improvement might not be noticeable. The problem is, for many applications, we might not be able to support the requisite business operations by keeping fewer than 1 million transactions in the database.

So the conclusion seems to be that table size does not matter; in other words, moving historical data is a waste of time and resources.

But not so fast: Let’s learn more about the structure of a B-tree index and how data changes affect it.

### B-tree Index Implementation Details

In our coverage of B-tree indexes in the second lesson, we saw that all levels of a balanced tree are (physically) ordered by key column values. However, when we want to insert, update, or delete an item, often we have to move a large amount of data to preserve the order.

Say we’re inserting in the middle of a block that happens to be full. We have to split the block, rearrange the data, and sometimes even update data on another B-tree level pointing to the current one.

To make such cases more efficient, each index item contains pointers to the previous and next rows, making it double-linked. For inserting in general, this means we just write the new items as close as possible to the previous one and correct the pointers.

When we need to split a block as well, we must write a new item in the previous B-tree level. This is just a matter of correcting a few more pointers—no need to rewrite large portions of the tree. After a split, both blocks of data are approximately half-full. Depending on where there is free space on the disk, “neighboring” blocks could be physically quite distant.

After some time, index fragmentation increases and the query execution slowdown becomes noticeable. With an RDBMS executing queries the way we described them, the assumption of the order and proximity of items becomes less and less correct, leading to far more reads. In the worst case, with all data blocks being half-empty, the system has to read twice as many blocks.

### B-tree Index Maintenance

The cure for this is index defragmentation (or “reindexing”). Every RDBMS provides a feature to recreate an entire index; after reindexing, indexes are once again physically ordered.

Reindexing is a pretty fast operation, even though it reads and writes a high volume of data. Modern RDBMSs typically offer two reindexing modes, with the faster one requiring tables to be locked during processing. Either way, it’s preferable to reindex in off-peak hours. Otherwise, processing might slow down database performance.

### Deleting Historical Data

When we have tables with billions or even hundreds of millions of rows, it might not be feasible to complete a reindexing operation during off-peak hours.

To avoid this situation, moving historical data [out of an OLTP database](https://www.toptal.com/insights/future-of-work/briefing-the-data-warehouse#the-data-warehouse-differs-from-the-transactional-database) might be the solution. However, if we simply delete rows that are older than a specific threshold, we make indexes even more fragmented, and we need to reindex them even more frequently.

## SQL Partitioning to the Rescue?

There is a way to avoid the fragmentation caused by removing historical data, keeping only “active” transactions in the production database. The idea that all major RDBMSs implement is to split a table into smaller chunks (called *partitions*) and provide the capability of adding them, removing them, and even switching them between tables (e.g., from an active table to a historical one with the same structure).

Let’s take a look at the `Reservations` table as partitioned in [this spreadsheet](https://docs.google.com/spreadsheets/d/1_w1afzAQjVEOeN2Qcie_ipu54lh18qANpfOZL6YhbWk/edit#gid=0). The table is split by month, with partition names mapped to date periods and other spreadsheets. To see how a query on a partitioned table is executed, we will do a few exercises.

### Exercise 4: Partition Query in SQL

From the spreadsheet linked above, try to extract the data requested by the following query—without using any indexes:

```
SELECT HotelID, ReservationID, ClientID, DateFrom, DateTo
FROM Reservations
WHERE DateFrom BETWEEN TO_DATE('2021-03-01','YYYY-MM-DD') AND TO_DATE('2021-03-03');
```

You probably figured out that you have first to look at the partition-mapping sheet and find the partition containing reservations from March 2021. After that, you opened the corresponding partition, read the data sequentially, and filtered out the rows that did not satisfy the condition.

While straightforward, you probably didn’t like keeping so few rows after reading so many. Reading the March partition was better than reading the entire reservation table but still not ideal. What about indexes?

### Global Indexes

RDBMSs allow us to create a *global index* to cover all partitions of a partitioned table. But there’s no difference between how global and regular indexes work underneath: Global indexes aren’t partition-aware. Thus, CRUD queries using a global index don’t involve the partition map for its table.

We only need to update the partition map when we drop a whole partition. We then have to remove any rows from the index that point to the removed partition. That means the entire global index needs rebuilding.

An outage window remains necessary because indexes can’t be used until obsolete items are removed. If we can regularly drop partitions, limiting the number of active ones, then the reindexing operation might fit into the outage window. So using partitions does help with the original issue by shortening the time required for maintenance tasks, including the maintenance of global indexes.

But what if we still can’t afford the outage?

### Globally Partitioned Indexes

This strategy resolves that problem: We simply partition the index the same way we partition the table. In the spreadsheets that the partition spreadsheet links to, each partition contains its portion of the `Reservations` table and an index sheet called IX\_DateFrom, both partitioned by `DateFrom`.

To execute the query from Exercise 4, an RDBMS would first look at an index partitions map and identify which partitions contain dates from the range. (In our case, it’s just one index partition.) After that, it would use B-tree lookups, cycle through to the leaf level, and finally access the table using the corresponding row address.

When we drop a partition from a table, it is enough to drop the corresponding partition from the index. No downtime is necessary.

### Local Indexes

The main drawback of the globally partitioned indexes is that we have to take care of dropping both the table and the corresponding index partition. There’s only a slight extra cost associated with reading from and maintaining the index partitions map itself.

Local indexes involve a similar but slightly different approach. Instead of partitioning a single global index, we create a local index *inside* each table partition. In doing so, local indexes share the main advantage of globally partitioned indexes—i.e., no downtime—while avoiding their drawbacks.

It seems like a perfect solution. But before we celebrate, let’s investigate the possible execution plan of a few queries.

### Exercise 5: Locally Partitioned Index

Try running the query again, this time using the locally partitioned index on `DateFrom`.

You probably used this execution plan:

```
For all partitions where [StartDateFrom, StartDateTo)
              intersects ['2021-03-01', '2021-03-03']
  Get first row from IX_DateFrom where DateFrom between '2021-03-01' and '2021-03-03'
  While found and DateFrom < '2021-03-04'
    Fetch Reservations.* where RowAddress = IX_DateFrom.RowAddress
    Write down HotelID, ReservationID, ClientID, DateFrom, DateTo
    Get next row from IX_DateFrom
```

We are lucky that all dates belong to a single partition, so we had to traverse just one local index. If the period were six months long, we would have to read six local indexes.

### Exercise 6: In Contrast

Your task is to use the Reservations partition map again, this time to make a list of periods when Client 124 visited Hotel 1:

```
SELECT DateFrom, DateTo
FROM Reservations
WHERE ClientID = 124
  AND HotelID = 1;
```

Here we can see the main drawback of local indexes. We had to read the local index sheet IX\_HotelID\_CientID from every partition of the `Reservations` table:

```
For all partitions
  Get first row from IX_HotelID_ClientID where ClientID = 124 and HotelID = 1
  While found and ClientID = 124 and HotelID = 1
    Fetch Reservations.* where RowAddress = IX_HotelID_ClientID.RowAddress
    Write down DateFrom, DateTo
    Get next row from IX_HotelID_ClientID
```

This execution would clearly read more blocks and take more time than if the table were not partitioned.

So while we did find a way to maintain the health of our indexes during the off-peak period, the strategy also made some of our queries slower.

If our business model allows us to keep a small number of partitions or at least the most frequent queries contain criteria allowing the RDBMS to read just one or two partitions, this solution could be what we need. Otherwise, we’d better avoid partitioning and work on improving the data model, indexes, and queries—and enhancing the database server.

## Indexes in SQL: What to Learn Next

This is the end of our journey. In SQL Indexes Explained, I focused on the index implementation that is common to all modern RDBMSs. I also focused on topics that application developers are interested in, at the expense of topics that typically concern database administrators. The latter would do well to research the impact of fill factor on index fragmentation, but people in both roles will likely find it useful to read further about:

- Data and index caching
- Non-B-tree index structures, such as hash, GiST, bitmap, and columnstore indexes
- Clustered indexes (known as *index-organized tables* in Oracle)
- Functional indexes
- Partial indexes

The partitioning approach we discussed is *range partitioning*. It’s the most commonly used type of partitioning, but there are others, like hash partitioning and list partitioning. Also, some RDBMSs offer the option of multiple levels of partitioning.

Lastly, [SQL developers](https://www.toptal.com/sql) would do well to explore other important topics around RDBMS query execution—first, query parsing, then cost-based execution plan compilation, caching, and reuse.

For the four RDMBSs I have experience with, I recommend these resources as next steps:

### Oracle

### PostgreSQL

### Microsoft SQL Server

### MySQL/MariaDB
