---
title: "Temporal: getting started with JavaScript’s new date time API"
date: '2021-06-29T10:46:30-03:00'
category: webclip
summary: 'The post introduces Temporal as a newer JavaScript date time API, explains its time zone and calendar model, and shows how its classes handle exact time, wall-clock time, and arithmetic.'
tags: ["javascript", "temporal", "date-time-api", "time-zones"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Temporal: getting started with JavaScript’s new date time API"
    url: "https://2ality.com/2021/06/temporal-api.html?utm_source=tldrnewsletter"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2021-06/2ality-com--temporal-getting-started-with-javascript-new-datetime-api.md"
    kind: repo
---

Temporal is presented as a newer and easier date time API for JavaScript than `Date`. The post focuses on how Temporal separates exact time from wall-clock time, supports time zones and non-Gregorian calendars, and uses specialized immutable classes for different kinds of temporal values.

## Reading notes

- Temporal is accessed through the global `Temporal` object and uses immutable values.
- The API supports time zones and non-Gregorian calendars.
- Different classes represent different kinds of time values, which makes the context of a value easier to understand.
- `Instant` represents exact UTC time and is mainly a container for epoch nanoseconds.
- `ZonedDateTime` combines wall-clock time, a time zone, and a calendar.
- `PlainDateTime`, `PlainDate`, and `PlainTime` are timezone-less, abstract representations of time.
- `PlainYearMonth` is used for a month in a year.
- `PlainMonthDay` is used for a day in a month.
- `Temporal.now` provides the current time in several forms, including `instant()`, `zonedDateTimeISO()`, `plainDateTimeISO()`, and `plainTimeISO()`.
- Temporal time zones are based on the IANA Time Zone Database.
- The post shows that the same time zone can have different offsets during standard time and daylight saving time.
- Temporal calendars are based on Unicode CLDR and include `iso8601`, `gregory`, `japanese`, `islamic`, and others.
- Temporal adds support for date time strings that can include IANA time zone names and calendar systems.
- `.from()` accepts strings, same-class instances, and field objects.
- `.toString()` can be configured with options such as `offset`, `timeZoneName`, and `smallestUnit`.
- Temporal values can be serialized to JSON with `.toJSON()`.
- Temporal supports human-readable output through `.toLocaleString()`, similar to `Intl.DateTimeFormat`.
- Legacy `Date` values can be converted to `Temporal.Instant`, and `Instant` can be converted back through epoch milliseconds.
- The post shows how to read field values, create modified copies with `.with()`, and sort values with `D.compare`.
- Temporal values can be converted between `Instant`, `ZonedDateTime`, and `PlainDateTime`.
- Temporal values can also be converted between time zones with `.withTimeZone()`.
- Duration arithmetic is used for differences and additions, including examples for flight time, next day computation, and finding the first Monday in September.
- The post notes that the proposal is not ready for unflagged shipping and that the polyfill is useful for experimentation but not for production.
