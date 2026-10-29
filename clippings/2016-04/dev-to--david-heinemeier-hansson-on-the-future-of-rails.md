---
url: "http://dev.to/ben/dhh-on-the-future-of-rails"
captured_at: "2016-04-18T12:59:50-03:00"
title: "David Heinemeier Hansson on the Future of Rails"
domain: "dev-to"
---

# David Heinemeier Hansson on the Future of Rails

---

### 

The Ruby on Rails framework has had an incredible impact since its creation a decade ago, becoming the choice for some of today's mightiest tech companies. Patterns and concepts popularized by the framework have also had an indelible effect on the application architecture discussion. Rails is an open-source project which depends on innovation and good software design from its core team in order to maintain its direction and status. New paradigms are constantly emerging and Rails has done well to evolve and remain the go-to for many developers.

Rails is an open-source project which depends on innovation and good software design from its core team in order to maintain its direction and status. So much of Rails' direction depends on the views of its opinionated creator and Basecamp CTO [David Heinemeier Hansson](https://twitter.com/dhh). I contacted David in order to glean some insight into the direction of Rails. David shared his vision of the future with Practical Developer.

## A lot has happened since Rails 4.0 was released in summer of 2013, particularly in the Node community. Where does Rails fit in now compared to the past?

Ruby on Rails has its eyes on the same prize its always had: Be the full-stack framework that makes building applications like Basecamp, Github, Shopify, Kickstarter, Airbnb, Zendesk and others possible and enjoyable for small teams. Programming never stands still, of course. We've seen Node, Elixir, Go, Rust, and all sorts of other languages and frameworks come, and that's wonderful. The more the merrier! The web is an amazing platform exactly because it puts all these approaches on a level playing field when it comes to generating HTML, JavaScript, CSS. On the web nobody knows whether your web server is running Ruby or Go or Node. For me, the projects I make, and the examples I listed above, though, I have yet to see anything that really gives Rails a serious run for its money.

## Turbolinks and API mode make for two very different approaches to developing the view. Are you and your team at Basecamp planning to make use of both of these design patterns? How has your personal position on client-side rendered apps changed over the last few years?

[Turbolinks](https://github.com/rails/turbolinks) has really been picking up steam. The early knee-jerk reaction has subsided and lots of people are giving it a second look and really liking what they see. We have a ground-up rewrite in Turbolinks 5 that takes this even further by focusing on integration with native iOS and Android wrappers. It's a big leap forward and its the technology that's enabled us to ship Basecamp 3 with amazing native clients without building huge native teams. I'm really excited to share all this progress and enable more teams to go native where it counts (mainly navigation and some peak UI fidelity areas) and then rely on their Rails app as the integrated system. The beautiful monolith.  
  
At the same time, API mode broadens the appeal of Rails to everyone who's rocking the client-side MVC approach as well as 100% native mobile apps. There's no reason that we shouldn't be collaborating on improving Active Record, Action Pack, Action Mailer, Active Job, Action Cable, and all the other frameworks that Rails provides which aren't tied to HTML-view generation. The vast majority of Rails is as relevant to API-only apps as it is to full-stack apps. So making the size of our tent explicit is exciting.

## Could you sum up what you think "The Rails Way" represents in 2016?

I'm actually working on a new mini-book called *The Rails Doctrine* at the moment that goes over all this in deep detail. But the short story is that the Rails mission is to equip small teams to tackle big projects. We're not here to make things slightly more efficient for the 500-person company, that's just a side effect. The allegiance for Rails is to make it possible for one, two, or a few programmers to create amazing apps that span web, email, mobile, native, API, and all the other platforms we need to cover in 2016. Delivering for the web is getting more complicated every day. There are a thousand vendors and peddlers of complexity who benefit when things get hard and compartmentalized. Rails is here to serve as a counter to that. To retain the beauty and simplicity of building for the web without needing an army of experts.

## How do you think your "Reconsider" article affected the general perception of Rails?

Rails has been counter cultural from day one. Many of the basic tenets, from Convention over Configuration to The menu is Omakase remain deeply controversial. Rails stands for something, which means it's bound to alienate some people who are offended by that. [RECONSIDER](https://signalvnoise.com/posts/3972-reconsider), the blog post I wrote lambasting the San Franciscan economic model, Venture Capital, and wet dreams of *total market domination* is just a natural continuation of believing in something. I doubt it's going to have much of an impact, really. As far as I can tell, much of the current crop of VC funded tech startups are already flocking to the latest tech buzz. For mostly better, and for scarcely worse, Rails is no longer the latest tech buzz. It's mainstream now, at least in terms of reach (despite the many tenets that continue to be counter cultural). I consider that a very good thing.

## Which other programming trends are piquing your interest?

The rise of functional programming is wonderful. I've let my programming style inspire heavily by key concepts, without the need to throw out Ruby. Ruby is such a wonderful sponge for the best ideas in programming. It's explicitly not a single-paradigm language, just like Rails isn't a single-paradigm framework. We get to adopt and be inspired by the best ideas from functional programming without the need to give up the best ideas of procedural or objective oriented programming either. May we continue to be influenced in just such ways. The rich history of programming languages from decades past still has much to teach us.
