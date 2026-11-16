---
url: "https://akoutmos.com/post/actor-model-genserver-app"
captured_at: "2026-11-16T03:01:35+00:00"
title: "OTP as the Core of Your Application Part 1"
domain: "akoutmos-com"
---

## Contents

*   [Intro](#intro)
*   [What is the Actor Model?](#what-is-the-actor-model)
*   [How does the Actor Model work on the BEAM?](#how-does-the-actor-model-work-on-the-beam)
*   [Show me the code!](#show-me-the-code)
*   [Step 1: Create a new Phoenix project and install dependencies](#step-1-create-a-new-phoenix-project-and-install-dependencies---a-hrefhttpsgithubcomakoutmosbook_storecommit172c86d-target_blankcommita)
*   [Step 2: Writing a data scraper using Floki](#step-2-writing-a-data-scraper-using-floki---a-hrefhttpsgithubcomakoutmosbook_storecommit8a4ba14-target_blankcommita)
*   [Step 3: Seeding our database with sample data](#step-3-seeding-our-database-with-sample-data---a-hrefhttpsgithubcomakoutmosbook_storecommitad5d6aa-target_blankcommita)
*   [Closing thoughts](#closing-thoughts)
*   [Additional Resources](#additional-resources)

## Intro

In this two part series, we’ll be taking a deep dive into what exactly the Actor Model is, how exactly the Actor Model is implemented in Elixir/Erlang and how we can leverage this pattern in a pragmatic way from within our applications.

To really understand these concepts, we will be writing a Phoenix application that relies on GenServers as the primary datasource that powers our business logic. In regards to our database, we will only be leveraging it as a means of persistent storage only when needed. Specifically, we will be performing all “read” operations from our GenServers and only falling back to Postgres when we need to perform some sort of mutation. Finally, we’ll adjust our application slightly to use the database directly in order to see how our performance characteristics differ between the two implementations. In addition, we’ll be using tools such as Registry and DynamicSupervisor in order to implement this architecture. We have a lot of ground to cover, so without further ado, let’s dive right into things!

## What is the Actor Model?

The Actor Model is a programming model that aims to provide a mechanism for dealing with and reasoning about concurrent programs. There are many paradigms and methodologies that exist to provide a pattern for concurrent programming and the Actor Model is just one of those. There are other concurrency models like CSP (Communicating Sequential Processes) and shared memory concurrency (using threads and locks), but for the purposes of this series we’ll be focusing specifically on the Actor Model and won’t draw many comparisons between the other models (if this is a topic that interests you, I would suggest picking up a copy of Seven Concurrency Models in Seven Weeks \[2\]).

So what exactly are some of the characteristics of an Actor Model implementation? An “actor” within an Actor Model system is something that is able to perform some work or computation. This actor is able to communicate with other actors only via message passing, and is able to guarantee that it alone has control over its own internal state. In other words, an actor is an independent entity that can work by itself or in concert with other actors but only through a clearly defined boundary. It should also be noted that when performing message passing between different actors, the data that is sent is copied and there is no shared mutable state between the two actors. If you are familiar with Erlang and/or Elixir, all this may sound familiar to you. If the word “GenServer” came to mind then you are absolutely on the right track! If not, keep reading and all will be clear :).

Enjoying the blog post so far? Follow me on Twitter for more content [**Follow @akoutmos**](https://twitter.com/intent/follow?screen_name=akoutmos "akoutmos Twitter")

* * *

Sign up for the mailing list and get notified via email when new blog posts come out.

## How does the Actor Model work on the BEAM?

In the context of the BEAM, an actor is a process (not an OS process but rather a process running in the Erlang virtual machine). This process is lightweight compared to an Operating System process and is preemptively scheduled within the BEAM by a scheduler (be sure to checkout \[7\] for detailed information regarding the inner workings of the BEAM scheduler). When the BEAM is running on a multicore machine, there is usually 1 scheduler running per CPU core and each of these schedulers will give each BEAM process a fair amount of time (see \[3\] for more details) to do the work that it has to do. Once its time is up, the BEAM will suspend that process and schedule another process to run for a fair amount of time. This cycle repeats so that every process gets a fair slice of time to use the CPU and perform computations.

Each of these processes has what is known as a “mailbox” from which it can read messages that have been sent to it by other processes. These messages are arranged in a queue and are processed one at a time as atomic operations. In other words, a process can only consume and act upon a single message at a time. While consuming only one message at a time may seem limiting and inefficient, it is actually a very important characteristic as it allows your actors to perform their operations without worrying about synchronizing their internal state with incoming messages. With a single process handling a single message from the mailbox at a time, this makes everything very easy to reason about.

While a single process can only do a single thing at a time, the real power of the BEAM comes from the fact that you can have thousands upon thousands of processes all running concurrently and performing valuable work. In addition, given that the preemptive scheduler on the BEAM does not allow any single process to hold the CPU hostage, you can see how this programming model lends itself quite nicely to concurrent applications. I would highly suggest watching Saša Jurić’s talk on The Soul of Erlang and Elixir \[6\] if you would like to see this in action.

## Show me the code!

In order to put these concepts into practice and to fully appreciate the power that we have at our disposal when leveraging the BEAM, we will be creating an application whose core business logic is powered by GenServers. We will also be sure to instrument our application with Phoenix LiveDashboard so that we can measure the performance of our application under load. Once we have everything in place, we will then refactor our application slightly to act as a traditional stateless application where all state resides in the database. With these two competing implementations and a stress test suite in place, we will be able to objectively see under what conditions each is best suited.

The application that we will be writing is a book store application. We will expose our functionality via a RESTful API powered by Phoenix. Our book store application will be able to keep track of all of the books that our store sells along with how many of each book we have on hand. When books are ordered, the inventory will be adjusted accordingly to reflect how much of each book we have left. We have quite a bit of work ahead of us so, with that all being said, let’s jump right into it!

## Step 1: Create a new Phoenix project and install dependencies - [commit](https://github.com/akoutmos/book_store/commit/172c86d)

Install the Phoenix project generator (if you don’t already have it installed) by running:

```
$ mix archive.install hex phx_new 1.5.3
```

With that done and in place, we’ll want to generate a new Phoenix project. You can replace `book_store` with what ever you want to call your project and can also re-enable generator features as you see fit. Run the following to generate your project:

```
$ mix phx.new book_store --no-webpack --no-html --no-gettext
```

Once your project is created, open up your `mix.exs` file and modify your `application/0` and `deps/0` functions as follows:

```
def application do
  [
    mod: {BookStore.Application, []},
    extra_applications: [:logger, :runtime_tools, :os_mon]
  ]
end

...

def deps do
  [
    ...
    {:floki, "~> 0.26.0"},
    {:httpoison, "~> 1.6"}
  ]
end
```

With all that in place go ahead and run `mix deps.get` to fetch all of your dependencies. The `:os_mon` atom that is added to `:extra_applications` is used to enable the “OS Data” tab in Phoenix LiveDashboard. With that in place it is time to write a simple web scraper using Floki so that we can have some useful application data.

## Step 2: Writing a data scraper using Floki - [commit](https://github.com/akoutmos/book_store/commit/8a4ba14)

In order to have a realistic feeling application, we will populate our online book store with books from the Manning catalog \[4\]. We will leverage HTTPoison and Floki to scrape all of the book links and then crawl all the book links for the relevant data that will power our application. You can find the results from the scraping the Manning catalog on the project GitHub as not to put unnecessary load on Manning’s site :). Our first step is to fetch all of the book links. Let’s create a new file at `lib/book_store/manning_book_scraper.ex` with the following contents:

```
defmodule BookStore.ManningBookScraper do
  def get_all_manning_books do
    books_data =
      get_manning_catalog_page()
      |> get_book_links_from_page()
      |> Task.async_stream(
        fn book ->
          get_book_details(book)
        end,
        max_concurrency: 5,
        timeout: 10_000
      )
      |> Enum.reduce([], fn {:ok, book_details}, acc ->
        [book_details | acc]
      end)
      |> inspect(pretty: true, limit: :infinity)

    data_file_location()
    |> File.write(books_data)
  end

  def data_file_location, do: "./books_data.exs"

  defp get_manning_catalog_page do
    %HTTPoison.Response{body: body} = HTTPoison.get!("https://www.manning.com/catalog")

    body
  end

  defp get_book_links_from_page(page_source) do
    page_source
    |> Floki.parse_document!()
    |> Floki.find("a.catalog-link")
    |> Enum.map(fn a_tag ->
      %URI{
        path: Floki.attribute(a_tag, "href"),
        host: "www.manning.com",
        scheme: "https"
      }
      |> URI.to_string()
    end)
  end
end
```

The above snippet will scrape the Manning catalog page [https://www.manning.com/catalog](https://www.manning.com/catalog) and the look for all of the `a` tags with the `.catalog-link` class using Floki. The `href` attribute is then plucked from the `a` tag and put into the path of a `URI` struct which is then output as a string. Those links are then passed to `get_book_details/1` inside of a `Task.async_stream/3` call. Let’s implement that function next and wrap up the scraper:

```
defmodule BookStore.ManningBookScraper do
  ...

  defp get_book_details(book_url) do
    %HTTPoison.Response{body: body} = HTTPoison.get!(book_url)

    parsed_page = Floki.parse_document!(body)

    %{
      title: get_title_from_book_page(parsed_page),
      authors: get_authors_from_book_page(parsed_page),
      description: get_description_from_book_page(parsed_page),
      price: get_price_from_book_page(parsed_page)
    }
  end

  defp get_title_from_book_page(parsed_page) do
    parsed_page
    |> Floki.find(".visible-sm .product-title")
    |> Floki.text(deep: false)
    |> String.trim()
  end

  defp get_authors_from_book_page(parsed_page) do
    parsed_page
    |> Floki.find(".visible-sm .product-authorship")
    |> Floki.text(deep: false)
    |> String.split([",", "and"])
    |> Enum.map(fn author ->
      String.trim(author)
    end)
    |> Enum.reject(fn
      "" -> true
      _ -> false
    end)
  end

  defp get_description_from_book_page(parsed_page) do
    primary_lookup =
      parsed_page
      |> Floki.find(".description-body > p")
      |> Floki.text(deep: false)
      |> String.trim()

    secondary_lookup =
      parsed_page
      |> Floki.find(".description-body")
      |> Floki.text(deep: false)
      |> String.trim()

    if primary_lookup == "", do: secondary_lookup, else: primary_lookup
  end

  defp get_price_from_book_page(parsed_page) do
    book_id =
      parsed_page
      |> Floki.find(".all-buy-bits-type-combo form[action=\"/cart/addToCart\"]")
      |> Floki.attribute("data-product-offering-id")

    parsed_page
    |> Floki.find("#price-#{book_id}")
    |> Floki.text(deep: false)
    |> String.trim()
    |> case do
      "" -> :not_for_sale
      value -> value
    end
  end
end
```

I won’t add too much explanation here as this code is mostly CSS selectors and data manipulation to extract what we need for the remainder of the project. The important thing to note is that we are extracting the following fields:

```
%{
  title: ..., # The title of the book
  authors: ..., # A list of all the authors associated with the book
  description: ..., # A short description of the book
  price: ... # A string representing the price
}
```

This scrape script is far from perfect given it doesn’t address any error conditions and some of the strings that are captured are not perfect…but it will more than suffice for this tutorial and is way more interesting than “Lorem Ipsum” :). Going forward, I’ll assume that you either fetched the `books_data.exs` file from the GitHub repo or ran `BookStore.ManningBookScraper.get_all_manning_books()` inside of an IEx session to generate the file.

## Step 3: Seeding our database with sample data - [commit](https://github.com/akoutmos/book_store/commit/ad5d6aa)

In order to load the data generated in the previous step into the database, we’ll need a migration that creates all of the necessary fields and an Ecto schema that mirrors the migration. Let’s start by creating a migration by running `mix ecto.gen.migration books` and put the following contents into the file:

```
defmodule BookStore.Repo.Migrations.Books do
  use Ecto.Migration

  def change do
    create table(:books, primary_key: false) do
      add :id, :binary_id, primary_key: true
      add :title, :string
      add :authors, {:array, :string}
      add :description, :text
      add :price, :string
      add :quantity, :integer

      timestamps()
    end
  end
end
```

Next, let’s create our Ecto Schema so that we can work with book information. Create the file `lib/book_store/books/book.ex` with the following contents:

```
defmodule BookStore.Books.Book do
  use Ecto.Schema

  import Ecto.Changeset

  alias __MODULE__

  @derive {Jason.Encoder, only: ~w(title authors description price quantity)a}
  @primary_key {:id, :binary_id, autogenerate: true}
  @foreign_key_type :binary_id
  schema "books" do
    field :title, :string
    field :authors, {:array, :string}
    field :description, :string
    field :price, :string
    field :quantity, :integer

    timestamps()
  end

  @doc false
  def changeset(%Book{} = book, attrs) do
    book
    |> cast(attrs, ~w(title authors description price quantity)a)
    |> validate_required(~w(title authors description quantity)a)
  end
end
```

If this were a “production grade” application, we would have more involved changesets and input validation, but this will suffice for now. Also notice that we have the `@derive` attribute defined in our schema. The reason that we do this is so that when it comes time to return JSON to the client, we can just call `json(conn, book)` from our controller and the serialization will be taken care of for us automatically via the `Jason.Encoder` protocol (in a production application I would suggest using JSON views \[5\]).

Next we’ll want to update our `priv/repo/seeds.exs` script so that our sample data can be loaded into the database:

```
alias BookStore.Books.Book
alias BookStore.Repo

{book_data, _} =
  BookStore.ManningBookScraper.data_file_location()
  |> Code.eval_file()

book_data
|> Enum.map(fn
  %{price: :not_for_sale} = book ->
    book
    |> Map.put(:price, "N/A")
    |> Map.put(:quantity, 0)

  book ->
    book
    |> Map.put(:quantity, 5_000)
end)
|> Enum.each(fn book ->
  %Book{}
  |> Book.changeset(book)
  |> Repo.insert()
end)
```

Our seed script reads all of the data that was captured from our `BookStore.ManningBookScraper` module, and then inserts it all into the database.

To verify that everything has been put together correctly, let’s start up our application along with a Postgres instance and give all of this a whirl. In a terminal run the following to stand up Postgres Docker container and start of the application:

```
# Run this command in one terminal session
$ docker run -p 5432:5432 -e POSTGRES_PASSWORD=password postgres:12

# Run these commands in a separate terminal session
$ mix ecto.setup
$ iex -S mix phx.server
```

The first command will download (if you don’t already have the image locally) and run the Postgres 12 container. Wait for the logs to come to a stop so that you are sure the container is up and running before proceeding. Also note that we have not attached any volumes to our docker run command. As a result, if you kill the container, you will lose all data that has been persisted to Postgres. This is not a big deal for our purposes here, but just something to keep in mind :).

With Postgres running, we can run our Ecto setup Mix command and get things rolling. The `mix ecto.setup` command will automatically create the database, run all the pending migrations, and also run our seed script. After that is done and Phoenix is up and running via `iex -S mix phx.server` you can either open up `psql` to verify that all of the test data is present, or you can run a Repo call in the currently running IEx session:

```
postgres@localhost:5432 [book_store_dev]> select count(*) from books;
 count
-------
  1183
(1 row)

Time: 1.637 ms
```

```
iex(1) ▶ BookStore.Repo.all(BookStore.Books.Book) |> length()
[debug] QUERY OK source="books" db=32.5ms queue=0.1ms idle=1355.8ms
SELECT i0."id", i0."title", i0."authors", i0."description", i0."price", i0."quantity", i0."inserted_at", i0."updated_at"
FROM "books" AS i0 []
1183
```

## Closing thoughts

Well done and thanks for sticking with me to the end! We covered quite a lot of ground and hopefully you picked up a couple of cool tips and tricks along the way. To recap, we laid the foundation for our Elixir Phoenix application, put together our web scraper and fetched some sample data for our application. You may be wondering to your self…“Where’s the Actor Model goodness that I was promised!?”. Rest assured all of that will be answered in Part 2!

With the base of our application in place and sample data to work with, Part 2 will focus on leveraging Registry and DynamicSupervisor so that we can interact with our application via GenServer processes instead of always needing the database. We’ll also use Phoenix LiveDashboard to take some before and after measurements to see what kind of an impact this design can have on our system.

Be sure to sign up for the mailing list and/or follow me on Twitter so that you won’t miss Part 2! Feel free to leave comments or feedback or even what you would like to see in the next tutorial. Till next time!

Enjoying the blog post so far? Follow me on Twitter for more content [**Follow @akoutmos**](https://twitter.com/intent/follow?screen_name=akoutmos "akoutmos Twitter")

* * *

Sign up for the mailing list and get notified via email when new blog posts come out.

## Additional Resources

Below are some additional resources if you would like to deep dive into any of the topics covered in the post.

*   \[1\] [https://en.wikipedia.org/wiki/Concurrent\_computing](https://en.wikipedia.org/wiki/Concurrent_computing)
*   \[2\] [https://pragprog.com/titles/pb7con/](https://pragprog.com/titles/pb7con/)
*   \[3\] [https://blog.stenmans.org/theBeamBook/#\_scheduling\_non\_preemptive\_reduction\_counting](https://blog.stenmans.org/theBeamBook/#_scheduling_non_preemptive_reduction_counting)
*   \[4\] [https://www.manning.com/catalog](https://www.manning.com/catalog)
*   \[5\] [https://hexdocs.pm/phoenix/views.html#rendering-json](https://hexdocs.pm/phoenix/views.html#rendering-json)
*   \[6\] [https://www.youtube.com/watch?v=JvBT4XBdoUE](https://www.youtube.com/watch?v=JvBT4XBdoUE)
*   \[7\] [https://hamidreza-s.github.io/erlang/scheduling/real-time/preemptive/migration/2016/02/09/erlang-scheduler-details.html](https://hamidreza-s.github.io/erlang/scheduling/real-time/preemptive/migration/2016/02/09/erlang-scheduler-details.html)

* * *
