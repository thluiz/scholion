---
url: "https://blog.bytebytego.com/p/interview-question-design-twitter?s=r"
captured_at: "2022-05-05T09:33:52-03:00"
title: "Interview question: Design Twitter (Episode 5)"
domain: "blog-bytebytego-com"
---

# Interview question: Design Twitter (Episode 5)

In this newsletter, we will talk about the following:

- Process vs Thread
- Interview Question: Design Twitter
- A visual guide on how to choose the right Database.
- Unique ID Generator

## Popular interview question: What is the difference between **Process** and **Thread**?

[![c3270dbf-818a-4d69-af57-c0a098986a31_2196x2319.webp](blog-bytebytego-com--interview-question-design-twitter-episode-5/75d750658a25d2d6da6c9e9252024d4e.webp)](https://cdn.substack.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fc3270dbf-818a-4d69-af57-c0a098986a31_2196x2319.png)

To better understand this question, let’s first take a look at what is a Program. A **Program** is an executable file containing a set of instructions and passively stored on disk. One program can have multiple processes. For example, the Chrome browser creates a different process for every single tab.

A **Process** means a program is in execution. When a program is loaded into the memory and becomes active, the program becomes a process. The process requires some essential resources such as registers, program counter, and stack.

A **Thread** is the smallest unit of execution within a process.

The following process explains the relationship between program, process, and thread.

1. The program contains a set of instructions.

2. The program is loaded into memory. It becomes one or more running processes.

3. When a process starts, it is assigned memory and resources. A process can have one or more threads. For example, in the Microsoft Word app, a thread might be responsible for spelling checking and the other thread for inserting text into the doc.

Main differences between process and thread:

Processes are usually independent, while threads exist as subsets of a process.

Each process has its own memory space. Threads that belong to the same process share the same memory.

A process is a heavyweight operation. It takes more time to create and terminate.

Context switching is more expensive between processes.

Inter-thread communication is faster for threads.

Over to you:

1). Some programming languages support coroutine. What is the difference between coroutine and thread?

2). How to list running processes in Linux?

## Interview Question: Design Twitter

This post is a summary of a tech talk given by Twitter in 2013. Let’s take a look.

[![30ef4280-3a20-4a59-97e0-a88da88c2674_2367x3213.webp](blog-bytebytego-com--interview-question-design-twitter-episode-5/8bdce9f67815f40e0f32c4c4e749c65e.webp)](https://cdn.substack.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F30ef4280-3a20-4a59-97e0-a88da88c2674_2367x3213.jpeg)

**The life of a Tweet**

1️⃣ A tweet comes in through the Write API.

2️⃣ The Write API routes the request to the Fanout service.

3️⃣ The Fanout service does a lot of processing and stores them in the Redis cache.

4️⃣ The Timeline service is used to find the Redis server that has the home timeline on it.

5️⃣ A user pulls their home timeline through the Timeline service.

**Search & Discovery**

Ingester: annotates and tokenizes Tweets so the data can be indexed.

Earlybird: stores search index.

Blender: creates the search and discovery timelines.

**Push Compute**

HTTP push

Mobile push

Disclaimer: This article is based on the tech talk given by Twitter in 2013 (https://bit.ly/3vNfjRp). Even though many years have passed, it’s still quite relevant. I redraw the diagram as the original diagram is difficult to read.

Over to you: Do you use Twitter? What are some of the biggest differences between LinkedIn and Twitter that might shape their system architectures?

## A visual guide on how to choose the right Database.

Picking a database is a long-term commitment so the decision shouldn’t be made lightly. The important thing to keep in mind is to choose the right database for the right job.

[![37cbc245-f68e-4588-887d-6dd61e328395_1400x1960.webp](blog-bytebytego-com--interview-question-design-twitter-episode-5/8d9a050814fb73608c8df2ffeaefca16.webp)](https://cdn.substack.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F37cbc245-f68e-4588-887d-6dd61e328395_1400x1960.png)

Data can be structured (SQL table schema), semi-structured (JSON, XML, etc.), and unstructured (Blob).

Common database categories include:

Relational

Columnar

Key-value

In-memory

Wide column

Time Series

Immutable ledger

Geospatial

Graph

Document

Text search

Blob

Thanks, [Satish Chandra Gupta](https://www.linkedin.com/feed/#)

Over to you - Which database have you used for which workload?

## Unique ID Generator

IDs are very important for the backend. Do you know how to generate globally unique IDs?

In this post, we will explore common requirements for IDs that are used in social media such as Facebook, Twitter, and LinkedIn.

Requirements:

Globally unique

Roughly sorted by time

Numerical values only

64 bits

Highly scalable, low latency

The implementation details of the algorithms can be found online so we will not go into detail here.

Over to you: What kind of ID generators have you used?

[![c002753e-36bc-4d7d-81ea-dd3183558e33_1434x1600.webp](blog-bytebytego-com--interview-question-design-twitter-episode-5/ec29957b54909706b427cf55f191f8ab.webp)](https://cdn.substack.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fc002753e-36bc-4d7d-81ea-dd3183558e33_1434x1600.png)
