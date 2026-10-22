---
title: "Date, Time, and Time Zone Enhancements in .NET 6"
date: '2021-06-14T09:03:24-03:00'
category: webclip
summary: 'The post introduces DateOnly and TimeOnly in .NET 6, explains why they improve type safety and storage, and describes time zone conversion, display name, and adjustment rule updates.'
tags: ["dotnet-6", "dateonly", "timeonly", "time-zone"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Date, Time, and Time Zone Enhancements in .NET 6 | .NET Blog"
    url: "https://devblogs.microsoft.com/dotnet/date-time-and-time-zone-enhancements-in-net-6/?utm_source=csharpdigest&utm_medium=email&utm_campaign=367"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2021-06/devblogs-microsoft-com--date-time-and-time-zone-enhancements-dotnet-6.md"
    kind: repo
---

The post presents new date and time types in .NET 6 and several time zone improvements. It explains how DateOnly and TimeOnly separate whole dates from times of day, and how the runtime now handles IANA and Windows time zone IDs more flexibly.

## Reading notes

- DateOnly represents only a year, month, and day, with no time component.
- It is meant for birth dates, anniversaries, hire dates, and other business dates that are not tied to a specific time.
- DateOnly improves type safety compared with using DateTime for whole dates.
- A DateOnly has no Kind value and is always effectively unspecified.
- Serializing DateOnly only requires year, month, and day, which avoids extra zeroes.
- DateOnly matches database date types more closely than DateTime.
- DateOnly can be constructed with supported calendars, but it always represents Proleptic Gregorian values.
- TimeOnly represents only a time of day.
- TimeOnly is meant for recurring meeting times, alarms, and business opening and closing times.
- TimeOnly has a range from 00:00:00.0000000 to 23:59:59.9999999.
- TimeOnly handles crossing midnight when time is added or subtracted.
- TimeOnly gives better type safety than using DateTime or TimeSpan for time-of-day values.
- TimeOnly can be combined with DateOnly to create a DateTime.
- The names DateOnly and TimeOnly were chosen to avoid reserved keywords and to fit .NET naming constraints.
- The post says Noda Time is a good library, but .NET chose to augment existing types instead of replacing them.
- TimeZoneInfo.FindSystemTimeZoneById now converts between IANA and Windows IDs when needed.
- The runtime uses CLDR mappings through ICU globalization support.
- New conversion helpers are TryConvertIanaIdToWindowsId and TryConvertWindowsIdToIanaId.
- TimeZoneInfo.HasIanaId indicates whether a TimeZoneInfo already uses an IANA identifier.
- On Linux and macOS, time zone display names were improved to be more specific and usable.
- The UTC display name now follows the current language on all operating systems.
- TimeZoneInfo.AdjustmentRule.BaseUtcOffsetDelta is now public.
- CreateAdjustmentRule also has an overload that accepts baseUtcOffsetDelta.
- The post says the built-in TimeZoneInfo methods already handle most adjustment-rule logic for common use.
