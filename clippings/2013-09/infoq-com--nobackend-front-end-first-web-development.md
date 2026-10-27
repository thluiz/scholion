---
url: "http://www.infoq.com/news/2013/05/nobackend"
captured_at: "2013-09-27T10:17:01-03:00"
title: "NoBackend: Front-End First Web Development"
domain: "infoq-com"
---

# **N**oBackend: Front-End First Web Development

by
[Zef Hemel](http://www.infoq.com/author/Zef-Hemel) 
on
May 02, 2013
*|*

At the [Front-Trends 2013 conference](http://2013.front-trends.com/)  last week, Gregor Martynus gave a talk entitled "[Look ma, no backend**!**](https://speakerdeck.com/gr2m/look-ma-no-backend) " about developing applications primarily from a front-end perspective, falling back to using server-side components only to implement the features the browser does not yet support**.** This approach is the opposite of how web applications have traditionally been developed: focusing primarily on the server-side part of an application, and then enhancing the application with front-end techniques**.** A website named [noBackend](http://nobackend.org)  was launched to further evangelize this idea**.**

InfoQ spoke to Gregor to find out more**.**

**noBackend is all about writing applications without focusing on the back-end, why is that interesting, or something we should aspire to -- what advantages does it have**?****

> We went pretty far with making the process of building apps very easy**.** But still, when I want to make an app, I start by thinking about how to do the back-end stuff first: what technology I'm going to use, what database**.** The design process of building an app is still dictated by the back-end world and its constraints**.** And I think: it doesn't need to be that way anymore**.** I think, from a users perspective, the design and user experience of an app is unique, nobody cares "how things work**.**" noBackend tries to reflect that by suggesting a front-end driven design process, where "everything is possible" at first, and then work backwards from there**.**

**Is a backend-less web application really possible, what are its limitations**?****

> When saying noBackend, I do not suggest that apps don't need a backend at all, I agree that the term is confusing, but it's catchy**.**  
> What I mean by noBackend is: you don't have to *think* about the backend any more**.** You don't have to differentiate about what a browser can do and what a browser cannot do today**.** We can fill the gaps with JavaScript today, hiding away that in reality it talks to a server behind the scenes**.** The front-end developer doesn't need to care**.** That's very empowering.
>
> From the technology perspective, there are two things that we need for a smooth frontend developer experience:
>
> 1. CORS, to make cross domain AJAX requests**.**
> 2. Async code, be it callbacks, events, or promises**.**
>
> Both are here today. So we're ready to do this now.

**Your site mentions [dreamcode](http://nobackend.org/dreamcode/) , what is that**?****

> When we started to work on [Hoodie](http://hood.ie) , we started with the JavaScript API facing the frontend developer**.** That's what we care most about**.** We don't care how complex things are behind the scenes, it has to be as simple as possible for the user**.** We decided to forget about all the constraints and think: "Okay, I want to sign up a user, what would be the simplest piece of JavaScript code to do that**.**" I've listed [some more use cases on our site](http://nobackend.org/dreamcode/) **.**
>
> A good example is jQuery**.** jQuery did an amazing job to provide an API that is both simple and powerful, and I think it's the #1 reason for its success**.**
>
> Another thing that's really cool about dreamcode: every developer can do it**.** No matter how experienced you are, you can dream code**.** Indeed, if you're a beginner, you might even have advantages as you are not thinking in the constraints that are branded into our senior developer brains**.**
>
> And dreamcode is the tool to lead the design process of an app the noBackend way**.** Usually, you'd tell the backend developers what you need, let's say user accounts, sending emails, uploads**.** The backend developers would build it, come back wit a RESTful API that the frontend people would then need to wire up using jQuery's AJAX methods for example**.** Instead, the frontend people can describe the exact needs of the users of the app with dreamcode, that now is the interface between the frontend and the backend, and both sides can work against it**.**
>
> From a backend perspective, dreamcode is:
>
> 1. Just another name for [BDD](http://en.wikipedia.org/wiki/Behavior-driven_development) /[TDD](http://en.wikipedia.org/wiki/Test-driven_development)
> 2. A successor of a REST API, which is simpler to define and more flexible when it comes to future changes**.**

**What are the security implications of noBackend's generic back-ends**?** For instance, what prevents a user from using an email API from the JavaScript console and using it to spam people**.****

> Nothing**.** noBackend defines just how to send an email the simplest way**.** Of course, I do agree that things have to be secure, when it comes to sending email, or receiving payments, you name it**.** I just think that the frontend API does not need to reflect that**.** It should be super simple**.** The logic to prevent SPAM should live on the server instead**.** For example, you can prevent visitors to send emails if they don't have an account**.** Or if they try to send more then 10 emails per minutes**.** These are problems that backend people are solving since ages, they are good at it**.** The frontend people just don't want to be bothered with it, and it's worth a lot to them**.** That I'm sure of**.**
>
> If you want to build the next heroku, take away all the pain that is the backend, provide a beautifully crafted frontend, and then: take all my money**.**

**How does noBackend relate to Backend-as-a-Service**?** The ideas sound very similar.**

> Backend-as-a-Service is a special kind of noBackend, and also describes it from the business perspective, while I try to use noBackend to put the UX developer perspective into the discussion**.**
>
> For example, [Firebase](http://firebase.com)  is Backend-as-a-Service, so is [Parse](http://parse.com) , [Kinvey](http://kinvey.com)  or [Backendless](http://backendless.com) **.** Then there are open source solutions that I still consider noBackend solutions, but you have to host them yourselves or hosting is optional, like [hood**.**ie](http://hood.ie) , [remotestorage.io](http://remotestorage.io)  or [deployd.com](http://deployd.com)

**Some of the noBackend services listed on your website (such as remotestorage**.**io and hood.ie) mention the ability to work offline and synchronize when an Internet connection is available**.** Is this important primarily for mobile applications, or does offline capability have wider relevance**?****

> The ability to work offline is not (only) about allowing users to work with apps without internet connection**.** It eliminates latency. And therefore provides a fantastic user experience**.** Take minutes.io as an example. It stores everything you do right away, while you're typing, to your browser's local cache**.** Then, in a second process, the data gets synced to the server**.**

**Is this the new way to develop applications, or does it only make sense to develop applications the "noBackend way" for a certain category of applications**?****

> I think every new technology is only for certain kinds of applications**.** It's a different approach that especially fits applications that hold most of its logic in the frontend, where the user experience is the most important feature**.**
>
> It's just another tool that developers should be aware of, especially the front-end developers, as noBackend solutions might be great tools to empower them build apps they wouldn't able to build by themselves before noBackend**.**

The [noBackend](http://nobackend.org)  website [lists a number of existing back-end solutions](http://nobackend.org/solutions/)  that can be used to start building noBackend-style applications today**.**

### Tell us what you think

**Re: Is this old**?****
by
"Yuriy Ryashko"

While any development is ruled by requirements and product specifications, there is a lot of duplicated code from project to project on a constant basis**.** You would not be writing your own database but use an off the shelf solution for data storage, would you**?** Then why would you want to write the same CRUD code over and over again when you can consume the persistence function as a service**?** The biggest value BaaS provides to developers is freeing them up from the dependency on server-side development (not mentioning hosting and administering servers issue)**.** Anyone can create a \*scalable\* client/server app simply by coding the client side and without any server-side coding**.** With the Backendless platform approach, the client-side can use just any framework**.**

[4](#theCommentsSection)
