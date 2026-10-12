---
url: "http://www.omniref.com/blog/blog/2014/02/18/whats-relevant-in-the-ruby-universe/?utm_source=rubyweekly&utm_medium=email"
captured_at: "2014-03-05T11:04:27-03:00"
title: "What's relevant in the Ruby Universe? - The Omniref Blog"
domain: "omniref-com"
---

# What's Relevant in the Ruby Universe?

Code doesn’t live in a vacuum, and documentation shouldn’t either. Today we’re releasing the largest update to our indexing system since launch — a nearly complete re-write of our code analysis pipeline that allows us to accurately infer cross references and make symbol resolutions that no other Ruby tool can match.

### (Re)inventing the Ruby universe

[RDoc](http://www.omniref.com/ruby/gems/rdoc) and [YARD](http://www.omniref.com/ruby/gems/yard) only consider the code within a single gem, so in order to cross-reference documentation for all gems, we need to build the full object graph linking all ruby code. To build the graph, we parse the classes/methods/modules for every ruby gem with all their relationships and serialize that data into a normalized, compressed and clustered 25GB table. It takes a few thousand machine hours to parse all the ruby code, so we built a cluster to handle the job.

Concurrently building all the docs gets more complex when you add shared dependency resolution. For example if 2 workers are building ActiveModel and ActionPack, which both depend on ActiveSupport (like 10,298 other gems), one will build the dependency and the other requeues its job and finds a new gem to work on in the meantime. In addition, there’s the usual subtlety to avoid deadlocks and races since the winner of a race winds up with broken links. There’s also fun with circular dependencies, and then you have to realize if a pathological gem is ever going to finish parsing, so you can decide what to do with its dependencies.

Ruby has a relatively complex grammar, so traversing the object graph efficiently makes for an interesting relational algebra exercise. Instead, we efficiently deserialize the relevant piece of the graph for any given gem, and traverse it in memory to check if every word in documentation is in fact a symbol reference (within that specific piece of documentations local context of course).

As our CS professors used to rant, there’s no such thing as a compiled or interpreted language, only implementations. It sounds strange to say, but we now have a (limited) implementation of a distributed ruby compiler and linker.

[![c059f5cb97add079b1a1a7bd2e8576f7.jpg](omniref-com--whats-relevant-in-the-ruby-universe/c059f5cb97add079b1a1a7bd2e8576f7.jpg)](http://www.omniref.com/blog/images/carina08_hst.jpg)

"If you wish to make an apple pie from scratch, you must first invent the universe." - Carl Sagan

### Apple Pie tastes so good

We’ve started sifting through the full web of ruby code, to find signals for the most important pieces, and wanted to share a few of the early insights we’ll be rolling into better search quality.

#### The most popular runtime dependencies

It looks like we’re not the only ones who’ve gotten used to all of activesupport’s goodies regardless of which project we’re working on. It’s being used 20% more than [rails](http://rubyonrails.org/). It’s also interesting to see that activerecord [3.0](http://www.omniref.com/ruby/gems/activerecord/3.0.0/) is still the most popular dependency of other gems, over [3.1](http://www.omniref.com/ruby/gems/activerecord/3.1.0/), [3.2](http://www.omniref.com/ruby/gems/activerecord/3.2.0/) or [4.0](http://www.omniref.com/ruby/gems/activerecord/4.0.0/). It’s also pretty clear that ruby works well for data transformation projects, good libraries like json and [nokogiri](http://nokogiri.org/) make it so much less of a chore than it used to be.

#### The most included modules

I loved [DataMapper](http://datamapper.org/), and it’s still a surprisingly popular ORM. It’s been EOL for a few years now, so that may have helped concentrate all dependencies on the last version available. This list is also dominated by web dev staples like XML parsing and networking.

#### The most inherited classes

It goes without saying that `Object` comes out way ahead, but it’s interesting to see that `Exception` classes in ruby are getting heavy usage. Also, just about every major version of `ActiveRecord::Base` shows up on this list sooner rather than later, but overall usage is broadly distributed among the different versions.

#### The most overridden methods

Ruby is popular for its dynamic programming, so it’s no surprise that `method_missing` is #1 and `respond_to?` makes an appearance on this list. It’s also good to see people writing plenty of tests for the insanity that too much meta programming can create. When tests fail, it looks like plenty of people fall back to printf debugging with `to_s` and `inspect`.

### Features a la mode (aka scope creep)

Thanks to this work, we’ve added some great new stuff to Omniref: for starters, you’ll now see the full ancestry of a class listed in the heading (e.g. check out `Slim::Interpolation` to see that it eventually inherits from `Temple::HTML::Filter` in the temple gem, and then `Object` defined in the standard library.)

We can also take things a step further, and now inline documentation from one library into others where it’s relevant. For example, `ActiveRecord::Base` includes modules from it’s sister gem, `ActiveModel::SecurePassword` and `ActiveModel::Conversion`, which are defined in a different gem, but you don’t need to worry about that — We’ve rendered the full public API on a [single page](http://www.omniref.com/ruby/gems/activerecord/4.0.2/classes/ActiveRecord::Base) so you won’t have to hunt for the relevant docs.
