---
url: "https://medium.com/@kenmazaika/why-im-betting-on-elixir-7c8f847b58"
captured_at: "2015-05-26T14:57:11-03:00"
title: "Why I’m betting on Elixir — Medium"
domain: "medium-com"
---

# Why I’m betting on Elixir

  
  

### And why you should too, unless you want to become a maintenance programmer.

  
  

***Background:*** *I’ve spent the past 6 years building web applications in Ruby and the Rails framework. I’ve flirted with new programming languages as they came out, but Elixir is the first language that has been able to captivate me.*

### Ruby Crushed It!

The ruby language and the Rails framework completely changed the way web applications were built; it started a religion of values that the community cared about. It pioneered the idea that the tools programmers use should be optimized for developer happiness and productivity.

It made the bold challenge that it is developers’ jobs to make sure their code was adequately tested and worked. Other languages and frameworks scoffed at the approach, until it started winning. Then they started incorporating principles from the ruby community in their language and framework.

![1*IT_FzO1BsR1YhuWsWXfCaQ.png](medium-com--why-im-betting-on-elixir/4dbb477331e8b887301350f6100570a7.png)

Ruby went from humble beginnings as an obscure language to one of the most popular languages, largely because of the Rails framework and tremendous leadership from people like DHH, Wycats, Aaron Patterson, Jose Valim and a ton of other superstars.

### But every so often, artifacts of ruby’s humble beginnings arise

#### Run-away memory!

In Zed Shaw’s infamous “Rails is a Ghetto” post, he rants about how problems with garbage collection required early Rails applications restart their processes around every 4 minutes in order to remain live.

One of the most popular rails servers out there today is unicorn. My production web application is a Rails application that is fairly simple, in comparison to other applications I’ve worked on. I moved the application to a 512MB DigitalOcean droplet following standard instructions. After being deployed for several days, my unicorns had eaten all available memory and the application was quite slow.

The solution? The [unicorn-worker-killer](https://www.digitalocean.com/community/tutorials/how-to-optimize-unicorn-workers-in-a-ruby-on-rails-app). It’s not unlike the solution from the early days.

My DigitalOcean droplet can handle two unicorn worker threads, which take most of the resources, and Postgres database and few other applications. Request times are okay though, so it gets the job done.

#### Concurrency!

I’ve spent years of developing Rails applications, **I have never spawned a new thread in a production Rails web application**. Rails itself is thread-safe, but I have the awareness that ***there be dragons*** when dealing with different threads, having used them heavily in Java, C++ and other object-oriented languages.

The fact is, that I don’t want to think about mutexes, semaphores, or anything like that. Pausing one thread, while executing another one doesn’t seem like it’s really concurrent anyway. Plus, are you ***sure*** your code doesn’t cause deadlocks?

Since the testing is a core tenant of the ruby community, it’s not a surprise that most ruby developers stay away from using threads as they’re basically un-testable, and tend to produce bugs that are difficult to reproduce.

I, like most sane Rails developers, use [sidekiq](https://github.com/mperham/sidekiq) or [resque](https://github.com/resque/resque) to process things in parallel. [Rails 2.2](http://weblog.rubyonrails.org/2008/11/21/rails-2-2-i18n-http-validators-thread-safety-jruby-1-9-compatibility-docs/) added thread-safety, but [Rails 4.2](http://weblog.rubyonrails.org/2014/12/19/Rails-4-2-final/) added the Active Job API, which in my opinion is a heck-of-a-lot more useful.

But background jobs are just that, done in the background. Mission critical stuff should remain in the main process, so you can react to failure or make sure transactions go through successfully before completing the task.

#### Speed!

I’m selfish. I value my time. I value it a lot. And that’s why test speed is something I care about. I spent [serious time](https://www.youtube.com/watch?v=V7g9amBX92A) optimizing my test suite performance, without making changes to the architecture of the application and causing test-induced-design-damage.

For a time the project I was working on had unit and functional tests that took just over 20 minutes! At the time I tested using hydra for distributed Rails tests, but I had a hard time getting the test suite to pass (likely due to an obnoxiously complex codebase, with some of the ***not-so-the-best*** code in it ☺).

Even test startup time started to take a long time, around 40 seconds. Ever wait 40 seconds to see: “*syntax error, unexpected end-of-input, expecting keyword\_end*”, or a similar foolish syntax goof-up? I have.

The solution? [Zeus](https://github.com/burke/zeus). A wonderful gem that pre-loads typical start-up stuff for a Rails app and can (according to GitHub):

> Boot any rails app in under a second.

I seriously love this gem and suggest you use it if you’re a Rails developer.

But, how were the developers able to achieve this? They wrote the core of it in friggin’ Go.

#### Scala

A couple years ago, I got super stoked about Scala. Then I started using it, and promptly started hating it.

It’s has a lot of functional programming concepts. The [akka framework](https://github.com/akka/akka), allows highly concurrent fault tolerant applications. It runs on the JVM so any Java library is fair game to use, and the JVM is incredibly well tuned for performance.

The language itself I found enjoyable, I liked pattern matching. The deal breaker for me? The JVM. Package management for jars IMO is seriously overcomplicated, when comparing it with Rubygems and Bundler.

There are a bunch of solutions: SBT, Maven, Ivy, but they all make me cringe when I need to import someone else’s library. Maybe I’ve been spoiled by Ruby, but Ruby’s package management is core to my productivity.

The other thing that bothered me about Scala was the libraries I was using were largely written in Java by people with an entirely different set of values than I have.

Building Scala web applications with the Play! framework felt like building a Java web application with the Play! framework, except with slightly better syntax and the ability to do pattern matching. While Play! is influenced by Rails quite a bit, the difference is visceral.

#### The Elixir Ecosystem

**Package Management with Mix**

When first venturing into playing with Elixir, I encountered Mix. Mix is like a hybrid of Bundler and rake in ruby. What blows me away about Mix is this: **it doesn’t feel worse than Bundler and Rake**. It doesn’t seem a lot better either, but the bar is incredibly high and meeting it is impressive!

Mix just does its job nicely, stays out of the way, and doesn’t force you to wrangle XML.

**The Erlang Virtual Machine**

Elixir runs on the Erlang virtual machine and embraces most of the values of the Erlang community. Both Elixir and Erlang pride themselves for an emphasis on functional programming that are fault-tolerant and highly scalable.

In most talks about Elixir you can watch on YouTube the following stories about Erlang:

- Erlang is powering around 50% of telecom networks. When was the last time your phone had “Scheduled Maintaince”?
- WhatsApp, which was acquired for billions of dollars, was running millions of processes on a single server, supported 450 million users, and had only 32 engineers.

These values are the same type of values that the Elixir community embraces. Because of this as an Elixir developer, when you use Erlang supervisors or the [cowboy http](https://github.com/ninenines/cowboy) server, you don’t feel like you’re sacrificing your values.

**The Phoenix Web Framework**

The [phoenix framework](https://github.com/phoenixframework/phoenix) is clearly heavily influenced by Ruby on Rails and coding a Phoenix Web Application feels a lot like coding a Rails app. I love the Rails router. I love ActionController, ActiveRecord, Rails Views and the way you code web application. I like the organization of Rails applications.

Phoenix is such a *Railsy* solution you’ll feel like you’re building a Rails app, with the exception being that it runs with Elixir and has all the benefits of Elixir and the Erlang virtual machine.

Phoenix also supports WebSockets through channels. It basically gives you the ease of use of WebSockets that Firebase provides with fine-grained control.

Did I mention it’s fast? It’s fast as lightning. Check out these logs from my $5/month DigitalOcean droplet. That’s right microsecond request speeds from a single core machine:

![1*O8sLJiIZ0Ny5A53cIHBLwQ.png](medium-com--why-im-betting-on-elixir/2fab5abe1cbfa7e1c828152c1fc38b76.png)

**Strong Leadership**

In my opinion, the difference between open source and ***movement***, is all around the leadership involved in the project. In short, I believe really smart people need to be ***putting the work in*** to improve the software every single day.

The Rails movement gained so much momentum because of all the work put in by DHH, Aaron Patterson, Jose Valim, Wycats, and a ton more brilliant people. Rails wasn’t launched at v1 and people stopped doing the work.

[It’s old-school put in the work mentality](http://instagram.com/p/yJ5JskI-ZK), and [building a community takes work](http://instagram.com/p/yXrMS-I-V9/)!

Jose Valim, Chris McCord, and all the members of the Elixir-Lang core team and Phoenix core team have, and continue to put in the work that needs to be done for the Elixir community to thrive.

### Friends, the web is about to under-go a transformational change

Let’s face it. CRUD apps are a commodity these days. The next: *AirBnB for Renting Ketchup* probably isn’t going to survive.

The people who will win are going to be the ones who embrace changes in technology. The fact that WebSockets, processes, and concurrency in Phoenix and Elixir are cheap, without sacrificing developer happiness is an absolute game-changer.

I totally love Ruby on Rails. It completely changed the way that people thought about building web applications from 2005–2014.

I expect Elixir and Phoenix to have a similar impact from 2015–2025.

If you want to start building web applications with Phoenix and Elixir, [**check out this tutorial**](http://phoenix.thefirehoseproject.com/), I built.

### *If you found value in this article, it would mean a lot to me if you hit the recommend button!*
