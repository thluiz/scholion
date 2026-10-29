---
url: "http://blog.diatomenterprises.com/remove-n1-queries-in-your-ruby-on-rails-app/"
captured_at: "2015-11-04T09:16:15-03:00"
title: "Remove N+1 queries in your Ruby on Rails app"
domain: "blog-diatomenterprises-com"
---

# Remove N+1 queries in your Ruby on Rails app

### Introduction

Ever wondered why your page loads slower than it should when you do simple data representation or iteration over a bunch of data? One answer might be that you have the N+1 problem which slows your page significantly. But what is that N+1 problem and how to resolve it? That is what we will take a look at.

---

### Example setup

For this post we will be using this database structure [@gist](https://gist.github.com/GuskiS/a59553704682c5f44da1) and this seed data [@gist](https://gist.github.com/GuskiS/9bbedd09db2d9d1a7b0d).

---

### N+1 problem

N+1 query problem is a situation when you are making an extra call(s) to database when you want to get a specific associated data over and over again. For example:

```
irb(main):001:0> .all.each { |item| item.category.title }  
    (.ms)  SELECT "items".*  "items"
  Category  (.ms)  SELECT  "categories".*  "categories" WHERE "categories". = ? LIMIT   [[, ]]
  Category  (.0ms)  SELECT  "categories".*  "categories" WHERE "categories". = ? LIMIT   [[, ]]
  Category  (.0ms)  SELECT  "categories".*  "categories" WHERE "categories". = ? LIMIT   [[, ]]
  Category  (.0ms)  SELECT  "categories".*  "categories" WHERE "categories". = ? LIMIT   [[, ]]
  Category  (.0ms)  SELECT  "categories".*  "categories" WHERE "categories". = ? LIMIT   [[, ]]
  Category  (.0ms)  SELECT  "categories".*  "categories" WHERE "categories". = ? LIMIT   [[, ]]
```

This example gets all items, then iterates each of those records and tries to get items category from database. Imagine this happening for 50 or 100 items, and when category model would be fatter.

---

### Common solutions

Most common solution is to use eager loading methods:

###### preload

Preload is default case for #includes method - it creates two separate queries, one for main query and other for associated data. That means we can't add #where({ categories: { title: "Fruits" } }), it will raise an error.

```
irb(main):001:0> .preload(:category).all.each { |item| item.category.title }  
    (.ms)  SELECT "items".*  "items"
  Category  (.ms)  SELECT "categories".*  "categories" WHERE "categories".  (, )
```

Example will load all items with preloaded category.

###### includes

Instead of #preload, #includes choses to make one query based on situation - if you add associated #where clause. This will make more complex SQL query:

```
irb(main):001:0> .includes(:category).where(categories: { title: 'Fruits' }).each { |item| item.category.title }  
   (.ms)  SELECT "items".  t0_r, "items"."title"  t0_r1, "items"."description"  t0_r2, "items"."price"  t0_r3, "items"."category_id"  t0_r4, "categories".  t1_r, "categories"."title"  t1_r1, "categories"."description"  t1_r2  "items"  OUTER  "categories"  "categories". = "items"."category_id" WHERE "categories"."title" = ?  [["title", "Fruits"]]
```

Example will load only items with preloaded category which title is Fruits.   
You can also force #includes to make one query with #references(using LEFT OUTER JOIN) method:

```
irb(main):001:0> .includes(:category).references(:categories).each { |item| item.category.title }  
   (.ms)  SELECT "items".  t0_r, "items"."title"  t0_r1, "items"."description"  t0_r2, "items"."price"  t0_r3, "items"."category_id"  t0_r4, "categories".  t1_r, "categories"."title"  t1_r1, "categories"."description"  t1_r2  "items"  OUTER  "categories"  "categories". = "items"."category_id"
```

###### eager\_load

This method is the same as combination of #includes and #references as it makes one query with LEFT OUTER JOIN:

```
irb(main):001:0> .eager_load(:category).each { |item| item.category.title }  
   (.ms)  SELECT "items".  t0_r, "items"."title"  t0_r1, "items"."description"  t0_r2, "items"."price"  t0_r3, "items"."category_id"  t0_r4, "categories".  t1_r, "categories"."title"  t1_r1, "categories"."description"  t1_r2  "items"  OUTER  "categories"  "categories". = "items"."category_id"
```

These are most common N+1 occurrences and they quite easy to notice if you take a look in Rails console logs but there some that don't look like this or are harder to notice.

---

### Other solutions

These solutions/workarounds I have gathered fixing project that had a lot of N+1 issues or many equal queries.

###### Count/sum/max/etc. with a dynamic condition

A lot of places I saw this or similar code:

```
specific_date_wrong(date)  
  .where("DATE(expire_at) = ?", date).count
```

and then called in a single page for the whole month, so 30 queries to get the count for each day. Dumb, if you ask me. This can be fixed with simple grouping:

```
specific_date_right(date)  
  @specific_date ||= .group('DATE(expire_at)').count
  @specific_date[date] ||
```

it will create instance variable with hash where keys are dates and values are occurrences. All that with one query.

###### Join multiple queries into one

There might be queries that can't be grouped but can be joined in SQL level. When it comes to complicated things, ActiveRecord isn't the thing you should be counting on. Instead, use plain SQL to get needed things from a database (be careful, if in future you decide to change database type, this might not work anymore).   
Silly example what I mean:

```
  .where(validated: ).count
  .where(validated: false).count
  .sum(:count_1)
  .sum(:count_2)
  .sum(:count_3)
  .sum(:count_4)
```

which can be written in one query:

```
Item.select("count(case when validated = 't' then 1 else null )  valid, count(  validated =      )  invalid")  
  .select("(count_1)  total_1, (count_2)  total_2, (count_3)  total_3, (count_4)  total_4")
  .take
```

It is a bit more complicated or messier, but that is how SQL rolls. Calling #attributes method on previous will show that it has attributes we aliased.

---

### Bullet

There is gem called bullet that helps finding N+1 queries in your application during development mode by showing you notifications in browser. Bullet will tell you when you need to eager load something or on the other hand - when you don't need to. You can find more about bullet at [github](https://github.com/flyerhzm/bullet).

---

### Summing it up

ActiveRecord is easy to learn tool for making Rails applications but it still requires you to know some things before writing fast pages. These examples are what I have gathered. Share your thoughs and examples which you are using day-to-day programming.
