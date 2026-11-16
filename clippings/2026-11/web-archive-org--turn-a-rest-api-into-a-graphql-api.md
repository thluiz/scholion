---
url: "https://web.archive.org/web/20200505183823id_/https://dev.to/feldroy/turn-a-rest-api-into-a-graphql-api-50kf"
captured_at: "2026-11-16T15:44:15+00:00"
title: "Turn a REST API into a GraphQL API"
domain: "web-archive-org"
---

I really like working with GraphQL APIs. I like being able to get data in the shape I want, and using subscriptions to get it in realtime. This weekend I discovered that transforming a REST API into a GraphQL one is easier than it sounds.

This is a walkthrough of turning one REST endpoint to GraphQL. Once you can do one, you can do more 😀

## [](#the-rest-api-endpoint-well-transform)The REST API Endpoint We'll Transform

To keep things simple, we'll use a simple GET REST endpoint as our starting point:

GET [https://pokeapi.co/api/v2/pokemon/pikachu/](https://pokeapi.co/api/v2/pokemon/pikachu/)

Now let's create a GraphQL endpoint.

## [](#define-the-graphql-schema-for-a-pokemon-object)Define the GraphQL Schema for a Pokemon Object

First we define our GraphQL type for the Pokemon data we'll be returning from our new API endpoint:  

```
type Pokemon {
  id:       String!
  name:     String!
  base_experience:  Int!
}
```

For the sake of example, we're limiting the fields, but add more if you want.

## [](#define-the-graphql-query-type)Define the GraphQL Query Type

Then we define a GraphQL query called `getPokemon` that takes an `id` and returns a `Pokemon` object:  

```
type Query {
  getPokemon(id: String!): Pokemon
}
```

## [](#define-the-query-resolver)Define the Query Resolver

When a `getPokemon` GraphQL query comes in, under the hood of our resolver, we send a GET request to `/pokemon/<id>/`:  

```
const resolvers = {
  Query: {
      getPokemon: async (_, { id }) => {

          const response = await fetch(MY_REST_URL + '/pokemon/' + id + '/');
          return response.json();
      },
  }
```

## [](#try-the-query-in-graphql-playground)Try the Query in GraphQL Playground

A copy of the above code is [editable here on Glitch](https://glitch.com/edit/#!/audreyr-pokemon-remote-schema), and running [live here with interactive querying via GraphQL Playground](https://audreyr-pokemon-remote-schema.glitch.me/)

Go to GraphQL Playground and try the query we just created:  

```
query {
  getPokemon(id: "pikachu"){
    id
    base_experience
  }
}
```

It responds with real data from PokeAPI:  

```
{
  "data": {
    "getPokemon": {
      "id": "25",
      "base_experience": 112
    }
  }
}
```

Yay! As a practice exercise, try implementing another field besides `base_experience`:

1.  Remix my Glitch app
2.  Add the field to the `Pokemon` schema
3.  Add it to your query and see the results in GraphQL Playground

[![You Can Do It](https://res.cloudinary.com/practicaldev/image/fetch/s--z2FELErr--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/rkibazax5pwy70oqb38e.jpg)](https://res.cloudinary.com/practicaldev/image/fetch/s--z2FELErr--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/rkibazax5pwy70oqb38e.jpg)

With this knowledge and a little practice, there's so much you can do. Enjoy!

The software industry moves fast. But if you keep up, you can have an incredible career.

_**[Join DEV. 100% Free Forever.](https://web.archive.org/enter)**_
