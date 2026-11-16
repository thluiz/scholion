---
url: "https://dev.to/vonagedev/sending-an-sms-with-phoenix-20od"
captured_at: "2026-11-16T01:09:24+00:00"
title: "Sending an SMS with Phoenix"
domain: "dev-to"
---

The [Elixir](https://elixir-lang.org/) programming language has been steadily gaining more adoption by developers, and for good reason. It is a functional language with an intuitive syntax and a supportive community around it. The most popular web framework in the Elixir ecosystem is [Phoenix](https://phoenixframework.org/). It, like Elixir, is built to be intuitive and with a low barrier to entry.

As someone who does a lot of work in Ruby, and in Rails, I have been wanting to learn Elixir and Phoenix for a while. I took the dive and started working my way through the Elixir tutorials, and this past weekend created my first simple Phoenix app with the ability to interact with the [Nexmo](https://developer.nexmo.com/) SMS API and send text messages.

Let's walk through how I built it.

## [](#starting-your-phoenix-server)Starting Your Phoenix Server

The first thing that you need is to make sure that both Elixir and Phoenix are installed on your system. You can use their guides [here](https://elixir-lang.org/install.html) and [here](https://hexdocs.pm/phoenix/installation.html) to get up and running with the installation.

Once you have the language and the framework installed, you can create a new Phoenix app by running the following command from your console:  

```
$ mix phx.new sms_app
```

Enter fullscreen mode Exit fullscreen mode

This will create the basics of your new application inside a `/sms_app` directory. For simplicity sake, I would recommend answering in the affirmative to the setup prompts when it asks you if you want to install dependencies. Phoenix uses npm to fetch and install its Node dependencies.

Go ahead and `cd` into your new app directory. Once in there, we need to create the database for our application. By default, Phoenix uses PostgreSQL and assumes that there is a `postgres/postgres` PostgreSQL superuser. You can modify the Phoenix database settings in `config/devs.exs` first, and once you are ready, you run `mix ecto.create` from your console to set up the database for your application.

If you now run `mix phx.server` and navigate to `https://localhost:4000` in your browser you will see a welcome page from Phoenix.

[![Phoenix welcome](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fskaysb9ir2mspya8t2tf.jpg)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fskaysb9ir2mspya8t2tf.jpg)

Your Phoenix server is up and running! Now let's set up our application to interact with the Nexmo SMS API and start sending text messages. Before that, though, we need to create a Nexmo account and receive our API credentials.

## [](#creating-a-nexmo-account)Creating a Nexmo Account

### [](#getting-api-credentials)Getting API Credentials

It is free to create a Nexmo account, and once you do, you are also given complimentary credit to begin playing with the Nexmo APIs immediately. Go ahead and navigate to the [sign up](https://dashboard.nexmo.com/sign-up) page on the Nexmo dashboard and submit the sign-up form.

Once you finished signing up, navigate to the [Settings](https://dashboard.nexmo.com/settings) page and fetch your API credentials.

[![Nexmo Dashboard API credentials](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fcsn64i8bvxiq2t9yqqve.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fcsn64i8bvxiq2t9yqqve.png)

### [](#buying-a-virtual-number)Buying a Virtual Number

In many countries, you can send an SMS without a valid sender phone number, but if you plan to send your text messages in the US, for example, you need to provision a Nexmo virtual number and use it as your originating phone number.

There are two ways to acquire a virtual number with Nexmo. You can use the [Nexmo CLI](https://github.com/nexmo/nexmo-cli) and execute the following commands from your console:  

```
$ nexmo number:search US --sms
14155550100
14155550101
14155550102
$ nexmo number:buy 14155550102 --confirm
Number purchased: 14155550102
```

Enter fullscreen mode Exit fullscreen mode

The numbers shown in the above are just an example output. When you run the command you will see in real time numbers available for you to purchase. You can also specify a specific country, other than the US, by replacing the two letter US country code with another two-letter country code in the first command.

The other way to acquire a number is to navigate to the [Numbers](https://dashboard.nexmo.com/buy-numbers) page in the Nexmo Dashboard and purchase a number using the web interface.

## [](#configuring-your-phoenix-app)Configuring Your Phoenix App

### [](#defining-the-routes)Defining The Routes

Open up the router for your application in `/lib/sms_app_web/router.ex` and add the following inside the `scope "/", SmsAppWeb do` block:  

```
get "/sms", SmsController, :index

post "/send", SmsController, :send

get "/update", SmsController, :update
```

Enter fullscreen mode Exit fullscreen mode

This tells our application where to direct two `GET` requests and one `POST` request. The `GET` `/sms` route is where the user will submit the SMS. The `POST` `/send` route is where the information will be submitted to. The `GET` `/update` route is where we will receive back information from the Nexmo API.

We now need to create those Controller methods.

### [](#defining-the-controller-methods)Defining The Controller Methods

Let's create a new Controller in `/lib/sms_app_web/controllers` called `sms_controller.ex` and add the following methods:  

```
defmodule SmsAppWeb.SmsController do
    use SmsAppWeb, :controller

    def index(conn, _params) do
        render(conn, "index.html", token: get_csrf_token())
    end

    def send(conn, %{"number" => number, "message" => message}) do
        url = "https://rest.nexmo.com/sms/json"
        req_body = "" 

        response = HTTPoison.post(url, req_body, [], params: %{api_key: "#{System.get_env("NEXMO_API_KEY")}", api_secret: "#{System.get_env("NEXMO_API_SECRET")}", from: "#{System.get_env("NEXMO_NUMBER")}", text: "#{message}", to: "#{number}"})
        if {:ok} do
            conn
            redirect(_conn, to: Routes.update_path(conn, :update))
        else {:error}
            Flash.put(:error, "Something went wrong.")
        end
    end

    def update(conn, _params) do
        render(conn, "update.html")
    end
end
```

Enter fullscreen mode Exit fullscreen mode

As you can see we define a method for each one of the routes we created in the router:

*   The `index/2` method renders our index page and also produces the CSRF token, that we must submit with every form in Phoenix, to prevent cross-site scripting attacks.
*   The `send/2` method is the heart of our application. We use the HTTPoison module to create a `POST` request to the Nexmo SMS API with our API credentials and the information the user submitted on the form on the index page. We then check to see if the message was successful. If it was successful, then we redirect to the `update/2` method, and if not, we share an error message with the user.
*   The `update/2` method renders the update page.

### [](#adding-httpoison-dependency)Adding HTTPoison Dependency

Open up the `mix.exs` file in the root directory of your application, and within the `defp deps do` code block add the following on a new line:  

```
[{:httpoison, "~> 1.4"}]
```

Enter fullscreen mode Exit fullscreen mode

Then, from the command line, run the following to install the new dependency:  

```
$ mix deps.get
```

Enter fullscreen mode Exit fullscreen mode

Now we need to set up our views, so let's go ahead and do that.

## [](#setting-up-the-views)Setting Up The Views

In `/lib/sms_app_web/views` add `sms_view.ex`. Add the following into it:  

```
defmodule SmsAppWeb.SmsView do
    use SmsAppWeb, :view
end
```

Enter fullscreen mode Exit fullscreen mode

Now navigate to `/lib/sms_app_web/templates` and add an `sms` folder and inside of it we are going to create the `index` and the `update` templates.  

```
# index.html.eex

<h2>Send an SMS with the Nexmo SMS API</h2>

<form action="/send" method="post">
  <input type="hidden" value="<%= @token %>" name="_csrf_token"/>
  <div class="field">
    <label for="number">
      Recipient Phone Number:
    </label>
    <br />
    <input type="text" name="number">
  </div>

  </div class="field">
    <label for="message">
      Message:
    </label>
    <br />
    <textarea name="message" placeholder="Enter message here"></textarea>
  </div>

  <div class="actions">
    <input type="submit" value="Send">
  </div>
</form>
```

Enter fullscreen mode Exit fullscreen mode

```
# update.html.eex

<div class="phx-hero">
  <h2>Your message was sent successfully.</h2>
</div>
```

Enter fullscreen mode Exit fullscreen mode

In this walk-through, we are not going to modify the default application layout, so you will still see the Phoenix logo, etc. If you wish, you can edit the `app.html.eex` in `/lib/sms_app_web/templates` to change some of that. Additionally, the CSS stylesheets for the application is in `/assets/css`, if you wish to modify that as well.

The last step we need to do to make our app functional is configure our API credentials as environment variables.

### [](#configuring-environment-variables)Configuring Environment Variables

Create a `.env` file in the root directory of your application and add the following inside of it:  

```
export NEXMO_API_KEY=""
export NEXMO_API_SECRET=""
export NEXMO_NUMBER=""
```

Enter fullscreen mode Exit fullscreen mode

Where there are blank quotation marks add the API credentials you received from the Nexmo dashboard, and the virtual phone number you purchased.

Make sure you add `/.env` to your `.gitignore` file if you are committing to GitHub to protect your credentials.

Once you are finished and the file is saved, run the following from the command line to incorporate your environment variables into your application:  

```
$ source.env
```

Enter fullscreen mode Exit fullscreen mode

![Success](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fuoxaqnbcpy92ntezsrop.gif)

That's it!

You now have a fully functioning Phoenix application that can send SMS messages with the Nexmo SMS API. You can navigate to `https://localhost:4000/sms` to begin sending messages.

If you are interested in seeing the full code for this walk-through, you can visit the [repository](https://github.com/benhayehudi/phoenix_sms_nexmo).

Thanks for joining me on this journey beginning to learn Phoenix. There is a lot more to learn and I am excited to keep on going down this road!
