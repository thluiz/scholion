---
url: "https://semaphoreci.com/community/tutorials/test-driven-apis-with-phoenix-and-elixir"
captured_at: "2016-01-25T08:48:07-03:00"
title: "Test-Driven APIs with Phoenix and Elixir"
domain: "semaphoreci-com"
---

# Test-Driven APIs with Phoenix and Elixir

Learn how to use fast feedback provided by TDD to better understand some of the Phoenix and Elixir components while implementing a feature.

**Brought to you by**

### Semaphore

[Learn More](https://semaphoreci.com/)

### Introduction

Starting with a new technology can be difficult. It usually takes some time to
understand the components and the way they work together. In this tutorial,
we're going to create an API, using Test Driven Development (TDD) to guide us
through its implementation. You'll learn how the feedback provided by our test
helps save us time. It does so by showing us clues on every fail and giving us
a better understanding of how things work.

### Prerequisites

First of all, let's make sure we have all the components we need:

Check your Elixir version to ensure it matches the one we're using:

```
→ elixir --version
Elixir 1.1.1
```

### Getting Started

We will start by thinking about what we want from our implementation. If we
simply jump into generators, things will probably work, but we will have a lot
of useless code in our codebase, and no understanding of the layers. Since we
want to create an API, we do not need any HTML views or stylesheets. That's
a good place to start:

```
mix phoenix.new watchlist --no-html --no-brunch
```

Make sure to reply with yes (Y) to install the dependencies:

```
Fetch and install dependencies? [Yn] Y
```

We don't need a database right now, but we will create one, since we are going
to use it at a later stage. We'll use Phoenix's default database, PostgreSQL.

```
mix ecto.create
```

This will compile the project and test our connection to the database. A failure
of `ecto.create` looks as follows:

```
** (Mix) The database for Watchlist.Repo couldn't be created, reason given: psql: could not connect to server: Connection refused
```

Sometimes when the OS crashes, a Postgres lock file remains on the file system,
making Postgres assume that there is a connection available:

```
rm /usr/local/var/postgres/postmaster.pid
```

Start (or restart) your Postgres server, and you'll be good to go:

```
→ mix ecto.create
The database for Watchlist.Repo has been created.
```

Now everything looks fine. We can start thinking about our first feature.

### Developing a Feature: Listing Movies

It's time to start thinking about the feature. We should avoid dealing with the
implementation details as much as possible.

#### Adding an API Endpoint

What do we know so far? We'll return a JSON response, which means that we need a
JSON library. We need `Poison`. Let's start by adding the following dependencies
to `mix.exs`:

```
   :phoenix "~> 1.0.4"
    :phoenix_ecto "~> 1.1"
    :postgrex ">= 0.0.0"
    :cowboy "~> 1.0"
    :poison "~> 1.5"
```

Next, we'll run `mix deps.get` to get those dependencies.

It's time to create an integration test. Create a `test/integration` directory
and a file named `listing_movies_test.exs` inside it.

Listing movies requires a get request for a movies resource. We need a HTTP GET
request to a '/movies' URI to return some content and a 200 status code.

We'll start with a simple:

```
defmodule ListingMoviesIntegrationTest 
   ExUnit.Case async 

   'listing movies' 
    response   '/movies'
    assert responsestatus
```

Here's how this will work: we'll add this test and run it. After running the
test, we will make changes every time it fails until we've added just enough
code to make it pass. We'll use `mix test
test/integration/listing_movies_test.exs` to run the test. The test returns the
following error message:

```
** (CompileError) test/integration/listing_movies_test.exs:5: function conn/2 undefined
```

We need `Plug`. Let's add it to `test/integration/listing_movies_test.exs`:

```
 Plug.Test
```

When we run it again, we'll get the following output:

```
  1) test listing movies (ListingMoviesIntegrationTest)
     test/integration/listing_movies_test.exs:5
     ** (FunctionClauseError) no function clause matching in URI.parse/1
     stacktrace:
       (elixir) lib/uri.ex:292: URI.parse('/movies')
       (plug) lib/plug/adapters/test/conn.ex:10: Plug.Adapters.Test.Conn.conn/4
       test/integration/listing_movies_test.exs:6
```

The problem here is the single quotes. Elixir provides double quoted strings.
Single quotes are for char lists. Let's fix this:

```
response   "/movies"
```

```
  1) test listing movies (ListingMoviesIntegrationTest)
     test/integration/listing_movies_test.exs:5
     Assertion with == failed
     code: response.status() == 200
     lhs:  nil
     rhs:  200
     stacktrace:
       test/integration/listing_movies_test.exs:7
```

We don't have a status code because we are creating a connection, but we're not
making a call to an endpoint with it. Let's add one. We'll need to call a
router, connect to it, and get a response:

```
defmodule ListingMoviesIntegrationTest 
   ExUnit.Case async 
   Plug.Test
  alias Watchlist.Router

  @opts Router
   'listing movies' 
       "/movies"
    response  Router @opts
    assert responsestatus
```

```
   1) test listing movies (ListingMoviesIntegrationTest)
     test/integration/listing_movies_test.exs:7
     ** (Phoenix.Router.NoRouteError) no route found for GET /movies (Watchlist.Router)
     stacktrace:
       (watchlist) web/router.ex:1: Watchlist.Router.match/4
       (watchlist) web/router.ex:1: Watchlist.Router.do_call/2
       test/integration/listing_movies_test.exs:9
```

The test fails because we don't have a route. We're making progress. Let's open
`web/router.ex` and add our route:

```
scope  Watchlist 
  pipe_through 

   "/movies" MovieController :index
```

We'll run the test again even though we know it is going to fail. In this case,
we'll get the following output:

```
   1) test listing movies (ListingMoviesIntegrationTest)
     test/integration/listing_movies_test.exs:7
     ** (Plug.Conn.WrapperError) ** (UndefinedFunctionError) undefined function: Watchlist.MovieController.init/1 (module Watchlist.MovieController is not available)
     stacktrace:
       Watchlist.MovieController.init(:index)
       (watchlist) web/router.ex:1: anonymous fn/1 in Watchlist.Router.match/4
       (watchlist) lib/phoenix/router.ex:255: Watchlist.Router.dispatch/2
       (watchlist) web/router.ex:1: Watchlist.Router.do_call/2
       test/integration/listing_movies_test.exs:9
```

So, we need to create a controller. Let's create a `movie_controller.ex` file on
the `web/controllers` directory:

```
defmodule Watchlist.MovieController 
   Watchlist.Web :controller

   index _params 
    render  movies
```

```
  1) test listing movies (ListingMoviesIntegrationTest)
     test/integration/listing_movies_test.exs:7
     ** (Plug.Conn.WrapperError) ** (UndefinedFunctionError) undefined function: Watchlist.MovieView.render/2 (module Watchlist.MovieView is not available)
```

Our action needs a view. Creating a `movie_view.ex` under `web/views` will fix
that:

```
defmodule Watchlist.MovieView 
   Watchlist.Web :view

   render"index.json" movies movies 
    movies
```

Let's run it again:

```
Compiled web/views/movie_view.ex
Generated watchlist app
.

Finished in 0.2 seconds (0.2s on load, 0.01s on tests)
1 test, 0 failures
```

Our first test has passed. Let's add an assertion for the body to make sure we
are on the right path:
`assert response.resp_body == "[]"`

The test passes. Now, let's try to consume our resource from bash, run the
server with `mix phoenix.server`, and use curl to retrieve the movies:

```
→ curl localhost:4000/movies
[]
```

#### Adding a Model

It works — our empty list is being returned. Now, we need to add a movie model
to persist our movies. Again, we'll use TDD to drive how our model is going to
look. We could read the model straight away, but adding it to our test first
will give us some time to consider what we want it to look like. Let's give it
a name and a rating, and assert its return:

```
defmodule ListingMoviesIntegrationTest 
   ExUnit.Case async 
   Plug.Test
  alias Watchlist.Router

  @opts Router
   'listing movies' 
    movie  Movie "Back to the future" rating 
            |> insert!

       "/movies"
    response  Router @opts

    assert responsestatus  
    assert responseresp_body  movie
```

```
** (CompileError) test/integration/listing_movies_test.exs:8: Movie.__struct__/0 is undefined, cannot expand struct Movie
    (elixir) src/elixir_map.erl:58: :elixir_map.translate_struct/4
```

Structure does not exist yet. Let's create it using the generator:

```
→ mix phoenix.gen.model Movie movies name rating:integer
* creating priv/repo/migrations/20151204182719_create_movie.exs
* creating web/models/movie.ex
* creating test/models/movie_test.exs

Remember to update your repository by running migrations:

    $ mix ecto.migrate
```

Now, migrate and take a look at `test/model/movie_test.exs` the generator
created for us:

```
defmodule Watchlist.MovieTest 
   Watchlist.ModelCase

  alias Watchlist.Movie

  @valid_attrs  "some content" rating 
  @invalid_attrs 

   "changeset with valid attributes" 
    changeset  MoviechangesetMovie @valid_attrs
    assert changesetvalid?
  

   "changeset with invalid attributes" 
    changeset  MoviechangesetMovie @invalid_attrs
    refute changesetvalid?
```

Let's run this test:

```
→ mix test test/models/movie_test.exs
..

Finished in 0.2 seconds (0.2s on load, 0.00s on tests)
2 tests, 0 failures
```

When we run the integration test again, we'll get the following error:

```
** (CompileError) test/integration/listing_movies_test.exs:8: Movie.__struct__/0 is undefined, cannot expand struct Movie
    (elixir) src/elixir_map.erl:58: :elixir_map.translate_struct/4
```

We've created our structure, but we haven't added it to our test. Let's add it:

```
alias Watchlist.Movie
```

Let's run the test again:

```
  1) test listing movies (ListingMoviesIntegrationTest)
     test/integration/listing_movies_test.exs:8
     ** (UndefinedFunctionError) undefined function: Repo.insert!/1 (module Repo is not available)
     stacktrace:
       Repo.insert!(%Watchlist.Movie{__meta__: #Ecto.Schema.Metadata<:built>, id: nil, inserted_at: nil, name: "Back to the future", rating: 5, updated_at: nil})
       test/integration/listing_movies_test.exs:10
```

The structure is here, but we can't insert it without using `Repo`.

```
alias Watchlist.Repo
```

```
  1) test listing movies (ListingMoviesIntegrationTest)
     test/integration/listing_movies_test.exs:9
     Assertion with == failed
     code: response.resp_body() == movie
     lhs:  "[]"
     rhs:  %Watchlist.Movie{__meta__: #Ecto.Schema.Metadata<:built>, id: nil, inserted_at: nil, name: "Back to the future", rating: 5, updated_at: nil}
     stacktrace:
       test/integration/listing_movies_test.exs:17
```

There are still some things left to fix. First of all, we are returning a
string, and we should be returning a list of movies. Let's fix that in
`web/movie_controller.ex`:

```
defmodule Watchlist.MovieController 
   Watchlist.Web :controller
  alias Watchlist.Movie

   index _params 
    movies  Movie
    render  movies movies
```

```
  1) test listing movies (ListingMoviesIntegrationTest)
     test/integration/listing_movies_test.exs:9
     ** (Plug.Conn.WrapperError) ** (Poison.EncodeError) unable to encode value: {nil, "movies"}
```

This means that we are trying to encode metadata for the client, and Poison
won't allow us to do this by default. We can solve this by implementing
`Poison.Encoder` in our model.

```
defmodule Watchlist.Movie 
   Watchlist.Web :model

  schema "movies" 
    field :name :string
    field :rating :integer

    timestamps
  

  @required_fields ~w(name rating)
  @optional_fields 

   
  Creates a changeset based on the `model` and `params`.

  If no params are provided, an invalid changeset is returned
  with no validation performed.

   changesetmodel params  :empty 
    model
    |> params @required_fields @optional_fields
  

  defimpl Poison.Encoder  Watchlist.Movie 
     encodemovie _options 
      movie
      |> from_struct
      |> :__meta__ :__struct__
      |> Poisonencode!
```

Let's run the test again:

```
   1) test listing movies (ListingMoviesIntegrationTest)
     test/integration/listing_movies_test.exs:9
     Assertion with == failed
     code: response.resp_body() == movie
     lhs:  "[{\"updated_at\":\"2015-12-07T17:08:24Z\",\"rating\":5,\"name\":\"Back to the future\",\"inserted_at\":\"2015-12-07T17:08:24Z\",\"id\":91}]"
     rhs:  %Watchlist.Movie{__meta__: #Ecto.Schema.Metadata<:loaded>, id: 91, inserted_at: #Ecto.DateTime<2015-12-07T17:08:24Z>, name: "Back to the future", rating: 5,
            updated_at: #Ecto.DateTime<2015-12-07T17:08:24Z>}
```

Notice we get a JSON response, but it fails. Our expectation is not encoded.
Let's encode the model we've just created in our integration test:

```
|> insert!
|> Poisonencode!
```

The output now looks as follows:

```
  1) test listing movies (ListingMoviesIntegrationTest)
     test/integration/listing_movies_test.exs:9
     Assertion with == failed
     code: response.resp_body() == movie
     lhs:  "[{\"updated_at\":\"2015-12-07T17:11:27Z\",\"rating\":5,\"name\":\"Back to the future\",\"inserted_at\":\"2015-12-07T17:11:27Z\",\"id\":92}]"
     rhs:  "{\"updated_at\":\"2015-12-07T17:11:27Z\",\"rating\":5,\"name\":\"Back to the future\",\"inserted_at\":\"2015-12-07T17:11:27Z\",\"id\":92}"
```

We're comparing a list with a single movie. Let's fix that:

```
defmodule ListingMoviesIntegrationTest 
   ExUnit.Case async 
   Plug.Test
  alias Watchlist.Router
  alias Watchlist.Movie
  alias Watchlist.Repo

  @opts Router
   'listing movies' 
    Movie "Back to the future" rating  |> insert!
    movies  Movie
             |> Poisonencode!

       "/movies"
    response  Router @opts

    assert responsestatus  
    assert responseresp_body  movies
```

```
.

Finished in 0.8 seconds (0.6s on load, 0.1s on tests)
1 test, 0 failures
```

Let's try using it with Curl:

```
→ curl localhost:4000/movies
[{"updated_at":"2015-12-04T21:46:08Z","rating":5,"name":"Ilha das flores","inserted_at":"2015-12-04T21:46:08Z","id":1}]
```

Our resource is done. Let's run all of our specs to make sure everything is
working before going further:

```
→ mix test

  1) test renders 404.json (Watchlist.ErrorViewTest)
     test/views/error_view_test.exs:7
     Assertion with == failed
     code: render(Watchlist.ErrorView, "404.json", []) == %{"errors" => %{"detail" => "Page not found"}}
     lhs:  %{errors: %{detail: "Page not found"}}
     rhs:  %{"errors" => %{"detail" => "Page not found"}}
     stacktrace:
       test/views/error_view_test.exs:8

  2) test render 500.json (Watchlist.ErrorViewTest)
     test/views/error_view_test.exs:12
     Assertion with == failed
     code: render(Watchlist.ErrorView, "500.json", []) == %{"errors" => %{"detail" => "Server internal error"}}
     lhs:  %{errors: %{detail: "Server internal error"}}
     rhs:  %{"errors" => %{"detail" => "Server internal error"}}
     stacktrace:
       test/views/error_view_test.exs:13

  3) test render any other (Watchlist.ErrorViewTest)
     test/views/error_view_test.exs:17
     Assertion with == failed
     code: render(Watchlist.ErrorView, "505.json", []) == %{"errors" => %{"detail" => "Server internal error"}}
     lhs:  %{errors: %{detail: "Server internal error"}}
     rhs:  %{"errors" => %{"detail" => "Server internal error"}}
     stacktrace:
       test/views/error_view_test.exs:18

...

Finished in 0.3 seconds (0.3s on load, 0.06s on tests)
6 tests, 3 failures
```

When the --no-html option was implemented, it was made with this syntax. It's
already been fixed on master, and it should be part of the next Phoenix release.
For now, we can fix this ourselves.

```
defmodule Watchlist.ErrorViewTest 
   Watchlist.ConnCase async 

  # Bring render/3 and render_to_string/3 for testing custom views
  import Phoenix.View

   "renders 404.json" 
    assert renderWatchlist.ErrorView "404.json"  
           errors detail "Page not found"
  

   "render 500.json" 
    assert renderWatchlist.ErrorView "500.json"  
           errors detail "Server internal error"
  

   "render any other" 
    assert renderWatchlist.ErrorView "505.json"  
           errors detail "Server internal error"
```

When we run the test again, everything should be working properly.

### Conclusion

When writing code, we need to have confidence in what we do, and TDD is a
powerful tool for this. The feedback it gives us can make things clearer when
we're not sure how to implement a feature. The faster this feedback loop is, the
faster we'll move forward, even with new technologies.
