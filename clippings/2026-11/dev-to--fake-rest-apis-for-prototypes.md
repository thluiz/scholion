---
url: "https://dev.to/aumayeung/fake-rest-apis-that-we-can-use-to-build-prototypes-54dm"
captured_at: "2026-11-16T01:14:03+00:00"
title: "Fake REST APIs That We Can Use to Build Prototypes"
domain: "dev-to"
---

**Subscribe to my email list now at [http://jauyeung.net/subscribe/](http://jauyeung.net/subscribe/)**

**Follow me on Twitter at [https://twitter.com/AuMayeung](https://twitter.com/AuMayeung)**

**Many more articles at [https://medium.com/@hohanga](https://medium.com/@hohanga)**

**Even more articles at [http://thewebdev.info/](http://thewebdev.info/)**

When we want to build prototypes, we want to build them fast. Therefore, we should find a fake REST API so that we don’t need to write our own for a quick prototype.

In this article, we’ll look at some fake REST APIs that we can use to mock out our back end for prototypes.

## [](#jsonplaceholder)JSONPlaceholder

[JSONPlaceholder](https://jsonplaceholder.typicode.com/) is a useful REST API that lets us do CRUD operators on their server by sending requests to their REST API.

It supports CORS so that we can use them with our front end apps.

The endpoints follow the REST API convention so it’s also great examples for us to follow.

There’re a few endpoints like `comments`, `photos`, `albums`, `todos`, and `posts` that we can query and send.

## [](#reqres)Reqres

[Reqres](https://reqres.in/) is a useful REST API to let us mock out our API for our front end.

It explicitly says that it supports Ajax requests so we can go ahead and use it with our front end directly.

There’re lots of routes that are available. They include GET, POST, PATCH, and DELETE routes.

Most of the routes are user-related routes, so we can fake an authentication system without building one ourselves.

## [](#typicodejsonserver)[typicode](https://github.com/typicode)/[json-server](https://github.com/typicode/json-server)

The JSON server program is a Node package that we can run on our local computer.

We can define our routes by providing them with fake JSON data.

Therefore, we can create any route we like, unlike the previous examples.

It’s very configurable and can be adapted to be used in any situation. It supports things like charging ports, HTTPS, custom routes, middleware, and more.

We can also serve static files with it. So it’s more comprehensive than the websites we have above.

## [](#fake-it-till-you-make-it)Fake it till you make it

[Fake it till you make it](https://fakejson.com/) is another mock back end API that we can use to speed up our development.

It comes with both free and paid tiers, The paid tier have 1000 fake units a day with arrays up to 10 elements in size.

We can get one API token to use the free version.

The nesting depth is up to 1 level deep for the free version. The paid version lets us nest our JSON deeper.

Requests parameters are accepted in the paid version. And paid versions can have custom fields.

Support is also available for the paid versions via email.

## [](#beeceptor)Beeceptor

[Beeceptor](https://beeceptor.com/) is another web app that lets us mock out a REST API. we can enter a name for our endpoint which is hosted in their subdomain.

It supports all kinds of requests like GET, POST, PUT, PATCH, and DELETE.

We can also simulate API responses and failures.

Payloads can be inspected for debugging purposes. Also, we can capture HTTP requests in real tine.

Other things it can do include A/B testing and simulate latencies and timeouts. These are all important things since we want to handle error cases in addition to successful cases.

[![](https://res.cloudinary.com/practicaldev/image/fetch/s--GNJRdpaj--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://miro.medium.com/max/10944/0%255C%2ASqfvDBCZrO7CKTqO)](https://res.cloudinary.com/practicaldev/image/fetch/s--GNJRdpaj--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://miro.medium.com/max/10944/0%255C%2ASqfvDBCZrO7CKTqO)

Photo by [Quentin Kemmel](https://unsplash.com/@kouglov?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com/?utm_source=medium&utm_medium=referral)

## [](#fake-rest)Fake Rest

[Fake Rest API](https://fake.rest/) is another fake API site. We can use them to mock out endpoints with data included.

Things like address, array, e-commerce data, and much more can all be retrieved right from this app.

We can also add our own data and use them whenever we like. We can specify any description for our endpoints including method name, verb, redirect, `Content-Type` , response code, and more.

## [](#ngducapinow)[ngduc](https://github.com/ngduc)/[api-now](https://github.com/ngduc/api-now)

`api-now` is a Node package that we can run locally on our computer to create a fake API instantly.

It comes with default datasets. Also, it can take `.json` or `.js` file for data.

It has some routes like file upload, login, todos, images and more. The login route provides us with a JSON web token for authentication.

Also, it can serve files in a static directory. We just have to run `npx api-now` to run this package.

## [](#mocky)Mocky

[Mocky](https://www.mocky.io/) is a simple app where we can enter the response we want to generate ourselves and get an endpoint for it on the fly.

We can use it to simulate responses with different status codes, body, and headers.

## [](#conclusion)Conclusion

There’re many fake API apps that we can use to mock out our API for prototypes.

Some include data and some are more configurable. So we can take our pick and choose one that’s right for us.
