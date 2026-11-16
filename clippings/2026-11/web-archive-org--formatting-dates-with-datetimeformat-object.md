---
url: "https://web.archive.org/web/20200613140219id_/https://thewebdev.info/2020/01/12/formatting-dates-with-the-datetimeformat-object/"
captured_at: "2026-11-16T07:55:54+00:00"
title: "Formatting Dates With the DateTimeFormat Object - The Web Dev"
domain: "web-archive-org"
---

Different parts of the world have different date formats. To deal with this, JavaScript has the `Intl.DateTimeFormat` constructor to let us format dates into different formats according to different locales.

This means that we can format dates for different places without manipulating date strings ourselves, making our lives much easier. The `Intl.DateTimeFormat` constructor takes a locale string as the argument.

With the `DateTimeFormat` constructed with the constructor, we can use the `format` instance method, which takes in a `Date` object to return a date string with the date formatted for the locale you specified in the `Intl.DateTimeFormat` constructor.

* * *

## The Constructor and the Format Method

To use the `Intl.DateTimeFormat` constructor, we can use it like in the following example:

```
const date = new Date(2019, 0, 1, 0, 0, 0);  
console.log(new Intl.DateTimeFormat('en-US').format(date));  
console.log(new Intl.DateTimeFormat('fr-ca').format(date));  
console.log(new Intl.DateTimeFormat(['ban', 'de']).format(date));
```

In the above example, we created the `Date` object, and then we used the `Intl.DateTimeFormat` constructor with one or more locales passed in as a string.

Then, we called `format` by passing in the `Date` object. The first example would log `1/1/2019` since the United States use the MM/DD/YYYY date format.

The second example would log `2019–01–01` since French Canadian dates are in YYYY-MM-DD format. The third example takes an array where there are multiple locales, the ones further to the right are the fallback locales for the ones for the left.

In our example, since we have an invalid locale string `ban` in the first entry of the array, we use the German date format `de` instead, to format the `Date` object, so we get `1.1.2019` since Germany uses the DD.MM.YYYY date format.

As we can see from the examples above, the `Intl.DateTimeFormat` constructor takes a locale string or an array of locale strings. It also accepts Unicode extension keys for locale strings, so that we can append them to our language tag.

The extension keys `nu` for setting the numbering system, `ca` for the calendar to format the date, and `hc` for the hour cycle are supported.

`nu`’s possible values can be `arab`, `arabext`, `bali`, `beng`, `deva`, `fullwide`, `gujr`, `guru`, `hanidec`, `khmr`, `knda`, `laoo`, `latn`, `limb`, `mlym`, `mong`, `mymr`, `orya`, `tamldec`, `telu`, `thai`, `tibt`.

`ca`’s possible values include `buddhist`, `chinese`, `coptic`, `ethiopia`, `ethiopic`, `gregory`, `hebrew`, `indian`, `islamic`, `iso8601`, `japanese`, `persian`, `roc`.

`hc`’s possible values include `h11`, `h12`, `h23`, `h24`. For example, to format dates according to the Buddhist calendar, we can write:

```
const date = new Date(2019, 0, 1, 0, 0, 0);  
console.log(new Intl.DateTimeFormat('en-US-u-ca-buddhist').format(date));
```

Then we get `1/1/2562` in the `console.log` since the Buddhist calendar’s year 0 is at 545 BC.

The second argument takes an object that lets us set various options in its properties to format the date.

The `localeMatcher` option specifies the locale-matching algorithm to use. The possible values are `lookup` and `best fit`. The lookup algorithm searches for the locale until it finds the one that fits the character set of the strings that are being compared.

`best fit` finds the locale that is at least, but possibly more, suited than the `lookup` algorithm. The `timeZone` option lets us set the time zone which formats the date.

The most basic implementation only recognizes UTC, but others may recognize IANA time zone names in the IANA time zone data database, like `Asia/Shanghai`, `Asia/Kolkata`, `America/New_York`.

The `hour12` option specifies whether the format is for 12-hour time or 24-hour time. The default is locale dependent. It overrides the `hc` language tag in the first argument.

It’s a `true` or `false` value where `true` means format the date time with 12-hour time. The `hourCycle` option has possible values of `h11`, `h12`, `h23`, `h24` and overrides the `hc` language tag. `hour12` takes precedence over this option if it’s specified.

The `formatMatcher` property specifies the matching algorithm to use. Possible values are `basic` and `best fit`. `best fit` is the default value.

The following subsets of the date time are required to match the date object to the correct format:

*   `weekday`, `year`, `month`, `day`, `hour`, `minute`, `second`
*   `weekday`, `year`, `month`, `day`
*   `year`, `month`, `day`
*   `year`, `month`
*   `month`, `day`
*   `hour`, `minute`, `second`
*   `hour`, `minute`

`weekday` represents the weekday value, possible values are:

*   `long` (e.g., `Friday`)
*   `short` (e.g., `Fri`)
*   `“narrow`" (e.g., `T`). Note that two weekdays may have the same narrow style for some locales. For example, `Tuesday`‘s narrow style is also `T`.

`era` represents the era, possible values are:

*   `long` (e.g., `Anno Domini`)
*   `short` (e.g., `AD`)
*   `narrow` (e.g., `A`)

`year` represents the year. The possible values are:

*   `numeric` (e.g., `2019`)
*   `2-digit` (e.g., `19`)

`month` is the representation of the month. The possible values are:

*   `numeric` (e.g., `2`)
*   `2-digit` (e.g., `02`)
*   `long` (e.g., `February`)
*   `short` (e.g., `Feb`)
*   `narrow` (e.g., `M`). Note that two months may have the same narrow style for some locales (e.g. `May`‘s narrow style is also `M`).

`day` represents the day. Possible values are:

*   `numeric` (e.g., `2`)
*   `2-digit` (e.g., `02`)

`hour` is the representation of the hour. The possible values are `numeric`, `2-digit`.

`minute` is the representation of the minute. The possible values are `numeric`, `2-digit`.

`second` is the representation of the second. The possible values are `numeric`, `2-digit`.

`timeZoneName` is the representation of the time zone name. The possible values are:

*   `long` (e.g., `Pacific Standard Time`)
*   `short` (e.g., `GMT-8`)

The default value for each component property above is `undefined`, but if all components are `undefined` then the `year`, `month`, and `day` are assumed to be `numeric`.

An example for using the options is below:

```
const date = new Date(2019, 0, 1, 0, 0, 0);  
const options = {  
  weekday: 'long',  
  year: 'numeric',  
  month: 'long',  
  day: 'numeric'  
};  
console.log(new Intl.DateTimeFormat('en-ca', options).format(date));
```

In the code above, we set the locale to Canadian English, and in the `options` object we set `weekday` to `long`, `year` to `numeric`, `month` to `long`, and `day` to `numeric`, so that we get the full weekday name in English, year as a number, month with the full name, and `day` as a number.

The `console.log` will log “Tuesday, January 1, 2019”. The example above can have a time zone added to it, as in the following example:

```
const date = new Date(2019, 0, 1, 0, 0, 0);  
const options = {  
  weekday: 'long',  
  year: 'numeric',  
  month: 'long',  
  day: 'numeric',  
  timeZone: 'America/Vancouver',  
  timeZoneName: 'long'  
};  
console.log(new Intl.DateTimeFormat('en-ca', options).format(date));
```

In the example above, we added the `timeZone` and `timeZoneLong` so that we get the time zone displayed, so that we get “Tuesday, January 1, 2019, Pacific Standard Time”.

The `Intl.DateTimeFormat` constructor handles non-English format equally well. For example, if we want to format a date into Chinese, we can change the locale and keep the options the same as above like in the following code:

```
const date = new Date(2019, 0, 1, 0, 0, 0);  
const options = {  
  weekday: 'long',  
  year: 'numeric',  
  month: 'long',  
  day: 'numeric',  
  timeZone: 'America/Vancouver',  
  timeZoneName: 'long'  
};  
console.log(new Intl.DateTimeFormat('zh-Hant', options).format(date));
```

Then, we get “2019年1月1日 星期二 太平洋標準時間”, which is the same as “Tuesday, January 1, 2019, Pacific Standard Time” in traditional Chinese.

* * *

## Other Instance Methods

Instances of the `Intl.DateTimeFormat` constructor object also have a few instance methods in addition to the `format()` method.

It also has the `formatToParts()` method to return an array of objects representing different parts of the date string. The `resolvedOptions()` method returns a new object with properties that reflect the locale and formatting options that we computed during the initialization of the object.

The `formatRange()` method accepts two `Date` objects as arguments and formats the date range in the most concise way, based on the locale and options provided when we instantiate the `DateTimeFormat` object.

Finally, it has the `formatRangeToParts()` method which accepts two `Date` objects as arguments and formats the date range in the most concise way based on the locale and options provided when we instantiate the `DateTimeFormat` object and return the date time parts in an array of objects.

For example, if we have the following code that calls the `formatRangeToParts()` method:

```
const startDate = new Date(2019, 0, 1, 0, 0, 0);  
const endDate = new Date(2019, 0, 2, 0, 0, 0);  
const options = {  
  weekday: 'long',  
  year: 'numeric',  
  month: 'long',  
  day: 'numeric',  
  timeZone: 'America/Vancouver',  
  timeZoneName: 'long'  
};  
const dateRange = new Intl.DateTimeFormat('zh-Hant', options).formatRangeToParts(startDate, endDate)  
console.log(dateRange);
```

Then we get the following date and time parts logged:

```
[  
  {  
    "type": "year",  
    "value": "2019",  
    "source": "startRange"  
  },  
  {  
    "type": "literal",  
    "value": "年",  
    "source": "startRange"  
  },  
  {  
    "type": "month",  
    "value": "1",  
    "source": "startRange"  
  },  
  {  
    "type": "literal",  
    "value": "月",  
    "source": "startRange"  
  },  
  {  
    "type": "day",  
    "value": "1",  
    "source": "startRange"  
  },  
  {  
    "type": "literal",  
    "value": "日 ",  
    "source": "startRange"  
  },  
  {  
    "type": "weekday",  
    "value": "星期二",  
    "source": "startRange"  
  },  
  {  
    "type": "literal",  
    "value": " ",  
    "source": "startRange"  
  },  
  {  
    "type": "timeZoneName",  
    "value": "太平洋標準時間",  
    "source": "startRange"  
  },  
  {  
    "type": "literal",  
    "value": " – ",  
    "source": "shared"  
  },  
  {  
    "type": "year",  
    "value": "2019",  
    "source": "endRange"  
  },  
  {  
    "type": "literal",  
    "value": "年",  
    "source": "endRange"  
  },  
  {  
    "type": "month",  
    "value": "1",  
    "source": "endRange"  
  },  
  {  
    "type": "literal",  
    "value": "月",  
    "source": "endRange"  
  },  
  {  
    "type": "day",  
    "value": "2",  
    "source": "endRange"  
  },  
  {  
    "type": "literal",  
    "value": "日 ",  
    "source": "endRange"  
  },  
  {  
    "type": "weekday",  
    "value": "星期三",  
    "source": "endRange"  
  },  
  {  
    "type": "literal",  
    "value": " ",  
    "source": "endRange"  
  },  
  {  
    "type": "timeZoneName",  
    "value": "太平洋標準時間",  
    "source": "endRange"  
  }  
]
```

As we can see from the console output above, we get the date and time parts in each entry of the array, with the parts of the `startDate` coming first and the `endDate` parts being in the latter parts of the array.

If we call the `formatRange()` method, like in the code below:

```
const startDate = new Date(2019, 0, 1, 0, 0, 0);  
const endDate = new Date(2019, 0, 2, 0, 0, 0);  
const options = {  
  weekday: 'long',  
  year: 'numeric',  
  month: 'long',  
  day: 'numeric',  
  timeZone: 'America/Vancouver',  
  timeZoneName: 'long'  
};  
const dateRange = new Intl.DateTimeFormat('en', options).formatRange(startDate, endDate)  
console.log(dateRange);
```

Then we get:

```
"Tuesday, January 1, 2019, Pacific Standard Time – Wednesday, January 2, 2019, Pacific Standard Time"
```

From the `console.log`.

To call the `resolvedOptions` method, we can write the code below:

```
const date = new Date(2019, 0, 1, 0, 0, 0);  
const options = {  
  weekday: 'long',  
  year: 'numeric',  
  month: 'long',  
  day: 'numeric',  
  timeZone: 'America/Vancouver',  
  timeZoneName: 'long'  
};  
const resolvedOptions = new Intl.DateTimeFormat('en', options).resolvedOptions(date)  
console.log(resolvedOptions);
```

Then we get the options that we passed in for formatting the date back:

```
{  
  "locale": "en",  
  "calendar": "gregory",  
  "numberingSystem": "latn",  
  "timeZone": "America/Vancouver",  
  "weekday": "long",  
  "year": "numeric",  
  "month": "long",  
  "day": "numeric",  
  "timeZoneName": "long"  
}
```

In the `console.log`.

To use the `formatToParts()` method, we can use it like the `format()` method, like in the following code:

```
const date = new Date(2019, 0, 1, 0, 0, 0);  
const options = {  
  weekday: 'long',  
  year: 'numeric',  
  month: 'long',  
  day: 'numeric',  
  timeZone: 'America/Vancouver',  
  timeZoneName: 'long'  
};  
const dateParts = new Intl.DateTimeFormat('en', options).formatToParts(date)  
console.log(dateParts);
```

Then we get the parts of the formatted date in the `console.log` like in the output below:

```
[  
  {  
    "type": "weekday",  
    "value": "Tuesday"  
  },  
  {  
    "type": "literal",  
    "value": ", "  
  },  
  {  
    "type": "month",  
    "value": "January"  
  },  
  {  
    "type": "literal",  
    "value": " "  
  },  
  {  
    "type": "day",  
    "value": "1"  
  },  
  {  
    "type": "literal",  
    "value": ", "  
  },  
  {  
    "type": "year",  
    "value": "2019"  
  },  
  {  
    "type": "literal",  
    "value": ", "  
  },  
  {  
    "type": "timeZoneName",  
    "value": "Pacific Standard Time"  
  }  
]
```

As we can see, the `Intl.DateTimeFormat` constructor is very useful for formatting dates for different locales. It eliminates a lot of hassle when formatting dates.

The constructor takes one or more locales as the first argument and a variety of options as the second argument.

It can format dates into one string and also format them and break them up into parts. This saves a lot of hassle when formatting dates for different regions since we don’t have to do any date string manipulation.
