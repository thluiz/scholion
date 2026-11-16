---
url: "https://medium.com/@maciejcha/elixir-currency-and-localized-number-format-518cafb9cc01"
captured_at: "2026-11-16T05:56:31+00:00"
title: "Elixir currency and localized number format | by Matt Chad | Medium"
domain: "medium-com"
---

Elixir
Phoenix Framework
Localization
Currency
Functional Programming
Elixir currency and localized number format
Matt Chad
2 min read
·
Apr 26, 2020

Elixir + Cldr

Today, I’ll show you how quickly and easily add support for ISO localization in Elixir. My app is named Bazaar, so you should rename all occurrences of Bazaar with your’s app name.
In the mix.deps file add dependencies for:

defp deps do
[
{:ex_cldr, "~> 2.0"},
{:ex_cldr_numbers, "~> 2.0"},
{:jason, "~> 1.0"},
{:gettext, "~> 0.11"}
]
end

We are using Cldr for localization with Cldr.Numbers for numbers and currency formatting and Jason lib for JSON decode/encode. Also, gettext lib is required by Cldr for additional locale support.
Download and compile dependencies:

mix deps.get && mix deps.compile

Configure Cldr lib:

defmodule Bazaar.Cldr do
use Cldr,
default_locale: "en",
json_library: Jason,
locales: ["en", "zh"],
gettext: Bazaar.Gettext,
data_dir: "./priv/cldr",
otp_app: :bazaar,
precompile_number_formats: ["¤¤#,##0.##"],
providers: [Cldr.Number],
generate_docs: true
end

We’ve just added support for en and zh locales where en locale is set as default one. There is also specified provider with Cldr.Number item that indicates we want to use ex_cldr_numbers hex.
Remember to add /priv/cldr/ to .gitignore because localization files are downloaded during compilation.

Time for testing. To start interactive Elixir and use dependencies from the current project, move to the project directory and run:

iex -S mix

Now you may use localization with this simple function call:

Bazaar.Cldr.Number.to_string 1231231, locale: "zh", currency: "USD"

Successful execution will result in printed amount of US dollars in Chinese locale format:

{:ok, "US$1,231,231.00"}

For full documentation, visit official page of Cldr hex provided in the links below.

Getting Started with Cldr 2.0
is an Elixir library for the Unicode Consortium's Common Locale Data Repository (CLDR). The intentions of CLDR, and…

hexdocs.pm

Number and Currency Localization and Formatting
ex_cldr_numbers is an addon library application for ex_cldr that provides localization and formatting for numbers and…

hexdocs.pm
