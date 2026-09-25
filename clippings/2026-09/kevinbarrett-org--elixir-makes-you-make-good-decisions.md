---
url: "https://kevinbarrett.org/elixir-makes-you-make-good-decisions/"
captured_at: "2026-09-25T17:12:19+01:00"
title: "Elixir Makes You Make Good Decisions"
domain: "kevinbarrett-org"
---

A month ago my cofounder and I launched [screen.garden](https://screen.garden/), a sync and multiplayer collaboration backend for Obsidian that also allows access to your vault from the web. It was a nights-and-weekends thing for us, the kind of project that steals sleep from the pure joy of working on it. We chose Elixir and Phoenix as the language/framework for building it, and now that we’re a month out I’m convinced that Elixir (and Phoenix, and Ecto, and…) makes you make make good decisions.

Real quick: if you use Obsidian for note-taking and wish it could do the Google Docs thing without making you leave your vault, take a look at [screen.garden](https://screen.garden/). It’s super fast, and taking meeting notes right in Obsidian with multiple cursors zooming around the note never gets old. I wrote this post with it, getting edits from others right in Obsidian.

I am a programmer. I’m in the business of making bad coding decisions, it’s sort of our whole thing. Staring at code written six months ago and saying out loud _what idiot wrote this?_ only to discover the idiot was you is, I’m pretty sure, a required credit in every CS program worldwide. But it’s eerie how solid our early architectural and structural decisions have been, how every dependency has been, well, dependable, and how easy shipping new features is.

## let\_me show you an example

Here‘s an example. In the early days of building screen.garden we had a pretty standard Phoenix LiveView app—contexts, views, Ecto schemas, etc.—and we realized that we needed some way to authorize user actions at the boundary between views and contexts. Say you’re a user on a team that has some notes and you want to load one of those notes and start editing it. We needed a simple, replicable way to answer the question, “should `actor` have `verb` access to `noun`? Sure, you can get there with lots of little database selects littered around your codebase, but there must be a way to cleanly abstract that, right?

I searched around a bit and found [let\_me](https://github.com/woylie/let_me), an excellent authorization library that transforms your ad-hoc authz checks into a DSL:

```
object :note do
  action :read do
    allow :is_member
    allow password: [:edit, :read], note_access: :password
    allow note_access: :public
  end
end
```

Given that policy, here’s how we check if `current_user` can read a note:

```
with :ok <- Policy.authorize(:note_read, current_user, note) do
  # Go ahead and load the note
end
```

The brilliant thing about let\_me is that it delegates the actual authorization checks to a module of functions that you can alter at will. This meant, for us, that when we decided to radically rewrite our access model _our contexts did not change_. We’re currently testing out a private collections feature internally, and building it was as simple as adding some Ecto schemas and let\_me checks—again, no spaghetti code.

## The power of the community

A common criticism of Elixir is that there is no waiting buffet of out-of-the-box deps; that because its community is small there are less options for tooling, dependencies, frontend components—the “TypeScript and React” argument.

I would like to counter this with another example. Our highest priority after launching screen.garden was adding support for file sync: we had fine-grained, realtime Markdown with multiple cursors, but the instant you dropped an image into your note you’d have to sync it elsewhere. So a couple of weeks after launch, once the initial flurry of talking about we’d built subsided, my cofounder [Sloane](https://sloanelybutsurely.com/) started designing an architecture to support file sync. She wanted to leverage as much of AWS’ native eventing as we could, and then found that [Broadway](https://github.com/dashbitco/broadway) had an SQS adapter, and of course [Oban Web](https://getoban.pro/docs/web/2.10.6/overview.html) is now free…and suddenly in a week we had end-to-end file sync with retries, backpressure, and sequencing that we could watch move through our backend in realtime:

![](https://kevinbarrett.org/elixir-makes-you-make-good-decisions/oban-web-file-sync.png)

An s3 event moving through a local app instance.

It’s hard to overstate just how powerful you feel with the toolbox Elixir and the BEAM give you.

## Real nice SaaS platform you got there,,,would be a shame if someone,,,,,,,tested it

I love writing tests in Elixir.

Let me reiterate what I said up top: I am pretty much your bog-standard programmer. I am the statistical mode of software engineers. If you say “estimate this ticket,” I say “between one week and two months.” If you say “jump,” I say “I’d really rather not.” I cannot recall a single time in my entire career prior to Elixir—across Java, Objective-C, Swift, Ruby, TypeScript, Go, to pick a few at random—that I was eager to write unit tests. And yet the instant I finish wiring up my Ecto schemas to a context I am _thrilled_ to write ExUnit tests.

The entire test framework is biased toward making testing as fast to author and as easy to design as possible. The mix generators scaffold tests for you. `setup` hooks and fixtures make it trivial to test against your actual schemas. `assert` and `refute` _do what you mean_, which sounds like a baseline testing requirement but I promise you is really not how much of the testing world works. It just feels good, and is a good decision to make, and Elixir makes me make it.

## (Korok sound)

My kid and I recently played through both _The Legend of Zelda: Breath of the Wild_ and its sequel, _Tears of the Kingdom_. In these games there are little leafchildren, Koroks, playing hide and seek throughout the world, often requiring you to solve little puzzles to discover them. These are the sidest of sidequests: completely optional. Tiny dopamine hits. For me, unlocking problems via Elixir feels a lot like finding Koroks—a puzzle piece slots into place, a little trill of horn plays (at least in my head as I stare at my editor), and the world is very slightly repaired.

If you’re a screen.garden user, this is why we’ve been able to ship a steady drumbeat of features and fixes since launch. And if you’re not, please [check it out](https://screen.garden/)—I’m so proud of what we built, both in terms of the service itself and what you can’t see, running on our servers, in happy and helpful world of Elixir.
