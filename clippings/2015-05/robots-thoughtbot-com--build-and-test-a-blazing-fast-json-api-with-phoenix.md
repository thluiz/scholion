---
url: "https://robots.thoughtbot.com/testing-a-phoenix-elixir-json-api?utm_campaign=Elixir+Radar&utm_source=hs_email&utm_medium=email&utm_content=17534844&_hsenc=p2ANqtz--_LEJbU9r6PN_QggZlPemtrA5uvuSiDn1CHFDBaYTmcGahTVGq3PaQ8592P4uC1_etr4w8Hcl2O-N-b15BNkLwn9M7Iw&_hsmi=17534844"
captured_at: "2015-05-07T13:16:46-03:00"
title: "Build and test a blazing fast JSON API with Phoenix, an Elixir framework"
domain: "robots-thoughtbot-com"
---

# Build and test a blazing fast JSON API with Phoenix, an Elixir framework

Let’s build a JSON API that serves a list of contacts. We’ll be writing it
using Elixir and Phoenix. [Phoenix](http://www.phoenixframework.org/) is a
framework written in Elixir that aims to make writing fast, low latency web
applications as enjoyable as possible. This will not go through installing
Elixir or Phoenix. See the
[Phoenix Guides](http://www.phoenixframework.org/v0.10.0/docs/getting-started)
to get started.

### Why Elixir and Phoenix?

Erlang is a Ferrari wrapped in the sheet metal of an old beater. It has
immense power, but to many people, it looks ugly. It has been used by
WhatsApp to handle billions of connections, but many people struggle with
the unfamiliar syntax and lack of tooling. [Elixir](http://elixir-lang.org/)
fixes that. It is built on top of Erlang, but has a beautiful and enjoyable
syntax, with tooling like
[mix](http://elixir-lang.org/getting-started/mix-otp/introduction-to-mix.html)
to help build, test and work with applications efficiently.

Phoenix builds on top of Elixir to create very low latency web applications, in
an environment that is still enjoyable. Blazing fast applications and an
enjoyable development environments are no longer mutually exclusive. Elixir
and Phoenix give you both. Response times in Phoenix are often measured in
*microseconds* instead of milliseconds.

Now that we’ve discussed why we might want to build something in with this
framework, let’s build something!

### Writing the test

See [getting started](http://www.phoenixframework.org/v0.10.0/docs)
on the Phoenix website to see how to create a new app called `HelloPhoenix`.
We’ll be using Phoenix 0.10.0 for this exercise.

Now that you have your Phoenix app setup let’s start by writing a test.
Let’s create a file at `test/controllers/contact_controller_test.exs`

```
defmodule HelloPhoenix.ContactControllerTest 
   ExUnit.Case, async: false
   Plug.Test
  alias HelloPhoenix.Contact
  alias HelloPhoenix.Repo
  alias Ecto.Adapters.SQL

  setup 
    begin_test_transaction(Repo)

    on_exit  ->
      rollback_test_transaction(Repo)
    
  

  test "/index returns a list of contacts" 
    contacts_as_json =
      %Contact{name: "Gumbo", phone: "(801) 555-5555"}
      |> Repo.insert
      |> List.wrap
      |> Poison.encode!

    response = conn(, "/api/contacts") |> send_request

    assert response.status == 
    assert response.resp_body == contacts_as_json
  

  defp send_request(conn) 
    conn
    |> put_private(:plug_skip_csrf_protection, )
    |> HelloPhoenix.Endpoint.call([])
```

We write a `setup` function to wrap our Ecto calls in a transaction that will
ensure that our database is always empty when we start our tests.

The test itself does what you would expect. `use Plug.Test` gives us access
to the `conn/2` function for creating test connections. In our test we
insert a new Contact, wrap it in a list and then encode it. After that we
create a new connection and send the request. We assert that the response
was successful and that the body contains a list of contacts encoded as
JSON.

Run `mix test` and we’ll see the error `HelloPhoenix.Contact.__struct__/0 is
undefined, cannot expand struct HelloPhoenix.Contact`. This means we haven’t
yet created our model. Let’s use [Ecto](https://github.com/elixir-lang/ecto) for
hooking up to a Postgres database.

### Creating our databases

Ecto uses a repository for saving and retrieving data from a database.
Phoenix already comes with a repo set up and a default configuration. Make
sure your Postgres username and password are correct in `config/dev.exs` and
`config/test.exs`.

Let’s see what new `mix` tasks we get from Ecto by running `mix -h | grep ecto`.

You’ll see a number of tasks you can use. For now let’s create the dev and
test databases. After that we can add our first model.

```
# This will create your dev database
$ mix ecto.create
# This will create your test database
$ env MIX_ENV=test mix ecto.create
```

### Adding the Contact model

Let’s add a schema for `Contact` at `web/models/contact.ex`.

```
defmodule HelloPhoenix.Contact 
   Ecto.Model

  schema "contacts" 
    field :name
    field :phone

    timestamps
```

Next we’ll create a migration with `mix ecto.gen.migration create_contacts`. In
the newly generated migration, write this:

```
defmodule HelloPhoenix.Repo.Migrations.CreateContacts 
   Ecto.Migration

   change 
    create table(:contacts) 
      add :name
      add :phone

      timestamps
```

The default column type for Ecto migrations is `:string`. To see what else
you can do, check out the
[Ecto.Migration docs](http://hexdocs.pm/ecto/Ecto.Migration.html).

Now run `mix ecto.migrate` to create the new table, and once more for test
`MIX_ENV=test mix ecto.migrate`.

### Adding the routes and controller

Let’s get to our API endpoint with a route that will look like `/api/contacts`.

```
# In our web/router.ex
defmodule HelloPhoenix.Router 
   Phoenix.Router

  pipeline  
    plug :accepts, ["json"]
  

  scope "/api", HelloPhoenix 
    pipe_through 

    resources "/contacts", ContactController
```

If you’re coming from Rails, you’ll note that `/api/contacts.json` will
result in a 404 not found. You are expected set the appropriate request
header. In a pinch you can do `/api/contacts?format=json`, but this is not
recommended. The trailing format param was not added for performance reasons
and because HTTP headers already enable this functionality.

Now, if we run `mix test` we see that we still need a `ContactController`.

```
** (UndefinedFunctionError) undefined function: HelloPhoenix.ContactController.init/1 (module HelloPhoenix.ContactController is not available)
```

Let’s create our controller at `web/controllers/contact_controller.ex`

```
defmodule HelloPhoenix.ContactController 
   HelloPhoenix.Web, :controller
  alias HelloPhoenix.Repo
  alias HelloPhoenix.Contact

  plug :action

   index(conn, _params) 
    contacts = Repo.all(Contact)
    render conn, contacts: contacts
```

First we make sure to get all the Contacts with `Repo.all(Contact)`. Then we
render JSON with `Phoenix.Controller.render/2`. The function is automatically
imported when we call `use HelloPhoenix.Web, :controller`. Check out
`web/web.ex` to see what else is imported.

If we run `mix test` our tests won’t pass quite yet.

```
** (UndefinedFunctionError) undefined function: HelloPhoenix.ContactView.render/2 (module HelloPhoenix.ContactView is not available)
```

We need a view to render our JSON.

### Rendering our JSON with a view

Views handle how to output our JSON. Right now it’s pretty simple, but in
the future, this is where we could change what we send based on user’s
permissions for example.

Let’s create a file in `web/views/contact_view.ex`

```
defmodule HelloPhoenix.ContactView 
   HelloPhoenix.Web, :view

   render("index.json", %{contacts: contacts}) 
    contacts
```

This will use pattern matching to set and then return `contacts`. Phoenix
will automatically encode the array of contacts to JSON. You can use this
view function to customize how the JSON is presented, but we’ll cover that in a
later post.

At this point when you run `mix test` all tests should pass.

### Cleanup

Let’s check out `HelloPhoenix.Web` in `web/web.ex` to cleanup our app a bit
more. If we open that file up we see that the controller function already
has an alias for `HelloPhoenix.Repo`.

```
   controller 
    quote 
      # Auto generated - This imports all the macros and functions that a controller needs.
       Phoenix.Controller

      # Auto inserted - The app was generated with an alias to Repo as a convenience.
      alias HelloPhoenix.Repo

      # This imports the router helpers so you can generate paths like
      # `api_contacts_path(conn)`
      import HelloPhoenix.Router.Helpers
```

This means that in your controller you can remove your alias for
`HelloPhoenix.Repo`.

Let’s use
[ExUnit.CaseTemplate](http://elixir-lang.org/docs/stable/ex_unit/ExUnit.CaseTemplate.html)
to clean up our tests a bit. In `test/test_helper.exs`

```
# Add this above `ExUnit.start`
defmodule HelloPhoenix.
   ExUnit.CaseTemplate
  alias Ecto.Adapters.SQL
  alias HelloPhoenix.Repo

  setup 
    begin_test_transaction(Repo)

    on_exit  ->
      rollback_test_transaction(Repo)
    
  

  using 
    quote 
      alias HelloPhoenix.Repo
      alias HelloPhoenix.Contact
       Plug.Test

      # Remember to change this from `defp` to `def` or it can't be used in your
      # tests.
       send_request(conn) 
        conn
        |> put_private(:plug_skip_csrf_protection, )
        |> HelloPhoenix.Endpoint.call([])
```

Adding code to `using` will make those functions and aliases available in
every test. This makes it so that we can remove `send_request/1` and the other
alias from our test and replace it with `use HelloPhoenix.Case`

```
defmodule HelloPhoenix.ContactControllerTest 
   HelloPhoenix.Case, async: false
  # We removed the other aliases since they're already included in
  # `HelloPhoenix.Case`. We also removed the `setup` macro.

  test "/index returns a list of contacts" 
    contacts_as_json =
      %Contact{name: "Gumbo", phone: "(801) 555-5555"}
      |> Repo.insert
      |> List.wrap
      |> Poison.encode!

    response = conn(, "/api/contacts") |> send_request

    assert response.status == 
    assert response.resp_body == contacts_as_json
  

  # We also removed the function definition for `send_request/1`
```

### That’s a wrap

Now you’ve seen how to create and test a Phoenix JSON API. We’ve also
learned how to cleanup our files and make it easier to use our modules in
other controllers and tests in the future by using `HelloPhoenix.Web` and
`ExUnit.CaseTemplate`. You can now deploy this app to Heroku with the [Elixir
buildpack](https://github.com/HashNuke/heroku-buildpack-elixir).
