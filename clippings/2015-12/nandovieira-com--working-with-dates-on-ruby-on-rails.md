---
url: "http://nandovieira.com/working-with-dates-on-ruby-on-rails"
captured_at: "2015-12-23T15:02:50-03:00"
title: "Working with dates on Ruby on Rails"
domain: "nandovieira-com"
---

# Working with dates on Ruby on Rails

December 09, 2015

Read in 8 minutes

Working with dates can be hard. You need to consider time zones, understand how to store dates in your database, parse strings into dates or even format dates and display them to the user. And there’s the daylight saving time.

In this article we’ll see how to use the utilities provided by Rails, so that your system can handle dates correctly.

## How Ruby works

Ruby has basically two different classes for handling dates: `Date` and `Time`[1](http://nandovieira.com/working-with-dates-on-ruby-on-rails#fn1). You can generate dates by parsing strings or using individual attributes that represent the year, hour, month, and so on.

```
require "time"

parse"Dec 8 2015 10:19"
#=> 2015-12-08 10:19:00 -0200

parse"Dec 8 2015"
#=> #<Date: 2015-12-08>

    
#=> 2015-12-08 10:19:00 -0200

  
#=> #<Date: 2015-12-08>
```

Every date calculation must be performed manually. Let’s say you want to advance one hour; all you have to do is add 3600 seconds to the date.

```
#=> 2015-12-08 10:26:40 -0200

  
#=> 2015-12-08 11:26:40 -0200
```

Most calculations are easy to implement, but things get complex when you have to consider time zones.

### Working with time zones

To set the time zone in a Ruby script, you have to set the `TZ` environment variable. This variable is not defined in most systems, but that will depend on how your server is configured. Older POSIX systems used this variable but this done by `/etc/localtime` now.

This is how Ruby behaves with and without the `TZ` variable.

```
#=> nil

#=> 2015-12-08 10:30:00 -0200

  "America/Los_Angeles"
#=> "America/Los_Angeles"

#=> 2015-12-08 04:30:14 -0800
```

The `date` command, available in *\*nix* systems, also use the `TZ` variable, changing how the date is presented in a user session.

```
$ date
Tue Dec  8 09:37:12 BRST 2015

$ export TZ=America/Los_Angeles

$ date
Tue Dec  8 03:37:27 PST 2015
```

The problem is that not every software out there will use this variable automatically (or use it at all). PostgreSQL won’t use the `TZ` variable, preferring the `timezone` configuration[2](http://nandovieira.com/working-with-dates-on-ruby-on-rails#fn2).

```
SELECT current_setting'timezone'
#=> Brazil
```

You’re better off avoiding the time zone in all pieces of your infrastructure; instead of using a specific time zone, just go with [Etc/UTC](http://yellerapp.com/posts/2015-01-12-the-worst-server-setup-you-can-make.html). This will free you from problems related to DST and cron jobs. It will also be easier to define how different systems will work with dates and communicate. The time zone presentation should be the application’s responsibility.

## How Ruby on Rails works

To define the time zone in Ruby on Rails application use the environment configuration file or create an initializer.

```
# config/initializers/time_zone.rb
  "America/Sao_Paulo"
```

Ruby on Rails can have a time zone configuration per application, totally ignoring the `TZ` environment variable, but this behavior has some implications.

First, Ruby won’t consider Rails’ time zone configuration. This means that if your system is using the `America/Sao_Paulo` time zone and your application is using `America/Los_Angeles`, Ruby will still consider the former configuration.

```
#=> "BRST"

  "America/Los_Angeles"
#=> "America/Los_Angeles"

#=> "BRST"
```

To generate dates that knows about the time zone, you should use methods defined by the ActiveSupport library. These methods will generate objects from the `ActiveSupport::TimeWithZone`[3](http://nandovieira.com/working-with-dates-on-ruby-on-rails#fn3) class. There are a large number of methods and their usage will depend on what you want to accomplish.

```
#=> Tue, 08 Dec 2015 03:37:57 PST -08:00

today
#=> Tue, 08 Dec 2015

current
#=> Tue, 08 Dec 2015 03:38:17 PST -08:00

#=> Tue, 08 Dec 2015 02:38:28 PST -08:00

from_now
#=> Wed, 09 Dec 2015 03:38:36 PST -08:00

yesterday
#=> Mon, 07 Dec 2015

tomorrow
#=> Wed, 09 Dec 2015
```

The general guidelines are:

- Use `Time.current` instead of `Time.now`.
- Use `Date.current` instead of `Date.today`.

Notice that `Time.current` will ignore the time zone information if your application doesn’t set it; the same will happen to `Date.current`, as you can see in ActiveSupport’s implementation:

```
# activesupport-4.2.5/lib/active_support/core_ext/time/calculations.rb
# line 30
class 
   current
        
  

# activesupport-4.2.5/lib/active_support/core_ext/date/calculations.rb
# line 46
class 
   current
      today  today
```

You can always use `Time.zone.today` and `Time.zone.now` for a deterministic result.

### Dealing with Daylight Saving Time

ActiveSupport uses the [TZInfo](https://rubygems.org/gems/tzinfo) gem so it can know about time zones. This gem will load all this information from your operating system; in Ubuntu, this information comes from the `tzdata` package.

This means that keeping your server up-to-date will provide fresh information about DST and all time zones from all around the world.

The code below shows how the dates know about DST, considering Brazil’s DST for 2016.

```
parse'2015-10-17'
#=> false

parse'2015-10-18'
#=> true

parse'2016-02-20'
#=> true

parse'2016-02-21'
#=> false
```

Sometimes you have to parse dates and DST can bring unexpected consequences. Recently I had to integrate some user-provided dates in calendar and the biggest challenge was displaying future dates, considering time zones and DST.

Turns out the solution is simple; when parsing dates, ignore the time zone information from the string and use the `Time.use_zone`.

```
current
#=> Mon, 07 Dec 2015 18:57:51 BRST -02:00

use_zone"America/Sao_Paulo" 
  starts_at  parse"2016-03-05 10:00"
  #=> Sat, 05 Mar 2016 10:00:00 BRT -03:00

  ends_at  parse"2016-03-05 17:00"
  #=> Sat, 05 Mar 2016 17:00:00 BRT -03:00
```

### How dates are persisted

ActiveRecord will persist dates in [UTC](https://en.wikipedia.org/wiki/Coordinated_Universal_Time) (Coordinated Universal Time). This behavior is defined by the `ActiveRecord::Base.default_timezone` and `ActiveRecord::Base.time_zone_aware_attributes` properties.

```
ActiveRecorddefault_timezone
#=> :utc

ActiveRecordtime_zone_aware_attributes
#=> true
```

Every time you persist an date attribute to the database, ActiveRecord will convert it to UTC. And after loading a record, ActiveRecord will do the other way around, converting the date back to the time zone defined in your application[4](http://nandovieira.com/working-with-dates-on-ruby-on-rails#fn4).

Notice that dates can be off by some hours if you use `Date.today` or `Time.now`.

```
  "America/Los_Angeles"
#=> "America/Los_Angeles"

beginning_of_day
#=> 2015-12-08 02:00:00 UTC

currentbeginning_of_day
#=> 2015-12-08 08:00:00 UTC
```

This happens because `Time.now` ignores the time zone defined by the application and will use the system’s one (in this case `BRST-0200`). That’s why is extremely important for you to use ActiveSupport methods, like I said before.

Since ActiveRecord assumes that all dates are persisted as UTC, you can also end up with wrongs dates if you update database records from outside the application. PostgreSQL has a column type that knows about time zones and will convert dates before persisting it. Unfortunately Rails doesn’t support [`time with time zone`](http://www.postgresql.org/docs/current/static/datatype-datetime.html), but you can easily add it to your application by creating an initializer with the following code:

```
# config/initializers/active_record.rb
ActiveRecordConnectionAdaptersPostgreSQLAdapter
  NATIVE_DATABASE_TYPES:datetime  name: "timestamp with time zone"
```

### Querying your database

We already know that ActiveRecord assumes your dates are stored as UTC. To make your queries work as expected, all you have to do is use dates that have this time zone knowledge (like `Time.current`) and the library will do the right thing.

```
Articlewhere"published_at >= ?" current
```

Remember that dates generated by `1.day.ago` and `Date.current.beginning_of_month` will consider the time zone, so feel free to use them.

### Parsing dates sent by users

When parsing dates you must also consider time zones. Ruby has the methods `Time.parse` and `Date.parse`, but they ignore this information. In this case you should use `Time.zone.parse` or your dates can be off by a few hours.

```
parse"8:47am Dec 7th, 2015"
#=> 2015-12-07 10:47:00 UTC

parse"8:47am Dec 7th, 2015"
#=> 2015-12-07 16:47:00 UTC
```

If you have numbers that represent the date, use `Time.zone.local` instead of `Time.new`.

```
#=> 2015-12-07 10:47:00 UTC

local     
#=> 2015-12-07 16:47:00 UTC
```

Finally, use `Time.zone.at` if you have a Unix timestamp.

```
1449506820
#=> 2015-12-07 16:47:00 UTC
```

To set the time zone for an execution context, use the method `Time.use_zone`, which sets the specified time zone only while running the block.

```
  "America/Sao_Paulo"
#=> "America/Sao_Paulo"

now_in_sao_paulo  current
#=> Tue, 08 Dec 2015 09:40:31 BRST -02:00

now_in_los_angeles  use_zone"America/Los_Angeles" 
  current

#=> Tue, 08 Dec 2015 03:40:31 PST -08:00

now_in_sao_paulo
#=> 2015-12-08 11:40:31 UTC

now_in_los_angeles
#=> 2015-12-08 11:40:31 UTC

now_in_sao_paulo  now_in_los_angeles
#=> true
```

You can use this method on your controller so you can set the user’s time zone.

```
class ApplicationController  ActionController
  around_action :set_timezone if: :logged_in?

  private

   set_timezoneaction
    use_zonecurrent_usertime_zone action
```

### Working with dates in JavaScript

You may need to communicate with your Rails application from JavaScript. The best way of dealing with dates is by using [moment.js](http://momentjs.com/).

Use the `Time#iso8601` method to send formatted dates to JavaScript; this will generate something like `2015-12-07T19:25:45Z`. You can then use moment.js to convert this string into a JavaScript `Date` object.

```
   moment"2015-12-07T19:25:45Z"
//=> Mon Dec 07 2015 17:25:45 GMT-0200 (BRST)

format"MMM DD, YYYY - h:mma"
//=> Dec 07, 2015 - 5:25pm
```

Notice that moment.js will use the browser’s time zone (`BRST-0200` in my case); if you need to convert the date to a different time zone, use [momentjs-timezone](http://momentjs.com/timezone).

## Wrapping up

If you application deals with dates, most notably date calculations, understand how Rails’ date handling works is essential. To make your life easier, just follow these rules:

- Use `Etc/UTC` as your server’s time zone.
- Always define the time zone in your Rails application, even if it’s `Etc/UTC`.
- Deal with time zone presentation on your application’s layer.
- Use `Time.current` and `Date.current` to retrieve the current date.
- Use `Time.zone.parse` para converter strings em datas.
- Convert `Date` em `ActiveSupport::TimeWithZone` for comparison, like `date.in_time_zone == Time.current.beginning_of_day`.

## Resources

---

1. There’s another class called `DateTime`, which is just a `Date` subclass that knows about the time part. The `Time` class had limitations on older Ruby versions running in 32-bit systems; in this case you should use `DateTime` instead. Ruby 1.9.2 fixed this problem and you can just use `Date` and `Time` classes, which now have [similar performance](https://gist.github.com/fnando/54ddc21c4640d09c30ce). [↩](http://nandovieira.com/working-with-dates-on-ruby-on-rails#fnref1)
2. PostgreSQL will only use the `TZ` environment variable if the `timezone` configuration is not specified on your `postgresql.conf` file. Since this configuration always have a default value, is unlikely that PostgreSQL will use `TZ` unless you really want it to. [↩](http://nandovieira.com/working-with-dates-on-ruby-on-rails#fnref2)
3. Methods like `Time.zone.today`, `Date.yesterday` and `Date.tomorrow` return objects from the `Date` class and don’t know about time zone. Convert the `Date` object into a `ActiveSupport::TimeWithZone` instance with `date.in_time_zone`. [↩](http://nandovieira.com/working-with-dates-on-ruby-on-rails#fnref3)
4. The `ActiveRecord::Base.time_zone_aware_attributes` configuration is disabled if you’re using ActiveRecord outside Rails. [↩](http://nandovieira.com/working-with-dates-on-ruby-on-rails#fnref4)
