---
url: "http://blog.plataformatec.com.br/2018/10/a-sneak-peek-at-ecto-3-0-breaking-changes/"
captured_at: "2026-11-16T20:07:59+00:00"
title: "A sneak peek at Ecto 3.0: breaking changes « Plataformatec Blog"
domain: "blog-plataformatec-com-br"
---

Welcome to the “A sneak peek at Ecto 3.0” series:

1.  [Breaking changes](http://blog.plataformatec.com.br/2018/10/a-sneak-peek-at-ecto-3-0-breaking-changes/) (you are here!)
2.  [Query improvements part 1](http://blog.plataformatec.com.br/2018/10/a-sneak-peek-at-ecto-3-0-query-improvements-part-1/)
3.  [Query improvements part 2](http://blog.plataformatec.com.br/2018/10/a-sneak-peek-at-ecto-3-0-query-improvements-part-2/)
4.  [Performance, migrations and more](http://blog.plataformatec.com.br/2018/10/a-sneak-peek-at-ecto-3-0-performance-migrations-and-more/)

We have spent the last 3 months working hard to release Ecto 3.0. As we get closer and closer to Ecto 3.0 release, we will do a series of blog posts highlighting what is up and coming.

Despite the major version change, we have kept the number of user-facing breaking changes to a minimum, mostly around three areas:

*   Split the Ecto repository apart
*   Remove the previously deprecated Ecto datetime types in favor of the Calendar types that ship as part of Elixir
*   Update to the latest JSON handling best practices

We will start our series of posts by going over the “bad news” and discuss how those breaking changes will affect you. In the next posts, we will highlight all of the upcoming new features and performance improvements.

Let’s get started.

## Split Ecto into `ecto` and `ecto_sql`

Ecto 3.0 will be broken in two repositories: `ecto` and `ecto_sql`. Since Ecto 2.0, an increased number of developers and teams have been using Ecto for data mapping and validation, without a need for a database. However, adding Ecto to your application would still bring a lot of the SQL baggage, such as adapters, sandboxes and migrations, which many considered to be a mixed message.

In Ecto 3.0, we will move all of the SQL adapters to a separate repository and Ecto will focus on the four building blocks: schemas, changesets, queries and repos. [You can see the discussion in the issues tracker](https://github.com/elixir-ecto/ecto/issues/2558).

If you are using Ecto with a SQL database, migrating to Ecto 3.0 will be very straight-forward. Instead of:

`{:ecto, "~> 2.2"}`

You should list:

`{:ecto_sql, "~> 3.0"}`

And if you are using `Ecto` only for data manipulation but with no database access, then it is just a matter of bumping its version. That’s it!

## Calendar types

`Ecto.Date`, `Ecto.Time` and `Ecto.DateTime` no longer exist. Instead, developers should use `Date`, `Time`, `DateTime` and `NaiveDateTime` that ship as part of Elixir and are the preferred types since Ecto 2.1. Odds are that you are already using the new types and not the deprecated ones.

We have used this opportunity to unify the support for microseconds across all databases. The types `:time`, `:naive_datetime`, `:utc_datetime` will now discard any microseconds information. Ecto v3.0 introduces the types `:time_usec`, `:naive_datetime_usec` and `:utc_datetime_usec` as an alternative for those interested in keeping microseconds. If you want to keep microseconds in your migrations and schemas, you will need to configure your repository:

```
config :my_app, MyApp.Repo,
  migration_timestamps: [type: :naive_datetime_usec]
```

And then in your schema:

`@timestamps_opts [type: :naive_datetime_usec]`

Note that database adapters have also been standardized to work with Elixir types and they no longer return tuples when developers perform raw queries.

## JSON handling

Ecto v3.0 moved the management of the JSON library to adapters. All adapters should default to [`Jason`](https://github.com/michalmuskala/jason).

The following configuration will emit a warning:

`config :ecto, :json_library, CustomJSONLib`

And should be rewritten as:

```
# For Postgres
config :postgrex, :json_library, CustomJSONLib

# For MySQL
config :mariaex, :json_library, CustomJSONLib
```

If you want to rollback to Poison, you need to configure your adapter accordingly:

```
# For Postgres
config :postgrex, :json_library, Poison

# For MySQL
config :mariaex, :json_library, Poison
```

We recommend everyone to migrate to Jason. Built-in support for Poison will be removed in future Ecto 3.x releases.

## Other changes

Now that we have unified the data types, the `Ecto.DataType` protocol is no longer necessary and has been removed. If you were implementing it in the past, you can just completely remove it and everything should still just work.

We have also improved `Ecto.Multi.run/5` to receive the repo module in which the transaction is executing as the first argument. Therefore, if you are passing a `module-function-args` to any of the `Ecto.Multi` functions, they need to be adapted to receive the repo as the first argument. This change will most likely lead to cleaner and less coupled code.

Finally, one of the changes we will cover in future posts is how the “prefix” support (called “schemas” in PostgreSQL) has been drastically improved in Ecto 3.0. Previously, you could only set a prefix for the whole query but Ecto 3.0 will give developers granular control over those. Therefore, if you are setting the `@schema_prefix` attribute in a schema, you will have to remember it only affects that particular schema, and no longer the whole the query.

We are really excited with Ecto 3.0! With the breaking changes out of the way, we are ready to explore many of the upcoming new features in the next blog posts.

[![banner-elixir development subscription](http://blog.plataformatec.com.br/wp-content/uploads/2018/10/Elixir_2-1-1024x213.png)](https://pages.plataformatec.com.br/elixir-development-subscription)

Tags: [ecto](http://blog.plataformatec.com.br/tag/ecto/), [elixir](http://blog.plataformatec.com.br/tag/elixir/), Posted in [English](http://blog.plataformatec.com.br/category/english/), Comments Off on A sneak peek at Ecto 3.0: breaking changes
