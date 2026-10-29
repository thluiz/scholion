---
url: "https://github.com/dotnetfringe/dotnetfringe.github.io/issues/73"
captured_at: "2016-03-29T16:07:07-03:00"
title: "What is the burning question for the future of .NET / Core CLR / Mono today? · Issue #73 · dotnetfringe/dotnetfringe.github.io"
domain: "github-com"
---

# What is the burning question for the future of .NET / Core CLR / Mono today?

[Adron](https://github.com/Adron) opened this Issue 8 days ago
· 25 comments

### Labels

[question](https://github.com/dotnetfringe/dotnetfringe.github.io/labels/question "question")

### Milestone

No milestone

### Assignee

No one assigned

### Notifications

You’re not receiving notifications from this thread.

### 14 participants

.NET/FRINGE/ member

What do you see as the burning issues and questions of the community today?

- Will Core CLR work? When will it be usable in production?
- What's the lifespan of Mono, since it's still the only real viable .NET x-plat solution?
- How will Xamarin fit into the fold at Microsoft?
  - What new OSS directions will MS & Xamarin's team bring to the community?
  - What's the future hold for mobile as MS pushes toward a more iOS & Android future?
- What's the future hold for distributed systems @ Microsoft? Will Orleans or Akka .NET bring us a viable disitributed systems story finally for the .NET Community (or would you argue it already has?)
- What does the future hold for F#? Microsoft seems to putter along but the F# Community has delivered some of the most modern and advanced capabilities for the .NET stack with F#, what would it take to get more of the community involved with the language?
- Java has an absurd level of libraries, in many cases far outpacing the .NET stack and with Core CLR, the entire list of libraries needs rewritten. How do you see the community filling that gap? How are you contributing to bringing the Core CLR to the forefront and into the future?
- How will Microservices shape the future of Nancy, ASPNET, and related frameworks and tools? Will it relapse into a more heavy handed SOA style architecture?

What other things weigh on your mind about the future of the .NET Stack? Will C# continue it's dominance in the stack? Will new languages crop up to fill the weak spots of C#? Will more learn F# to bring its strengh into more focus and push the stack forward as Scala has been used in the Java stack? Will things continue to be simplified following KISS to make the ASPNET stack more and more like how Node.js has come to form the server side JavaScript stack?

Let's talk, throw in a comment or three! [anexo ausente]

All good questions, and yet I can only think of one... Is the recent push of .NET to OSS/\*-nix too little too late? I mean what does .NET bring to the stack/community that doesn't already exist?

I am interested in F# but that Microsoft is the origin of it gives me pause. I have invested time in other frameworks that were awesome only to have the rug pulled out and the lights turned off. C# has history and if nothing else maintenance work for the forseeable future. F# needs to continue being adopted by the community until the point at which it has a chance to survive its creators. As for dotnetcore 1.0, they need to deliver the next beta, which they are actually going to go ahead and call a release candidate. I am hopeful it will be great all sarcasm aside. The writing is on the wall in pink neon spray paint that dotnetcore will supplant all of the current stable AspNet stuff. Along with where and how we write web apps in .net. I don't think the majority of dev and devops folk know about the new x-plat dev workflow and tooling. Which could make adoption a challenge. The teams at Microsoft really need to finish up and get dotnetcore 1.0 feature complete so we can put all this waiting behind us and get our apps to work on the new platform.

I see some interesting questions around the business adoption and implications of an OSS .NET stack. The part of me that does OSS in my free time and loves the community thinks it's great, but the part of me that earns a living developing line of business apps for crusty old-school companies is giving that other part the side-eye.

For example, it took the legal team at my organization over 6 months to review and agree to sign the MS CLA. And they're still not thrilled with all this hippy OSS taking over our infrastructure. I'm guessing this attitude probably exists at a lot of enterprises where the dev team is either small or the old ways of thinking are still entrenched. I know MS is going to offer non-OSS licenses for the official releases, but what about the overall shift in posture towards an entire OSS stack and heavy reliance on third-party OSS libraries?

I guess the question for those of us in the OSS community is what we can do to make the transition easier for these organizations. Are there any steps we can or should take when building our own libraries to make them "enterprise-friendly"? Should that even be a goal?

[@bm2yogi](https://github.com/bm2yogi) : good question. to my mind we all benefit from the diversity of the ecosystem. it may well be true that .NET won't revolutionize OSS/\*-nix. to me it does at least 3 things: (1) it keeps .NET in the game, (2) it enables those familiar with the stack to use their skills and target/embrace different platforms (3) it provides an alternative. who knows in the future things may be different. if there is a push in this direction I'm all for it.

I am interested in knowing if the CoreRT with its native compilation will have first class ARM support which would allow more efficient programming on medium sized embedded platforms.

Has CoreRT made much penetration in the market [@vercruysb](https://github.com/vercruysb)? I ask because I honestly don't know and have seen very little about it in the media/conversations, etc.

I also just read a good post by [@arielbh](https://github.com/arielbh) <http://blogs.microsoft.co.il/arielbh/2016/02/27/microsoft-acquiring-xamarin-my-take/>

[@daveaglick](https://github.com/daveaglick) yeah, the whole OSS vs. not OSS debates in companies are still tough, meanwhile a huge majority of programmers just keep using OSS - especially in .NET - and just not even talking about the fact they're doing it. Any new project pretty much pulls in a ton of Nuget packages that have all sorts of licenses and corporations are often blind to this fact, and have poor structures to even contribute back for all the **inadvertent mooching** they're doing. It's rather hilarious to me, but for .NET it would be nice if some of the companies would actually contribute back some for all the mooching they do. Especially the fortune 500 which uses .NET so heavily, and also respectively a ton of OSS (I mean, even .NET is OSS these days, LOLz)

As for "enterprise-friendly" I wouldn't concern myself with that. It really is just stick a pertinent license on it to make them happy, throw on a large price tag, an SLA, a support model, a thoroughly confusing configuration model, and boom it's enterprise ready. I've seen some things born out of enterprises, but it's **always** like how things are described in Innovator's Dilemma - an outside acquisition is made, it's bought, or some other way is found to innovate because the large enterprise doesn't/won't/can't do it. So just insure they're slightly (or far) behind the curve in the land of safe versions and safe software and they it ought to be enterprise-friendly enough IMHO. ;)

[@anewton](https://github.com/anewton) one of the good things about F# IMHO these days is it isn't under Microsoft at all anymore. That hurts it in some ways, but it also gives it the freedom to have one of the most active OSS contributor core out there. The ecosystem around it is currently working, production ready, and blows past Core CLR w/ just use of Mono. I wish Microsoft could pull off what the community has or would at least become a 100% partner - don't get me wrong they contribute - but it's in bits and pieces and often ignore the ecosystem and languages since it's slightly out of their grasp now. Microsoft AND the community have a huge chance to make F# one of the bleeding edge tools out there, but currently my bets are if it happens, it'll be entirely because of the community.

Re: distributed systems story, Orleans and Akka.net are actor frameworks, does a distributed system require an actor framework to be viable/successful?

On the SOA question, I'm assuming you're inferring to SOA *vendor's* heavy-handed approaches. SOA itself was never heavy handed. Then absolutely, we're seeing that today, with vendors jumping whole hog onto the microservice bandwagon - look no further than "docker" becoming synonymous with microservices.

- Will Core CLR work? When will it be usable in production?

> CoreCLR will work, and probably be production ready from end of 2016, though 'bet-the-farm' would be mid-2017. The biggest CoreCLR problem remains the clarity of branding message about how to built C# solutions 'tomorrow'. MS may need to shift emphasis to clarify there is a new clean platform that you can transfer your skills too, but would be a migration effort for an application. It also needs to clarify between CLR and Native which are both targets. I would suggest a new 'brand' instead of .NET for the new CLR, and a clearer message around building for different targets. UWP is still too confusig considering the point of a reboot should be to 'simplify' not obfusticate.

- What's the lifespan of Mono, since it's still the only real viable .NET x-plat solution?

> I would expect to see increasing convergance of the Mono and CoreCLR codebases, with pull and push in both directions, but timescales for one and one only would feel more like 2019 than imminent.

- How will Xamarin fit into the fold at Microsoft?

> I would guess the toolchain for x-platform development

- What new OSS directions will MS & Xamarin's team bring to the community?

> I think it's less about new as delivering a framework that takes us from the app in small data center world of .NET to apps in IAAS or PAAS of 'post.NET'. Small runtimes, progressive download, faster update cycles, leaner base class libraries. The competition is node.js etc.

- What's the future hold for mobile as MS pushes toward a more iOS & Android future?

> The UI is shallow in a world where most of the functionality lives on the server, so the question is how much value x-platform gives when you probably need to write device specific UI code. I'd expect changing paradigms of development, a re-emergence of conversations about thin client to be more telling than x-platform over time. What interests me here is that there is a lot of knowledge locked in the .NET community from being the key desktop development toolchain on how to build 'smart' clients that is transferrable to mobile. I would be interested to see opportunities for MS to leverage that before it vanishes.

- What's the future hold for distributed systems @ Microsoft? Will Orleans or Akka .NET bring us a viable disitributed systems story finally for the .NET Community (or would you argue it already has?)

> Akka is a greatl products although there are other 'distributed' platforms than the Actor model i.e. broker (Brighter, MassTransit, NServiceBus) that may be an easier transition, or just using HTTP self-hosted services (though that raises issues of availability if handled naively). Orleans and MS Fabric offerings are platform dependent and so may not get traction in the wider space.

- What does the future hold for F#? Microsoft seems to putter along but the F# Community has delivered some of the most modern and advanced capabilities for the .NET stack with F#, what would it take to get more of the community involved with the language?

> The key problem for F# is that C# is good enough, so the pressure to move is low for most developers and the higher salaries commanded by F# developers can be a disincentive outside of finance as CTOs worry how to resource teams. Crossing the chasm really needs either a 'killer framework' (in the same way that Rails was a 'killer framework') that everyone wants to use which drives adoption, or greater prevalance of success stories built on F# like Jet.com.

- Java has an absurd level of libraries, in many cases far outpacing the .NET stack and with Core CLR, the entire list of libraries needs rewritten. How do you see the community filling that gap? How are you contributing to bringing the Core CLR to the forefront and into the future?

> With a cleaner space the opportunity is actually to clean the slate. the opportunity to build new frameworks can create interest in a platform as it creates chances for developers to grab mindshare. We will be supporting CoreCLR with Brighter (although we have a dependency on a CoreCLR RabbitMQ client for folks using that Broker). As a newer library we would hoppe that CoreCLR support gave us a chance to become better known.

- How will Microservices shape the future of Nancy, ASPNET, and related frameworks and tools? Will it relapse into a more heavy handed SOA style architecture?

> Lots of folks will build microservices using HTTP over Brokers so Nancy and ASP.NET Core have a role to play. I don't think that the ESB issue is quite as prevalent in .NET where smart endpoints and dumb pipes was often the rule. Most tooling was of the lightweight broker variety, outside of the BizTalk hell that some enterprises entered. So I think the reflexes of many .NET devs are more attuned to this world. I think a bigger danger is the lack of practitioners experienced at distributed systems and significant ramp up for the community to understand the trade-offs.

- With all this focus on web and server technologies, what is the future of desktop application development?
- Is there any plans to consolidate all the different XAML platforms into one?
- Will there be forward movement of the XAML platform, or will there just be more v1.0 releases of XAML for different systems (Linux XAML 1.0, Mac XAML 1.0, etc)?

- With all this focus on web and server technologies, what is the future of desktop application development?

> I don't know, but x-platform using [Chrome Apps](https://developer.chrome.com/apps/about_apps) or [Electron](https://github.com/atom/electron) are a threat to native platforms on desktop. Most of them look good and allow html/css/js as the language of choice for development.

We went that way, with a custom container that used .NET/Mono and embedded chromium but is otherwise similiar to the Electron idea.

[@iancooper](https://github.com/iancooper) Electron/html/css/js is one option for greenfield development, but it requires retraining of your xaml developers, and rewriting of your existing xaml projects. So not ideal.

Similar to [@lenadroid](https://github.com/lenadroid) comment. Here is our issue log for this: [iancooper/Paramore#45](https://github.com/iancooper/Paramore/issues/45)

[@distantcam](https://github.com/distantcam): longer term I suspect we'll see a rich MS tooling narrative (perhaps through Xamarin) for building WebAssembly artefacts from XAML.

Perhaps with the new componentised Core stack we'll see better LLVM artefacts too XAML targeting android and iOS?

I have a question. With Node and .NET co-existing more and more. Will we see Native node modules compiled from .NET as opposed to marshalling / bridging tech like edge.js? I've had a few gigs whereby the "distributed" has been more about interop than anything else introducing costs.

.NET/FRINGE/ member

[@jbogard](https://github.com/jbogard) re: SOA - yeah, that is what I was referring to, since the heavy-handed nature of vendor solutions (and seriously, when it comes to enterprises, when is it not a heavy handed approach to things, bumps the billable hours right?) SOA strikes me overall as a reasonable approach to things, and as someone (was it you?) mentioned, microservices is just the new "Thought Leaders" high billable talking point. Cool ideas and I dig em', think there is a lot of good stuff there. But it also seems evolutionary not particularly revolutionary. Docker however and immutable infrastructure, from an infrastructure point of view definitely seems revolutionary more than evolutionary. But I digress...

Distributed system probably needs defining. When I think of a truly effective, powerful, and really useful distributed system I think of high availability, no single point of failures, large scale or prospectively large scale # of instances, with the capability to spread compute/storage or whatever the system is about across many instances. Of course, Oracle, Microsoft, and other companies have called all sorts of things distributed systems, including highly SPOF (Single Point of Failure) systems like SQL Server, Oracle DB, Exchange, etc and I tend to refer to those as vertical scaled/vertical oriented server systems and not distributed systems. In much of the distrib/cloud dev circles that I went to work with when leaving the MS enterprise world (i.e. I went to Basho, Tier 3, New Relic, other providers and users of large distributed systems w/o SPOFs - or at least extremely minimized SPOFs to almost zero) it seems they don't talk about these things like that either as distributed systems. So...

On that note - I tend to see akka .net and orleans as possible ways to get more of the systems that are readily available and fairly mature now in JVM & Node.js land (i.e. Netflix's, Walmart Labs, etc all have very developed microservices + minimal SPOF streaming, distrib systems, etc). Currently I've been consulting with and am helping companies get streaming data, large scale, distributed w/ minimal or no SPOFs and in every situation I'm forced to bring in an arsenal of JVM/Node.js tools to use with .NET / Core CLR / Mono tooling which is a great and fun challenge, yet from a business perspective it leaves companies scratching their head as to why they're using .NET if it requires all this trouble to get these capabilities. I honestly like the challenge, and am tech neutral on the matter, but it comes up a lot and I end up explaining the situation as best as I can.

[@edblackburn](https://github.com/edblackburn) re: UI & Native style apps. I expect in the coming years we'll see more bridged, more x-plat UI platforms around Xamarin's stuff & things like Electron as [@distantcam](https://github.com/distantcam) mentioned. But also I imagine hacks to make things appear native similar to how [@iancooper](https://github.com/iancooper) mentioned w/ the project above.

Also [@iancooper](https://github.com/iancooper) mentioned "I think a bigger danger is the lack of practitioners experienced at distributed systems and significant ramp up for the community to understand the trade-offs." <- this I've seen first hand, and imagine and I'm preparing to deal with more of this until more of the distributed systems concepts and practices are understood. Honestly, it's going to cause some huge heartache and heartburn for some companies and coders dealing with said things, but I'm looking forward to the coming challenges - super excited about it!! :)

As for .NET Core, I'm stoked when I see things like [iancooper/Paramore#45](https://github.com/iancooper/Paramore/issues/45) and [akkadotnet/akka.net#992](https://github.com/akkadotnet/akka.net/issues/992) (As [@lenadroid](https://github.com/lenadroid) and [@iancooper](https://github.com/iancooper) mentioned) This movement of OSS projects (and comparable projects that are closed like Project Rider) I think, and am confident, that they will prove pivotal to the future efforts and success of the Core CLR (.NET Core, whatever it ends up being called) projects.

.NET/FRINGE/ member

[@edblackburn](https://github.com/edblackburn) per "... Node and .NET co-existing more and more. Will we see Native node modules compiled from .NET as opposed to marshalling / bridging tech like edge.js? I've had a few gigs whereby the "distributed" has been more about interop than anything else introducing costs."

That's a good question. Honestly I keep seeing a ton of companies just going whole hog with Node.js to remove the need for interoperability at the application tier. Other companies I see implement them side by side, but often with them remaining in silos. It's hard to say from my vantage point which way things will go in this regard. When Core CLR is really working and operable - I think we'll see pretty rapidly (6-12 months after a solid working version is out) whether it is going to gain traction and really get people porting/moving to the platform or if Node.js and other tooling will continue to bleed the C#/.NET/Core CLR Ecosystem of developers.

What I'd like to see, is a solid Core CLR get released that is 100% solid x-plat dev that can really be used wherever - using C# to implement greenfield apps on Linux or otherwise opens up the stack to an honest inroad to the startup and related parts of the industry and opens up enterprises to a lot of additional tech that do want to keep/use/expand on C#/Core CLR use. Pre-Core CLR .NET still really doesn't offer a whole lot of choices around these options. Again, that's my vantage point from the Silicon Valley/San Francisco/Seattle/Redmond tech scene. I'm curious how others see and what they'd like to see for the success scenario with Core CLR / C# / F#, some have been chiming in, but laying out more of "what we'd like to see" brings it closer to fruition! :)

[@iancooper](https://github.com/iancooper)

> Orleans and MS Fabric offerings are platform dependent and so may not get traction in the wider space.

Orleans is platform agnostic.

I guess I'm confused, I was building large-scale systems with no SPOF for Dell.com like 10-12 years ago on the MS stack. We scaled up and down with the holiday seasons, just in a more manual fashion. But it wasn't OSS and it wasn't cheap. I'm watching the microservices community go through the exact same pains and problems the SOA community went through over a decade ago, like doing HTTP APIs everywhere and assuming that it's somehow better than the CORBA then SOAP solutions. Same constraints, different tech, but now much more available.

If your clients don't care about what tech they use, why go in assuming .NET needs to be used at all? Most of my customers have existing investments in .NET, so to move off would be a substantial risk.

.NET/FRINGE/ member

[@jbogard](https://github.com/jbogard) what are you confused about? I couldn't put my finger on the exact pain point.

As for clients, I don't make that assumption. Sounds like we're in a similar boat. For those existing investments I like to see paths like Core CLR that opens up options in the future that don't leave .NET apps stuck primarily on Windows Server.

The weekly ASP.NET Community Standup puts their Q&A info up on the .NET Web Development and Tools Blog ( <https://live.asp.net/> , <https://blogs.msdn.microsoft.com/webdev/> ). There are a bunch of good questions up there as well. Today I was hoping there would be news about RC2 dates but they are now swamped with getting ready for the //build conference. Instead Damian Edwards basically said they have 5 teams or more across all of dev-div working on it, and writing a reset for x-plat is hard work. [@iancooper](https://github.com/iancooper) was saying it won't be "bet the farm" ready until mid-2017 and I have to agree.

[@Adron](https://github.com/Adron) currently in the market most definitely not, however I have been following it for some time now and I do like what they are trying to do and certainly when they support ARM which could enable all kinds of IoT like scenario's and eco systems. I do not know if this is what they envision also but this is something I would like to see happening.

[@Adron](https://github.com/Adron) I probably misread it, it looked like originally an assertion that a viable distributed system ecosystem requires an actor framework, whereas I think you were speaking in the general, not the specific.

I think Service Fabric will have a big part in the Microsoft narrative. It’s apparently based on Orleans and is cloud and platform neutral with APIs for .NET, PHP and Node? This may help the enterprise market, whose constituents invariable have a heterogeneous hosting and platform environments, many having public / private clouds. I suppose Azure will have excellent management facilities for Service Fabric to encourage you to use that cloud offering.

Will Core play nicely with other stacks? Things that interest me are:

1. Writing native node modules in .NET. For node and Electron, so VS Code extensions could be written in .NET too?
2. Extensions for the CoreCLR/RT Trying to make “everything” cross platform seems a fools errand to me. Not everyone is going to want “everything” on every platform. Examples would be:

   - Access to various filesystems, an extension with hooks into Hadoop (libhadoop.so?) would be useful for example. Perhaps something like FUSE, or even FUSE?
   - First class actors within the CoreCLR would be fascinating could “Orleans” actually be an optional extension within the CoreCLR allowing other frameworks to sit atop? I know Beam offers this on steroids but Erlang isn’t accessible to everyone, why not compete with Elixir / Phoenix now?
   - Interop with other platforms? Native integration with Rust and V8 / ChakraCore would be interesting. A native JS story would be an enlightenment(!) Allowing people to extend the CoreCLR in rust for example could help foster an ecosystem of extensions?

I Appreciate that nuget and C# could accomplish much of this but I suspect closer interop with the runtime will offer better performance and opportunities for cross language support too.

[@Adron](https://github.com/Adron) Whilst the Node / .NET setup started with frontend devs using node and backend devs exposing their components with a combination of queues (for writes) and web services for reads. I too am noticing that Node is eating more and more into the .NET “backend” space for the organizations that took such an approach.

One client whose .NET backend populated an Elastic Search cluster that their Node components used as a read source decided to replace the .NET with more node or java component by component, whilst replacing their SQL Server db with Postgres because their BizSpark programme was drawing to a close and compared to their homogeneous private cloud peacemeal migrating to Linux and Amazon was fiscally a no brainer.

I’m hearing more and more variants of this story. I suspect this is a motivating factor behind .NET “Core”.

Regarding distributed software, MBrace it's a great framework that is very flexible, easy to use and non prescriptive. There are also libraries for both AWS and Azure that allow distributed programming for many use cases.

Attach files by dragging & dropping,
[selecting them](https://github.com/dotnetfringe/dotnetfringe.github.io/issues/73?utm_content=buffer17717&utm_medium=social&utm_source=twitter.com&utm_campaign=buffer#), or pasting
from the clipboard.
[anexo ausente] Uploading your files…
Unfortunately, we don’t support that file type.
[Try again](https://github.com/dotnetfringe/dotnetfringe.github.io/issues/73?utm_content=buffer17717&utm_medium=social&utm_source=twitter.com&utm_campaign=buffer#) with a
PNG, GIF, JPG, DOCX, PPTX, XLSX, TXT, PDF, or ZIP.
Attaching documents requires write permission to this repository.
[Try again](https://github.com/dotnetfringe/dotnetfringe.github.io/issues/73?utm_content=buffer17717&utm_medium=social&utm_source=twitter.com&utm_campaign=buffer#) with a PNG, GIF, or JPG.
Unfortunately, we don’t support that file type.
[Try again](https://github.com/dotnetfringe/dotnetfringe.github.io/issues/73?utm_content=buffer17717&utm_medium=social&utm_source=twitter.com&utm_campaign=buffer#) with a PNG, GIF, or JPG.
Yowza, that’s a big file.
[Try again](https://github.com/dotnetfringe/dotnetfringe.github.io/issues/73?utm_content=buffer17717&utm_medium=social&utm_source=twitter.com&utm_campaign=buffer#) with a file smaller than 10MB.
This file is empty.
[Try again](https://github.com/dotnetfringe/dotnetfringe.github.io/issues/73?utm_content=buffer17717&utm_medium=social&utm_source=twitter.com&utm_campaign=buffer#) with a file that’s not empty.
This browser doesn’t support file attachments.
We recommend updating to the latest
[Internet Explorer](https://www.microsoft.com/ie),
[Google Chrome](https://chrome.google.com/), or
[Firefox](https://www.mozilla.org/firefox).
Something went really wrong, and we can’t process that file.
[Try again.](https://github.com/dotnetfringe/dotnetfringe.github.io/issues/73?utm_content=buffer17717&utm_medium=social&utm_source=twitter.com&utm_campaign=buffer#)
