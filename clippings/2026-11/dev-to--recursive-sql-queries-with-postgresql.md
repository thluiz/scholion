---
url: "https://dev.to/martinheinz/recursive-sql-queries-with-postgresql-1i6h"
captured_at: "2026-11-16T01:49:45+00:00"
title: "Recursive SQL Queries with PostgreSQL"
domain: "dev-to"
---

When working with databases, most of the time, all you need is `SELECT`, `UPDATE` (CRUD operations), few `JOIN`s and `WHERE` clauses and that's about it. But, sometimes you will run into datasets and tasks, that will require you to use much more advanced features of SQL. One of them is CTE or _common table expression_ and more specifically, _Recursive CTE_, which we can use to make recursive SQL queries. Let's look at how it works and what we can do with it!

## [](#why-recursive-queries)Why Recursive Queries?

First of all, why is this actually even a thing? What are recursive queries good for? - In general recursive queries come in handy when working with self-referential data or graph/tree-like data structures. Just a few examples of these use cases are:

*   Self-referential data:
    
    *   _Manager -> Subordinate (employee)_ relationship
    *   _Category -> Subcategory -> Product_ relationship
    *   Graphs - Flight (Plane Travel) map
*   Trees:
    
    *   Any taxonomy system - books, animals, genetics...
    *   Links between articles - for example on Wikipedia
    *   Comment section - for example threads on Reddit

For any of these examples, it would require you to build temporary tables or use cursors to actually get useful data from such datasets. Now that I hopefully persuaded you that recursive queries are pretty useful, let's see what they are and how we can use them.

## [](#what-will-we-need)What Will We Need?

Recursive queries leverage something called _CTE - Common Table expression_, which is SQL `WITH` clause, more commonly used for simplifying very complex queries (subqueries). Let's look at example of that:  

```
WITH avg_salary AS (
    SELECT avg(salary)
    FROM employees
)
SELECT avg_salary;
```

Enter fullscreen mode Exit fullscreen mode

This is very simple example, but you can surely imagine how this can be used to make very complicated queries containing multiple subqueries much more readable.

Apart from the syntax above, we will also need some data that we can use for our recursive queries. For that we will use _Manager - Subordinate_ hierarchy using one self-referencing table, defined like so:

[![Employee Table](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2Fb78rqs7wdtqbk5yabtaf.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2Fb78rqs7wdtqbk5yabtaf.png)

Here's SQL to create such table including some data to play with:  

```

CREATE TABLE employees (
   id serial PRIMARY KEY,
   name varchar(255) NOT NULL,
   salary integer,
   job varchar(255),
   manager_id int,
   FOREIGN KEY (manager_id) REFERENCES employees (id) ON DELETE CASCADE
);

INSERT INTO employees (
    id,
    name,
    manager_id,
    salary,
    job
)
VALUES
    (1,  'John', NULL, 10000, 'CEO'),
    (2,  'Ben', 5, 1400, 'Junior Developer'),
    (3,  'Barry', 5, 500, 'Intern'),
    (4,  'George', 5, 1800, 'Developer'),
    (5,  'James', 7, 3000, 'Manager'),
    (6,  'Steven', 7, 2400, 'DevOps Engineer'),
    (7,  'Alice', 1, 4200, 'VP'),
    (8,  'Jerry', 1, 3500, 'Manager'),
    (9,  'Adam', 8, 2000, 'Data Analyst'),
    (10, 'Grace', 8, 2500, 'Developer');
```

Enter fullscreen mode Exit fullscreen mode

So, with that out of the way, let's build some recursive queries!

> To iterate is human, to recur, divine - L. Peter Deutsch

## [](#recursion)Recursion

Let's start with formal structure of recursive SQL query:  

```
WITH RECURSIVE name [(col_1,..., col_n)] AS (
    non_recursive_part
    UNION [ALL]
    recursive_part
)
```

Enter fullscreen mode Exit fullscreen mode

It looks pretty simple, but doesn't tell us much, so let's see human readable example:  

```
WITH RECURSIVE nums (n) AS (
    SELECT 1
  UNION ALL
    SELECT n+1 FROM nums WHERE n+1 <= 10
)
SELECT n FROM nums;
```

Enter fullscreen mode Exit fullscreen mode

And output of that query:  

```
 n  
----
  1
  2
...
  9
 10
(10 rows)
```

Enter fullscreen mode Exit fullscreen mode

In this example, our non-recursive base case is just `SELECT 1` and recursive part is `SELECT n+1 FROM nums WHERE n+1 <= 10`. This part creates recursion by referring to name of _CTE_ (`nums`) and unioning all the results. At the end we have `WHERE` clause to terminate the recursion, so that our query doesn't run infinitely.

## [](#real-world-examples)Real World Examples

Previous section showed very basic example that explains how it works, but doesn't really show how the recursive _CTE_ can help us. So, let's go through some examples using _Manager - Subordinate_ hierarchy data from above:

Getting _"manager tree"_ for some employee:  

```
WITH RECURSIVE managers AS (
        SELECT id, name, manager_id, job, 1 AS level
        FROM employees
        WHERE id = 7 -- Alice, the VP
    UNION ALL
        SELECT e.id, e.name, e.manager_id, e.job, managers.level + 1 AS level
        FROM employees e
        JOIN managers ON e.manager_id = managers.id
)

SELECT * FROM managers;
```

Enter fullscreen mode Exit fullscreen mode

This query can be used to generate list of all subordinates of some manager, which essentially is subtree starting from some specific employee. As a base case here, we select one employee (manager) by ID and we also include `level` to indicate how many levels down we went in the tree. In the recursive part we `JOIN` employees table to _CTE_ (`managers`) using manager IDs. Again, we include `level` by incrementing level of results from previous step of recursion. This is the output:  

```

 id |  name  | manager_id |       job        | level 
----+--------+------------+------------------+-------
  7 | Alice  |          1 | VP               |     1
  5 | James  |          7 | Manager          |     2
  6 | Steven |          7 | DevOps Engineer  |     2
  2 | Ben    |          5 | Junior Developer |     3
  3 | Barry  |          5 | Intern           |     3
  4 | George |          5 | Developer        |     3

```

Enter fullscreen mode Exit fullscreen mode

To better visualize what happens there, look at the following tree. The highlighted part is what is returned by query:

[![Alt Text](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2F65g5u77jjp1yrfr4ckkn.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2F65g5u77jjp1yrfr4ckkn.png)

Another practical example using same data is computing _degrees of separation between 2 employees_:  

```
WITH RECURSIVE rec AS (
        SELECT id, 0 AS degree
        FROM employees
        WHERE id = 1 -- John, the CEO
    UNION ALL
        SELECT e.id, rec.degree + 1 AS degree
        FROM employees e
        JOIN rec ON e.manager_id = rec.id
)
SELECT
    'John and ' || employees.name || ' are separated by ' ||
    TO_CHAR(rec.degree, '9') ||
    ' degrees of separation'
FROM employees
JOIN rec
    ON (employees.id = rec.id)
    WHERE employees.name = 'George';
```

Enter fullscreen mode Exit fullscreen mode

The recursive _CTE_ is quite similar to the one in previous example. To simplify things, we only select ID and `degree` (instead of level). Next, we need query that looks up and tells us degrees of separation for 2 employees - to do so, we join `employees` table to our previously built `rec` table containing IDs and `degrees` using IDs in respective tables. In the final `SELECT` part we do some formatting to get nicer output and in `WHERE` clause we optionally specify the other (second) employee for whom we want the degrees of separation. Output:  

```
-----------------------------------------------------------
 John and George are separated by  3 degrees of separation
(1 row)

```

Enter fullscreen mode Exit fullscreen mode

Again, playing with the same data, let's find out what might be the job progression in the hypothetical company:  

```
WITH RECURSIVE rec AS (
        SELECT id, manager_id, job, 0 AS level
        FROM employees
        WHERE id = 4  -- George, the Developer
    UNION ALL
        SELECT e.id, e.manager_id, e.job, rec.level + 1 AS level
        FROM employees e
        JOIN rec ON e.id = rec.manager_id
)

SELECT STRING_AGG(job,' > ' ORDER BY level ASC) AS path FROM rec;
```

Enter fullscreen mode Exit fullscreen mode

This time we run the recursion from the bottom up. This is achieved by flipping the `ON` clause, compared to previous examples. To create readable output, we use `STRING_AGG` function, which takes rows from above `SELECT` and concatenates them using `>` as delimiter. This is what the query gives us:  

```
              path              
--------------------------------
 Developer > Manager > VP > CEO
(1 row)

```

Enter fullscreen mode Exit fullscreen mode

## [](#recursion-on-graphs)Recursion on Graphs

Enough of that _employee_ data set, let's explore what we can to with graphs - graphs as a data structure are ideal candidate for traversing using recursion. So, let's first define simple table and insert some data, so we have something to play with:  

```
CREATE TABLE edges (
   src integer,
   dest integer
);

INSERT INTO edges (
    src,
    dest
)
VALUES
    (1, 2),
    (2, 3),
    (2, 4),
    (3, 4),
    (4, 1),
    (3, 5);
```

Enter fullscreen mode Exit fullscreen mode

[![Graph](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2F8ic35yu80eb0pdesn0cw.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2F8ic35yu80eb0pdesn0cw.png)

As an example, we will do the obvious thing - find paths is graph. For that we will need a _PostgreSQL_ special - `ARRAY` data type. Arrays are not a common relational database feature, but are very handy here for storing paths. If you are not familiar with this data type, then these are the things you need for understanding SQL below:

*   Create array - `ARRAY[value_1, value_2]`
*   Concatenate array - `ARRAY[value_1, value_2] || ARRAY[value_3]`
*   `ALL` function - `"x" != ALL(ARRAY["a", "b", "c"])` - compares `"x"` to each value in array, results is `true` if all comparisons result in `true`

Alright, now for the query:  

```
WITH RECURSIVE paths (src, dest, path) AS (
        SELECT e.src, e.dest, ARRAY[e.src, e.dest]
        FROM edges e
    UNION
        SELECT p.src, e.dest, p.path || ARRAY[e.dest]
        FROM paths p
        JOIN edges e
        ON p.dest = e.src AND e.dest != ALL(p.path)
)
SELECT * FROM paths;
```

Enter fullscreen mode Exit fullscreen mode

The query above first selects all the direct neighbours in the non-recursive case. Then in recursive part, we build on the base case (and during subsequent iterations on previous recursive cases) and append available edge to existing paths and replace destination with same edge. We do this for every row where end of the existing path (`dest`) is same as start of the selected edge and where new destination is not yet in path (to prevent cycles). And this is the full output:  

```
 src | dest |    path     
-----+------+-------------
   1 |    2 | {1,2}
   2 |    3 | {2,3}
   2 |    4 | {2,4}
   3 |    4 | {3,4}
   4 |    1 | {4,1}
   3 |    5 | {3,5}
   4 |    2 | {4,1,2}
   1 |    3 | {1,2,3}
   1 |    4 | {1,2,4}
   2 |    4 | {2,3,4}
   2 |    5 | {2,3,5}
   2 |    1 | {2,4,1}
   3 |    1 | {3,4,1}
   3 |    2 | {3,4,1,2}
   4 |    3 | {4,1,2,3}
   1 |    4 | {1,2,3,4}
   1 |    5 | {1,2,3,5}
   2 |    1 | {2,3,4,1}
   4 |    5 | {4,1,2,3,5}
```

Enter fullscreen mode Exit fullscreen mode

## [](#infinite-tables)Infinite Tables

Aside from the useful things above, you can also use recursive _CTE_ with infinite streams of data:  

```
WITH RECURSIVE nums (n) AS (
    SELECT 1
  UNION ALL
    SELECT n+1 FROM nums
)
SELECT n FROM nums;
-- ... Runs forever

SELECT n FROM nums LIMIT 15;
-- Works just fine, returns 15 rows
```

Enter fullscreen mode Exit fullscreen mode

Recursive table is built iteratively with each step and each step produces finite number of rows, therefore it's possible to use `LIMIT` to retrieve first `n` rows from infinite query!

## [](#bonus-recursive-view)Bonus: Recursive VIEW

As a quick little bonus, I want to also show, that it is possible (as of PostgreSQL 9.3) to even create recursive views:  

```
CREATE RECURSIVE VIEW paths (src, dest, path) AS (
        SELECT e.src, e.dest, ARRAY[e.src, e.dest]
        FROM edges e
    UNION
        SELECT p.src, e.dest, p.path || ARRAY[e.dest]
        FROM paths p
        JOIN edges e
        ON p.dest = e.src AND e.dest != ALL(p.path)
);

SELECT * FROM paths WHERE src = 4;

 src | dest |    path     
-----+------+-------------
   4 |    1 | {4,1}
   4 |    2 | {4,1,2}
   4 |    3 | {4,1,2,3}
   4 |    5 | {4,1,2,3,5}
(4 rows)
```

Enter fullscreen mode Exit fullscreen mode

Even though, this is just a syntax sugar, it can make your life easier when working with some of recursive queries and data.

## [](#conclusion)Conclusion

Recursion is very powerful tool, that can solve some problems in very elegant way. Using it with SQL is not so common though, so hopefully this article showed you some ways for how to leverage it, in case you run into data that can only be processed recursively.

Recursion however, can make your code less readable, so use it sparingly, especially with SQL, as it is often not that easy parse and understand  
even without recursion.
