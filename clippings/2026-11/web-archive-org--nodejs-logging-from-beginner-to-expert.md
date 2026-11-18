---
url: "https://web.archive.org/web/20200418035704id_/https://dev.to/gkoniaris/nodejs-logging-from-beginner-to-expert-30a6"
captured_at: "2026-11-18T12:18:32+00:00"
title: "NodeJS logging, from beginner to expert."
domain: "web-archive-org"
---

This article was originally published [here](https://gkoniaris.gr/nodejs/nodejs-logging-from-beginner-to-expert).

In this tutorial, we will discuss how to correctly perform logging on NodeJS. We will start from simple console logs, moving to more advanced features, one step at a time. At the end of this read, you will be able to create a custom logger using the Winston npm library and add transports where logs will be streamed. You will also learn how to add some advanced features, like request tracking and how to implement extra safety precautions that will make you sleep like a baby at night.

I recommend that you clone the code from my [Github repo](https://github.com/gkoniaris/blog/tree/master/logging-tutorial), as this is a big tutorial and it will be easier to follow the steps this way. Let’s make it happen!!!

Just a note. This tutorial will get you from simple logging using console.log to advanced logging features. You can skip any parts that you think are too basic for your experience. Please decide which of the following logging practices is best for your own circumstances, based on your application size, requirements, etc. You can stop at any step you think is enough for your own needs. For the sake of simplicity, I am using ExpressJS for all the examples. Most NodeJS developers have used ExpressJS for at least one time in their life, and there is plenty of documentation.

### [](#the-most-simple-form-of-nodejs-logging-the-console-object)The most simple form of NodeJS logging, the console object

So we have set up an ExpressJS API and we want to start adding logs to our web application. Let’s assume that we want to retrieve a post from the database, and then return its data through the API.  

```
app.get('/post/:id', function (req, res) {
  // We have created a fake model class with a function that returns a post in case id === 1, or null in all other cases

  // In a real world example we would use async await 
  // or use a promise based structure
  const post = Post.find(req.params.id); 
  return res.json({post});
});
```

We are ready. Let’s add some logs to our API call. We will add an info log for the case that the post is not found, and an error log for the case that the connection with the database throws an exception.

For the following example, we have to mention that id 2 returns null. Id 3 throws an exception in the fake Post model.  

```
app.get('/post/:id', function (req, res) {
  try {
    const id = req.params.id;
    const post = Post.find(id); // We assume that we have some kind of ORM in the app.

    if (!post) {
      console.log(`Post with id ${id} was not found`);
      return res.status(404).json({error: 'Post not found'});
    }

    return res.json({post});
  } catch(e) {
    console.log(e);
    return res.status(500).json({error: 'Something went wrong'});
  }
});
```

We wrapped the code in a try-catch clause and handled the database exception by logging an error. We also handled the case where the post with the provided id does not exist and printed an info log.

This way, we have our first logging mechanism, kind of. When we use console.log we get a simple log like “Post with id 2 was not found”. When we try to retrieve post with id 3, we get an error along with its stack trace, prefixed with the string “Error:”.  

```
Error: Database unreachable
    at .......
```

Now, let’s take NodeJS logging to the next level.

### [](#use-a-dedicated-nodejs-npm-logging-library)Use a dedicated NodeJS npm logging library

We have already made progress, we went from no logging to some logging in just one step. We also found out how we can use different log levels by using the Javascript console function. But what if we want more?

We can create a NodeJS module that exposes console.log functions, and maybe uses a module like `chalk` to color the output of these logs. But then what if we need to only show specific logs based on their level on a production server? We don’t want to show debug logs on a production system. We can create a function to filter logs based on their level. And then what about formatting? Nahhh, that’s too much job. What we can and in most cases should do, is use a professional library to perform logging. For the following examples, I will use the Winston npm logging library.

##### [](#installation)Installation

So let’s build a NodeJS logging module. First, we have to install Winston. We can do this by running the following command in our terminal:  

```
npm install --save winston
```

##### [](#basic-setup)Basic setup

Then we have to create a class for our logger. The reason we create a class (or a function, whatever you like) instead of using the logger directly is that it grants us the ability to extend and override its functionality.  

```
const winston = require('winston');

class Logger {
  constructor(name) {
    this.logger = winston.createLogger({
        level: 'info',
        defaultMeta: { service: name }
    });
  }

  // We expose four levels of logging for this tutorial

  debug(log, metadata) {
    this.logger.debug(log, metadata);
  }

  info(log, metadata) {
    this.logger.info(log, metadata);
  }

  warn(log, metadata) {
    this.logger.warn(log, metadata);
  }

  error(log, metadata) {
    this.logger.error(log, metadata);
  }

  log(level, log, metadata) {
      const metadataObject = {}
      if (metadata) metadataObject.metadata = metadata

      this.logger[level](log, metadataObject)
  }
}

// We want our logger to have a name, like 'logging-tutorial'
module.exports = new Logger(process.env.APP_NAME)

// We will also expose a function if we want
// to use the logger with custom parameters
module.getLogger = (name) => {
  return new Logger(name);
}
```

We created four functions, one for each level of severity. A general log function was also created to be called from these functions. This function is generic and it will contain all the logger’s logic. Text or objects can be passed as the first argument, as well as an object containing metadata as the second argument.

### [](#create-a-console-transport-and-format-logs)Create a console transport and format logs

Our logger is set up, now let’s give it a try and see what logs it produces. In this example we will use the following test API:  

```
app.get('/logger', function(req, res) {
  logger.info('I am an info log', {name: 'George', tutorial: 'Logging tutorial'});
  return res.json({logged: true});
});
```

If we try to call this API, we will get the following:  

```
[winston] Attempt to write logs with no transports {"service":"logging-tutorial","level":"info","message":"I am an info log"}
```

That’s because we have not configured our logger to use any transports. Without transports, Winston doesn’t know where to send logs. So, let’s add our first transport. We have to change the constructor’s code to this:  

```
constructor(name) {
    this.logger = winston.createLogger({
        level: 'debug',
        defaultMeta: { service: name },
        transports: [
            new winston.transports.Console({
                format: winston.format.combine(
                    winston.format.timestamp(),
                    winston.format.metadata({fillExcept: ['timestamp', 'service', 'level', 'message']}),
                    winston.format.colorize(),
                    this.winstonConsoleFormat()
               )
           })
    ]
});
```

I know, I know… too much info here. So let’s break it down. Firstly, we added a transports array in our Winston options object, which from now on will contain all transports that will be used by Winston. We added a Console transport in the array, so Winston can log to the terminal. We also set the following formats.

##### [](#winston-formats-explained)Winston formats explained

*   timestamp(). Exposes the timestamp field to use in another format.
*   metadata(). Exposes the metadata field to use in another format. We also set the option fillExcept, because by default metadata contains a timestamp, message, service, and level key. We will log them as text so we don’t want them in the metadata object.
*   colorize(). Colorize specific parts of the log, like the log level.
*   winstonConsoleFormat(). Our custom formatter, we will explain it’s code right now.

```
winstonConsoleFormat() {
    return printf(({ timestamp, level, message, metadata }) => {
        const metadataString = metadata != null ? JSON.stringify(metadata) : '';

        return `[${timestamp}][${level}][${this.name}@${this.hostname}] ${message}. ${'metadata: ' + metadataString}`;
    })
}
```

We just concatenated all the info in one single line and added the hostname of the machine running the application, using the `os.getHostname()` command, from the built-in NodeJS `os` module. Our function returns the printf function, as this is what Winston expects.

By testing this API call we will get something like the following in our console.  

```
[2020-04-16T14:08:47.023Z][info][logging-tutorial@ubuntu] I am a log Metadata: {"author":"George","tutorial":"Logging tutorial"}
```

That’s pretty nice, right? We have a tone of extra info about our log now, like the time it was logged, the hostname of our machine, the name of the logger as well as the log’s severity level. Our log is also presented in a nice human-readable format. Furthermore, we can pass extra metadata that will help us debug each problem easier.

### [](#allow-only-specific-severity-levels-to-be-logged)Allow only specific severity levels to be logged

In the previous examples, we got rid of console logs, we used a professional logging library and explained how it works, and how to format logs in a way that is meaningful. In this step, we will show how to set the minimum log level of the logger, and why it matters.

First, let’s deep into the code. To set a minimum log level for our logger, we will change the Console transport, so it takes the log level from a variable. We will set the minimum level to ‘info’, so we don’t get annoying debug messages in our production server. To do this, we will change the code that creates the logger and make it look like the following:  

```
this.logger = winston.createLogger({
        level: options.logLevel,
......
```

So now our logger will do the exact same thing, but we can now pass the severity level through the options object. Let’s move the ‘info’ string, to an env variable and pass it to the logger when we are exporting it. This way we can define it in our .env file, and make it easier to change in the future.  

```
module.exports = new Logger(process.env.APP_NAME, {
    logLevel: process.env.LOG_LEVEL
});
```

O.k., but why even bother doing something like this. There are a couple of reasons that you should consider not allowing all kinds of severity levels in your production environment.

*   We don’t want to pollute our valuable log stream with annoying debug or trace logs.
*   In case we use some kind of persistent storage, something that we will discuss later in this tutorial, we may end up with a great number of logs occupying too much space in our server.
*   Streaming to the `process.stdout`, although an asynchronous process, can be a resource-intensive operation if you use it without limit.

### [](#persist-our-logs-to-files)Persist our logs to files

Watching our logs while running your app form a terminal is very useful. But some times we may have to check old logs, to debug something that occurred days ago. To achieve this we have to persist our logs to some kind of storage. The most common solution is to persist our logs in files.

Winston allows us to define a transport to stream our logs to files. By defining a file transport our logs will be written to that file, along with the terminal. We will not use an npm module to do this, as Winston comes with built-in file streaming functionality.

As we did before, we will just add a new entry in the transports array. The transport will look like the following.  

```
new winston.transports.File({ 
    filename: './logs/' + name + '.log',
    format: winston.format.combine(
        winston.format.errors({ stack: true }),
        winston.format.metadata(),
        winston.format.json()
    )
})
```

We set the filename of the logs to \[name\].log, so we can have separate log files for each application that we run (eg each microservice). Please refer to the Winston documentation if you want to suffix your log files with the current date.

So now, logs will also be streamed to ./logs/logging-tutorial.log file. Keep in mind that you can define different log levels for each stream based on your needs. Logging in files is very important, and it is one of the most fault-tolerant ways to log. Unless you run out of disk space or there is a corrupted disk, it’s almost impossible to have logs not been written to the file, while streaming them.

### [](#use-an-external-logging-provider)Use an external logging provider

Sometimes we want to make our logs searchable, so we can easily track bugs, assign them to developers and more. We can do this by using an external logging provider, or by setting up some kind of storage that allows this kind of operations, like Elasticsearch. In this part, we will show how to integrate our logger with Sentry. Sentry is a tool allowing us to aggregate all our logs, filter them, assign them to developers, mark them as resolved and find regressions.

#### [](#setup-the-transport)Setup the transport

We will use an npm module implementing the Sentry transport (we will show how to make a custom transport in another tutorial). The module is called `winston-sentry-log`. I have created a free account on [Sentry](https://sentry.io/) and added the DSN of the project that I created to my .env file. DSN is a URL used to post logs to sentry, and you can find it in the Sentry dashboard under the project that you created. So, let’s the transport:  

```
npm install --save winston-sentry-log
```

After installing `winston-sentry-log`, we just have to require the module in our logger and add the Winston transport to the logger’s transport array.  

```
// On top of logger file
const Sentry = require('winston-sentry-log');
....
....
// Inside the transports array
new Sentry({
    config: {
        dsn: process.env.SENTRY_DSN
    },
    level: "warn"
})
```

It seems like magic, but we are ready! Do you see how easy it is to add new transports to Winston? There is a huge list of plug and play transports that you can install from npm. Now our logs will be sent to Sentry without any extra effort. I chose to send warnings and error logs only, but you can pass whatever severity level you like from the options object.

This is what we get in the Sentry UI.

[![](https://res.cloudinary.com/practicaldev/image/fetch/s--OqkeeKjk--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://cdn.gkoniaris.gr/wp-content/uploads/2020/04/sentry-1024x349.png)](https://res.cloudinary.com/practicaldev/image/fetch/s--OqkeeKjk--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://cdn.gkoniaris.gr/wp-content/uploads/2020/04/sentry-1024x349.png)An info log in the Sentry UIHmm, but what happened to the author field? Sentry has some built-in data scrubbers and it considered that an author field could leak important info. That’s why it was filtered out. You can disable this functionality and add your own sensitive fields. We will try to implement something like in our logger, later in this tutorial.

### [](#abstract-parts-of-our-nodejs-logging-using-middlewares)Abstract parts of our NodeJS logging using middlewares

We’ve made great progress till now. But there is something that I don’t really like. Let’s see the following example.  

```
app.get('/automated-error-handling', function(req, res) {
    try {
        Post.find(3);
        return res.json({success: true})
    } catch(e) {
        logger.error(e);
        return res.status(500).json({error: 'Something went wrong'});
    }
});
```

Do you see what’s wrong in this example, or at least could be improved? We handle exceptions that cannot be prevented, like an unreachable database, log the error that occurred, and always return the same JSON response in our API. Could we abstract this logic somewhere else?

Of course, and in my humble opinion it’s a must. Let’s move this logic to an express post-middleware.  

```
const logger = require('../libs/Logger')

module.exports = function(err, req, res, next){
    if (err) {
        logger.error(err);
    }

    return res.status(500).json({error: 'Something went wrong'});
}
```

Yes, that’s all. We will use our middleware after all our routes are registered like this:  

```
app.use(require('./middlewares/postErrorHandler'))
```

This way, when an error is thrown and not caught inside a route or controller, it will be caught by this post middleware, the error will be logged and a message will be returned from the API, informing the user that something went wrong. So, our previous example would become something like this:  

```
app.get('/logging-tutorial/v2/automated-error-handling', function(req, res) {
    Post.find(3);
    return res.json({success: true})
});
```

Basically, by abstracting these logs and the part of the JSON response, we automatically get rid of every try-catch clause that was responsible for handling errors that we cannot prevent just by writing extra code, like a database connection problem.

### [](#keep-track-of-our-nodejs-logs-order)Keep track of our NodeJS logs order

Let’s suppose that we perform a complex operation in our API, and we have multiple steps with multiple info logs. Wouldn’t it be nice to be able to keep track of these logs order and context?

For this, we will use NodeJS async hooks. This is an experimental NodeJS API so if you decide to use it, please test thoroughly before deploying. Now, let’s create our LocalStorage library. We will export a new instance of NodeJS local storage.  

```
const { AsyncLocalStorage } = require('async_hooks');
const asyncLocalStorage = new AsyncLocalStorage();

module.exports = asyncLocalStorage;
```

We will also change our log funtion to start like this.  

```
const store = LocalStorage.getStore();
const metadataObject = {};

if (store) {
    metadataObject.uniqueId = store.id;
}
```

Now, we will retrieve the current store and inject the store.id field in the metadataObject. We will show how to start a new store for each request in the following example.  

```
app.get('/logging-tutorial/async-hook', function(req, res) {
    // We have installed a uuid module to produce unique ids
    const store = LocalStorage.enterWith({id: uuid()});
    logger.info('I am the first log');
    logger.info('I am the second log');
    logger.info('I am the third log');
    return res.json({});
})
```

By using the enterWith function, and injecting a UUID to the store, the UUID will follow the request until it ends. So even if we log by calling a service that exists in another file, for example, the UUID logged in the metadataObject will always be the same for the specific request. Then, we can filter our logs based on the UUID, and sort them by timestamp.

So, by running these logs we will get:  

```
[2020-04-16T15:49:53.354Z][info][logging-tutorial@ubuntu] I am the first log. Metadata: {"uniqueId":"e8be59d6-2d44-46e5-8665-82759beadfee"}
[2020-04-16T15:49:53.357Z][info][logging-tutorial@ubuntu] I am the second log. Metadata: {"uniqueId":"e8be59d6-2d44-46e5-8665-82759beadfee"}
[2020-04-16T15:49:53.358Z][info][logging-tutorial@ubuntu] I am the third log. Metadata: {"uniqueId":"e8be59d6-2d44-46e5-8665-82759beadfee"}

```

If we rerun the request, we will get:  

```
[2020-04-16T15:49:57.432Z][info][logging-tutorial@ubuntu] I am the first log. Metadata: {"uniqueId":"227899b6-efd5-4b52-92fb-a316d72c81ab"}
[2020-04-16T15:49:57.435Z][info][logging-tutorial@ubuntu] I am the second log. Metadata: {"uniqueId":"227899b6-efd5-4b52-92fb-a316d72c81ab"}
[2020-04-16T15:49:57.437Z][info][logging-tutorial@ubuntu] I am the third log. Metadata: {"uniqueId":"227899b6-efd5-4b52-92fb-a316d72c81ab"}
```

You can also create a pre middleware for ExpressJS, so the uniqueId is injected automatically in every request. By binding a context to your logs, you can easier debug errors by checking all info or warning logs that were printed before the final error, by tracing the logs by their UUID.

### [](#allow-stack-traces-to-be-manually-logged)Allow stack traces to be manually logged

We know that when we log an error the stack trace is automatically logged. But sometimes, we just want to log the current stack trace for an info log, just for debugging purposes. We may need the filename and the line where a log was printed, or trace from which file the logger was called. To achieve this, we can manually create an empty error inside our logger and just retrieve its stack trace.

To achieve this, we will create a custom function called, logTrace.  

```
logTrace(level, log, metadata) {
    const stackTrace = new Error().stack;
    this.log(level, log, metadata, stackTrace);
}
```

So by calling logTrace, an error will be created, and it will be forwarded to the log function along with all data passed to the logTrace function, like level, log, metadata and the stack trace of course.

Then, in the log function, we will just inject the stack trace in the metadataObject, so it will be printed along with the log.  

```
if (stackTrace) metadataObject.stackTrace = stackTrace;
```

### [](#make-our-nodejs-logger-a-little-safer)Make our NodeJS logger a little safer

In an earlier step, we saw that Sentry filtered out the author field in our metadata. Wouldn’t it be cool to be able to filter our metadataObject in the console and files transports too? Let’s take our NodeJS logging module a step further.

What we are going to do is inject a list of top level keys that we consider sensitive in our constructor.  

```
if (options.sensitiveFields) {
    //eg ['password', 'creditCard']
    this.sensitiveFields= options.sensitiveFields;
    this.checkSensitiveFields = true;
}
```

Now in our log function, we can perform a check, inside our metadataObject, and if any sensitive fields are found, we will log a warning instead of the original log.  

```
if (this.checkSensitiveFields) {
    const sensitiveFieldFound = Object.keys(metadataObject.metadata || {}).find(key => this.sensitiveFields.includes(key));
    if (sensitiveFieldFound) return this.logTrace('warn', `You tried to log the following sensitive key: "${sensitiveFieldFound}". Please check attached stack trace.`);
}
```

Boom!!! We just saved the day. Now if we try to log a password in the metadata, we will get the following warning log.  

```
// Removed stack trace to save space
You tried to log the following sensitive key: "password". Please check attached stack trace.. METADATA: {"stackTrace":"...."}
```

### [](#decide-what-log-rotation-strategy-we-want-to-use)Decide what log rotation strategy we want to use

Although there are transports for rotating logs using Winston, I personally think that it’s not the logger’s responsibility to do stuff like that. I prefer to use a tool like pm2 that has an extension for log rotation, or even better the log-rotate tool that many UNIX distributions offer. That’s all for the technical part of this section, I won’t get into details on how to perform log rotation using pm2 or Linux.

Now, there are two main reasons that you should perform log rotation.

##### [](#logs-size)Logs size

In case you don’t perform systematic log rotation, sooner or later you will get in a situation that the logs kept in your server will occupy a great amount of space. Make sure you implement log rotation as one of the first steps in your NodeJS logging strategy.

##### [](#legal-reasons)Legal reasons

In some cases, you will have to delete old logs due to the fact that they are considered identifiable personal user data. You may want to keep this logs in some other kind of storage if your country’s law allows it. Please consult a professional lawyer for stuff like that.

### [](#how-do-you-perform-nodejs-logging)How do you perform NodeJS logging?

In this article, I tried to create a complete NodeJS logging tutorial. Some of the features mentioned above may be an overkill for a small project. On the other hand, some other features may be a performance killer for APIs. One example would be handling millions of requests per day and checking every log for sensitive fields. If you think that any of those features cause a bottleneck to your application, you can move them in another layer. A good example would be request logging, which can be run in the proxy server.

If you liked my NodeJS logging tutorial, you can share it on your favorite social networks. I would also be very interested to hear about your approach to how you perform NodeJS logging in your personal or professional setup.

Below you will find some of the articles related to logging and ExpressJS. I hope they will help you get your NodeJS Logging to the next level.

[Before and after middlewares in ExpressJS](https://medium.com/@ganeshsurfs/expressjs-series-how-can-i-implement-before-and-after-middlewares-13da90892d72)

[A great tutorial about Continuation Local Storage](https://medium.com/trabe/continuation-local-storage-for-easy-context-passing-in-node-js-2461c2120284)

[Async await usage and global error handling in ExpressJS](https://medium.com/@Abazhenov/using-async-await-in-express-with-node-8-b8af872c0016)

And finally…

[The official winston documentation](https://www.npmjs.com/package/winston)

[Business vector created by fullvector – www.freepik.com](https://www.freepik.com/free-photos-vectors/business)
