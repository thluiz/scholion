---
title: "Reading Rails - The Adapter Pattern"
date: '2014-03-05T11:04:25-03:00'
category: webclip
summary: 'The article surveys how Rails uses the Adapter Pattern to hide differences between JSON libraries, databases, and time classes, keeping a uniform API while still handling library-specific details.'
tags: ["adapter-pattern", "rails", "activerecord", "activesupport"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Reading Rails - The Adapter Pattern - Monkey and Crow"
    url: "http://monkeyandcrow.com/blog/reading_rails_the_adapter_pattern/?utm_source=rubyweekly&utm_medium=email"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2014-03/monkeyandcrow-com--reading-rails-the-adapter-pattern.md"
    kind: repo
---

Rails uses the Adapter Pattern to present a uniform interface over libraries and classes that behave differently. The article shows this with JSON parsers, database adapters, and ActiveSupport changes to DateTime and Time.

## Reading notes

- The Adapter Pattern wraps different interfaces so code can use one consistent API.
- In the example, special cases for different locator libraries quickly become hard to maintain.
- A GeoFish adapter and an ActsAsFound adapter let the rest of the code call the same method.
- MultiJSON adapts JSON libraries so ActiveSupport can switch parsers without changing every call site.
- The Oj adapter renames `:symbolize_keys` to `:symbol_keys` before calling `Oj.load`.
- The Yajl adapter builds a parser with `:symbolize_keys` and then parses the string.
- ActiveRecord uses adapters for PostgreSQL, MySQL, and SQLite under `lib/connection_adapters`.
- `AbstractAdapter` provides shared behavior, while database-specific adapters customize it.
- `quoted_date` in `AbstractAdapter` formats dates with `value.to_s(:db)`.
- The PostgreSQL adapter extends that result with microseconds when available.
- It also appends `BC` for negative years.
- PostgreSQL and MySQL use different native SQL for `primary_key` when creating tables.
- ActiveSupport adds methods to DateTime and Time so they expose more similar APIs.
- `DateTime#to_i` is defined through helper methods that compute seconds since the Unix epoch.
- Even with these additions, DateTime and Time still differ in behavior, such as what `+ 1` means.
- ActiveSupport adds methods like `change` and `Duration` to smooth out those differences.
- The article concludes that Rails uses adapters to hide many details, but developers still need to know the underlying differences.
