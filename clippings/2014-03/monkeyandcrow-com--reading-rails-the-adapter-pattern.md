---
url: "http://monkeyandcrow.com/blog/reading_rails_the_adapter_pattern/?utm_source=rubyweekly&utm_medium=email"
captured_at: "2014-03-05T11:04:25-03:00"
title: "Reading Rails - The Adapter Pattern - Monkey and Crow"
domain: "monkeyandcrow-com"
---

# Reading Rails - The Adapter Pattern

![5ee5b4afad61cb6dc62d01d41cc2523b.png](monkeyandcrow-com--reading-rails-the-adapter-pattern/5ee5b4afad61cb6dc62d01d41cc2523b.png)

Author:
:   Adam Sanderson

Published:
:   2014-02-25

Series:
:   [Reading Rails](http://monkeyandcrow.com/series/reading_rails/)
    (1 of 9)

  
  
This article references [Rails 4.0.2](https://github.com/rails/rails/tree/98d06c6bd4eefeeb342d05116fccefa11875cb9b). *Some code snippets have been abbreviated for clarity.*

Today instead of reading a specific piece of code, we're going to do a survey of a common design pattern implemented by Rails, the [Adapter Pattern](http://en.wikipedia.org/wiki/Adapter_pattern). This isn't exhaustive by any means, but I hope to highlight some practical examples.

To follow along, open each library in your editor with [qwandry](https://github.com/adamsanderson/qwandry), or just look it up on [Github](https://github.com/rails/rails/tree/5505c1d700f17e2009e1189a7aa6dafafe7062a4).

## The Adapter Pattern

I feel like 90% of my Java code was writing Adapters.

The [Adapter Pattern](http://en.wikipedia.org/wiki/Adapter_pattern) can be used to wrap different interfaces, and provide a uniform one, or make one object look like another type of object. In statically typed languages, this is often required to satisfy the type system, but in more loosely typed languages like Ruby, we aren't forced to use it. All the same, it has plenty of value for us.

When using third party classes or libraries, we often start out fine:

```
def find_nearest_restaurant(locator)
  locator.nearest(:restaurant, self.lat, self.lon)
end
```

We assume one interface for `locator`, but what if we want `find_nearest_restaurant` to support another library? We might be tempted to add a special case:

```
def find_nearest_restaurant(locator)
  if locator.is_a? GeoFish
    locator.nearest(:restaurant, self.lat, self.lon)
  elsif locator.is_a? ActsAsFound
    locator.find_food(:lat => self.lat, :lon => self.lon)
  else
    raise NotImplementedError, "#{locator.class.name} is not supported."
  end
end
```

  
  
The road to hell is lined with quick fixes, but so is the road to deploying.

This is a pragmatic solution. Perhaps we will never support another library. Perhaps `find_nearest_restaurant` is the only place we use a `locator`.

What happens if you need to support a new `locator` though? Now you have three special cases. What if you need to implement `find_nearest_hospital`? Now you have two places where you need to maintain these special cases. When you reach the point where this becomes untenable, you should consider the Adapter Pattern.

In this case, we could write `GeoFish` and `ActsAsFound` adapters so the rest of our code doesn't need to know which library we are using:

```
def find_nearest_hospital(locator)
  locator.find :type => :hospital, 
               :lat => self.lat, 
               :lon => self.lon
end

locator = GeoFishAdapter.new(geo_fish_locator)
find_nearest_hospital(locator)
```

Enough with the contrived examples, let's see some real code.

## MultiJSON

Follow along:  
 `qw multi_json`

ActiveSupport's JSON decoding uses MultiJSON, an adapter for JSON libraries. Each library parses JSON, but does so slightly differently. Let's look at adapters for [oj](https://github.com/ohler55/oj) and [yajl](https://github.com/brianmario/yajl-ruby).

```
module MultiJson
  module Adapters
    class Oj < Adapter
      #...
      def load(string, options={})
        options[:symbol_keys] = options.delete(:symbolize_keys)
        ::Oj.load(string, options)
      end
      #...
```

The Oj Adapter modifies the `options` hash, translating `:symbolize_keys` to Oj's `:symbol_keys` option using `Hash#delete`:

```
options = {:symbolize_keys => true}
options[:symbol_keys] = options.delete(:symbolize_keys) # => true 
options                                                 #=> {:symbol_keys=>true}
```

This is a convenient way to update a Hash in place if you need to adapt options.

Next MultiJSON calls `::Oj.load(string, options)`. MultiJSON's adapted API is quite similar to Oj's, so not much is going on here. Did you notice how Oj was referenced though? `::Oj` references the top level `Oj` class instead of `MultiJson::Adapters::Oj`.

Now let's look at how MultiJSON adapts the Yajl library:

```
module MultiJson
  module Adapters
    class Yajl < Adapter
      #...
      def load(string, options={})
        ::Yajl::Parser.new(:symbolize_keys => options[:symbolize_keys]).parse(string)
      end
      #...
```

This adapter implements `load` differently. With Yajl, a parser instance is created, and `Yajl::Parser#parse` is called on the string. The options hash is also handled a little differently. The only option passed to Yajl is `:symbolize_keys`.

These JSON adapters may look trivial, but they allow you to switch between libraries without having to update every place you parse JSON.

## ActiveRecord

Follow along:  
 `qw activerecord`

JSON libraries tend to follow very similar patterns, which makes adapting them fairly easy. What if you are dealing with something more complex? ActiveRecord contains adapters for several databases. Although PostgreSQL and MySQL are both SQL databases, there are many differences between them that ActiveRecord hides using the Adapter Pattern.

Look in ActiveRecord's `lib/connection_adapters` directory; there are adapters for PostgreSQL, MySQL, and SQLite. There is also an `AbstractAdapter`, which serves as the base class for each specific adapter. The `AbstractAdapter` implements common functionality found in most databases and is customized by subclasses such as the `PostgreSQLAdapter` and the `AbstractMysqlAdapter`, which in turn acts as a common parent for two different MySQL adapters, the `MysqlAdapter` and `Mysql2Adapter`. Let's see how this all fits together with a few real world examples.

PostgreSQL and MySQL implement slightly different dialects SQL. While a `SELECT * FROM users` will behave the same in both databases, there are subtle differences in how they handle some types. The time format in MySQL and PostgreSQL is slightly different. While PostgreSQL supports microseconds, MySQL has only [recently supported](http://dev.mysql.com/doc/refman/5.6/en/fractional-seconds.html) them in a stable release. How do the two adapters handle this discrepancy?

ActiveRecord quotes dates using the `quoted_date` helper in `ActiveRecord::ConnectionAdapters::Quoting`, which is mixed into the `AbstractAdapter`. The `AbstractAdapter`'s implementation just formats the date:

```
def quoted_date(value)
  #...
  value.to_s(:db)
end
```

  
  
Curious?  
 `qw activesupport` and look at `core_ext/time/conversions.rb`

Rails' ActiveSupport extends `Time#to_s` to accept a symbol representing a named format. The `:db` format is `%Y-%m-%d %H:%M:%S`:

```
# Examples of common formats:
Time.now.to_s(:db)      #=> "2014-02-19 06:08:13"
Time.now.to_s(:short)   #=> "19 Feb 06:08"
Time.now.to_s(:rfc822)  #=> "Wed, 19 Feb 2014 06:08:13 +0000"
```

None of the MySQL adapters override `quoted_date`, so they will all get this behavior. The `PostgreSQLAdapter` however makes two changes to the date:

```
def quoted_date(value)
  result = super
  if value.acts_like?(:time) && value.respond_to?(:usec)
    result = "#{result}.#{sprintf("%06d", value.usec)}"
  end

  if value.year < 0
    result = result.sub(/^-/, "") + " BC"
  end
  result
end
```

  
  
Curious about `acts_like?`  
`qw activesupport` and read `core_ext/object/acts_like.rb`

It starts off by calling `super`, so it will get a date formatted just like MySQL. Next it checks to see if the `value` is similar to a time. This is a special method ActiveSupport has added which various `Time` like classes will return `true` to. This makes it easier to declare that various objects should be assumed to be similar to a `Time`.

The second half of the condition checks to see if the `value` has a `usec` method, which returns microseconds. If microseconds are available then they are tacked onto the end of the result string using `sprintf`. Just as there are multiple time formats, there are many different ways of formatting numbers with `sprintf`:

```
sprintf("%06d", 32) #=> "000032"
sprintf("%6d",  32) #=> "    32"
sprintf("%d",   32) #=> "32"
sprintf("%.2f", 32) #=> "32.00"
```

Finally, if the date is negative, the `PostgreSQLAdapter` will reformat it to add "BC", which is indeed required for PostgreSQL:

```
SELECT '2000-01-20'::timestamp;   
-- 2000-01-20 00:00:00
SELECT '2000-01-20 BC'::timestamp;
-- 2000-01-20 00:00:00 BC
SELECT '-2000-01-20'::timestamp;
-- ERROR:  time zone displacement out of range: "-2000-01-20"
```

This is just one tiny way that ActiveRecord adapts multiple APIs, but prevents you from having to worry about many of the details in different databases.

Another way SQL databases differ is in how tables are created. Primary keys are treated differently in MySQL and PostgreSQL:

```
# AbstractMysqlAdapter
NATIVE_DATABASE_TYPES = {
  :primary_key => "int(11) DEFAULT NULL auto_increment PRIMARY KEY",
  #...
}

# PostgreSQLAdapter
NATIVE_DATABASE_TYPES = {
  primary_key: "serial primary key",
  #...
}
```

Both adapters understand ActiveRecord's notion of a `primary_key`, but they translate that into different SQL when creating a new table. Next time you write a migration, or run a query think about ActiveRecord's adapters and all the little things they deal with for you.

## DateTime and Time

Follow along:  
 `qw activesupport`

While MultiJson and ActiveRecord implement traditional adapters, Ruby's flexibility allows another solution. `DateTime` and `Time` both represent instants in time, but they handle it differently internally. The APIs they expose are similar, though there are subtle differences:

```
t = Time.now
t.day     #=> 19         (Day of month)
t.wday    #=> 3          (Day of week)
t.usec    #=> 371552     (Microseconds)
t.to_i    #=> 1392871392 (Epoch secconds)

d = DateTime.now
d.day     #=> 19         (Day of month)
d.wday    #=> 3          (Day of week)
d.usec    #=> NoMethodError: undefined method `usec'
d.to_i    #=> NoMethodError: undefined method `to_i'
```

ActiveSupport smooths some of these differences away by directly modifying the `DateTime` and `Time` classes by adding the missing methods. For instance, here is how ActiveSupport defines `DateTime#to_i`:

```
class DateTime
  def to_i
    seconds_since_unix_epoch.to_i
  end

  def seconds_since_unix_epoch
    (jd - 2440588) * 86400 - offset_in_seconds + seconds_since_midnight
  end

  def offset_in_seconds
    (offset * 86400).to_i
  end

  def seconds_since_midnight
    sec + (min * 60) + (hour * 3600)
  end
end
```

Each of the support methods, `seconds_since_unix_epoch`, `offset_in_seconds`, and `seconds_since_midnight` use or extend `DateTime`'s existing API to add methods that match those of `Time`.

If the adapters we looked at previously are external to the objects being adapted, then this could be considered an internal adapter. Unlike an external adapter though, this approach works within the confines of the existing API, and can lead to some awkward inconsistencies. For instance `DateTime` and `Time` still behave differently under some circumstances:

```
datetime == time #=> true 
datetime + 1     #=> 2014-02-26 07:32:39
time + 1         #=> 2014-02-25 07:32:40
```

While adding 1 to a `DateTime` increments by a day, adding 1 to a `Time` increments by a second. ActiveSupport layers on a variety of methods like `change` and the `Duration` value class which provide unified behavior as long as you remember to use them.

Is this a good pattern? It certainly is a convenient, but as we've seen you still need to be aware of some differences.

## Recap

Design patterns aren't just for Java. Rails uses the Adapter Pattern to provide a uniform interface for JSON parsing and database manipulation. Due to Ruby's flexibility, classes such as `DateTime` and `Time` can be directly modified to provide more similar interfaces. The Rails source is a great place to find real world examples of various design patterns.

We also saw a few interesting bits of code along the way:

- `hash[:foo] = hash.delete(:bar)` is a handy way to rename Hash entries.
- Calling `::ClassName` references the top level class.
- ActiveSupport adds an optional format argument to `Time`, `Date`, and other classes.
- `sprintf` can be used to format numbers.

Curious?  
 `qw activesupport` and look at `xml_mini.rb`

Want to see more? Go back and look at how MultiJson handles formatting as well as parsing. Peruse the ActiveRecord adapter for the database of your choice. Peek inside ActiveSupport's `XmlMini` for xml adapters that are similar to the JSON adapters in MultiJson. There's plenty to learn out there.

## Enjoyed this article?

[Read 8 more articles](http://monkeyandcrow.com/series/reading_rails/) in Reading Rails.

[← Reading Rails - Errors and Validators](http://monkeyandcrow.com/blog/reading_rails_errors_and_validators/ "Reading Rails - Errors and Validators")
