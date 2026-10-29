---
url: "https://www.amberbit.com/blog/2015/12/22/when-choose-elixir-over-ruby-for-2016-projects/"
captured_at: "2016-01-09T18:06:09-03:00"
title: "When to choose Elixir over Ruby for 2016 projects?"
domain: "amberbit-com"
---

# When to choose Elixir over Ruby for 2016 projects?

##### 2015-12-22

You are planning to build something in 2016, aren’t you? Some decisions
have to be made, team to be hired. For a few years now you have been
relying on Ruby (and Rails) for all your work and you have been
reasonably happy. You have been hearing a lot about this new
[Elixir](http://elixir-lang.org/)
thing and considering giving it a shot? Let me tell you a bit more about
it and help you make a good decision.

## Ruby on Rails

A few years ago, Ruby on Rails exploded with popularity. A lot of people
switched from PHP to build web-based systems better and faster. Plenty
of Java folks made a switch too, being happy to deliver things way
faster now. Many advantages Ruby had over other languages are still
valid. The same can be said about Rails framework. The company I am
happy to be part of, [AmberBit](https://www.amberbit.com/) has been
building Rails-based apps to satisfy clients for many years now. Just as
many other Ruby developers, we have been looking for alternatives for
some time now. You probably want to know why.

## Change

The web changed *a lot* since the year 2006. If you don’t believe me,
[have a
look](https://web.archive.org/web/20060110071818/http://facebook.com/)
at some of the sites on [web.archive.org](http://web.archive.org/). The
web changed it’s look and feel, but also changed the way it works. The
applications are way more heavy on the front-end. They need to speak to
different variety of devices, and usually handle more traffic. The
overall [number of Internet
users](http://www.statista.com/statistics/273018/number-of-internet-users-worldwide/)
tripled during last 10 years. Users’ expectations about web apps changed
too. People don’t want to wait or reload page to see the effect. They
want to see more and more live/instant updates. Almost all systems we
have built at [AmberBit](https://www.amberbit.com/) these last couple of
years, had more or less features like that. We have been joking about
making a “real-time Rails app” template that integrates Faye, share.js
and couple of other useful tools into the standard stack. In fact, this
is [where Rails slowly evolved in the
end](http://weblog.rubyonrails.org/2015/12/18/Rails-5-0-beta1/) by
introducing [ActionCable](https://github.com/rails/actioncable).

## When to stick to Rails in 2016

Having said all the above, Ruby on Rails [may be just
enough](https://www.amberbit.com/blog/2015/4/22/why-rails-5-turbolinks-3-action-cable-matter-and-why-dhh-was-right-all-along/)
for you. Let me show you a few cases where I think it’s still a great
fit.

### 1. Internal apps for your organization

If you want to build internal app, that is heavy on forms and user
input, Rails may be a perfect choice. Those sorts of applications are
usually not receiving so much traffic. They are not exposed to the
general traffic on the web. You don’t expect anything fancy. All you
need is a tool that will help you improve the processes in the
organization. Ruby on Rails comes with good support for data validations
via third party or built-in functions. There are libraries to choose for
authentication and user management. You can also pick some templates to
help you style the thing on your own. From my experience, a lot of
companies rely on building such apps. They are willing to spend limited
amount of money on building them. The budgets tend to be reasonable -
yet limited. Rails helps to meet those constraints.

### 2. Prototypes

Not all prototypes I may say. This depends on the system you are
building. The nice thing about Rails is that you can put together a
“scaffold” for your app in just a few days. User authentication,
administrative dashboards, permissions management come all in form of
third party plugins. This means your developers don’t need to write all
the code to handle the boring stuff. They will spend most of their time
building the core features instead. That is what makes your system
different, unique. The stuff that investors will look into when making
financing decisions.

Word of caution here: you may be required to dump the code base
altogether at some point in future. Scaling Rails is not easy, and one
of the major reasons you may want to go with Elixir instead!

### 3. Systems with limited target user base

In many cases, your system will be targeting specific group of people.
If you are not expecting hundreds of thousands of concurrent users at
the same time, you will avoid the scaling problems altogether. Ruby on
Rails does not scale easily I am afraid.

### 4. Systems that nicely divide into smaller subsystems

One of the patterns we have been using to work around issues with
scaling, is splitting the apps. If you can divide your monolith to
smaller parts easily - go for it.

Some systems can be split into identical instances serving different
people. You can run a number of instances of your app, on dedicated
servers instead. It can simplify the design too. Multi-tenancy is not an
issue, since apps connect to dedicated databases.

Good example of a system that may be doing that behind the scenes is
Slack. You set up organization account, that is identified by a unique
URL. Those URLs for may be pointing to the machines running
independently. Doing this will also make your systems independent of
each other. Being more resistant to total system failures is an
advantage. Worst thing that can happen is the failure that affects all
your clients. You want to keep the failures as much localized as
possible.

### 5. Systems that can use caching effectively

To avoid scaling issues (again) you may want to use caching techniques.
Ruby on Rails may be still a good fit for you if you are expecting high
traffic, but you *can cache* most of your pages. This is very true for
web publishing platforms, blogs, news sites and so on. We have been
using caching to avoid system overload in times of high traffic spikes
in many projects now. That said, not all high-traffic systems can use
content caching in equal amount. Caching is hard when your system
provides personalized experience.

## When would I recommend choosing Elixir over Rails?

### 1. High-traffic systems

Typical Rails app responds in tens or hundreds of milliseconds to web
request. Elixir applications can respond in microseconds instead. This
can be put to great use. You can handle more requests on the same
hardware. Elixir is simply faster by an order of magnitude.

Erlang and Elxir, are great fit for modern hardware. It has been
evolving to having more and more number of processors. Ruby will have
issues trying to provide work for all the cores. This is the same case
with other “traditional” programming languages - like Python too.
Elixir’s programs are built in distributed manner even if they run on
single machine. This allows you to use the resources you have better.

### 2. Systems that do stuff asynchronously

Integrating with external services may require doing things
asynchronously. Ruby and Rails is not really great with waiting and
responding to asynchronous events. Sometimes this lack of being able to
perform things in asynchronous manner makes “easy” thinks ridiculously
difficult.

Last year we have been building a system that had to send a greeting
message over Pusher channel exactly 5 seconds after user signed up.
Combine it with a high number of subscribers, and Ruby’s inability to
handle threads to get the idea. Similar issues will arise when you are
in a need of communicating with external web services, run slow database
queries etc.

Ruby does not come with tools to create pools of workers. Supervising
them and handle asynchronous communication will be difficult too.
Erlang/OTP does help. You can design all sorts of asynchronous systems
easier in Elixir. Your developers will have to write less code. They
will re-use existing patterns and libraries rather than trying to
re-invent the wheel.

One could argue this is the typical area of expertise of Node.js. This
is right. In my opinion, the approach Elixir takes here is way better.
The code will be cleaner and easier to maintain. There is a good chance
the overall performance will be improved too. This is thanks to *true*
concurrency that the Erlang VM supports.

### 3. Distributed / clustered systems

It is usually better idea to scale horizontally if possible, rather than
vertically. This means that instead of buying a bigger, more expensive
server system, you get yourself 3, 5 or ten ones. They are
semi-independent machines. The idea is that you connect them in some
sort of networked fashion. Handling the incoming requests is performed
in some sort of shared manner. You may want to randomly distribute
requests to all nodes. This can be done in fact in Ruby with a proxy
sitting in front of your “cluster”. If you want to share state between
those nodes in any way, you need to rely on external to Ruby tools such
as Redis.

Ruby comes with a distributed computing solution called dRB or
Distributed Ruby. It’s designed in a way that exposes objects over a
network. It also handles incoming requests in new threads. You probably
know how this is going to turn out. Erlang and Elixir rely on message
passing rather than function calls and sharing state. This makes it
perfect for building systems, that are decentralized and fault tolerant.

### 4. High-availability systems with true zero-downtime

Elixir can help you maintain 100% up-time, while still delivering
updates to the production system. This is possible thanks to Erlang’s
ability to do code hot-swapping. The feature has been in use for years
by telecom companies. You don’t really get interrupted calls when they
need to update their software. If your systeem will rely on being
available 24/7 and it’s critical you won’t miss a single request - go
with Elixir.

### 5. Server-side push and real-time applications

I have mentioned ActionCable when discussing advantages of Rails. The
fact is, that Elixir’s main web framework
[Phoenix](http://phoenixframework.org/) had similar functionality
built-in before. I haven’t seen benchmarks of ActionCable yet. I do
have, however, pretty solid experience with Faye library it’s based on.
I suspect it won’t scale well, especially when generating a lot of
server-sent messages. We [do
know](http://www.phoenixframework.org/blog/the-road-to-2-million-websocket-connections),
that Phoenix channels do scale really nicely already.

### 6. Large applications

If the code base of your application is expected to be large, go with
Elixir without further thinking. Elixir has a built-in tools, such as
[umbrella
projects](http://elixir-lang.org/getting-started/mix-otp/dependencies-and-umbrella-apps.html)
that allow you to split the code base into chunks. You can do similar
thing with Ruby’s gems, but there is fundamental difference in
philosophy behind. Systems running on Erlang’s VM can be split into
“applications”. The individual processes also share no memory. They
communicate via sending and receiving messages. The code is more loosely
coupled by design enforced by the language itself. I found maintaining
the large code bases one of the greatest challenges. Developers do
appreciate a system that facilitates tools making it easier from day 1.

### 7. When you need smart, experienced developers

Your stack of choice can be a filter for the developers you are hiring.
I am observing experienced developers migrating from Ruby to Elixir or
Clojure these days. If your goal is to hire the best of the best, you
may want to use the technology as a filter to get to them. Ruby’s
ecosystem is flooded with junior developers. This is a result of the
great demand for the developers in the technology. There is way less
Elixir developers out there, but if they took their time to learn new
stack, that’s a good sign of their skills.

## Summary and shameless advertising ;)

If you are still not decided, I am happy to help. Just drop me a line at
[hubert.lepicki@amberbit.com](https://www.amberbit.com/blog/2015/12/22/when-choose-elixir-over-ruby-for-2016-projects/mailto:hubert.lepicki@amberbit.com) and we
can talk it over. I may be even able to provide you with a great dev
team for either stacks - if you need one!

by [Hubert Łępicki](https://www.amberbit.com/blog/2015/12/22/when-choose-elixir-over-ruby-for-2016-projects/mailto:hubert.lepicki@amberbit.com) -
[@hubertlepicki](https://www.amberbit.com/blog/2015/12/22/when-choose-elixir-over-ruby-for-2016-projects/twitter.com/hubertlepicki)
