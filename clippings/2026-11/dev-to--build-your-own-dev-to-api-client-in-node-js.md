---
url: "https://dev.to/bearer/build-your-own-dev-to-api-client-in-node-js-5e5p"
captured_at: "2026-11-16T01:45:10+00:00"
title: "Build your own Dev.to API client in Node.js"
domain: "dev-to"
---

_📣 This post originally appeared as [Build your own API client in Node.js](https://blog.bearer.sh/api-client-library-node-js/) on [The Bearer Blog](https://blog.bearer.sh/)._

**Note: The [dev.to API](https://docs.dev.to/api/) recently saw a big update, so it's a great time to experiment with it.**

When you interact with a REST API, are you making calls directly or are you using a client from the API provider? Many APIs now provide clients, wrappers, or SDKs. These terms all mean the same thing in this context. What happens if the API you are using doesn't offer a client? Do you even need one? Is there any benefit? In this article, we will explore some of the reasons you may want to build one. We will also build an example API client that can be used as a foundation for a more full-featured API.

## [](#use-cases)Use cases

API clients, sometimes called API SDKs or API wrappers, are an interface for interacting indirectly with the API. Some features common to API clients include:

*   Centralize authentication and setup
*   Speed up development
*   Handle error logic and provide custom errors
*   Enforce language-specific conventions

The key goal with most API clients is to make development easier. This lets new users of an API get up and running faster. If you are the provider of an API, it may be useful to consider a client. If you are the consumer of an API, creating a wrapper can help abstract away reused functionality. There are even some tools that automate this process. If your API uses the OpenAPI standard, tools like [Swagger's Codegen](https://swagger.io/tools/swagger-codegen/) can generate SDKs for a variety of languages.

With that in mind, let's look at creating our own API client from scratch for Node.js and the Browser.

## [](#plan-and-setup)Plan and setup

For this example, we want to focus on a few core features.

1.  Centralized setup and authentication
2.  Simplified REST interactions

We also want to choose a request library that will suit our needs. Since [Fetch](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API) is standard in the browser, we'll use it. We will include a library like [`isomorphic-unfetch`](https://www.npmjs.com/package/isomorphic-unfetch) to manage legacy support _and_ Node.js support. If you prefer, you can adapt any of the concepts mentioned in this article to your [library of choice](https://blog.bearer.sh/top-node-request-libraries/). You can even use the included `https` module in Node.js if you are only concerned with server usage.

_⚠️ Note: While the client we are building works in the browser and Node.js, it is important not to expose API keys in client-side javascript unless they are public. Make sure to confirm the preferred key usage with the API you are using before making client-side calls._

To get started, make sure you have Node.js and NPM installed. Then set up a new Node.js project with the following terminal commands:  

```
# Make a new directory
mkdir node-api-client-demo

# Change to the new directory
cd node-api-client-demo

# Initialize a new Node.js project
npm init -y
```

Enter fullscreen mode Exit fullscreen mode

Next, create a new file called `index.js`. We will be placing all of our code in a single file for ease of use, but you can break the code out into modules if you prefer.

## [](#define-the-client-interface)Define the client interface

For this example, we will be using part of the [Dev.to API](https://docs.dev.to/api/). It currently only offers key-based authentication, which keeps our example straightforward. To follow along, you'll need an account and an API key. You can follow the steps [on their documentation](https://docs.dev.to/api/#section/Authentication) to get both. Alternatively, you can use an API like [The Movie DB](https://www.themoviedb.org/documentation/api) or a similar API-Key-based platform.

Before we start building the wrapper, let's look at how the user might want to interact with it. This is a documentation-first approach.  

```
const api = new DevTo({
  api_key: "xxxxxxxxx"
})

api.getArticles(options).then(articles => {})
api.getArticleById(id).then(article => {})

api.createArticle(body).then(article => {})
```

Enter fullscreen mode Exit fullscreen mode

In the code above, we create an instance of the `DevTo` class and pass it the `api_key`. Then, we can see a variety of methods that will interact with the API. For brevity, we will focus on retrieving articles, getting a specific article, and creating a new article. If you pay close attention to the documentation URLs for the [Dev.to API](https://docs.dev.to/api/#operation/getArticles), you'll notice that we are using the same names as their internal getters and setters. This isn't required, but the naming schemes are fairly common.

Now we can start building out our class.

## [](#build-the-client-class)Build the client class

Open the `index.js` file from earlier, and create a class as follows:  

```

class DevTo {
  constructor(config) {
    this.api_key = config.api_key
    this.basePath = "https://dev.to/api"
  }
}
```

Enter fullscreen mode Exit fullscreen mode

The code above defines the `DevTo` class and sets up the constructor to accept a config object. It then sets the `api_key` from the config and sets the `basePath` property to the base url for the API endpoints. Now, install and require an [HTTP library](https://blog.bearer.sh/top-node-request-libraries/). We will use `isomorphic-unfetch` for this example, as it is promise-based.

Install `isomorphic-unfetch`:  

```
npm install isomorphic-unfetch
```

Enter fullscreen mode Exit fullscreen mode

Require the package at the top of the `index.js` file:  

```
// index.js
const fetch = require("isomorphic-unfetch")

class DevTo {
  /*...*/
}
```

Enter fullscreen mode Exit fullscreen mode

Next, we can scaffold out our methods. We'll need the three from our use-case example above, as well as a reusable `request` method that handles building and making the request.  

```

class Devto{
  constructor(config) {
    this.api_key = config.api_key
    this.basePath = "https://dev.to/api"
  }

  request(endpoint, options) { /*...*/ }

  getArticles(options) {
    // 1. Convert options to query string
    // 2. return this.request
  }
  getArticleById(id) {
    // 1. Build endpoint based on id
    // 2. return this.request
  }
  createArticle(body) {
    // 1. Build endpoint
    // 2. return this.request with body attached
  }
 }
```

Enter fullscreen mode Exit fullscreen mode

Our methods above include the steps each will need. We'll build them out individually, but first, we need to make `request` usable.  

```

request(endpoint = "", options = {}) {

  let url = this.basePath + endpoint

  let headers = {
    'api_key': this.api_key,
    'Content-type': 'application/json'
  }

  let config = {
    ...options,
    ...headers
  }


  return fetch(url, config).then(r => {
    if (r.ok) {
      return r.json()
    }
    throw new Error(r)
  })
}
```

Enter fullscreen mode Exit fullscreen mode

In the above code block, we've filled in the functionality for `request`. It takes an `endpoint` string and `config` object as arguments. We then build the `url` from the `endpoint` and `basePath`. The Dev.to API uses the `api_key` as a header for authentication, so we define it as a header along with `Content-Type` to preemptively handle the `POST` requests we will make later. Next, we merge the incoming `options` object with the `headers` into a new `config` using the [spread operator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax).

Finally, we are returning `fetch` and doing some light error checking and json transformation. _This is the important part_. Return, combined with the returns from our other methods, will allow users to interact with our client just as they would with any other promise. Either by chaining `then` or by using async/await.

Next, let's define the `getArticles` method. For this, we'll need a small helper utility to merge our options object into a query string. If you are in the browser, you can use [one of the libraries on NPM](https://www.npmjs.com/search?q=querystring) or write your own. If you're in Node, you can use the built-in `querystring` module.

First, require the module at the top after `isomorphic-unfetch`:  

```
const querystring = require("querystring")
```

Enter fullscreen mode Exit fullscreen mode

Then, fill in the `getArticles` method:  

```
getArticles(options) {
  let qs = options ? "?" + querystring.stringify(options) : ""

  let url = "/articles" + qs
  let config = {
    method: 'GET'
  }
  return this.request(url, config)
}
```

Enter fullscreen mode Exit fullscreen mode

Here we are building a query string from any options that the user passes in. The [`GET /articles` endpoint](https://docs.dev.to/api/#operation/getArticles) allows for quite a few query parameters. We let the user provide them as an object, but then process them into a query string that the API will understand. We then add it to the endpoint, and set up a basic config that defines the `method` as `GET`. `GET` is the default, so you could leave this off if you want.

Next, for a slightly different version of the above, we can fill in the `getArticleById` method.  

```
getArticleById(id) {
  let url = "/articles/" + id
  return this.request(url, {})
}
```

Enter fullscreen mode Exit fullscreen mode

Here we follow the same pattern of building the URL, then returning the `request` method with the appropriate arguments.

Finally, let's build our `createArticle` method.  

```
createArticle(body) {
  const options = {
    method: 'POST',
    body: JSON.stringify(body)
  }
  return this.request('/articles', options)
  // Optional: add your own .catch to process/deliver errors or fallbacks specific to this resource
}
```

Enter fullscreen mode Exit fullscreen mode

The end is the same as the previous methods. The only difference is that our configuration now sets the `method` to `POST` and stringifies the article object as the `body`. After all of the returns, you can optionally chain a `catch` to handle any error handling specific to the resources. Otherwise, your user will have to handle any errors.

## [](#bringing-it-all-together)Bringing it all together

With the client in place, we can return to our initial client implementation example:  

```
const api = new DevTo({
  api_key: "XXXXXXXXX"
})

api.getArticles({ username: "bearer", page: 1 }).then(data => console.log(data))
```

Enter fullscreen mode Exit fullscreen mode

This will return the first page of articles from the [Bearer account on Dev.to](https://dev.to/bearer). As a consumer of this client, we can take it a step further by using [Bearer](https://bearer.sh/) to monitor the API calls:  

```
const Bearer = require("@bearer/node-agent")

Bearer.init({
  secretKey: "YOUR-SECRET-KEY"
}).then(() => {
  const api = new DevTo({
    api_key: "XXXXXXXXX"
  })

  api
    .getArticles({ username: "bearer", page: 1 })
    .then(data => console.log(data))
})
```

Enter fullscreen mode Exit fullscreen mode

This is just the beginning. Your API client can handle all kinds of repeated use-cases. It can lock API version to client version, it can allow for more [complex authentication methods](https://blog.bearer.sh/the-three-most-common-api-authentication-methods/), and you can tailor the developer experience to the needs of your users. Here's the [full code from our example](https://gist.github.com/markmichon/a4abeae93009232bc5a6cbe463fdbbd7). Have you built a wrapper around an API you use often? Let us know at [@BearerSH](https://twitter.com/bearersh) and follow the [Bearer Blog](https://blog.bearer.sh/) for more posts on working with APIs.
