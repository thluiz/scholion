---
url: "https://www.toptal.com/express-js/routes-js-promises-error-handling?utm_campaign=Toptal%20Engineering%20Blog&utm_medium=email&_hsmi=146444123&_hsenc=p2ANqtz-_y50iEQ9NYud-e3vXiuxiGpG2qBFu9jj6kUqLJX1qmsoA_LUTciVzFJEb7_DPZfqczP6_pyAdoWsDnxnoG6L1JS-MlWA&utm_content=146444123&utm_source=hs_email"
captured_at: "2021-08-04T12:25:27-03:00"
title: "Using Express.js Routes for Promise-based Error Handling | Toptal"
domain: "toptal-com"
---

# Using Express.js Routes for Promise-based Error Handling

The Express.js tagline rings true: It’s a “fast, unopinionated, minimalist web framework for Node.js.” It’s so unopinionated that, despite current [JavaScript best practices](https://www.toptal.com/javascript/asynchronous-javascript-async-await-tutorial) prescribing the use of promises, Express.js doesn’t support promise-based route handlers by default.

With many Express.js tutorials leaving out that detail, developers often get in the habit of copying and pasting result-sending and error-handling code for each route, creating technical debt as they go. We can avoid this antipattern (and its fallout) with the technique we’ll cover today—one I’ve used successfully in apps with hundreds of routes.

## Typical Architecture for Express.js Routes

Let’s start with an Express.js tutorial application with a few routes for a user model.

In real projects, we would store the related data in some database like MongoDB. But for our purposes, data storage specifics are unimportant, so we will mock them out for the sake of simplicity. What we won’t simplify is good project structure, the key to half the success of any project.

Yeoman can yield much better project skeletons in general, but for what we need, we’ll simply create a project skeleton with [express-generator](https://expressjs.com/en/starter/generator.html) and remove the unnecessary parts, until we have this:

```
bin
  start.js
node_modules
routes
  users.js
services
  userService.js
app.js
package-lock.json
package.json
```

We’ve pared down the lines of the remaining files that aren’t related to our goals.

Here’s the main Express.js application file, `./app.js`:

```
const createError  = require('http-errors');
const express = require('express');
const cookieParser = require('cookie-parser');
const usersRouter = require('./routes/users');

const app = express();
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(cookieParser());
app.use('/users', usersRouter);
app.use(function(req, res, next) {
  next(createError(404));
});
app.use(function(err, req, res, next) {
  res.status(err.status || 500);
  res.send(err);
});

module.exports = app;
```

Here we create an Express.js app and add some basic middleware to support JSON use, URL encoding, and cookie parsing. We then add a `usersRouter` for `/users`. Finally, we specify what to do if no route is found, and how to handle errors, which we will change later.

The script to start the server itself is `/bin/start.js`:

```
const app = require('../app');
const http = require('http');

const port = process.env.PORT || '3000';

const server = http.createServer(app);
server.listen(port);
```

Our `/package.json` is also barebones:

```
{
  "name": "express-promises-example",
  "version": "0.0.0",
  "private": true,
  "scripts": {
    "start": "node ./bin/start.js"
  },
  "dependencies": {
    "cookie-parser": "~1.4.4",
    "express": "~4.16.1",
    "http-errors": "~1.6.3"
  }
}
```

Let’s use a typical user router implementation in `/routes/users.js`:

```
const express = require('express');
const router = express.Router();

const userService = require('../services/userService');

router.get('/', function(req, res) {
  userService.getAll()
    .then(result => res.status(200).send(result))
    .catch(err => res.status(500).send(err));
});

router.get('/:id', function(req, res) {
  userService.getById(req.params.id)
    .then(result => res.status(200).send(result))
    .catch(err => res.status(500).send(err));
});

module.exports = router;
```

It has two routes: `/` to get all users and `/:id` to get a single user by ID. It also uses `/services/userService.js`, which has promise-based methods to get this data:

```
const users = [
  {id: '1', fullName: 'User The First'},
  {id: '2', fullName: 'User The Second'}
];

const getAll = () => Promise.resolve(users);
const getById = (id) => Promise.resolve(users.find(u => u.id == id));

module.exports = {
  getById,
  getAll
};
```

Here we’ve avoided using an actual DB connector or ORM (e.g., Mongoose or Sequelize), simply mimicking data fetching with `Promise.resolve(...)`.

## Express.js Routing Problems

Looking at our route handlers, we see that each service call uses duplicate `.then(...)` and `.catch(...)` callbacks to send data or errors back to the client.

At first glance, this may not seem serious. Let’s add some basic real-world requirements: We’ll need to display only certain errors and omit generic 500-level errors; also, whether we apply this logic or not must be based on the environment. With that, what will it look like when our example project grows from its two routes into a real project with 200 routes?

## Approach 1: Utility Functions

Maybe we would create separate utility functions to handle `resolve` and `reject`, and apply them everywhere in our Express.js routes:

```
// some response handlers in /utils 
const handleResponse = (res, data) => res.status(200).send(data);
const handleError = (res, err) => res.status(500).send(err);

// routes/users.js
router.get('/', function(req, res) {
  userService.getAll()
    .then(data => handleResponse(res, data))
    .catch(err => handleError(res, err));
});

router.get('/:id', function(req, res) {
  userService.getById(req.params.id)
    .then(data => handleResponse(res, data))
    .catch(err => handleError(res, err));
});
```

Looks better: We’re not repeating our implementation of sending data and errors. But we’ll still need to import these handlers in every route and add them to each promise passed to `then()` and `catch()`.

## Approach 2: Middleware

Another solution could be to use Express.js [best practices](http://expressjs.com/en/advanced/best-practice-performance.html#use-promises) around promises: Move error-sending logic into Express.js error middleware (added in `app.js`) and pass async errors to it using the `next` callback. Our basic error middleware setup would use a simple anonymous function:

```
app.use(function(err, req, res, next) {
  res.status(err.status || 500);
  res.send(err);
});
```

Express.js understands that this is for errors because the function signature has four input arguments. (It leverages the fact that every function object has a `.length` property describing how many parameters the function expects.)

Passing errors via `next` would look like this:

```
// some response handlers in /utils 
const handleResponse = (res, data) => res.status(200).send(data);

// routes/users.js
router.get('/', function(req, res, next) {
  userService.getAll()
    .then(data => handleResponse(res, data))
    .catch(next);
});

router.get('/:id', function(req, res, next) {
  userService.getById(req.params.id)
    .then(data => handleResponse(res, data))
    .catch(next);
});
```

Even using the official best practice guide, we still need our JS promises in every route handler to resolve using a `handleResponse()` function and reject by passing along the `next` function.

Let’s try to simplify that with a better approach.

## Approach 3: Promise-based Middleware

One of the greatest features of JavaScript is its dynamic nature. We can add any field to any object at runtime. We’ll use that to extend Express.js result objects; Express.js middleware functions are a convenient place to do so.

### Our `promiseMiddleware()` Function

Let’s create our promise middleware, which will give us the flexibility to structure our Express.js routes more elegantly. We’ll need a new file, `/middleware/promise.js`:

```
const handleResponse = (res, data) => res.status(200).send(data);
const handleError = (res, err = {}) => res.status(err.status || 500).send({error: err.message});

module.exports = function promiseMiddleware() {
  return (req,res,next) => {
    res.promise = (p) => {
      let promiseToResolve;
      if (p.then && p.catch) {
        promiseToResolve = p;
      } else if (typeof p === 'function') {
        promiseToResolve = Promise.resolve().then(() => p());
      } else {
        promiseToResolve = Promise.resolve(p);
      }

      return promiseToResolve
        .then((data) => handleResponse(res, data))
        .catch((e) => handleError(res, e));  
    };

    return next();
  };
}
```

In `app.js`, let’s apply our middleware to the overall Express.js `app` object and update the default error behavior:

```
const promiseMiddleware = require('./middlewares/promise');
//...
app.use(promiseMiddleware());
//...
app.use(function(req, res, next) {
  res.promise(Promise.reject(createError(404)));
});
app.use(function(err, req, res, next) {
  res.promise(Promise.reject(err));
});
```

Note that **we do not omit our error middleware**. It’s still an important error handler for all synchronous errors that may exist in our code. But instead of repeating error-sending logic, the error middleware now passes any synchronous errors to the same central `handleError()` function via a `Promise.reject()` call sent to `res.promise()`.

This helps us handle synchronous errors like this one:

```
router.get('/someRoute', function(req, res){
  throw new Error('This is synchronous error!');
});
```

Finally, let’s use our new `res.promise()` in `/routes/users.js`:

```
const express = require('express');
const router = express.Router();

const userService = require('../services/userService');

router.get('/', function(req, res) {
  res.promise(userService.getAll());
});

router.get('/:id', function(req, res) {
  res.promise(() => userService.getById(req.params.id));
});

module.exports = router;
```

Note the different uses of `.promise()`: We can pass it a function or a promise. Passing functions can help you with methods that don’t have promises; `.promise()` sees that it’s a function and wraps it in a promise.

Where is it better to actually send errors to the client? It’s a good code-organization question. We could do that in our error middleware (because it’s supposed to work with errors) or in our promise middleware (because it already has interactions with our response object). I decided to keep all response operations in one place in our promise middleware, but it’s up to each developer to organize their own code.

### Technically, `res.promise()` Is Optional

We’ve added `res.promise()`, but we’re not locked into using it: We’re free to operate with the response object directly when we need to. Let’s look at two cases where this would be useful: redirecting and stream piping.

### Special Case 1: Redirecting

Suppose we want to redirect users to another URL. Let’s add a function `getUserProfilePicUrl()` in `userService.js`:

```
const getUserProfilePicUrl = (id) => Promise.resolve(`/img/${id}`);
```

And now let’s use it in our users router in `async`/`await` style with direct response manipulation:

```
router.get('/:id/profilePic', async function (req, res) {
  try {
    const url = await userService.getUserProfilePicUrl(req.params.id);
    res.redirect(url);
  } catch (e) {
    res.promise(Promise.reject(e));
  }
});
```

Note how we use `async`/`await`, perform the redirection, and (most importantly) still have one central place to pass any error because we used `res.promise()` for error handling.

### Special Case 2: Stream Piping

Like our profile picture route, piping a stream is another situation where we need to manipulate the response object directly.

To handle requests to the URL we’re now redirecting to, let’s add a route that returns some generic picture.

First we should add `profilePic.jpg` in a new `/assets/img` subfolder. (In a real project we would use cloud storage like AWS S3, but the piping mechanism would be the same.)

Let’s pipe this image in response to `/img/profilePic/:id` requests. We need to create a new router for that in `/routes/img.js`:

```
const express = require('express');
const router = express.Router();

const fs = require('fs');
const path = require('path');

router.get('/:id', function(req, res) {
  /* Note that we create a path to the file based on the current working
   * directory, not the router file location.
   */

  const fileStream = fs.createReadStream(
    path.join(process.cwd(), './assets/img/profilePic.png')
  );
  fileStream.pipe(res);
});

module.exports = router;
```

Then we add our new `/img` router in `app.js`:

```
app.use('/users', require('./routes/users'));
app.use('/img', require('./routes/img'));
```

One difference likely stands out compared to the redirect case: We haven’t used `res.promise()` in the `/img` router! This is because the behavior of an already-piped response object being passed an error will be different than if the error occurs in the middle of the stream.

[Express.js developers](https://www.toptal.com/express-js) need to pay attention when working with streams in Express.js applications, handling errors differently depending on when they occur. We need to handle errors before piping (`res.promise()` can help us there) as well as midstream (based on the `.on('error')` handler), but further details are beyond the scope of this article.

### Enhancing `res.promise()`

As with *calling* `res.promise()`, we’re not locked into *implementing* it the way we have either. `promiseMiddleware.js` can be augmented to accept some options in `res.promise()` to allow callers to specify response status codes, content type, or anything else a project might require. It’s up to developers to shape their tools and organize their code so that it best suits their needs.

## Express.js Error Handling Meets Modern Promise-based Coding

The approach presented here allows for **more elegant route handlers** than we started with and a **single point of processing results and errors**—even those fired outside of `res.promise(...)`—thanks to error handling in `app.js`. Still, we are **not forced** to use it and can process edge cases as we want.

The full code from these examples is [available on GitHub](https://github.com/vssenko/express-promises-example). From there, developers can add custom logic as needed to the `handleResponse()` function, such as changing the response status to 204 instead of 200 if no data is available.

However, the added control over errors is much more useful. This approach helped me concisely implement these features in production:

- Format all errors consistently as `{error: {message}}`
- Send a generic message if no status is provided or pass along a given message otherwise
- If the environment is `dev` (or `test`, etc.), populate the `error.stack` field
- Handle database index errors (i.e., some entity with a unique-indexed field already exists) and gracefully respond with meaningful user errors

This Express.js route logic was all in one place, without touching any service—a decoupling that left the code much easier to maintain and extend. This is how simple—but elegant—solutions can drastically improve project structure.

---

### Further Reading on the Toptal Engineering Blog:

- [How to Build a Node.js Error-handling System](https://www.toptal.com/nodejs/node-js-error-handling)
