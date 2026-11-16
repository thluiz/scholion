---
title: "Formatting Dates With the DateTimeFormat Object"
date: '2020-02-22T12:11:43+00:00'
category: webclip
summary: 'JavaScript’s Intl.DateTimeFormat formats dates for different locales without manual string handling. It accepts locale tags and options, and also offers methods for parts, ranges, and resolved settings.'
tags: ["javascript", "internationalization", "dates", "locales"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Formatting Dates With the DateTimeFormat Object - The Web Dev"
    url: "https://web.archive.org/web/20200613140219id_/https://thewebdev.info/2020/01/12/formatting-dates-with-the-datetimeformat-object/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/web-archive-org--formatting-dates-with-datetimeformat-object.md"
    kind: repo
---

JavaScript’s `Intl.DateTimeFormat` formats dates according to locale, so the same `Date` object can produce different strings for different regions. The constructor accepts one or more locale tags, and options can change the calendar, numbering system, time zone, hour cycle, and which date and time fields appear.

It also exposes methods beyond `format()`. `formatToParts()` returns the formatted value as parts, `resolvedOptions()` shows the locale and options in use, and `formatRange()` and `formatRangeToParts()` format a date range in the most concise form for the selected locale.

## Reading notes

- The constructor formats dates for different locales without manual date-string manipulation.
- The first argument can be a locale string or an array of locale strings, with fallback locales on the right.
- Unicode extension keys supported in locale tags include `nu`, `ca`, and `hc`.
- `nu` controls the numbering system, `ca` controls the calendar, and `hc` controls the hour cycle.
- The second argument accepts an options object for formatting behavior.
- `localeMatcher` can be `lookup` or `best fit`.
- `timeZone` can use UTC or IANA time zone names such as `Asia/Shanghai` and `America/New_York`.
- `hour12` sets 12-hour or 24-hour output and overrides `hc`.
- `hourCycle` can be `h11`, `h12`, `h23`, or `h24`.
- `formatMatcher` can be `basic` or `best fit`.
- The required date-time field combinations include year, month, and day, and also hour, minute, and second combinations.
- `weekday`, `era`, `year`, `month`, `day`, `hour`, `minute`, `second`, and `timeZoneName` each accept specific display styles.
- If all component options are `undefined`, `year`, `month`, and `day` default to `numeric`.
- `format()` returns a locale-formatted date string from a `Date` object.
- `formatToParts()` returns an array of objects for the formatted parts.
- `resolvedOptions()` returns the locale and formatting options computed at initialization.
- `formatRange()` formats two dates as a concise range.
- `formatRangeToParts()` returns the parts of a formatted date range as an array.
- The examples show the same date formatted in English, French Canadian, German, Buddhist calendar English, and Traditional Chinese.
