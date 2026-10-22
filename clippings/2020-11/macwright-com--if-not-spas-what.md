---
url: "https://macwright.com/2020/10/28/if-not-spas.html"
captured_at: "2020-11-02T00:16:26-03:00"
title: "If not SPAs, What? - macwright.com"
domain: "macwright-com"
---

# If not SPAs, What?

A few months ago, I [wrote an article about how the SPA pattern has failed to simplify web development](https://macwright.com/2020/05/10/spa-fatigue.html). The *SPA pattern* (Single-Page Apps), I tried to define, was about the React model, which also covers, to a large extent, the model of Vue, Angular, and other frontend frameworks.

Like any critique, it begs for a prescription and I didn’t give one, other than gesturing toward server-side frameworks like Rails and Django. But I think there are some trends starting to form. I had queued up some time to *really dive into the frameworks*, but things like [walking in parks](https://macwright.com/2020/10/12/holly-park.html) have taken priority, so here’s just a grand tour.

### Opinionated full-stack JavaScript frameworks

Primarily I’m talking about [Remix](https://remix.run/features), [RedwoodJS](https://redwoodjs.com/), and [Blitz.js](https://blitzjs.com/), though I’m sure there are similar efforts in the non-React world that are relevant. [Next.js](https://nextjs.org/) *almost* falls into this category, but as far as I can tell, it’s still unopinionated about the data layer and most sites that use Next.js are still going to use a separate API stack. But that’s subject to change, because all of these are moving fast.

It’s interesting to note that Remix, Redwood, and Next are all backed by companies or foundations, and that Blitz is aiming early on to be a [sponsor-funded project](https://github.com/sponsors/blitz-js). These projects, I think, are trying to sidestep the “tragedy of the commons” failures of earlier open source, wherein overworked and unpaid maintainers service a large userbase and eventually burn out and abandon the project.

To take Remix as an example, it re-ties data loading with routes, and then gives the pretty amazing promise of *no client side data fetching by default*. These frameworks are also *opinionated about status codes and caching strategies*. RedwoodJS automatically creates an [ORM-like interface using GraphQL and Prisma](https://redwoodjs.com/tutorial/side-quest-how-redwood-works-with-data).

As context, Remix is backed by the folks from [React Training](https://reacttraining.com/), who are also the folks from [React Router](https://reactrouter.com/), which is as much React pedigree as you can get without joining the team at Facebook. Redwood is run by [Preston-Werner Ventures](https://prestonwernerventures.com/), of [Tom Preston-Werner](https://en.wikipedia.org/wiki/Tom_Preston-Werner), a GitHub founder. Next.js is sponsored and heavily promoted by [Vercel](https://vercel.com/), née Zeit.

### Turbolinks

It’s worthwhile to just mention [Turbolinks](https://github.com/turbolinks/turbolinks). I didn’t use it until this year, and apparently there were issues with it before, but the pitch for Turbolinks 5 is: *what is the bare minimum you need to do to get the SPA experience without any cooperation from your application?*

So it’s a tiny JavaScript library that sits on top of an existing server-rendered application and replaces full pageloads with SPA-like partial pageloads. Instead of loading a page from scratch, pages are loaded with AJAX, page contents are replaced, and client-side navigation updates your URLs. Basically, it prevents the ‘blink’ of real page transitions and saves on all othe sorts of costs of fully loading a new page. Turbolinks was spawned from the [Ruby on Rails](https://rubyonrails.org/) project, and works great with Rails but doesn’t require it.

In terms of power-to-weight for user experience improvements, Turbolinks is a standout: it adds very little complexity and a tiny size impact for a big user experience improvement.

### Server-side-state frameworks

These are the spiciest new solution. The main contenders are [Laravel Livewire](https://laravel-livewire.com/) (in PHP), [Stimulus Reflex](https://docs.stimulusreflex.com/) (for Ruby on Rails), and [Phoenix LiveView](https://github.com/phoenixframework/phoenix_live_view) (on Phoenix, in Elixir).

The pitch here is: *what if you didn’t have to write any JavaScript?* It sort of hearkens back to the critique of JavaScript in [\_why’s ART && CODE talk](https://vimeo.com/5047563), that web development is the only kind where you normally have to write in three (or more) languages. These languages also most remnants of “client-side” logic, putting it all on the server side.

How do they do this? Well, a lot of WebSockets, in the case of Reflex and LiveView, as well as very tightly coupled server interactions. As you can see in the [LiveView demo](https://www.phoenixframework.org/blog/build-a-real-time-twitter-clone-in-15-minutes-with-live-view-and-phoenix-1-5), which I highly recommend, these frameworks tend to operate sort of like reactive DOM libraries on the front end – in which the framework figures out minimal steps to transform from one state to another - except those steps are computed on the server side and then generically applied on the client side. They also do a lot more data storage & state management on the server-side, because a lot of those interactions which wouldn’t be persisted to the server are now at least communicated to the server.

These frameworks are exciting, and also extremely contrarian, because they are the polar opposite of the “frontend plus agnostic API layer” pattern, and they also wholeheartedly embrace the thing everyone tries to avoid: mutable state on the server.

### Modest progressive-enhancement JavaScript frameworks

These are typically used “in addition” to the above, but they certainly deserve a shout-out because I think a wide swath of frontend-programming concerns actually only need a tiny hint of JavaScript. But the main caveat is that *they assume that you know JavaScript and the DOM*, which are not necessarily universal skills anymore. A lot of developers growing up on React have acquired a real blind spot for native browser APIs.

The main ones I’ve looked at are [Stimulus](https://stimulusjs.org/) (out of the Ruby on Rails camp), [Alpine](https://github.com/alpinejs/alpine/), and [htmlx](https://htmx.org/). They’re all tiny, and work great in *existing pages*. I think – and here come the flames – [Web Components](https://developer.mozilla.org/en-US/docs/Web/Web_Components) also fit into this sphere of progressive enhancement! If you just use good web components - [only ones that GitHub writes is a good rule of thumb](https://github.com/search?q=topic%3Aweb-components+org%3Agithub&type=Repositories) - then they can fit the role of just improving an existing static UI. It’s where you start to use Web Components as an apples-to-apples replacement for full-fledged frontend frameworks is where things seem to get dicey.

These frameworks have the luxury of operating on a deeply improved web stack, one with fundamental components like [fetch()](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API) and [MutationObserver](https://developer.mozilla.org/en-US/docs/Web/API/MutationObserver). These things were previously at the core of the utility of progressive enhancement frameworks, and now they can just be the utilities that those frameworks build on.

---

I’m sure that there are additional patterns out there! But these currents all seem strong right now, and it’s fascinating to see some really divergent and adventurous – and common-sense – approaches start to crop up.
