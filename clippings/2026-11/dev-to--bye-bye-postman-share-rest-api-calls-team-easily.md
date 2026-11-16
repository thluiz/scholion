---
url: "https://dev.to/monisnap/bye-bye-postman-let-s-share-your-rest-api-calls-in-team-easily-h6l"
captured_at: "2026-11-16T00:43:58+00:00"
title: "Bye bye Postman ! Let's share your REST API calls in team, easily !"
domain: "dev-to"
---

As developer, we are using tools to make REST API calls _(Postman, Insomnia, PostWoman...)_, and these tools are very usefull.

## [](#the-limits)The limits

Make calls to test an API is fine, but if you want to edit, version, or simply share it with your team ... it's not very handy.

Indeed, you can use Postman paid plans for instance, but it means that you need to pay, and it means that all your team needs to use Postman, again one more tool...

## [](#do-you-know-rest-client-)Do you know **REST Client** ?

[![Logo REST Client VS Code Extension](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fthepracticaldev.s3.amazonaws.com%2Fi%2F452qob0efqpz249wrvnm.png "Logo REST Client VS Code Extension")](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fthepracticaldev.s3.amazonaws.com%2Fi%2F452qob0efqpz249wrvnm.png)

[REST Client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client)\* is a **VS Code extension**.

It will let you to send HTTP requests and view responses **into VS Code**. And only based on a text file, which can easily be **versioned** among your repository. 🙏

## [](#pros)Pros

The main advantage is to be able to version and share your API calls.

If you're working on an internal API, you may want to share how to test a new endpoint with your colleagues.

REST Client is a good easy way to do it !

Another good point is simplicity. All you need to do/have, is **ONE file**. Also, if you jump between projects and do not remember how works an API/Service on which you did not work since a while, just look at this file !

## [](#cons)Cons

You have to use VS Code... but for a lot of known reasons among internets, you are using Emacs, VI, or VS Code 😄

### [](#whats-next-)What's next ?

Here is how to begin.

### [](#the-file)The file

Only create a file with .http extension, for instance doc.http

\# REST Client tests on https://github.com/tronalddump-io/tronald-app

@baseUrl = https://api.tronalddump.io

\### Get a random clever quote

GET {{baseUrl}}/random/quote

Accept: application/hal+json

And then, VS Code will show you the file as :

[![doc.http preview into VS Code](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fthepracticaldev.s3.amazonaws.com%2Fi%2F3ssx618zejysxau11b20.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fthepracticaldev.s3.amazonaws.com%2Fi%2F3ssx618zejysxau11b20.png)

And by clicking on **"Send Request"**, a new tab with all request response details will be opened.

[![doc.http response preview into VS Code](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fthepracticaldev.s3.amazonaws.com%2Fi%2Ffqamilfzz042c6vgvl5s.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fthepracticaldev.s3.amazonaws.com%2Fi%2Ffqamilfzz042c6vgvl5s.png)

### [](#go-further)Go further

You may also use environment variables to easily switch between you env and avoid any api-key or token manually update in the file, or url update etc...

Here is how to use environment variables, just like that :

"my-api.env-var": {

"$shared": {

"partnerUniqueToken": "A\_SHARED\_TOKEN"

},

"local": {

"host": "https://my-api-local.domain.com/v1",

"token": "MY\_LOCAL\_TOKEN"

},

"dev": {

"host": "https://my-api-dev.domain.com/v1",

"token": "MY\_DEV\_TOKEN"

},

"staging": {

"host": "https://my-api-staging.domain.com/v1",

"token": "MY\_STAGING\_TOKEN"

},

"production": {

"host": "https://my-api.domain.com/v1",

"token": "MY\_PROD\_TOKEN"

}

}

Here, I created 4 environments : local, dev, staging, production.

These 4 environments have their own host and token variables, with their specific values.  
But they also share a variable, named `partnerUniqueToken` (don't ask me why ... too many partners don't have several env...).

Hope it helps !

###### [](#big-up-to-julien-who-discovered-this-extension-)Big up to [Julien](https://dev.to/monisnapjulien) who discovered this extension !
