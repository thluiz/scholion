---
url: "https://blog.plataformatec.com.br/2016/06/deploying-elixir-applications-with-edeliver"
captured_at: "2026-11-16T03:52:05+00:00"
title: "Deploying Elixir applications with Edeliver « Plataformatec Blog"
domain: "blog-plataformatec-com-br"
---

We’ve been talking about deploy and releases with Elixir lately, like [how to run migrations on top of a release](https://blog.plataformatec.com.br/2016/04/running-migration-in-an-exrm-release/) or [how to deal with environment variables](https://blog.plataformatec.com.br/2016/05/how-to-config-environment-variables-with-elixir-and-exrm/). Now it’s time to discover another tool that can help us release our Elixir application.

After practicing deploy and [tracing through nodes](https://blog.plataformatec.com.br/2016/04/how-to-trace-elixir-nodes-with-erlyberly/) with [Exrm](https://github.com/bitwalker/exrm), we got more comfortable knowing that there is a tool we can count on for managing production releases. Our next biggest concern was how could we make the deploy process more manageable. We couldn’t stop thinking about Capistrano, which we normally use for our Rails projects, then we found [Edeliver](https://github.com/boldpoker/edeliver). From Edeliver’s README description:

> edeliver is based on deliver and provides a bash script to build and deploy Elixir and Erlang applications and perform hot-code upgrades.

Trying the whole deploy process manually was a bit harsh with some repetitive tasks. Using Edeliver for our first `script/deploy` was awkwardly easy! In the end, the whole manual process was simplified to:

```
    #!/bin/bash -ex

    BRANCH=${1:-master};

    mix edeliver build release --branch=BRANCH --verbose
    mix edeliver deploy release to production --verbose
    mix edeliver start production --verbose
    mix edeliver migrate production up --verbose
```

You’re probably going to need to customize this script, adapting it for your needs. In this case, we’re using this script only for production deploys, but you can customize it for staging servers pretty easily. We’ll explain how environments work further along.

## How it works

As we saw before in the README quote, Edeliver makes pretty much everything with bash scripts. The Mix tasks we saw above will be executed with Elixir, but they’ll result in bash script instructions. Part of the instructions are executed in the scripts locally, which will build new instructions that will run remotely via RPC (Remote procedure call).

Let’s go deeper in some aspects of the lib.

## Environments

Edeliver is a cool option for launching and distributing releases in multiple environments. It has a concept of three environments: build, staging and production. Among these, only the build environment should get a bit more of attention.

For a release to work in a server, it must have been built in a machine with the same architecture where the release will run. That’s because Edeliver uses Exrm for building its releases. Exrm will internally use its local [NIFs](http://erlang.org/doc/tutorial/nif.html) (C functions used by Erlang) which may vary in a different architecture, thus causing, for example, an OSX release not working on Linux. You can read more about it in [this Phoenix issue](https://github.com/phoenixframework/phoenix_guides/issues/254) where people are discussing cross-compiling issues and there are some other [issues in Exrm](https://github.com/bitwalker/exrm/issues?utf8=%E2%9C%93&q=is%3Aissue+cross+compiling+) as well.

In order to use the build environment in our own development machine, it needs to use the same architecture of our staging and production servers, otherwise it won’t work.

To configure our environments, we’ll need to create a `.deliver` directory in our project and add a `config` file. Let’s see the suggested configs from Edeliver’s README for this file:

```
#!/usr/bin/env bash

APP="your-erlang-app" # name of your release

BUILD_HOST="build-system.acme.org" # host where to build the release
BUILD_USER="build" # local user at build host
BUILD_AT="/tmp/erlang/my-app/builds" # build directory on build host

STAGING_HOSTS="test1.acme.org test2.acme.org" # staging / test hosts separated by space
STAGING_USER="test" # local user at staging hosts
TEST_AT="/test/my-erlang-app" # deploy directory on staging hosts. default is DELIVER_TO

PRODUCTION_HOSTS="deploy1.acme.org deploy2.acme.org" # deploy / production hosts separated by space
PRODUCTION_USER="production" # local user at deploy hosts
DELIVER_TO="/opt/my-erlang-app" # deploy directory on production hosts
```

It’s pretty easy to configure our environments, we only need to make sure we have `ssh` permission for these servers specified. A cool thing about this whole configuration, as mentioned before, is that it’s possible to distribute the releases through several servers.

## How can I include extra tasks to my deploy process?

What Edeliver does is generic for Elixir and Erlang applications. When we’re using Phoenix, for example, we need to run some tasks before generating the release. The most important tasks are `brunch build --production` and `mix phoenix.digest` so we can have our assets working on our release.

To make these work, we’ll need to define a hook in our `.deliver/config` file:

```
pre_erlang_clean_compile() {
  status "Preparing assets with: brunch build and phoenix.digest"
  __sync_remote "
    # runs the commands on the build host
    [ -f ~/.profile ] && source ~/.profile # load profile (optional)

    # fail if any command fails (recommended)
    set -e

    # enter the build directory on the build host (required)
    cd '$BUILD_AT'

    mkdir -p priv/static # required by the phoenix.digest task

    # installing npm dependencies
    npm install

    # building brunch
    brunch build --production

    # run your custom task
    APP='$APP' MIX_ENV='$TARGET_MIX_ENV' $MIX_CMD phoenix.digest $SILENCE
  "
} 
```

This was extracted from an Edeliver doc sample, which explains all the possibilities of hooks.

## What about my environment variables?

We shared a tip on [dealing with environment variables with Exrm](https://blog.plataformatec.com.br/2016/05/how-to-config-environment-variables-with-elixir-and-exrm/) in order to avoid exporting them in our build environment and it’s still up! Although, there’s an important detail we’ll need to pay attention.

In order to make the environments replaceable we needed to set `RELX_REPLACE_OS_VARS=true` before our start command. But that’s not possible with Edeliver because the start task runs locally.

`mix edeliver start production`

Then a possible solution is to export the `RELX_REPLACE_OS_VARS` in your production environment.

## Considerations

Edeliver seems like a cool option for dealing with our releases and deploy process, I found it really easy to use. I didn’t enter in implementation details in this post, so make sure to read its [README](https://github.com/boldpoker/edeliver) and docs, they’re very useful and well-explained.

This was a solution we found to ease our deploy process. How have you been managing your process? Did this post help you?

* * *

If you are into Elixir-Phoenix, you may also like…

[![What's new in Ecto 2.0 -- Reserve your copy](https://blog.plataformatec.com.br/wp-content/uploads/2016/05/CTA-blog-ebook-ecto-2-0.png)](http://pages.plataformatec.com.br/ebook-whats-new-in-ecto-2-0?utm_source=our-blog&utm_medium=referral&utm_campaign=ebook-ecto-2-0&utm_content=cta-blog-post-bottom-with-title)

Tags: [config](https://blog.plataformatec.com.br/tag/config/), [deployment](https://blog.plataformatec.com.br/tag/deployment/), [elixir](https://blog.plataformatec.com.br/tag/elixir/), [phoenix](https://blog.plataformatec.com.br/tag/phoenix/), Posted in [English](https://blog.plataformatec.com.br/category/english/), [7 Comments »](https://blog.plataformatec.com.br/2016/06/deploying-elixir-applications-with-edeliver/#comments)
