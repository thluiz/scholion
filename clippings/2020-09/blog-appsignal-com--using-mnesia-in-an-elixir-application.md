---
url: "https://blog.appsignal.com/2020/05/19/using-mnesia-in-an-elixir-application.html"
captured_at: "2020-09-07T17:02:53-03:00"
title: "Using Mnesia in an Elixir Application | AppSignal Blog"
domain: "blog-appsignal-com"
---

# Using Mnesia in an Elixir Application

> “I absolutely love AppSignal.”

---

"I absolutely love AppSignal. It’s helped me identify errors quickly and has provided some great insight on performance."

[Discover AppSignal](https://appsignal.com/)

In today’s post, we’ll learn about Mnesia, see when you would use such a tool, and take a look at some
of the pros and cons of using it. After covering the fundamentals of Mnesia, we’ll dive right into a sample
application where we’ll build an Elixir application that uses Mnesia as its database. Let’s jump right in!

## Introduction to Mnesia

At a high level, Mnesia is a Database Management System (DBMS) that is baked into OTP. Thus, if you are
using Elixir or Erlang, you have the ability to leverage Mnesia out-of-the-box. No additional dependencies need to be
installed and no separate systems need to be running. Before considering migrating everything from your existing
database to Mnesia, let’s discuss what Mnesia was designed for and what problems it aims to solve.

Mnesia was largely designed to solve the problems that existed in the telecommunications problem space. Specifically,
some of the following requirements needed to be fulfilled ([check out this research paper for more details](http://erlang.se/publications/mnesia_overview.pdf)):

- Fast key/value lookup times where you need soft real-time latency guarantees. A soft real-time system is one where the
  system should be able to service the majority of its requests within a given time frame and a failure to do so
  generally means degradation of service (i.e the data is no longer useful after the time frame has passed). A hard
  real-time system, on the other hand, is a system that *must* respond within a given time frame or else it is considered
  a system failure.
- The ability to perform complex queries (like you would in SQL for example), but without soft real-time latency
  guarantees
- A high level of fault tolerance

In a typical DBMS, your application would need to either make a network call to a separate machine where the database is
running, or it would have to connect to the database process that is running on the same machine. Either way, the data
that is contained within that database resides in an entirely separate memory space than the application, and therefore,
there is an inescapable amount of latency overhead.

On the other hand, Mnesia runs within the same memory space as the
application. As a result of being baked into the language and runtime, you are able to fetch data out of Mnesia at soft
real-time speeds. In other words, your application and database are running side-by-side and there is little to no
communication overhead between the two.

Another important thing to note is that Mnesia stores all of the Erlang data
types natively, and so there is no need to marshall/unmarshall data when you read/write to Mnesia (marshalling is the
process of converting data from one format to another for the purposes of storing it or transmitting it).

When performing complex queries against your Mnesia database, you can either leverage [Query List Comprehensions](https://erlang.org/doc/man/qlc.html) (QLC) or you can write [Match Specifications](http://erlang.org/doc//apps/erts/match_spec.html). In addition, you can also add indexes to your Mnesia tables
for fields that you know you’ll be querying often. Using these tools, you can perform arbitrary queries against your
tables and extract the relevant data.

A primary requirement of telecommunications systems is that they must be running nonstop. Downtime means missed or
dropped calls. Mnesia addresses this by allowing tables to be replicated across the various nodes in the cluster.

When running within a transaction, the data that needs to be committed must be written to all the configured table
replicas. If nodes are unavailable during a write, the transaction will update the available node replicas and will
update the unavailable node replicas when they come back online. Through this replication mechanism, Mnesia is able to
provide a high level of fault tolerance.

## Mnesia and the CAP Theorem

You may be wondering exactly where it falls in regards to the CAP theorem. For those unfamiliar with the CAP theorem, it
basically states that, when dealing with distributed systems, you have three characteristics at play but can only
guarantee two at any given time. Those three characteristics are:

- Consistency: Whenever a read is made against your database, the database will respond with the most recently updated
  data.
- Availability: Whenever a request is made against your database, the database will respond with some data even if it’s out of date (i.e. newer data has been committed but has not propagated to all nodes).
- Partition tolerance: Whenever a request is made against your database, it will be able to respond regardless of some
  nodes being unavailable.

When a network partition does occur (i.e. some database nodes are unavailable), your system must make a trade-off. Does
it favor consistency and error out on any requests while some nodes are unavailable, or does it favor availability by
servicing the request with the understanding that there may be some data inconsistency when the missing nodes come back
online?

Given that Mnesia will propagate transaction commits across all table replicas and does not support any kind of eventual
consistency, it is more of a CP style database. In the case of a network partition where the separate partitions are
both handling requests, the application will need to deal with reconciliation of the data.

## When To Use Mnesia Over PostgreSQL or Other Database

Like many things in Software Engineering and Systems Design, it’s all about making the correct trade-offs. Whether
Mnesia is right or not for your application largely depends on its requirements. Personally, I
have used Mnesia in production primarily to support some soft real-time use cases with very good results.

The data that
was stored in Mnesia was needed only for the duration of the user’s session and would then get cleared after the user’s
interaction with the system ceased. Thus, there wasn’t a lot of pressure on system resources (RAM specifically, as
the tables need to fit into RAM), as the size of the tables would reflect the number of users actively using the system.
For situations where you need to store a large amount of data and you do not require soft real-time response times, a
traditional DBMS such as MySQL or Postgres may be a better choice.

For situations where you see yourself reaching for
Redis or Memcached, you may want to consider looking into Mnesia, given that it fills a similar need and is built into
OTP. For more information regarding this topic, I would suggest [looking at Mnesia docs](https://erlang.org/doc/apps/mnesia/Mnesia_overview.html#when-to-use-mnesia).

## Hands-on Project with Mnesia

In order to get familiar with Mnesia, we’ll be creating a very simple banking application that leverages Mnesia as its
database. While we could leverage the Mnesia API directly via `:mnesia`, we will instead opt to use the [Amnesia library](https://github.com/meh/amnesia) as it provides a nice Elixir wrapper around the Mnesia API. Our banking application will support the following
operations:

1. Create new accounts
2. Transfer money between accounts
3. Fetch account details
4. Deposit funds into an account
5. Withdraw funds from an account
6. Search for accounts with a low balance

To begin, let’s create a new Elixir project using the following terminal command:

|  |  |
| --- | --- |
| ``` 1 ``` | ``` $ mix new fort_knox --sup ``` |

After creating the Elixir project, open up the `mix.exs` file and make sure that your `deps/0` function looks like
the following:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 ``` | ``` defp deps do   [     {:amnesia, "~> 0.2.8"}   ] end ``` |

After that has been done, you can run `mix deps.get` to fetch the `amnesia` dependency. Next, we’ll want to create a
module that defines all the table schemas in our Mnesia database. For our sample application, we will only have one table
defined for bank accounts. To do this, add the following content to `lib/database.ex`

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 ``` | ``` use Amnesia  defdatabase Database do   deftable(     Account,     [{:id, autoincrement}, :first_name, :last_name, :balance],     type: :ordered_set,     index: [:balance]   ) end ``` |

Our database contains only the `Account` table and specifies that it has 3 fields along with an auto-incrementing `id`
field. With the database definition in place, let’s go back to our terminal and run the following command:

|  |  |
| --- | --- |
| ``` 1 ``` | ``` $ mix amnesia.create -d Database --disk ``` |

After executing that command, you will notice that a new directory (`Mnesia.nonode@nohost`) has been created for us at the root of
our project. This directory contains all the disk persisted data so that our data can be maintained across application
restarts. To delete all of the persisted database data, you can either `rm -rf Mnesia.nonode@nohost` or run
`mix amnesia.drop -d Database --schema`.

With that in place, it’s time to work on some of our business logic. Let’s create a file at `lib/fort_knox/accounts.ex`
and start off by creating functions that will create a new account and fetch existing accounts:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 ``` | ``` defmodule FortKnox.Accounts do   require Amnesia   require Amnesia.Helper   require Exquisite   require Database.Account    alias Database.Account    def create_account(first_name, last_name, starting_balance) do     Amnesia.transaction do       %Account{first_name: first_name, last_name: last_name, balance: starting_balance}       |> Account.write()     end   end    def get_account(account_id) do     Amnesia.transaction do       Account.read(account_id)     end     |> case do       %Account{} = account -> account       _ -> {:error, :not_found}     end   end end ``` |

Our module begins with a few `require` statements to pull in Amnesia functionality. We can then leverage `Account` as a
struct to conveniently interact with the `Account` table in Mnesia. To create a new `Account` entry in the table, we
create the struct and call `Account.write()` within a transaction. If you do not want to perform your database actions
within a transaction, you can also leverage the dirty read/write API calls, but that is not recommended. When looking up
existing accounts by their id, we once again leverage a transaction and match on an `Account` struct if an account was
found. Let’s go ahead and add the remainder of our functionality in `lib/fort_knox/accounts.ex`:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 ``` | ``` defmodule FortKnox.Accounts do   ...    def transfer_funds(source_account_id, destination_account_id, amount) do     Amnesia.transaction do       accounts = {Account.read(source_account_id), Account.read(destination_account_id)}        case accounts do         {%Account{} = source_account, %Account{} = destination_account} ->           if amount <= source_account.balance do             adjust_account_balance(destination_account, amount)             adjust_account_balance(source_account, -amount)             :ok           else             {:error, :insufficient_funds}           end          {%Account{}, _} ->           {:error, :invalid_destination}          {_, _} ->           {:error, :invalid_source}       end     end   end    def get_low_balance_accounts(min_balance) do     Amnesia.transaction do       Account.where(balance < min_balance)       |> Amnesia.Selection.values()     end   end    def deposit_funds(account_id, amount) do     Amnesia.transaction do       case Account.read(account_id) do         %Account{} = account ->           adjust_account_balance(account, amount)          _ ->           {:error, :not_found}       end     end   end    def withdraw_funds(account_id, amount) do     Amnesia.transaction do       case Account.read(account_id) do         %Account{} = account ->           if amount <= account.balance do             adjust_account_balance(account, -amount)           else             {:error, :insufficient_funds}           end          _ ->           {:error, :not_found}       end     end   end    defp adjust_account_balance(%Account{} = account, amount) do     account     |> Map.update!(:balance, &(&1 + amount))     |> Account.write()   end end ``` |

The `withdraw_funds/2`, `deposit_funds/2` and `transfer_funds/3` functions should be relatively straight forward as they
are a mixture of reads and writes to update accounts within a transaction. The `get_low_balance_accounts/1` will
probably seem new as we have a `where` clause to query our database records. The Exquisite library (which Amnesia depends
on) provides the ability to generate Mnesia Match Specifications which are used to perform custom queries [5].

With all that in place, let’s take this all for a test drive. We’ll first seed our database with some initial accounts
and then transfer some funds between the accounts. Open up an IEx session via `iex -S mix` and type the following:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 ``` | ``` iex(1) ▶ [ ...(1) ▶ {"Josh", "Smith", 1_000}, ...(1) ▶ {"Tom", "Lee", 500}, ...(1) ▶ {"Joe", "Diaz", 1_500} ...(1) ▶ ] |> ...(1) ▶ Enum.each(fn {first_name, last_name, amount} -> ...(1) ▶ FortKnox.Accounts.create_account(first_name, last_name, amount) ...(1) ▶ end) :ok  iex(2) ▶ FortKnox.Accounts.get_account(1) %Database.Account{balance: 1000, first_name: "Josh", id: 1, last_name: "Smith"}  iex(3) ▶ FortKnox.Accounts.get_account(2) %Database.Account{balance: 500, first_name: "Tom", id: 2, last_name: "Lee"}  iex(4) ▶ FortKnox.Accounts.transfer_funds(2, 1, 400) :ok  iex(5) ▶ FortKnox.Accounts.get_account(1) %Database.Account{balance: 1400, first_name: "Josh", id: 1, last_name: "Smith"}  iex(6) ▶ FortKnox.Accounts.get_account(2) %Database.Account{balance: 100, first_name: "Tom", id: 2, last_name: "Lee"}  iex(7) ▶ FortKnox.Accounts.get_low_balance_accounts(250) [%Database.Account{balance: 100, first_name: "Tom", id: 2, last_name: "Lee"}] ``` |

After running all of these commands, feel free to quit from IEx via Ctrl+C and go back to using `iex -S mix`. If you run
`Database.Account.count()`, you’ll see that we get a value of 3 since our data persisted across IEx sessions and was not
destroyed.

## Conclusion

Thanks for sticking with me to the end and hopefully you learned a thing or two about Mnesia and how to go about using
it within an Elixir application. Regardless of whether you decide to use Mnesia in a production context or not, I would
highly suggest at least experimenting with it so as to better appreciate the amazing things that you get out-of-the-box
with OTP.

*Guest author [Alex Koutmos](https://akoutmos.com/top/about/) is a Senior Software Engineer who writes backends in Elixir, frontends in VueJS and deploys his apps using Kubernetes. When he is not programming or blogging he is wrenching on his 1976 Datsun 280z.*

**P.S. If you’d like to read Elixir Alchemy posts as soon as they get off the press, [subscribe to our Elixir Alchemy newsletter and never miss a single post](https://blog.appsignal.com/category/elixir-alchemy.html#elixir-alchemy)!**
