---
url: "http://blog.diatomenterprises.com/remove-n1-queries-in-your-ruby-on-rails-app/"
captured_at: "2015-11-03T12:04:18-03:00"
title: "Remove N+1 queries in your Ruby on Rails app"
domain: "blog-diatomenterprises-com"
---

# Remove N+1 queries in your Ruby on Rails app

28 October 2015 on [ruby on rails](http://blog.diatomenterprises.com/tag/ruby-on-rails/), [N+1](http://blog.diatomenterprises.com/tag/n1/), [queries](http://blog.diatomenterprises.com/tag/queries/), [ActiveRecord](http://blog.diatomenterprises.com/tag/activerecord/), [bullet gem](http://blog.diatomenterprises.com/tag/bullet-gem/), [solutions](http://blog.diatomenterprises.com/tag/solutions/)

### Introduction

Ever wondered why your page loads slower than it should when you do simple data representation or iteration over a bunch of data? One answer might be that you have the N+1 problem which slows your page significantly. But what is that N+1 problem and how to resolve it? That is what we will take a look at.

---

### Example setup

For this post we will be using this database structure [@gist](https://gist.github.com/GuskiS/a59553704682c5f44da1) and this seed data [@gist](https://gist.github.com/GuskiS/9bbedd09db2d9d1a7b0d).

---

### N+1 problem

N+1 query problem is a situation when you are making an extra call(s) to database when you want to get a specific associated data over and over again. For example:

```
irb(main):001:0> Item.all.each { |item| item.category.title }  
  Item Load (0.9ms)  SELECT "items".* FROM "items"
  Category Load (0.1ms)  SELECT  "categories".* FROM "categories" WHERE "categories"."id" = ? LIMIT 1  [["id", 1]]
  Category Load (0.0ms)  SELECT  "categories".* FROM "categories" WHERE "categories"."id" = ? LIMIT 1  [["id", 1]]
  Category Load (0.0ms)  SELECT  "categories".* FROM "categories" WHERE "categories"."id" = ? LIMIT 1  [["id", 1]]
  Category Load (0.0ms)  SELECT  "categories".* FROM "categories" WHERE "categories"."id" = ? LIMIT 1  [["id", 2]]
  Category Load (0.0ms)  SELECT  "categories".* FROM "categories" WHERE "categories"."id" = ? LIMIT 1  [["id", 2]]
  Category Load (0.0ms)  SELECT  "categories".* FROM "categories" WHERE "categories"."id" = ? LIMIT 1  [["id", 2]]
```

This example gets all items, then iterates each of those records and tries to get items category from database. Imagine this happening for 50 or 100 items, and when category model would be fatter.

---

### Common solutions

Most common solution is to use eager loading methods:

###### preload

Preload is default case for #includes method - it creates two separate queries, one for main query and other for associated data. That means we can't add #where({ categories: { title: "Fruits" } }), it will raise an error.

```
irb(main):001:0> Item.preload(:category).all.each { |item| item.category.title }  
  Item Load (0.9ms)  SELECT "items".* FROM "items"
  Category Load (0.1ms)  SELECT "categories".* FROM "categories" WHERE "categories"."id" IN (1, 2)
```

Example will load all items with preloaded category.

###### includes

Instead of #preload, #includes choses to make one query based on situation - if you add associated #where clause. This will make more complex SQL query:

```
irb(main):001:0> Item.includes(:category).where(categories: { title: 'Fruits' }).each { |item| item.category.title }  
  SQL (0.2ms)  SELECT "items"."id" AS t0_r0, "items"."title" AS t0_r1, "items"."description" AS t0_r2, "items"."price" AS t0_r3, "items"."category_id" AS t0_r4, "categories"."id" AS t1_r0, "categories"."title" AS t1_r1, "categories"."description" AS t1_r2 FROM "items" LEFT OUTER JOIN "categories" ON "categories"."id" = "items"."category_id" WHERE "categories"."title" = ?  [["title", "Fruits"]]
```

Example will load only items with preloaded category which title is Fruits.   
You can also force #includes to make one query with #references(using LEFT OUTER JOIN) method:

```
irb(main):001:0> Item.includes(:category).references(:categories).each { |item| item.category.title }  
  SQL (0.1ms)  SELECT "items"."id" AS t0_r0, "items"."title" AS t0_r1, "items"."description" AS t0_r2, "items"."price" AS t0_r3, "items"."category_id" AS t0_r4, "categories"."id" AS t1_r0, "categories"."title" AS t1_r1, "categories"."description" AS t1_r2 FROM "items" LEFT OUTER JOIN "categories" ON "categories"."id" = "items"."category_id"
```

###### eager\_load

This method is the same as combination of #includes and #references as it makes one query with LEFT OUTER JOIN:

```
irb(main):001:0> Item.eager_load(:category).each { |item| item.category.title }  
  SQL (0.1ms)  SELECT "items"."id" AS t0_r0, "items"."title" AS t0_r1, "items"."description" AS t0_r2, "items"."price" AS t0_r3, "items"."category_id" AS t0_r4, "categories"."id" AS t1_r0, "categories"."title" AS t1_r1, "categories"."description" AS t1_r2 FROM "items" LEFT OUTER JOIN "categories" ON "categories"."id" = "items"."category_id"
```

These are most common N+1 occurrences and they quite easy to notice if you take a look in Rails console logs but there some that don't look like this or are harder to notice.

---

### Other solutions

These solutions/workarounds I have gathered fixing project that had a lot of N+1 issues or many equal queries.

###### Count/sum/max/etc. with a dynamic condition

A lot of places I saw this or similar code:

```
def specific_date_wrong(date)  
  Item.where("DATE(expire_at) = ?", date).count
end
```

and then called in a single page for the whole month, so 30 queries to get the count for each day. Dumb, if you ask me. This can be fixed with simple grouping:

```
def specific_date_right(date)  
  @specific_date ||= Item.group('DATE(expire_at)').count
  @specific_date[date] || 0
end
```

it will create instance variable with hash where keys are dates and values are occurrences. All that with one query.

###### Join multiple queries into one

There might be queries that can't be grouped but can be joined in SQL level. When it comes to complicated things, ActiveRecord isn't the thing you should be counting on. Instead, use plain SQL to get needed things from a database (be careful, if in future you decide to change database type, this might not work anymore).   
Silly example what I mean:

```
  Item.where(validated: true).count
  Item.where(validated: false).count
  Item.sum(:count_1)
  Item.sum(:count_2)
  Item.sum(:count_3)
  Item.sum(:count_4)
```

which can be written in one query:

```
Item.select("count(case when validated = 't' then 1 else null end) as valid, count(case when validated = 'f' then 1 else null end) as invalid")  
  .select("sum(count_1) as total_1, sum(count_2) as total_2, sum(count_3) as total_3, sum(count_4) as total_4")
  .take
```

It is a bit more complicated or messier, but that is how SQL rolls. Calling #attributes method on previous will show that it has attributes we aliased.

---

### Bullet

There is gem called bullet that helps finding N+1 queries in your application during development mode by showing you notifications in browser. Bullet will tell you when you need to eager load something or on the other hand - when you don't need to. You can find more about bullet at [github](https://github.com/flyerhzm/bullet).

---

### Summing it up

ActiveRecord is easy to learn tool for making Rails applications but it still requires you to know some things before writing fast pages. These examples are what I have gathered. Share your thoughs and examples which you are using day-to-day programming.

#### [Edvards Lazdāns](http://blog.diatomenterprises.com/author/edvards-lazdans/)

Read [more posts](http://blog.diatomenterprises.com/author/edvards-lazdans/) by this author.

#### Share this post

[](https://twitter.com/share?text=Remove%20N%2B1%20queries%20in%20your%20Ruby%20on%20Rails%20app&url=http://blog.diatomenterprises.com/remove-n1-queries-in-your-ruby-on-rails-app/)
[](https://www.facebook.com/sharer/sharer.php?u=http://blog.diatomenterprises.com/remove-n1-queries-in-your-ruby-on-rails-app/)
[](https://plus.google.com/share?url=http://blog.diatomenterprises.com/remove-n1-queries-in-your-ruby-on-rails-app/)
