---
url: "https://toptal.com/nodejs/smart-node-js-form-validation"
captured_at: "2026-11-16T06:18:50+00:00"
title: "Node.js Form Validation Using Datalize | Toptal®"
domain: "toptal-com"
---

BACK-END
8-MINUTE READ
Smart Node.js Form Validation

Bulletproof data validation is fundamental to implementing a back-end API. Find out how datalize, a Node.js library, makes this easy—and formats your data nicely, too.

authors are vetted experts in their fields and write on topics in which they have demonstrated experience. All of our content is peer reviewed and validated by Toptal experts in the same field.

By
Andrej Adamcik

Verified Expert
in Engineering
11 Years of Experience

Andrej is an award-winning full-stack developer with experience on projects for global brands such as Spotify, Gartner, Comcast, or Fantasy.

EXPERTISE

Node.js
API
Back-end Developers

One of the fundamental tasks to perform in an API is data validation. In this article, I’d like to show you how to add bulletproof validation for your data in a way that also returns it nicely formatted.

Doing custom data validation in Node.js is neither easy nor quick. There’s a lot of functionality you need to write in order to cover any kind of data. While I’ve tried a few Node.js form data libraries—for both Express and Koa—they’ve never fulfilled the needs of my projects. There were problems with extending libraries and the libraries not working with complex data structures or asynchronous validation.

Form Validation in Node.js with Datalize

That’s why I eventually decided to write my own tiny-but-powerful form validation library called datalize. It’s extendable, so you can use it in any project and customize it to your requirements. It validates a request’s body, query, or params. It also supports async filters and complex JSON structures like arrays or nested objects.

Setup

Datalize can be installed via npm:

npm install --save datalize

To parse a request’s body, you should use a separate library. If you don’t already use one, I recommend koa-body for Koa or body-parser for Express.

You can apply this tutorial to your already-set-up HTTP API server, or use the following simple Koa HTTP server code.

const Koa = require('koa');
const bodyParser = require('koa-body');

const app = new Koa();
const router = new (require('koa-router'))();

// helper for returning errors in routes
app.context.error = function(code, obj) {
this.status = code;
this.body = obj;
};

// add koa-body middleware to parse JSON and form-data body
app.use(bodyParser({
enableTypes: ['json', 'form'],
multipart: true,
formidable: {
maxFileSize: 32 * 1024 * 1024,
}
}));

// Routes...

// connect defined routes as middleware to Koa
app.use(router.routes());
// our app will listen on port 3000
app.listen(3000);

console.log('🌍 API listening on 3000');

However, this is not a production setup (you should use logging, enforce authorization, handle errors, etc.), but these few lines of code will work just fine for the examples I’ll show you.

Note: All code examples use Koa, but the data validation code will work for Express as well. The datalize library also has an example for implementing Express form validation.

A Basic Node.js Form Validation Example

Let’s say you have a Koa or Express web server and an endpoint in your API that creates a user with several fields in the database. Some fields are required, and some can only have specific values or must be formatted to correct type.

You could write simple logic like this:

/**
* @api {post} / Create a user
* ...
*/
router.post('/', (ctx) => {
const data = ctx.request.body;
const errors = {};

if (!String(data.name).trim()) {
errors.name = ['Name is required'];
}

if (!(/^[\-0-9a-zA-Z\.\+_]+@[\-0-9a-zA-Z\.\+_]+\.[a-zA-Z]{2,}$/).test(String(data.email))) {
errors.email = ['Email is not valid.'];
}

if (Object.keys(errors).length) {
return ctx.error(400, {errors});
}

const user = await User.create({
name: data.name,
email: data.email,
});

ctx.body = user.toJSON();
});

Now let’s rewrite this code and validate this request using datalize:

const datalize = require('datalize');
const field = datalize.field;

/**
* @api {post} / Create a user
* ...
*/
router.post('/', datalize([
field('name').trim().required(),
field('email').required().email(),
]), (ctx) => {
if (!ctx.form.isValid) {
return ctx.error(400, {errors: ctx.form.errors});
}

const user = await User.create(ctx.form);

ctx.body = user.toJSON();
});

Shorter, cleaner, so easy to read. With datalize, you can specify a list of fields and chain to them as many rules (functions that throw an error if the input is invalid) or filters (functions that format the input) as you want.

The rules and filters are executed in the same order as they’re defined, so if you want to trim a string for whitespace first and then check if it has any value, you have to define .trim() before .required().

Datalize will then create an object (available as .form in the wider context object) with just the fields you have specified, so you don’t have to list them again. The .form.isValid property tells you whether validation was successful or not.

Automatic Error Handling

If we don’t want to check whether the form is valid or not with every request, we can add a global middleware which cancels the request if the data didn’t pass validation.

To do this we just add this piece of code to our bootstrap file where we create our Koa/Express app instance.

const datalize = require('datalize');

// set datalize to throw an error if validation fails
datalize.set('autoValidate', true);

// only Koa
// add to very beginning of Koa middleware chain
app.use(async (ctx, next) => {
try {
await next();
} catch (err) {
if (err instanceof datalize.Error) {
ctx.status = 400;
ctx.body = err.toJSON();
} else {
ctx.status = 500;
ctx.body = 'Internal server error';
}
}
});

// only Express
// add to very end of Express middleware chain
app.use(function(err, req, res, next) {
if (err instanceof datalize.Error) {
res.status(400).send(err.toJSON());
} else {
res.send(500).send('Internal server error');
}
});

And we don’t have to check if data is valid anymore, as datalize will do it for us. If the data is invalid, it will return a formatted error message with a list of invalid fields.

Query Validation

Yes, you can even validate your query parameters very easily—it doesn’t have to be used with POST requests only. We just use the .query() helper method, and the only difference is that the data is stored in the .data object instead of .form.

const datalize = require('datalize');
const field = datalize.field;

/**
* @api {get} / List users
* ...
*/
router.post('/', datalize.query([
field('keywords').trim(),
field('page').default(1).number(),
field('perPage').required().select([10, 30, 50]),
]), (ctx) => {
const limit = ctx.data.perPage;
const where = {
};

if (ctx.data.keywords) {
where.name = {[Op.like]: ctx.data.keywords + '%'};
}

const users = await User.findAll({
where,
limit,
offset: (ctx.data.page - 1) * limit,
});

ctx.body = users;
});

There is also a helper method for parameter validation, .params(). Query and form data can be validated together by passing two datalize middlewares in the router’s .post() method.

More Filters, Arrays, and Nested Objects

So far we’ve used really simple data in our Node.js form validation. Now let’s try some more complex fields like arrays, nested objects, etc.:

const datalize = require('datalize');
const field = datalize.field;
const DOMAIN_ERROR = "Email's domain does not have a valid MX (mail) entry in its DNS record";

/**
* @api {post} / Create a user
* ...
*/
router.post('/', datalize([
field('name').trim().required(),
field('email').required().email().custom((value) => {
return new Promise((resolve, reject) => {
dns.resolve(value.split('@')[1], 'MX', function(err, addresses) {
if (err || !addresses || !addresses.length) {
return reject(new Error(DOMAIN_ERROR));
}

resolve();
});
});
}),
field('type').required().select(['admin', 'user']),
field('languages').array().container([
field('id').required().id(),
field('level').required().select(['beginner', 'intermediate', 'advanced'])
]),
field('groups').array().id(),
]), async (ctx) => {
const {languages, groups} = ctx.form;
delete ctx.form.languages;
delete ctx.form.groups;

const user = await User.create(ctx.form);

await UserGroup.bulkCreate(groups.map(groupId => ({
groupId,
userId: user.id,
})));

await UserLanguage.bulkCreate(languages.map(item => ({
languageId: item.id,
userId: user.id,
level: item.level,
));
});

If there is no built-in rule for data we need to validate, we can create a custom data validation rule with the .custom() method (great name, right?) and write the necessary logic there. For nested objects, there is the .container() method in which you can specify a list of fields the same way as in the datalize() function. You can nest containers within containers or supplement them with .array() filters, which converts values to arrays. When the .array() filter is used without a container, the specified rules or filters are applied to every value in the array.

So .array().select(['read', 'write']) would check if every value in the array is either 'read' or 'write' and if any are not, it will return a list of all indexes with errors. Pretty cool, huh?

PUT/PATCH

When it comes to updating your data with PUT/PATCH (or POST), you don’t have to rewrite all your logic, rules, and filters. You just add an extra filter like .optional() or .patch(), which will remove any field from the context object if it was not defined in the request. (.optional() will make it always optional, whereas .patch() will make it optional only if the HTTP request’s method is PATCH.) You can add this extra filter so it works for both creating and updating data in your database.

const datalize = require('datalize');
const field = datalize.field;

const userValidator = datalize([
field('name').patch().trim().required(),
field('email').patch().required().email(),
field('type').patch().required().select(['admin', 'user']),
]);

const userEditMiddleware = async (ctx, next) => {
const user = await User.findByPk(ctx.params.id);

// cancel request here if user was not found
if (!user) {
throw new Error('User was not found.');
}

// store user instance in the request so we can use it later
ctx.user = user;

return next();
};

/**
* @api {post} / Create a user
* ...
*/
router.post('/', userValidator, async (ctx) => {
const user = await User.create(ctx.form);

ctx.body = user.toJSON();
});

/**
* @api {put} / Update a user
* ...
*/
router.put('/:id', userEditMiddleware, userValidator, async (ctx) => {
await ctx.user.update(ctx.form);

ctx.body = ctx.user.toJSON();
});

/**
* @api {patch} / Patch a user
* ...
*/
router.patch('/:id', userEditMiddleware, userValidator, async (ctx) => {
if (!Object.keys(ctx.form).length) {
return ctx.error(400, {message: 'Nothing to update.'});
}

await ctx.user.update(ctx.form);

ctx.body = ctx.user.toJSON();
});

With two simple middlewares, we can write most logic for all POST/PUT/PATCH methods. The userEditMiddleware() function verifies if the record that we want to edit exists and throws an error otherwise. Then userValidator() does the validation for all endpoints. Finally, the .patch() filter will remove any field from the .form object if it’s not defined and if the request’s method is PATCH.

Node.js Form Validation Extras

In custom filters, you can get values of other fields and perform validation based on that. You can also get any data from the context object, like request or user information, as it’s all provided in custom function callback parameters.

The library covers a basic set of rules and filters, but you can register custom global filters that you can use with any fields, so you don’t have to write the same code over and over:

const datalize = require('datalize');
const Field = datalize.Field;

Field.prototype.date = function(format = 'YYYY-MM-DD') {
return this.add(function(value) {
const date = value ? moment(value, format) : null;

if (!date || !date.isValid()) {
throw new Error('%s is not a valid date.');
}

return date.format(format);
});
};

Field.prototype.dateTime = function(format = 'YYYY-MM-DD HH:mm') {
return this.date(format);
};

With these two custom filters you can chain your fields with .date() or .dateTime() filters to validate date input.

Files can also be validated using datalize: There are special filters just for files like .file(), .mime(), and .size() so you don’t have to handle files separately.

Start Writing Better APIs Now

I’ve been using datalize for Node.js form validation in several production projects already, for both small and large APIs. It’s helped me to deliver great projects on time and with less stress while making them more readable and maintainable. On one project I’ve even used it to validate data for WebSocket messages by writing a simple wrapper around Socket.IO and the usage was pretty much the same as defining routes in Koa, so that was nice. If there is enough interest, I might write a tutorial for that as well.

I hope this tutorial will help you and I build better APIs in Node.js, with perfectly validated data without security issues or internal server errors. And most importantly, I hope it will save you a ton of time that you would otherwise have to invest in writing extra functions for form validation using JavaScript.

UNDERSTANDING THE BASICS
Is Node.js "front end" or "back end"?

Node.js a back-end platform. As its name implies, Node.js apps are written in JavaScript (JS) or any language that can compile or transpile to it.

What is Node.js not good for?

CPU-heavy computation does not work well with Node.js, because that would block its event loop.

What do you mean by form validation?

A user can send any kind of data to the back end—maybe it’s not validated on the front end, or maybe it’s submitted directly via your API. This data is received mostly in plain text or in a binary format on the back end and must be parsed and validated to prevent errors caused by incorrect/malicious user input.

What is the difference between Express and Node.js?

Express is a web framework used on top of Node.js, while Node.js is a server environment for running JavaScript on the back end.

What do you use Node.js for?

Node.js has many use cases, but it’s best used for real-time apps (e.g. chat, data streaming, collaborative services), server-side-rendered web apps, CLIs, and APIs.

Why is form validation required?

In order to ensure that the format and type of input data are correct, that data only contains allowed values, etc., it must be validated. Otherwise, you may run into issues when inserting it into a database. Validation also prevents security leaks caused by malicious user data.
