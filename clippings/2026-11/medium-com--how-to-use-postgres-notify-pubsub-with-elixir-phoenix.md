---
url: "https://medium.com/elixir-bytes/in-this-post-i-would-like-to-illustrate-how-to-take-advantage-of-the-notify-feature-of-postgres-in-f5a919316f0b"
captured_at: "2026-11-16T06:15:47+00:00"
title: "How to use Postgres NOTIFY PubSub with Elixir/Phoenix | by Lorenzo Sinisi | elixir-bytes | Medium"
domain: "medium-com"
---

How to use Postgres NOTIFY PubSub with Elixir/Phoenix
Lorenzo Sinisi
3 min read
·
Oct 1, 2018

In this post I would like to illustrate how to take advantage of the NOTIFY feature of Postgres in our Phoenix application. One example of the application of this feature is to automate the ‘welcome’ email for new members in a specific platform, or to make a specific API call every time a row in the database changes to maybe keep two systems always in sync (imagine Elasticsearch or two services that share some data via APIs and need to be in sync).

“The NOTIFY command sends a notification event together with an optional “payload” string to each client application that has previously executed LISTEN channel for the specified channel name in the current database.

NOTIFY provides a simple interprocess communication mechanism for a collection of processes accessing the same PostgreSQL database. A payload string can be sent along with the notification, and higher-level mechanisms for passing structured data can be built by using tables in the database to pass additional data from notifier to listener(s).

The information passed to the client for a notification event includes the notification channel name, the notifying session’s server process PID, and the payload string, which is an empty string if it has not been specified […]” — from the Postgres documentation https://www.postgresql.org/docs/10/static/sql-notify.html

Using this feature we can ‘make’ Postgres call a function of our application every time a row changes on a specific table. Let’s see how it will work using the package ‘phoenix_postgres_pub_sub’ and creating an example application. (note: I am the creator of that package)

First let’s create a new Phoenix application with the following task:

$ mix phx.new phoenix_postgres_pub_sub_example

Than we will create the User schema under the Account context:

$ mix phx.gen.html Accounts User users name:string

I run the migration and create the database

$ mix ecto.setup

And add the dependency to the mix file

def deps do
[
{:phoenix_postgres_pub_sub, "~> 0.1.0"}
]
end

Get the dependency with mix mix deps.get

$ mix deps.get

And add the following to the config.exs of our app

config :phoenix_postgres_pub_sub, :config,
adapter: PhoenixPostgresPubSubExample,
repo: PhoenixPostgresPubSubExample.Repo

Now let’s create the module that will be called every time something changes in the table ‘users’, I will place it in the /lib folder and name it “PhoenixPostgresPubSubExample.PhoenixPostgresPubSub”. For now let’s just print out every notification.

# in the file just created lib/phoenix_postgres_pub_sub.ex
defmodule PhoenixPostgresPubSubExample.PhoenixPostgresPubSub do
def handle_postgres_notification(notification, _state) do
IO.inspect(notification, label: "Some table has changed")
end
end

Now I create the migration to create the Postgres function and trigger that will be used by the phoenix_postgres_pub_sub GenServer to dispatch the notification to our PhoenixPostgresPubSubExample.PhoenixPostgresPubSub module.

$ mix phoenix_postgres_pub_sub.gen.channel user_changes — table=users

With this, we make sure that every time a row in the ‘users’ table changes, the function “PhoenixPostgresPubSubExample.PhoenixPostgresPubSubExample.handle_postgres_notification/2” gets called.

Now we will run the migration

$ mix ecto.migrate

And we are almost done! Its time to add the worker to our application.

defmodule PhoenixPostgresPubSubExample.Application do
use Application
def start(_type, _args) do
import Supervisor.Spec
children = [
supervisor(PhoenixPostgresPubSubExample.Repo, []),
supervisor(PhoenixPostgresPubSubExampleWeb.Endpoint, []),
worker(
PhoenixPostgresPubSub,
[
[
"users_changes"
]
],
restart: :permanent
)
]
...
end

Note: the arguments of the added worker PhoenixPostgresPubSub is always a list of strings that are the combination of the table that we want to monitor and the word ‘changes’. In this case we want to monitor the table ‘users’, so the argument of the worker are [[“user_changes”]]. If we were monitoring accounts we could have had [[“user_changes”, “accounts_changes”, …]] as argument of the PhoenixPostgresPubSub worker.

Wanna see the code? Check out the demo project on Github https://github.com/lorenzosinisi/phoenix_postgres_pub_sub_example

Feel free to leave a comment if you have any doubt or question!
