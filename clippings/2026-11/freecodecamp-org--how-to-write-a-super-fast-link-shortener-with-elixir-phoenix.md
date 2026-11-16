---
url: "https://freecodecamp.org/news/how-to-write-a-super-fast-link-shortener-with-elixir-phoenix-and-mnesia-70ffa1564b3c"
captured_at: "2026-11-16T04:12:09+00:00"
title: "How to write a super fast link shortener with Elixir, Phoenix, and Mnesia"
domain: "freecodecamp-org"
---

![How to write a super fast link shortener with Elixir, Phoenix, and Mnesia](https://cdn-media-1.freecodecamp.org/images/1*_5mxMoPtToWHgTEyslbYnA.png)

By Ben Church

Let's start this month’s tutorial with two statements that are going to get me in trouble:

1.  Elixir is the most productive language out there.
2.  Bit.ly charges way much for their paid plan

Elixir, the Phoenix framework, and the Erlang VM allows us to make production ready systems fast, easily, and with very few moving parts. At this point, you can see where we’re going with this. Let’s use what comes out of the box with Elixir to create a link shortener and prevent a $500 monthly bill.

Let’s dive in!

### Initial Setup

#### Before you start

Please make sure you have the following:

1.  [Elixir](https://elixir-lang.org/install.html)
2.  [Phoenix](https://hexdocs.pm/phoenix/installation.html)

#### Create a new Phoenix Project

The first thing to do as always is to have Phoenix create the skeleton of the project. For this demo, we won't have a “frontend” so we can tell the initializer to leave those out.

In your terminal type:

```
mix phx.new shorten_api --no-html --no-brunch
```

#### Update your dependencies

Next, we're going to add a few dependencies to `mix.exs`. Go ahead and update the `deps/0` function in that file to look like this:

### Logic!

Ok basic set up out of the way. That means we’re into setting up the logic that will:

1.  Allow us to save URLs
2.  Reference these URLs by a unique HashId (ex. `abc123`)
3.  Navigate to `/abc123` and it redirects to the URL that it references

First up, creating a way to store these links.

#### Creating a way to store these links

Let's use Phoenix’s built-in generators to do this for us. In your terminal run:

`mix phx.gen.json Links Link links hash:string:unique url:string:unique`

This will create the

1.  `Links` context
2.  `Link` model
3.  `Link` controller
4.  Database migration

That’s honestly the end of that step. It will ask you to put a few lines in your `router.ex` file but for now, you can skip that if you want as we will touch on it later. Let's move onto how we can modify what was created above to automatically create the id’s we will use to reference these links.

#### Autogenerate the HashId on Link creation

By default in these systems, models are given an `id` column in the database that is a number, unique and auto increments: 1, 2, 3 and so on. In our system we want the `id` to be a:

1.  Short
2.  Unique
3.  String
4.  That auto-generates.

_Ecto makes this really easy._

The first thing to do is make a custom Ecto Type which will handle all of this for us. Create a new file `shorten_api/ecto/hash_id.ex` and populate it as follows:

What we did above is essentially create a new type that can be used the same way we define a field as a `String` or an `Integer`. Now we can define a field as a `HashId`.

> _You can learn more about this in the [Ecto documentation](https://hexdocs.pm/ecto/Ecto.Type.html)._

So let's do just that and update `shorten_api/links/link.ex` to use a `HashId` as it’s a primary key instead of an `Integer`:

#### Update the migration

Now that the `HashId` is setup in our code, we want to update the migration to set up the database to reflect what's happening in our model file. You should have a file in your project that ends with `_create_links.exs` . Find it, open it and modify it to resemble the below code:

Alright, that's the majority of our plumbing steps, now we’re going to jump into the core logic of this whole project.

#### Redirect from an Id to a URL

First, we need a function in our controller that

1.  Takes an `Id` of a `Link`
2.  Looks up the `Link`
3.  Redirects to the `URL` attached to that `Link`

To do this, let's add a new function to our link controller found here: `shorten_api_web/controllers/link_controller.ex`

#### Hook it all up to our router

Now that we have this new controller function, the only thing left is to hook it up. Update the `router.ex` file to reflect the following:

> Note: we will also be adding the routes to `mix phx.gen` suggested earlier

### TADA! ?

At this point, you should be able to run the project with `mix phx.server` and have everything function as expected! However, we’re not stopping here.

### Secret sauce

Because link shorteners sit between a user and the actual content, it is crucial that these systems are fast. While Elixir is already fast, the main lag time in this process comes from our database. It takes time to look up the Link attached to an id.

To speed this up, link shorteners will often opt to use an in-memory datastore like Redis as opposed to an on-disk database like Postgres (which Phoenix sets us up with by default). **Thankfully because Elixir is built on top of the Erlang VM, we already have an in-memory datastore built in: Mnesia!**

In the next section, we’re going to alter our configuration to use Mnesia instead of Postgres.

#### Swapping from Postgres to Mnesia

This process is actually very simple. First update `config.exs` as shown:

#### Create your Mnesia database

Then create the location where Mnesia will back data up to and initialize the database through Ecto:

```
mkdir priv/datamkdir priv/data/mnesiamix ecto.createmix ecto.migrate
```

**Boom done!** You’re now using an In-Memory database to hold our Link information. Wasn’t that easy?

### Kick it off

You now can

1.  start the project (again for many of you):

`mix phx.server`

2.  Create a shortened link via `curl`:

```
curl --request POST \  --url http://localhost:4000/api/links/ \  --header 'content-type: application/json' \  --data '{ "link": {  "url": "https://twitter.com/bnchrch" }}'
```

3.  Take the `hash` returned in the response

`{“data”:{“url”:”[https://twitter.com/bnchrch](https://twitter.com/bnchrch)","hash":"7cJY_ckq"}}`

4.  And be redirected appropriately when you go to `localhost:4000/{hash}`:

![Image](https://cdn-media-1.freecodecamp.org/images/1*5jbpF4xVkeo2K7UIQKJWXg.gif)

### Wrap up

Amazing how easy it was with all these tools to create a fast, easy to maintain and simple to extend link shortener. A lot of the credit here can go to the BEAM (Erlang VM), Jose Valim (creator of Elixir), and Chris McCord (creator of Phoenix). The rest of the praise goes to how simple the idea of a link shortener is, in no way justifying a $500 per month introductory price tag. Still looking at you Bit.ly.

#### ?‍ This is open source! you can f[ind it here on Github](https://github.com/bechurch/shorten_api_tutorial)

#### ❤️ I only write about programming and remote work. If you [follow me on Twitter](https://www.twitter.com/bnchrch) I won’t waste your time.

* * *

Learn to code for free. freeCodeCamp's open source curriculum has helped more than 40,000 people get jobs as developers. [Get started](https://www.freecodecamp.org/learn)
