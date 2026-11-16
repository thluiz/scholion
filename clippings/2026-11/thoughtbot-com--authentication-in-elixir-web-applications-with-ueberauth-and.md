---
url: "https://thoughtbot.com/blog/authentication-in-elixir-web-applications-with-guardian-part-1"
captured_at: "2026-11-16T03:14:07+00:00"
title: "Authentication in Elixir Web Applications with Ueberauth and Guardian: Part 1"
domain: "thoughtbot-com"
---

The majority of web applications require some kind of user or account authentication at some point in their life cycle. One popular option for authentication in an Elixir or Phoenix web application is to use the [Guardian](https://hexdocs.pm/guardian/introduction-overview.html) package together with [Ueberauth](https://hexdocs.pm/ueberauth/api-reference.html). In order to learn about this authentication option, this series of posts will build a basic Phoenix application with at least the following features:

A user can:

*   register for an account using their email and password or by using their Google account
*   log in to their account using their email and password or by using their Google account
*   log out of their account
*   access protected resources only after logging in

In order to follow along with these posts, it’s best if you have basic familiarity with Elixir, Phoenix, and with running commands on the command line. If these are unfamiliar to you, the [Elixir language getting started guide](https://elixir-lang.org/getting-started/introduction.html), the [Phoenix guides](https://hexdocs.pm/phoenix/overview.html), and [Learn Enough Command Line to Be Dangerous](https://www.learnenough.com/command-line-tutorial/basics) are good places to begin.

## [Setting up a basic Phoenix application with authentication pages](#setting-up-a-basic-phoenix-application-with-authentication-pages)

This first post will cover creating a basic Phoenix application called Yauth—an amalgamation of “You Authenticate”—and creating the pages needed for authentication. If you’ve not done so already, you will need to [install Phoenix](https://hexdocs.pm/phoenix/installation.html) by following the instructions on the Phoenix web site. This tutorial will be using Phoenix 1.4.14 but any version >= 1.4 should be fine to follow along.

Once you have Phoenix installed, run the following command to generate the Phoenix application.

```
mix phx.new yauth
```

When prompted, accept the request to install dependencies and then follow the instructions to change into the application directory, establish the database, and confirm that the application runs.

## [Test driving the application from the outside in](#test-driving-the-application-from-the-outside-in)

While these posts will not follow a strict test-driven development approach, a great place for us to start is by writing a feature test from the perspective of our users. Given we are building a web application, we should begin by writing tests that use a browser to drive the application in the same way our end user will. To accomplish those browser-based tests, these posts will use [Wallaby](https://hexdocs.pm/wallaby/readme.html), a popular Elixir acceptance testing package.

### [Setting up Wallaby for automated browser tests](#setting-up-wallaby-for-automated-browser-tests)

First, let’s add Wallaby to our list of dependencies.

```
# mix.exs
defmodule Yauth.MixProject do
  # ...
  defp deps do
    [
      # ...
      {:wallaby, "~> 0.23.0", [runtime: false, only: :test]},
    ]
  end
  # ...
end
```

Now we can tell `mix` to get those dependencies:

```
mix deps.get
```

Wallaby uses a browser driver to interact with a browser. It uses PhantomJS by default but, as PhantomJS has been discontinued, this tutorial will use the headless `chromedriver` instead. You will need to install `chromedriver` by [following the instructions on the chromedriver website](https://chromedriver.chromium.org/getting-started).

We will also need to make a few additions to our project to work with Wallaby.

First, we need ensure that Wallaby has started when our tests are started. Add the following to our test helper:

```
# test/test_helper.exs
# ...
{:ok, _} = Application.ensure_all_started(:wallaby)
Application.put_env(:wallaby, :base_url, YauthWeb.Endpoint.url)
```

Next we need to configure our application to ensure that the Phoenix `Endpoint` is running as a server during tests, to indicate which browser driver to use, and to set the database to use the sandbox mode to allow for concurrent testing.

```
# config/test.exs
# ...
config :yauth, YauthWeb.Endpoint,
  server: true

config :yauth, :sql_sandbox, true

config :wallaby,
  driver: Wallaby.Experimental.Chrome
```

We also need to configure the `Endpoint` to use the SQL sandbox if that option is set.

```
# lib/yauth_web/endpoint.ex
defmodule YauthWeb.Endpoint do
  use Phoenix.Endpoint, otp_app: :yauth

  if Application.get_env(:yauth, :sql_sandbox),
    do: plug(Phoenix.Ecto.SQL.Sandbox)
  # ...
end
```

Finally, to make testing with Wallaby easier, let’s create a `FeatureCase` that can be used by our browser-based tests.

```
# test/support/feature_case.ex
defmodule YauthWeb.FeatureCase do
  @moduledoc """
  This module defines the test case to be used by browser-based tests.
  """

  use ExUnit.CaseTemplate

  using do
    quote do
      use Wallaby.DSL
    end
  end

  setup tags do
    :ok = Ecto.Adapters.SQL.Sandbox.checkout(Yauth.Repo)

    unless tags[:async] do
      Ecto.Adapters.SQL.Sandbox.mode(Yauth.Repo, {:shared, self()})
    end

    metadata = Phoenix.Ecto.SQL.Sandbox.metadata_for(Yauth.Repo, self())
    {:ok, session} = Wallaby.start_session(metadata: metadata)
    {:ok, session: session}
  end
end
```

This case does a few things for us. By `use`ing the `Wallaby.DSL`, it imports all of the functions of `Wallaby.Browser` and aliases `Wallaby.{Browser, Element, Query}`, making those modules available to our tests under those aliases. It also establishes a Wallaby session and makes it available to each test case.

With Wallaby in place, we can now write our first feature test. This test will confirm that a user can reach the first two pages of our application—a registration page and a login page—by visiting those pages and asserting that the content is as expected.

For the registration page, we will expect to see a form with fields for an email address, a password, a password confirmation, and links to the social logins we (will eventually) support. Similarly, the login page should contain a form with fields for email and password as well as links for social login.

```
# test/yauth_web/features/authentication_pages_test.exs
defmodule YauthWeb.Features.AuthenticationPagesTest do
  use YauthWeb.FeatureCase, async: true
  import Query, only: [fillable_field: 1, link: 1]

  @email_field fillable_field("account[email]")
  @password_field fillable_field("account[password]")
  @password_confirmation_field fillable_field("account[password_confirmation]")

  test "Visiting the registration page", %{session: session} do
    session = visit(session, "/register")

    assert_text(session, "Register")
    assert_has(session, @email_field)
    assert_has(session, @password_field)
    assert_has(session, @password_confirmation_field)
    assert_has(session, link("Google"))
    assert_has(session, link("Twitter"))
  end

  test "Visiting the login page", %{session: session} do
    session = visit(session, "/login")

    assert_text(session, "Log In")
    assert_has(session, @email_field)
    assert_has(session, @password_field)
    assert_has(session, link("Google"))
    assert_has(session, link("Twitter"))
  end
end
```

At this point, we can run our tests with `mix test` and see our first failing tests. Once these tests are passing, we can be confident our authentication pages are in place.

## [Creating authentication pages](#creating-authentication-pages)

Our tests above are expecting our application to have a “/register” and a “/login” route. To make those available, make the following changes to our `Router`.

```
# lib/yauth_web/router.ex
defmodule YauthWeb.Router do
  # ...

  scope "/", YauthWeb do
    pipe_through :browser

    get "/", PageController, :index
    get "/register", RegistrationController, :new
    get "/login", SessionController, :new
  end
end
```

Here we configure our `Router` to route GET requests at “/register” to the `new/2` function of the `RegistrationController` and GET requests at “/login” to the `new/2` function of the `SessionController`. Running our tests with `mix test` will highlight the need to create these controller modules.

```
# lib/yauth_web/controllers/registration_controller.ex
defmodule YauthWeb.RegistrationController do
  use YauthWeb, :controller

  def new(conn, _) do
    render(conn, :new, changeset: conn, action: "/register")
  end
end

# lib/yauth_web/controllers/session_controller.ex
defmodule YauthWeb.SessionController do
  use YauthWeb, :controller

  def new(conn, _params) do
    render(conn, :new, changeset: conn, action: "/login")
  end
end
```

For now, our intention is simply to display these pages to the user without providing any actual functionality. We are passing a changeset and an action as assigns even though we don’t have a schema or actual changeset at this point. Fortunately, the `form_for` function accepts either a `%Plug.Conn{}` or a changeset so we’ll take advantage of that here so we don’t have to change our templates in the future. We are also just hard coding the action paths for now.

Both of these controllers simply render the `:new` template. In order for that rendering to happen, however, Phoenix needs a view module (a module that organizes all of the functions of a controller’s view) and an HTML template. We can create the views for these controllers with the following:

```
# lib/yauth_web/views/registration_view.ex
defmodule YauthWeb.RegistrationView do
  use YauthWeb, :view
end

# lib/yauth_web/views/session_view.ex
defmodule YauthWeb.SessionView do
  use YauthWeb, :view
end
```

Next, we will need the HTML templates for these views. The form will use the `@changeset` (really the `%Plug.Conn{}` at this point) and the `@action` provided in the assigns. It will also use the `:as` keyword option to identify the data in the form as account data.

```
# lib/yauth_web/templates/registration/new.html.eex
<div class="row">
  <div class="column column-50 column-offset-25">
    <h1>Register</h1>
    <%= form_for @changeset, @action, [as: :account], fn f -> %>
      <%= label f, :email, "Email address" %>
      <%= email_input f, :email %>
      <%= error_tag f, :email %>

      <%= label f, :password, "Password" %>
      <%= password_input f, :password %>
      <%= error_tag f, :password %>

      <%= label f, :password_confirmation, "Password Confirmation" %>
      <%= password_input f, :password_confirmation %>
      <%= error_tag f, :password_confirmation %>

      <%= submit "Register", class: "button button-primary" %>
    <% end %>
  </div>
</div>
<div class="row">
  <div class="column column-50 column-offset-25">
    <p>
      Already have an account?
      <%= link("Log in here", to: Routes.session_path(@conn, :new)) %>
    </p>
  </div>
</div>
<div class="row">
  <div class="column column-50 column-offset-25">
    <%= render(YauthWeb.SessionView, "social_links.html", assigns) %>
  </div>
</div>
```

And the template for the login view is similar:

```
# lib/yauth_web/templates/session/new.html.eex
<div class="row">
  <div class="column column-50 column-offset-25">
    <h1>Log In</h1>
    <%= form_for @changeset, @action, [as: :account], fn f -> %>
      <%= label f, :email, "Email address" %>
      <%= email_input f, :email %>
      <%= error_tag f, :email %>

      <%= label f, :password, "Password" %>
      <%= password_input f, :password %>
      <%= error_tag f, :password %>

      <%= submit "Log In", class: "button button-primary" %>
    <% end %>
  </div>
</div>
<div class="row">
  <div class="column column-50 column-offset-25">
    <p>
      Need an account?
      <%= link "Register here", to: Routes.registration_path(@conn, :new) %>
    </p>
  </div>
</div>
<div class="row">
  <div class="column column-50 column-offset-25">
    <%= render(YauthWeb.SessionView, "social_links.html", assigns) %>
  </div>
</div>
```

And the template for the social login links:

```
<!-- lib/yauth_web/templates/session/social_links.html.eex -->
<div class="social-log-in">
  <p>Or log in with</p>
  <%= link "Google", to: "#", class: "button button-outline" %>
  <%= link "Twitter", to: "#", class: "button button-outline" %>
</div>
```

Now when we run our tests with `mix test` all of our test should pass.

## [Recap](#recap)

In this post we created a new Phoenix application called Yauth. We added routes for displaying a registration and a login form to a user. We added the controller, views, and templates to provide those forms. We also added the test infrastructure needed for browser-based testing and added a test to ensure those forms are displayed. This will lay the groundwork from which we can build our authentication features.

In [the next post](https://thoughtbot.com/blog/authentication-in-elixir-web-applications-with-guardian-part-2), we will add the functionality for actually creating an account for the user and logging them in during that creation process.
