---
url: "http://www.creativedeletion.com/2020/05/25/calendar-standard-library-2020.html"
captured_at: "2020-05-28T11:23:52-03:00"
title: "You might not need the Calendar or Timex libraries"
domain: "creativedeletion-com"
---

# You might not need the Calendar or Timex libraries

May 25, 2020

Five years ago Elixir code would usually have to call third party applications to handle date, time and time zones. And blog posts (including on this blog), tutorials, books, and code still point people to using third party libraries. But today for most purposes, they are no longer necessary.

Since Elixir 1.3 more and more date and time functionality has been added to the Elixir time zone library.

Before Elixir 1.3 there were no native date/time types built into Elixir. With [Elixir 1.3 that changed](http://www.creativedeletion.com/2016/11/12/elixirconf-2016-date-time.html). However to do time zone calculations you still needed either the [Calendar library](https://github.com/lau/calendar) or [Timex library](https://github.com/bitwalker/timex) which would use the [Tzdata library](https://hex.pm/packages/tzdata).

In Elixir 1.8 the `Calendar.TimeZoneDatabase` behaviour was introduced. This means that you can use Elixir standard library functions to do time zone calculations. So today the standard library lets you do things such as:

- Comparison and difference/subtraction/addition calculations for date/time types
- Time zone calculations ([with a time zone database configured](https://hexdocs.pm/elixir/Calendar.TimeZoneDatabase.html))
- Safe polymorphism that lets you e.g. use a `DateTime` with a [`Date` function](https://hexdocs.pm/elixir/Date.html#day_of_year/1), but not the [other way around](https://hexdocs.pm/elixir/DateTime.html#to_iso8601/2)
- Convert to and from Unix time (whole seconds, milliseconds and more)
- Day of year, day of week, quarter, leap year
- Date ranges
- Format and parse to/from ISO 8601 formats

The master branch of Elixir adds [`Calendar.strftime/3` for formatting date/time](https://github.com/elixir-lang/elixir/blob/b028ac88a8b3faabcba5969944123925613f3614/lib/elixir/lib/calendar.ex#L479). This will be released with Elixir 1.11 - scheduled for release around October 2020.

## Why the standard library over a third party library?

The Elixir standard library is always there and the same for every developer. If an Elixir standard library function does the same thing as a third party one, I tend to choose the standard library. Some of the reasons include:

- Fewer dependencies to manage.
- In general the standard library has more contributions and maintenance. This is also important over the long term, looking years ahead.
- Every developer using Elixir uses the standard library. More developers will be familiar with it today and in the future.

## When should you use a third party library?

If the functionality you need is not available in the standard library, it can make sense to use a third party library. But you don’t have to use them for anything that the standard library can do.

If you are starting a new project and are used to using the Calendar or Timex libraries, you could first check to see if the functionality is available in the standard library before adding them as dependencies. And even if they are dependencies, make sure to only use them for functionality not available in the standard library.

## Mix and match

Today the libraries all usually use the same types (`Date`, `Time`, `NaiveDateTime`, `DateTime`) as the standard library. So you can call the standard library (e.g. [`DateTime.utc_now/1`](https://hexdocs.pm/elixir/DateTime.html#utc_now/1)) and pass a datetime to a third party library to do something that the standard library doesn’t do. Or take a result from a third party library and pass it to a standard library function.

## Getting started

For time zone calculations specifically you will have to add a timezone database library to the dependencies of your application.

Currently the most popular option is the tzdata library by yours truly. See the [tzdata](https://github.com/lau/tzdata#getting-started) or [Elixir documentation](https://hexdocs.pm/elixir/DateTime.html#module-time-zone-database) for how to set it up. You basically need `:tzdata` as a dependency in your mix file and then this line in your configuration: `config :elixir, :time_zone_database, Tzdata.TimeZoneDatabase`.

For anything else see the documentation for [`Date`](https://hexdocs.pm/elixir/Date.html), [`DateTime`](https://hexdocs.pm/elixir/DateTime.html), [`NaiveDateTime`](https://hexdocs.pm/elixir/NaiveDateTime.html) and [`Time`](https://hexdocs.pm/elixir/Time.html).

## Library authors

If you maintain any Elixir library that needs to do time zone calculations the functions [from\_naive/3](https://hexdocs.pm/elixir/DateTime.html#from_naive/3) and [shift\_zone/3](https://hexdocs.pm/elixir/DateTime.html#shift_zone/3) can be used for time zone calculations.

You don’t even need to have the `tzdata` package as a dependency. Instead require the end-user of the library to [set a database for Elixir](https://hexdocs.pm/elixir/DateTime.html#module-time-zone-database) to allow time zone calculations. If `{error, :utc_only_time_zone_database}` is returned - meaning such a library hasn’t been configured - errors can be raised as seen appropriate.

This way the user of the library is able to choose any time zone database library that implements the [`Calendar.TimeZoneDatabase`](http://www.creativedeletion.com/2020/05/25/behaviour%20https://hexdocs.pm/elixir/Calendar.TimeZoneDatabase.html).

## Looking ahead

Many projects can get their date/time functionality covered with the functions in the standard library and tzdata (or equivalent `TimeZoneDatabase`). And with each new recent version of Elixir more has been added.

However it was never meant to do everything. Third party libraries can still fill in the gaps to complement the functions in the standard library.
