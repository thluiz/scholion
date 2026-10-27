---
title: "Does everyone hate MongoDB?"
date: '2013-12-11T09:29:29-03:00'
category: webclip
summary: 'The post argues that many MongoDB complaints come from deployment mistakes, missing documentation, or issues already fixed in newer releases, while Server Density says MongoDB has worked well for its own use cases.'
tags: ["mongodb", "database-operations", "replication"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Does everyone hate MongoDB? - Server Density Blog"
    url: "https://blog.serverdensity.com/does-everyone-hate-mongodb/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2013-12/blog-serverdensity-com--does-everyone-hate-mongodb-server-density-blog.md"
    kind: repo
---

The post argues that many “don’t use MongoDB” stories reflect deployment mistakes, weak understanding of MongoDB’s architecture, or problems that newer versions have already addressed. It also says documentation and driver guidance should make important defaults and limits more visible.

## Reading notes

- MongoDB is presented as a system that needs careful understanding of its architecture and scaling profile before production use.
- The post says some criticism comes from basic mistakes in deployment and understanding rather than from MongoDB itself.
- It says the company behind MongoDB provides detailed documentation, events, training, webinars, and free online courses.
- In one cited case, a 32-bit server limited the database to 2GB, and writes were silently discarded because safe writes were not used and errors were not checked.
- The post says MongoDB uses unsafe writes by default in the sense that a driver does not confirm success without calling getLastError.
- It says the documentation should make that default clearer, and notes that PHP docs do this while Ruby and Python quick starts do not.
- In another case, the post says the working set is hard to estimate and that MongoDB offers little visibility into which collections are queried most.
- It says a common guideline is to provide enough RAM for all data plus indexes, or at least for the indexes.
- It says the global lock in MongoDB <= 2.0 was a real issue earlier, but was improved in 2.0 and removed in 2.2.
- It says hot replicas are a difficult problem for many databases, not only MongoDB.
- The post says replica sets handle replication and automated failover robustly in the author’s experience.
- It says failover happens within seconds and drivers reconnect to the new master automatically.
- It says MongoDB can be scaled vertically with more resources or horizontally by adding shards.
- It says uncompressed field names can waste space on large datasets where memory use matters.
- It says compaction is a manual process and can block, so update patterns may require planning.
- It says one complaint about arbitrary queries is addressed by the update query with the multi parameter set to true.
- It says map/reduce has been a weak point historically, and that MongoDB 2.2 adds an aggregation framework.
- The conclusion is that MongoDB has worked well for Server Density for historical time series data, core app data, and simple queuing.
- It frames much of the backlash as part of a hype cycle, not as proof that everyone hates MongoDB.
