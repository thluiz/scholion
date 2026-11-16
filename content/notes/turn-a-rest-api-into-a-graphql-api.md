---
title: "Turn a REST API into a GraphQL API"
date: '2026-11-16T15:44:15+00:00'
category: webclip
summary: 'The article shows a simple way to wrap one REST endpoint in GraphQL by defining a schema, adding a query, and writing a resolver that fetches from the REST URL.'
tags: ["graphql", "rest-api", "resolver"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Turn a REST API into a GraphQL API"
    url: "https://web.archive.org/web/20200505183823id_/https://dev.to/feldroy/turn-a-rest-api-into-a-graphql-api-50kf"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/web-archive-org--turn-a-rest-api-into-a-graphql-api.md"
    kind: repo
---

The post explains how to turn a single REST endpoint into a GraphQL endpoint. It uses the PokeAPI Pikachu endpoint as the starting point, then defines a `Pokemon` type, a `getPokemon` query, and a resolver that fetches data from `/pokemon/<id>/`.

## Reading notes

- The example starts from a simple GET REST endpoint for Pikachu.
- The GraphQL schema defines a `Pokemon` type with `id`, `name`, and `base_experience`.
- The query type adds `getPokemon(id: String!): Pokemon`.
- The resolver handles `getPokemon` by sending a GET request to `MY_REST_URL + '/pokemon/' + id + '/'`.
- The article shows the query in GraphQL Playground and returns real data from PokeAPI.
- It suggests adding another field to the schema and query as a practice exercise.
