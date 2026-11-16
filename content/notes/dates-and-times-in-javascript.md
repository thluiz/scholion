---
title: "Dates and Times in JavaScript"
date: '2020-08-26T19:31:25+00:00'
category: webclip
summary: 'The post asks for feedback on the Temporal proposal, says Date is hard to work with, and explains that Temporal aims to handle dates, times, time zones, DST, and calendars more cleanly.'
tags: ["javascript", "temporal", "date", "time"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Dates and Times in JavaScript"
    url: "https://blogs.igalia.com/compilers/2020/06/23/dates-and-times-in-javascript"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/blogs-igalia-com--dates-and-times-in-javascript.md"
    kind: repo
---

The post asks readers to try the Temporal proposal, use the polyfill, and fill out the survey, but not to use it in production yet. It presents Temporal as a new JavaScript API for dates, times, timestamps, time zones, daylight saving time, date-only and time-only data, and non-Gregorian calendars.

## Reading notes

- JavaScript Date is described as broken in ways that cannot be fixed without breaking the web.
- Temporal is a new globally available object proposed for JavaScript.
- The API is meant to make date and time work more robust and modern.
- Temporal supports converting dates between time zones.
- Temporal handles adding and subtracting while accounting for daylight saving time.
- Temporal can work with date-only data and time-only data.
- Temporal also supports non-Gregorian calendars.
- The proposal is at Stage 2 in TC39 and the authors want to move it to Stage 3 soon.
- Readers are asked to test the API and give feedback so the proposal can still change if needed.
- The post says the API documentation can be used in the browser, in RunKit, or through the npm polyfill.
- The polyfill should not be used in production applications.
