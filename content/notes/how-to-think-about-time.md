---
title: "How to Think About Time"
date: '2026-09-25T08:40:09+01:00'
category: webclip
summary: 'The guide separates physical time from civil time, defines instants, durations, datetimes, periods, and time zones, and warns about ambiguous math, storage, and wall-clock use.'
tags: ["time","date-time","time-zones"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "How to Think About Time"
    url: "https://errorprone.info/docs/time"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/errorprone-info--how-to-think-about-time.md"
    kind: repo
---

The guide builds time from two distinct realms. Physical time uses instants and durations on a timeline. Civil time uses datetimes and periods, with calendars and time zones as separate concerns. It argues that code should keep these concepts apart because mixing them creates ambiguity and bugs.

It also warns about several practical pitfalls: negative durations and periods, month-based math, storing values without thinking through time-zone changes, and using wall time to measure elapsed time. UTC is useful as a reference, but zone-independent code should stay in physical time and use types that model instants and durations only.

## Reading notes

- The text proposes a mental model for dates and times based on separate concepts, rather than loose practices.
- Physical time is described as a timeline with instants and durations, measured in seconds.
- Durations are differences between instants; months and years do not have precise meaning in this use.
- Negative durations are possible, but the text recommends avoiding them because of bugs and implicit expectations.
- The valid operations in physical time are instant minus instant equals duration, instant plus or minus duration equals instant, duration with duration, and duration times or divided by a real number.
- A particular instant can only be referred to with the help of a duration in relation to a reference instant, called epoch.
- Civil time is presented as a set of human concepts such as months, years, business days, holidays, and calendars.
- In the Gregorian calendar, date is year, month, and day; time of day is hour, minute, and second; datetime combines these six fields.
- The text treats the proleptic Gregorian calendar to extend the system to all history.
- Time zone is not a seventh field of civil datetime; it is the set of rules that converts between instant and datetime.
- The best time zones are those from the IANA database, such as `America/New_York` and `Asia/Kolkata`.
- Three-letter codes like `PST` are pointed out as bad because they generate ambiguity and inconsistent behavior.
- UTC is described as the simplest time zone, with fixed zero offset, used as a reference point.
- For zone-independent code, the text recommends staying only in physical time and using types that model instants and durations.
- Storing instants or datetimes requires thinking about user time-zone changes and changes in time-zone rules.
- The text advises against types that mix datetime or instant with time zone, because they join physical and civil time and make serialization ambiguous.
- Wall time is approximate, can be adjusted, and should not be used to measure elapsed time.
- Elapsed time should be measured with a dedicated tool, such as Stopwatch.
- Leap seconds are treated as rare exceptions that can usually be ignored, although they affect clock readings.
- Midnight does not always exist in a local day; sometimes the correct term is start of day.
- Recurrences are rules for selecting successive dates or datetimes, distinct from period arithmetic.
- The text recommends writing dates in ISO `YYYY-MM-DD` format to avoid cultural ambiguity.
- The final section lists APIs by language that represent each concept separately.
