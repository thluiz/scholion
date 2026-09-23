---
title: "Really Good Search is Really Hard"
date: "2026-09-23T15:52:15+01:00"
category: webclip
summary: "Abhi documents building Index, a hybrid search system for AI agents on Postgres/pgvector and Cloudflare Workers, that matched ChromaDB's retrieval quality with sub-300ms P99 latency."
tags:
  - search-systems
  - pgvector
  - cloudflare-workers
  - ai-agents
has_commentary: false
sources:
  - title: "Abhi on X: \"Really Good Search is Really Hard\""
    url: "https://x.com/abh1a0/status/1993033150323392720?utm_source=tldrnewsletter"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2025-11/x-com--really-good-search-is-really-hard.md"
    kind: repo
---

Abhi's starting premise is that search built for humans doesn't transfer to agents. A person builds a mental model of a search space over repeated visits and learns its blind spots; an agent hits a corpus fresh on every query, with no memory of what worked last time, which pushes hallucination and drift risk onto the retrieval layer itself. Index targets agent-oriented retrieval across thousands of constantly changing documents, with a latency budget measured in milliseconds rather than the minutes a deep-research agent can afford.

Index runs on Postgres with pgvector instead of a dedicated vector database, combining TSVector full-text search, fuzzy ranking and vector similarity in one hybrid query, with metadata filtering happening at the SQL level before any vector computation.

## Fichamento

- The ingestion pipeline has six steps per document: recursive chunking, hash-based change detection, embedding of changed chunks, LLM-generated summaries for agent grounding, upsert to the database, and deletion of stale chunks.
- Migrating the chunk store from Supabase to PlanetScale's Metal infrastructure cut P99 search latency from 475ms to 209ms, more than half, under thousands of parallel indexing queries.
- Search results are normalized to a 0-1 range and merged with a tunable "alpha" value that sets how much weight vector similarity gets against full-text matching, at query time.
- Caching runs two layers: a KV store keyed by exact query hash for repeated searches, and a Vectorize semantic cache that matches queries similar enough to a past one within the same entity boundary.
- Cache invalidation uses a reverse index, chunks mapped to every search hash they appear in, so deleting an outdated chunk invalidates every cached result that touched it, both direct and semantic.
- Benchmarked against ChromaDB on 10,000 MSMARCO pairs (Recall@K, MRR@K, MAP@K, NDCG@K, K=10, BGE-M3 embeddings), Index matched ChromaDB's retrieval quality while adding hybrid search, multi-tenant isolation, and sub-300ms P99 latency.
- Next steps move Index from flat retrieval toward understanding: tracking temporal and evolutionary relationships between chunks, popularity signals for chunk selection, and distilled embedding models tuned to the specific use case.
