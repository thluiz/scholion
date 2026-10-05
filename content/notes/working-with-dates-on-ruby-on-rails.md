---
title: "Working with dates on Ruby on Rails"
date: '2015-12-23T15:02:50-03:00'
category: webclip
summary: 'The article explains how Ruby on Rails handles dates across time zones, DST, persistence, queries, parsing, and JavaScript, and recommends using Rails and ActiveSupport time-zone-aware methods.'
tags: ["ruby-on-rails", "dates", "time-zones", "activesupport"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Working with dates on Ruby on Rails"
    url: "http://nandovieira.com/working-with-dates-on-ruby-on-rails"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-12/nandovieira-com--working-with-dates-on-ruby-on-rails.md"
    kind: repo
---

Rails date handling depends on using time-zone-aware helpers instead of Ruby methods that ignore application settings. The article recommends keeping infrastructure on UTC, defining the application time zone, and using ActiveSupport and Time.zone for current time, parsing, and comparisons.

## Reading notes

- Ruby uses Date and Time for date handling, and calculations like advancing an hour are done manually.
- The TZ environment variable affects Ruby, the date command, and can differ from PostgreSQL’s own timezone setting.
- Using Etc/UTC across infrastructure avoids DST problems and makes date behavior easier to coordinate.
- Rails can define its own application time zone in a configuration file or initializer, independent of TZ.
- Ruby does not follow Rails time zone settings, so application code should use ActiveSupport methods that return ActiveSupport::TimeWithZone.
- The article recommends Time.current instead of Time.now and Date.current instead of Date.today.
- Time.zone.today and Time.zone.now give deterministic results.
- ActiveSupport relies on TZInfo and the operating system’s tzdata, so keeping the server updated matters for DST data.
- When parsing dates, the article says to ignore embedded time-zone information and use Time.use_zone.
- ActiveRecord persists dates in UTC and converts them back to the application time zone when loading records.
- Using Time.now or Date.today can produce incorrect hours when records are persisted or loaded.
- PostgreSQL supports a time-with-time-zone column type, and the article shows adding it through an initializer.
- Queries should use time-zone-aware values such as Time.current so ActiveRecord can generate the expected SQL.
- For user input, use Time.zone.parse, Time.zone.local, and Time.zone.at instead of Ruby’s parsing and construction methods.
- Time.use_zone can set a time zone only for the duration of a block and can be used in a controller around_action.
- For JavaScript, the article recommends sending ISO 8601 strings with Time#iso8601 and using moment.js, with momentjs-timezone when a different zone is needed.
- The closing guidelines are to use UTC on the server, define the Rails time zone, keep presentation in the application layer, use Time.current and Date.current, parse with Time.zone.parse, and convert Date to ActiveSupport::TimeWithZone for comparison.
