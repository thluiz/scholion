---
title: "The 5 laws of API dates and times"
date: '2013-09-27T10:16:48-03:00'
category: webclip
summary: 'The page argues that APIs should use ISO 8601, accept any timezone, store times in UTC, return UTC, and avoid time values when only a date is needed to reduce ambiguity and parsing problems.'
tags: ["api", "dates-and-times", "iso-8601", "utc"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "The 5 laws of API dates and times | API UX"
    url: "http://apiux.com/2013/03/20/5-laws-api-dates-and-times/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2013-09/apiux-com--the-5-laws-of-api-dates-and-times.md"
    kind: repo
---

The page gives five rules for handling dates and times in APIs. It recommends ISO 8601, accepting any timezone input, storing times in UTC, returning UTC to consumers, and leaving out time values when only a date is needed.

## Reading notes

- Use ISO 8601 because it sorts naturally, handles timezone offsets, avoids locale ambiguity, and is widely supported by programming languages and libraries.
- Accept any timezone because API users can come from anywhere, and the API should not assume one timezone for everyone.
- Store dates and times in UTC, since UTC is the common reference point and avoids tying data to the company headquarters timezone.
- Return dates and times in UTC so consumers can apply the offset they need and the API team does not have to calculate offsets for every request.
- Do not use time when it is not needed, especially for date-only values like a target completion date, because adding a random time can create interpretation problems across timezones.
