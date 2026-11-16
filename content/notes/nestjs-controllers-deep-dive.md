---
title: "NestJS Controllers Deep Dive"
date: '2026-11-16T01:53:33+00:00'
category: webclip
summary: 'The post explains what controllers do in NestJS, how HTTP verbs map to controller methods, how to return responses, use route params, async actions, and register controllers in a module.'
tags: ["nestjs", "controllers", "http-verbs", "routing"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "NestJS Controllers Deep Dive"
    url: "https://dev.to/santoshyadav198613/nestjs-controllers-deep-dive-30fk"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/dev-to--nestjs-controllers-deep-dive.md"
    kind: repo
---

The post presents controllers as the core part of a NestJS app for handling requests. It shows how each HTTP verb maps to a method, how status codes differ for POST and other methods, and how a controller can return JSON, text, files, or XML. It also covers how to create a controller with Nest CLI and how controllers are registered in a module.

## Reading notes

- Controllers handle requests sent to the server and expose multiple endpoints.
- Each endpoint is identified by an HTTP method.
- GET is used to read data and can accept params for filtering.
- POST is used to create records and can also be used for filtering with data sent in the request.
- PUT updates records and expects the sent data to replace what is in the database.
- PATCH modifies only part of the data.
- DELETE removes records from the server.
- POST returns status code 201 on success, while other methods return 200.
- A controller can return a list of products from a class property.
- The `@Controller` decorator sets the base route for the controller.
- Nest CLI can generate a controller and create a controller file plus a spec file.
- The `@Get` decorator maps a GET request to a method.
- The `@Post` decorator maps a POST request to a method.
- The `@Req` decorator gives access to the request object, including body and headers.
- PUT, PATCH, and DELETE have corresponding decorators.
- `@Res()` lets a method override the response body or status code.
- `@HttpCode()` sets a custom status code.
- `@Header()` adds custom response headers.
- Route names can be set explicitly, and dynamic routes can use `:id`.
- `@Param` gives access to values from a dynamic route.
- Controller methods can be async and return a Promise or an Observable.
- Controllers must be registered in NestJS modules.
