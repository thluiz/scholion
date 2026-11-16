---
url: "https://toptal.com/nodejs/node-js-error-handling"
captured_at: "2026-11-16T06:06:11+00:00"
title: "Best Practices for Node.js Error-handling | Toptal®"
domain: "toptal-com"
---

BACK-END
7-MINUTE READ
How to Build a Node.js Error-handling System

Node.js developers often find themselves working with chaotic code that’s anything but clean. This can obviously cause productivity issues and outright errors.

In this article, Toptal Full-stack Developer Jay Huang will introduce you to error-handling in Node.js and demonstrate how you can build a robust error-handling system yourself.

Last updated: May 11, 2026
authors are vetted experts in their fields and write on topics in which they have demonstrated experience. All of our content is peer reviewed and validated by Toptal experts in the same field.

By
Jay Huang

Jay is a full-stack developer with extensive experience in computer science. He specializes in JavaScript but is also proficient in Django, RoR, GraphQL, and SQL.

It is not hard to see that some people are struggling to handle errors, and some are even totally missing it. Handling errors properly means not only reducing the development time by finding bugs and errors easily but also developing a robust codebase for large-scale applications.

In particular, Node.js developers sometimes find themselves working with not-so-clean code while handling various kinds of errors, incorrectly applying the same logic everywhere to deal with them. They just keep asking themselves “Is Node.js bad at handling errors?” or If not, how to handle them?” My answer to them is “No, Node.js is not bad at all. That depends on us developers.”

Here is one of my favorite solutions for that.

Node.js Error-handling: Error Types

First of all, it is necessary to have a clear understanding of errors in Node.js. In general, Node.js errors are divided into two distinct categories: operational errors and programmer errors.

Operational errors represent runtime problems whose results are expected and should be dealt with in a proper way. Operational errors don’t mean the application itself has bugs, but developers need to handle them thoughtfully. Examples of operational errors include “out of memory,” “an invalid input for an API endpoint,” and so on.
Programmer errors represent unexpected bugs in poorly written code. They mean the code itself has some issues to solve and was coded wrong. A good example is to try to read a property of “undefined.” To fix the issue, the code has to be changed. That is a bug a developer made, not an operational error.

With that in mind, you should have no problem distinguishing between these two categories of errors: Operational errors are a natural part of an application, and programmer errors are bugs caused by developers. A logical question that follows is: “Why is it useful to divide them into two categories and deal with them?”

Without a clear understanding of errors, you might feel like restarting an application whenever an error occurs. Does it make sense to restart an application due to “File Not Found” errors when thousands of users are enjoying the application? Absolutely not.

But what about programmer errors? Does it make sense to keep an application running when an unknown bug appears that could result in an unexpected snowball effect in the application? Again, definitely not!

It’s Time to Handle Errors Properly

Assuming you have some experience with async JavaScript and Node.js, you might have experienced drawbacks when using callbacks for dealing with errors. They force you to check errors all the way down to nested ones, causing notorious “callback hell” issues that make it hard to follow the code flow.

Using promises or async/await is a good replacement for callbacks. The typical code flow of async/await looks like the following:

const doAsyncJobs = async () => {
try {
const result1 = await job1();
const result2 = await job2(result1);
const result3 = await job3(result2);
return await job4(result3);
} catch (error) {
console.error(error);
} finally {
await anywayDoThisJob();
}
}

Using Node.js built-in Error object is a good practice because it includes intuitive and clear information about errors like StackTrace, which most developers depend on to keep track of the root of an error. And additional meaningful properties like HTTP status code and a description by extending the Error class will make it more informative.

class BaseError extends Error {
public readonly name: string;
public readonly httpCode: HttpStatusCode;
public readonly isOperational: boolean;

constructor(name: string, httpCode: HttpStatusCode, description: string, isOperational: boolean) {
super(description);
Object.setPrototypeOf(this, new.target.prototype);

this.name = name;
this.httpCode = httpCode;
this.isOperational = isOperational;

Error.captureStackTrace(this);
}
}

//free to extend the BaseError
class APIError extends BaseError {
constructor(name, httpCode = HttpStatusCode.INTERNAL_SERVER, isOperational = true, description = 'internal server error') {
super(name, httpCode, isOperational, description);
}
}

I only implemented some HTTP status codes for the sake of simplicity, but you are free to add more later.

export enum HttpStatusCode {
OK = 200,
BAD_REQUEST = 400,
NOT_FOUND = 404,
INTERNAL_SERVER = 500,
}

There is no need to extend BaseError or APIError, but it is okay to extend it for common errors according to your needs and personal preferences.

class HTTP400Error extends BaseError {
constructor(description = 'bad request') {
super('NOT FOUND', HttpStatusCode.BAD_REQUEST, true, description);
}
}

So how do you use it? Just throw this in:

...
const user = await User.getUserById(1);
if (user === null)
throw new APIError(
'NOT FOUND',
HttpStatusCode.NOT_FOUND,
true,
'detailed explanation'
);

Centralized Node.js Error-handling

Now, we are ready to build the main component of our Node.js error-handling system: the centralized error-handling component.

It is usually a good idea to build a centralized error-handling component in order to avoid possible code duplications when handling errors. The error-handling component is in charge of making the caught errors understandable by, for example, sending notifications to system admins (if necessary), transferring events to a monitoring service like Sentry.io, and logging them.

Here is a basic workflow for dealing with errors:

In some parts of the code, errors are passed to error-handling middleware when async route handlers reject or throw.

app.post('/users', async (req: Request, res: Response) => {
const newUser = await userService.addNewUser(req.body);
res.status(200).json(newUser);
});

In Express 5, rejected promises from async route handlers are automatically passed to the error-handling middleware. In Express 4, the same pattern requires a wrapper or an explicit catch(next) call to forward asynchronous errors correctly.

The error-handling middleware is a good place to distinguish between error types and send them to the centralized error-handling component. Knowing the basics about Express error-handling would certainly help. (It’s also worth a deep dive into Express error-handling best practices using Promises.)

app.use(async (err: Error, req: Request, res: Response, next: NextFunction) => {
if (!errorHandler.isTrustedError(err)) {
next(err);
}
await errorHandler.handleError(err);
});

By now, one can imagine what the centralized component should look like because we have already used some of its functions. Bear in mind that it is totally up to you how to implement it, but it might look like the following:

class ErrorHandler {
public async handleError(err: Error): Promise<void> {
await logger.error(
'Error message from the centralized error-handling component',
err,
);
await sendMailToAdminIfCritical();
await sendEventsToSentry();
}

public isTrustedError(error: Error) {
if (error instanceof BaseError) {
return error.isOperational;
}
return false;
}
}
export const errorHandler = new ErrorHandler();

Sometimes, the output of the default “console.log” makes it difficult to keep track of errors. Rather, it could be much better to print errors in a formatted way so that developers can quickly understand the issues and make sure they are fixed.

Overall, this will save developers time making it easy to keep track of errors and handle them by increasing their visibility. It is a good decision to employ a customizable logger like winston or morgan.

Here is a customized winston logger:

const customLevels = {
levels: {
trace: 5,
debug: 4,
info: 3,
warn: 2,
error: 1,
fatal: 0,
},
colors: {
trace: 'white',
debug: 'green',
info: 'green',
warn: 'yellow',
error: 'red',
fatal: 'red',
},
};

const formatter = winston.format.combine(
winston.format.colorize(),
winston.format.timestamp({ format: 'YYYY-MM-DD HH:mm:ss' }),
winston.format.splat(),
winston.format.printf((info) => {
const { timestamp, level, message, ...meta } = info;

return `${timestamp} [${level}]: ${message} ${
Object.keys(meta).length ? JSON.stringify(meta, null, 2) : ''
}`;
}),
);

class Logger {
private logger: winston.Logger;

constructor() {
const prodTransport = new winston.transports.File({
filename: 'logs/error.log',
level: 'error',
});
const transport = new winston.transports.Console({
format: formatter,
});
this.logger = winston.createLogger({
level: isDevEnvironment() ? 'trace' : 'error',
levels: customLevels.levels,
transports: [isDevEnvironment() ? transport : prodTransport],
});
winston.addColors(customLevels.colors);
}

trace(msg: any, meta?: any) {
this.logger.log('trace', msg, meta);
}

debug(msg: any, meta?: any) {
this.logger.debug(msg, meta);
}

info(msg: any, meta?: any) {
this.logger.info(msg, meta);
}

warn(msg: any, meta?: any) {
this.logger.warn(msg, meta);
}

error(msg: any, meta?: any) {
this.logger.error(msg, meta);
}

fatal(msg: any, meta?: any) {
this.logger.log('fatal', msg, meta);
}
}

export const logger = new Logger();

What it basically provides is logging at multiple different levels in a formatted way, with clear colors, and logging into different output media according to the runtime environment. The good thing with this is you can watch and query logs by using winston’s built-in APIs. Furthermore, you can use a log analysis tool to analyze the formatted log files to get more useful information about the application. It’s awesome, isn’t it?

In modern production environments, structured logs are often integrated with observability platforms such as Datadog, New Relic, or OpenTelemetry. These tools allow teams to correlate logs with metrics and traces, making it easier to diagnose issues across distributed systems and understand application behavior in real time.

Up to this point, we mostly discussed dealing with operational errors. How about programmer errors? The best way to deal with these errors is to crash immediately and restart gracefully with an automatic restarter like PM2—the reason being that programmer errors are unexpected, as they are actual bugs that might cause the application to end up in a wrong state and behave in an unexpected way.

process.on('uncaughtException', (error: Error) => {
errorHandler.handleError(error);
if (!errorHandler.isTrustedError(error)) {
process.exit(1);
}
});

Last but not least, I am going to mention dealing with unhandled promise rejections and exceptions.

You might find yourself spending a lot of time dealing with promises when working on Node.js/Express applications. It is not hard to see warning messages about unhandled promise rejections when you forget to handle rejections.

In modern Node.js versions, unhandled promise rejections are treated more strictly than they once were. Since Node.js 15, the default behavior is to raise an unhandled rejection as an uncaught exception when no unhandledRejection hook is set. A global unhandledRejection handler is still useful, but its main role is now cleanup, logging, and graceful shutdown rather than simply preventing a warning.

The typical error-handling flow might look like the following:

// somewhere in the code
...
User.getUserById(1).then((firstUser) => {
if (firstUser.isSleeping === false) throw new Error('He is not sleeping!');
});
...

// get the unhandled rejection and throw it to another fallback handler we already have.
process.on('unhandledRejection', (reason: Error, promise: Promise<any>) => {
throw reason;
});

process.on('uncaughtException', (error: Error) => {
errorHandler.handleError(error);
if (!errorHandler.isTrustedError(error)) {
process.exit(1);
}
});

Error-handling in Node.js: A Must-have

When all is said and done, you should realize that error-handling is not an optional extra but rather an essential part of an application, both in the development stage and in production.

The strategy of handling errors in a single component in Node.js will ensure developers save valuable time and write clean and maintainable code by avoiding code duplication and missing error context.

I hope you enjoyed reading this article and found the discussed error-handling workflow and implementation helpful for building a robust codebase in Node.js.

Further Reading on the Toptal Blog:
Using Express.js Routes for Promise-based Error Handling
How to Use JWT and Node.js for Better App Security
UNDERSTANDING THE BASICS
Why is error-handling important?

Proper error-handling makes apps robust resulting in superior user experience and improved productivity.

What are the strategies or techniques used for error-handling?

Using promises or async/await, handling errors in a centralized component, handling uncaught exceptions.

Why do we need error-handling?

Error-handling is a must-have part of all apps. It prevents apps from being error-prone and saves valuable development time.

How do you handle unchecked exceptions?

By subscribing to process.on(‘unhandledRejection’), process.on(‘uncaughtException’)

Is Node.js bad at handling errors?

No, it is not. That depends on developers and the way they choose to handle them.
