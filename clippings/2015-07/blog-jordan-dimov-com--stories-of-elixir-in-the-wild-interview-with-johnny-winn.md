---
url: "http://blog.jordan-dimov.com/stories-of-elixir-in-the-wild-interview-with-johnny-winn/"
captured_at: "2015-07-09T15:12:43-03:00"
title: "Stories of Elixir in the Wild: Interview with Johnny Winn"
domain: "blog-jordan-dimov-com"
---

# Stories of Elixir in the Wild: Interview with Johnny Winn

09 July 2015

In the first part of this series [I talked to Shane Logsdon](http://blog.jordan-dimov.com/stories-of-elixir-in-the-wild-chatblend/) about ChatBlend's use of Elixir to power their back­end API.

This time I interview Johnny Winn ([@johnny\_rugger](https://twitter.com/johnny_rugger)), who has written several open­-source projects in Elixir, each having a reasonably high adoption rate: [calliope](https://github.com/nurugger07/calliope), [inflex](https://github.com/nurugger07/inflex), and [chronos](https://github.com/nurugger07/chronos).

**JD: Did you enjoy the interview with Shane Logsdon?**

JW: It's always great to hear about companies using Elixir and lately it seems like I am hearing about them more and more. Shane has been around the Elixir Community for some time but I don't think I have ever heard his story. The most I knew was his work on the [Sugar web framework](https://github.com/sugar-framework/sugar) and more recently on [Placid](https://github.com/slogsdon/placid).

**JD: Can you tell us a bit more about each of your open-­source Elixir projects and how they came to be?**

JW: My Elixir projects were as much about me learning the language as overcoming functionality I missed from Ruby. I remember starting with [chronos](https://github.com/nurugger07/chronos), a time formatting library, because dealing with datetimes as tuples was tedious. Also, I wanted some features that I could use in testing with functions like `days_from/2` or `beginning_of_the_week/1`. It was a simple tool but its functionality was very useful to me.

Next, I built a very small [Elixir library to pluralize/singularize words](https://github.com/nurugger07/inflex). Originally, it was used in Phoenix and additional functionality was added for parameterization and camel casing. It has since been removed from Phoenix but still widely used.

My largest undertaking was [calliope, a haml parser](https://github.com/nurugger07/calliope). The designer that I used to work with asked for it. She did the designs for the Elixir Fountain, plus a couple of other projects, and preferred haml. Calliope, by the way, is in the middle of a major overhaul. I am looking to move away from regular expressions and begin leveraging Elixir's AST format to simplify parsing.

It's an exciting time to get into Elixir because of the opportunity to create, or recreate, tools while learning the language.

**JD: You are also in the process of starting a new project initiative at your current company, can you provide some more details on that?**

This is still in the very early stages but it’s moving forward. We started with a monolithic Rails application that was moved to a service-based architecture. Now it is being divided into micro­services and I saw that as an opportunity to mix in Elixir. Smaller segments of the application can be written and tested with Elixir. I am positive that those segments will out-perform their Ruby counterparts.

**JD: This sounds very interesting. José Valim has recently written a great piece about [Elixir and microservices](http://blog.plataformatec.com.br/2015/06/elixir-in-times-of-microservices/). What aspects of Elixir do you find most useful in your work?**

JW: Elixir offers an elegant simplicity that doesn't suffer from a lack of power. It makes it easy to convey intent without jeopardizing performance. Some of that elegance stems from the combination of pattern matching and recursion. In fact, those are two of the features I miss the most when I go back to Ruby. I think I've even mentioned that a few times on twitter.

**JD: What did you struggle with the most?**

JW: Immutability. It's that simple. Josh Adams and I were just discussing this in an Elixir Fountain episode and I recalled one of my first hiccups with it. I had been working with Dynamo, the original Elixir web framework, and ran into an issue passing the conn variable into a function expecting it to be updated. I was kicking myself after that one, but live and learn, right?

**JD: What improvements would you like to see in Elixir or the ecosystem?**

JW: One thing I just thought of the other day, but haven't had a chance to look into, would be the ability to hotswap code changes while debugging. This isn't a completely crazy idea, because Smalltalk has a similar functionality and it would be interesting to say the least.

**JD: Which non-­Elixir books or resources would you recommend to people who want to become better Elixir developers?**

JW: If you are like me and coming from a object­oriented background I would recommend [Functional Programming for the Object-­Oriented Developer](https://leanpub.com/fp-oo) by Brian Marick. It uses Clojure but the concepts help you grok the paradigm. One of my favorite Erlang resources is [Learn You Some Erlang For Great Good](http://learnyousomeerlang.com/). I found myself searching for various concepts or documentation and it always seemed to be at the top of the list. It really seems to serve as the unofficial documentation for Erlang. The book is free on-line, but I ended up buying a copy to support the author.

---

Johnny Winn is [@johnny\_rugger](https://twitter.com/johnny_rugger) on twitter and [nurugger07](https://github.com/nurugger07) on github. He is also author of the upcoming book "[Elixir for the Functional Rubyist](http://elixir-for-rubyists.com/)."

Make sure to check out the [Elixir Fountain](https://soundcloud.com/elixirfountain), your biweekly podcast for news and interviews from around the Elixir community. For daily news follow [@elixirfounatin](https://twitter.com/elixirfountain) on twitter.

If you or your organisation has successfully used Elixir in a real-world project, please fill in the [Elixir in the Wild](http://goo.gl/forms/9VYvslUb2t) survey.
