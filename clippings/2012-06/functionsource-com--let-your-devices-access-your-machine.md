---
url: "http://functionsource.com/post/let-your-devices-access-your-machine"
captured_at: "2012-06-08T11:48:56-03:00"
title: "Let your devices access your machine"
domain: "functionsource-com"
---

Sam Stephenson has published [Xip.io](http://xip.io/), “a magic domain name that provides wildcard DNS for any IP address.” All written in CoffeeScript and node!

  

It probably reminds you of [\*.localtest.me](http://readme.localtest.me/), which does the same thing… but it only works for localhost (127.0.0.1).

  

With Xip.io, you can get to another IP simply by putting it in the domain (e.g. “foo.bar.10.0.0.1.xip.io resolves to 10.0.0.1″).

  

That is all well and good, you can now through a domain into Mobile Safari and get there on the local network, but what about sharing beyond? That is a job for [showoff.io](https://showoff.io/). This takes things to the next level as you now actually go to a public IP which is routed to your machine.

  
> gem install showoff-io  
>  show 3000

  

At this point you can share a URL that will really get you through to localhost. Good stuff!

  
   
   
   
 from FunctionSource Posts <http://functionsource.com/post/let-your-devices-access-your-machine>
