---
url: "http://www.infoq.com/news/2013/10/gotober-do-dont-webapi"
captured_at: "2013-11-03T15:15:53-03:00"
title: "GOTO Berlin: DO’s and DON’Ts in a Web API"
domain: "infoq-com"
---

# **G**OTO Berlin: DO’s and DON’Ts in a Web API

by
[Jan Stenberg](http://www.infoq.com/author/Jan-Stenberg) 
on
Oct 19, 2013
*|*
[Discuss](#theCommentsSection)

There are a lot of discussions in matters around [REST](http://en.wikipedia.org/wiki/REST)  and [web APIs](http://en.wikipedia.org/wiki/Web_api)  in mailing lists and discussion forums and this is my opinionated thoughts in some of these matters, there is no absolute truth here, [Oliver Wolf](http://gotocon.com/berlin-2013/speaker/Oliver+Wolf) , principal consultant at InnoQ, started his [talk](http://gotocon.com/berlin-2013/presentation/Web API DOs and DON'Ts)  at the [GOTO Berlin Conference](http://gotocon.com/berlin-2013/speaker/Oliver+Wolf)  called ”Web API DOs and DON'Ts"**.**

**Don’t think in terms of endpoints****.** [SOAP](http://en.wikipedia.org/wiki/SOAP)  has a facade with a single entry point**.** In contrast the web has lots of entry points that are built on relations and interconnections with hypermedia as a critical element**.** Instead of letting your API be a black hole with only one way in you should use hypermedia controls to link your resource representations in ways that are meaningful for your audience**.**

**Don’t expose your domain model in the API****.** A problem with many models is that they contain only data, lacking all form of behaviour, so called [anaemic models](http://www.martinfowler.com/bliki/AnemicDomainModel.html) **.** If you expose such a model you will end up with [CRUD](http://en.wikipedia.org/wiki/CRUD) , (Create, Read, Update, Delete), resources**.** This doesn’t necessarily have to be a bad thing, sometimes all you need is a pure CRUD API**.** Otherwise a problem exposing a CRUD model is that a client using such an API needs a lot of knowledge; what actions it can perform on which resources, in what order to do things and so on**.** A lot of logic is encoded in the client, giving a tight coupling between client and server**.**

**Design your API after intent****.** Think about what your client wants to do and how they will do it**.** Sometimes this requires a trade-off between clarity and flexibility, how clear and simple your API should be versus what flexibility is needed**.** A flexible but also more imperative way of getting the most profitable customers might be:

```
GET /customers?sortBy=grossmargin&order=descending
```

In contrast, a more declarative style, exposing intent, but also less flexible, might be:

```
GET /most_profitable_customers
```

Oliver’s take-away point here is to think about what a client needs to use your API for, what the intent should be and try to tailor it for that need**.**

**Don’t overuse GET and POST****.** Basically this means you shouldn’t use them in the wrong way and violate the HTTP specification**.** You should for example not use GET or POST to delete a resource**.** The HHTP verbs are defined for a reason, they have complimentary qualities and you gain a lot by embracing the specification**.** Using the verbs communicates intent, what the client wants to do and what behaviour the client can expect from the server**.**

**Don’t limit your choice of error codes to 200 and 500****.** Use the whole spectrum of error codes, there are 160 error codes to choose from so there is one for almost every conceivable type of error**.** Using the right error code is a key in proper error handling on the client**.**  
A common problem is servers returning 200, OK, although an error has occurred**.** Pretending that everything is fine when in fact it’s not is seldom a good idea**.**

**Don’t ignore caching**. There will be caches involved no matter what, and they are an important part of the web**.** Help the caches by adding proper cache headers, e.g. if you don’t want caching, be explicit and turn them off**.**  
One of the better ways of controling caching is to use validators, preferably Etags**.** They allow the server side to act on arbitrary data, an Etag is just a value the server generates and passes to the cache, the cache later on passes the Etag back, asking the server if the resource if fresh or not**.**

**Don’t require versioning****.** What is thought of as a change in a resource is often in fact just a change in the representation; it’s still the same resource and should have the same URL, therefore avoid versioning the URL**.** Instead there should be a new version of the media type, e.g. by adding v2

```
Content-Type=application/vnd.company.v2+xml
```

**Don’t use extensions for content negotiation****.** The proper way to negotiate about a representation format is using Accept and Content-Type in the header**.**

The [GOTO Berlin Conference 2013](http://gotocon.com/berlin-2013/)  is the first GOTO conference in Berlin, with about 420 attendees and 80 speakers**.**

### Tell us what you think
