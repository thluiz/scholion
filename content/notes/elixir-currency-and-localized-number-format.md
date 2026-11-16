---
title: "Elixir currency and localized number format"
date: '2026-11-16T05:56:31+00:00'
category: webclip
summary: 'The post shows how to add CLDR-based localization in Elixir, set up dependencies, configure locales, and format a currency amount with `Cldr.Number.to_string/2`.'
tags: ["elixir", "localization", "currency-formatting", "cldr"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Elixir currency and localized number format | by Matt Chad | Medium"
    url: "https://medium.com/@maciejcha/elixir-currency-and-localized-number-format-518cafb9cc01"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/medium-com--elixir-currency-and-localized-number-format.md"
    kind: repo
---

The post explains how to add ISO localization support in an Elixir app using `ex_cldr`, `ex_cldr_numbers`, `jason`, and `gettext`. It then shows a `Cldr` module configured with `en` as the default locale and `en` and `zh` enabled.

## Reading notes

- Add `ex_cldr`, `ex_cldr_numbers`, `jason`, and `gettext` to `mix.deps`
- Run `mix deps.get && mix deps.compile`
- Define `Bazaar.Cldr` with `default_locale: "en"`, `locales: ["en", "zh"]`, `gettext: Bazaar.Gettext`, and `providers: [Cldr.Number]`
- Add `/priv/cldr/` to `.gitignore` because the localization files are downloaded during compilation
- Start IEx with `iex -S mix`
- Call `Bazaar.Cldr.Number.to_string 1231231, locale: "zh", currency: "USD"`
- The example returns `{:ok, "US$1,231,231.00"}`
