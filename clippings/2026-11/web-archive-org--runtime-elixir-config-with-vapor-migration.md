---
url: "https://web.archive.org/web/20200514101634id_/https://blog.appsignal.com/2020/04/28/configuring-your-elixir-application-at-runtime-with-vapor.html"
captured_at: "2026-11-18T11:39:41+00:00"
title: "Configuring your Elixir Application at Runtime with Vapor"
domain: "web-archive-org"
---

Configuration has long been a hot topic in the Elixir community, and luckily, in the recent months, there has been a great deal of thoughtful work put into making this problem an easier one to solve. Today, we’re going to show you how to migrate from an Elixir application that has been configured with the widely used `config/*.exs` files at compile-time, to an application that instead uses environment variables for configuration and is configured at runtime.

But, before we get into the details of some of the recent and upcoming changes happening in this area, let’s just go over some of the historical problems that came from the way Elixir applications were configured in the past.

## What’s Wrong with `config.exs`?

Well, for some applications, nothing. But there is an increasing number of teams that have encountered issues around the configuration of their applications as they become larger, and especially, as their deployment strategy changes. As someone who has spent the majority of the last 4 years as a freelancer working on several different Elixir applications, I can say that I’ve personally seen issues on every project I’ve worked on in that time, except for one (and that one was a greenfield project that was designed to be configured in the way we’ll be discussing today). Some of the most common configuration related issues that the community has been seeing are:

### Confusing Runtime vs. Compile-time Configuration

If you are compiling and deploying [OTP releases](https://elixir-lang.org/getting-started/mix-otp/config-and-releases.html#releases) for your application, I have a suspicion that you’ve run into at least one case where you were confused by an environment variable shown as “missing” in production even though you were **sure** it had been set. The code around this might have looked something like this (in `config/config.exs`):

1
2

config :my\_app, MyApp.Repo,
  url: System.get\_env("DATABASE\_URL")

You might have found that it worked just fine locally and in your CI environment, but for some reason, not in production. Very confusing! This is because the `System.get_env/1` there is evaluated at _compile time_ and not at runtime! If the correct environment variable isn’t set for your production database url in whichever environment your release is compiled, then the configuration for your application will be incorrect.

What we really want is for this environment variable to be evaluated at runtime, instead of at compile-time, in whichever environment it is running.

### Compiled Releases Cannot Be Used in Different Environments

As noted above, the `System.get_env/1` call is evaluated at compile time. This means that if we have a staging environment that our application is deployed to for testing before deployment to production, we’ll need to compile a separate OTP release for production. It is far safer to be able to deploy the same build artifact that’s been tested on staging, directly to production as this limits your ability to have differences between these two environments and reduces the likelihood of bugs stemming from build or configuration issues.

### Configuring Multiple Instances of an (OTP) Application

If your application depends on an OTP application that uses an application configuration for its behavior, this essentially limits your ability to use it to only a single version. For example, imagine we have an API client and we need to configure an API key for that client. That library might get that API key by calling `Application.get_env(:api_client, :api_key)`. Now, imagine that you need to handle more than one API key? This would be basically impossible, since setting the “correct” API key before calling some function in the library is too dangerous to rely on in a highly parallel runtime like the BEAM!

### Difficulties Using Non `config.exs` Files for Configuration

There are different types of ways to configure an application—especially relating to configuration and management of sensitive or secret values—and in the past, using something like HashiCorp Vault, AWS Secrets Manager or some other configuration management tool was rather difficult and unintuitive to use. There was a lot of work involved to make this stuff function at all, but it relied on disparate, loosely-enforced conventions like the `REPLACE_OS_VARS` setting in `distillery` or the `{:system, "ENV_VAR"}` solution as a signal to libraries that “this environment variable should be evaluated at runtime instead of compile time.”

## Recent and Upcoming Changes to Application Configuration

As I mentioned above, the problem of configuration is one that has been worked on quite frequently over the last year or so. We’ve seen the inclusion of `mix release` and the `Config`, `Config.Provider` and `Config.Reader` modules in Elixir 1.9, and in Elixir 1.10 we saw the addition of the `Application.compile_env/3` function that makes it crystal clear that any configuration retrieved from there was set at compile-time and cannot be changed. These have all been great changes!

Coming, sometime in the future, will be the deprecation of using `Application.get_env/3` at compile-time altogether, which will make it even easier to avoid incorrectly using runtime configuration by accident. But, I think most importantly, we’ve also seen the release of several libraries that have made the distinction between runtime and compile-time configuration clearer, including the tool we’ll look at today—`vapor`.

We can see that at the root of many of these problems is the need to cleanly and clearly separate runtime from compile-time configuration. In addition to this, there is some work for libraries and applications to do to change some of their APIs so that they rely less on application configuration and more on arguments to functions when configuring an OTP application. A great example of the kind of change that I’m talking about here is the [`init/2` callbacks](https://hexdocs.pm/ecto/Ecto.Repo.html#c:init/2) that have been added to Ecto and Phoenix.Endpoint. These make it trivially easy to configure these parts of your application almost entirely at runtime!

## Getting Started With `vapor`

And so today, we’re going to look at how one might get started with `vapor` and how we can make changes over time to migrate to configuring an application in a safe, consistent, and reliable way that will last well into the future. The first step, of course, is adding `vapor` as a dependency in `mix.exs` by adding `{:vapor, "~> 0.8.0"}` to your `deps()` function. `vapor` has a lot of functionality, and what I’m going to show today is just _one_ way of using it, but I find it to be a nice, easy migration, and so it’s what I like to recommend.

So, now that we’ve added `vapor` as a dependency, we need to start using it! We add `vapor` to our `start/2` function in our application like so:

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

defmodule VaporExample.Application do
  use Application

  def start(\_type, \_args) do
    Vapor.load!(\[%Vapor.Provider.Dotenv{}\])

    children \= \[
       VaporExampleWeb.Endpoint,
       VaporExample.Repo
    \]

    opts \= \[strategy: :one\_for\_one, name: VaporExample.Supervisor\]
    Supervisor.start\_link(children, opts)
  end
end

`vapor` has a great feature that allows it to read from a `.env` or `.env.test` file, and from that, it populates the system environment for you at runtime. It does nothing if those files don’t exist, so it’s totally safe to start with that for now. But, we don’t want to stop there—we’re going to make one more small change before we’re done with our first step.

In `config/config.exs` let’s imagine that we had the following configuration for our `VaporExample.Endpoint` module (which is our Phoenix Endpoint) to set the port for our Endpoint to `4000`:

1
2

config :vapor\_example, VaporExample.Endpoint,
  http: \[port: 4000\]

This is currently configured at compile-time, but there’s absolutely no reason it can’t be done at runtime instead. So let’s do that! First, we’ll delete that `http: [port: 4000]` line, then we’ll add `PORT=4000` to the `.env` file I spoke about earlier to automatically set that environment variable in our application, and then we’ll add a new function to `VaporExample.Application` called `load_system_env/0`. This function’s job will be taking environment variables and putting them in application configuration, and this is done once, when we start the application.

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
21
22
23
24
25
26

defmodule VaporExample.Application do
  use Application

  def start(\_type, \_args) do
    Vapor.load!(\[%Vapor.Provider.Dotenv{}\])
    load\_system\_env()

    children \= \[
       VaporExampleWeb.Endpoint,
       VaporExample.Repo
    \]

    opts \= \[strategy: :one\_for\_one, name: VaporExample.Supervisor\]
    Supervisor.start\_link(children, opts)
  end

  defp load\_system\_env() do
    port \=
      case System.get\_env("PORT") do
        nil \-> raise("Environment variable PORT must be set")
        value \-> String.to\_integer(value)
      end

    Application.put\_env(:vapor\_example, VaporExample.Endpoint, http: \[port: port\])
  end
end

Now, whether you’re starting your application with `mix` or as a `release`, in `dev`, `test` or `prod`, the behavior of configuring the port for your Endpoint to listen to will _always_ be the same! The above implementation also ensures that our application doesn’t start if it’s not configured correctly, which keeps us from running a partially (but maybe subtly) broken application. This is a huge benefit, and really shows us that the rule for configuring an Elixir application should really be “if it **can** be set at runtime, it **should** be set at runtime.”

But wait, there’s more! We see that we’re kind of doing a lot just to turn one environment variable into the application environment in our `load_system_env/0` function. Luckily, `vapor` can make that easier for us! Besides being able to populate our system environment from a `.env` file, it can also declare bindings to that system environment to handle much of the work we did in `load_system_env/0` for us! So, we can change that function to look like this:

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

defmodule VaporExample.Application do
  use Application

  \# ...

  defp load\_system\_env() do
    providers \= %Vapor.Provider.Env{bindings: \[
      {:port, "PORT", map: &String.to\_integer/1}
    \]}

    config \= Vapor.Provider.load!(providers)

    Application.put\_env(:vapor\_example, VaporExample.Endpoint, http: \[port: config.port\])
  end
end

This will do the same thing as our previous implementation—converting the string `"4000"` to the integer `4000` and returning an error if the variable isn’t set, so that we can raise an exception—but does so with a nice, consistent API.

Now, with these basics in place, you can start moving over compile-time configuration to runtime easily! After everything that can be set at runtime is set at runtime, you could then move on to trying to reduce the use of the application environment altogether and use things like the `init/2` callback in your `Endpoint` and `Repo`, and find other places where a dependency on the application environment can be replaced by passing arguments to functions instead.

Moving over to this style of configuration will ensure that your Elixir applications are configured correctly well into the future, and should hopefully also make for a more consistent and clear configuration experience for your whole team.

**P.S. If you’d like to read Elixir Alchemy posts as soon as they get off the press, [subscribe to our Elixir Alchemy newsletter and never miss a single post](https://blog.appsignal.com/category/elixir-alchemy.html#elixir-alchemy)!**

_Guest author Devon is a senior Elixir engineer currently working at Sketch. He spent 8 years as a freelance developer, working primarily with Elixir & Erlang since 2015. He has helped numerous companies benefit from the power of the BEAM. He is also a writer, international conference speaker, and committed supporter of open-source software as a maintainer of Benchee and the Elixir track on [Exercism](https://exercism.io/), as well as a frequent contributor to Elixir._
