---
url: "http://dickey.xxx/mysql-is-done-it-s-the-postgres-age"
captured_at: "2012-05-23T18:34:07-03:00"
title: "MySQL is done. It's the Postgres Age. by Jeff Dickey"
domain: "dickey-xxx"
---

# [MySQL is done. It's the Postgres Age.](http://dickey.xxx/mysql-is-done-it-s-the-postgres-age)

May 23, 2012

## [postgres](http://dickey.xxx/tags/postgres) [database](http://dickey.xxx/tags/database)

![196a38db33650ee9d56134f1583501a5.jpg](dickey-xxx--mysql-is-done-postgres-age-jeff-dickey/196a38db33650ee9d56134f1583501a5.jpg)

Postgres is a relational(-ish) database that's really starting to become the one-size-fits-all of databases. I think this is very interesting since I wouldn't have predicted this direction a year ago.

**[Schema-less data](http://schneems.com/post/19298469372/you-got-nosql-in-my-postgres-using-hstore-in-rails) , [array columns](http://www.postgresql.org/docs/9.1/static/arrays.html) , [queueing](https://github.com/ryandotsmith/queue_classic) , [full-text searching](https://github.com/Casecommons/pg_search) , geo-spatial indexing, it's insane what Postgres can do.**

I had a conversation yesterday with [Sam Stokes](http://linkedin.com/in/samstokesuk) of [Rapportive](http://rapportive.com/) . I wanted to know about their experience using Postgres. They run a pretty massive Postgres system. Sam mentioned that it's gone very well and, if he were to do it again from scratch, he would absolutely use Postgres.

Sam's not the only one, I've heard some great comments about people using Postgres for just about their entire data back-end. Even the data guys I know love Postgres.

I would say that Postgres is by far the top tool being raved about in web dev.

## Has nosql failed?

A couple years ago, I thought the nosql tools would be the future. It was really all about "using the right tool for the job". I thought this was an awesome new way of thinking. RDBs shouldn't be the go-to, but a combination of tools. Tools catered to solve the right problem.

Postgres has taken the features out of all of these tools and integrate it right inside the platform. Now you don't need to spin up a mongo cluster for non-rel data, rabbitmq cluster for queueing, solr box for searching. You can just have a single postgres server. That saves a huge ops headache since each of those clusters/boxes have to be durable, replicated, and scalable.

## The bad part of using Postgres for everything

Now obviously, there's a glaring downside with this approach: you get one box. Maybe a read slave or something, but really, you can't scale it. I don't want to get into pre-optimization here, but one Postgres box is probably fine no matter what you're doing. If a part starts to underperform, pull it out.

Making a giant distributed data system is a lot of work though. Pre-optimizing here could certainly compromise your project.

Backup is also a huge issue with a distributed system. When you have one box, you can go back into any point in time without any issues. Having even one more data system makes backup really hard. In fact, I'm not even sure how you'd do it.

MySQL has the same problem of having one box, but obviously supports none of these features.

## More awesome Postgres shit

Want more? Schema changes in Postgres can work in a transaction. Rails will use this by default.

That means that if you make a schema change and it fails, the entire thing aborts. If that happens in MySQL? You'd better have a backup handy.

Concurrent indexing. With a simple 'concurrent' flag in Postgres, you can make adding a column happen without locking the table. It takes a long time but it works.

Window functions are a feature that lets you create some awesome queries that are impossible in MySQL. It's a concept that would warrant its own article, [so here's one](http://postgresguide.com/tips/window.html) .

I also want to comment that Postgres is now breaking nearly all the database rules I was taught in college. Not BCNF, not 3NF, not 2NF, not even 1NF! (Arrays break 1NF I believe). I always thought those were stupid impractical rules anyways.

## What about MySQL?

Now to address my link-bait:

MySQL is done. There is no reason to use it anymore. The current state of Postgres blows MySQL out of the water. I don't see the MySQL community catching up either. Postgres has been solidly improving.

Performance-wise, it seems to be a wash.

I seriously want someone to tell me just ONE feature that MySQL has over Postgres. I ask everybody this question, and I haven't heard a single thing. Yes, Google and Facebook use it, but I don't really care.

## I want to use it!

If you're on Rails, you're in luck. Ryan Bates just posted a [Railscast](http://railscasts.com/episodes/342-migrating-to-postgresql) on the topic.
