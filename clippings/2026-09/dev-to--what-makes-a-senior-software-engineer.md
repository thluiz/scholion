---
url: "https://dev.to/klnusbaum/what-makes-a-senior-software-engineer"
captured_at: "2026-09-25T00:24:33+01:00"
title: "What Makes A Senior Software Engineer"
domain: "dev-to"
---

As a Senior Software Engineer here at Uber, I often spend time helping to mentor newer software engineers. One of the questions I get asked most often from my mentees is “How do I become a Senior Engineer?”

This is a complex question. Any true answer will contain caveats and nuances. However, in my opinion there is one broad answer that cuts to the core of the question. The distinction between a Junior Engineer and a Senior can be boiled down to a one word difference:

> Junior engineers **build on the** rails, Seniors **build the** rails.

What I mean by this is that Junior Engineers are going to be building on the work already done by Senior Engineers. Senior Engineers essentially multiply the work they do by creating technologies/architectures that enable other engineers to write better code.

* * *

Let's look at an example. Back when I was at Facebook on the messenger team we had a problem: implementing new message types required changes across our entire stack. Changes needed to happen across multiple layers of abstractions on both clients and the backend. It was a huge pain in the assÂ¹.

Together with the help of several other engineers, I helped build a technology called XMAs (extensible message attachments). The result of building XMAs was that adding a new message type became as simple as making single, small change on the backend and a corresponding single, small change on each client.

New types of messages that would've taken months to develop using a team of engineers could now be built in a week or two with a handful of engineers. The work my team and I did enabled easy development of new features, increasing developer productivity. We built out new rails.

* * *

It's worth noting that we based our XMA technology off of another technology at Facebook, Story Attachments. The engineer who had built that was, in my opinion, working at higher level than a Senior Engineer. They had enabled engineers to enable even more engineers, further multiplying their effect.

Think about some of the most esteemed engineers you know. The Kent Becks, the Dennis Ritches, the Grace Hoppers. What's the one thing they all have in common? They've enabled thousands of engineers to write better software.

That's really what growing as an engineer is, enabling larger and larger amounts of engineers to do more work. So if you find yourself wondering how you can improve your abilities as an engineer, try asking yourself a different question: how can I enable other engineers to be better?

* * *

_Kurtis Nusbaum is a Mobile and Backend Developer at Uber. He's an avid long distance runner and diversity advocate. Here's his [mailing list](http://tinyletter.com/kurtis). Here's his [Twitter](https://twitter.com/klnusbaum), and [LinkedIn](https://www.linkedin.com/in/knusbaum). Here's his [github](https://github.com/klnusbaum). If Kurtis seems like the kind of guy with whom you'd like to work, shoot him an e-mail at [kcommiter@gmail.com](mailto:kcommiter@gmail.com)._

* * *

Â¹ As a general rule of thumb, if something is a huge pain in the ass for you, two facts can be assumed: it's a pain in the ass for others, and creating a solution is highly leveraged work. Problems like these are ripe for the fixing and will most likely enable other engineers.
