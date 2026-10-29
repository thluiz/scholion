---
title: "Internationalization using Gettext in the Phoenix framework"
date: '2015-12-23T18:36:07-03:00'
category: webclip
summary: 'The post explains i18n and l10n in Phoenix 1.1, shows why Linguist was unwieldy, and walks through using Gettext, .pot and .po files, and a locale-switching plug.'
tags: ["gettext", "phoenix", "elixir", "internationalization"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Internationalization using Gettext in the Phoenix framework"
    url: "http://sevenseacat.net/2015/12/20/i18n-in-phoenix-apps.html"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-12/sevenseacat-net--internationalization-using-gettext-in-phoenix-framework.md"
    kind: repo
---

The post explains internationalization as adapting a web app for different languages or cultures, and localization as the work of actually implementing those language or culture changes. It contrasts Phoenix’s earlier Linguist approach with Gettext, which lets templates mark translatable text directly with `gettext` and defaults to returning the original string if no translation is available.

## Reading notes

- Internationalization is the process of adapting an app for different languages or cultures, and localization is the process of implementing a different language or culture in the app.
- Linguist required translation keys in views, but the post says it created too much overhead and became messy in large applications.
- Phoenix 1.1 added Gettext support, which uses `gettext` in templates to mark text for translation.
- `gettext` can be added before localization work starts, and if no other language is needed it simply returns the original string.
- `gettext.extract` generates or updates `.pot` template files from translatable strings in the app.
- `.pot` files store the template strings and should not be edited manually.
- `.po` files store translations for a locale, and `gettext.merge` updates them from the `.pot` files.
- The post shows adding an Esperanto locale with `mix gettext.merge priv/gettext --locale eo` and editing the generated `default.po` file with Esperanto translations.
- A custom plug can read a `locale` query parameter, set the application locale with `Gettext.put_locale`, and store it in the session.
- The plug is added to the browser pipeline so requests can switch between locales through the URL.
- The maintenance workflow is to wrap new template text in `gettext` and periodically run `mix gettext.extract --merge` to keep template and translation files in sync.
