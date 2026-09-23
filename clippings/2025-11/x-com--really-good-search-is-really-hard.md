---
url: "https://x.com/abh1a0/status/1993033150323392720?utm_source=tldrnewsletter"
captured_at: "2025-11-27T16:22:52+00:00"
title: "Abhi on X: \"Really Good Search is Really Hard\" / X"
domain: "x-com"
---

Really Good Search is Really Hard

I designed a multi-tenant search engine that allows for intelligent queries in milliseconds, across constantly changing documents. This write-up outlines the process of building Index, a system for agent-oriented retrieval over dynamic corpora.

# Background

## Context

Search systems aren't built for agents, they're built for humans. This is because humans adapt. They build mental models of the search space they are exploring, find boundaries, spot inconsistencies and remember how to work around them, and refine their work over time.

AI doesn't do any of that. Agents search across a corpus without intuition, and each search does not build further understanding about that corpus they're working within. Even deeper research agents, such as OpenAI's, create a search trajectory, searching across variety of keywords and context to determine what the user is looking for. Models also have a tendency to hallucinate, get lost, or return results they may deem accurate, as they have no mental model or memory of that corpus. This may work for less complex systems, or for corpora that have millions of documents where a difference of a few words is inconsequential.

However, our use case does not have that liberty. We need agents to search across thousands of documents, and rely on the corpus for the right ideas.

We can't rely both on the user to have the right information, nor on the model to have the right memory or trajectory. We are required to build a system that can return the most accurate result (or set of results) regardless of the scale of the search. And lastly, we're building a consumer-facing application, so latency is a major factor. Unlike deep research tasks that have the liberty to take minutes, we only have milliseconds to make sure we get a result and proceed.

## Meaning

Document search is also less structured. We can't build link graphs the way Google indexes webpages, as documents may not have explicit relationships between content. We can't rely on structural information the way coding tools like Cursor tokenize programs.

Inherently, a user's knowledge is fragmented across journal entries, lecture notes, files, and more, and none of it comes with popularity or memory as the searcher (the AI) needs to proactively know what they want.

A purely semantic approach might return the right concept from the wrong overall file, which would mess with what the model sees, while full-text search might miss more abstract concepts entirely. With this much ambiguity, a system that supports hybrid search matters.

## Problems

Lastly, here are some constraints that we have to fulfill:

- Speed - We need to consistently optimize for the fastest possible solution in the search path, and optimize for low-latency retrieval under concurrency.
- Accuracy Across Ambiguity - The system must provide the most relevant result, even when the same concept exists across multiple sets of unstructured files. The system cannot rely on the document providing any insight, and it cannot rely on the agents knowing how to search it.
- Multi-Tenant Boundaries - We need to be easily able to search across a user's profile, or a user and their group, or a group and the web, or communities, all at the same time with no performance drop off (tying back to Speed).
- Global Latency - We serve users worldwide, and agents can run anywhere. We need to run as much of the system as close to the users as possible.
- Constant Change - Documents update as you add content, share them with friends, publish them, and many more. This constant change is more difficult across multiple databases, meaning we need to maintain some ground source of truth.

Thus, we needed a search system that could return the most accurate result in milliseconds, across fragmented, multi-tenant data, without relying on structure, emotional language, or other noisy signals.

# Problem Solving

## Storage

When deciding on the solution, I didn't immediately go for a dedicated vector database. The following were the issues that I had to resolve:

1. Metadata as first-class - We need the most optimal ways to reduce our search space, whether that be across partitions or columns. SQL gives us highly optimized and native operations for filtering at the database level before any vector computations, which helps us optimize beyond what dedicated Vector databases offer, often through post-processing or less optimized methods.
2. Multi-tenancy Requirement - We need to be able to quickly search across different sets of entities sometimes across searches. To keep things faster than even parallel queries, we want the search space to expand or contract before the search is completed.
3. Hybrid Search - To capture both nuance of documents through vectors and content of documents or keyword matching. This means full-text search, fuzzy ranking, and embeddings at once, and natively returning results with the correct rankings based on our parameters.
4. Updates and Caching - Documents change as you work with them. We need a way to maintain a cache, quickly invalidate it, and update the source data without having to worry about different locations where it lives. Additionally, we want to optimize UPSERT and DELETE operations, rather than working through other database APIs to keep track of our data.

While choosing Postgres/pgvector for a semantic search system isn't the most popular or highly recommended choice, Index isn't doing only semantic search. SQL lets us bring TSVector and Fuzzy search into a hybrid system, have variable search sizes, and powerful metadata filtering before any vector similarity is computed. But there are performance optimizations to make, that I'll come back to shortly.

I want to include here that for solving generalized search, pgvector might not be a end-all solution, and there are many great companies doing great work for this purpose, whose products we enjoy! Index is meant to solve a really specific problem in making it easier for our agent systems to search, hence why we made the decisions outlined here :)

## Globalization

Two of the constraints in our problem space that I had mentioned were Speed and Global Latency. For this, @CloudflareDev came to be our best solution.

By building on the Workers Platform, we automatically optimize for scale in our services and distribute it worldwide. We also gain access to a wonderful set of developer primitives that make it much easier to implement our cache layer and document processing workflow.

Additionally, for text embeddings and reranking, we can use the Workers AI tools to gain access to inference of multilingual models on a global network. Rather than relying on first party services for this, we also have the benefit of building atop open source.

## Designing Processing

Thus far, the key parts of the system have been established. The storage and the code layer. Now, we have to put them together, adhering to the strict memory constraints of Cloudflare Workers. For this, I designed the workflow atop object storage.

This started with building a storage system with Workers, that support multipart uploads and presigned uploads through the Cloudflare R2 S3-compatible API. This is our place for storage of documents and intermediate artifacts, allowing for memory efficiency in our durable workflows and for the stateless containers to create a "processing pool."

The ingestion pipeline has three responsibilities: store documents, detect changes, and produce searchable chunks.

1. Chunking - We chunk the document into focused sections using a recursive algorithm. Recursive chunking was chosen as other methods depend largely on the types of documents they are serving, or add latency to the system. We were originally using Mastra's library for this, but to optimize the package size and remove dependencies to minimize our containers, I cut it down to just the recursive functions.
2. Categorization - Since this document might previously exist in the database, we match the existing chunks and compare them based on a hash value to detect what chunks changed (and need to be re-embedded), or can be upserted with new metadata.
3. Embedding - All chunks that require embedding get those values computed. To optimize for speed and cost of inference, I've been slowly distilling embedding models in the background with layer reduction. For now, this runs on Cloudflare Workers AI.
4. Summarization - To keep agents grounded for the documents they are searching across, we generate summaries, sampled from document content or generated by LLMs with high token speeds depending on the size of document.
5. Saving - All chunks that we processed are upserted to the database.
6. Deletion - All chunks that are now outdated with the new document are deleted, and the workflow completes.

Now, we need to get back to how we're storing chunks. As Opennote uses Supabase for user-level storage, that originally seemed like a quick fix. However I quickly hit speed bottlenecks, especially when running thousands of parallel queries and indexing jobs in evaluation. That led me to encounter an article from @PlanetScale that had me migrate our MVP implementation over to their Metal infrastructure. This cut our P99 latency (measured from round trip time to search) over half, going from 475ms to 209ms.

This, alongside partitioning the database across entities and building in other smaller improvements (such as precomputing full-text vectors), helped significantly in improving query speed for benchmarking with many documents.

## Designing Search

Now, we have the chunks in the database, we just need to find them. The search system works as follows:

1. Query Parsing - We receive a query from an agent alongside any parameters. Any agent parameters are cleaned and validated before anything is sent to the database.
2. Filtering - Now, the rest of search runs within our Postgres database. We slice the search space down to respect entity boundaries, filtered document IDs, sources, tags, timestamps, and explicit exclusions, to keep the search space as small as possible.
3. Search - We now run queries for full text matches and semantic matches over the filtered candidate set based on the thresholds. Postgres supported functionality (i.e. pgvector, pg_tgrm, and the tsvector functions) all work together to give us the best result set.
4. Normalization - These searches use different ranking methods and incompatible ranges, so we normalize our final "scores" from 0->1. This lets us merge based on our "alpha" value, which we set at query time.
5. Various other steps, such as optional deduplication (for unique documents rather than just chunks), are completed in the database before the ranked top-K results are returned, alongside chunk metadata.
6. Once returned back to the worker, these chunks can be optionally reranked if that has been enabled, or written to the cache, and then finally delivered to the user.

Search runs through a Cloudflare Hyperdrive binding, to optimize for the fastest time possible in end-to-end search.

## Caching

As is with any good search system, there needs to be some form of cache path for queries to optimize at scale.

However, caching for our use case has some nuances. We want our agents to be able to send many queries in a single task, and ideally with overlap, we don't want these to choke the database. At the same time, LLMs are highly non-deterministic when it comes to more advanced tasks, which leads to repetitive searches that, again, drive compute.

Index runs into three key problems that we had to solve:

- Cache separation by entity
- Invalidation across changing documents
- Agents might have slightly different queries across different sessions, as they are non-deterministic.

The put operation places search results into a KV store based on the hash of the query and certain opinionated parameters, such as entities, filters, etc. Meanwhile, a Vectorize store maintains a semantic mapping of the query text to the KV-stored results, with metadata filtering to make sure that queries don't overlap across entities.

When getting from the cache, first, we look if the entire query hash is available in KV (i.e. a repeated search). If that is missed, we can check the semantic cache for a query that might've been similar with the same entity, to some threshold. If that is missed, then the search pipeline can be enacted. All "get" operations use Entity IDs as a primary filter, making sure that there is no overlap with results.

Lastly, the main problem becomes invalidation. We maintain a reverse map: instead of searches mapping to chunks, we also maintain a KV store of chunks mapping to the search hashes that they show up in. If a chunk is outdated and about to be deleted, all the caches of results that it appears in are invalidated in both the direct and semantic lookups.

With that, as well as robust error handling and retry methods due to the expected rigor of Index in production, we have the makings of the entire search system.

# Results

With the system complete, it is now time to validate. These evals were to certify that Index is uncompromising on search quality while consistently meeting the constraints alongside the architecture we're looking for.

We tested Index against ChromaDB on 10,000 MSMARCO pairs with 100 searches and K=10 results per search, with the following metrics measured:

- Recall@K – whether all relevant documents were retrieved within the top K results.
- MRR@K – reciprocal rank of the first relevant document, or the average position of the correct document in the result set.
- MAP@K – average precision across relevant positions, or how consistently the system ranks the top result at the top of the result set.
- NDCG@K – rank-aware gain normalized by the ideal ordering.

Using the BGE-M3 Embedding Model (for multilingual support) with K=10: Index upheld ChromaDB's quality across all metrics, while simultaneously supporting hybrid search, multi-tenant isolation (and dynamic search spaces), and sub-300ms P99 latency per query.

To clarify, Index's goal was not to take a specialized search system and blow it out of the water, or optimize for the highest numbers possible. Chroma has built an amazing product that we quite enjoy, but we also now have something that can fit our use case and support a variety of queries in a way we need, adapted to our usage patterns.

Running these evals also confirmed that Index meets its design objectives: fast multi-tenant search, reliable chunk selection for agent systems, and predictable behavior across document structures, all while maintaining retrieval quality comparable to a dedicated semantic search engine.

Index is already in production powering Opennote Communities, and will be the foundation for the knowledge layer of the platform.

# Looking Ahead

Index currently excels at retrieval over non-stateful knowledge — journals, transcripts, documents that contain isolated facts, for both users and AI alike. But chunks are just facts, and we already have the infrastructure to link them.

These are our next steps to move Index from retrieval to understanding:

- Temporal and evolutionary relationships between chunks
- Popularity signals to improve chunk selection
- Distilled embedding models optimized for our use cases
- Agent configurability for multi-step search trajectories

Building atop SQL gives us a foundation for this evolution.

# Wrapping Up

Building Index was an end-to-end optimization project, from storage to pipelines, embedding models, APIs, cache behavior, SDK design and developer experience. It had me obsessing over every little detail, whether it was reading Cloudflare's docs late into the night to study Workers and our operational constraints, and required viewing search from first-principles rather than existing abstractions, and deciding trade-offs between many decisions.

Search remains a highly open problem, especially as the standard for agents nowadays is to have readily available access to information, without a human-in-the-loop.
