---
title: "You can do full-text search in Postgres?"
date: '2025-06-06T18:06:46+00:00'
category: comic
summary: "Milan Jovanović's YouTube community post on Postgres full-text search with EF Core, with a C# code card using ToTsVector and PlainToTsQuery."
tags: ["milan-jovanovic", "postgres", "ef-core"]
has_commentary: false
sources:
  - title: "You can do full-text search in Postgres?"
    author: "Milan Jovanović"
    url: "https://youtube.com/post/Ugkx0OQyBeiUbOXSs3eJ-6NEmoYgpnN0E_QA"
    kind: web
---

Community post by Milan Jovanović (@MilanJovanovicTech) on YouTube. [Post](https://youtube.com/post/Ugkx0OQyBeiUbOXSs3eJ-6NEmoYgpnN0E_QA).

> You can do full-text search in Postgres? 🐘
>
> Yes — and you can even wire it up with EF Core.
>
> With this, you can:
>
> - Set up full-text search indexes
> - Write efficient search queries
> - Rank and sort results by relevance
> - Integrate it smoothly inside your .NET apps
>
> Want a clean architecture foundation to plug these features into?
>
> P.S. Grab my Clean Architecture template here: https://www.milanjovanovic.tech/templates/clean-architecture
>
> What Postgres features have surprised you the most?

![Code card "Full-text Search with Postgres + EF Core": a C# query over db.Articles filtering with EF.Functions.ToTsVector("english", title plus content).Matches(EF.Functions.PlainToTsQuery("english", searchTerm)), then printing each article's Id and Title.](postgres-fts-ef-core.png)
