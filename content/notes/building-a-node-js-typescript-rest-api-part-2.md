---
title: "Building a Node.js/TypeScript REST API, Part 2: Models, Middleware, and Services"
date: '2021-01-28T12:41:09-03:00'
category: webclip
summary: 'The article organizes a users REST API into DTOs, DAOs, services, controllers, and middleware, using an in-memory store to show CRUD flow, validation, and route composition.'
tags: ["nodejs", "typescript", "rest-api", "middleware"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Express.js/TypeScript REST API, Part 2: Architecture | Toptal"
    url: "https://www.toptal.com/express-js/nodejs-typescript-rest-api-pt-2?utm_campaign=Toptal%20Engineering%20Blog&utm_medium=email&_hsmi=108339818&_hsenc=p2ANqtz-94s7zl7MzSzUxfgu-UNvrtYXd2YREcmy8-TEILqcDJKB4WnhgpB1SZ-8xJJp5BPvXSdr1GlPT24pPFaki_dwKDOt5jzA&utm_content=108339818&utm_source=hs_email"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2021-01/toptal-com--building-a-node-js-typescript-rest-api-part-2.md"
    kind: repo
---

The article splits the users API into layers. DTOs describe the user shape, the DAO stores users in an in-memory array, the service wraps CRUD calls, controllers handle requests, and middleware runs validation before requests reach the controller.

## Reading notes

- The series continues from Part 1 and assumes the project structure and tooling are already in place.
- The API is organized around services, middleware, controllers, and models.
- The example uses a temporary in-memory database that stores users in an array and supports basic CRUD only.
- The article introduces DAO and DTO as separate concepts.
- A DAO performs CRUD operations against a database.
- A DTO carries raw data that matches the data model.
- DTOs help TypeScript objects conform to the model structure.
- TypeScript does not perform runtime validation of incoming user input.
- User input may contain extra fields, miss required fields, or use the wrong types.
- Packages such as ajv can help with runtime validation.
- The example user DTO requires id, email, and password, with firstName, lastName, and permissionLevel optional.
- The DAO is implemented as a singleton so every import shares the same users array.
- shortid is used to generate user IDs.
- The DAO includes create, read, update, patch, delete, and get-by-email operations.
- putUserById can accept values outside the DTO-defined model because TypeScript does not validate at runtime.
- patchUserById updates only selected fields and depends on a separate allowlist.
- The service layer implements a CRUD interface and delegates work to the DAO.
- The service also follows the singleton pattern.
- The controller hashes passwords with argon2 before storing them.
- Controller methods list users, fetch one user, create a user, patch a user, update a user, and delete a user.
- Middleware validates required fields, checks whether an email already exists, prevents changing the email after creation, checks that a user exists, and copies userId from the route into the request body.
- Routes combine middleware and controller functions.
- The .all() handler on /users/:userId runs the existence check before GET, PUT, PATCH, and DELETE handlers.
- POST and PUT share the required-fields validation.
- The article says the example only covers basic validations and assumes users cannot change their email.
- Testing is shown with curl requests.
- A GET on /users initially returns an empty array.
- A POST without required fields returns a middleware error.
- A valid POST returns a generated user id.
- PUT updates the full resource, while PATCH updates only part of it.
- The example response shows the password stored as an argon2 hash.
- DELETE removes the user, and the list becomes empty again.
- The article closes by saying the next part will replace the in-memory database with MongoDB and Mongoose, add JWT security, and configure automated testing.
