---
url: "https://www.amberbit.com/blog/2015/4/22/why-rails-5-turbolinks-3-action-cable-matter-and-why-dhh-was-right-all-along/"
captured_at: "2026-09-25T21:50:34+01:00"
title: "Why Rails 5 / Turbolinks 3.0 / Action Cable matter, and why @dhh was right all along"
domain: "amberbit-com"
---

## tl;dr

Rails won the hearts of developers and entrepreneurs because it made creation of shiny web apps easy and fast. This is not the same experience you have when you build Single Page Apps using JavaScript frameworks (it tends to be way slower, and you end up with bunch of new problems to solve). Rails 5 might be good enough for you as it is.

## How it all started

If you are a Rails developer in 2015, there is a good chance you were not programming with Rails in it’s early days. I have the privilege to remember how it felt coding Rails in 2006 and 2007. It was pure magic. You could literally build modern-looking web application in matter of hours. From concept to prototype in one day? Try that within your current stack, where installing and configuring dependencies on it’s own will probably eat up half of that time.

One of the first projects on which I worked with Rails was a platform for a major UK political party. I was helping a (slightly) more experienced developer, who happened to know Rails for couple of months already. After investing long hours, blood, sweat and tears, we were able to launch the platform just in time for elections. Or a few days after elections, but that’s not really the point.

The system crashed frequently, required Cron job to restart both background tasks and web server instances on hourly basis, but it worked. The code was probably pile of spaghetti dipped in mud, with hacks on top of hacks. But it worked. Two inexperienced developers created fairly big, working system for established organization, in a matter of weeks. The magic of Rails made this possible. This would not be doable with any other technology that existed out there, at that time.

## Developers like fashion

We love buzzwords. They come and go in a matter of months, but we do love them for short periods of time, and then, we usually start to hate them. Remember AJAX? DHTML? MVC? TDD? BDD? NoSQL? Node.js? SPA? The last one, Single Page Applications, seems to be the trending now. Serious developers or entrepreneurs do need to consider their options carefully, before choosing stack, approach or architecture. The fact that something is trending at the very moment, might not be good advice. NoSQL seems to be the best example: a few years ago a lot of us jumped into new projects and replaced MySQL with MongoDB, Riak or CouchDB. I dare to say that majority of people who followed the trend blindly, at some point realized their decision was premature. They did have relational data. What they really needed was a SQL database such as… MySQL. Do not get me started on Node.js.

We like to follow the trends, as people in general. This is probably something anthropologists or psychologists might explain better than me. I feel that this is the same phenomenon as with political ideologies or religions. People start following them because their family, neighbours, everyone around them do. If everyone is saying the same thing, it has to be right. The problem is - it is often wrong or very wrong (think about communism, fascism or scientology).

## Your current stack

As a fashionable developer you are probably jumped on the SPA train already. No matter what the problem is, the solution is to build “modern web application” with some sort of “client-side MVC JavaScript framework”.

The problem is, even if you are experienced developer, it takes more time to add new features to the application than it would have in 2007 with Rails 1.2. That’s already including the fact that there is less mess with a browsers support (things got way better!) and you do have amazing CSS frameworks to help you. You are slower, because you need to write more code. The same applies to changing existing features - you are less agile.

If you are inexperienced developer… there is no way on Earth you can start writing complex SPA+backend applications immediately. You will face more problems, and have to choose between more possible solutions. The learning curve became way sharper than it was in the old days.

I am an employer, and I happen to run ([with a friend](http://twitter.com/wpiekutowski)) [Ruby on Rails web development shop](https://www.amberbit.com/). I take care of hiring of developers as well. I have been told recently by university graduates, that they do not want to do web development because it is too difficult. I have been told by my own employees that they do want to specialize in backend only, or front-end only. My friends, back in 2007, did not want to do web development because it was not real programming to them. They considered the work inferior, less prestigious and less difficult than, say, programming enterprise Java or desktop applications. Young graduates of today, that I spoke with, are more likely to choose Objective-C (or Swift) or Java programming because it’s easier than web development. If you have missed it, you must see [Ryan Stout](https://github.com/ryanstout) talking about complexity in web development at [RubyConf 2014](https://www.youtube.com/watch?v=7i6AL7Walc4). First 8 minutes will do the trick. We must have taken wrong turn at some point, if we ended up in the place web development is right now.

## What exactly has been introduced for Rails 5?

David Heinemeier Hansson ([@dhh](http://twitter.com/dhh)) introduced two key components of Rails 5: Turbolinks 3.0 and Action Cable. While Turbolinks 3.0 are not entirely new (you can grab the “master” branch of the Github repository and try it already), Action Cable is new kid on the block.

Turbolinks 3.0 is not revolutionary (but rather evolutionary) step forward. So far, the library worked by replacing the whole content of the page with new HTML, returned from the server. In most cases, this felt faster for the user, because no JavaScript or extra assets had to be re-downloaded from the server, CSS was already there. It caused some minor problems for libraries based on observing document.ready, but nothing that could not be [worked around](http://reed.github.io/turbolinks-compatibility/). In new release, you have a choice to do partial updates. If you add new comment, you can request that only the list of comments will be updated, leaving the rest of page untouched. This is performed with unobtrusive JavaScript `data-` attribute tags and/or server-side Rack middleware that wraps rendered HTML blocks in appropriate JavaScript code. In your Rails controllers you only do have to specify something like: `render :index, update: :comment`. No extra JavaScript has to be written in majority of cases.

Action Cable is a new concept for extending Rails functionality with real-time message passing with WebSockets. Two days before RailsConf 2015, I was playing with [Phoenix Framework for Elixir language](http://www.phoenixframework.org/). The part that stood out, was the integrated WebSockets layer. Couple of weeks ago, I also played with [Play framework](https://www.playframework.com/) for Java (I do not digest Scala easily). It also has integrated WebSockets functionality into the framework. These were clear inspirations for [@dhh](http://twitter.com/dhh). It’s not fashion, this is based on real-life requirements for building modern web applications. Out of 5 projects I worked on last year (2014), 3 had real-time/push functionality built in. Two had chatrooms. We were thinking about building a Rails template that includes Faye or Pusher preconfigured to speed up building future projects. It turns out, this feature is so demanded that [@dhh](http://twitter.com/dhh) wants to include it in Rails. My experience tells me this is requested often enough to be part of his default backpack. Shipping WebSocket layer within Rails means that we can start to build engines that will integrate with it. Creation of reusable chat component, or websocket-based notification system that can be plugged into multiple applications, just became way easier.

The third interesting thing that is going to be released with Rails 5 is integration of [rails-api into Rails itself](https://github.com/rails/rails/pull/19832). For those who missed it, rails-api makes it easier to build slimmer, faster, API-only Rails applications that… can be ideal backends for SPAs. As you can see, [@dhh](http://twitter.com/dhh) is not neglecting existence of SPAs (or other API consumers), or a need to support this style of development.

## Backpack? It might be just good enough

My company is often building solutions for start-ups. I understand what the ‘backpack’ analogy and ‘integrated systems’ mean for speed of development. The fact that got our jaws dropped in 2007 was that you could build a startup in a month, week or even a day. Rails came with latest goodies bundled. It came with REST, prototype.js, it had sessions built in and ORM. Rails had ERB views and flash messages. It was amazing: all components were there, you just had to put them together into software you wanted. Of course this had bad sides. Rails applications of that era could be slow, unreliable and painful to maintain. None of that mattered if you built microblogging platform before competition did. If you were the first Twitter, you already won the market share and could afford a rewrite in Scala, Java or whatever works best.

Having comprehensive backpack with familiar tools, means that your developers just need to learn those tools. They will be productive, they will follow conventions and not reinvent the wheel. At the same time, Rails is not losing anything of it’s flexibility. If you want to add React to the equation: go ahead. If you decide to build the whole application as API + SPA, go ahead! Having some tools bundled by default, does not mean you cannot exchange them with the ones you prefer (or the ones that will better do the job in your particular use case).

At some point, the expression ‘the rails way’ gained negative meaning. I do not think that people who mean that, understand that it’s not about going back to the ugly pile of hacks from 2007. You do not have to put logic into your models if you don’t feel like doing so (I will not mention controllers). We (as a Ruby community) gained lots of experience during last few years, that we should use to build better apps. I do not put any logic into my models, I even do not put validations there. But I still consider the approach ‘the Rails way’, it does not have to sound bad. I do not believe that the defaults [@dhh](http://twitter.com/dhh) chose for Rails 5 are that bad. If you do not like Turbolinks, you still can disable it. But if it’s good enough for your use case, you get that amazing performance boost at virtually no cost. This is ‘the Rails way’ in my understanding.

## Your future stack

Are Turbolinks going to stay? I seriously doubt it. I suspect the idea will be evolving and we will see Opal.rb and Virtual DOM (React? vDom?) mixed into the equation. Isomorphic Ruby maybe (another buzzword!)? [Volt Framework](http://voltframework.com/) might steal the Rails’ thunder at some point, but it’s not quite there just yet. Maybe less revolutionary approach of [React on Rails](https://github.com/reactjs/react-rails) will take over the world (possibly thanks to [that publication](http://blog.arkency.com/rails-react/))? It looks like, however, there is still going to be space for traditional applications, that return HTML from the server, and are not SPAs, at least in foreseeable future. That means Rails is not going away anytime soon.

## Final words

Announcement of Rails 5 does not mean you have to trash your Ember app just yet. There are valid use cases for building Single Page Applications. Rails is great as a backend for that use case, and it is going to get only better with inclusion of rails-api into core framework.

I would encourage you, however, to be sceptical about your choices. Are you really choosing best tool for the job? Does additional cost/effort is justified by the value your business/customers get? Is SPA necessary, good to have or unnecessary introduction of two extra layers of abstraction? Those are some of the questions you have to ask yourself when you start a new project.

## Links

[DHH’s keynote on RailsConf 2015](http://replay.li/) - yes, it’s Ember app and it’s great use case for one

![](https://www.amberbit.com/images/people/hlepicki.jpg)

### Post by Hubert Łępicki

Hubert is partner at AmberBit. Rails, Elixir and functional programming are his areas of expertise.
