---
url: "https://akoutmos.com/post/ecto-repo-testing"
captured_at: "2026-11-16T03:42:16+00:00"
title: "The Repository Pattern, Ecto, and Database-less Testing"
domain: "akoutmos-com"
---

## Contents

*   [Intro](#intro)
*   [What is the repository pattern?](#what-is-the-repository-pattern)
*   [Why is the repository pattern useful?](#why-is-the-repository-pattern-useful)
*   [Show me the code!](#show-me-the-code)
*   [Step 1: Create a new Elixir project with Ecto boilerplate](#step-1-create-a-new-elixir-project-with-ecto-boilerplate---a-hrefhttpsgithubcomakoutmosstore_inventorycommit95e5e60-target_blankcommita)
*   [Step 2: Create migration and inventory item schema](#step-2-create-migration-and-inventory-item-schema---a-hrefhttpsgithubcomakoutmosstore_inventorycommit56e57e5-target_blankcommita)
*   [Step 3: Writing a mocked Repo](#step-3-writing-a-mocked-repo---a-hrefhttpsgithubcomakoutmosstore_inventorycommit4ff11db-target_blankcommita)
*   [Closing thoughts](#closing-thoughts)
*   [Additional Resources](#additional-resources)

## Intro

In this blog post, we’ll be talking about what exactly the repository pattern is, how it applies to Ecto, and how you can go about testing your Ecto backed applications without using a database. We’ll play around with this concept by putting together a simple Elixir application that leverages Postgres during development. But, then we will write some tests that make use of a database-less mock Repo. Without further ado, let’s dive right into things!

Before going any further, let’s unpack what exactly the repository pattern is and how Ecto implements it. The repository pattern is a design pattern that provides an abstraction that sits between your data models and your data persistence layer. This abstraction, as the name implies, is called the “repository”. Only through the clearly defined “repository” interface are you able to interact with your data persistence layer. For example, if you wanted to insert a new record into your database, you would:

1.  Construct a data structure that has all the necessary data
2.  That data structure would then be passed on to your repository
3.  Your repository would attempt to insert it into the database.

Let’s walk through this step by step with a real world code sample:

```
def insert_user(opts) do
  %User{}
  |> User.create_changeset(opts)
  |> Repo.insert()
end
```

As a reference, let’s also look at the `insert/2` callback definition in `Ecto.Repo` \[1\]:

```
@callback insert(
              struct_or_changeset :: Ecto.Schema.t() | Ecto.Changeset.t(),
              opts :: Keyword.t()
            ) :: {:ok, Ecto.Schema.t()} | {:error, Ecto.Changeset.t()}
```

In our `insert_user/1` function, we start off by creating a changeset based on the incoming parameters. In this case, the changeset is the data structure that our repository requires in order to perform its database specific operations. With the changeset, the repository adapter can decide whether to insert the record (changeset is valid), or ignore the changeset (changeset is invalid). The important thing to note here is that our data model (the `User` schema) is completely separate from the database. We provide the repository the data it needs, and it sorts out how to deal with the database.

Enjoying the blog post so far? Follow me on Twitter for more content [**Follow @akoutmos**](https://twitter.com/intent/follow?screen_name=akoutmos "akoutmos Twitter")

* * *

Sign up for the mailing list and get notified via email when new blog posts come out.

## Why is the repository pattern useful?

The repository patten (in my opinion), is a very useful and pragmatic abstraction since it decouples your data from your persistence layer. The two are still able to work pleasantly together given that they share an agreed upon interface. In addition, the behavior of one, does not impose restrictions upon the other. This is evident when looking at the separation of the `ecto` and `ecto_sql` when Ecto 3 was released \[2\]. The `ecto` library was able to focus specifically on data mapping and validation, and the `ecto_sql` library was able to focus on providing functionality for database adapters.

Another thing to consider (which happens to be the focus of this article), is that your persistence layer adapter can be swapped out at any time. As long as the repository adapter that gets swapped in adheres to the same interface, everything should be good to go. One real world example where this is useful is when you are testing your application. While I think we are very spoiled here in the Elixir community thanks to Ecto Sandbox \[3\], there are times when you have no choice but to mock out your database as it is not feasible to run a throw-away database along with your tests. The repository pattern makes this mocking process very simple and completely pain-free.

Last but not least, having a separate mechanism in place to control your database access allows you to easily support things like read/write replicas \[4\]. Your data model will neither know nor care where the data is being written to or fetched from. As such, the repository can easily delegate work to replicas when it is able to in a fairly intuitive and transparent manner.

## Show me the code!

In order to get familiar with these concepts, we’ll put together a very basic Elixir application that makes use of Ecto and Postgres. Our application will be a simple inventory system where we can add items to our inventory and also query our inventory. We will then experiment with having an actual Postgres instance running while in `MIX_ENV=dev` and then when `MIX_ENV=test`, we will leverage a repository that will have some pre-baked data for the purposes of testing. With that all being said, let’s jump right into it!

## Step 1: Create a new Elixir project with Ecto boilerplate - [commit](https://github.com/akoutmos/store_inventory/commit/95e5e60)

To begin, let’s start off by creating a new Elixir project with a supervisor. Do that by running the following in the terminal:

```
$ mix new store_inventory --sup
```

When that command wraps up, open up your `mix.exs` file and ensure that your `deps/0` function looks like the following:

```
defp deps do
  [
    {:ecto_sql, "~> 3.0"},
    {:postgrex, ">= 0.0.0"}
  ]
end
```

With the necessary dependencies in place, go ahead and run `mix deps.get` to pull them all down. Once all the dependencies have been fetched, go ahead and run `mix ecto.gen.repo -r StoreInventory.Repo` to generate your boilerplate Ecto related files. We’ll need to adjust the generated code a bit to get things actually working. Let’s start off by adding our `StoreInventory.Repo` to our supervision tree. Open up `lib/store_inventory/application.ex` and update it as follows:

```
defmodule StoreInventory.Application do
  @moduledoc false

  use Application

  def start(_type, _args) do
    opts = [strategy: :one_for_one, name: StoreInventory.Supervisor]
    Supervisor.start_link(get_children(), opts)
  end

  defp get_children do
    case Mix.env() do
      :test -> []
      _ -> [StoreInventory.Repo]
    end
  end
end
```

The reason that we have the `get_children/0` function in place is that during testing (when `MIX_ENV=test`), we don’t actually want to start up our Postgres Repo. As a result, there are no children that need to be added to the supervision tree. In a production application you would opt for using `Application` configuration and then fetch your configured Repos via `Application.get_env`, but this will suffice for a tutorial :). Next we’ll want to open up `config/config.exs` and update our configuration so that we can connect to Postgres:

```
import Config

config :store_inventory, ecto_repos: [StoreInventory.Repo]

config :store_inventory, StoreInventory.Repo,
  database: "store_inventory_repo",
  username: "postgres",
  password: "postgres",
  hostname: "localhost"

import_config "#{Mix.env()}.exs"
```

At the bottom of our `config.exs` file we also import environment specific configuration files. We’ll be using this in order to have our real Repo running in `:dev`, and our test Repo running in `:test`. With that said, create a file `config/dev.exs` with the following contents:

```
import Config

config :store_inventory, repo: StoreInventory.Repo
```

Also create the configuration file `config/test.exs` with the following contents:

```
import Config

config :store_inventory, repo: StoreInventory.TestRepo
```

With all this in place, we should be able to start up our application in an IEx session without any errors (to kill the Postgres container you can run `docker ps` to get the container ID and then run `docker kill CONTAINER_ID` to kill it):

```
$ docker run -p 5432:5432 -e POSTGRES_PASSWORD=postgres postgres:12 &
$ mix ecto.create
$ iex -S mix
```

## Step 2: Create migration and inventory item schema - [commit](https://github.com/akoutmos/store_inventory/commit/56e57e5)

Let’s start off by creating a migration for our store inventory application. Our migration will add a new table that will keep track of all the items, their price, quantity, etc. Run `mix ecto.gen.migration items` from the terminal and add the following to the generated file:

```
defmodule StoreInventory.Repo.Migrations.Items do
  use Ecto.Migration

  def change do
    create table("items") do
      add(:name, :string)
      add(:description, :string)
      add(:price, :decimal)
      add(:quantity, :integer)

      timestamps()
    end
  end
end
```

With that in place, go ahead and run `mix ecto.migrate` while your Postgres docker container is still running. Once the migration has run, we can create a new file `lib/store_inventory/item.ex` and put in the following contents to define our Ecto schema for the corresponding database table:

```
defmodule StoreInventory.Item do
  use Ecto.Schema

  import Ecto.Changeset

  alias __MODULE__

  @all_fields [:name, :description, :price, :quantity]

  schema "items" do
    field(:name, :string)
    field(:description, :string)
    field(:price, :decimal)
    field(:quantity, :integer)

    timestamps()
  end

  def changeset(%Item{} = item, params \\ %{}) do
    item
    |> cast(params, @all_fields)
    |> validate_required(@all_fields)
    |> validate_number(:quantity, greater_than: 0)
    |> validate_number(:price, greater_than: 0)
  end
end
```

All that is left now is to add a module that we can use to interact with our configured `Repo` and `Item` schema. Let’s create a file `lib/store_inventory.ex` with the following contents:

```
defmodule StoreInventory do
  alias StoreInventory.Item

  @repo Application.get_env(:store_inventory, :repo)

  def insert_item(params) do
    %Item{}
    |> Item.changeset(params)
    |> @repo.insert()
  end

  def all_items do
    @repo.all(Item)
  end

  def average_item_price do
    {total, num_items} =
      all_items()
      |> Enum.reduce({0, 0}, fn %Item{} = item, {sum, count} ->
        {sum + item.price, count + 1}
      end)

    if num_items == 0,
      do: 0,
      else: total / num_items
  end
end
```

The migration and schema modules are pretty standard, so I won’t dive into those. This module on the other hand has some bits that are worth discussing. At the top of the module you’ll notice an attribute `@repo` that is set to the value fetched from the Application configuration `Application.get_env(:store_inventory, :repo)`. If you recall from Step 1, this value was `StoreInventory.Repo` by default as defined in `config/config.exs` and only when `MIX_ENV=test` is that value set to `StoreInventory.TestRepo`. Usually you would not put an `Application.get_env` or `System.get_env` call as a module attribute since it is evaluated at compile time and usually you are looking to have these things configured at run-time. In this case it is acceptable to do so since we are merely setting which module is our actual Repo. There is no run-time configuration associated with this value (specifically which module is being used), so we are in the clear. All of our actual database connection configuration is store in a separate place (in this case `config/config.exs`).

With all that in place, let’s fire up an IEx session and give all this a go! Run `iex -S mix` in the terminal and play around with adding some items to our store inventory:

```
iex(1) ▶ StoreInventory.insert_item(%{name: "Macbook Air", description: "Cheapest Apple laptop you can buy", price: 1000, quantity: 5})
{:ok,  %StoreInventory.Item{...}}

iex(2) ▶ StoreInventory.insert_item(%{name: "System76 Thelio", description: "Super cool Linux desktop", price: 3200, quantity: 5})
{:ok,  %StoreInventory.Item{...}}

iex(3) ▶ StoreInventory.insert_item(%{name: "Dell XPS 13", description: "Makes for a fine Linux laptop", price: 1100, quantity: 5})
{:ok,  %StoreInventory.Item{...}}

iex(4) ▶ StoreInventory.all_items()
[
  %StoreInventory.Item{
    __meta__: #Ecto.Schema.Metadata<:loaded, "items">,
    description: "Cheapest Apple laptop you can buy",
    id: 1,
    inserted_at: ~N[2020-05-29 02:37:59],
    name: "Macbook Air",
    price: #Decimal<1000>,
    quantity: 5,
    updated_at: ~N[2020-05-29 02:37:59]
  },
  %StoreInventory.Item{
    __meta__: #Ecto.Schema.Metadata<:loaded, "items">,
    description: "Super cool Linux desktop",
    id: 2,
    inserted_at: ~N[2020-05-29 02:38:44],
    name: "System76 Thelio",
    price: #Decimal<3200>,
    quantity: 5,
    updated_at: ~N[2020-05-29 02:38:44]
  },
  %StoreInventory.Item{
    __meta__: #Ecto.Schema.Metadata<:loaded, "items">,
    description: "Makes for a fine Linux laptop",
    id: 3,
    inserted_at: ~N[2020-05-29 02:40:00],
    name: "Dell XPS 13",
    price: #Decimal<1100>,
    quantity: 5,
    updated_at: ~N[2020-05-29 02:40:00]
  }
]
```

It looks like everything is working as intended :). Next we’ll put together some tests to validate our `StoreInventory` module without needed a running database.

## Step 3: Writing a mocked Repo - [commit](https://github.com/akoutmos/store_inventory/commit/4ff11db)

Before writing our tests, let’s put together a mocked Repo module that will provide all the mocked responses for our tests. Create the file `lib/store_inventory/test_repo.ex` with the following contents:

```
defmodule StoreInventory.TestRepo do
  alias Ecto.Changeset
  alias StoreInventory.Item

  def all(Item, _opts \\ []) do
    [
      %Item{
        name: "Thing 1",
        description: "A really cool thing",
        price: 100,
        quantity: 2
      },
      %Item{
        name: "Thing 2",
        description: "Another really cool thing",
        price: 50,
        quantity: 0
      },
      %Item{
        name: "Thing 3",
        description: "A really cool thing",
        price: 75,
        quantity: 5
      }
    ]
  end

  def insert(changeset, opts \\ [])

  def insert(%Changeset{errors: [], changes: values}, _opts) do
    {:ok, struct(Item, values)}
  end

  def insert(changeset, _opts) do
    {:error, changeset}
  end
end
```

Normally when providing a mocked implementation of behaviour, you would see something like `@behaviour Ecto.Repo` at the top of the module. We are not doing that in this case since the `Ecto.Repo` behaviour has a handful of required callbacks that we won’t be implementing in order to keep our mock implementation lean and clean. Either way, we will respect the contracts specified in the `Ecto.Repo` behaviour so that our test Repo can be swapped in without any issues \[5\].

Our `all/0` callback is rather straightforward in that it merely returns a pre-baked list of `Item`s. Our `insert/2` callback is a bit more involved. What it does is check whether the incoming changeset is valid or not. If it is valid, we return an `:ok` tuple with the changes wrapped into the `Item` struct. If it is invalid, we return an `:error` tuple with the provided changeset. This behaviour directly mimics the functionality that you would expect from a real Repo, so our tests should have a solid mock to work with.

With that in place, all that is left is to add our tests. In the `test/store_inventory_test.exs` file add the following:

```
defmodule StoreInventoryTest do
  use ExUnit.Case

  alias Ecto.Changeset
  alias StoreInventory.Item

  test "insert_item/1 should return an error when invalid params are provided" do
    params = %{
      name: "Item",
      description: "Something people want",
      price: 1,
      quantity: "INVALID"
    }

    {:error, changeset} = StoreInventory.insert_item(params)

    expected_error = {"is invalid", [type: :integer, validation: :cast]}
    assert %Changeset{errors: [quantity: ^expected_error]} = changeset
  end

  test "insert_item/1 should return an :ok tuple when valid params are provided" do
    params = %{
      name: "Item",
      description: "Something people want",
      price: 1,
      quantity: 5
    }

    assert {:ok, %Item{}} = StoreInventory.insert_item(params)
  end

  test "average_item_price/0 should return the average price of all the items in the DB" do
    assert 75.0 = StoreInventory.average_item_price()
  end
end
```

With our tests wrapped up, go ahead and kill your database if it is still running via `docker kill CONTAINER_ID` (you can get the container ID of the Postgres container by running `docker ps`). Now that we are confident that there is no database running, you should be able to run `mix test` and get the following success output:

```
mix test
Compiling 1 file (.ex)
...

Finished in 0.03 seconds
3 tests, 0 failures

Randomized with seed 105041
```

And with that, we now have a mock Repo in place to test our application!

## Closing thoughts

Well done and thanks for sticking with me to the end! We covered quite a lot of ground and hopefully you picked up a couple of cool tips and tricks along the way. To recap, we created an Elixir application that leveraged Ecto to connect to a database during development, but during testing, we were able to provide a hard-coded mock module. This technique can be useful in situations where you don’t have access to a database during testing, but still want your code to remain as natural as possible. For example, if you are using Ecto to connect to a proprietary database that you can’t easily host via Docker or on your local machine, this may be a useful tool to have in the toolbox. All this to say that you should not go out and rewrite all your Ecto Sandbox based tests with this pattern. Ecto Sandbox is quite performant, reliable, and super easy to use and this technique should be used in cases where you can’t easily run your tests within an actual database.

Feel free to leave comments or feedback or even what you would like to see in the next tutorial. Till next time!

Enjoying the blog post so far? Follow me on Twitter for more content [**Follow @akoutmos**](https://twitter.com/intent/follow?screen_name=akoutmos "akoutmos Twitter")

* * *

Sign up for the mailing list and get notified via email when new blog posts come out.

## Additional Resources

Below are some additional resources if you would like to deep dive into any of the topics covered in the post.

*   \[1\] [https://hexdocs.pm/ecto/Ecto.Repo.html](https://hexdocs.pm/ecto/Ecto.Repo.html)
*   \[2\] [https://dashbit.co/blog/a-sneak-peek-at-ecto-3-0-breaking-changes](https://dashbit.co/blog/a-sneak-peek-at-ecto-3-0-breaking-changes)
*   \[3\] [https://hexdocs.pm/ecto\_sql/Ecto.Adapters.SQL.Sandbox.html](https://hexdocs.pm/ecto_sql/Ecto.Adapters.SQL.Sandbox.html)
*   \[4\] [https://hexdocs.pm/ecto/replicas-and-dynamic-repositories.html](https://hexdocs.pm/ecto/replicas-and-dynamic-repositories.html)
*   \[5\] [https://hexdocs.pm/ecto/Ecto.Repo.html#callbacks](https://hexdocs.pm/ecto/Ecto.Repo.html#callbacks)

* * *
