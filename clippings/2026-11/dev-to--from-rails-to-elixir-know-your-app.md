---
url: "https://dev.to/jdcosta/from-rails-to-elixir-know-your-app-131m"
captured_at: "2026-11-16T19:33:22+00:00"
title: "From Rails to Elixir: Know Your App"
domain: "dev-to"
---

_This is the first of a series of articles about my journey going from Ruby on Rails to Elixir/Phoenix._  
_\\Part1 [From Rails to Elixir: Know Your App](https://dev.to/jdcosta/from-rails-to-elixir-know-your-app-131m/edit)_  
_\\Part-2 [From Rails to Elixir: Safe Rewrites with NOOP Deployments](https://dev.to/jdcosta/from-rails-to-elixir-safe-rewrites-with-noop-deployments-40cb)_

I've been doing a lot of Ruby on Rails during my career as a Software Engineer, **I absolutely love it** and I don't necessarily plan to stop doing it.

In fact, Rails has been the _de facto_ choice not only for my professional projects but also for my personal ones. Most of the times I come up with this revolutionary new ideia that will change the world (no doubt about that) and I rush to the implementation because I don't want to lose the excitement. Since I'm usually in a hurry, it seems natural to me to use the most off-the-shelf set of tools out there that allow me to prototype my brain dump as quickly as possible.

## [](#the-price-tracker-app)The Price Tracker App

That's what I've done, once again, when I decided that I was going to build a **price tracker app** meant to be compatible with any online shop in the interwebz. Users will mark items as favourites and then receive notifications by email when their price changes.

I wanted people to be able to use a browser extension to save items so I immediately saw trucks loaded with JavaScript coming my way; then I needed some sort of backend to store this information and periodically scrape online pages for updated prices. I also needed something to help me send email notifications.

Here's how my mind works at this point: it needs HTML/CSS/JS to show at least a simple list of items being tracked, an API to get items from the database, a database of course, and perhaps some kind of background processing thing for the scraping and notifications. So...

![Ruby on Rails logo](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fi.imgur.com%2F6B5FbZm.png%3F1)

![PostgreSQL logo](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fi.imgur.com%2FaFv7C7m.png)

![Sidekiq logo](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fi.imgur.com%2F5m4M8aE.png%3F1)

![Redis logo](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fi.imgur.com%2FEaNM0ps.png%3F1)

###### [](#-i-always-found-that-sidekiq-logo-hilarous)\* I always found that Sidekiq logo hilarous.

Did I get the tech stack right!? Off I go.

I built the browser extension, built the API to get items through both ways, built a background worker that wakes up every two hours and downloads the HTML page for each stored item and built another background worker that parses all these HTML documents searching for updated prices. I even built a small use-and-discard HTTP proxy repository to get away unnoticed with my scraping but I'm saving it for another blog post.

I think I had a working version after one week of coding during my free time (mostly evenings), because **Rails** ❤️.

## [](#shipping-it-to-production)Shipping it to Production 💰

I chose to put it all in one server in order to keep things smooth and simple, which means **PostgreSQL**, **Rails**, **Redis** and **Sidekiq** sharing a single CPU and 1.70GB of memory.

First deploy with just PostgreSQL and Rails went fine, then I added Sidekiq and Redis and the thing just blew up unexpectedly during the deploy - I was using [Capistrano](https://capistranorb.com/). After more than 1 hour of frustration, I finally figured out that my server was **out of memory** while trying to compile assets and spawn fresh copies of Rails and Sidekiq.

I shouldn't be compiling assets in the production server to start with, but that's how Capistrano works by default. I could also perhaps have spent some time trying to find a way to restart the app in a more memory efficient manner but I felt that I would be fighting against the technology I had imposed on myself. Plus, any time spent on this particular issue felt worthless to me.

So, next up in Google Cloud was a 3.75GB virtual machine which I imagined would be enough for now. As a side note, I was on Google Cloud because I had heard good stuff about it, plus I was planning to use [Google Cloud Functions](https://cloud.google.com/functions/) in a later stage and being in the same cloud provider would eliminate network transfer costs.

Everything great so far. My app was running, I was iterating as fast as new JavaScript frameworks are released 😏 and I even managed to convince some friends to start testing it as real users. I was happy!

...until I saw the bill 💰💰💰😐.

[![throwing money away](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fi.imgur.com%2Fn0cAopZ.jpg%3F1)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fi.imgur.com%2Fn0cAopZ.jpg%3F1)

Paying as much as **USD 24.27 /month** (at the time of this writing) to keep alive a low-effort side project was a total waste of money, even more so because the server itself wasn't doing much and sitting still for most of the time. On the other hand, I needed an expensive amount of memory available to accommodate the baseline memory requirements for Puma/Rails and Sidekiq.

It would make sense for a startup company who is committed to a project to pay such a small amount (in these terms) because the compensatory added value in the form of development speed is far superior. There's [this controversial article](https://m.signalvnoise.com/ruby-has-been-fast-enough-for-13-years-afff4a54abc7) by Rail's creator [DHH](https://twitter.com/dhh) about Ruby being fast and cheap enough for companies (I agree to a certain extent).

It wasn't the case for me though, I wasn't burning VC money, hadn't committed to any sort of deadline and I didn't have any salaries to pay so I was prepared to bring down my development speed in exchange for a less expensive infrastructure.

## [](#know-your-app)Know Your App

Luckily, I've been doing scaling and optimisation on a Rails-based system for the last 2 and a half years as part of my full time job. I learned valuable lessons about **knowing my systems before thinking about optimisations** by monitoring every workflow, hunt for bottlenecks, deeply understand the underlying workload patterns (are they fundamentally synchronous, can they be concurrent, who depends on who, etc) and finally tracking down who's stealing the most of your CPU and memory resources.

This acquired experience made me look at my price tracker in a sort of zoomed out version of the system, where the specific parts such as classes and objects and how they interact with each other were not important anymore. Instead, what became relevant to me was how the system could be divided into high level concerns, how these concerns were represented and how they were interacting with each other.

In the end I realised that my price tracker could be divided in four separate concerns:

[![architecture diagram dark](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fi.imgur.com%2F5PSZTh3.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fi.imgur.com%2F5PSZTh3.png)

1\\ The **Web Server**'s job was to provide a way for users to manage item lists. This component was just a standard stateless HTTP server, in which each request is 100% isolated from other requests. This is very important because it tells us that they are allowed to run concurrently. Since its main job was to insert and retrieve stuff from a database, most of its execution time was being spent waiting on I/O operations.

2\\ The **Page Downloader** is a background process that wakes up every two hours to gather item URLs from the database and download the corresponding HTML pages into disk. I'm again looking at another type of workload that can run concurrently because there's no shared state between downloads.

3\\ The **Page Parser** is another background process that grabs HTML pages from disk, proceeds with parsing them and then navigates through text nodes searching for updated prices. Whether it finds great prices or not, the final result is reported back to the database. Similarly to the aforementioned services, there's no shared state between different pages being processed, meaning they could also run concurrently. Perhaps the main difference between this and the others is the fact that it might tend to be a little more heavy on CPU than memory due to text search.

4\\ The **Notifications** part of the system is not represented for simplicity, but I plan to write a future blog post about how it integrates with the current topology.

By doing this high level analysis, I learned that all four components had the ability to do their work independently from each other - this didn't happen by accident as they were **designed to work concurrently** in the first place. The Page Downloader could keep downloading pages while the Parser was already processing the first batch that came through. The Web Server was also there on the side letting users manage their item list without blocking the rest of the system.

I also learned that my system was severely I/O bound as most downloads would take several seconds to complete. I should leverage the slack time the CPU was getting by forcing it to do other useful stuff while waiting.

_If you're interested in learning more about concurrent workloads, I recommend the first part of this great talk presented by [Golang](https://golang.org/)'s co-creator [Rob Pike](https://twitter.com/rob_pike)._

If I had a real world application with a fair amount of traffic, I would also spend some time studying server and application metrics. It's important to know every hot path on your system so that you can reason about which parts need to be designed with performance in mind - a concept that is generally described in economy as the [Pareto Principle](https://en.wikipedia.org/wiki/Pareto_principle).

That's why people keep talking about monitoring, it really is important, and nowadays there are plenty of options out there to do it, both in premises or as a service. I have used [New Relic](https://newrelic.com/) in the past and I got some pretty valuable insights into my platform from it. Totally recommend it.

## [](#make-the-decision)Make the Decision

Once I knew that I needed 1) a concurrency-friendly environment to work on top of; and 2) a runtime that would consume very low memory; I felt ready to hunt for the right tool for the job.

In 2018, what is it that pops up in your head when the matter is concurrency? Well, I'm sure the answer to this question will differ based on individual's experiences but in my head it's [Elixir](https://elixir-lang.org/) and [Go](https://golang.org/).

About Go, the syntax scares me personally and I don't really feel comfortable with the way they do [error handling](https://blog.golang.org/error-handling-and-go). Although they have an elegant way of doing concurrent stuff using [Communicating Sequential Processes](https://en.wikipedia.org/wiki/Communicating_sequential_processes) (CSP), it's easy to mess up because data structures are still mutable. On top of this, as I heard in a recent podcast, I don't feel that it is capable of providing a high enough abstraction for problems like the one I had in hands.

No hard feelings though, others will have different perspectives 👍.

![Elixir logo](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fi.imgur.com%2FvyyMHds.png%3F1)

![erlang logo](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fi.imgur.com%2Fz0qaATC.png%3F1)

![phoenix framework logo](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fi.imgur.com%2FBE0hjDM.png%3F1)

Elixir, on the other hand, felt immediately familiar to me. Maybe it's because the syntax makes it look like Ruby (it's a trap!) but I can also find similarities in the community. Elixir's creator [José Valim](https://twitter.com/josevalim) was a prolific member in the Ruby community, maybe that's why.

Additionally, because it runs on top of [BEAM](https://en.wikipedia.org/wiki/BEAM_\(Erlang_virtual_machine\)) (Erlang's virtual machine), concurrency primitives are deeply embedded in the language and the actual programming model - the [Actor Model](https://en.wikipedia.org/wiki/Actor_model) - is all about concurrency. This felt like a perfect fit for my concurrency hungry platform. You can learn more about how Elixir shines in this field [in this article](https://elixirschool.com/en/lessons/advanced/concurrency/).

Once I started diving deeper into Elixir and the ecosystem, I started to feel that I was advancing in the right direction:

1\\ **Great tooling**. I needed a web framework and [Phoenix](https://phoenixframework.org/) checked all the boxes; I needed a jobs framework capable of integrating with Sidekiq for the initial migration and [Exq](https://github.com/akira/exq) was there; I needed an HTTP client library and [httpotion](https://github.com/myfreeweb/httpotion) was there; I needed an HTML parser and [floki](https://github.com/philss/floki) was there; finally, I needed deployment gear and [distillery](https://github.com/bitwalker/distillery) looked fine; All these packages were well documented and well maintained just like I was used to in Ruby land.

2\\ It had a **Stable and Growing Ecosystem**, so I wasn't worried about possibly be using an overhyped tool destined to die in a couple of years. Erlang has been around for 20 years now and Elixir is unleashing its potential by making it more accessible. Even Erlang developers are getting excited by this new language and consequently getting involved in the community. This can only be a positive sign.

3\\ It checks all the boxes in terms of my **Concurrency** requirements. I would be able to spread my workloads across the server and run them in a concurrent fashion, maximising CPU and memory usage. I foresee hundreds or even thousands of downloads happening at the same time in a single machine with little effort.

4\\ The native concept of **Umbrella Projects** would allow me to segregate the different concerns of the platform without the risk of engaging in any sort of over-engineering. More info [here](https://elixirschool.com/en/lessons/advanced/umbrella-projects/).

5\\ **Infrastructure Costs** were expected to be lower judging by all the articles you can read online about companies migrating to Elixir and being able to reduce their fleets from hundreds of servers to just a few. Unfortunately, there's little information about how much memory Elixir needed at rest, but Erlang's website states that people have successfully ran BEAM in a system with just 16MB of RAM, which doesn't mean much. If you have valuable information about memory consumption please reach out.

I would have tested my memory assumptions thoroughly if I was on a real world scenario. In my development machine, I could see an average of **40MB** of RAM being used by the BEAM after running `iex -S mix` with just a few loaded dependencies. I don't know how believable this number is.

6\\ I can think of at least two friends of mine that will be very happy once they know I'm finally leaning over Elixir. Seriously guys, if you're reading this, please stop annoying me with all your Elixir shenanigans! It's done, I'm Elixiring now.

_Check out their contributions to the community: 1) A super fast jobs framework [ExJob](https://github.com/eidge/ex_job) based on event sourcing and GenStage by [@eidge](https://twitter.com/eidgeare); and 2) a task scheduling system [Cronex](https://github.com/jbernardo95/cronex) by [@jbamaro](https://twitter.com/jbamaro)._

More about the pros and cons of Elixir [in here](https://github.com/bignerdranch/why_elixir).

At this point I felt confident enough to go for this rewrite and I have to add that I was very excited too. I wrote a few modules just to test drive the thing and it really caught my attention. All of the sudden I was devouring documentation, podcasts and online talks so I was **genuinely interested and having fun** with it. This is very important to me. 🤓🤓

## [](#companies)Companies

I was working by myself on this stuff with virtually no restrictions apart from wanting to keep infrastructure costs low. My main goal was to learn and have fun building a low-budget toy product.

Had I been in the context of a company, there's a whole lot of other elements I would have to factor in before making such a decision: 1) it's a relatively new technology so I guess it will be harder to find experienced/keen developers; 2) rewrites usually require considerable development effort and might not produce immediate short-term results; 3) new software might introduce new bugs or bring back old ones; 4) the moment of the switch over to the new platform can be disruptive and takes time to plan carefully; 5) younger startups might benefit from using off-the-shelf tools like Ruby on Rails instead to maximise development speed and consequently burn as less time/money as possible. These are just a few factors worth considering off the top of my head, but I'm sure there are others.

Having said that, once certain products mature and reach considerable scale, it might be worth to replace parts of the system with more performant alternatives either to be able to handle more traffic or reduce costs. Or both. [These dudes](https://www.techworld.com/apps-wearables/how-elixir-helped-bleacher-report-handle-8x-more-traffic-3653957/) were able to reduce their fleet of servers from 150 to just 5 by replacing their Ruby on Rails monolith with Elixir/Phoenix. Having done my bit of infrastructure management myself, I can only imagine the vast sums of money they're saving each month.

I guess the lesson here is: if you're a company, **always assess the worthiness** of a platform migration of this kind before jumping off the cliff.

## [](#final-thoughts-amp-next-up)Final Thoughts & Next Up

At the time of this writing I don't know how much money I'll be able to save as I'm not done with the full migration yet. My goal is to document the whole journey in a series of articles, so you can follow me to get notified for the upcoming posts. There's plenty to talk about, all the way from choosing technologies, going over various implementation details, and finally discuss how to switch over to the new platform in production.

I'm planning to release a follow up on how to approach these kind of platform migrations in the next article of the series. I want to dive into the thinking process behind streamlining the whole migration (decide which parts should be migrated first, etc) in order to mitigate eventual risks. I'm going to use the **Price Tracker App** as an example.

If you find this article too conceptual, I'm planning to get more technical as the series goes, so expect to see some Ruby and Elixir snippets going forward.

Well, thank you for stopping by and stay tuned for the next one.

Feedback is much appreciated 👍
