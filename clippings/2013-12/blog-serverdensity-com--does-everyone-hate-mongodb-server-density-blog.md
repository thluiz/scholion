---
url: "https://blog.serverdensity.com/does-everyone-hate-mongodb/"
captured_at: "2013-12-11T09:29:29-03:00"
title: "Does everyone hate MongoDB? - Server Density Blog"
domain: "blog-serverdensity-com"
---

# Does everyone hate MongoDB**?**

![f3606eb0c1914f4998bdd78b6746115e.jpg](blog-serverdensity-com--does-everyone-hate-mongodb-server-density-blog/f3606eb0c1914f4998bdd78b6746115e.jpg)

Written by David Mytton

For a guaranteed surge of traffic and to hit the Hacker News homepage, all you need to do is write about why you hate MongoDB and/or migrated to some other database**.** We’ve been using it to power our server monitoring service, [Server Density](http://www.serverdensity.com) , for over 3 years now and so with experience, many of the problems cited in these posts seem like basic mistakes in deployment and understanding**.**

With any product, if you decide to deploy it to production you need to be sure you fully understand its architecture and scaling profile**.** This is even more important with newer products like MongoDB because there is less community knowledge and understanding**.** This is partly the responsibility of the developers using those tools but also the responsibility of the vendor to ensure that major gotchas are highlighted**.**

[When we originally switched to MongoDB](https://blog.serverdensity.com/choosing-a-non-relational-database-why-we-migrated-from-mysql-to-mongodb/)  back in 2009 one of the plus points was the detailed documentation**.** It’s even more detailed now and [there is a large project underway rewriting the existing wiki docs](http://docs.mongodb.org/manual/) **.** 10gen, the company behind MongoDB, also run huge numbers of [conferences](http://www.10gen.com/events)  around the world so others can share knowledge, offer commercial training, free webinars and recently announced [free online courses](http://education.10gen.com/) **.**

However, there seem to have been quite a few “don’t use MongoDB” posts over the last few months so is there actually a real problem with MongoDB itself**?** Let’s take a look at a few of them to see what the issues were:

**[I’ll Give MongoDB Another Try**.** In Ten Years](http://diegobasch.com/ill-give-mongodb-another-try-in-ten-years)  – 24 Sept 2012**

**Headline problem**: Deployed on 32 bit server so was limited to 2GB database**.** Writes were being silently discarded**.**

**Mistake**: Deployed to 32 bit servers without knowledge of the limit**.** Did not use safe writes and didn’t check for errors after writes**.**

**Comments**: The [32 bit limit](http://blog.mongodb.org/post/137788967/32-bit-limitations)  is noted (perhaps it should be a warning) on the [download page](http://www.mongodb.org/downloads)  but the main problem was the author did not know when writes started to fail**.** MongoDB uses unsafe writes by default in the sense that from the driver, you do not know if the write has succeeded without a further call to getLastError**.** This is because one of the often cited use cases for MongoDB is fast writes, which is achieved by fire and forget queries**.**

There has been much discussion about whether this is a sensible default and here we’ve seen someone caught out by this**.** I’ve spoken to quite a few people who didn’t understand this so if it isn’t to be changed, the documentation should highlight it**.** [The PHP docs do this](http://php.net/manual/en/mongo.writes.php)  but the quick start tutorials for Ruby and Python don’t**.** With 10gen controlling all official drivers, this inconsistence could be rectified**.**

Many suggest this default is a good way to get favourable benchmarks [but there are no official ones](http://www.mongodb.org/display/DOCS/Benchmarks)  so I don’t think that’s relevant**.**

**[Migrating to Riak at Shareaholic](http://blog.shareaholic.com/2012/08/migrating-to-riak-at-shareaholic/)  – 31 Aug 2012**

**Problems**: Working set needs to fit into memory, global write lock blocks all queries, slave replication not hot**.**

**Comments**: Getting your working set in memory is one of the most difficult things to calculate and plan for with MongoDB**.** There are currently no tools and no visibility from Mongo itself as to which collections are queried the most and there are few hints into what should be considered the working set**.** This has to be estimated based on your understanding of your query patterns and by looking at the slow query log for queries not hitting indexes, no indexes or seeing which queries produce slower responses (figuring out your working set through inference)**.**

A general guideline is to provide as much RAM as you can to fit all your data plus indexes or if that’s not possible, at least your indexes**.** But this isn’t much different from other databases – the more memory the better and disk i/o is bad ([mitigated by using SSDs](https://blog.serverdensity.com/mongodb-performance-ssds-vs-spindle-sas-drives/) )**.** There was no further clarification of how this is different in Riak, which they migrated to**.**

The global lock in MongoDB <= 2**.**0 is an oft-cited problem and pre 2.0 it was an issue that required workarounds, such as throttling of inserts**.** The way MongoDB yielded [was improved in 2.0 in a very significant way](http://blog.pythonisito.com/2011/12/mongodbs-write-lock.html)  and this was [taken further in 2**.**2 with the complete removal of the global lock](https://blog.serverdensity.com/goodbye-global-lock-mongodb-2-0-vs-2-2/)  as a step towards more granular concurrency**.** Saying “that’s fixed in the latest version” is only partly acceptable in the sense that new users don’t need to be worried about this any more but even for older users, we found the problem was usually exaggerated**.**

Keeping your replicas “hot” is also a difficult problem not unique to MongoDB**.** Indeed, [the recent Github outages included a similar problem with MySQL](https://github.com/blog/1261-github-availability-this-week) **.** This can be worked around by sending queries to your slaves or by [using the new touch command in 2**.**2](http://docs.mongodb.org/manual/reference/commands/#touch) (previously you could do this in the filesystem before starting MongoDB)**.**

**[From MongoDB to Riak](http://devblog.bu.mp/from-mongodb-to-riak-7138)  – 14 May 2012**

This post doesn’t explain why they moved from MongoDB other than some general hand waving about “operational qualities”:

> Now we no longer care if one of the nodes kernel panics in the middle of the night; as has happened a few times already**.** Nagios will email us instead of page us, and over coffee the next morning we’ll fire up IPMI, reboot the machine, and Riak will read-repair as necessary**.** No longer will we have to do any master-slave song and dance, nor will we fret about performance, capacity, or scalability; if we need more, we’ll just add nodes to the cluster**.**

This seems to imply they had problems with the replication in MongoDB, in particular how failover happens**.** We’ve found that replica sets in MongoDB are a very robust way to handle replication and automated failover**.** We rarely have instances fail but when they have (and when we regularly test failover), this is generally seemless**.** Failover happens very quickly (within seconds) and all the drivers we use to connect MongoDB handle this internally by reconnecting to the new master**.** This triggers an alert and we then investigate what happened**.**

We have also found we can easily scale MongoDB either vertically by adding more resources (memory, SSDs) or by adding new shards**.** Adding a new shard requires some work to get a new replica set deployed but with all our servers managed using Puppet this doesn’t actually take long**.**

**[A year with MongoDB](http://blog.engineering.kiip.me/post/20988881092/a-year-with-mongodb)  – April 2012**

**Problems** Non-counting b-trees, memory management, uncompressed field names, global write lock, safe off by default, table compaction, hot slaves**.**

**Comments** Using OS memory management has its advantages such as maintaining the cache through process restarts and leaving the OS to decide what is best with knowledge of the whole system, but it does mean that some optimisations can’t be implemented by the database itself**.** I don’t have enough knowledge of the internals to comment further but this can go back to the comments above regarding the difficulties of calculating the working set**.**

Uncompressed field names is [a problem I’ve written about in the past](https://blog.serverdensity.com/on-shortened-field-names-in-mongodb/)  and is an issue for huge data sets where you’re trying to optimise memory usage (working set) because those duplicated field names can take up a significant amount of space**.**

Compaction remains a problem if you do a large volume of inserts and removes**.** [Compaction](http://docs.mongodb.org/manual/reference/command/compact/)  is a manual process and blocks (on a database rather than server level in 2**.**2). MongoDB uses a [padding factor](http://docs.mongodb.org/manual/reference/glossary/#term-padding-factor) if you do a lot of updates to avoid having to move the data on disk but you may need to consider strategies such as pre-populating documents if you know they are going to be updated/grown in the future**.**

**[Goodbye MongoDB](http://www.zopyx.de/blog/goodbye-mongodb)  – no date**

This post is much more of a rant rather than a reasoned technical analysis of why certain things do not work**.** A number of the points are covered above but some are just wrong**.** For example:

> It is still not possible to express arbitrary queries like in SQL using JSON**.** One would argue: not needed – but in reality there are always cases where you need more complex queries**.** The only way around is to implement something client-side or use the server-side JS code execution (single-threaded, slow)**.** Having no option to perform an operation comparable to UPDATE table SET foo=bar WHERE…**.** (which is possibly a low-hanging fruit).

This is [the update query](http://www.mongodb.org/display/DOCS/Updating#Updating-update%28%29) with the multi parameter set to `true`**.**

There is also a complaint about map/reduce which has historically been a weak point due to the single threaded JS engine**.** New in MongoDB 2**.**2 is the [aggregation framework](http://docs.mongodb.org/manual/aggregation/)  which is supposed to offer an easy introduction to analysis of data, although not a map/reduce replacement**.** I have not used this so cannot comment further on map/reduce**.**

**Conclusions**

For Server Density, MongoDB has been an excellent tool**.** We really understand how it works and it works very well**.** We use it for many different things including storing historical time series data for server metrics, our core app data store and for simple queuing**.** It’s also benefited us on a marketing front as we have grown with new MongoDB releases and have been able to talk about them at conferences and user groups**.**

As more and more people use a technology there will be those who make mistakes, get burnt or find use cases where it’s not suitable**.** I think that categorises all of the “MongoDB hate” posts and many of the problems are solved in newer versions so need not concern people thinking about using MongoDB for new projects**.** When you switch technologies it’s often a valid reason at the time but with the fast paced development, such issues are often fixed in the next release**.**

Both MongoDB and 10gen are incredibly successful with a huge number of deployments, large and small, so what we’re really seeing the [hype cycle](https://en.wikipedia.org/wiki/Hype_cycle)  in action rather than everyone hating MongoDB**.**

![fec980ed357f28f6cc8250e8422b2585.jpg](blog-serverdensity-com--does-everyone-hate-mongodb-server-density-blog/fec980ed357f28f6cc8250e8422b2585.jpg)
