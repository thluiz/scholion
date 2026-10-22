---
url: "https://2ality.com/2021/06/temporal-api.html?utm_source=tldrnewsletter"
captured_at: "2021-06-29T10:46:30-03:00"
title: "Temporal: getting started with JavaScript’s new date time API"
domain: "2ality-com"
---

# Temporal: getting started with JavaScript’s new date time API

**Update 2021-06-29:** Clarified how `Instant` uses the ISO-8601 calendar. Listed the methods of some classes.

---

`Date`, JavaScript’s current date time API is [infamously difficult to use](https://maggiepint.com/2017/04/09/fixing-javascript-date-getting-started/). [The ECMAScript proposal “Temporal”](https://github.com/tc39/proposal-temporal) is a new and better date time API and currently at stage 3. It was created by [Philipp Dunkel](https://github.com/pipobscure), [Maggie Johnson-Pint](https://github.com/maggiepint), [Matt Johnson-Pint](https://github.com/mattjohnsonpint), [Brian Terlson](https://github.com/bterlson), [Shane Carr](https://github.com/sffc), [Ujjwal Sharma](https://github.com/ryzokuken), [Philip Chimento](https://github.com/ptomato), [Jason Williams](https://github.com/jasonwilliams), and [Justin Grant](https://github.com/justingrant).

This blog post has two goals:

- Giving you a feeling for how Temporal works
- Helping you get started with it

However, it is not an exhaustive documentation: For many details, you will have to consult [the (excellent) documentation for Temporal](https://tc39.es/proposal-temporal/docs/).

**Warning: These are my first explorations of this API – feedback welcome!**

---

**Table of contents:**

---

## The Temporal API  [#](https://2ality.com/2021/06/temporal-api.html?utm_source=tldrnewsletter#the-temporal-api)

The Temporal date time API is accessible via the global variable `Temporal`. It is a pleasure to use:

- All objects are immutable. Changing them produces new values, similarly to how strings work in JavaScript.
- There is support for time zones and non-Gregorian calendars.
- There are several specialized classes for Temporal values (date time values with time zones, date time values without time zones, date values without time zones, etc.). That has several benefits:
  - The context of a value (time zone or not, etc.) is easier to understand.
  - It is often more obvious how to achieve a given task.
  - `.toString()` can be used with much less consideration.
- January is month 1.

Parts of this blog post:

- The post starts with background knowledge. That will help you with the remainder of the post, but you should be fine without it.
- Next, there is an overview of all the classes of the Temporal API and how they fit together.
- At the end, there is a comprehensive section with examples.

## Background: representing time  [#](https://2ality.com/2021/06/temporal-api.html?utm_source=tldrnewsletter#background%3A-representing-time)

### From solar time to standard time  [#](https://2ality.com/2021/06/temporal-api.html?utm_source=tldrnewsletter#from-solar-time-to-standard-time)

Historically, how we measure time has progressed over the years:

- [Apparent solar time (local apparent time)](https://en.wikipedia.org/wiki/Solar_time#Apparent_solar_time): One of the earliest ways of measuring time was to base the current time on the position of the sun. For example, noon is when the sun is directly overhead.
- [Mean solar time (local mean time)](https://en.wikipedia.org/wiki/Solar_time#Mean_solar_time): This time representation corrects the variations of apparent solar time so that each day of the year has the same length.
- [Standard time](https://en.wikipedia.org/wiki/Standard_time) and time zones: Standard time specifies how the clocks within a geographical region are to be synchronized. It was established in the 19th century to support weather forecasting and train travel. In the 20th century, standard time was defined globally and geographical regions became *time zones*.

*Wall-clock time* is the current time within a time zone (as shown by a clock on the wall). Wall-clock time is also called *local time*.

### Time standards: UTC vs. Z vs. GMT  [#](https://2ality.com/2021/06/temporal-api.html?utm_source=tldrnewsletter#time-standards%3A-utc-vs.-z-vs.-gmt)

UTC, Z, and GMT are ways of specifying time that are similar, but subtly different:

- UTC (Coordinated Universal Time) is the time standard that all times zones are based on. They are specified relative to it. That is, no country or territory has UTC as its local time zone.
- Z (Zulu Time Zone) is a military time zone that is often used in aviation and the military as another name for UTC+0.
- GMT (Greenwich Mean Time) is a time zone used in some European and African countries. It is UTC plus zero hours and therefore has the same time as UTC.

Sources:

### Time zones vs. time offsets  [#](https://2ality.com/2021/06/temporal-api.html?utm_source=tldrnewsletter#time-zones-vs.-time-offsets)

Temporal’s time zones are based on [the IANA Time Zone Database (short: tz database)](https://en.wikipedia.org/wiki/Tz_database). IANA stands for Internet Assigned Numbers Authority. In that database, each time zone has an identifier and rules defining offsets for UTC times. If a time zone has standard time and daylight saving time, the offsets change during a year:

```
const standardTime = Temporal.ZonedDateTime.from({
  timeZone: 'Europe/Zurich',
  year: 1995,
  month: 11,
  day: 30,
  hour: 3,
  minute: 24,
});
assert.equal(
  standardTime.toString(),
  '1995-11-30T03:24:00+01:00[Europe/Zurich]'); // (A)

const daylightSavingTime = Temporal.ZonedDateTime.from({
  timeZone: 'Europe/Zurich',
  year: 1995,
  month: 5,
  day: 30,
  hour: 3,
  minute: 24,
});
assert.equal(
  daylightSavingTime.toString(),
  '1995-05-30T03:24:00+02:00[Europe/Zurich]'); // (B)
```

In standard time, the time offset for the `Europe/Zurich` time zone is +1:00 (line A). In daylight saving time, the time offset is +2:00 (line B).

#### Resources for working with time zones  [#](https://2ality.com/2021/06/temporal-api.html?utm_source=tldrnewsletter#resources-for-working-with-time-zones)

- [“Time Zone Database”](https://www.iana.org/time-zones) on the IANA website is a list of time zone names.
- [“List of tz database time zones”](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) on Wikipedia is another list of time zone names.
- [“Time Difference” (“Zeitverschiebung”)](https://2ality.com/2021/06/temporal-api.html?utm_source=tldrnewsletter) lists time zones for cities etc. – for example, the time zone for San Francisco is `America/Los_Angeles`.

### Calendars  [#](https://2ality.com/2021/06/temporal-api.html?utm_source=tldrnewsletter#calendars)

The calendars supported by Temporal are based on the standard [Unicode Unicode Common Locale Data Repository (CLDR)](http://cldr.unicode.org/core-spec) – among [others](https://github.com/unicode-org/cldr/blob/latest/common/bcp47/calendar.xml):

- `buddhist`: Thai Buddhist calendar
- `chinese`: Traditional Chinese calendar
- `coptic`: Coptic calendar
- `dangi`: Traditional Korean calendar
- `ethiopic`: Ethiopic calendar, Amete Mihret (epoch approx, 8 C.E.)
- `gregory`: Gregorian calendar
- `hebrew`: Traditional Hebrew calendar
- `indian`: Indian calendar
- `islamic`: Islamic calendar
- `iso8601`: ISO calendar (Gregorian calendar using the ISO-8601 calendar week rules)
- `japanese`: Japanese Imperial calendar
- `persian`: Persian calendar
- `roc`: Republic of China calendar

`iso8601` is used by most western countries and gets extra support in Temporal, via methods such as `Temporal.now.zonedDateTimeISO()` (which returns the current date and wall-clock time in the system time zone and ISO-8601 calendar).

### ECMAScript Extended ISO-8601/RFC 3339 Strings  [#](https://2ality.com/2021/06/temporal-api.html?utm_source=tldrnewsletter#ecmascript-extended-iso-8601%2Frfc-3339-strings)

The standards ISO-8601 and RFC 3339 specify how to represent dates in strings. Currently, they are missing functionality that is needed and [added by Temporal](https://tc39.es/proposal-temporal/docs/iso-string-ext.html):

- Representing month-day data as strings
- Representing IANA Time Zone Names in date time strings
- Representing calendar systems in date time strings

The goal is to eventually get these additions standardized (beyond ECMAScript).

#### Month-day syntax  [#](https://2ality.com/2021/06/temporal-api.html?utm_source=tldrnewsletter#month-day-syntax)

Month-day syntax looks like this:

```
> Temporal.PlainMonthDay.from('12-24').toString()
'12-24'
```

#### Date time strings with IANA Time Zone Names and calendar systems  [#](https://2ality.com/2021/06/temporal-api.html?utm_source=tldrnewsletter#date-time-strings-with-iana-time-zone-names-and-calendar-systems)

The following code shows what a full date time string looks like. In practice, many of these parts will often be missing:

```
const zdt = Temporal.ZonedDateTime.from({
  timeZone: 'Africa/Nairobi',
  year: 2019,
  month: 11,
  day: 30,
  hour: 8,
  minute: 55,
  second: 0,
  millisecond: 123,
  microsecond: 456,
  nanosecond: 789,
});

assert.equal(
  zdt.toString({calendarName: 'always', smallestUnit: 'nanosecond'}),
  '2019-11-30T08:55:00.123456789+03:00[Africa/Nairobi][u-ca=iso8601]');
```

Parts of the date time string in the previous example:

- Date: `'2019-11-30'`
  - year `'-'` month `'-'` day
- Separator between date and time: `'T'`
- Time: `'08:55:00.123456789'`
  - hour `':'` minute `':'` seconds
  - `'.'` (separator between seconds and fractions of a second)
  - milliseconds (3 digits)
  - microseconds (3 digits)
  - nanoseconds (3 digits)
- Time offset relative to UTC: `'+03:00'`
  - Alternative: `'Z'` which means `'+0:00'`
- Time zone: `'[Africa/Nairobi]'`
- Calendar: `'[u-ca=iso8601]'`

The last two items are not currently standardized.

## An overview of the Temporal API  [#](https://2ality.com/2021/06/temporal-api.html?utm_source=tldrnewsletter#an-overview-of-the-temporal-api)

This section gives an overview of the classes of the Temporal API. They can all be accessed via the global variable `Temporal` (`Temporal.Instant`, `Temporal.ZonedDateTime`, etc.).

Examples of using them are given after this section.

### Wall-clock time vs. exact time  [#](https://2ality.com/2021/06/temporal-api.html?utm_source=tldrnewsletter#wall-clock-time-vs.-exact-time)

Temporal distinguishes two kinds of time. Given a global instant of time:

- *Wall-clock time* (also called *local time* or *clock time*) varies globally, depending on the time zone of a clock.
- *Exact time* (also called *UTC time*) is the same everywhere.

*Epoch time* is one way of representing exact time: It’s a number counting time units (such as nanoseconds) before or since *Unix epoch* (midnight UTC on January 1, 1970).

### Creating instances of date time values  [#](https://2ality.com/2021/06/temporal-api.html?utm_source=tldrnewsletter#creating-instances-of-date-time-values)

All date and/or time classes in Temporal support two ways of direct creation.

On one hand, the constructor accepts the minimal amount of data needed to fully specify the date time value. For example, in the case of the two classes for exact time, `Instant` and `ZonedDateTime`, the time itself is specified via epoch nanoseconds.

```
const epochNanoseconds = 6046761644163000000n;
const timeZone = 'America/Los_Angeles'; // San Francisco
const zdt1 = new Temporal.ZonedDateTime(epochNanoseconds, timeZone);
assert.equal(
  zdt1.toString(),
  '2161-08-12T09:00:44.163-07:00[America/Los_Angeles]');
```

The static factory method `.from()` is overloaded. Most classes support three kinds of values for its parameter.

First, if the parameter is an instance of the same class, then that instance is cloned:

```
const zdt2 = Temporal.ZonedDateTime.from(zdt1);
assert.equal(
  zdt2.toString(),
  '2161-08-12T09:00:44.163-07:00[America/Los_Angeles]');
```

Second, all other objects are interpreted as specifying various fields with time-related information:

```
const zdt3 = Temporal.ZonedDateTime.from({
  timeZone: 'America/Los_Angeles',
  year: 2161,
  month: 8,
  day: 12,
  hour: 9,
  minute: 0,
  second: 44,
  millisecond: 163,
  microsecond: 0,
  nanosecond: 0,
});
assert.equal(
  zdt3.toString(),
  '2161-08-12T09:00:44.163-07:00[America/Los_Angeles]');
```

Third, all primitive values are coerced to string and parsed:

```
const zdt4 = Temporal.ZonedDateTime.from(
  '2161-08-12T09:00:44.163[America/Los_Angeles]'); // (A)
assert.equal(
  zdt4.toString(),
  '2161-08-12T09:00:44.163-07:00[America/Los_Angeles]'); // (B)
```

Note that we didn’t need to specify the offset in line A, but it is shown in line B.

The following table gives an overview of the date time classes:

| `Temporal.*` | Cal | Zone |
| --- | --- | --- |
| `ZonedDateTime` | ✓ | ✓ |
| ← epoch, zone, cal? |  |  |
| `Instant` | (✓) |  |
| ← epoch |  |  |
| `PlainDateTime` | ✓ |  |
| ← Y, M, D, h?, m?, s?, ms?, μs?, ns?, cal? |  |  |
| `PlainDate` | ✓ |  |
| ← Y, M, D, cal? |  |  |
| `PlainTime` |  |  |
| ← h?, m?, s?, ms?, μs?, ns? |  |  |
| `PlainYearMonth` | ✓ |  |
| ← Y, M, cal?, refIsoDay? |  |  |
| `PlainMonthDay` | ✓ |  |
| ← M, D, cal?, refIsoYear? |  |  |

Legend:

- cal: calendar
- zone: time zone
- epoch: epoch nanoseconds
- Y, M, D: ISO year, month, day
- h, m, s: ISO hour, minute, second
- ms, μs, ns: ISO milliseconds, microseconds, nanoseconds
- refIsoDay: reference ISO day, used for disambiguation when using calendars other than the ISO-8601 calendar
- refIsoYear: reference ISO year, used for disambiguation when using calendars other than the ISO-8601 calendar
- `Instant` uses an ISO-8601 calendar internally (e.g. for `.toString()`), but it is not stored in instances.

Naming:

- `Zoned` indicates an explicitly specified time zone
- `Plain` indicates that a value has no associated time zone (abstract time)

### `now`: the current time  [#](https://2ality.com/2021/06/temporal-api.html?utm_source=tldrnewsletter#now%3A-the-current-time)

The object `Temporal.now` has several factory methods for creating Temporal values representing the current time:

```
> Temporal.now.instant().toString()
'2021-06-27T12:51:10.961Z'

> Temporal.now.zonedDateTimeISO('Asia/Shanghai').toString()
'2021-06-27T20:51:10.961+08:00[Asia/Shanghai]'

> Temporal.now.plainDateTimeISO().toString()
'2021-06-27T20:51:10.961'

> Temporal.now.plainTimeISO().toString()
'20:51:10.961'
```

Properties of `Temporal.now`:

- `.timeZone()`
- `.instant()`
- `.plainDateTime(calendar, temporalTimeZoneLike?)`
- `.plainDateTimeISO(temporalTimeZoneLike?)`
- `.zonedDateTime(calendar, temporalTimeZoneLike?)`
- `.zonedDateTimeISO(temporalTimeZoneLike?)`
- `.plainDate(calendar, temporalTimeZoneLike?)`
- `.plainDateISO(temporalTimeZoneLike?)`
- `.plainTimeISO(temporalTimeZoneLike?)`

These properties are documented [here](https://tc39.es/proposal-temporal/docs/now.html).

#### Context provided by the system: time zone and calendar  [#](https://2ality.com/2021/06/temporal-api.html?utm_source=tldrnewsletter#context-provided-by-the-system%3A-time-zone-and-calendar)

We can use `Temporal.now` to access the current time zone of the system. This time zone can change – for example, when the system travels:

```
> Temporal.now.timeZone().toString()
'Asia/Shanghai'
```

Accessing the current calendar is more complicated:

```
const sysCal = new Intl.DateTimeFormat().resolvedOptions().calendar;
```

### Exact time: class `Instant`, class `ZonedDateTime`, nanoseconds since epoch  [#](https://2ality.com/2021/06/temporal-api.html?utm_source=tldrnewsletter#exact-time%3A-class-instant%2C-class-zoneddatetime%2C-nanoseconds-since-epoch)

Temporal represents exact time in three ways:

- Via class `Instant` (UTC time).
- Via class `ZonedDateTime` (wall-clock time plus a time zone and a calendar).
- Via a bigint number expressing nanoseconds since epoch.

#### Class `Instant`  [#](https://2ality.com/2021/06/temporal-api.html?utm_source=tldrnewsletter#class-instant)

Class `Instant` represents global exact time. Its time standard is UTC. It is mostly a container for nanoseconds since epoch. For some operations (such as `.toString()`), it internally uses an ISO-8601 calendar, but that calendar is not stored in instances.

Use case:

- Internal dates that are not shown to end users (time stamps in logs, etc.).

```
const instant = Temporal.now.instant();
assert.equal(
  instant.toString(),
  '2021-06-27T08:32:33.18174345Z');
```

Properties of `Instant`:

- `.from(item)`
- `.fromEpochSeconds(epochSeconds)`
- `.fromEpochMilliseconds(epochMilliseconds)`
- `.fromEpochMicroseconds(epochMicroseconds)`
- `.fromEpochNanoseconds(epochNanoseconds)`
- `.compare(one, two)`

Properties of `Instant.prototype`:

- `get .epochSeconds`
- `get .epochMilliseconds`
- `get .epochMicroseconds`
- `get .epochNanoseconds`
- `.add(temporalDurationLike)`
- `.subtract(temporalDurationLike)`
- `.until(other, options?)`
- `.since(other, options?)`
- `.round(options)`
- `.equals(other)`
- `.toString(options?)`
- `.toLocaleString(locales?, options?)`
- `.toJSON()`
- `.valueOf()`
- `.toZonedDateTime(item)`
- `.toZonedDateTimeISO(item)`

These properties are documented [here](https://tc39.es/proposal-temporal/docs/instant.html).

#### Class `ZonedDateTime`  [#](https://2ality.com/2021/06/temporal-api.html?utm_source=tldrnewsletter#class-zoneddatetime)

Class `ZonedDateTime` represents time via wall-clock time plus a time zone and a calendar.

Use cases for this class:

- Representing actual events
- Converting time between zones
- Time computations where daylight saving time may play a role (“one hour later”)

```
// Current time in Melbourne, Australia (in ISO-8601 calendar)
const zonedDateTime = Temporal.now.zonedDateTimeISO(
  'Australia/Melbourne');
assert.equal(
  zonedDateTime.toString(),
  '2021-06-27T10:46:31.179753181+10:00[Australia/Melbourne]');
```

Properties of `ZonedDateTime`:

- `.from(item, options?)`
- `.compare(one, two)`

Properties of `ZonedDateTime.prototype`:

- `get .calendar`
- `get .timeZone`
- `get .year`
- `get .month`
- `get .monthCode`
- `get .day`
- `get .hour`
- `get .minute`
- `get .second`
- `get .millisecond`
- `get .microsecond`
- `get .nanosecond`
- `get .epochSeconds`
- `get .epochMilliseconds`
- `get .epochMicroseconds`
- `get .epochNanoseconds`
- `get .dayOfWeek`
- `get .dayOfYear`
- `get .weekOfYear`
- `get .hoursInDay`
- `get .daysInWeek`
- `get .daysInMonth`
- `get .daysInYear`
- `get .monthsInYear`
- `get .inLeapYear`
- `get .offsetNanoseconds`
- `get .offset`
- `.with(temporalZonedDateTimeLike, options?)`
- `.withPlainTime(plainTimeLike?)`
- `.withPlainDate(plainDateLike)`
- `.withTimeZone(timeZoneLike)`
- `.withCalendar(calendarLike)`
- `.add(temporalDurationLike, options?)`
- `.subtract(temporalDurationLike, options?)`
- `.until(other, options?)`
- `.since(other, options?)`
- `.round(options)`
- `.equals(other)`
- `.toString(options?)`
- `.toLocaleString(locales?, options?)`
- `.toJSON()`
- `.valueOf()`
- `.startOfDay()`
- `.toInstant()`
- `.toPlainDate()`
- `.toPlainTime()`
- `.toPlainDateTime()`
- `.toPlainYearMonth()`
- `.toPlainMonthDay()`
- `.getISOFields()`

These properties are documented [here](https://tc39.es/proposal-temporal/docs/zoneddatetime.html).

### Plain (wall-clock time) classes  [#](https://2ality.com/2021/06/temporal-api.html?utm_source=tldrnewsletter#plain-(wall-clock-time)-classes)

#### Class `PlainDateTime`, `PlainDate`, `PlainTime`  [#](https://2ality.com/2021/06/temporal-api.html?utm_source=tldrnewsletter#class-plaindatetime%2C-plaindate%2C-plaintime)

If a class doesn’t have a time zone, Temporal calls it “plain”. There are three timezone-less classes: `PlainDateTime`, `PlainDate`, and `PlainTime`. They are abstract representations of time.

Use cases for these classes:

- Displaying the wall-clock time in a given time zone (see below).
- Time computations when the time zone doesn’t matter (“The first Wednesday of May 1998”).

```
const zonedDateTime = Temporal.now.zonedDateTimeISO('Asia/Novosibirsk');
assert.equal(
  zonedDateTime.toString(),
  '2021-06-27T10:46:31.179+07:00[Asia/Novosibirsk]');

// Get the wall-clock time as a string
const plainDateTime = zonedDateTime.toPlainDateTime()
assert.equal(
  plainDateTime.toString(),
  '2021-06-27T10:46:31.179');
```

Properties of `PlainDateTime`:

- `.from(item, options?)`
- `.compare(one, two)`

Properties of `PlainDateTime.prototype`:

- `get .calendar`
- `get .year`
- `get .month`
- `get .monthCode`
- `get .day`
- `get .hour`
- `get .minute`
- `get .second`
- `get .millisecond`
- `get .microsecond`
- `get .nanosecond`
- `get .dayOfWeek`
- `get .dayOfYear`
- `get .weekOfYear`
- `get .daysInWeek`
- `get .daysInMonth`
- `get .daysInYear`
- `get .monthsInYear`
- `get .inLeapYear`
- `.with(temporalDateTimeLike, options?)`
- `.withPlainTime(plainTimeLike?)`
- `.withPlainDate(plainDateLike)`
- `.withCalendar(calendar)`
- `.add(temporalDurationLike, options?)`
- `.subtract(temporalDurationLike, options?)`
- `.until(other, options?)`
- `.since(other, options?)`
- `.round(options)`
- `.equals(other)`
- `.toString(options?)`
- `.toLocaleString(locales?, options?)`
- `.toJSON()`
- `.valueOf()`
- `.toZonedDateTime(temporalTimeZoneLike, options?)`
- `.toPlainDate()`
- `.toPlainYearMonth()`
- `.toPlainMonthDay()`
- `.toPlainTime()`
- `.getISOFields()`

These properties are documented [here](https://tc39.es/proposal-temporal/docs/plaindatetime.html).

`PlainDate` and `PlainTime` have subsets of `PlainDateTime`’s properties.

#### Class `PlainYearMonth`  [#](https://2ality.com/2021/06/temporal-api.html?utm_source=tldrnewsletter#class-plainyearmonth)

An instance of `PlainYearMonth` abstractly refers to a particular month in a particular year.

Use case:

- Identifying a monthly recurring event (“the October 2020 meeting”)

```
const plainYearMonth = Temporal.PlainYearMonth.from(
  {year: 2020, month: 10});
assert.equal(
  plainYearMonth.toString(),
  '2020-10');
```

#### Class `PlainMonthDay`  [#](https://2ality.com/2021/06/temporal-api.html?utm_source=tldrnewsletter#class-plainmonthday)

An instance of `PlainMonthDay` abstractly refers to a particular day in a particular month.

Use case:

- Identifying a yearly recurring event (“Bastille Day is July 14”)

```
// Bastille Day
const bastilleDay = Temporal.PlainMonthDay.from({month: 7, day: 14});
assert.equal(
  bastilleDay.toString(),
  '07-14');

// Bastille Day in 1989 in Paris
const zonedDateTime = bastilleDay
  .toPlainDate({year: 1989})
  .toZonedDateTime('Europe/Paris');
assert.equal(
  zonedDateTime.toString(),
  '1989-07-14T00:00:00+02:00[Europe/Paris]');
```

### Helper classes  [#](https://2ality.com/2021/06/temporal-api.html?utm_source=tldrnewsletter#helper-classes)

#### `Calendar`  [#](https://2ality.com/2021/06/temporal-api.html?utm_source=tldrnewsletter#calendar)

All Temporal classes that contain full dates use calendars to help them with various computations. Most code will use the ISO-8601 calendar, but other calendar systems are supported, too.

These are three common ways of specifying calendars:

```
const pd1 = new Temporal.PlainDate(1992, 2, 24,
  'iso8601');
const pd2 = new Temporal.PlainDate(1992, 2, 24,
  {calendar: 'iso8601'});
const pd3 = new Temporal.PlainDate(1992, 2, 24,
  new Temporal.Calendar('iso8601'));
```

#### `TimeZone`  [#](https://2ality.com/2021/06/temporal-api.html?utm_source=tldrnewsletter#timezone)

Instances of `TimeZone` represent time zones. They support IANA time zones, UTC, and UTC offsets. For most use cases, IANA time zones are the best choice because they enable proper handling of daylight saving time.

These are three common ways of specifying time zones:

```
const zdt1 = new Temporal.ZonedDateTime(0n,
  'America/Lima');
const zdt2 = new Temporal.ZonedDateTime(0n,
  {timeZone: 'America/Lima'});
const zdt3 = new Temporal.ZonedDateTime(0n,
  new Temporal.TimeZone('America/Lima'));
```

#### `Duration`  [#](https://2ality.com/2021/06/temporal-api.html?utm_source=tldrnewsletter#duration)

A duration represents a length of time – for example, 3 hours and 45 minutes.

Durations are used for temporal arithmetic:

- Measuring differences between two Temporal values
- Adding time to a temporal value
- Etc.

```
const duration = Temporal.Duration.from({hours: 3, minutes: 45});
assert.equal(
  duration.total({unit: 'second'}),
  13500);
```

Note that there is no simple normalization for durations:

- Sometimes, we mean “90 minutes”.
- Sometimes, we mean “1 hour 30 minutes”.

The former should not be automatically converted to the latter.

## Examples  [#](https://2ality.com/2021/06/temporal-api.html?utm_source=tldrnewsletter#examples)

### Input and output  [#](https://2ality.com/2021/06/temporal-api.html?utm_source=tldrnewsletter#input-and-output)

#### Converting from and to strings  [#](https://2ality.com/2021/06/temporal-api.html?utm_source=tldrnewsletter#converting-from-and-to-strings)

The static factory method `.from()` always accepts strings:

```
const zdt = Temporal.ZonedDateTime.from(
  '2019-12-01T12:00:00[Pacific/Auckland]');
```

The `.toString()` method works predictably and can be configured:

```
assert.equal(
  zdt.toString(),
  '2019-12-01T12:00:00+13:00[Pacific/Auckland]');

assert.equal(
  zdt.toString({offset: 'never', timeZoneName: 'never'}),
  '2019-12-01T12:00:00');

assert.equal(
  zdt.toString({smallestUnit: 'minute'}),
  '2019-12-01T12:00+13:00[Pacific/Auckland]');
```

However, `.toString()` doesn’t let you hide minutes in this case – you have to convert the `ZonedDateTime` to a `PlainDate` if that is what you want:

```
assert.equal(
  zdt.toPlainDate().toString(),
  '2019-12-01');
```

#### Converting to and from JSON  [#](https://2ality.com/2021/06/temporal-api.html?utm_source=tldrnewsletter#converting-to-and-from-json)

All Temporal date time values have a `.toJSON()` method and can therefore be stringified to JSON:

```
const zdt = Temporal.ZonedDateTime.from(
  '2019-12-01T12:00[Asia/Singapore]');

// Stringifying a zoned date time directly:
assert.equal(
  JSON.stringify(zdt),
  '"2019-12-01T12:00:00+08:00[Asia/Singapore]"');

// Stringifying a zoned date time inside an object:
const obj = {startTime: zdt};
assert.equal(
  JSON.stringify(obj),
  '{"startTime":"2019-12-01T12:00:00+08:00[Asia/Singapore]"}');
```

If you want to parse JSON with date time values, you need to set up [a JSON reviver](https://exploringjs.com/impatient-js/ch_json.html#example-parsing-unsupported-values).

#### Converting to human-readable strings  [#](https://2ality.com/2021/06/temporal-api.html?utm_source=tldrnewsletter#converting-to-human-readable-strings)

Temporal’s support for converting date time values to human readable strings is similar to [`Intl.DateTimeFormat`’s](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat):

```
const zdt = Temporal.ZonedDateTime.from(
  '2019-12-01T12:00[Europe/Berlin]');

assert.equal(
  zdt.toLocaleString(),
  '12/1/2019, 12:00:00 PM GMT+1');

assert.equal(
  zdt.toLocaleString('de-DE'),
  '1.12.2019, 12:00:00 MEZ');

assert.equal(
  zdt.toLocaleString('en-GB', {
    weekday: 'long',
    year: 'numeric',
    month: 'long',
    day: 'numeric',
  }),
  'Sunday, 1 December 2019');
```

Temporal does not support parsing human-readable strings.

#### Converting between legacy `Date` and `Temporal`  [#](https://2ality.com/2021/06/temporal-api.html?utm_source=tldrnewsletter#converting-between-legacy-date-and-temporal)

On one hand, we can convert legacy dates to Temporal instants:

```
const legacyDate = new Date('1970-01-01T00:00:01Z');

const instant1 = legacyDate.toTemporalInstant();
assert.equal(
  instant1.toString(),
  '1970-01-01T00:00:01Z');
```

This is an alternative to the previous approach:

```
const ms = legacyDate.getTime();
const instant2 = Temporal.Instant.fromEpochMilliseconds(ms);
assert.equal(
  instant2.toString(),
  '1970-01-01T00:00:01Z');
```

On the other hand, one of the fields exposed by `Instant` provides us with the epoch time in milliseconds – which we can use to create a date:

```
const instant = Temporal.Instant.from('1970-01-01T00:00:01Z');
const legacyDate = new Date(instant.epochMilliseconds);

assert.equal(
  legacyDate.toISOString(),
  '1970-01-01T00:00:01.000Z');
```

### Working with Temporal values  [#](https://2ality.com/2021/06/temporal-api.html?utm_source=tldrnewsletter#working-with-temporal-values)

#### Using field values  [#](https://2ality.com/2021/06/temporal-api.html?utm_source=tldrnewsletter#using-field-values)

Most date time classes support a rich set of fields such as `.dayOfWeek`, `.month`, and `.calendar`. The notable exception is `Instant`, whose time zone and calendar is fixed and whose setup and state is based on epoch time.

In all other date time classes, we can use the static factory function `.from()` to configure instances:

```
const zonedDateTime = Temporal.ZonedDateTime.from({
  timeZone: 'Africa/Lagos',
  year: 1995,
  month: 12,
  day: 7,
  hour: 3,
  minute: 24,
  second: 30,
  millisecond: 0,
  microsecond: 3,
  nanosecond: 500,
});
assert.equal(
  zonedDateTime.toString(),
  '1995-12-07T03:24:30.0000035+01:00[Africa/Lagos]');
```

These and other fields are also available as properties, but these properties are immutable:

```
assert.equal(
  zonedDateTime.year,
  1995);

assert.equal(
  zonedDateTime.month,
  12);

assert.equal(
  zonedDateTime.dayOfWeek,
  4);

assert.equal(
  zonedDateTime.epochNanoseconds,
  818303070000003500n);
```

If we want to change the fields, we need to create a new value via `.with()`:

```
const newZonedDateTime = zonedDateTime.with({
  year: 2222,
  month: 3,
});
assert.equal(
  zonedDateTime.toString(),
  '1995-12-07T03:24:30.0000035+01:00[Africa/Lagos]');
```

#### Sorting dates  [#](https://2ality.com/2021/06/temporal-api.html?utm_source=tldrnewsletter#sorting-dates)

Every date time class `D` provides a function `D.compare` for sorting instances of `D`:

```
const dates = [
  Temporal.ZonedDateTime.from('2022-12-01T12:00[Asia/Tehran]'),
  Temporal.ZonedDateTime.from('2001-12-01T12:00[Asia/Tehran]'),
  Temporal.ZonedDateTime.from('2009-12-01T12:00[Asia/Tehran]'),
];
dates.sort(Temporal.ZonedDateTime.compare);
assert.deepEqual(
  dates.map(d => d.toString()),
  [
    '2001-12-01T12:00:00+03:30[Asia/Tehran]',
    '2009-12-01T12:00:00+03:30[Asia/Tehran]',
    '2022-12-01T12:00:00+03:30[Asia/Tehran]',
  ]);
```

### Converting between Temporal values  [#](https://2ality.com/2021/06/temporal-api.html?utm_source=tldrnewsletter#converting-between-temporal-values)

#### Converting `Instant` to `ZonedDateTime` and `PlainDateTime`  [#](https://2ality.com/2021/06/temporal-api.html?utm_source=tldrnewsletter#converting-instant-to-zoneddatetime-and-plaindatetime)

```
const instant = Temporal.Instant.from('1970-01-01T00:00:01Z');

const zonedDateTime = instant.toZonedDateTimeISO('Europe/Madrid');
assert.equal(
  zonedDateTime.toString(),
  '1970-01-01T01:00:01+01:00[Europe/Madrid]');

const plainDateTime1 = zonedDateTime.toPlainDateTime();
assert.equal(
  plainDateTime1.toString(),
  '1970-01-01T01:00:01');

const timeZone = Temporal.TimeZone.from('Europe/Madrid');
const plainDateTime2 = timeZone.getPlainDateTimeFor(instant);
assert.equal(
  plainDateTime2.toString(),
  '1970-01-01T01:00:01');
```

#### Converting `ZonedDateTime` to `Instant` and `PlainDateTime`  [#](https://2ality.com/2021/06/temporal-api.html?utm_source=tldrnewsletter#converting-zoneddatetime-to-instant-and-plaindatetime)

```
const zonedDateTime = Temporal.ZonedDateTime.from(
  '2019-12-01T12:00[Europe/Minsk]');

const instant = zonedDateTime.toInstant();
assert.equal(
  instant.toString(),
  '2019-12-01T09:00:00Z');

const plainDateTime = zonedDateTime.toPlainDateTime();
assert.equal(
  plainDateTime.toString(),
  '2019-12-01T12:00:00');
```

#### Converting `PlainDateTime` to `ZonedDateTime` and `Instant`  [#](https://2ality.com/2021/06/temporal-api.html?utm_source=tldrnewsletter#converting-plaindatetime-to-zoneddatetime-and-instant)

```
const plainDateTime = Temporal.PlainDateTime.from(
  '1995-12-07T03:24:30');

const zonedDateTime = plainDateTime.toZonedDateTime('Europe/Berlin');
assert.equal(
  zonedDateTime.toString(),
  '1995-12-07T03:24:30+01:00[Europe/Berlin]');

const instant = zonedDateTime.toInstant();
assert.equal(
  instant.toString(),
  '1995-12-07T02:24:30Z');
```

### Converting between time zones  [#](https://2ality.com/2021/06/temporal-api.html?utm_source=tldrnewsletter#converting-between-time-zones)

```
const source = Temporal.ZonedDateTime.from(
  '2020-01-09T02:00[America/Chicago]');
const target = source.withTimeZone('America/Anchorage');

assert.equal(
  target.toString(),
  '2020-01-08T23:00:00-09:00[America/Anchorage]');
```

### Date time arithmetic  [#](https://2ality.com/2021/06/temporal-api.html?utm_source=tldrnewsletter#date-time-arithmetic)

#### Time difference  [#](https://2ality.com/2021/06/temporal-api.html?utm_source=tldrnewsletter#time-difference)

```
const departure = Temporal.ZonedDateTime.from(
  '2017-05-08T12:55[Europe/Berlin]'); // Munich
const arrival = Temporal.ZonedDateTime.from(
  '2017-05-08T17:10[America/Los_Angeles]'); // Seattle

const flightTime = departure.until(arrival);
assert.equal(
  flightTime.toString(), 'PT13H15M');
```

#### A day after a given date  [#](https://2ality.com/2021/06/temporal-api.html?utm_source=tldrnewsletter#a-day-after-a-given-date)

```
const plainDate = Temporal.PlainDate.from('2020-03-08');
assert.equal(
  plainDate.add({days: 1}).toString(),
  '2020-03-09');
```

#### First Monday in September  [#](https://2ality.com/2021/06/temporal-api.html?utm_source=tldrnewsletter#first-monday-in-september)

To compute Labor Day (first Monday in September) for a given year, we need to figure out how many days to add to September 1 in order to get to weekday 1 (Monday).

```
const mod = (a, b) => ((a % b) + b) % b;

function getLaborDay(year) {
  const firstOfSeptember = Temporal.PlainDate.from({
    year,
    month: 9,
    day: 1,
  });
  // How many days until Monday?
  const MONDAY = 1;
  const daysToAdd = mod(MONDAY - firstOfSeptember.dayOfWeek, 7);
  return firstOfSeptember.add({days: daysToAdd});
}

assert.equal(
  getLaborDay(2021).toString(),
  '2021-09-06');
assert.equal(
  getLaborDay(2022).toString(),
  '2022-09-05');
```

## Implementations of the Temporal API  [#](https://2ality.com/2021/06/temporal-api.html?utm_source=tldrnewsletter#implementations-of-the-temporal-api)

For now, the proposal warns:

> Although this proposal's API is not expected to change, implementers of this proposal MUST NOT ship unflagged Temporal implementations until IETF standardizes timezone/calendar string serialization formats. See [#1450](https://github.com/tc39/proposal-temporal/issues/1450) for updates.

The proposal links to a polyfill. Caveat: The polyfill works well for playing with the API, but it should be considered deprecated (to be replaced by better implementations soon) and not be used in production.

## More information on the APIs `Temporal` and `Date`  [#](https://2ality.com/2021/06/temporal-api.html?utm_source=tldrnewsletter#more-information-on-the-apis-temporal-and-date)

- The official Temporal documentation is currently [hosted on GitHub](https://tc39.es/proposal-temporal/docs/), but will eventually be moved to [MDN Web Docs](https://developer.mozilla.org/en-US/).
- The legacy `Date` API is documented in [a chapter](https://exploringjs.com/impatient-js/ch_dates.html) in the book “JavaScript for impatient programmers”.
