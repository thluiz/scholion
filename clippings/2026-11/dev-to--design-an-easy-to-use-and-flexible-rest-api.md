---
url: "https://dev.to/khalyomede/design-an-easy-to-use-and-flexible-rest-endpoints-3fia"
captured_at: "2026-11-16T00:58:44+00:00"
title: "Design an easy to use and flexible REST API"
domain: "dev-to"
---

If you have already built an application that uses a REST API, and you have been responsible for the back-end interface, you have probably already wondered how to design your URLs, what convention to adopt, and how to keep this API simple to use without making it harder and harder to maintain.

I created this article for folks who are looking for tips to make their REST API fun to use.

On the menu today:

*   [Start from a good database design](#start-from-a-good-database-design)
*   [Example: the todo app](#example-the-todo-app)
*   [How to customize server responses?](#how-to-customize-server-responses)
*   [Conclusion](#conclusion)

## [](#start-from-a-good-database-design)Start from a good database design

If your client-side application has difficulty easily obtaining the data it needs because it requires calling several routes that depend on each other, or these calls don't make much sense, or because these calls are redundant with each other, it's probably an opportunity to think about another way to design your database.

You can follow these advices to help you keep a well designed database:

*   ensure you are not repeating connections between your entites, nor making repetitives circular connections
*   your entites contain only the data related to them, and not related to another dependent entity
*   safely add new dependencies without heavy rework of your existing tables

To help you on the track of a better database schema, [Database normalization](https://en.wikipedia.org/wiki/Database_normalization) is a tool that will help you determine if your database schema is consistent.

[@lorrli274](https://dev.to/lorrli274) made a tremendeous job at explaining the firsts levels of the database normal form principle. Obviously, I have it on my reading list, and you should too 😉

Let's look at an example to apply these principles.

## [](#example-the-todo-app)Example: the Todo app

I find the example of the todo app to be versatile enough to explore the principles we saw earlier. Let's dive into it.

We will see:

*   [1\. The database schema](#1-the-database-schema)
*   [2\. The REST endpoint](#2-the-rest-endpoint)
*   [3\. Designing non-CRUD commands](https://dev.to3-designing-non-crud-commands/)
*   [4\. Should you store timestamps in table?](#4-should-you-store-timestamps-in-table)

### [](#1-the-database-schema)1\. The database schema

To begin, let's summarize the business need.

*   Users
    *   A user can create a user
    *   A user can view the detail of a user, including its assigned tasks
    *   A user can view the list of the users
    *   A user can edit a user
    *   A user can delete a user
*   Tasks
    *   A user can create a task
    *   A task can assign a user to a task
    *   A user can view the detail of a task, including the assigned users
    *   A user can view a list of all the tasks
    *   A user can edit a task
    *   A user can remove a task
    *   A user can unassign a user from a task

I mapped the [CRUD](https://en.wikipedia.org/wiki/Create,_read,_update_and_delete) concept to our todo app.

From these statements, we can create our database in the following way.

[![Alt Text](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Ftqgix42uxq7oc2ye02j1.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Ftqgix42uxq7oc2ye02j1.png)

To help you create a maintainable database schema, you can imagine the table columns as a way to qualify the entity they represent.

If you find yourself adding columns that do not represent your entity, it means that this is not the right place to add these columns.

### [](#2-the-rest-endpoint)2\. The REST endpoint

The [REST protocol](https://en.wikipedia.org/wiki/Representational_state_transfer) will help us create URLs that accurately represent our entities. Here is an example of an implementation from our database.

*   Users
    *   **GET** `/api/user` Get the list of all users
    *   **GET** `/api/user/{id}` Get the detail of a user
    *   **GET** `/api/user/{id}/task` Get the list of all the task assigned to this user
    *   **POST** `/api/user` Create a new user
    *   **PUT** `/api/user/{id}` Update a user
    *   **DELETE** `/api/user/{id}` Delete a user
*   Tasks
    *   **GET** `/api/task` Get the list of all tasks
    *   **GET** `/api/task/{id}` Get the detail of the task
    *   **GET** `/api/task/{id}/user` Get the list of all the users assigned to this task
    *   **POST** `/api/task` Create a new task
    *   **POST** `/api/task/{id}/user/{id}` Attach an existing user to the task
    *   **PUT** `/api/task/{id}` Update a task
    *   **DELETE** `/api/task/{id}` Delete a task
    *   **DELETE** `/api/task/{id}/user/{id}` Dettach an existing user from the task

Because our schema is "atomic" (the columns of the tables are relevant), you can see that our REST endpoints make sense.

From these URLs, you can imagine your UI, such as being able to present a list of users to the user (GET `/api/user`), so that he/she can choose to which user(s) to assign this task (POST `/api/task/{id}/user/{id}`).

One note, some folks would be tempted to design the API in such way that we could get the assigned users to a task simply via the `/api/task/{id}`. I think this is not a safe way to design your REST API for these reasons:

*   As soon as you want to filter on the data returned by your server, you will be forced to use a syntax that will differentiate the fields of your entities (for example, you want to retrieve only the id of your tasks and your users, you will write something similar to `/api/task/{id}?select=task.id,task.user.id`), which will make the task of parsing your server-side query strings more complicated
*   As a general rule, you should not retrieve 1-N relationships in the route that returns the detail of your entity (`/api/user/{id}`, `/api/task/{id}`), because the user of your web application may not need this information, so don't waste bandwidth and CPU time for nothing, the best thing is to propose a button to access this information in your user interface

### [](#3-designing-noncrud-commands)3\. Designing non-CRUD commands

The most common pattern I know that comes out of the CRUD concept is trashing/untrashing users. This is not a deletion because the data still exists in the database, so these actions will not be correct if they are processed via the DELETE protocol. Nevertheless, it can be seen as a suppression because it prevents to see the trashed entities, and it will be necessary to obtain them via a special route (`/api/user?filter=active eq false`).

To avoid this problem, let's update our database schema.

[![Alt Text](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F9iqh248uuzi9tcct0jac.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F9iqh248uuzi9tcct0jac.png)

From now on, when you want to put a user in the trash, you can use the PUT method and pass the active column to false.

```


PUT /api/user/{id} HTTP 2.0
Host: example.com
Content-Type: application/json
Content-Length: 21

{
  "active": false
}


```

Enter fullscreen mode Exit fullscreen mode

Another thing, don't let your user be able to trash an entity from the edit form. This action is more important than a simple modification, place it in a separate and dedicated place, such as when clicking a button for example.

### [](#4-should-your-store-timestamps-in-table)4\. Should your store timestamps in table?

Many frameworks provide shortcuts to create fields that allow you to know when an entity was created and modified.

For example, in Laravel, you might have probably used this in the migration.

```


Schema::create("task", function(Blueprint $table) {
  $table->increments("id");
  $table->string("title");
  $table->string("description");
  $table->timestamps(); // <---
});


```

Enter fullscreen mode Exit fullscreen mode

This will create the table, its columns, and add 2 additional columns: `created_at` and `updated_at`.

Here we have 2 problems:

*   If we want to know who created this task, we will need to add a junky "created\_by" column, and this is breaking the atomicity of your table
*   If I edit 4 times this task, who will know the edit history (except your cat)?

For all these reasons, I like to keep thinking in an atomic way. If you need to trace who creates, modifies, and deletes your entities, this means that you need to model this need as a separate table.

[![Alt Text](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fsyntvrdhbtqacsqspu2h.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fsyntvrdhbtqacsqspu2h.png)

By modeling your history in this way, you will allow your users to browse the list of changes to the selected entity on demand. The associated REST endpoint would be a GET `/api/task/{id}/history`, which makes sense.

Some people may argue that it is useless to add a `history_type` table since we know that we are working with a finite list: "creation", "edition", "deletion".

Unfortunately, if you decide to leave an enumerable type in your table, you will also have to copy these values into your client-side application, since you will not have a way to retrieve them from your database.

If you need to display them to the user so that he can see only the "deletion" type changes, for example, the code duplication will make your application less maintainable (if you change "deletion" to "delete", will you be happy to make the change in two different places?).

BEFORE `/api/task/{id}/history?filter=historyType eq delete`  
AFTER `/api/task/{id}/history?filter=historyTypeId eq 3`

GET `/api/history-type`

```


[
  {"id": 1, "name": "creation"},
  {"id": 2, "name": "edition"},
  {"id": 3, "name": "deletion"}
]


```

Enter fullscreen mode Exit fullscreen mode

```


<option id="1">creation</option>
<option id="2">edition</option>
<option id="3">deletion</option>


```

Enter fullscreen mode Exit fullscreen mode

As you can see, I introduced a bizarre way of filtering data coming from the GET endpoint we saw earlier, using this `?filter=...` syntax. I took inspiration from the [OData v4 - URL convention](http://docs.oasis-open.org/odata/odata/v4.01/odata-v4.01-part2-url-conventions.html), and this will be the perfect transition for the last part of this article.

## [](#how-to-customize-server-responses)How to customize server responses?

I think the greatest added value to GraphQL is the ability to request the server in such a flexible way that you can surgically target the columns and the relations to be retrieved.

If you have the opportunity, just check out this wonderful concept, it's worth it: [Introduction to GraphQL](https://graphql.org/learn/).

In the mean time, back to the REST world there is this issue that GraphQL elegantly solved: to be able to customize the server response.

Imagine you are developing the tasks list view in your web app. You want to provide a mouse hover effect which will allow the user to have a preview of the first 50 characters of the description. Cool!

On the other side, the Android team is building the same app, but as this is targeting the mobile users, they choose to only display the tasks names, without any click-tooltip effect.

Both team will need to query the server for the `/api/task` endpoint response (via GET). Only the Android team will have a performance issue because they get the description of each tasks, for nothing.

### [](#odata-v4-protocol)OData v4 protocol

At the office, I used the [Microsoft Graph API](https://docs.microsoft.com/fr-fr/graph/api/overview?view=graph-rest-1.0) to connect our users to their Outlook accounts so that they can view their emails without leaving our web application.

I like this API because it offers a flexible way to retrieve emails and their related data, using the OData protocol. For example, you can fetch a particular email by its id:

```


GET https://graph.microsoft.com/v1.0/me/messages/AAMkADhMGAAA=


```

Enter fullscreen mode Exit fullscreen mode

And you can customize the fields you retrieve:

```


GET https://graph.microsoft.com/v1.0/me/messages/AAMkADhAAAW-VPeAAA=/?$select=internetMessageHeaders


```

Enter fullscreen mode Exit fullscreen mode

OData protocol adds useful helpers (see the documentation) to manipulate the data processed by your REST endpoints.

To be able to respond to client requests that requires to customize the server response using this protocol, you should add a logic layer right before returning results. Fortunately, tools have been made by awesome open sourcers to let us get started quickly, like [odata-parser](https://www.npmjs.com/package/odata-parser) for NodeJS.

The protocol, IMHO, is a bit hard to digest as it is. This part of this article is open for any suggestion on how to smoothly integrate the protocol within existing frameworks.

## [](#conclusion)Conclusion

I think building REST APIs is pretty exciting. I really appreciate any well designed API, because it quickly becomes a true asset when I try to add it to any of my web app.

The opportunity to filter and customize server responses can be a game changer when you deal with complex tables, because you can save some precious bytes and parsing time client side.

OData offers a beautiful way to tackle this problem, if you can tame this technology. Give me your point of view regarding this protocol, and tell me if you use it or a similar pattern to deal with server side response management.

That's all folks, I hope you learned something, I took a real pleasure to write on Dev.to as always, so stay tuned for future articles, and in the meantime, take care of yourself!

Happy optimization!

_All the diagrams you have seen have been made by the free [Draw.io](https://www.draw.io/) web app._

_Cover photo by [Lorenzo Cafaro](https://pixabay.com/fr/users/3844328-3844328/?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=1857175) from [Pixabay](https://pixabay.com/fr/?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=1857175)._
