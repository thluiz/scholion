---
url: "http://devblog.avdi.org/2014/02/23/rumors-of-rubys-demise/?utm_source=rubyweekly&utm_medium=email"
captured_at: "2014-03-05T11:04:25-03:00"
title: "Rumors of Ruby’s Demise | Virtuous Code"
domain: "devblog-avdi-org"
---

# Rumors of Ruby’s Demise

Periodically someone on the Internet becomes aware of concurrency-oriented programming languages like Erlang or Scala, and climbs up the bell tower to sound the “is Ruby dying” bell. This topic came up on [Parley](http://parley.rubyrogues.com/) recently. A few people asked me to post my reply publicly, so here it is, with some embellishments.

First though, a disclaimer of sorts: it’s perfectly reasonable to suspect me of having a bias here. After all, most of my work in the past ~7 years has been in Ruby. And I make a lot of money from books and screencasts about Ruby. So yeah. Bias.

I’m not a “Rubyist”, though. I’m a hacker. As I state below, I like to think that any implicit bias I have towards Ruby is because using it is pragmatic as well as *fun,* to a degree I haven’t found in any other language. That said, other languages are fun too. Honestly I’ve been looking for an excuse to use Clojure on a real project; something that just cries out *this can’t be done, or even prototyped, as easily in Ruby*. I’m sure those projects exist; one just hasn’t come across my desk recently.

Anyway, onwards to my original reply…

---

I regularly dive into other languages, and Ruby is still the most programmer-friendly mainstream language I’ve used, by a long shot. I think as long as programmer joy enters into the picture at all, Ruby will still be a contender, and the desire of developers to use Ruby will drive its implementations to be more performant. Also, if Matz ever gets around to baking higher-level concurrency features into the language I suspect they’ll be wonderfully well thought-out and easy to use, because Matz.

I do wonder if the focus on concurrency and scalability is a little overblown. There’s a natural bias, because it’s only the largest organizations that have incentives which drive them to create whole new languages like Go and Clojure to solve their massive problems. Then they naturally capture the spotlight, because they are big, and new tech is interesting, and massive problems are interesting, and “scaling a big system stories” are the supermarket checkout tabloid fodder of the programmer world. Everyone wants to have that amazing scaling story to tell.

Meanwhile, I suspect 80% of programmers are still working on problems where their development velocity is a much bigger problem than how many hits their server can take before falling over. I dunno, maybe my view of the industry is skewed. I just don’t think there are really that many developers, statistically speaking, who can cite system capacity as their current problem #1. Or #2, or #3.

It’s kind of like [when we talked to Ilya Grigorik](http://rubyrogues.com/135-rr-http-2-0-with-ilya-grigorik/) recently, and he was talking about how most companies are using lots of binary protocols to link their systems together internally. And James and I were like “um, I think you’re thinking of Google, not most companies”.

Another thing to keep in mind: the most important asset your team has is your shared understanding of the problem. There are lots of great scaling stories out there that don’t involve replacing the language; they just involve quickly rewriting a major component to have a more performant design once the team had a better handle on the problem space. It’s easy to overestimate how much time you’ll save by making “scalable” choices up front, ignoring the fact that most successful system eventually experience a rewrite or three regardless. Maybe that rewrite happens to be in Clojure or Elixir because with your improved understanding, you realize how you could use their special features to great effect.

Final thoughts – you should, of course, use the best tool for the job. In my book that doesn’t mean pondering long and hard over what the right tool will be a year from now. It means whipping out my friendly pocket Leatherman tool, and only hauling the big toolbox once I’ve satisfied myself that the Leatherman is insufficient. *My* Leatherman happens to be Ruby.

---

So that’s my original reply. James Edward Gray then piped up with the following anecdote:

> This is just one datapoint, but…
>
> - I currently work on an SOA system that’s about 30 processes talking to each other
> - We aired a 70 spot TV ad earlier this week in Germany (our primary market)
> - The publicity pushed our peek performance up to 40,000 requests per minute
> - This system is all Ruby, except for a tiny Node.js frontend
>
> I won’t say we didn’t see problems at this scale. We did. But it held up, even running at those speeds.
>
> I’m now testing a set of changes based on the things we saw during the traffic peek. I’ll have it ready to deploy in another day or two tops and it will drastically speed the system up from where we already are. In the worst cases, I’m seeing tasks take about 3% of the previous time.
>
> This is real world production code. We’re just finding bottlenecks and fixing them, like you do.
>
> Also, we’re just using MRI.

---

I think there’s a kind of peer-pressure when you’re deeply embedded in the developer community to switch to the new hotness or fall woefully behind. For instance, I feel like I *really* ought to be studying Backbone, Angular or Ember right now. The other day I wrote a single-page realtime chat app for fun, and just assumed that I’d need to plug in one of those frameworks once I got to the client-side part. As it turned out, all I wound up needing was a few lines of jQuery.

The important thing to keep in mind is that *[nearly] every new hotness was developed to solve someone’s specific problem*. And if it’s really, really hot, that’s probably because it solved a really, really hard problem. If you have the same problem, it behooves you to sit up and take note. But bear in mind that just because your CMS app delivers data via HTTP and someone else’s realtime statistics visualization app also delivers data via HTTP, does not mean you have the “same problem”.
