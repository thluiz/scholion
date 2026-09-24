---
url: "https://dev.to/emanuelgustafzon/dependency-injection-made-simple-3d4c?ref=dailydev"
captured_at: "2026-09-24T23:58:50+01:00"
title: "Dependency Injection made simple."
domain: "dev-to"
---

Dependency Injection is an intimitating word. But actually the concept is quite simple.

Dependency Injection is a way of handling `objects` that are `dependent` on `other objects`

We will make an implementation in `JavaScript` and then in `C# with interfaces.`

Let’s start with a simple example of an object being dependent of another object.  

```
class DatabaseConnection {
  connect() {
    console.log("Connected to database");
  }
}

class PostsRouter {
  get() {
    const db = new DatabaseConnection();
    db.connect();
    console.log("Posts retrieved");
  }
}
const posts = new PostsRouter;
posts.get();
```

Enter fullscreen mode Exit fullscreen mode

In the example above the posts router is dependent on the database connection.

BUT there is a problem here. Even though this solution works, it’s not flexible. The code is, as we say tightly coupled.

What if you have two different database connections? One for SQLite and one for MySQL? To change the connection object you need to change the code in the posts route.

That’s when dependency injection comes in.

Dependency injection is basically nothing more than `passing an object` into the `constructor` or `setter` of a `class` that depends on that object.

Let’s try that!  

```
class SQLiteConnection {
  connect() {
    console.log("Connected to SQlite");
  }
}

class MySqlConnection {
  connect() {
    console.log("Connected to MySQL");
  }
}

class PostsRouter {
  constructor(connection) {
    this.connection = connection;
  }
  get() {
    this.connection.connect();
    console.log("Posts retrieved");
  }
}

const mySql = new MySqlConnection;
const sqlite = new SQLiteConnection;

const mysqlPosts = new PostsRouter(mySql);

const sqlitePosts = new PostsRouter(sqlite);

mysqlPosts.get();
sqlitePosts.get();
```

Enter fullscreen mode Exit fullscreen mode

You see! This makes the code more flexible. The connection object is decoupled from the posts object. You can pass any object to the constructor.

## [](#benefits)Benefits

*   The code is decoupled and easier to manage.
*   The code is easier to test. You can create a mock object and pass it to the post router.

## [](#interfaces)Interfaces

You might have noticed that our implementation worked fine in JavaScript because we don’t need to think about types.

But many times we work with strongly typed languages like TypeScript, C# and Java.

So the issue is when we send the connection object into the posts object we need to define a type.

That’s why we need interfaces. Interfaces is like classes but there is no implementation of methods or properties it’s just the types.

Let’s implement an interface for the connection objects.  

```
interface IDb {
  public void connect();
}
```

Enter fullscreen mode Exit fullscreen mode

This is the structure of the connection object. It has a public method called connect and it returns void and has no parameters.

Now the connection classes can inherit from IDb to enforce the same structure.  

```

class SQLiteConnection : IDb {
  public void connect() {
    Console.WriteLine("Connected to SQlite");
  }
}

class MySqlConnection : IDb {
  public void connect() {
    Console.WriteLine("Connected to MySQL");
  }
}
```

Enter fullscreen mode Exit fullscreen mode

It’s worth noticing, that a class can inherit multiple interfaces in most languages.

Now we can pass the connection objects in the constructor of the posts route object using IDb as the type.  

```

class PostsRouter {
  IDb _connection;

  public PostsRouter(IDb connection) {
    this._connection = connection;
  }
  public void get() {
    this._connection.connect();
    Console.WriteLine("Posts retrieved");
  }
}
```

Enter fullscreen mode Exit fullscreen mode

I hope this explanation made sense to you!

Here is the full example.  

```

using System;

interface IDb {
  public void connect();
}

class SQLiteConnection : IDb {
  public void connect() {
    Console.WriteLine("Connected to SQlite");
  }
}

class MySqlConnection : IDb {
  public void connect() {
    Console.WriteLine("Connected to MySQL");
  }
}

class PostsRouter {
  IDb _connection;

  public PostsRouter(IDb connection) {
    this._connection = connection;
  }
  public void get() {
    this._connection.connect();
    Console.WriteLine("Posts retrieved");
  }
}

class Program {
  public static void Main (string[] args) {
    IDb sqlConnection = new SQLiteConnection();
    IDb mySqlConnection = new MySqlConnection();

    PostsRouter posts = new PostsRouter(sqlConnection);
    PostsRouter posts2 = new PostsRouter(mySqlConnection);
    posts.get();
    posts2.get();
  }
}
```

Enter fullscreen mode Exit fullscreen mode

[![Google AI Education track image](https://media2.dev.to/dynamic/image/width=775%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fu09y9fffqrb2one15j3g.png)](https://dev.to/deved/build-apps-with-google-ai-studio?bb=238781)

## [](#build-apps-with-google-ai-studio)[Build Apps with Google AI Studio 🧱](https://dev.to/deved/build-apps-with-google-ai-studio?bb=238781)

This track will guide you through Google AI Studio's new "Build apps with Gemini" feature, where you can turn a simple text prompt into a fully functional, deployed web application in minutes.

[Read more →](https://dev.to/deved/build-apps-with-google-ai-studio?bb=238781)
