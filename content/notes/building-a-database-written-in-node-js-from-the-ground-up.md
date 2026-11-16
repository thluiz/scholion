---
title: "Building a Database Written in Node.js from the Ground Up"
date: '2026-11-16T01:59:47+00:00'
category: webclip
summary: 'HarperDB says it chose Node.js because the team knew it well, it is lightweight and scalable, and npm helped speed development. The article outlines the stack, REST API, clustering, and LMDB storage.'
tags: ["nodejs", "database-architecture", "harperdb", "npm"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Building a Database Written in Node.js from the Ground Up"
    url: "https://dev.to/harperdb/building-a-database-written-in-node-js-from-the-ground-up-2hgm"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/dev-to--building-a-database-written-in-node-js-from-the-ground-up.md"
    kind: repo
---

HarperDB says it built its database in Node.js because the team already knew the language, wanted rapid development, and valued the ecosystem around npm. The article also frames Node as lightweight and scalable, while noting limits such as weaker OS and file system control and less performance than C/C++.

## Reading notes

- The founding team built the first and only database written in Node.js.
- The main reason for choosing Node was that the team already knew it well.
- The team valued Node for being lightweight, fast for development, and supported by many npm packages.
- The article lists drawbacks, including weaker control over the operating system and file system, less performance than C/C++, and the lack of native threading at the time.
- HarperDB presents its product as a REST API and says it is built as microservices with a single endpoint and POST-based operations.
- The tech stack includes a React-based Management Studio, a custom NoSQL parser, AlaSQL for SQL parsing, SocketCluster for distributed computing, and LMDB for storage.
- The Management Studio is described as a React front end built on top of the HarperDB REST API.
- The article says HarperDB uses AlaSQL and math.js to extend SQL functionality and relies on npm packages instead of building everything from scratch.
- Clustering and replication are described as peer-to-peer, fault tolerant, table-level, and based on a pub-sub model.
- HarperDB says it originally stored its exploded data model on the file system, then moved to LMDB for better performance.
- The article claims a benchmark where HarperDB was about 37 times faster than MongoDB, largely because of LMDB.
