---
url: "https://blog.moodle.net/2018/elixir-choice/"
captured_at: "2020-09-07T16:48:24-03:00"
title: "Why did we choose Elixir for the backend development of MoodleNet? – MoodleNet"
domain: "blog-moodle-net"
---

# Why did we choose Elixir for the backend development of MoodleNet?

[admin](https://blog.moodle.net/author/admin/ "Posts by admin") 

[Technical](https://blog.moodle.net/category/technical/) 

October 5, 2018October 11, 2018 
3 Minutes

Welcome to a new series of technical posts on the MoodleNet blog! These won’t show up on the front page but will be included in the [RSS feed](https://blog.moodle.net/feed/). We’ll also post links to them to the MoodleNet [Twitter account](https://twitter.com/moodlenet), and to the [moodle.org forum](https://moodle.org/mod/forum/view.php?id=8352).

---

Hi everyone, I’m [Alex Castaño](https://blog.moodle.net/2018/introducing-alex/), the newest member of the MoodleNet team! [Mayel de Borniol](https://blog.moodle.net/2018/welcome-mayel/), our technical architect, is currently on holiday, so I thought I’d get the ball rolling here.

Back in August, Mayel did some research around languages for both frontend and backend development. After talking with people and reading a lot of information, he decided that we should use [Elixir](https://elixir-lang.org/) for backend development. I am obviously very pleased that he made this decision, as I’ve been working with Elixir for the past few years!

![saad-salim-765833-unsplash_1200x.jpg](blog-moodle-net--why-we-chose-elixir-for-moodlenet-backend/ced6819570d527490ea129caa382e855.jpg)

Some people, both within Moodle HQ and the Moodle community, have asked why we’re using Elixir for MoodleNet. Fortunately, Mayel has written a very detailed [wiki page](https://docs.moodle.org/dev/MoodleNet/tech/stack) explaining the benefits and drawbacks of Elixir, and in particular using the [Phoenix framework](https://phoenixframework.org/). Here are some of the benefits:

1. **Performance** – “The Phoenix web framework has been found to perform better than Rails, PHP, and Python. One benchmark showed Phoenix handling over 10x more requests than Rails in a given period. Phoenix was also much more consistent under load – Rails was more prone to have some requests bog down. This can cause a “chain reaction” because Rails apps are configured with a fixed number of application processes, so if some of them are slow, it can mean that others have to wait in line, which dramatically increases the app’s response time.”
2. **Scalability** – “The Erlang VM’s model of concurrency is great for multi-core CPUs, but it was created before they existed. Its original purpose was to support concurrency and fault-tolerance via the use of many different machines. This makes it an excellent tool for building systems that can handle more load by simply adding more servers.”
3. **Developer productivity & happiness** – “When people argue about programming languages, often the performance card is pulled (“this language is so much faster in these benchmarks”). But performance isn’t the only consideration: while it’s possible to just add more servers, developer time often costs more than servers. More important then is which framework helps write software faster, of a better quality, and which benefits the programmer’s wellbeing.”
4. **Reliability** – “While Elixir is a fairly new language, it is mostly a friendly interface to the Erlang virtual machine, which has been used since the 80s to build some of the most reliable systems in the world: telephone systems. It is made for running a complex system with almost no downtime, like having multiple levels of “supervising” processes in a system to reboot parts that have errors. Basically, microservices before microservices were cool.”
5. **Concurrency** – “CPUs are no longer getting dramatically faster each year. Instead, we get machines with more cores. Our code can run faster, but only if it can run concurrently – meaning, different bits of code run simultaneously on different cores.”
6. **Simplicity** – “For modern web applications (written in languages like PHP or Ruby on Rails) to do everything we require of them, they depend on a lot of other pieces running on the server… In Elixir, on the other hand, it is possible to spin up a nearly limitless number of processes as needed.”
7. **Flexibility** – “Using Phoenix and Elixir opens the door to building applications that are not possible with other web frameworks.”
8. **Correctness** – “Elixir’s [Ecto](https://hexdocs.pm/ecto/Ecto.html) database library embraces database constraints, with built-in support for adding them, catching constraint violations, and turning them back into friendly user-facing error messages.”

As Mayel points out, there are some downsides to Elixir, but these are mainly to do with its relative newness and potential difficulty in finding developers. However, the MoodleNet team has already solved the second of these problems in finding me!

**Read more**: <https://docs.moodle.org/dev/MoodleNet/tech/stack>

### Share this:

### Like this:

Loading...
