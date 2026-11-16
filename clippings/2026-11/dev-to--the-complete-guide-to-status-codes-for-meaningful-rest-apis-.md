---
url: "https://dev.to/khaosdoctor/the-complete-guide-to-status-codes-for-meaningful-rest-apis-1-5c5"
captured_at: "2026-11-16T00:30:20+00:00"
title: "The Complete Guide to Status Codes for Meaningful ReST APIs - Let's start!"
domain: "dev-to"
---

_Photo by Joanna Kosinska on Unsplash_

For more than 10 years we've been working with HTTP and APIs following the [ReST](http://bit.ly/2IXukYW) architecture. Most people think that APIs are just interfaces you can use to interact with some third-party program and that [ReST](http://bit.ly/2IXukYW) is all about HTTP verbs, however, most of the communication we use nowadays may be wrong just because we are using wrong HTTP **status codes** to express our responses. And this can be a life changer when we're talking of modern web applications.

That's right! An API is much more expressive than just writing _GET_ to fetch data or _POST_ to create data, this is the request part, what about the response?

In this article, we'll explore a bit more about **HTTP Status Codes**, when to use each one of them and their definitions! So, let's dive in!

## [](#summary)Summary

*   [Summary](#summary)
*   [What are HTTP Status Codes?](#what-are-http-status-codes)
*   [Code Classes](#code-classes)
*   [Why do I need to know them?](#why-do-i-need-to-know-them)
*   [Picking the right code for your API](#picking-the-right-code-for-your-api)
    *   [Most Used API Codes](#most-used-api-codes)
    *   [200x](#200x)
        *   [200 - OK](#200-ok)
        *   [201 - Created](#201-created)
    *   [300x](#300x)
        *   [301 - Moved Permanently](#301-moved-permanently)
        *   [302 - Found](#302-found)
    *   [400x](#400x)
        *   [400 - Bad Request](#400-bad-request)
        *   [401 - Unauthorized](#401-unauthorized)
        *   [403 - Forbidden](#403-forbidden)
        *   [404 - Not Found](#404-not-found)
        *   [405 - Method not allowed](#405-method-not-allowed)
        *   [429 - Too many requests](#429-too-many-requests)
    *   [500x](#500x)
        *   [500 - Internal Server Error](#500-internal-server-error)
        *   [502 - Bad Gateway](#502-bad-gateway)
        *   [503 - Service Unavailable](#503-service-unavailable)
        *   [504 - Gateway Timeout](#504-gateway-timeout)
*   [Coffee Break](#coffee-break)

## [](#what-are-http-status-codes)What are HTTP Status Codes?

Every protocol we use today has been defined and specified in a document we call **R**equest **F**or **C**omments, or simply, RFC, HTTP [Status Codes](http://bit.ly/38ZENhl) are defined along with the HTTP protocol itself within the [RFC2616](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html), the document that defines what is HTTP/1.1, more specifically, on section 10. They're also defined on the [RFC7231](https://tools.ietf.org/html/rfc7231#section-6) section 6 about HTTP/1.1 Semantics. They're a number code that varies from 100 to 500ish and aims to make the HTTP response more meaningful to the client.

Incredible, we've cited the whole history of the Internet just to get a definition, right? But what does it mean? Every time we click on a button and send a request to a [client-server-based](http://bit.ly/2U29ePH) application, this application answers us with another HTTP-based response, both the request and the response contains a header, which is responsible for giving us the context of that requisition. [Status codes](http://bit.ly/38ZENhl) come on every response in a header called `Status` (how original), and they are there just to give us a clue of what happened to our request after it's been processed.

Most of the time, common users won't see those [status codes](http://bit.ly/38ZENhl) – unless something went terribly wrong – but, for us, programmers, they're extremely valuable. For instance, every time we cannot find a resource or a webpage we're presented with a **404** error page, this **404** is the HTTP status code for **Not Found**.

[![](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fkinsta.com%2Fwp-content%2Fuploads%2F2016%2F08%2Fgoogle-404-1-1.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fkinsta.com%2Fwp-content%2Fuploads%2F2016%2F08%2Fgoogle-404-1-1.png)

In short, they give us more information about what's happening and what has happened to the request we made, and they're pretty valuable to front-enders who want to show the correct status messages based on what the server has answered.

## [](#code-classes)Code Classes

As we mentioned earlier, HTTP [Status Codes](http://bit.ly/38ZENhl) are numbered from 100 to 500, however, this interval is not entirely filled, for example, we do not have a 174 status code because this was made to split codes into categories. These categories are defined in hundreds, each hundred of the HTTP interval represents a different category or class:

*   **100s**: These are informational codes, just to acknowledge that the request has been received and it's being processed.
*   **200s**: Success codes, returned when everything has been processed or understood properly, generally, this means that the client does not need to perform any more actions
*   **300s**: Redirection codes, meaning that the client should request that resource somewhere else
*   **400s**: Client error codes, when the client messed things up
*   **500s**: Server error codes, when the server messed things up

## [](#why-do-i-need-to-know-them)Why do I need to know them?

[Status codes](http://bit.ly/38ZENhl) are not only important to programmers because we need to know what's happening so we can perform validations or error messaging, but also they're important to monitor the health of our application, as well as SEO.

In monitoring, is easier to know the health of an application by its status code, for example, if your website is returning a lot of 404s, probably someone messed up and forgot to put some page online, however, if your application is displaying a lot of 500s, it **is** probably offline and no one can use it. So it is a lot easier for the dev team to debug an application when it displays the correct information.

On the other hand, out of the dev environment, when we talk about SEO, [status codes](http://bit.ly/38ZENhl) are the only way the crawling bots can understand what is happening when they "see" your website. This means that, if you're a blind robot that only understands [status codes](http://bit.ly/38ZENhl) then if a page keeps returning 404, this means that this page is not very good since it does not exist, so its rank should be lower than other pages that return a 200 status code because they **DO** exist.

I won't explain this in much detail here because our focus is on the [status codes](http://bit.ly/38ZENhl) and their returns, but you can read more about it [in this excellent article I used for reference](https://kinsta.com/blog/http-status-codes/#why-http-status-codes-and-errors-matter-for-search-engine-optimization-seo).

## [](#picking-the-right-code-for-your-api)Picking the right code for your API

In this section, we'll go through **all** the defined [status codes](http://bit.ly/38ZENhl) and their meanings, but we'll do it differently. Let's split this section into three:

1.  Most used API codes, where we'll talk about the codes we already use and how should we use them properly
2.  Codes not-so-often used, but we should use it more
3.  Other codes, where we'll finish the guide explaining less used status codes, which doesn't mean they're useless – except for one

In **this** article, we'll cover just the first part so it is not a very loooong reading for all of you! But, in the next articles of the series, we'll be covering the other two parts!

And we'll illustrate everything with [cats](https://http.cat/) and [dogs](https://httpstatusdogs.com/) so we can have a little fun while doing it!

## [](#most-used-api-codes)Most Used API Codes

First of all, let's dive in the most common stuff, there won't be much new content here, after all, they're already mostly used. So let's go through the most common of the [status codes](http://bit.ly/38ZENhl) by classes:

### [](#200x)200x

#### [](#200-ok)200 - OK

[![](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fhttp.cat%2F200)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fhttp.cat%2F200)

I believe this is the most common status code ever returned

The **200 OK** is the standard response for successful requests. Generally, this is what we are eager to see. However, the response for this code should differ from an HTTP Method to another as described [in the RFC7231](https://tools.ietf.org/html/rfc7231#section-6.3.1).

**When to use it**: Generally there's another HTTP Status Code that would express what you want to say in a better way, but, if you have doubts about what HTTP code to use and your response is a success, then 200 it is!

#### [](#201-created)201 - Created

[![](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fhttpstatusdogs.com%2Fimg%2F201.jpg)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fhttpstatusdogs.com%2Fimg%2F201.jpg)

This status code is usually used along with the `POST` method since it describes a resource that has been created into the server after the successful fulfillment of the request.

*   [Take a look at the definition](https://tools.ietf.org/html/rfc7231#section-6.3.2)

**When to use it:** When creating stuff. For example, when you create a new user in the database, the response should be 201 with the newly created document as the body.

### [](#300x)300x

#### [](#301-moved-permanently)301 - Moved Permanently

[![](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fhttpstatusdogs.com%2Fimg%2F301.jpg)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fhttpstatusdogs.com%2Fimg%2F301.jpg)

Used when the resource you're looking for has been permanently moved to another location. [This status code](https://tools.ietf.org/html/rfc7231#section-6.4.2) usually comes along with another header telling the exact location where the resource has been moved.

**When to use it:** Normally used for permanent redirections, for instance, a website that has an index page on `http://contoso.com` and should be redirected to `http://foo.com`. But the catch is, **this status code should only be used with GET or HEAD request methods**, for all other methods we should use [308](#308-permanent-redirect)

#### [](#302-found)302 - Found

[![](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fhttpstatusdogs.com%2Fimg%2F302.jpg)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fhttpstatusdogs.com%2Fimg%2F302.jpg)

Despite the text "found" don't give us much clue of what this is all about, the [302 status code](https://tools.ietf.org/html/rfc7231#section-6.4.3) is commonly used by temporary redirects, telling that the resource has been moved but it has been found on another URI described in the `Location` header.

**When to use it:** Mostly the same thing as [301](#301-moved-permanently), but used on temporary redirections where the resource will eventually be found in the current URL again. However, the rule applies, **this status code should only be used with GET or HEAD request methods**, for all other methods we should use [307](#307-temporary-redirect)

### [](#400x)400x

#### [](#400-bad-request)400 - Bad Request

[![](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fhttp.cat%2F400)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fhttp.cat%2F400)

[This status code](https://tools.ietf.org/html/rfc7231#section-6.5.1) is the official representation of the phrase "don't know, don't care". Since it only says that the server has found an error in the client's request and was unable to process it. The biggest mistake of most web developers is to return this error for **EVERY** request that they cannot handle. Which reduces the amount of information given to the client and, therefore, the meaningfulness of the API.

**When to use it:** When you have tried _everything_ and still could not find what was wrong with the request. Otherwise, please use a more meaningful error code.

#### [](#401-unauthorized)401 - Unauthorized

[![](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fhttp.cat%2F401)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fhttp.cat%2F401)

[The 401 status code](https://tools.ietf.org/html/rfc7235#section-3.1) is normally mistaken with [403](#403-forbidden), the biggest difference is that, in the case of 401, the client is still not authenticated, therefore it cannot access the page

**When to use it:** When a resource cannot be accessed due to **authentication reasons**, normally used in login pages when the user tries to log in with a wrong user/password

#### [](#403-forbidden)403 - Forbidden

[![](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fhttp.cat%2F403)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fhttp.cat%2F403)

Differently from [401](#401-unauthorized), the [403 status code](https://tools.ietf.org/html/rfc7231#section-6.5.3) refers to a resource that is off the limits for the request for any other reason **other than authorization**, for example, scope limiting.

**When to use it:** Generally used when we have a boundary to what users can do in the application, for instance, if I'm not the admin I should not be allowed to delete other users, therefore, if I try to do so, I'll get a _403 - Forbidden_ error. The rule of thumb is to remember the following sequence:

*   If I **don't** know who is making the request, then it's _401 - Unauthorized_
*   If I **do** know who's making the request, but the user doesn't have permissions to do so, then it's _403 - Forbidden_

#### [](#404-not-found)404 - Not Found

[![](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fhttp.cat%2F404)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fhttp.cat%2F404)

[The 404 status code](https://tools.ietf.org/html/rfc7231#section-6.5.4) is the most familiar to everyone, even those who are not devs. It is pretty straight forward, the resource you were looking for could not be found on this site.

**When to use it:** When you cannot find a page or resource, a not-so-known use case is to return 404 when a _find_ query – like `/users/1234` – returns null. This is a good practice because the user was looking for a specific resource and it does not exist. On the other hand, if you're on a _search_ query – like `/users` – where you could return 0 or more then the default response for "There are no users registered" or "Empty list" would be 200.

#### [](#405-method-not-allowed)405 - Method not allowed

[![](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fhttpstatusdogs.com%2Fimg%2F405.jpg)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fhttpstatusdogs.com%2Fimg%2F405.jpg)

Generally, when we don't implement a route but it is there, we use the [405 status code](https://tools.ietf.org/html/rfc7231#section-6.5.5). This code says that the method we're using is a known method to the server – which means it can process it – however **that** particular resource does not accept it.

**When to use it:** Let's explain by example. If you have a `POST /users` and a `GET /users` but do not have a `DELETE /users`, then if I try to `DELETE /users` you should return a _405_ status code to me, this status code generally comes along with another header called `Allow` stating which methods are allowed.

#### [](#429-too-many-requests)429 - Too many requests

[![](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fhttp.cat%2F429)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fhttp.cat%2F429)

The classic "Are you trying to DDoS me?". [The 429 status code](https://tools.ietf.org/html/rfc6585#section-4) is defined on another RFC, the RFC-6585 for additional HTTP headers. It states that the requester has sent too many requests in a given amount of time, this is what we call _rate limiting_.

**When to use it:** This should be the default to all APIs out there that don't want to be crashed by DDoS attacks, but, since this is not the case today, the most common use case to this status code is to limit the number of requests that a user can make before it is blocked by the server. Most API gateways and user-exposed APIs use it, like Twitter, for instance, which allows about 15 requests per minute.

> Also, if you're looking to do it yourself, Azure has [a pretty cool tool](http://bit.ly/33qzI0d) that makes it possible

### [](#500x)500x

#### [](#500-internal-server-error)500 - Internal Server Error

[![](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fhttp.cat%2F500)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fhttp.cat%2F500)

The classic "I messed things up". [This status code](https://tools.ietf.org/html/rfc7231#section-6.6.1) is sent as the response when the server did something wrong on its side and do not know how to proceed. If a user is seeing this, then your application is in bad shape, since these status codes should be visible only to the internal side of the application. The user side should format the error and show a more user-friendly message.

**When to use it:** When an exception is thrown by the server and not caught and you do not know what happened, but you do know it is on the server. I've seen a lot of people using 400 status codes to show server-side errors, this is wrong on so many levels...

#### [](#502-bad-gateway)502 - Bad Gateway

[![](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fhttpstatusdogs.com%2Fimg%2F502.jpg)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fhttpstatusdogs.com%2Fimg%2F502.jpg)

[This status code](https://tools.ietf.org/html/rfc7231#section-6.6.3) is meant for proxied servers. It states that the server which is acting as a gateway or a proxy could not complete the request, or it received an invalid one from the client.

**When to use it:** The programmer should never need to use it manually unless you're writing a proxy API or a proxy server, in this case, you need to return this message instead of the [500](#500-internal-server-error) error we mentioned earlier.

#### [](#503-service-unavailable)503 - Service Unavailable

[![](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fhttpstatusdogs.com%2Fimg%2F503.jpg)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fhttpstatusdogs.com%2Fimg%2F503.jpg)

[The 503 code](https://tools.ietf.org/html/rfc7231#section-6.6.4) is more of an information code than an error one since it states that the server handling the requests is not available due to an overload or scheduled maintenance. In the case of the latter, the server can optionally send a `Retry-After` header with an amount of time so the user can try again.

**When to use it:** As I mentioned on the other 500x errors, this code is usually not set by programmers since it is on server-side code, unless you're the developer of a server, in this case, the use case is pretty obvious.

#### [](#504-gateway-timeout)504 - Gateway Timeout

[![](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fhttp.cat%2F504)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fhttp.cat%2F504)

[This code](https://tools.ietf.org/html/rfc7231#section-6.6.5) is a variation from the [502](#502-bad-gateway) code, the difference is that instead of not receiving a good request, the upstream server did not send the request within the expected time frame.

**When to use it:** This code should be only returned if you're coding a gateway and the proxied server did not answer your request.

## [](#coffee-break)Coffee Break!

Stop for now! Grab a coffee as you prepare for the next part of this series, where we'll talk about the APIs we don't see very often, but we should.

See ya!
