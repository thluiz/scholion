---
title: "Configuring your Elixir Application at Runtime with Vapor"
date: '2020-07-05T14:10:42+00:00'
category: webclip
summary: 'Explains problems with compile-time config.exs in Elixir and shows how to migrate to runtime, env‑driven configuration using Vapor, .env files, and Application.put_env.'
tags: ["elixir", "configuration", "runtime-config"]
has_commentary: false
generated_by: "openai/gpt-5.1"
sources:
  - title: "Configuring your Elixir Application at Runtime with Vapor"
    url: "https://web.archive.org/web/20200514101634id_/https://blog.appsignal.com/2020/04/28/configuring-your-elixir-application-at-runtime-with-vapor.html"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/web-archive-org--runtime-elixir-config-with-vapor-migration.md"
    kind: repo
---

The text describes issues Elixir teams face when relying on compile‑time `config/*.exs` files, especially as applications and deployment setups grow more complex. It contrasts compile‑time and runtime configuration, summarizes recent Elixir features that clarify this boundary, and introduces the `vapor` library as a practical way to move configuration to runtime using environment variables. The example walks through loading `.env` files, converting environment variables into application configuration on startup, and then refining that using Vapor’s providers.

## Reading notes

- Configuration has been a recurring pain point in the Elixir community, and recent work aims to make it easier to solve, particularly by improving runtime configuration.
- Many teams using `config/*.exs` encounter problems as apps and deployment strategies scale, even though some smaller or simpler applications work fine with this approach.
- A common confusion arises when `System.get_env/1` is used in `config.exs`; it is evaluated at compile time, so missing env vars in the build environment produce incorrect production configuration.
- The desired behavior is to read environment variables at runtime in the environment where the release actually runs, rather than when it is compiled.
- Because `System.get_env/1` in config is evaluated at compile time, a release built for staging cannot safely be reused in production; separate builds are needed for each environment.
- Reusing the same tested build artifact across staging and production is safer, since it reduces configuration and build differences between environments.
- Libraries that rely on `Application.get_env/3` for behavior effectively support only a single configuration instance, which makes it hard to use multiple instances (for example, an API client with multiple API keys) in a concurrent runtime.
- Historically, integrating secret management tools like Vault or AWS Secrets Manager was awkward and relied on conventions such as `REPLACE_OS_VARS` in `distillery` or `{:system, "ENV_VAR"}` markers to signal runtime evaluation.
- Elixir 1.9 introduced `mix release` and modules like `Config`, `Config.Provider`, and `Config.Reader`, along with Elixir 1.10’s `Application.compile_env/3` to clearly denote compile‑time configuration.
- There are plans to deprecate using `Application.get_env/3` at compile time, which would further reduce accidental misuse of configuration intended for runtime.
- New libraries, including `vapor`, help make the division between runtime and compile‑time configuration more explicit and easier to handle.
- A broader shift is encouraged where libraries and apps move away from heavy use of application environment and instead accept configuration as function arguments.
- The `init/2` callbacks in Ecto and `Phoenix.Endpoint` are cited as good examples of enabling runtime configuration for repos and endpoints.
- To start with `vapor`, the library is added as a dependency in `mix.exs` using `{:vapor, "~> 0.8.0"}`.
- `vapor` can be integrated in the application’s `start/2` callback by calling `Vapor.load!([%Vapor.Provider.Dotenv{}])` before starting children in the supervision tree.
- The Dotenv provider allows `vapor` to read `.env` or `.env.test` files and populate the system environment at runtime, and does nothing if these files are absent.
- The example shows an initial compile‑time configuration for `VaporExample.Endpoint` setting `http: [port: 4000]` in `config/config.exs`.
- This endpoint port setting is moved to runtime by deleting the `http` entry in `config.exs`, adding `PORT=4000` to `.env`, and adding a `load_system_env/0` function in the application module.
- The first version of `load_system_env/0` reads the `PORT` env var with `System.get_env/1`, raises if it is missing, converts the value to an integer, and then calls `Application.put_env/3` for the endpoint’s `http` configuration.
- This approach ensures that whether the app is started via `mix` or as a release, and in `dev`, `test`, or `prod`, the port configuration behaves consistently.
- Failing fast on missing configuration prevents the application from starting in a subtly broken state, enforcing correctness early in the boot process.
- The author proposes a guiding rule that any configuration that can be set at runtime should be set at runtime.
- The initial manual `load_system_env/0` contains boilerplate for reading and converting env vars, which `vapor` can simplify through its provider API.
- A refined `load_system_env/0` version uses `%Vapor.Provider.Env{bindings: [ {:port, "PORT", map: &String.to_integer/1} ]}` and `Vapor.Provider.load!/1` to map env vars to a config struct.
- This `vapor`‑based approach still converts string values like `"4000"` into integers and surfaces missing variables as errors, but centralizes logic in a consistent configuration API.
- Once the basic runtime setup with `vapor` is in place, developers can gradually migrate other compile‑time configurations to runtime.
- After maximizing runtime configurability, teams can further reduce reliance on the application environment itself by using callbacks like `init/2` and passing configuration as arguments where possible.
- Adopting this runtime‑oriented configuration style is presented as a way to keep Elixir applications correctly configured in the long term and to give teams a clearer, more uniform configuration workflow.
