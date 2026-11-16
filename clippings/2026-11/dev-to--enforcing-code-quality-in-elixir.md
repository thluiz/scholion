---
url: "https://dev.to/leandrocp/enforcing-code-quality-in-elixir-4on9"
captured_at: "2026-11-16T18:55:36+00:00"
title: "Enforcing code quality in Elixir"
domain: "dev-to"
---

Enforcing your Elixir code to be well formatted, with no warnings and hopefully free of bugs. I’m talking about a `mix alias` that will check the quality of the code, and that can be used during local development and also on CI/CD pipelines to enforce the team (or yourself) to keep a clean code. But keep in mind that there’s no magic, you’re still responsible for creating a code that’s well organized, performant, without security issues, and pleasant for human reading.

## [](#tldr)TL;DR

The complete example is at the end of the article.

## [](#tools)Tools

### [](#credo-and-dialyzer)Credo and Dialyzer

[Credo](https://github.com/rrrene/credo) is responsible for checking if the code is adherent to common good code practices established by the community. And [dialyzer](http://erlang.org/doc/man/dialyzer.html) is a static analysis tool that identifies software discrepancies, such as definite type errors, code that has become dead or unreachable because of a programming error (paraphrasing the official docs), but we’ll use [dialyxir](https://github.com/jeremyjh/dialyxir), which is wrapper around dialyzer written in Elixir that simplify the use of dialyzer.

### [](#sobelow)Sobelow

[Sobelow](https://github.com/nccgroup/sobelow) is a security-focused static analysis tool for the Phoenix framework. If you’re not using Phoenix, just remove it from the deps, configs, and alias described on this article.

### [](#mix-format)mix format

The [mix format](https://hexdocs.pm/mix/Mix.Tasks.Format.html) task was [introduced in Elixir v1.6](https://elixir-lang.org/blog/2018/01/17/elixir-v1-6-0-released/), and it’s used to format your code automatically. One of the main benefits of using it is to avoid boring and endless discussions like “how we should format the code ?”, “what should be the line length ?”, and so on. [Elixir also uses it](https://github.com/elixir-lang/elixir/blob/v1.8/Makefile#L215-L216) to enforce a standard format.

### [](#warning-as-errors)Warning as errors

That’s not a tool, actually, it’s an [Elixir compile attribute](https://hexdocs.pm/mix/Mix.Tasks.Compile.Elixir.html) that will treat warnings in the current project as errors and return a non-zero exit code, which means that your project won’t compile if it has any warning.

### [](#a-note-before-we-continue)A note before we continue

Having all those tools and configs turned on _may be_ annoying. A module without doc, a wrong spec or even an unused variable will stop you from compiling and shipping the code. The level of enforcement is up to you, so you should adapt the tools and configs as required for your project (and your stress level). But it’s a good ideia to plan for the long term.

## [](#implementation)Implementation

Ok, let’s change the files to implement the quality check. Let’s do that piece by piece, or better saying, function by function.

### [](#mixexs)mix.exs

First, let’s install the deps. Add the following in _deps list_:  

```
{:credo, "~> 1.0", only: [:dev, :test], runtime: false},
{:dialyxir, "~> 1.0.0-rc.6", only: [:dev, :test], runtime: false},
{:sobelow, "~> 0.7", only: [:dev, :test], runtime: false}
```

And let’s change the project’s config. Add this to the _project function_:  

```
elixirc_options: [warnings_as_errors: true],
aliases: aliases(),
dialyzer: [
  plt_file: {:no_warn, "priv/plts/dialyzer.plt"},
  ignore_warnings: ".dialyzer_ignore.exs"
]
```

Which will be like:  

```
defmodule YourProject.MixProject do
  use Mix.Project

  def project do
    [
      # current configs...

      elixirc_options: [warnings_as_errors: true],
      aliases: aliases(),
      dialyzer: [
        plt_file: {:no_warn, "priv/plts/dialyzer.plt"},
        ignore_warnings: ".dialyzer_ignore.exs"
      ]
    ]
  end

  defp deps do
    [
      # current deps...

      # dev, test
      {:credo, "~> 1.0", only: [:dev, :test], runtime: false},
      {:dialyxir, "~> 1.0.0-rc.6", only: [:dev, :test], runtime: false},
      {:sobelow, "~> 0.7", only: [:dev, :test], runtime: false}
    ]
  end
end
```

I recommend reading [dialyxir doc](https://hexdocs.pm/dialyxir/0.4.1/readme.html) to know more about its config, especially the [Continuous Integration](https://github.com/jeremyjh/dialyxir#continuous-integration) if you want to enforce it on your CI/CD pipeline.

Continuing, let’s create an alias function in your mix.exs file, _if you don’t have this function already created_, and add two aliases:  

```
defp aliases do
  [
    # current aliases...

    quality: ["format", "credo --strict", "sobelow --verbose", "dialyzer", "test"],
    "quality.ci": [
      "test",
      "format --check-formatted",
      "credo --strict",
      "sobelow --exit",
      "dialyzer --halt-exit-status"
    ]
  ]
end
```

I like using one alias specific for local development (quality) and one for CI/CD (quality.ci) because I have more freedom on the order of the tasks and its arguments. For example, on local development I don’t want to check if the code is formatted, I just format the code directly; and I like to see test results at the end. Adapt as you want.

### [](#dialyzerignoreexs).dialyzer\_ignore.exs

Create the file _.dialyzer\_ignore.exs_ in the root dir of the project:  

```
[
  {":0:unknown_function Function ExUnit.Callbacks. __merge__ /3 does not exist."},
  {":0:unknown_function Function ExUnit.CaseTemplate. __proxy__ /2 does not exist."}
]
```

Remember I said those tools may be annoying ? Specially the dialyzer. Don’t get me wrong, dialyzer is amazing and I believe you should use it, but sometimes you need to ignore a warning or two, and that’s the file where you can do that.

About the content of this file: we’ll run our aliases on the test environment (MIX\_ENV=test) and dialyzer reclaim that those functions are errors, but that’s not a big deal and let’s just ignore it.

### [](#credo)Credo

You don’t need to change anything in order to make credo work, but the default rules may not be suitable for your project. You can change that using a [.credo.exs](https://github.com/rrrene/credo#configuration-via-credoexs) file or [using special comments](https://github.com/rrrene/credo#inline-configuration-via-config-comments).

### [](#gitignore).gitignore

Add to .gitignore:  

```
# Dialyzer
/priv/plts/*.plt
/priv/plts/*.plt.hash

# Sobelow
.sobelow
```

Those files are environment-dependent.

## [](#executing)Executing

Finally, you’re ready to go! 😅

First, let’s create the dir where dialyzer will store plt files:

`mkdir -p priv/plts`

And then just execute in your terminal:

`MIX_ENV=test mix quality`

Take some time off and grab a coffee, the first execution will take some time to build all dialyzer artefacts, but those files will be cached, don’t worry.

And change your CI/CD pipeline to execute:

`MIX_ENV=test mix quality.ci`

Whenever this command finds an issue in your code, the CI/CD pipeline will halt and return a failure.

## [](#complete-example-files)Complete example files

_mix.exs_  

```
defmodule YourProject.MixProject do
  use Mix.Project

  def project do
    [
      app: :your_project,
      version: "0.1.0",
      elixir: "~> 1.6",
      elixirc_paths: elixirc_paths(Mix.env()),
      elixirc_options: [warnings_as_errors: true],
      compilers: [:phoenix, :gettext] ++ Mix.compilers(),
      start_permanent: Mix.env() == :prod,
      aliases: aliases(),
      deps: deps(),
      dialyzer: [
        plt_file: {:no_warn, "priv/plts/dialyzer.plt"},
        ignore_warnings: ".dialyzer_ignore.exs"
      ]
    ]
  end

  # Configuration for the OTP application.
  #
  # Type `mix help compile.app` for more information.
  def application do
    [
      mod: {YourProject.Application, []},
      extra_applications: [:logger, :runtime_tools]
    ]
  end

  # Specifies which paths to compile per environment.
  defp elixirc_paths(:test), do: ["lib", "test/support"]
  defp elixirc_paths(_), do: ["lib"]

  # Specifies your project dependencies.
  #
  # Type `mix help deps` for examples and options.
  defp deps do
    [
      {:phoenix, "~> 1.4.3"},
      {:phoenix_pubsub, "~> 1.1"},
      {:phoenix_ecto, "~> 4.0"},
      {:ecto_sql, "~> 3.0"},
      {:postgrex, ">= 0.0.0"},
      {:phoenix_html, "~> 2.11"},
      {:phoenix_live_reload, "~> 1.2", only: :dev},
      {:gettext, "~> 0.11"},

      # dev, test
      {:credo, "~> 1.0", only: [:dev, :test], runtime: false},
      {:dialyxir, "~> 1.0.0-rc.6", only: [:dev, :test], runtime: false},
      {:sobelow, "~> 0.7", only: [:dev, :test], runtime: false}
    ]
  end

  # Aliases are shortcuts or tasks specific to the current project.
  # For example, to create, migrate and run the seeds file at once:
  #
  # $ mix ecto.setup
  #
  # See the documentation for `Mix` for more info on aliases.
  defp aliases do
    [
      quality: ["format", "credo --strict", "sobelow --verbose", "dialyzer", "test"],
      "quality.ci": [
        "test",
        "format --check-formatted",
        "credo --strict",
        "sobelow --exit",
        "dialyzer --halt-exit-status"
      ],
      "ecto.setup": ["ecto.create", "ecto.migrate", "run priv/repo/seeds.exs"],
      "ecto.reset": ["ecto.drop", "ecto.setup"],
      test: ["ecto.create --quiet", "ecto.migrate", "test"]
    ]
  end
end
```

_.dialyzer\_ignore.exs_  

```
[
  {":0:unknown_function Function ExUnit.Callbacks. __merge__ /3 does not exist."},
  {":0:unknown_function Function ExUnit.CaseTemplate. __proxy__ /2 does not exist."}
  ]
```

_.gitignore_  

```
# The directory Mix will write compiled artifacts to.
/_build/

# If you run "mix test --cover", coverage assets end up here.
/cover/

# The directory Mix downloads your dependencies sources to.
/deps/

# Where 3rd-party dependencies like ExDoc output generated docs.
/doc/

# Ignore .fetch files in case you like to edit your project deps locally.
/.fetch

# If the VM crashes, it generates a dump, let's ignore it too.
erl_crash.dump

# Also ignore archive artifacts (built via "mix archive.build").
*.ez

# Ignore package tarball (built via "mix hex.build").
your_project-*.tar

# If NPM crashes, it generates a log, let's ignore it too.
npm-debug.log

# The directory NPM downloads your dependencies sources to.
/assets/node_modules/

# Since we are building assets from assets/,
# we ignore priv/static. You may want to comment
# this depending on your deployment strategy.
/priv/static/

# Files matching config/*.secret.exs pattern contain sensitive
# data and you should not commit them into version control.
#
# Alternatively, you may comment the line below and commit the
# secrets files as long as you replace their contents by environment
# variables.
/config/*.secret.exs

.elixir_ls

# Dialyzer
/priv/plts/*.plt
/priv/plts/*.plt.hash%

# Sobelow
.sobelow
```

## [](#references)References

*   [Adopting Elixir - From Concept to Production](https://pragprog.com/book/tvmelixir/adopting-elixir)
    
*   [https://blog.dnsimple.com/2018/10/elixir-dialyzer-in-ci/](https://blog.dnsimple.com/2018/10/elixir-dialyzer-in-ci/)
