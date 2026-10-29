---
url: "http://learningelixir.joekain.com/fragments-in-ecto/"
captured_at: "2016-02-29T10:53:30-03:00"
title: "Fragments in Ecto"
domain: "learningelixir-joekain-com"
---

# Fragments in Ecto

A few weeks ago I wrote about a [set of experiments I ran to try to diagnose a problem I was having with Ecto and timex](http://learningelixir.joekain.com/experiments-with-ecto-queries/). I have still not figured out what’s going wrong but I’ve moved on a bit. In this post I want to write a little bit about Ecto and date ranges. I’ll use the date ranges as an example while describing how to use custom SQL in Ecto queries.

In this post I’ll be using Elixir 1.2.1 and the following dependencies (according to mix.lock):

```
connection"  :connection 1.0.2"
  db_connection"  :db_connection 0.2.3"
  decimal"  :decimal 1.1.1"
  ecto"  :ecto 1.1.3"
  poolboy"  :poolboy 1.5.1"
  postgrex"  :postgrex 0.11.0"
```

## Date Ranges

Let’s start with a new mix project:

```
$ mix new date_ranges
* creating README.md
* creating .gitignore
* creating mix.exs
* creating config
* creating config/config.exs
* creating lib
* creating lib/date_ranges.ex
* creating test
* creating test/test_helper.exs
* creating test/date_ranges_test.exs

Your Mix project was created successfully.
You can use "mix" to compile it, test it, and more:

    cd date_ranges
    mix test

Run "mix help" for more commands.
```

## Setup Ecto

I’ve covered this in [Setting up Ecto in Elixir](http://learningelixir.joekain.com/setting-up-ecto-in-elixir/) and repeated a lot of it in [Experiments with Ecto Queries](http://learningelixir.joekain.com/experiments-with-ecto-queries/) so I won’t repeat all the steps here. But here’s a summary of what I’ve done:

- Install and Start Ecto
- Configure the Database
- Write the Repo Module
- Create the database

These steps come directly from [Setting up Ecto in Elixir](http://learningelixir.joekain.com/setting-up-ecto-in-elixir/). For more detail see that post or for to see the exact changes I made you can check out the [github repo](https://github.com/joekain/date_ranges).

## Create a Model

Next we need a model to store some date ranges. We can write up something simple like this:

```
defmodule DateRangesDateRange 
   Schema

  schema date_ranges" 
    field :start 
    field  

    timestamps
```

We just describe a date range with a `start` and `end` date. We also need a migration to add a corresponding table to our database. This will do:

```
defmodule DateRangesMigrationsAddDateRanges 
   Migration

   change 
    create table:date_ranges 
       :start :date
        :date

      timestamps
```

And then we can migrate our database:

```
$ mix ecto.migrate

08:46:48.270 [info]  == Running DateRanges.Repo.Migrations.AddDateRanges.change/0 forward

08:46:48.270 [info]  create table date_ranges

08:46:48.277 [info]  == Migrated in 0.0s
```

## Querying Date Ranges

My goal with this project is to show how to write Ecto queries against date ranges. So, let’s get started with a test to demonstrate:

### Setup tests

We want to run our tests within a database transaction. In order to do this we need to configure Ecto to use the Sandbox adapter. Usually we would do this only for the test env. But, in this example we really only care about the test env. There is no dev or prod. So I’ll modify config.exs and add this line:

```
 config :date_ranges, DateRanges.Repo,
   adapter: Ecto.Adapters.Postgres,
   database: "date_ranges",
   username: "postgres",
   password: "postgres",
+  pool: Ecto.Adapters.SQL.Sandbox
```

Next, I added this line to begin transactions when starting up the tests:

```
ExUnit.start()
+
+ Ecto.Adapters.SQL.begin_test_transaction(DateRanges.Repo)
```

As the final setup step I wrote up a skeleton for my test file with a `setup/1` function:

```
defmodule DateRangeTest 
   ExUnit

  alias DateRanges
  alias DateRangesDateRange

  setup  
    unless :async 
      Adaptersrestart_test_transactionDateRanges 
    

    

    
  

    

  

    
    ranges  
             
               
               
             
             
               
               
              
             
               
               
               
    

     ranges    ->
      insert! DateRange
        start: from_erl
         from_erl
```

The `setup` function restarts the database transaction at the beginning of each test. This maintains a clean environment for each tests. Then `setup` calls `seed` to fill in some default data that I reference in the tests.

The `seed` function uses a list, `ranges`, which is just a bunch of dates I made up (in Erlang date format). Then I insert them all into the database using `Enum.each` over `Repo.insert!`.

Finally, there is one test in the middle but it is currently a placeholder. The next step is to…

### Write a Test

```
 It can query overlapping ranges" 
  target  DateRange
    start: from_erl  
     from_erl  
  

  expected  DateRange 
    start: from_erl  
     from_erl  
  

  result  target
  |> DateRangeoverlapping
  |> 

  assert resultstart  expectedstart
  assert result  expected
```

Of course, this test fails:

```
1) test It can query overlapping ranges (DateRangeTest)
   test/date_range_test.exs:17
   ** (UndefinedFunctionError) undefined function DateRanges.DateRange.overlapping/1
   stacktrace:
     (date_ranges) DateRanges.DateRange.overlapping(%DateRanges.DateRange{__meta__: #Ecto.Schema.Metadata<:built>, end: #Ecto.Date<2016-04-21>, id: nil, inserted_at: nil, start: #Ecto.Date<2016-04-18>, updated_at: nil})
     test/date_range_test.exs:29

.

Finished in 0.1 seconds (0.1s on load, 0.03s on tests)
2 tests, 1 failure
```

### Make the test pass

To pass this test we need to implement an `overlapping/1` function. This function
is passed a target date and returns something we can pass to `Repo.all/2`. This means `DateRange.overlapping/1` must return an `Ecto.Query.t` value, that is it should be a query. We want something like this:

```
 overlappingtarget 
   range  DateRange where: overlapsrange target
```

But what is `overlaps`? The Ecto query language doesn’t expose this.

Fortunately, [Postgres has an overlaps function](http://www.postgresql.org/docs/9.0/static/functions-datetime.html). We can write a custom SQL fragment to use this overlaps function like this:

```
import Query only: from:  from: 

 overlappingtarget 
   range  DateRangesDateRange where: fragment(?, ?) OVERLAPS (?, ?)"
             rangestart range targetstart  target
```

With this implementation of `overlapping/1` the test passes:

```
Finished in 0.1 seconds (0.1s on load, 0.03s on tests)
2 tests, 0 failures
```

How does this work?

The beginning of our query looks quite normal: `from range in DateRanges.DateRange, where:`. Next, we have a call to the `fragment/1` macro. It starts with a string:

```
(?, ?) OVERLAPS (?, ?)"
```

This is a fragment of SQL which uses the `OVERLAPS` function to compare two date ranges. The `?` characters are placeholders that need to be filled in with real values. Those values are described as further arguments to `fragment/1`. We are effectively generating SQL that would look something like this:

```
(range.start, range.end) OVERLAPS (^target.start, target.end)"
```

The last piece to explain is the the `type/2` calls. With fragments Ecto doesn’t know the type of the data elements and we can use the `type/2` function to describe the type. In `overlapping/1` we describe `target.start` and `target.end` as `Ecto.Date`.

## Conclusion

In this post we looked at how to use Ecto fragments to inject custom SQL into a composable query. I learned a lot about how to do this while working on an app of mine. And I hope I was able to explain it and help others to do the same thing.

---

**Fragments in Ecto** was published on February 02, 2016.
