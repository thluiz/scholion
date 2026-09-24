---
url: "https://dev.to/encore/how-to-make-your-expressjs-apis-9x-faster-with-encorets-1ke2?context=digest"
captured_at: "2026-09-24T23:59:37+01:00"
title: "How to make your Express.js APIs 9x faster with Encore.ts"
domain: "dev-to"
---

Encore.ts is Open Source backend framework for TypeScript. This guide walks you through how to migrate an [Express.js](https://expressjs.com/) app to [Encore.ts](https://encore.dev/) to gain type-safe APIs and 9x performance boost.

## [](#why-migrate-to-encorets)Why migrate to Encore.ts?

Express.js is a great choice for building simple APIs, but as your application grows you will likely run into limitations. There is a large community around Express.js, providing many plugins and middleware to work around these limitations. However, relying heavily on plugins can make it hard to find the right tools for your use case. It also means that you will need to maintain a lot of dependencies.

Encore.ts is an [Open Source](https://github.com/encoredev/encore) framework that aims to make it easier to build robust and type-safe backends with TypeScript. Encore.ts has **0 npm dependencies**, is built with **performance in mind**, and has a lot of **built-in features** for building production ready backends. You can [self-serve](https://encore.dev/docs/how-to/self-host) an Encore.ts app on any hosting service that accepts Docker containers, or use [Encore Cloud Platform](https://encore.dev/use-cases/devops-automation) to fully automate your DevOps and infrastructure.

### [](#performance)Performance

Encore.ts has its own high-performance runtime, with a multi-threaded, asynchronous event loop written in Rust. The Encore Runtime handles all I/O like accepting and processing incoming HTTP requests. This runs as a completely independent event loop that utilizes as many threads as the underlying hardware supports. The result of this is that Encore.ts performs **9x faster** than Express.js.

**Encore.ts handles 9x more requests/sec than Express.js**  
[![encore.ts req per second](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F635n5lw1xmjxgl293w12.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F635n5lw1xmjxgl293w12.png)

**Encore.ts has 80% less response latency than Express.js**  
[![encore.ts latency](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fkvyyvoe6oc1npo822mpb.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fkvyyvoe6oc1npo822mpb.png)

### [](#builtin-benefits)Built-in benefits

When using Encore.ts you get a lot of built-in features without having to install any additional dependencies:

[Type-safe API schemas](https://encore.dev/docs/ts/primitives/apis)

[CORS handling](https://encore.dev/docs/ts/develop/cors)

[Structured logging](https://encore.dev/docs/ts/develop/logging)

[Authentication](https://encore.dev/docs/ts/develop/auth)

[Pub/Sub integrations](https://encore.dev/docs/ts/primitives/pubsub)

[Secrets management](https://encore.dev/docs/ts/primitives/secrets)

[Infrastructure integrations](https://encore.dev/docs/deploy/infra)

[Database integrations](https://encore.dev/docs/ts/primitives/databases)

[Architecture Diagrams](https://encore.dev/docs/observability/encore-flow)

[Local Development Dashboard](https://encore.dev/docs/observability/dev-dash)

[Service Catalog](https://encore.dev/docs/develop/api-docs)

[TypeScript native](https://encore.dev/docs/ts)

[Debugging](https://encore.dev/docs/ts/develop/debug)

[Error handling](https://encore.dev/docs/ts/develop/errors)

[Multithreading](https://encore.dev/blog/event-loops)

[Request validation](https://encore.dev/blog/event-loops)

[Tracing](https://encore.dev/docs/observability/tracing)

[API Client generation](https://encore.dev/docs/develop/client-generation)

[Automatic local infrastructure](https://encore.dev/docs/deploy/infra)

[Automated testing](https://encore.dev/docs/ts/develop/testing)

_Local Development Dashboard_

## [](#migration-guide)Migration guide

Below we've outlined two main strategies you can use to migrate your existing Express.js application to Encore.ts. Pick the strategy that best suits your situation and application.

### [](#forklift-migration-quick-start)Forklift migration (quick start)

When you quickly want to migrate to Encore.ts and don't need all the functionality to begin with, you can use a forklift migration strategy. This approach moves the entire application over to Encore.ts in one shot, by wrapping your existing HTTP router in a catch-all handler.

**Approach benefits**

*   You can get your application up and running with Encore.ts quickly and start moving features over to Encore.ts while the rest of the application is still untouched.
*   You will see a partial performance boost right away because the HTTP layer is now running on the Encore Rust runtime. But to get the full performance benefits, you will need to start using Encore's [API declarations](https://encore.dev/docs/ts/primitives/services-and-apis) and [infrastructure declarations](https://encore.dev/docs/ts#see-how-to-use-each-primitive).

**Approach drawbacks**

*   Because all requests will be proxied through the catch-all handler, you will not be able to get all the benefits from the distributed tracing.
*   The automatically generated architectural diagrams and API documentation will not be able to show you the full picture of your application until you start moving services and APIs over to Encore.ts.
*   You will not be able to use the API Client Generation feature until you start defining APIs in Encore.ts.

**Forklift migration step-by-step**

#### [](#1-install-encore)1\. Install Encore

If this is the first time you're using Encore, you first need to install the CLI that runs the local development environment. Use the appropriate command for your system:

*   **macOS:** `brew install encoredev/tap/encore`
*   **Linux:** `curl -L https://encore.dev/install.sh | bash`
*   **Windows:** `iwr https://encore.dev/install.ps1 | iex`

[Installation docs](https://encore.dev/docs/install)

#### [](#2-add-encorets-to-your-project)2\. Add Encore.ts to your project

```


npm i encore.dev


```

Enter fullscreen mode Exit fullscreen mode

#### [](#3-initialize-an-encore-app)3\. Initialize an Encore app

Inside your project directory, run the following command to create an Encore app:

```


encore app init


```

Enter fullscreen mode Exit fullscreen mode

This will create an `encore.app` file in the root of your project.

#### [](#4-configure-your-tsconfigjson)4\. Configure your tsconfig.json

To the `tsconfig.json` file in the root of your project, add the following:

```


{
   "compilerOptions": {
      "paths": {
         "~encore/*": [
            "./encore.gen/*"
         ]
      }
   }
}


```

Enter fullscreen mode Exit fullscreen mode

When Encore.ts is parsing your code it will specifically look for `~encore/*` imports.

#### [](#5-define-an-encorets-service)5\. Define an Encore.ts service

When running an app using Encore.ts you need at least one [Encore service](https://encore.dev/docs/ts/primitives/services). Apart from that, Encore.ts in not opinionated in how you structure your code, you are free to go with a monolith or microservice approach. Learn more in our [App Structure docs](https://encore.dev/docs/ts/develop/app-structure).

In the root of your App, add a file named `encore.service.ts`. The file must export a service instance, by calling `new Service`, imported from `encore.dev/service`:

```


import {Service} from "encore.dev/service";

export default new Service("my-service");


```

Enter fullscreen mode Exit fullscreen mode

Encore will consider this directory and all its subdirectories as part of the service.

#### [](#6-create-a-catchall-handler-for-your-http-router)6\. Create a catch-all handler for your HTTP router

Now let's mount your existing app router under a [Raw endpoint](https://encore.dev/docs/primitives/services-and-apis#raw-endpoints), which is an Encore API endpoint type that gives you access to the underlying HTTP request.

Here's a basic code example:

```


import { api, RawRequest, RawResponse } from "encore.dev/api";
import express, { request, response } from "express";

Object.setPrototypeOf(request, RawRequest.prototype);
Object.setPrototypeOf(response, RawResponse.prototype);

const app = express();

app.get('/foo', (req: any, res) => {
  res.send('Hello World!')
})

export const expressApp = api.raw(
  { expose: true, method: "*", path: "/!rest" },
  app,
);


```

Enter fullscreen mode Exit fullscreen mode

By mounting your existing app router in this way, it will work as a catch-all handler for all HTTP requests and responses.

#### [](#7-run-you-app-locally)7\. Run you app locally

You will now be able to run your Express.js app locally using the `encore run` command.

#### [](#next-steps-incrementally-move-over-encorets-to-get-all-the-benefits)Next steps: Incrementally move over Encore.ts to get all the benefits

You can now gradually break out specific endpoints using the Encore's [API declarations](https://encore.dev/docs/ts/primitives/apis) and introduce infrastructure declarations for databases and cron jobs etc. This will let Encore.ts understand your application and unlock all Encore.ts features. See the [Feature-by-feature migration](#featurebyfeature-migration) section for more details. You will eventually be able to remove Express.js as a dependency and run your app entirely on Encore.ts.

For more thoughts on migrating an existing backend to Encore.ts, check out our [general migration guide](https://encore.dev/docs/how-to/migrate-to-encore). You can also [join Discord](https://encore.dev/discord) to ask questions and meet fellow Encore developers.

### [](#full-migration)Full migration

This approach aims to fully replace your applications dependency on Express.js with Encore.ts, unlocking all the features and performance of Encore.ts.

In the next section you will find a Feature-by-feature migration guide to help you with the refactoring details.

**Approach benefits**

*   Get all the advantages of Encore.ts, like distributed tracing and architecture diagrams.
*   Get the full performance benefit of Encore.ts - **9x faster** than Express.js.

**Approach drawbacks**

*   This approach may require more time and effort up front compared to the Forklift migration strategy.

## [](#featurebyfeature-migration)Feature-by-feature migration

Check out our [Express.js compared to Encore.ts example](https://github.com/encoredev/examples/tree/main/ts/expressjs-migration) on GitHub for all of the code snippets in this feature comparison.

**APIs**

With Express.js, you create APIs using the `app.get`, `app.post`, `app.put`, `app.delete` functions. These functions take a path and a callback function. You then use the `req` and `res` objects to handle the request and response.

With Encore.ts, you create APIs using the `api` function. This function takes an options object and a callback function. The main difference compared to Express.js is that Encore.ts is type-safe, meaning you define the request and response schemas in the callback function. You then return an object matching the response schema. In case you need to operate at a lower abstraction level, Encore supports defining raw endpoints that let you access the underlying HTTP request. Learn more in our [API Schemas docs](https://encore.dev/docs/ts/develop/api-schemas).

**Express.js**

```


import express, {Request, Response} from "express";

const app: Express = express();

// GET request with dynamic path parameter
app.get("/hello/:name", (req: Request, res: Response) => {
  const msg = `Hello ${req.params.name}!`;
  res.json({message: msg});
})

// GET request with query string parameter
app.get("/hello", (req: Request, res: Response) => {
  const msg = `Hello ${req.query.name}!`;
  res.json({message: msg});
});

// POST request example with JSON body
app.post("/order", (req: Request, res: Response) => {
  const price = req.body.price;
  const orderId = req.body.orderId;
  // Handle order logic
  res.json({message: "Order has been placed"});
});


```

Enter fullscreen mode Exit fullscreen mode

**Encore.ts**

```


import {api, Query} from "encore.dev/api";

// Dynamic path parameter :name
export const dynamicPathParamExample = api(
  {expose: true, method: "GET", path: "/hello/:name"},
  async ({name}: { name: string }): Promise<{ message: string }> => {
    const msg = `Hello ${name}!`;
    return {message: msg};
  },
);

interface RequestParams {
  // Encore will now automatically parse the query string parameter
  name?: Query<string>;
}

// Query string parameter ?name
export const queryStringExample = api(
  {expose: true, method: "GET", path: "/hello"},
  async ({name}: RequestParams): Promise<{ message: string }> => {
    const msg = `Hello ${name}!`;
    return {message: msg};
  },
);

interface OrderRequest {
  price: string;
  orderId: number;
}

// POST request example with JSON body
export const order = api(
  {expose: true, method: "POST", path: "/order"},
  async ({price, orderId}: OrderRequest): Promise<{ message: string }> => {
    // Handle order logic
    console.log(price, orderId)

    return {message: "Order has been placed"};
  },
);

// Raw endpoint
export const myRawEndpoint = api.raw(
  {expose: true, path: "/raw", method: "GET"},
  async (req, resp) => {
    resp.writeHead(200, {"Content-Type": "text/plain"});
    resp.end("Hello, raw world!");
  },
);


```

Enter fullscreen mode Exit fullscreen mode

**Microservices communication**

Express.js does not have built-in support for creating microservices or for service-to-service communication. You will most likely use `fetch` or something equivalent to call another service.

With Encore.ts, calling another service is just like calling a local function, with complete type-safety. Under the hood, Encore.ts will translate this function call into an actual service-to-service HTTP call, resulting in trace data being generated for each call. Learn more in our [Service-to-Service Communication docs](https://encore.dev/docs/ts/develop/app-structure#multi-service-application-distributed-system).

**Express.js**

```


import express, {Request, Response} from "express";

const app: Express = express();

app.get("/save-post", async (req: Request, res: Response) => {
  try {
    // Calling another service using fetch
    const resp = await fetch("https://another-service/posts", {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify({
        title: req.query.title,
        content: req.query.content,
      }),
    });
    res.json(await resp.json());
  } catch (e) {
    res.status(500).json({error: "Could not save post"});
  }
});


```

Enter fullscreen mode Exit fullscreen mode

**Encore.ts**

```


import {api} from "encore.dev/api";
import {anotherService} from "~encore/clients";

export const microserviceCommunication = api(
  {expose: true, method: "GET", path: "/call"},
  async (): Promise<{ message: string }> => {
    // Calling the foo endpoint in anotherService
    const fooResponse = await anotherService.foo();

    const msg = `Data from another service ${fooResponse.data}!`;
    return {message: msg};
  },
);



```

Enter fullscreen mode Exit fullscreen mode

**Authentication**

In Express.js you can create a middleware function that checks if the user is authenticated. You can then use this middleware function in your routes to protect them. You will have to specify the middleware function for each route that requires authentication.

With Encore.ts, when an API is defined with `auth: true`, you must define an authentication handler in your application. The authentication handler is responsible for inspecting incoming requests to determine what user is authenticated.

The authentication handler is defined similarly to API endpoints, using the `authHandler` function imported from `encore.dev/auth`. Like API endpoints, the authentication handler defines what request information it's interested in, in the form of HTTP headers, query strings, or cookies.

If a request has been successfully authenticated, the API Gateway forwards the authentication data to the target endpoint. The endpoint can query the available auth data from the `getAuthData` function, available from the `~encore/auth` module.

Learn more in our [Auth Handler docs](https://encore.dev/docs/ts/develop/auth)

**Express.js**

```


import express, {NextFunction, Request, Response} from "express";

const app: Express = express();

// Auth middleware
function authMiddleware(req: Request, res: Response, next: NextFunction) {
  // TODO: Validate up auth token and verify that this is an authenticated user
  const isInvalidUser = req.headers["authorization"] === undefined;

  if (isInvalidUser) {
    res.status(401).json({error: "invalid request"});
  } else {
    next();
  }
}

// Endpoint that requires auth
app.get("/dashboard", authMiddleware, (_, res: Response) => {
  res.json({message: "Secret dashboard message"});
});


```

Enter fullscreen mode Exit fullscreen mode

**Encore.ts**

```


import { api, APIError, Gateway, Header } from "encore.dev/api";
import { authHandler } from "encore.dev/auth";
import { getAuthData } from "~encore/auth";

interface AuthParams {
  authorization: Header<"Authorization">;
}

// The function passed to authHandler will be called for all incoming API call that requires authentication.
export const myAuthHandler = authHandler(
  async (params: AuthParams): Promise<{ userID: string }> => {
    // TODO: Validate up auth token and verify that this is an authenticated user
    const isInvalidUser = params.authorization === undefined;

    if (isInvalidUser) {
      throw APIError.unauthenticated("Invalid user ID");
    }

    return { userID: "user123" };
  },
);

export const gateway = new Gateway({ authHandler: myAuthHandler });

// Auth endpoint example
export const dashboardEndpoint = api(
  // Setting auth to true will require the user to be authenticated
  { auth: true, method: "GET", path: "/dashboard" },
  async (): Promise<{ message: string; userID: string }> => {
    return {
      message: "Secret dashboard message",
      userID: getAuthData()!.userID,
    };
  },
);


```

Enter fullscreen mode Exit fullscreen mode

**Request validation**

Express.js does not have built-in request validation. You have to use a library like [Zod](https://github.com/colinhacks/zod).

With Encore.ts, request validation for headers, query params and body is. You supply a schema for the request object and in the request payload does not match the schema the API will return a 400 error. Learn more in our [API Schemas docs](https://encore.dev/docs/ts/develop/api-schemas).

**Express.js**

```


import express, {NextFunction, Request, Response} from "express";
import {z, ZodError} from "zod";

const app: Express = express();

// Request validation middleware
function validateData(schemas: {
  body: z.ZodObject<any, any>;
  query: z.ZodObject<any, any>;
  headers: z.ZodObject<any, any>;
}) {
  return (req: Request, res: Response, next: NextFunction) => {
    try {
      // Validate headers
      schemas.headers.parse(req.headers);

      // Validate request body
      schemas.body.parse(req.body);

      // Validate query params
      schemas.query.parse(req.query);

      next();
    } catch (error) {
      if (error instanceof ZodError) {
        const errorMessages = error.errors.map((issue: any) => ({
          message: `${issue.path.join(".")} is ${issue.message}`,
        }));
        res.status(400).json({error: "Invalid data", details: errorMessages});
      } else {
        res.status(500).json({error: "Internal Server Error"});
      }
    }
  };
}

// Request body validation schemas
const bodySchema = z.object({
  someKey: z.string().optional(),
  someOtherKey: z.number().optional(),
  requiredKey: z.array(z.number()),
  nullableKey: z.number().nullable().optional(),
  multipleTypesKey: z.union([z.boolean(), z.number()]).optional(),
  enumKey: z.enum(["John", "Foo"]).optional(),
});

// Query string validation schemas
const queryStringSchema = z.object({
  name: z.string().optional(),
});

// Headers validation schemas
const headersSchema = z.object({
  "x-foo": z.string().optional(),
});

// Request validation example using Zod
app.post(
  "/validate",
  validateData({
    headers: headersSchema,
    body: bodySchema,
    query: queryStringSchema,
  }),
  (_: Request, res: Response) => {
    res.json({message: "Validation succeeded"});
  },
);


```

Enter fullscreen mode Exit fullscreen mode

**Encore.ts**

```


import {api, Header, Query} from "encore.dev/api";

enum EnumType {
  FOO = "foo",
  BAR = "bar",
}

// Encore.ts automatically validates the request schema and returns and error
// if the request does not match the schema.
interface RequestSchema {
  foo: Header<"x-foo">;
  name?: Query<string>;

  someKey?: string;
  someOtherKey?: number;
  requiredKey: number[];
  nullableKey?: number | null;
  multipleTypesKey?: boolean | number;
  enumKey?: EnumType;
}

// Validate a request
export const schema = api(
  {expose: true, method: "POST", path: "/validate"},
  (data: RequestSchema): { message: string } => {
    console.log(data);
    return {message: "Validation succeeded"};
  },
);


```

Enter fullscreen mode Exit fullscreen mode

**Error handling**

In Express.js you either throw an error (which results in a 500 response) or use the `status` function to set the status code of the response.

In Encore.ts throwing an error will result in a 500 response. You can also use the `APIError` class to return specific error codes. Learn more in our [API Errors docs](https://encore.dev/docs/ts/develop/errors).

**Express.js**

```


import express, {Request, Response} from "express";

const app: Express = express();

// Default error handler
app.get("/broken", (req, res) => {
  throw new Error("BROKEN"); // This will result in a 500 error
});

// Returning specific error code
app.get("/get-user", (req: Request, res: Response) => {
  const id = req.query.id || "";
  if (id.length !== 3) {
    res.status(400).json({error: "invalid id format"});
  }
  // TODO: Fetch something from the DB
  res.json({user: "Simon"});
});


```

Enter fullscreen mode Exit fullscreen mode

**Encore.ts**

```


import {api, APIError} from "encore.dev/api"; // Default error handler

// Default error handler
export const broken = api(
  {expose: true, method: "GET", path: "/broken"},
  async (): Promise<void> => {
    throw new Error("This is a broken endpoint"); // This will result in a 500 error
  },
);

// Returning specific error code
export const brokenWithErrorCode = api(
  {expose: true, method: "GET", path: "/broken/:id"},
  async ({id}: { id: string }): Promise<{ user: string }> => {
    if (id.length !== 3) {
      throw APIError.invalidArgument("invalid id format");
    }
    // TODO: Fetch something from the DB
    return {user: "Simon"};
  },
);


```

Enter fullscreen mode Exit fullscreen mode

**Serving static files**

Express.js has a built-in middleware function to serve static files. You can use the `express.static` function to serve files from a specific directory.

Encore.ts also has built-in support for static file serving with the `api.static` method.

The files are served directly from the Encore.ts Rust Runtime. This means that zero JavaScript code is executed to serve the files, freeing up the Node.js runtime to focus on executing business logic. This dramatically speeds up both the static file serving,  
as well as improving the latency of your API endpoints. Learn more in our [Static Assets docs](https://encore.dev/docs/ts/primitives/static-assets)

**Express.js**

```


import express from "express";

const app: Express = express();

app.use("/assets", express.static("assets")); // Serve static files from the assets directory


```

Enter fullscreen mode Exit fullscreen mode

**Encore.ts**

```


import { api } from "encore.dev/api";

export const assets = api.static(
  { expose: true, path: "/assets/*path", dir: "./assets" },
);


```

Enter fullscreen mode Exit fullscreen mode

**Template rendering**

Express.js has a built-in support for rendering templates.

With Encore.ts you can use the `api.raw` function to serve HTML templates, in this example we are using Handlebars.js but you can use whichever templating engine you prefer. Learn more in our [Raw Endpoints docs](https://dev.to/docs/ts/primitives/services-and-apis#raw-endpoints)

**Express.js**

```


import express, {Request, Response} from "express";

const app: Express = express();

app.set("view engine", "pug"); // Set view engine to Pug

// Template engine example. This will render the index.pug file in the views directory
app.get("/html", (_, res) => {
  res.render("index", {title: "Hey", message: "Hello there!"});
});


```

Enter fullscreen mode Exit fullscreen mode

**Encore.ts**

```


import {api} from "encore.dev/api";
import Handlebars from "handlebars";

const html = `
<!doctype html>
<html lang="en">
<head>
  <meta charset="UTF-8"/>
  <link rel="stylesheet" href="/assets/styles.css">
</head>
<body>
<h1>Hello {{name}}!</h1>
</body>
</html>
`;

// Making use of raw endpoints to serve dynamic templates.
// https://encore.dev/docs/ts/primitives/services-and-apis#raw-endpoints
export const serveHTML = api.raw(
  {expose: true, path: "/html", method: "GET"},
  async (req, resp) => {
    const template = Handlebars.compile(html);

    resp.setHeader("Content-Type", "text/html");
    resp.end(template({name: "Simon"}));
  },
);


```

Enter fullscreen mode Exit fullscreen mode

**Testing**

Express.js does not have built-in testing support. You can use libraries like [Vitest](https://vitest.dev/) and  
[Supertest](https://www.npmjs.com/package/supertest).

With Encore.ts you are able to call the API endpoints directly in your tests, just like any other function. You then run the tests using the `encore test` command. Learn more in our [Testing docs](https://encore.dev/docs/ts/develop/testing).

**Express.js**

```


import {describe, expect, test} from "vitest";
import request from "supertest";
import express from "express";
import getRequestExample from "../get-request-example";

/**
 * We need to add the supertest library to make fake HTTP requests to the Express.js app without having to
 * start the server. We also use the vitest library to write tests.
 */
describe("Express App", () => {
  const app = express();
  app.use("/", getRequestExample);

  test("should respond with a greeting message", async () => {
    const response = await request(app).get("/hello/John");
    expect(response.status).to.equal(200);
    expect(response.body).to.have.property("message");
    expect(response.body.message).to.equal("Hello John!");
  });
});


```

Enter fullscreen mode Exit fullscreen mode

**Encore.ts**

```


import {describe, expect, test} from "vitest";
import {dynamicPathParamExample} from "../get-request-example";

// This test suite demonstrates how to test an Encore route.
// Run tests using the `encore test` command.
describe("Encore app", () => {
  test("should respond with a greeting message", async () => {
    // You can call the Encore.ts endpoint directly in your tests,
    // just like any other function.
    const resp = await dynamicPathParamExample({name: "world"});
    expect(resp.message).toBe("Hello world!");
  });
});



```

Enter fullscreen mode Exit fullscreen mode

**Database**

Express.js does not have built-in database support. You can use libraries like [pg-promise](https://www.npmjs.com/package/pg-promise) to connect to a PostgreSQL database but you also have to manage Docker Compose files for different environments.

With Encore.ts, you create a database by importing `encore.dev/storage/sqldb` and calling `new SQLDatabase`, assigning the result to a top-level variable.

Database schemas are defined by creating migration files. Each migration runs in order and expresses the change in the database schema from the previous migration.

Encore.ts automatically provisions databases to match what your application requires. Encore.ts provisions databases in an appropriate way depending on the environment. When running locally, Encore creates a database cluster using Docker. In the cloud, it depends on the environment type:

To query data, use the `.query` or `.queryRow` methods. To insert data, or to make database queries that don't return any rows, use `.exec`.

Learn more in our [Database docs](https://encore.dev/docs/ts/primitives/databases).

**Encore.ts**

_db.ts_

```


import {api} from "encore.dev/api";
import {SQLDatabase} from "encore.dev/storage/sqldb";

// Define a database named 'users', using the database migrations in the "./migrations" folder.
// Encore automatically provisions, migrates, and connects to the database.
export const DB = new SQLDatabase("users", {
  migrations: "./migrations",
});

interface User {
  name: string;
  id: number;
}

// Get one User from DB
export const getUser = api(
  {expose: true, method: "GET", path: "/user/:id"},
  async ({id}: { id: number }): Promise<{ user: User | null }> => {
    const user = await DB.queryRow<User>`
        SELECT name
        FROM users
        WHERE id = ${id}
    `;

    return {user};
  },
);

// Add User from DB
export const addUser = api(
  { expose: true, method: "POST", path: "/user" },
  async ({ name }: { name: string }): Promise<void> => {
    await DB.exec`
        INSERT INTO users (name)
        VALUES (${name})
    `;
    return;
  },
);


```

Enter fullscreen mode Exit fullscreen mode

_migrations/1\_create\_tables.up.sql_

```


CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL UNIQUE
);


```

Enter fullscreen mode Exit fullscreen mode

**Logging**

Express.js does not have built-in support for logging. You can use libraries like [Winston](https://www.npmjs.com/package/winston) to log messages.

Encore.ts offers built-in support for Structured Logging, which combines a free-form log message with structured and type-safe key-value pairs. Logging is integrated with the built-in [Distributed Tracing](https://encore.dev/docs/observability/tracing) functionality, and all logs are automatically included in the active trace. Learn more in our [Logging docs](https://encore.dev/docs/ts/develop/logging).

**Encore.ts**

```


import log from "encore.dev/log";

log.error(err, "something went terribly wrong!");
log.info("log message", { is_subscriber: true });


```

Enter fullscreen mode Exit fullscreen mode

## [](#other-related-articles)Other related articles
