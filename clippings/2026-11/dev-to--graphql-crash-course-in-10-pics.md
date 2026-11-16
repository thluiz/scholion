---
url: "https://dev.to/hexrcs/graphql-crash-course-in-10-pics-3b04"
captured_at: "2026-11-16T19:11:44+00:00"
title: "🔥 GraphQL Crash Course (in 10 pics!)"
domain: "dev-to"
---

_Originally posted on Twitter as a thread: [https://twitter.com/hexrcs/status/1190332090149150720](https://twitter.com/hexrcs/status/1190332090149150720)_

Always wanted to use GraphQL for your new projects, but never got time to learn how it works? 😃

Let's start the week with some new GraphQL knowledge in hand! 🙌

👇 Here's a 10-minute GraphQL crash course for you! 🥳

## [](#1-how-graphql-works)1 - How GraphQL works

GraphQL is a query language for making flexible API calls.

We describe what we want in a single request with nested fields, then we will receive a data payload of the exact shape.

No need to make many small requests to stitch data together or over-fetch unwanted parts!

[![How GraphQL works](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fi.imgur.com%2FZalpOf7.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fi.imgur.com%2FZalpOf7.png)

## [](#2-a-graphql-query-exchange)2 - A GraphQL Query Exchange

GraphQL is not a library, but a language spec.

We send structured queries as POST or GET requests. The server checks if they're valid with a predefined schema, runs corresponding resolver functions to perform operations, then prepares the data to be returned to the client.

[![A GraphQL Query Exchange](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fi.imgur.com%2FcIqFAw8.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fi.imgur.com%2FcIqFAw8.png)

## [](#3-the-graphql-schema)3 - The GraphQL Schema

GraphQL schema defines the structure of valid queries and the return data types of them. It's the protocol the client & server use to communicate under.

They're strongly typed, can be nested. In addition to the most common "object" types, the schema also supports unions, enums, interfaces, etc.

There are 3 operation types in GraphQL - `query`, `mutation`, or `subscription`. `query` is the most commonly used operation.

[![The GraphQL Schema](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fi.imgur.com%2FzyTgxJr.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fi.imgur.com%2FzyTgxJr.png)

## [](#4-argument)4 - Argument

Some queries allow us to pass in arguments in order to eg. filter results. The schema defines all valid arguments.

On the backend, we need to have corresponding resolvers to fulfill those conditioned queries.

NOTE: GraphQL has no builtin comparison operators or functions like `>` or `TOP`, `LIMIT` in SQL! Those additional features **must** be implemented in the resolvers. Most GraphQL frameworks however already ship with those utility resolvers.

[![Arguments](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fi.imgur.com%2FjldtXcJ.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fi.imgur.com%2FjldtXcJ.png)

## [](#5-alias)5 - Alias

Sometimes in a query, we select the same field multiple times, but each time with a different argument (like in the pic). This will cause naming conflicts, so we need to assign aliases to the fields.

Aliases can be added to any field.

[![Alias](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fi.imgur.com%2FTEp0pnR.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fi.imgur.com%2FTEp0pnR.png)

## [](#6-fragment)6 - Fragment

We can wrap "subfields" into a Fragment and reuse them with the spread operator in selections. Useful when we select the same fields over and over again. Think of it as a JS object for GraphQL field names that can be destructured!

The Fragment is sent to the server alongside the main operation in the `query` field of the HTTP request payload.

[![Fragment](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fi.imgur.com%2FVBCpQ0L.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fi.imgur.com%2FVBCpQ0L.png)

## [](#7-variable)7 - Variable

Using GraphQL variables makes it easy to modularize and share/reuse our prewritten query code. We declare them at the beginning of a query, and are allowed to assign default values to them. The variables can be nested, just like a normal JSON object.

Noticed the GraphQL request payload in the pic of section _2 - A GraphQL Query Exchange_? This is what the "variables" field is for.

[![Variable](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fi.imgur.com%2FCZ9IXJ1.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fi.imgur.com%2FCZ9IXJ1.png)

## [](#8-interface)8 - Interface

Interfaces in a GraphQL schema allow us to flexibly create and use complex data types in an OOP manner.

Types can implement (multiple) interfaces.

When the return type is an interface, we can use the `on` keyword to conditionally access fields of a specific implementation.

[![Interface](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fi.imgur.com%2FR2W9Kax.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fi.imgur.com%2FR2W9Kax.png)

## [](#9-mutation-operation)9 - Mutation Operation

Contrary to queries, a Mutation operation is used to change the serverside data - eg. to create an account, generate auth token, or add data entries.

Like queries, we can supply arguments to a mutation. The mutation also returns value, so don't forget to select the fields we need!

[![Mutation Operation](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fi.imgur.com%2FguzWD0X.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fi.imgur.com%2FguzWD0X.png)

## [](#10-subscription-operation)10 - Subscription Operation

Instead of sending queries over HTTP back and forth, GraphQL also has a Subscription operation type for creating WebSocket connections, so the server can push continuous updates to the client.

Particularly useful for real-time apps like 💹 stock market or 💬 messaging apps.

[![Subscription Operation](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fi.imgur.com%2FXZ5jtC2.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fi.imgur.com%2FXZ5jtC2.png)

## [](#bonus)BONUS

### [](#online-playgrounds)Online Playgrounds

Many GraphQL frameworks come with a web IDE with autocompletion support and interactive schema lookups like [GraphiQL](https://github.com/graphql/graphiql) or [GraphQL Playground](https://github.com/prisma-labs/graphql-playground). Make use of them when debugging your queries! ✨

You can also create your own playground online with [CodeSandbox](https://codesandbox.io/) by selecting the _Apollo GraphQL Server_ sandbox.

However, if you are as lazy as me 🤪, there are also a few zero-config public GraphQL APIs to play with online 👉 [https://apis.guru/graphql-apis/](https://apis.guru/graphql-apis/)

### [](#additional-resources)Additional Resources

There's a [great episode](https://ladybug.dev/episode/what-the-heck-is-graphql/) on GraphQL from the [Ladybug Podcast](https://ladybug.dev/), do check it out!

I hope you have enjoyed this GraphQL crash course! 😁 Have a great and productive week ahead! 🙌

(Thread crash course format inspired by [@chrisachard](https://twitter.com/chrisachard) 😁 Check out his excellent React/Redux, Git crash courses!)

* * *

While you are still here, if you've got 13 more minutes and are interested in learning the new hot framework Svelte, I've also got a crash course with companion videos here 👉 [**Svelte Crash Course** 🔥](https://dev.to/hexrcs/svelte-crash-course-with-pics-27cc)

**Like this post?**

_I'll be posting more on Twitter: [@hexrcs](https://twitter.com/hexrcs)_  
_You can also find me at my homepage: [xiaoru.li](https://www.xiaoru.li/)_
