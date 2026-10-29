---
url: "http://sorentwo.com/2016/02/08/folding-window-functions-into-ecto.html?utm_campaign=elixir_radar_38&utm_medium=email&utm_source=RD+Station"
captured_at: "2016-02-29T10:49:59-03:00"
title: "Folding Window Functions Into Ecto"
domain: "sorentwo-com"
---

# Folding Window Functions Into Ecto

*by* Parker Selbert

*This is a reinterpretation of [Folding Window Functions Into Rails](http://blog.codeship.com/folding-postgres-window-functions-into-rails/), rewritten and adapted from ActiveRecord to [Ecto](https://github.com/elixir-lang/ecto) 2.0.
The results were unexpected…*

Perhaps you’ve heard of window functions in PostgreSQL, but you aren’t quite sure what they are or how to use them.
On the surface they seem esoteric and their use-cases are ambiguous.
Something concrete would really help cement when window functions are the right tool for the job.
That’s precisely what we’ll explore in this post:

1. How to recognize where a window function is helpful
2. How to build an Ecto query that implements window functions
3. How to use tests to drive a switch from naive Ecto to a window function query

## An Anecdotal Example

You’ve recently finished shipping a suite of features for an application that helps travelers book golf trips.
Things are looking good, and a request comes in from your client:

> Our application started by being the go-to place to find golf trips, and our users love it.
> Some of the resorts that list trips with us also offer some non-golf events, such as tennis, badminton, and pickleball.
> When we begin listing other trips it would be great to highlight our user’s favorite trips for each category.
> Can you do that for us?
>
> —Anonymous Client

Why, of course you can do that!
The application lets potential traveler’s flag trips they are interested in as favorites, providing a reliable metric that we can use to rank trips.
With the simple addition of a `category` for each trip we can also filter or group trips together.
This seems straight forward enough…

## Survey the Scene

A look at the `Trip` schema reveals that it currently has these relevant fields: `name`, `category`, and `favorites`.

```
defmodule Triptastic 
   Schema

  @categories  tennis badminton pickleball

  schema trips" 
    field :name :string
    field :category :string
    field :favorites :integer default: 
  

   categories  @categories
```

Instead of listing all of the top ranked trips we’ll only show the *top two* trips in each category.
Some tests will help verify that we’re getting the expected results.

```
defmodule TriptasticTripRepoTest 
   ExUnit

  alias Triptastic 

  setup 
      AdaptersSandboxcheckoutTriptastic

    trips   category <- categories favorites <-  
      name: categoryfavorites
        category: category
        favorites: favorites
    

    insert_all trips

    
  

   grouping top trips by category" 
    trips   |>  |> popular_by_category

    assert lengthtrips  
    assert trips favorites
```

The test seeds the test database with trips across four categories with a varying number of favorites.
The `popular_by_category/2` function expects a list of trips and returns the most popular two from each category.

Initially we’ll approach this with pure naive Elixir.
All of the trips are loaded into memory, grouped by category, ranked according to the number of favorites, and then the requested `per` amount is taken off of the top.
Do note that sorting is comprised of both favorites and name, which is necessary to force deterministic sorting in the likely event that trips are equally popular.

```
# Defined within the Triptastic.Trip module shown above

 popular_by_categorytrips    
  trips
  |> group_bycategory
  |> flat_mappopular_in_subset 

 popular_in_subset_category trips  
  trips
  |> sort_byfavorites 
  |>
```

As a wizened developer you immediately recognize that loading every trip into memory simply to retrieve eight results is rather inefficient.
It makes fine use of the `Enum` module and some piping, but it isn’t suitable for production usage.

## Move the Logic to PostgreSQL

Between various sub-selects, `GROUP BY` with aggregates and multiple queries, there are many ways to manipulate the trips data in SQL.
One advanced feature of PostgreSQL that is particularly adept at solving this categorization problem are [window functions](http://www.postgresql.org/docs/9.4/static/tutorial-window.html).
Directly from the documentation:

> A window function performs a calculation across a set of table rows that are somehow related to the current row.
>
> [Postgres Documentation](http://www.postgresql.org/docs/9.4/static/tutorial-window.html)

The key part phrase is the power of calculating across related rows.
In our case, the rows are *related* by category, and the *calculation* being performed is ordering them within those categories.
In the realm of window functions this is handled with an [`OVER` clause](http://www.postgresql.org/docs/9.4/interactive/sql-expressions.html#SYNTAX-WINDOW-FUNCTIONS).
There are additional expressions for fine tuning the window, but for now we can achieve all we need with `PARTITION BY` and `ORDER BY` expressions.
Dropping into `psql`, let’s see how to partition the data set by category:

```
SELECT category, favorites, row_number() OVER (PARTITION BY category) FROM trips;
```

```
  category  | favorites |  row_number
------------+-----------+-------------
 badminton  |         0 |          1
 badminton  |         1 |          2
 badminton  |         2 |          3
 badminton  |         3 |          4
 golf       |         0 |          1
 golf       |         1 |          2
```

The `row_number` is a *window function* that calculates number of the current row within its partition.
Row number becomes crucial when the partitioned data is then ordered:

```
SELECT category, favorites, row_number() OVER (
  PARTITION BY category ORDER BY favorites DESC
) FROM trips;
```

```
  category  | favorites | row_number
------------+-----------+------------
 badminton  |         3 |          1
 badminton  |         2 |          2
 badminton  |         1 |          3
 badminton  |         0 |          4
 golf       |         3 |          1
 golf       |         2 |          2
```

All that remains is limiting the results to the top ranked rows and our query matches the expected output.

## Move It Into Ecto

At this time there aren’t any constructs for `OVER` built into Ecto 2.0 and it doesn’t support arbitrary `FROM` clauses.
The only way to utilize window functions is with the raw `Ecto.Adapters.SQL.query` function.
Using the `from` macro from `Ecto.Query` with a sub-select would be preferable to working with a raw string, but we aren’t there yet.

We’ll make a new test that is very similar to the last, but which expects a `Postgrex.Result` struct instead.
The `Result` struct wraps a list of raw rows with all of the trip data.

```
 grouping top trips by category using windows" 
   result  popular_over_category

  assert resultnum_rows  
  assert result   >=
```

Now the `popular_over_category/1` function must be defined to construct a SQL query:

```
 popular_over_category   
  query  """
    SELECT * FROM (SELECT *, row_number() OVER (
      PARTITION BY category
      ORDER BY favorites DESC, name ASC
    ) FROM trips) AS t WHERE t.row_number <= $1::integer;
  """

  AdaptersqueryTriptastic query
```

The query string uses a subquery to build up trips partitioned by category.
The `where` clauses filters out any trips with a `row_number` below the desired threshold, and only the top favorites in each category are returned.
With the change in place the new test is now passing!

Inspecting the test results, with the help of some formatting, yields:

```
  category  | favorites | row_number
------------+-----------+------------
 badminton  |         3 |          1
 badminton  |         2 |          2
 golf       |         3 |          1
 golf       |         2 |          2
 pickleball |         3 |          1
 pickleball |         2 |          2
 tennis     |         3 |          1
 tennis     |         2 |          2
```

Those are precisely the results we’re looking for!

## How Much Better Is It?

Here is where the presumptions behind this article fall apart and the BEAM blows my mind.
The original version of this article was written about window queries in Rails.
In those benchmarks the window function was *539.3x* faster than the naive version.
Naturally, I was excited to see how well the Elixir/Ecto variant would perform in comparison.

This benchmarking test has a lot of boilerplate just to set up the sandbox and insert an arbitrary number of trips into the database.
An outer `for` comprehension builds up a sequence of tests with an increasing number of trips for comparison.
All tests are run in separate processes via `Task.async |> Task.await`, which introduces the slight complication of sharing sandboxed connection ownership.
Note that the test caps out at 20,000 trips because any more breask `Repo.insert_all`, and that is plenty for a comparison.

```
defmodule TriptasticTripBenchmarkTest 
   ExUnit

  alias Triptastic 

  setup 
      AdaptersSandboxcheckout
  

   parent  
    async ->
      AdaptersSandboxallow parent 
      begin  timestamp
      
      finish  timestamp
      :timernow_difffinish begin  
     |> await
  

    <-   5_000 10_000 20_000 
      
     compare memory and windows for  trips"   
      categories  Streamcyclecategories

      trips    <-  
          categories 
          trunc:randuniform  

        name:  category:  favorites: 
      

      insert_all trips

          ->  |>  |> popular_by_category 
          -> popular_over_category 
          -> popular_over_category_joined |>
```

With a small number of trips the performance difference is negligible.
As the number of trips increases the cost of loading that many records into memory simply to filter them out does start to add up.
Even with 20,000 records being slurped in for manipulation, the naive strategy is only *2x* slower.
For now, if you are working in Ecto, you can rest assured that the performance of naive queries is good enough not to worry about fiddling with raw SQL.

The simple application used for testing can be found in [triptastic on GitHub](https://github.com/sorentwo/triptastic).

**Edit**: The benchmark test and chart now includes a hybrid approach where the `OVER` sub-select is performed in a join.
This was suggested by Jośe Valim as a way to avoid SQL queries, and provides better query interop with comparable performance.
