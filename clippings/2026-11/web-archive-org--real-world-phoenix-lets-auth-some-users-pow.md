---
url: "https://web.archive.org/web/20190721084510id_/https://www.theguild.nl/real-world-phoenix-lets-auth-some-users/"
captured_at: "2026-11-16T08:13:48+00:00"
title: "Real World Phoenix |> Let's auth some users |> Pow!"
domain: "web-archive-org"
---

![Tjaco oostdijk](https://images.ctfassets.net/8v4g74v8oew0/4Am1jXaiUwOCgCkSgGUwe/d5e1b277de5afed7f8c259526a8ffeae/tjaco_oostdijk.png)

Tjaco Oostdijk – 7 June 2019  
861 words in about 4 minutes

If you have lived in the Rails world for a while, you have been spoiled by user authentication libraries being present in the ecosystem. One popular choice is often Devise, which makes user authentication a breeze. In Elixir / Phoenix land there are already some options available but I recently came across a new ‘kid on the block’ that aims to make user authentication for developers a breeze, while still keeping the Elixir mindset of being explicit and modular into account.

This library is called [Pow](https://github.com/danschultzer/pow). And as Dan Schultzer mentions in his introductory post on the Elixir Forum, he basically was missing such a library. I think we need more Dan’s in the Elixir world. I have also noticed how quick and thoughtful he responds to bug and feature requests, so I hope we can all learn from his enthousiasm.

## Pow

Here is a snippet of his first introduction to his library:

_None of the current solutions worked well for me, so I went ahead and built a user management system from scratch. This project took far longer than I initially thought, and I would love to get some help to iron out everything. So please try it out and let me know what you think!_

## Real World Phoenix

In this series of Real World Phoenix posts I’d like to explore some of the ways we can use Phoenix to build a more straightforward app without necesarily making use of the OTP framework explicitly (we are ofcourse using the OTP framework implicitly, because Phoenix utilises that ;) ). In our journey we’ll discover what libraries we can use and also where we can just do without any library and be explicit, the Elixir way! Aside from my job as a programmer I also teach drums and need to manage student information, lesson notes and a whole lot of other stuff related to teaching. So why not build an app to manage student information and some tools to make life as a teacher a bit more manageable.

## User Management / Authentication

In this first exploration I want to start the App by getting user authentication setup. Almost all apps eventually will need some sort of authentication. Of course it’ll become custom at some point, but at the start it is mostly the same stuff for every app. Let’s see how Pow can get us up and running as quickly as possible.

## Starter Template

As a start I have used my Live View Dashboard starter app, just because that is convenient and that already has some defaults setup. I have added ecto and postgres to that. For more information on that template, check my repo here: [gen\_template\_phx\_live\_view](https://github.com/drumusician/gen_template_phx_live_view)

Ok, once we have that up-and-running let’s crack open the Pow readme and see how far that get’s us.

So, the first thing we’ll need to do is add the Pow dependency to our mix.exs file:

```
1
2
3
4
5
def deps do
# ...
{:pow, "~> 1.0.7"}
  # ...
end
```

Then run `mix deps.get` to install the dependency.

Dan has clearly thought of his end users as he also has a guide for when you have an umbrella app setup. Nice one Dan! And he also put in a little mix task to get us up and running quickly.

```
1
mix pow.install
```

After running the command above, we get a whole lot of information of what we should do next. There are basically two files that Pow creates for us. A file in `LIB_PATH/users/user.ex` and a migration in `PRIV_PATH/repo/migrations/TIMESTAMP_create_user.ex`. I already know that I am going to prefer a bounded context of Accounts, so I’ll change the `users/user.ex` to `accounts/user.ex`. This is possible, because pow provides a config option so you can actually change what user will be used for authentication.

You provide that configuration option in `config/config.exs`:

```
1
2
3
4
# config/config.exs
config :student_manager, :pow
  user: Studentmanager.Accounts.User,
  repo: StudentManager.Repo
```

Then we need to setup a session Plug in our endpoint after the already existing `plug Plug.Session...`:

```
1
2
3
4
5
6
7
8
9
# WEB_PATH/endpoint.exs
# ...
  plug Plug.Session,
    store: :cookie,
    key: "_my_app_key",
    signing_salt: "secret"

  plug Pow.Plug.Session, otp_app: :student_manager
# ...
```

And Pow also provides a function that expands to some basic routes for user registration and authentication which you can add to your routes file:

```
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
# ... pipelines

  pipeline :protected do
    plug Pow.Plug.RequireAuthenticated,
      error_handler: Pow.Phoenix.PlugErrorHandler
  end

  scope "/" do
    pipe_through :browser

    pow_routes() # <= magic pow routes!
  end

  scope "/", MyAppWeb do
    pipe_through [:browser, :protected]

    # Add your protected routes here
  end

  # ... routes
```

Now once you run `mix ecto.setup` to get your database up and running, you can start up Phoenix and create a new user by visiting the user registration route: `http://localhost:4000/registration/new`

## Conclusion

Now that was pretty straightforward to get user registration and session based authentication up and running. Of course Pow provides all kinds of customisation options and you can also generate the templates being used into your own project so you are able to customise fully. We are gonna leave this as is for now and in the next post we’ll expand our User model and implement user Roles so that a teacher can manage his/her students.

Hope you enjoyed this post, until next time!
