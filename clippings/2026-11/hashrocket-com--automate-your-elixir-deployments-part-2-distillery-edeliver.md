---
url: "https://hashrocket.com/blog/posts/automate-your-elixir-deployments-part-2-distillery-edeliver"
captured_at: "2026-11-16T04:04:15+00:00"
title: "Automate Your Elixir Deployments - Part 2 - Distillery & eDeliver"
domain: "hashrocket-com"
---

[![Profile picture of Dorian Karter](https://dkj231ikyz7c1.cloudfront.net/uploads/rocketeer/profile_image/91/image_100x100_dorian-karter.jpg)](https://hashrocket.com/blog/posts/automate-your-elixir-deployments-part-2-distillery-edeliver)

In this post we will walk through the steps necessary to build an Elixir release using Distillery and deploy the release to production using eDeliver.

This post builds on a [previous post](https://hashrocket.com/blog/posts/automate-your-elixir-deployments-part-1-ansible) in which we set up a server, using Ansible, to accept build and deploy requests from eDeliver. In this post we will configure our release and deploy strategies using Distillery and eDeliver, and deploy our application to production.

You can follow along using the [companion repository on Github](https://github.com/dkarter/deploy-elixir-example).

[

## Assumptions

](#assumptions)

This post assumes you have a basic Phoenix 1.5 application without Ecto (to keep things simple). If you don't have one and want to create a new project you can do so with the following command:

```
$ mix phx.new example --live --no-ecto
```

> The `--live` flag is optional. It will add [Phoenix Live View](https://github.com/phoenixframework/phoenix_live_view) support which is not necessary for this guide, but is supported in the Nginx configuration we added in the previous post.

[

## Initial Setup

](#initial-setup)

We will start by adding the necessary dependencies. From your project's root directory, open your `mix.exs` file and add the following dependencies:

```
defp deps do
  [
    {:distillery, "~> 2.1.1"},
    {:edeliver, "~> 1.8.0"},
    # ...
  ]
end
```

Save the file and run:

```
$ mix deps.get
```

[

## Production Configuration

](#production-configuration)

Elixir comes with a `config/prod.secret.exs` file which we will use to load environment variables:

```
# In this file, we load production configuration and secrets
# from environment variables. You can also hardcode secrets,
# although such is generally not recommended and you have to
# remember to add this file to your .gitignore.
use Mix.Config

secret_key_base =
  System.get_env("SECRET_KEY_BASE") ||
    raise """
    environment variable SECRET_KEY_BASE is missing.
    You can generate one by calling: mix phx.gen.secret
    """

config :example, ExampleWeb.Endpoint,
  http: [
    port: String.to_integer(System.get_env("PORT") || "4000"),
    transport_options: [socket_opts: [:inet6]]
  ],
  secret_key_base: secret_key_base

# ## Using releases (Elixir v1.9+)
#
# If you are doing OTP releases, you need to instruct Phoenix
# to start each relevant endpoint:
#
#     config :example, ExampleWeb.Endpoint, server: true
#
# Then you can assemble a release by calling `mix release`.
# See `mix help release` for more information.
```

Make sure to add a few more keys to the endpoint configuration at `config/prod.exs`:

```
config :example, ExampleWeb.Endpoint,
  url: [host: "example.com", port: 80],
  cache_static_manifest: "priv/static/cache_manifest.json",
  server: true,
  code_reloader: false,
  check_origin: ["//example.com"]
```

Replace `example.com` with your domain.

[

## Configuring Distillery

](#configuring-distillery)

Distillery manages our releases, but before we can start using it we need to initialize a configuration file:

```
$ mix distillery.init
```

Output:

> An example config file has been placed in rel/config.exs, review it, make edits as needed/desired, and then run `mix distillery.release` to build the release

Let's take a look at `rel/config.exs` (we only care about the production environment at this time):

```
environment :prod do
  set include_erts: true
  set include_src: false
  set cookie: :"uH$COG~8[4U9~An<?Ykj0ZqarRnjvxpFelB_1bkOya~mO{lY.sL!fkQS(;kqCCDp"
  set vm_args: "rel/vm.args"
end
```

We are going to change the `:prod` configuration so that our Erlang Cookie is not committed to git. If you recall, in the previous post we created an environment variable called `ERLANG_COOKIE`, now we are going to read it from the environment variables. Replace the `:prod` configuration with:

```
environment :prod do
  prod_cookie = fn ->
    cookie = System.get_env("ERLANG_COOKIE") || :crypto.strong_rand_bytes(64)

    :sha256
    |> :crypto.hash(cookie)
    |> Base.encode16()
    |> String.to_atom()
  end

  set(include_erts: true)
  set(include_src: false)
  set(cookie: prod_cookie.())
  set(vm_args: "rel/vm.args")
end
```

[

## Configuring eDeliver

](#configuring-edeliver)

Unlike Distillery, eDeliver does not provide an automatically generated configuration template via a Mix Task, but it does provide a [template on the github README](https://github.com/edeliver/edeliver). At the the time of writing, it looks like this:

```
# .deliver/config

APP="myapp"

BUILD_HOST="my-build-server.myapp.com"
BUILD_USER="builder"
BUILD_AT="/tmp/edeliver/myapp/builds"

STAGING_HOSTS="stage.myapp.com"
STAGING_USER="web"
DELIVER_TO="/home/web"

# For *Phoenix* projects, symlink prod.secret.exs to our tmp source
pre_erlang_get_and_update_deps() {
  local _prod_secret_path="/home/builder/prod.secret.exs"
  if [ "$TARGET_MIX_ENV" = "prod" ]; then
    __sync_remote "
      ln -sfn '$_prod_secret_path' '$BUILD_AT/config/prod.secret.exs'
    "
  fi
}
```

We will take the default and modify it a bit to suit our needs. In `.deliver/config`, insert the following (feel free to delete the annotations):

```
APP="example"

# We'll be using the production machine for building the app
BUILD_HOST="example.com"
BUILD_USER="deploy"
BUILD_AT="/home/deploy/app_build"

# This is where the app will be served from
PRODUCTION_HOSTS="example.com"
PRODUCTION_USER="deploy"
DELIVER_TO="/home/deploy/app_release"

# Automatically generate version numbers for builds
# (https://github.com/edeliver/edeliver/wiki/Auto-Versioning)
AUTO_VERSION=commit-count+git-revision+branch-unless-master

# Copy the prod.secret.exs to the build directory
pre_erlang_get_and_update_deps() {
  local _prod_secret_path="/home/$BUILD_USER/app_config/prod.secret.exs"

  if [ "$TARGET_MIX_ENV" = "prod" ]; then
    __sync_remote "
      ln -sfn '$_prod_secret_path' '$BUILD_AT/config/prod.secret.exs'
    "
  fi
}

# Source environment variables and build static assets
pre_erlang_clean_compile() {
  status "Build static assets"
  __sync_remote "
    set -e
    . /home/$PRODUCTION_USER/example.env
    cd '$BUILD_AT'
    mkdir -p priv/static
    APP='$APP' MIX_ENV='$TARGET_MIX_ENV' $MIX_CMD phx.digest.clean $SILENCE
    npm install --prefix assets
    npm run deploy --prefix assets
    APP='$APP' MIX_ENV='$TARGET_MIX_ENV' $MIX_CMD phx.digest $SILENCE
  "
}

# symlink static assets to the release location after deploying a release
symlink_static(){
  status "Symlinking statics"
  __sync_remote "
    set -e
    cp -r $BUILD_AT/priv/static $DELIVER_TO/$APP/releases/$VERSION/static
    ln -sfn $DELIVER_TO/$APP/releases/$VERSION/static $DELIVER_TO
  "
}

post_extract_release_archive() {
  symlink_static
}

post_upgrade_release() {
  symlink_static
}

# Temporary workaround from https://github.com/edeliver/edeliver/issues/314#issuecomment-522151151
# start_erl.data is not being upgraded when new release is deployed
# should not be necessary once a new distillery version is released (> 2.1.1):
# https://github.com/bitwalker/distillery/issues/729
post_extract_release_archive() {
  status "Removing start_erl.data"
  __remote "
    [ -f ~/.profile ] && source ~/.profile
    set -e
    mkdir -p $DELIVER_TO/$APP/var $SILENCE
    cd $DELIVER_TO/$APP/var $SILENCE
    rm -f start_erl.data $SILENCE
  "
}
```

The insertions we made above included:

1.  Code for compiling the static assets on the server (see steps in the `pre_erlang_clean_compile` callback).
2.  Code for symlinking the compiled assets into the release directory, so that we can rollback releases and each release has a copy of its compiled assets.
3.  A workaround to address a [known issue in Distillery](https://github.com/bitwalker/distillery/issues/693) that is expected to be fixed in the next version (> 2.1.1) - you should be able to remove the `post_extract_release_archive` callback once the issue is fixed.

As always, modify the code to match your project name and domain.

[

## Building The Release

](#building-the-release)

Now that eDeliver is set up, we can build a new release! In the project's root, run:

```
$ mix edeliver build release
```

We should see an output resembling this:

```
BUILDING RELEASE OF EXAMPLE APP ON BUILD HOST

-----> Authorizing hosts
-----> Ensuring hosts are ready to accept git pushes
-----> Pushing new commits with git to: deploy@example.com
-----> Resetting remote hosts to 26b6853c000982d80466818c7a1028e392b60483
-----> Cleaning generated files from last build
-----> Updating git submodules
-----> Fetching / Updating dependencies
-----> Build static assets
-----> Compiling sources
-----> Generating release
-----> Copying release 0.1.0+1-26b6853 to local release store
-----> Copying example.tar.gz to release store

RELEASE BUILD OF EXAMPLE WAS SUCCESSFUL!
```

We will need to copy the automatically generated version number of the release (in the output above it is `0.1.0+1-26b6853`).

The release that was generated on the server will be copied locally to `.deliver/releases`, so make sure to add that to `.gitignore`:

```
$ echo '.deliver/releases' >> .gitignore
```

This is important to do, especially on public repositories, since Elixir compiles secrets into the release.

[

## Deploying The Release

](#deploying-the-release)

Using the version number from the `build release` command, run the `deploy to production` command:

```
$ mix edeliver deploy release to production --version=0.1.0+1-26b6853
```

We should see the following output:

```
DEPLOYING RELEASE OF EXAMPLE APP TO PRODUCTION HOSTS

-----> Authorizing hosts
-----> Uploading archive of release 0.1.0+1-26b6853 from local release store
-----> Extracting archive example_0.1.0+1-26b6853.tar.gz into /home/deploy/app_release
-----> Removing start_erl.data
-----> Starting deployed release

DEPLOYED RELEASE TO PRODUCTION!
```

Now to start the deployed release run:

```
$ mix edeliver restart production
```

When you visit your domain you should see your Phoenix application running!

The full code for the application and deployment scripts [can be found here](https://github.com/dkarter/deploy-elixir-example).

[

## Conclusion

](#conclusion)

Deploying Elixir to bare-metal does not have to be scary, and if you automate the process, iteration can be a lot faster and repeatable by your team.

At Hashrocket, we love Elixir, Phoenix and LiveView and have years of experience delivering robust, well-tested Elixir applications to production. [Reach out](https://hashrocket.com/contact) if you need help with your Elixir project!

Photo by Gareth Davies on Unsplash
