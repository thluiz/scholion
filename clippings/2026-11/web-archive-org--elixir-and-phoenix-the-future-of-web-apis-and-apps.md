---
url: "https://web.archive.org/web/20200226082723id_/https://blog.carbonfive.com/2016/04/19/elixir-and-phoenix-the-future-of-web-apis-and-apps/"
captured_at: "2026-11-16T08:19:46+00:00"
title: "Elixir and Phoenix: The Future of Web APIs and Apps?"
domain: "web-archive-org"
---

####  [![](https://secure.gravatar.com/avatar/86792f159b0bd5029f256f6841199bf3?s=45&d=mm&r=g)](https://blog.carbonfive.com/author/cnelson/)Posted on 19th April 2016 _by in [Development](https://blog.carbonfive.com/category/development/), [Elixir](https://blog.carbonfive.com/category/elixir/)_

![](https://blog.carbonfive.com/wp-content/uploads/2016/04/phoenix-elixir-1.png) Buzz has been building up around [Elixir](http://elixir-lang.org/) (and [Phoenix](http://www.phoenixframework.org/)) in the development community over the last year. We’re pretty excited about them too and want to share the reasons why they’ve piqued our interest and what we’ve learned so far. We decided to kick the tires by rewriting one of our in-house web applications using Elixir and Phoenix so that we could answer the questions that are most front of mind:

*   How productive is the stack?
*   Are there any emergent benefits?
*   Are there any significant gotchas?
*   What are the performance characteristics?
*   What’s the community like?

## What’s important?

First, let’s talk a little bit about what we’re looking for in any tech stack and why. Ultimately, we want to build using tech that’s highly productive and doesn’t make it difficult to adapt or grow as products mature and become more sophisticated. That is, we want to be able to be productive in the short-, medium- and long-term. We define productivity as being able to get features in front of users quickly. It’s influenced by the language, the frameworks and libraries, the development toolchain, and the services that make development and deployment easier. We also want to be a part of a community that’s welcoming, inclusive, supportive and generally positive.

## Why is productivity so important to us?

We’re in the business of building products in such a way that tightens the feedback loop, so that we’re validating assumptions and course correcting early and as often as necessary. We love tech, but what we love more is building the right product, and that almost never happens on the first swing. That’s why productivity and quick iteration are so important. Practically every decision we make is made with this in mind. It’s this quest for productivity that drove us away from Java EJBs to the lighter, faster, better Java stack of Spring, Hibernate, and Tomcat around 2005. Then it drove us to Ruby on Rails around 2008, which is still our go-to for most products. It was the reason for using Node.js on products that require near real-time distribution of messages across many clients. And it inspires ongoing experimentation and evaluation of any new, promising tech.

## How might Elixir and Phoenix fit into this evolution?

The hypothesis we’re testing is that Elixir and Phoenix will be as productive — maybe more — as other stacks we have used, while giving us better performance, stability and scalability out-of-the-box. No better way to find out than to try it…

## Elixir and Phoenix (in the tiniest nutshell)

Haven’t heard of Elixir or Phoenix? Here’s what you need to know: **Elixir** is about 4 years old. It’s a new functional language designed for productivity and maintainability that runs on the Erlang VM. The **Erlang VM** is time tested (more than 20 years old), very fast and has awesome concurrency and inter-process communication (called [OTP](http://erlang.org/doc/design_principles/des_princ.html)). **Phoenix** is a modern web framework that makes building APIs and web applications easy. Since it’s built with Elixir and runs on that awesome Erlang VM, it’s fast as hell and has excellent support for handling very large numbers of simultaneous users. More information is a Google search away.

## What Have We Learned?

We learned a lot by rewriting one of our own applications in Elixir and Phoenix. The application is a project- and people-tracking tool. It shows who’s working on what, what skills each person has, when people are taking vacations, and rotations between projects. It supports real-time updates and collaboration with numerous simultaneous users. We use it everyday to help run our business. As the product owner, I learned that smart full-stack Ruby developers can pick Elixir and Phoenix up quickly and get real work done without _that much_ ramp-up. This rewrite took between 5-6 developer-weeks total. We treated it like a real project and didn’t skimp on code quality, tests, loading assets from a CDN, database bootstrapping (for easy first-time development), writing efficient queries in [Ecto](https://github.com/elixir-lang/ecto), or anything else. All of the developers really enjoyed working in Elixir and with Phoenix. Here’s what they had to say about it…

> Elixir has been my first time working with functional programming. I’d say that the functional paradigm and immutable data are the biggest benefit of building a Phoenix application. Coming from OO, it definitely takes some time to get used to, but for me it makes the code easier to reason about and reduces some of the cognitive load of trying to remember what is/isn’t mutable. That’s usually what people say about functional languages, but I experienced it in practice. -Alex

> I really enjoy being able to specify contracts in my function definitions with pattern matching. Like being able to say, “this function should absolutely accept only these parameters.” I can delegate all my worries about error handling to the supervisors. Along with that I feel like I can express myself in simpler terms in Elixir. Especially with pipelining data transformations. I can write out each step and it’s clear what should be happening. Overall I just feel empowered to solve hard problems with Elixir. I don’t know if that’s because of the concurrency and supervisors, or syntax, or all of the tooling that’s already built in to Erlang. But the stuff I struggle with in Ruby and JS just doesn’t get in my way with Elixir. -Chris

## Takeaways

**Phoenix is productive, but isn’t as productive as Rails… yet.** There are good reasons for this, most prominently, our lack of experience with Elixir and the relative newness of the open source ecosystem (i.e. fewer libraries). Having said that, our team was still very productive. I can see the gap closing quickly. We’re helping close the gap by contributing to the language and framework, and through new projects like [Wallaby](https://github.com/keathley/wallaby). **Phoenix performs better out of the box.** A rather large JSON request was taking about 1.5-2.0s against our Rails backend (no caching). That same request (same h/w, database queries and data) takes about 400ms with Phoenix. The standard deviation was much lower with Phoenix too. We didn’t go deep on the benchmarking this time around, but maybe we will and share our findings in another post. **Channels are easy to use and fast.** We migrated from [Pusher](https://pusher.com/) (a great service!) to [Channels](http://www.phoenixframework.org/docs/channels), which removed an external service, reducing cost and simplifying things operationally without increasing app complexity. The migration was painless and Channels are solid. **Between low latency and Channels, the application went from sluggish to extremely responsive…** without having to introduce page, fragment, or “Russian doll” caching. Everyone who uses the application commented on how the app “works much better” now. Interestingly, the only thing that changed was the responsiveness. Goes to show that high latency makes an application feel broken, not just slow. **The Erlang VM makes much better use of resources.** Our application went from using just shy of 1 GB across 2 dynos to a single dyno using less than 100 MB. That single dyno is notably faster and can handle higher concurrency (about 10x). **Elixir/Erlang is less fiddly than Ruby or Node.js from an ops standpoint.** Erlang/Elixir doesn’t have an GIL (like MRI Ruby does) and a single (operating system) process makes use of all available cores (unlike Node.js). Additionally, there are no long, unpredictable GC pauses due to how the Erlang VM works. You can even deploy new code to a running VM without having to restart the process (how cool is that?!).

## Still evaluating…

We’re not done evaluating as there are some things you can’t answer with a short project. Here are some of the things we hope will be true: **Productivity will continue to improve as the community and platform mature.** Our hope is that Elixir and Phoenix match or beat the productivity we’ve seen with Ruby on Rails over the years. **Phoenix (without caching) will perform better than Rails (with caching).** We already know this is true on a small app, and we can’t wait to see how it pans out on a large one. We don’t expect to completely avoid caching with Phoenix, but it would be nice to avoid having to do it aggressively and early, as we have had to on our Rails projects to get reasonable performance and latency. Rails makes it “easy,” but it’s still time consuming and hard to get right. It also creates friction that reduces productivity. **“Cost per active 1000 users” will be much lower than with other platforms.** We really want to see what scaling looks like for a mid-to-high traffic application. We’ve seen others’ benchmarks and they look good, but nothing beats first-hand experience. **It will be easy to maintain a large, growing Phoenix application.** Small apps are easy to keep clean and simple, even elegant. What happens after 6 months or a year of development? It is easy to keep the code well factored, create good abstractions, and manage technical debt? Stay tuned for that in a future post. **Phoenix applications will be more stable and less bug prone given the functional/immutable nature of Elixir.** This will be hard to measure, but I think we’ll be able to make a reasonable judgement call after a few months.

## Other Important Questions

**Is it a safe bet? Will this tech be around in a few years?** We can’t predict the future, but the signs certainly suggest it will be. When you look at the number of conferences, meetups, newsletters and other signals, you see something that has reached escape velocity and is picking up speed. There are big products that leverage Elixir, including [Bleacher Report](http://eng.bleacherreport.com/about/) and [Pinterest](https://engineering.pinterest.com/blog/introducing-new-open-source-tools-elixir-community). And there are plenty built on Erlang, including WhatsApp and parts of the Heroku platform. **Will I be able to hire developers?** There are certainly fewer Elixir developers out there than just about any other stack, which at first may sound like a problem, but may not be. There are also significantly fewer companies competing for those people, which makes it easier to stand out compared to those competing with you over talent. We’ve also seen a trend in senior Ruby developers wanting to cross over to Elixir, rather than build yet another Rails app. Elixir is a shiny new thing with real promise, which helps attract very enthusiastic developers. **Can I use the services I know and love, like GitHub, Heroku, CircleCI, Code Climate, New Relic, etc?** Mostly, with a few caveats. We’re using GitHub, Heroku and CircleCI and they all work great. CircleCI needs a couple of additions to the circle.yml, but it’s nothing unusual. New Relic doesn’t support Elixir/Phoenix yet, but there’s the Erlang Observer and Exometer (see [measuring your phoenix app](https://medium.com/@mschae/measuring-your-phoenix-app-d63a77b13bda#.xz9e919h2)). Code Climate doesn’t work out of the box, but if you’re adventurous, there are some projects you can probably get working. All of this is to say, we didn’t find it hard to get started and stay productive… the things we rely on most heavily basically just worked.

## Conclusion

We’re bullish on Elixir and Phoenix and are excited to see what it’s like to build more apps and live with them for a while. We’re about to start our next Phoenix project — a web app and mobile API — and will keep contributing to the open source ecosystem. Who knows where we’ll be in a year? Maybe half (most?) of our projects will be Phoenix projects? Can’t wait to find out!

## Suggested Reading

*   [Elixir Homepage](http://elixir-lang.org/)
*   [Phoenix Framework Homepage](http://www.phoenixframework.org/)
*   [The Road to 2 Million Websocket Connections in Phoenix](http://www.phoenixframework.org/blog/the-road-to-2-million-websocket-connections)
*   [The WhatsApp Architecture Facebook Bought For $19 Billion](http://highscalability.com/blog/2014/2/26/the-whatsapp-architecture-facebook-bought-for-19-billion.html)
*   [Elixir vs Ruby Showdown – Phoenix vs Rails](http://www.littlelines.com/blog/2014/07/08/elixir-vs-ruby-showdown-phoenix-vs-rails/)
*   [Phoenix is not Rails](https://dockyard.com/blog/2015/11/18/phoenix-is-not-rails)
*   [What I learned migrating a Rails app to Elixir/Phoenix](https://medium.com/@stueccles/what-i-learned-migrating-a-rails-app-to-elixir-phoenix-f707436749aa#.7rygvk3t6)
*   [The weekly Elixir newsletter, by Plataformatec](http://plataformatec.com.br/elixir-radar)
*   [Weekly Elixir Digest](http://elixirdigest.net/)

* * *

* * *
