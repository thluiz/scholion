---
url: "http://timkadlec.com/2015/02/client-side-templatings-major-bug/"
captured_at: "2015-02-10T10:55:05-03:00"
title: "Client-side MVC's major bug - TimKadlec.com"
domain: "timkadlec-com"
---

# Client-side MVC's Major Bug

Over the past year I conducted performance audits on a handful of sites that all used client-side MVC’s, typically Angular but not always. Each site had their own optimizations that needed to take place to improve performance. Yet a pattern emerged: client-side MVC’s were the major bottleneck for each. It slowed down the initial rendering of the page (particularly on mobile) and it limited our ability to optimize the critical path.

So I get a great deal of happiness from reading posts from much smarter folks than I who are rallying against this all-to-common mistake.

Back in December, [The Filament Group analyzed a bunch of client -side MVC frameworks](http://www.filamentgroup.com/lab/mv-initial-load-times.html) to see their impact on the initial load time of a page. The results to render a simple To-Do app were disappointing:

- Ember: 5s on a Nexus 5, 3G connection
- Angular: 4s on a Nexus 5, 3G connection
- Backbone: 1s on a Nexus 5, 3G connection

Only Backbone scores in a way that is at all acceptable, particularly in a world where people are trying to break the 1000 SpeedIndex barrier.

And just last month PPK wrote up his [thoughts on client-side templating](http://www.quirksmode.org/blog/archives/2015/01/angular_and_tem.html). The full post is well worth your time, but for those of you who would like to cut to the chase:

> I think it is wasteful to have a framework parse the DOM and figure out which bits of default data to put where while it is also initialising itself and its data bindings.

> Populating an HTML page with default data is a server-side job because there is no reason to do it on the client, and every reason for not doing it on the client.

[I’ve said it before](https://twitter.com/tkadlec/statuses/512677101292756992): if your client-side MVC framework does not support server-side rendering, that is a bug. It cripples performance.

It also limits reach and reduces stability. When you rely on client-side templating you create a single point of failure, something so commonly accepted as a bad idea that we’ve all been taught to avoid them even in our day-to-day lives.

“Don’t put all your eggs in one basket.”

It’s pretty good advice in general, and it’s excellent advise when you’re wading through an environment as unpredictable as the web with it’s broad spectrum of browsers, user settings, devices and connectivity.

This might sound like I’m against these tools altogether. I’m not. I love the idea of a RESTful API serving up content that gets consumed by a JavaScript based templating system. I love the performance benefits that can be gained for subsequent page loads. It’s a smart stack of technology. But if that stack doesn’t also consist of a middle layer that generates the data—in full and on the server—for the first page load, then it’s incomplete.

This isn’t idealism. Not only have I seen this on the sites I’ve been involved with, but companies like [Twitter](https://blog.twitter.com/2012/improving-performance-on-twittercom), [AirBnB](http://nerds.airbnb.com/isomorphic-javascript-future-web-apps/), [Wal-Mart](http://radar.oreilly.com/2014/10/isomorphic-javascript-with-lazojs.html) and [Trulia](http://www.slideshare.net/bigethan/isomorphic-javascript-at-trulia) have all espoused the benefits of server-side rendering. In at least the case of the latter three, they’ve found that they don’t have to necessarily give up those JS-based templating systems that everyone loves. Instead, they’re able to take advantage of what [Nicholas Zakas coined “the new web front-end”](http://www.nczonline.net/blog/2013/10/07/node-js-and-the-new-web-front-end/) by introducing a layer of Node.js into their stack and sharing their templates between Node and the client.

This is where it gets interesting and where we can see the real benefits: when we stop with the stubborn insistence that everything has to be done entirely on the client-side and start to take advantage of the strengths of each of the layers of the web stack. Right now most of the progress in this area is coming from everyday developers who are addressing this issue for their own sites. Ember is aggressively pursuing this with FastBoot and [making exciting progress](https://twitter.com/tomdale/status/555153656127840256). React.js emphasizes this as well. But most of the other popular tools haven’t made a ton of progress here.

I sincerely hope that this starts to change, sooner rather than later. Despite what is commonly stated, this isn’t a “web app” (whatever that is) vs “website” issue.

It’s a performance issue.

It’s a stability issue.

It’s a reach issue.

It’s a “building responsibly for the web” issue.
