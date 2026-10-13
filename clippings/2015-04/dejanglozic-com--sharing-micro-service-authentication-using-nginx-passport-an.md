---
url: "http://dejanglozic.com/2014/10/07/sharing-micro-service-authentication-using-nginx-passport-and-redis/"
captured_at: "2015-04-10T22:15:26-03:00"
title: "Sharing micro-service authentication using Nginx, Passport and Redis"
domain: "dejanglozic-com"
---

# Sharing micro-service authentication using Nginx, Passport and Redis

[![abgeschlossen_1.jpg](dejanglozic-com--sharing-micro-service-authentication-using-nginx-passport-an/678cb241856e699a1e297b0aab355a02.jpg)](https://dglozic.files.wordpress.com/2014/10/abgeschlossen_1.jpg)

Wikimedia Commons, Abgeschlossen 1, by Montillona

And we are back with the regularly scheduled programming, and I didn’t talk about micro-services in a while. Here is what is occupying my days now – securing a micro-service system. Breaking down a monolith into a collection of micro-services has some wonderful properties, but also some nasty side-effects. One of them is authentication.

The key problem of a micro-service system is ensuring that its federated nature is transparent to the users. This is easier to accomplish in the areas that are naturally federated (e.g. a collection of API end points). Alas, there are two areas where it is very hard to hide the modular nature of the system: composing Web pages from contributions coming from multiple services, and security. I will cover composition in one of the next posts, which leaves us with the topic of the day.

In a nutshell, we want a secure system but not at the expense of user experience. Think about European Union before 1990. In some parts of Europe, you could sit in a car, drive in any direction and cross five countries before the sunset. In those days, waiting in line at the custom checkpoint would get old fast and could even turn into quite an ordeal in extreme cases.

Contrast it to today – once you enter EU, you just keep driving, passing countries as if they are Canadian provinces. Much better user experience.

We want this experience for our micro-service system – we want to hop between micro-services, be secure yet not being actively aware that the system is not a monolith.

**It starts with a proxy**

A first step in securing a micro-service system starts at a proxy such as Nginx. Placing a multi-purpose proxy in front of our services have several benefits:

1. It allows us to practice friendly URL architecture – we can proxy nice front end URLs such as <http://foobar.io/users> or <http://foobar.io/projects> to separate micro-services (‘users’ and ‘projects’, respectively). It also goes around the fact that each Node.js service runs on a separate port (something that JEE veterans tend to hate in Node.js, since several apps running in the same JEE container can share ports).
2. It allows us to enable load balancing – we can proxy the same front end location to a collection of service instances running in different VMs or virtual containers (unless you are using a PaaS, at which point you just need to increment the instance counter).
3. It represents a single domain to the browser – this is beneficial when it comes to sharing cookies, as well as making Ajax calls without tripping the browser’s ‘same origin’ policy (I know, CORS, but this is much easier)

If we wanted to be really cheap, we could tack on another role for the front end proxy – authentication. Since all the requests are passing through it, we can configure a module to handle authentication as well and make all the micro-services behind it handle only authenticated requests. Basic auth module is [readily available for Nginx](http://nginx.org/en/docs/http/ngx_http_auth_basic_module.html), but anything more sophisticated is normally not done this way.

**Use Passport**

Most people will need something better than basic auth, and since we are using Node.js for our micro-service system, [Passport](http://passportjs.org/) is a natural choice. It has support for several different authentication strategies, including OAuth 1.0 and OAuth 2.0, and several well known providers (Twitter, Facebook, LinkedIn). You can easily start with a stock strategy and extend it to handle your unique needs (this will most likely be needed for OAuth 2.0 which is not a single protocol but an authentication framework, much to the [dismay of Eran Hammer](http://hueniverse.com/2012/07/26/oauth-2-0-and-the-road-to-hell/)).

Passport is a module that you insert in your Node.js app as middleware, and hook up to the Express session. You need to expose two endpoints: ‘/auth/<provider>’ and ‘/auth/<provider>/callback’. The former is where you redirect the flow in order to start user login, while the latter is where the Auth server will call back after authenticating the user, bringing in some kind of authorization code. You can use the code to go to the token endpoint and obtain some kind of access token (e.g. bearer token in case of OAuth 2.0). With the access token, you can make authenticated calls to downstream services, or call into the profile service and fetch the user info. Once this data is obtained, Passport will tack it on the request object and also serialize it in the session for subsequent use (so that you don’t need to authenticate for each request).

Passport module has a very nice web site with plenty of examples, so we don’t need to rehash them here. Instead, I want us to focus on our unique situation of securing a number of micro-services working together. What that means is:

1. Each micro-service needs to be independently configured with Passport. In case of OAuth (1.0 or 2.0), they can share client ID and secret.
2. Each micro-service can have a different callback URL as long as they all have the same domain. This is where we reap the benefit of the proxy – all the callback URLs do have the same domain thanks to it. In order to make this work, you should register your client’s callback\_uri with the authentication provider as the shared root for each services’ callback. An actual callback passed to the authentication endpoint for each micro-service can be longer than the registered callback\_uri as long as they all share common root.
3. Each micro-service should use the same shared authentication strategy and user serialization/deserialization.

Using this approach, we can authenticate paths served by different micro-services, but we still don’t have Single Sign-On. This is because Express session is configured using an in-memory session store by default, which means that each micro-service has its own session.

**Shared session cookie**

This is not entirely true: since we are using the default session key (or can provide it explicitly when configuring session), and we are using single domain thanks to the proxy, all Node.js micro-services are sharing the same **session cookie**. Look in the Firebug and you will notice a cookie called ‘connect.sid’ once you authenticate. So this is good – we are getting there. As I said, the problem is that while the session cookie is shared, this cookie is used to store and retrieve session data that is in memory, and this is private to each micro-service instance.

This is not good: even different instances of the same micro-service will not share session data, let alone different micro-services. We will be stuck in a pre-1990 Europe, metaphorically speaking – asked to authenticate over and over as we hop around the site.

**Shared session store**

In order to fix this problem, we need to configure Express session to use an external session store as a service. Redis is wonderfully easy to set up for this and works well as long as you don’t need to persist your session forever (if you restart Redis, you will lose session data and will need to authenticate again).

|  |  |
| --- | --- |
|  | `var ropts = {`  `host: "localhost",`  `port: 5556,`  `pass: "secret"`  `}`  `...`  `app.use(express.session({ key: 'foobar.sid',`  `store: new RedisStore(ropts),`  `secret: 'secret'}));`  `app.use(passport.initialize());`  `app.use(passport.session());` |

I am assuming here that you are running Redis somewhere (which could range from trivial if you are using a PaaS, to somewhat less trivial if you need to install and configure it yourself).

What we now have is a system joined at both ends – Nginx proxy ensures session cookie is shared between all the micro-service instances it proxies, and Redis store ensures actual session data is shared as well. The corollary of this change is that no matter which service initiated the authentication handshake, the access token and the user profile are stored in the shared session and subsequent micro-services can readily access it.

[![micro-authentication.png](dejanglozic-com--sharing-micro-service-authentication-using-nginx-passport-an/d1fda78a17bc57f0e418f75e4776964a.png)](https://dglozic.files.wordpress.com/2014/10/micro-authentication.png)

**Single Sign Off**

Since we have Redis already configured, we can also use it for pub/sub to propagate the ‘logout’ event. In case there is state kept in Passport instances in micro-services, a system-wide logout for the session ensures that we don’t have a “partially logged on” system after a log out in one service.

I mentioned Redis just for simplicity – if you are writing a micro-service system, you most likely have some kind of a message broker, and you may want to use it instead of Redis pub/sub for propagating logout events for consistency.

**Calling downstream services**

Not all micro-services will need full Passport configuration. You can configure services that require access token – they can just look for ‘Authorization’ header and refuse to do anything if it is not present. For example, for OAuth 2.0 authentication, the app will need something like:

|  |  |
| --- | --- |
|  | `Authorization: Bearer 0b79bab50daca910b000d4f1a2b675d604257e42` |

The app can go back to the authentication server and verify that the token is still valid, or go straight to the profile endpoint and obtain user profile using the token (this doubles as token validation because the profile service will protest if the token is not valid). API services are good candidates for this approach, at least as one of the authentication mechanisms (they normally need another way for app-to-app authentication that does not involve an actual user interacting with the site).

**What about Java or Go?**

This solution obviously works great if all the micro-services are written in Node.js. In a real-world system, some services may be written using other popular stacks. For example, what will happen if we write a Java service and try to participate?

Obviously, running a proxy to the Java micro-service will ensure it too has access to the same session cookie. Using open source Redis clients like [Jedis](https://github.com/xetorthio/jedis) will allow it to connect to the same session store. However, the picture is marred slightly by the fact that Express session signs the cookie with a combination of HMAC-Sha256 and ‘base64′ digest, plus some [additional tweaking](https://github.com/visionmedia/node-cookie-signature/blob/master/index.js). This is obviously a very Express-centric approach and while it can be re-created on the Java side, there is this lingering feeling we created a Node-centric system and not a stack-agnostic one.

Java has its own session management system and you can see the JSESSIONID cookie sitting next to the one created by Express. I will need to study this more to see if I can make Java and Node share the session cookie creation and signing in a more stack-neutral way. In a system that is mostly Node.js with a Java service here and there, signing and unsigning the session cookie the way Express likes it may not be a big deal.

In addition, my current experimentation with Java points at creation of a JEE filter (middleware) that checks for the session cookie and redirects to authentication endpoints if a user is not found in the session. True Java authentication solutions are not used, which may or may not be a problem for you if you are a JEE veteran. JEE filters provide for wrapping HTTP requests so methods such as ‘getRemoteUser()’ can be implemented to provide the expected results to Java servlets.

I mentioned Go because it is an up and coming language that people seem to use for writing micro-services more and more these days. I have no idea how to write the session support for Go in this context so I am tossing this in just as food for thought. If you know more, drop me a line.

**Closing thoughts**

There are many alternative ways to solve this problem, and I profess my mixed feelings about authentication. For me, it is like broccoli – I understand that it is important and good for me, but I cannot wait to get to the ice cream, or whatever is the ice cream equivalent in writing micro-service systems. Spending time with Passport and OAuth 2.0, I had to learn more than I ever wanted to know about authentication, but I am fairly pleased with how the system works now. What I like the most is its relative simplicity (to the extend that authentication can be). My hope is that by avoiding [smart solutions](http://dejanglozic.com/2013/10/01/dumb-code-good-smart-code-bad/ "Dumb Code Good, Smart Code Bad"), the chances of the system actually working well and not presenting us with difficult edge cases every day are pretty good. I will report back if I was too naive.

© Dejan Glozic, 2014

[About these ads](http://wordpress.com/about-these-ads/)
