---
url: "http://nathanmlong.com/2016/03/when-to-use-constraints-in-ecto/?utm_campaign=elixir_radar_42&utm_medium=email&utm_source=RD+Station"
captured_at: "2016-03-30T14:48:17-03:00"
title: "NathanMLong.com - When to Use Constraints in Ecto"
domain: "nathanmlong-com"
---

# When to Use Constraints in Ecto

elixir
postgresql
phoenix

Posted on: March 5, 2016

I recently had the pleasure of [contributing to](https://github.com/elixir-lang/ecto/commit/6d9de1ffbfe42f0430fcd2a56b997bada353744b) Ecto, the Elixir database querying library.
(I got a lot of kind help from [José Valim](https://github.com/josevalim) along the way.)

As a result, Ecto 2.0 will support [every kind of constraint that PostgreSQL 9.5 offers](http://www.postgresql.org/docs/9.5/static/ddl-constraints.html).🎊 🎆 (See [the changelog](https://github.com/elixir-lang/ecto/blob/v2.0.0-beta.1/CHANGELOG.md) for more.)

But when and how should you use them?

## Constraints vs Validations

The difference between validations and constraints is simple: validations are checked in application code, but constraints are checked by the database.
This means that **constraints are checked at the moment you insert or update data**.
As a result, constraints can offer guarantees that validations can’t.

Imagine you have an `events` table. Every event has a `name`, `start_time`, and `end_time`. You want to enforce the following rules:

- An event’s name can’t be blank
- An event’s name must be unique
- An event’s `end_time` must be after its `start_time`
- No two events can overlap

How can we check these in Ecto?

### Name can’t be blank

This is easy to check in a validation; the application code knows whether it has an empty string or not.

In Ecto 2.0, you’d simply use this changeset function:

```
def changeset(event, params \\ :invalid) do
  event
  |> cast(params, ~w(name start_time end_time))
  |> validate_required(~w(name))
end
```

## Name must be Unique

This can’t really be checked in a validation.
Yes, in theory, you could run a `SELECT` to see whether the name is in use before doing your `INSERT`, but someone else may claim that name before you finish.

Ecto recognizes that the only guaranteed way to check uniqueness is with a database constraint.

Do do this, you’d create the constraint within a migration, like this:

```
create unique_index(:events, [:name])
```

Then you’d tell your Ecto changesets about it, saying essentially “when updating, you may see PostgreSQL complain that this column isn’t unique. If you do, show the user a nice error message.”

```
def changeset(event, params \\ :empty) do
  event
  |> cast(params, ~w(name start_time end_time))
  |> unique_constraint(:name, message: "Ooops, another event already has that name!")
end
```

## An event’s `end_time` must be after its `start_time`.

You can and should check this in a validation, but there’s a race condition.
Two different users could start editing the same meeting, one to change the start time and one to change the end time.
The resulting meeting schedule would surprise them both!

Validating `end_time > start_time` in the application code would be useful: it would prevent invalid records from being inserted, and would catch most of the invalid updates (the ones where you don’t have two users editing simultaneously).
But in a race condition like the one above, it wouldn’t be enough, because **only the database knows what data is stored right now**.
On the other hand, a [check constraint](http://nathanmlong.com/2016/01/protect-your-data-with-postgresql-constraints/#check_constraints) could enforce this rule at the moment the `INSERT` or `UPDATE` runs.

So in this case, you might use **both a validation and a constraint**.

You’d have to write a custom validation function to check for positive duration.
Daniel Berkompas has [explained how on his blog](http://blog.danielberkompas.com/elixir/2015/05/20/useful-ecto-validators.html).

You could create the check constraint in a migration like this:

```
create constraint("events", "positive_duration", check: "end_time > start_time")
```

And if the database complained about a violation, you could ensure the user got a nice message by using this in your changeset:

```
def changeset(event, params \\ :empty) do
  event
  |> cast(params, ~w(name start_time end_time))
  # custom validation function
  |> validate_positive_duration(:end_time)
  |> check_constraint(
     :end_time,
     name: :positive_duration,
     message: "end time must be after start time"
   ) 
end
```

Of course, one could argue that the real problem here is allowing any user to do an `UPDATE` starting from stale data.
So we should probably use [`optimistic_lock`](https://hexdocs.pm/ecto/Ecto.Changeset.html#optimistic_lock/3) to prevent that.

## No two events can overlap

Now here’s a requirement that only the database can really check.
At the moment you attempt to insert or update data, only the database knows what the other rows in the table contain.

You can use an [exclusion constraint](http://nathanmlong.com/2016/01/protect-your-data-with-postgresql-constraints/#exclusion_constraints) to say “this row’s time may not overlap with the time of any other row”.

```
create constraint(
  :meetings,
  :cannot_overlap,
  exclude: ~s|gist tsrange("start_time", "end_time", '[]') WITH &&)|
)
```

If the database says “this was violated”, you could turn it into a nice error with

```
 exclusion_constraint(
   changeset,
   :meetings,
   name: :cannot_overlap,
   message: "must not overlap with another meeting"
 )
```

## Caveats for Constraints

Constraints offer strong data guarantees, but they have some downsides.

First, whereas validations can be applied situationally, constraints can’t.
With validations, you can require users to supply a password when signing up, but allow admins to create users without passwords; all you need is different changeset functions for the two situations.
If you make `password` a `NOT NULL` field, you get a strong guarantee that no code - not in this application, or in any other that uses the same database - can make the password `NULL`.
But you lose situational flexibility.
So my first suggestion for using constraints is to **only use them for truly inviolable rules**.

Second, **whereas multiple validations can be checked simultaneously, constraints fail one-by-one**.
In other words, if you try an `UPDATE` that violates three constraints, Postgres will only give you an error for the first failure it notices.
Relying on this would mean the user might submit the form, see an error, fix it, submit again, see another error, fix it, and repeat until all constraints were satisfied.
This is a bad user experience.
So my second suggestion for using constraints is to **catch every possible error with validations first**.
If a true guarantee is only possible with a `CHECK` constraint, you might still catch 99% of cases with a validation, and give a better user experience in the process.
Then you could consider your constraint as a form of “defense in depth” from bad data.
