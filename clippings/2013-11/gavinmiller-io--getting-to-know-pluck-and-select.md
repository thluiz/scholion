---
url: "http://gavinmiller.io/2013/getting-to-know-pluck-and-select/"
captured_at: "2013-11-30T23:12:53-03:00"
title: "Getting to Know Pluck and Select - Gavin Miller"
domain: "gavinmiller-io"
---

# **G**etting to Know Pluck and Select

[activerecord](http://gavinmiller.io/categories/activerecord/) , [performance](http://gavinmiller.io/categories/performance/) , [rails](http://gavinmiller.io/categories/rails/) 

Let’s take some time to get familiar with `pluck` and `select`**.** They’re two very useful methods in ActiveRecord and using both effectively can really contribute to improving performance of your app**.**

Before there was `pluck` there was `select`**.** `select` was *THE WAY* for you to query for a single field from your database**.**

|  |  |
| --- | --- |
| ``` 1 2 3 4 ``` | ``` User.select(:id).to_a  # => User Load (0.9ms)  SELECT id FROM "users" # => [#<User id: 12>, #<User id: 42>, #<User id: 1>, #<User id: 24>, #<User id: 200>, ...] ``` |

In this example, `select` creates an array of `User` models where only `id` is returned**.** (You need to include `to_a` so that the query runs, without it you’ll simply get an `ActiveRecord::Relation` object**.**)

`pluck` was a introduced in Rails 3**.**2 and with it you can perform a `select` and skip the overhead of building ActiveRecord models**.**

|  |  |
| --- | --- |
| ``` 1 2 3 4 ``` | ``` User.pluck(:id)  # => (0.9ms)  SELECT "users"."id" FROM "users" # => [12, 42, 1, 24, 200, ..., 365] ``` |

The results are nearly the same from an iteration standpoint**.** With `pluck` your results are an `Array` of integers, instead of `User` models**.** Now I can hear you saying: “Wait just a minute there**!** Both queries took 0.9ms, so there’s no difference between the two methods”**.** And to that I would reply…

Not so!

The difference is in [the cost of object construction, which Rails is hiding from you**!**](http://gavinmiller.io/2013/active-records-dirty-little-secret/)

Let’s use Benchmark to find out the real cost of `select` and `pluck`**.** For each method we’ll do 5 runs, reject the lowest and highest times, then average the 3 results**.**

|  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` puts Benchmark.measure { User.select(:id).to_a }     user    system     total        real 0.883333  0.006667  0.890000 (  1.113816) ``` |

And pluck:

|  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` puts Benchmark.measure { User.pluck(:id) }     user    system     total        real 0.043333  0.000000  0.046667 (  0.089493) ``` |

I ran the two queries across 10,000 user records, and it’s easy to see that select was 91% slower than pluck**.** For the record, both queries take the same amount of time to run, it’s the object creation that eats up that additional time with `select`

This is no big secret**.** `pluck` was introduced to remove the overhead caused by Rails object creation, which was commonly seen when running a query like this: `User.select(:id).map(&:id)`

Something I didn’t know prior to writing this post is that you can `pluck` on multiple columns**!** *(Note: that this is available as of Rails 4**.**0)*

|  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` User.pluck(:first_name, :last_name, :email) # =>   (2.2ms)  SELECT "users"."first_name", "users"."last_name", "users"."email" FROM "users" # => [[nil, nil, "jeff@gmail.com"], ['joe', nil, "joe.brown@gmail.com"], ["Edward", "Stanza", "ed@email.com"], ...] ``` |

`pluck` is however slightly different than `select` when it comes to multiple columns**.** With select you can pass `:first_name, :last_name, :email` or `[:first_name, :last_name, :email]` whereas if you pass an array to pluck it’s going to barf on you – oddly, this was a [deliberate choice](https://github.com/rails/rails/pull/6500#issuecomment-6030292)**.**

This post wouldn’t be complete without talking about the use case for `select`**.** Namely when you need to run model methods on the results that come back from `select`**.** There’s no way to do that with `pluck`**.** In one simple sentence:

> pluck for model values, select for model objects

That’s it for now**.** In the future you can look forward to regular posts on difference ways to improve the performance of your Rails application**!**

If you want to receive regular tips on improving Rails performance **add your name in the below box**:

|  |  |
| --- | --- |
| Email: |  |
| First Name: |  |

I will not sell your email address, you can unsubscribe at anytime, and I am not an affiliate for anything**.** In the event that I build or make something related to this blog, I'll send you discounts, early access, and freebies**!**

This page was delicately crafted on
Oct 20th, 2013 by Gavin Miller**.**
