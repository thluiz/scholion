---
url: "https://amberbit.com/blog/2017/12/27/ecto-as-elixir-data-casting-and-validation-library"
captured_at: "2026-11-16T04:14:20+00:00"
title: "(Ab)using Ecto as Elixir data casting and validation library"
domain: "amberbit-com"
---

How do you create service modules that take user input, cast it and validate before executing? How do you write CQRS commands that validate payload before being executed?

After trying out different approaches for all of the above questions, nowadays I tend to respond with: just use Ecto as general-purpose data casting and validation library.

That’s great, but how?

## Ecto as database access layer

Ecto is mostly a database access library. You would define schemas that map directly to database tables. You would use `Repo` to fetch, and retrieve structs from database. You would also use migrations to change your database schema as you develop the application.

The other two components of Ecto are, however, opening additional use case possibilities. You can use `Ecto.Changeset`, including data casting and validations without `Ecto.Schema`, making it perfect for many other use cases.

## Let’s talk changesets

Ecto comes with concept of `changeset`. If you, like me, are coming from Rails or similar framework, the concept will be new. Overall, module [Ecto.Changeset](https://hexdocs.pm/ecto/Ecto.Changeset.html) defines bunch of functions that allow you to create changesets, cast data and manipulate various attributes of changesets. Let’s start with the basics, however.

A changeset represents _a set of changes_. This might seem obvious but let’s dig a bit deeper. When you are thinking in database tables, a changeset would represent all of the changes that user made to the underlying database table.

This changeset is created, given existing row from database, and params submitted to Phoenix controller as form data, parsed JSON or query string parameters.

In case of creating record, a changeset would carry over all the data user submitted using a form, that got processed (filtered out extra data, being casted to required types) and validated, _but is different from what row currently holds_. This means, a changeset does _not_ contain values for fields that were _not_ changed.

Conceptually, a changeset is not related at all to Ecto schemas / models. `App.User` module would often have `changeset` function to generate changeset, and would also `import Ecto.Changeset` for convenience, but you can use schemas without changeset at all. If you decide to do it, however, your responsibility is to cast and validate the data.

Let’s think we need a database table representing users. All we gather is their full name and e-mail address. I would often define my `App.User` schema to map to `users` database table this way:

```
defmodule App.User do
  use Ecto.Schema
  import Ecto.Changeset

  schema "users" do
    field :full_name, :string
    field :email, :string

    timestamps()
  end

  @allowed_fields [:full_name, :email]

  def changeset(%App.User{} = user \\ %App.User{}, %{} = params \\ %{}) do
    user
    |> Ecto.Changeset.cast(params, @allowed_fields)
    |> validate_required([:full_name])
  end
end
```

As you can see the `schema` macro takes a block, where we declare what fields and of which types user’s attributes are.

The interesting part is the `App.User.changeset/2` function. I often declare it this way, so both arguments are optional. Whenever I need to populate a form with empty values (creating new user), in my controller I would use:

```
def new(conn, _) do
  conn
  |> assign(:user_changeset, App.User.changeset())
  |> render "form.html"
end
```

and in the `update` function, I would create a changeset based on previously fetched `user` struct and submitted params:

```
def create(conn, %{"user" => user_params}) do
  ...
  user_changeset = App.User.changeset(user, user_params))
  case App.Repo.insert(user_changeset) do
    ...
  end
end
```

What happens behind this code, is that our `App.User.changeset/2` function creates a changeset based on form submitted by the user. For example, whenever user submits form for new user, “Hubert Łępicki”, “hubert.lepicki@amberbit.com” as `full_name` and `email` fields, the changeset would look as follows:

```
iex> App.User.changeset(%App.User{}, %{full_name: "Hubert Łępikci", email:
"hubert.lepicki@amberbit.com"})

#Ecto.Changeset<action: nil,
 changes: %{email: "hubert.lepicki@amberbit.com",
   full_name: "Hubert Łępikci"}, errors: [], data: #App.User<>, valid?: true>
```

And similar form for updating existing user would result in:

```
iex> App.User.changeset(%App.User{id: 1, full_name: "Hubert", email:
"hubert.lepicki@amberbit.com"}, %{full_name: "Hubert Łępikci", email:
"hubert.lepicki@amberbit.com"})

#Ecto.Changeset<action: nil, changes: %{full_name: "Hubert Łępikci"},
 errors: [], data: #App.User<>, valid?: true>
```

And when we miss some required parameter:

```
iex> App.User.changeset(%App.User{id: 1, full_name: "Hubert", email:
"hubert.lepicki@amberbit.com"}, %{full_name: ""})                         

#Ecto.Changeset<action: nil, changes: %{},
 errors: [full_name: {"can't be blank", [validation: :required]}],
 data: #App.User<>, valid?: false>
```

As you can see, in the first two examples we created a changeset for new user, and then created a changeset for existing user. Both changeset are valid, i.e. their validations passed, which `valid?: true` field tells us about.

In the third case, we did provide full name as blank string (we could also use `nil` here). We can see that changeset is no longer `valid?`, and appropriate error message is added to `errors` field in changeset struct. See how there is no error message on `email`? We did not provide any e-mail, but we did not specify the key in params either. This could lead to some errors if we assume validation will fail in this case. It won’t since validations are passing because we haven’t actually changed the `email` field at all. It must be present on the form we attempt to submit, or it must be present in the JSON we submit to controller. Moreover, the value has to be different to the one present before - otherwise there is no change visible in changeset.

None of the above changesets, however, would result in forms written using [Phoenix.Html](https://hexdocs.pm/phoenix_html/Phoenix.HTML.html) to render errors. This is because `action` attribute on changeset is not set. Whenever we render empty forms for `new` or `edit` actions, we usually do not want to see the validation errors until user submits the form. The `action` field on changeset is automatically set for us by calling `Repo.insert` or `Repo.update`, but if we do need to show validation errors without - we can either specify `action` ourselves `{changeset | action: :insert}` or use [Ecto.Changeset.apply\_action/2](https://hexdocs.pm/ecto/Ecto.Changeset.html#apply_action/2) which would be my personal preference. This will come in handy when dealing with changesets not backed up by schemas and database tables.

I believe what we did so far, is pretty standard pattern of doing things. This can be, however, mentally detached from thinking CRUD and database tables, to thinking _user input and commands_ as we see below. Ecto still comes in handy, even when we don’t have database to work with!

## Commands or services and not database schemas

In some cases, we do not want to write anything in the database, but we need to take user’s input, cast types and validate it. Let’s consider a contact form. We might have 3 required fields here: name, message and a checkbox asking user to accept `ToS` before submitting his or her details. We can put additional, optional e-mail field on the form as well. We take that information, and do something about it - only if all the requirements are met. In this case, a checkbox is checked, and user entered their name.

Let’s think of simple API, that will work for us and our `phoenix_html`\-backed contact form. We want to use form helpers with changesets so we display error messages when we need it. We might want to also pre-fill the form with some data. For now, something like this would do well:

```
defmodule AppWeb.ContactFormsController do
  use AppWeb, :controller

  def new(conn, _) do
    conn
    |> assign(:changeset, App.ContactForm.new())
    |> render "form.html"
  end 

  def create(conn, %{"contact_form" => form_params}) do
    case App.ContactForm.submit(form_params) do
      :ok ->
        render(conn, "success.html")

      {:error, changeset} ->

        conn
        |> assign(:changeset, changeset)
        |> render "form.html"

    end 
  end 
end
```

As you can see, the `new` and `create` actions are almost identical to what we would use with database-backed form submits. The only difference is that instead of `Repo.insert(changeset)` we are using custom service `App.ContactForm` and it’s function `submit/1` that accepts user’s input.

We expect this function to return `:ok` in case contact form was successfully filled in. Behind the scenes it would send e-mail to website owner with message entered by the user. In case of failure, we expect it to return tuple of `{:error, changeset}`. We assign this changeset and re-render form with error messages this time.

Let’s write the service:

```
defmodule App.ContactForm do
  import Ecto.Changeset

  @schema %{
    full_name: :string,
    email: :string,
    message: :string,
    accept_tos: :boolean
  }

  def new do
    # we could pre-fill with default values here
    cast(%{})
  end

  def submit(params) do
    case process_params(params) do
      {:ok, data} ->
        IO.inspect("New message from #{data.full_name}:")
        IO.inspect(data.message)
        :ok
      error ->
  error
    end
  end

  defp validate(changeset) do
    changeset
    |> validate_required([:full_name, :message])
    |> validate_acceptance(:accept_tos)
  end

  defp process_params(params) do
    params
    |> cast()
    |> validate()
    |> apply_action(:insert)
  end

  defp cast(params) do
    data = %{}
    empty_map = Map.keys(@schema) |> Enum.reduce(%{}, fn key, acc -> Map.put(acc, key, nil) end)

    changeset = {data, @schema} |> Ecto.Changeset.cast(params, Map.keys(@schema))

    put_in(changeset.changes, Map.merge(empty_map, changeset.changes))
  end
end
```

## Update as of 2020

You can now use `embedded_shema` directly to avoid some possible issues with above code.

```
    defmodule App.ContactForm do
        use Ecto.Schema
        import Ecto.Changeset

        embedded_schema do
            field(:full_name, :string)
            field(:email, :string)
            field(:message, :string)
            field(:accept_tos, :boolean)
        end

        @required_fields [:full_name, :messsage]
        @optional_fields [:accept_tos]

        def changeset(attrs) do
            %__MODULE__{}
            |> cast(attrs, @required_fields ++ @optional_fields)
            |> validate_required(@required_fields) 
        end

        ...

        # add submit() or any other higher-level function here
    end
```

Now, a few interesting things are happening here. First of, we declared `@schema` as a map of fields and types. This will be used by our `cast/1` function defined at the very bottom.

`cast/1` function takes parameters submitted by the user, and performs type cast using `@schema` definition and `Ecto.Changeset.cast/3` function. We need to also manually assemble `changeset.changes` to include all the fields user might not have submitted. Remember, Ecto’s validations only work if the keys in `changeset.changes` are present for fields that were left out blank. The last line in `cast/1` function ensures this is always happening, and user can’t cheat on our form validations by removing fields from HTML form.

The `new/0` and `submit/1` are our public API, the two functions that get exported but our service module. `new/0` creates an empty changeset, for use in `new` action in controller. If we wanted to pre-fill some fields, for example user’s name based on session data - we would do it here.

The `submit/1` function takes user input, processes it (casts, validates, sets `:action` field on changeset). If validations pass `apply_action` returns `{:ok, data}` tuple, where `data` is no longer a changeset, but a simple map with type-casted user input. We can fetch form fields with `data.full_name` or `data.message` for example, and send out e-mail to website owner.

In case of error, we return the changeset to controller.

The last bit of our puzzle is the form. Let’s keep it simple and create `form.html` with following:

```
<h2>New contact</h2>

<%= form_for @changeset, "/contact_form", [as: :contact_form], fn f -> %>
  <div>
    <%= text_input f, :full_name, placeholder: "Your full name" %>
    <%= error_tag f, :full_name %>
  </div>

  <div>
    <%= email_input f, :email, placeholder: "Your e-mail" %>
    <%= error_tag f, :email %>
  </div>

  <div>
    <%= textarea f, :message, placeholder: "Your message" %>
    <%= error_tag f, :message %>
  </div>

  <div>
    <label>
      <%= checkbox f, :accept_tos %>
      I accept Terms of Service
    </label>
    <%= error_tag f, :accept_tos %>
  </div>

  <%= submit "Submit" %>
<% end %>
```

If you play with this form, you will see that it only attempts to render `success.html` template, when you filled in full name and checked `accept_tos` field. If you attempt to send it without those details filled in, you will see error messages.

Congratulations, you just created your first service module with `Ecto` (ab)used as data casting and validation library!

## Cleaning it up

The solution above is pretty fine, but it does have a lot of boilerplate code we can DRY-up. What I often do, is to create a `service.ex` file with simple macro, and reduce my services code to schema declaration, validations and business logic that gets performed when they pass. Ideally, I end up with the following neat and short services:

```
defmodule App.ContactForm do
  use App.Service, %{
      full_name: :string,
      email: :string,
      message: :string,
      accept_tos: :boolean
    }

  def submit(params) do
    case process_params(params) do
      {:ok, data} ->
        IO.inspect("Sending email from #{data.full_name}:")
        IO.inspect(data.message)
        :ok
      error ->
        error
    end
  end

  defp validate(changeset) do
    changeset
    |> validate_required([:full_name, :message])
    |> validate_acceptance(:accept_tos)
  end
end
```

That’s nice and short. Ideal API for me, would also make the `new/0` and `validate/1` functions optional. So in case I don’t need to have any validations on my forms, I would not define them at all. We can do it with Elixir’s `defoverridable` macro. Let’s write some not so fancy metaprogramming to extract the code we’ll share among services into our `service.ex` file:

```
defmodule App.Service do
  defmacro __using__(schema) do
    quote do
      import Ecto.Changeset

      def new, do: cast(%{})
      defp validate(changeset), do: changeset

      defoverridable [new: 0, validate: 1]

      defp process_params(params) do
        params
        |> cast()
        |> validate()
        |> apply_action(:insert)
      end 

      defp cast(params) do
        data = %{} 
        types = Enum.into(unquote(schema), %{})
        empty_map = Map.keys(types) |> Enum.reduce(%{}, fn key, acc -> Map.put(acc, key, nil) end)

        changeset = {data, types} |> Ecto.Changeset.cast(params,  Map.keys(types))

        put_in(changeset.changes, Map.merge(empty_map, changeset.changes))
      end 
    end 
  end 
end
```

…and we’re done! That’s how I use Ecto to back up my services, tableless forms, or forms that manipulate data across multiple tables or records.

Do you have some other ideas or better solutions? Leave a comment, I’d love to hear from you!
