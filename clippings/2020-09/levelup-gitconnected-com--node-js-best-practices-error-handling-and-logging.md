---
url: "https://levelup.gitconnected.com/node-js-best-practices-error-handling-and-logging-341fc4ce6a72"
captured_at: "2020-09-21T15:10:01-03:00"
title: "Node.js Best Practices — Error Handling and Logging | by John Au-Yeung | Level Up Coding"
domain: "levelup-gitconnected-com"
---

# Node.js Best Practices — Error Handling and Logging

![0*m5MCIlkRK238MORB](levelup-gitconnected-com--node-js-best-practices-error-handling-and-logging/971f3ad97e48d0e337e41450932692dd.jpg)

Photo by [Honey Fangs](https://unsplash.com/@honeyfangs?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com/?utm_source=medium&utm_medium=referral)

Node.js is a popular runtime to write apps in JavaScript. To make maintaining them easier, we’ve to set some guidelines for people to follow.

In this article, we’ll look at how to document APIs and gracefully exit processes.

# Document API errors using GraphQL

We can build our API using GraphQL libraries. This provides us with a sandbox for querying data. It also provides strong typing and only returns what we want.

It also provides schema and comments so that we can document our APIs without adding more documentation.

To create a GraphQL API, we can use the `graphql` and `express-graphql` packages to create a GraphQL API. We install it by running:

```
npm i express-graphql graphql
```

Then we can create a simple GraphQL API by writing:

```
const express = require('express');  
const bodyParser = require('body-parser');  
const graphqlHTTP = require('express-graphql');  
const { buildSchema } = require('graphql');  
const app = express();app.use(bodyParser.json());  
app.use(bodyParser.urlencoded({ extended: true }));const schema = buildSchema(`  
  type Query {  
    quoteOfTheDay: String  
  }  
`);const root = {  
  quoteOfTheDay: () => {  
    return 'hello';  
  },  
};app.use('/graphql', graphqlHTTP({  
  schema: schema,  
  rootValue: root,  
  graphiql: true,  
}));app.listen(3000, () => console.log('server started'));
```

We should then be able to go to `/graphql` and test out our `quotwOfTheDay` query. Autocomplete should be available because of strong typing.

# Exit the Process Gracefully When an Unknown Error Occurs

When an unknown error occurs, we should exit the process since we don’t know why it’s failing. A common practice is to restart the process with a process management tool like Forever or PM2.

It’s a bad idea to continue running an app in a faulty state.

# Use a Mature Logger to Increase Error Visibility

To make errors easier to spot, we can use a logger like Winston, Bunyan, Log4js or Pino to log activities that happened in our app. For instance, we can use Winston with the `express-winston` package to add logging to an Express app as follows:

```
const express = require('express');  
const bodyParser = require('body-parser');  
const winston = require('winston');  
const expressWinston = require('express-winston');const app = express();  
app.use(bodyParser.json());  
app.use(bodyParser.urlencoded({ extended: true }));app.use(expressWinston.logger({  
  transports: [  
    new winston.transports.Console()  
  ],  
  format: winston.format.combine(  
    winston.format.colorize(),  
    winston.format.json()  
  ),  
  meta: true,  
  msg: "HTTP {{req.method}} {{req.url}}",  
  expressFormat: true,  
  colorize: false,  
  ignoreRoute: function (req, res) { return false; }  
}));app.get('/', (req, res, next) => {  
  res.send('hello')  
});app.get('/foo', (req, res, next) => {  
  try {  
    throw new Error('error')  
    res.send('hello')  
  } catch (err) {  
    next(err)  
  }  
});app.use((err, req, res, next) => {  
  res.send('error occurred')  
})  
app.listen(3000, () => console.log('server started'));
```

We just added the logger straight into our app by using the `expressWinston.logger` function.

# Test Error Flows Using Our Favorite Test Framework

Relying on manual testing is slow and error-prone. Therefore, we should add automated tests to our app. It lets us check for both positive and error scenarios by running code which runs in seconds.

There’re many test frameworks like Mocha, Chai, and Jest which can do this for us.

# Discover Errors and Downtime Using APM Products

We can use downtime and performance monitoring products to monitor the status of our app.

For Express apps, we can add the `express-status-monitor` package to watch the status of our app, including CPU and memory usage, response time, request per second, and more.

We just have to install the package by running:

```
npm i express-status-monitor
```

Then we can use it by writing the following code:

```
const express = require('express');  
const bodyParser = require('body-parser');const app = express();  
app.use(require('express-status-monitor')());  
app.use(bodyParser.json());  
app.use(bodyParser.urlencoded({ extended: true }));app.get('/', (req, res, next) => {  
  res.send('hello')  
});app.listen(3000, () => console.log('server started'));
```

We just put the package straight into our app with `app.use(require(‘express-status-monitor’)());` .

Then when we go to the `/status` page, we’ll see all the performance and health metrics listed.

![0*sReX3xl9eaIIfqvJ](levelup-gitconnected-com--node-js-best-practices-error-handling-and-logging/3c60c4f4b24d200e46f80adfad0f60fe.jpg)

![]()

Photo by [v2osk](https://unsplash.com/@v2osk?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com/?utm_source=medium&utm_medium=referral)

# Catch Unhandled Promise Rejections and Error Events

Unhandled promise rejections should be caught. Therefore, we should always add a `catch` callback for regular promises or `catch` block catching rejected promises.

We should also subscribe to the `process.unhandledRejection` to handle error events. For example, if we try to access a file that doesn’t exist and fails, we should write something :

```
const fs = require('fs')  
const stream = fs.createReadStream('does-not-exist')process.on('unhandledRejection', (reason, promise) => {  
  console.log(`Unhandled Rejection at: ${reason.stack || reason}`)  
})
```

Then we handle the error raised from trying to access a file that’s not found without crashing the app.

To catch rejected promises errors, we write:

```
Promise.reject('error')  
.catch(err=> console.log(err))
```

or:

```
(async()=>{  
  try {  
    await Promise.reject('error')  
  }  
  catch(ex){  
    console.log(ex);  
  }  
})();
```

# Conclusion

We should catch errors in our code and handle them gracefully. Also, we should log activities in our app with loggers and watch the health and performance of our app with a monitoring tool. Documentation of our app is also very important.
