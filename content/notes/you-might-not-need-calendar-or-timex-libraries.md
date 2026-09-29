---
title: "You might not need the Calendar or Timex libraries"
date: '2020-05-28T11:23:52-03:00'
category: webclip
summary: 'Elixir’s standard library now covers most date, time, and timezone needs. Third-party libraries still matter for missing features, but many projects can avoid them.'
tags: ["elixir", "date-time", "time-zone", "standard-library"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "You might not need the Calendar or Timex libraries"
    url: "http://www.creativedeletion.com/2020/05/25/calendar-standard-library-2020.html"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2020-05/creativedeletion-com--you-might-not-need-calendar-or-timex-libraries.md"
    kind: repo
---

Elixir’s standard library now includes native date and time types, time zone calculations through `Calendar.TimeZoneDatabase`, Unix time conversion, ranges, parsing, formatting, and other common date and time operations. The post argues that for most uses, Calendar or Timex are no longer required.

It recommends preferring the standard library when it offers the same functionality because it means fewer dependencies, more long-term maintenance, and more familiarity across Elixir developers. Third-party libraries still make sense for gaps in the standard library, and time zone calculations still require a time zone database such as `tzdata` or another `TimeZoneDatabase` implementation.

## Reading notes

- Elixir 1.3 introduced native date and time types.
- Elixir 1.8 added the `Calendar.TimeZoneDatabase` behaviour for time zone calculations.
- The standard library now supports comparison, arithmetic, time zones, Unix time conversion, calendar fields, date ranges, and ISO 8601 parsing and formatting.
- `Calendar.strftime/3` is added on the master branch and is scheduled for Elixir 1.11.
- The standard library is preferred when it provides the same feature as a third-party library because it reduces dependencies and increases shared familiarity.
- Third-party libraries are still useful when the standard library does not provide the needed functionality.
- For time zone calculations, applications need a timezone database dependency and configuration such as `tzdata`.
- Library authors can use `from_naive/3` and `shift_zone/3` and let end users choose the time zone database implementation.
