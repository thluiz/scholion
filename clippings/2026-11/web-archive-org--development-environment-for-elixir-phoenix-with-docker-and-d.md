---
url: "https://web.archive.org/web/20200818140203id_/https://dev.to/hlappa/development-environment-for-elixir-phoenix-with-docker-and-docker-compose-2g17"
captured_at: "2026-11-16T15:43:31+00:00"
title: "Development environment for Elixir + Phoenix with Docker and Docker-compose"
domain: "web-archive-org"
---

I've been following Elixir, Phoenix and Docker for a two years now. I Started with small demos and experiments. Back then configuring Elixir and Phoenix to Docker environment was a pain, especially the configuration for runtime. There was at least a 20 different ways and tutorials how to configure Elixir and Phoenix for Docker and Docker-compose. Each of those tutorials worked out, but some were outdated or too complicated.

Today I had some spare time to deep dive again into this problem and configure proper hot-reloaded local development environment for Elixir + Phoenix using Docker and Docker-compose.

## [](#prerequisite)Prerequisite

In this article I'm not going to go through installing these tools, but below is a list of what is needed.

*   Docker
*   Docker-compose
*   Elixir (I used latest 1.10.4)
*   Phoenix framework (I used latest 1.5.4)
*   Hex

## [](#creating-phoenix-application)Creating Phoenix application

Once you have everything installed you're ready to generate new Phoenix project by executing:  

```
$ mix phx.new "your application name"
```

There are a few flags to pass along this command, but this command covers everything we need (Ecto, webpack etc). More on [phx.new documentation](https://hexdocs.pm/phoenix/Mix.Tasks.Phx.New.html#module-options).

## [](#deps-and-nodemodules)Deps and node\_modules

During the project bootstrap `mix` will execute command `deps.get & deps.compile` to fetch and compile needed dependencies and run `npm install` to fetch needed Javascript packages.

This is problematic since we want to run our program/web-server in container, not on bare host system. In order to run Elixir application it needs to be compiled in same system architecture where the release binary will be run on. For now, it's safe to remove `deps` and `node_modules` folders from the project structure (node\_modules-folder lives inside assets-folder).

Now lets dive into setting up our Docker configuration for our newly created application!

## [](#docker-and-dockercompose)Docker and Docker-compose

In this section we will be creating following files:

*   Dockerfile
*   docker-compose.yml
*   .env

`Dockerfile` is used to build Docker image which holds our application, dependencies and needed tools.

`docker-compose.yml` - yaml-markup file to define our services, volumes etc.

`.env` - Holds our environment variables for the application.

## [](#dockerfile)Dockerfile

Below you can see the contents of our Dockerfile.  

```
FROM bitwalker/alpine-elixir-phoenix:latest

WORKDIR /app

COPY mix.exs .
COPY mix.lock .

RUN mkdir assets

COPY assets/package.json assets
COPY assets/package-lock.json assets

CMD mix deps.get && cd assets && npm install && cd .. && mix phx.server
```

On the first line we define our base image which is used to build our image on to. As you can see, we're using `bitwalker/alpine-elixir-phoenix` which holds Elixir, Phoenix and other needed tools for the application.

On the next few lines we're defining our working directory, copying files and making one new directory.

The `CMD` is the line which is executed when we fire up our container. There is few commands for fetching deps, installing npm packages and firing up our server. Those commands could be in `.sh`\-script file, but I left it there to clarify what is being executed and in which order.

## [](#dockercomposeyml)docker-compose.yml

```
version: '3.6'
services:
  db:
    environment:
      PGDATA: /var/lib/postgresql/data/pgdata
      POSTGRES_PASSWORD: postgres
      POSTGRES_USER: postgres
      POSTGRES_HOST_AUTH_METHOD: trust
    image: 'postgres:11-alpine'
    restart: always
    volumes:
      - 'pgdata:/var/lib/postgresql/data'
  web:
    build: .
    depends_on:
      - db
    environment:
      MIX_ENV: dev
    env_file:
      - .env
    ports:
      - '4000:4000'
    volumes:
      - .:/app
volumes:
  pgdata:
```

Here we defined our docker-compose script version, needed services and volumes to be created.

As you can see, there is two services(containers) being created `db` and `web`. `db` is our database container which is used by `web`\-container. On the image-property we define our image, which is `postgres:11-alpine`. You could use newer version, for example PostgreSQL 12. It really depends what version you are going to use in production environment. I recommend to use same versions across the environments to minimize infrastructure related problems.

More explanation of the properties can be found from [docker-compose documentation](https://docs.docker.com/compose/compose-file/)

## [](#env).env

```
DATABASE_URL=postgres://postgres:postgres@db:5432/myapp_dev
```

For now there is only our environment variable for database URL. Later on when your application grows you will be storing your application environment variables in this file.

## [](#fire-it-up)Fire it up

First we need to build our Docker image:  

```
$ docker-compose build
```

If you did everything correctly, the image should be built relatively quick. Now we have our image ready, but first we need to configure our application to use our environment variable for database URL, so lets do that.

Navigate to `config/dev.exs` and open it up. Change the content from this:  

```
use Mix.Config

# Configure your database
config :myapp, Myapp.Repo,
  username: "postgres",
  password: "postgres",
  database: "myapp_dev",
  hostname: "localhost",
  show_sensitive_data_on_connection_error: true,
  pool_size: 10

# For development, we disable any cache and enable
# debugging and code reloading.
#
# The watchers configuration can be used to run external
# watchers to your application. For example, we use it
# with webpack to recompile .js and .css sources.
config :myapp, MyappWeb.Endpoint,
  http: [port: 4000],
  debug_errors: true,
  code_reloader: true,
  check_origin: false,
  watchers: [
    node: [
      "node_modules/webpack/bin/webpack.js",
      "--mode",
      "development",
      "--watch-stdin",
      cd: Path.expand("../assets", __DIR__)
    ]
  ]

# ## SSL Support
#
# In order to use HTTPS in development, a self-signed
# certificate can be generated by running the following
# Mix task:
#
#     mix phx.gen.cert
#
# Note that this task requires Erlang/OTP 20 or later.
# Run `mix help phx.gen.cert` for more information.
#
# The `http:` config above can be replaced with:
#
#     https: [
#       port: 4001,
#       cipher_suite: :strong,
#       keyfile: "priv/cert/selfsigned_key.pem",
#       certfile: "priv/cert/selfsigned.pem"
#     ],
#
# If desired, both `http:` and `https:` keys can be
# configured to run both http and https servers on
# different ports.

# Watch static and templates for browser reloading.
config :myapp, MyappWeb.Endpoint,
  live_reload: [
    patterns: [
      ~r"priv/static/.*(js|css|png|jpeg|jpg|gif|svg)$",
      ~r"priv/gettext/.*(po)$",
      ~r"lib/myapp_web/(live|views)/.*(ex)$",
      ~r"lib/myapp_web/templates/.*(eex)$"
    ]
  ]

# Do not include metadata nor timestamps in development logs
config :logger, :console, format: "[$level] $message\n"

# Set a higher stacktrace during development. Avoid configuring such
# in production as building large stacktraces may be expensive.
config :phoenix, :stacktrace_depth, 20

# Initialize plugs at runtime for faster development compilation
config :phoenix, :plug_init_mode, :runtime
```

To this:  

```
use Mix.Config

database_url = System.get_env("DATABASE_URL")

# Configure your database
config :myapp, Myapp.Repo,
  url: database_url,
  show_sensitive_data_on_connection_error: true,
  pool_size: 10

# For development, we disable any cache and enable
# debugging and code reloading.
#
# The watchers configuration can be used to run external
# watchers to your application. For example, we use it
# with webpack to recompile .js and .css sources.
config :myapp, MyappWeb.Endpoint,
  http: [port: 4000],
  debug_errors: true,
  code_reloader: true,
  check_origin: false,
  watchers: [
    node: [
      "node_modules/webpack/bin/webpack.js",
      "--mode",
      "development",
      "--watch-stdin",
      cd: Path.expand("../assets", __DIR__)
    ]
  ]

# Watch static and templates for browser reloading.
config :myapp, MyappWeb.Endpoint,
  live_reload: [
    patterns: [
      ~r"priv/static/.*(js|css|png|jpeg|jpg|gif|svg)$",
      ~r"priv/gettext/.*(po)$",
      ~r"lib/myapp_web/(live|views)/.*(ex)$",
      ~r"lib/myapp_web/templates/.*(eex)$"
    ]
  ]

# Do not include metadata nor timestamps in development logs
config :logger, :console, format: "[$level] $message\n"

# Set a higher stacktrace during development. Avoid configuring such
# in production as building large stacktraces may be expensive.
config :phoenix, :stacktrace_depth, 20

# Initialize plugs at runtime for faster development compilation
config :phoenix, :plug_init_mode, :runtime

```

As you can see, we deleted SSL section since we're not going to use SSL secured connection in our local development. The actual change you should be looking at is on top of the file. We are fetching our database URL for database connection from the container environment.

Now we should be ready for our application start-up:  

```
$ docker-compose up
```

It checks the deps, installs npm packages and compiles deps & source files, but wait a second...  

```
[error] Postgrex.Protocol (#PID<0.3932.0>) failed to connect: ** (Postgrex.Error) FATAL 3D000 (invalid_catalog_name) database "myapp_dev" does not exist
```

We don't have a database where to connect! Lets fix that:  

```
$ docker-compose run web mix ecto.create
```

After running this you should be greeted with a pleasant one line message which tells you that the database for YourApp.Repo has been created! Wonderful!

Note that you can execute any mix commands inside the container since it has mix tooling available. You can run migrations, seeds, destroy the database and set it up again for a clean start etc.

Now execute:  

```
$ docker-compose up
```

The application should start up with database connection and be ready for development! Navigate to `localhost:4000` and now if you make changes to the source files, the changes will be updated to the server, so no need for manual restart of the containers!

## [](#conclusion)Conclusion

This is a pretty simplistic setup with minimal amount of files to support/configure.

I'll do a follow-up post where we will deploy Elixir application to Azure. It will include configuring the application for production environment, Terraform infrastructure and little bit of CI magic.

Thanks for reading, hope you liked it! 🙂
