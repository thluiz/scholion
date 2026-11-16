---
url: "https://dev.to/thakursachin467/how-to-get-started-with-a-graph-ql-react-apollo-client-and-apollo-server-app-2l7b"
captured_at: "2026-11-16T19:34:35+00:00"
title: "How to Get Started With a Graph QL, React, Apollo Client, and Apollo Server App"
domain: "dev-to"
---

This is a two-part series. In part one we will learn what graphql is and what are some of its advantages and build a backend using graphql. In part two we will learn to integrate our graphql backed to our react frontend service using Apollo Client. This series was originally posted on my personal blog. You can find link to both parts below

1.  [How to Get Started With a Graph QL, React, Apollo Client, and Apollo Server App](https://bitoverflow.net/How-to-Get-Started-With-a-Graph-QL-React-Apollo-Client-and-Apollo-Server-App)
2.  [How to Get Started With a Graph QL, React, Apollo Client, and Apollo Server App- Part 2](https://bitoverflow.net/How-to-Get-Started-With-a-Graph-QL-React-Apollo-Client-and-Apollo-Server-App-Part-2)

* * *

Graphql has been around for quite some time now and we often think that graphql is some complex thing but in reality, all graphql is a specification of how the data will be exchanged between the server and the client over the HTTP. It’s essentially a query language for your API’s and defined what data can be fetched from the server. Now, this is unlike anything you might have used in terms of a standard API, where you have a specific endpoint for fetching specific data. Like in the case of a medium API, we might have an API called `/api/allarticles/:userId` which returns us all articles for a specific user. Now this was of building API is known as REST API’s and we have been building APIs using this technique for quite some time now and before that, we had SOAP in which we use to have XML data structure. Now, what makes graphql different if how it improves upon the ideas of REST. In case of rest, where we hit a URL and get some data back in case of graphql we can specifically ask for what we are looking for and fetch only a specific subset whatever we want to build a specific page.

### [](#getting-started)Getting Started

Now, after this small introduction let dive right into some demo. In this demo, we will be focusing on building a small react application using Apollo Client a graphql client library that is available for all major front end javascript framework and Apollo server for building our backend. Now all code for this tutorial will be available [on Github](https://github.com/thakursachin467/graphql-starter). So, let’s get right into building a simple application.

Now, this demo will be focused on building a simple application to get started with Apollo client on the front end with ReactJs and Apollo server for building a lightweight graphQl backend. Let’s start by setting up a simple folder structure. Now for sake of simplicity in this starting guide, we will have both backend and frontend inside the same folder. So, let’s get started.

[![Basic Project Setup Commands](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fcdn-images-1.medium.com%2Fmax%2F800%2F1%2A192kZgLVZpzibBF0NV_KnQ.png "Basic Project Setup Commands")](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fcdn-images-1.medium.com%2Fmax%2F800%2F1%2A192kZgLVZpzibBF0NV_KnQ.png)

[![Basic Folder Structure](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fcdn-images-1.medium.com%2Fmax%2F800%2F1%2APXmHUcvlwMo83v36XcJbwQ.png "Basic Folder Structure")](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fcdn-images-1.medium.com%2Fmax%2F800%2F1%2APXmHUcvlwMo83v36XcJbwQ.png)

Now, after setting up the folder structure we will start by building our backend first and then move on to build a react frontend to showcase our data.

* * *

### [](#building-backend-service-with-apollo-graphql)Building Backend Service with Apollo graphQl

[![Basic backend Setup commands](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fcdn-images-1.medium.com%2Fmax%2F800%2F1%2AdsTJZqU4-yTfut5wdZY8Eg.png "Basic backend Setup commands")](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fcdn-images-1.medium.com%2Fmax%2F800%2F1%2AdsTJZqU4-yTfut5wdZY8Eg.png)

[![Folder Structure for our backend Service](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fcdn-images-1.medium.com%2Fmax%2F800%2F1%2A1JZx3jumziVWkJ00lLRqVA.png "Folder Structure for our backend Service")](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fcdn-images-1.medium.com%2Fmax%2F800%2F1%2A1JZx3jumziVWkJ00lLRqVA.png)

Now, Since we are done with the initial Folder let’s start by writing some code and get started learning a few things about the apollo server. So let’s get right into our `index.js` file and initialize our server with basic minimal configuration.  

```
const {ApolloServer, gql} = require('apollo-server');

const server = new ApolloServer({
  typeDefs,
  resolvers,
});

server.listen()
    .then(({url}) => {
      console.log(`Server ready at ${url}`);
    })
    .catch(err => {console.log(err)})
```

Enter fullscreen mode Exit fullscreen mode

Now, before we move any further let’s just analyze the 12 lines of code we have written so far and see what we are working with. Now most of the code is pretty straight forward except we see something called `typeDefs` and `resolvers` . So let’s first explore what exactly `typeDefs` and `resolvers` are.

Every graphQl server needs to define the data that can be accessed by the client and that can be done through a schema and these schemas are stored inside our `typeDefs` file. Now, this schema can have three root operation. These three operations are `Query` , `Mutation` and `subscription` . And all these have their specific purpose. `Query` are generally used for fetching the data which already exists in our database, `Mutation` are used to create or update any data and `Subscription` are used to listen to the events generated by our graphql server. Subscriptions depend on the use of a publish and subscribe primitive to generate the events that notify a subscription.

Now, since we are done with some basic introduction to `Query` , `Mutation` and `Subscription` . Similarly a `resolver` is essentially a function or a method that resolves some value for a field in the schema. They are the once which perform all the task to fetch data, create data, run some business logic to resolve the fields asked by the client. let’s get into some examples of how we can use them together to create our graphql server.

Now, let’s move forward with our example application. I personally prefer separating my `resolvers` and `typeDefs` so l et's create our files for `resolvers` and `typeDefs` .

[![Creating typeDefs and resolvers file](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fcdn-images-1.medium.com%2Fmax%2F800%2F1%2AX79Dg9oDPYP8ICKCJ0XBJg.png "Creating typeDefs and resolvers file")](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fcdn-images-1.medium.com%2Fmax%2F800%2F1%2AX79Dg9oDPYP8ICKCJ0XBJg.png)

After creating our files let’s look at our new folder structure and then we can start working with `typeDefs` because `typeDefs` are essentially like interfaces for our client based on which our client can ask for data from the server. So let’s start by creating our first `typeDefs` .

[![New Folder structure after adding typeDefs and resolvers file](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fcdn-images-1.medium.com%2Fmax%2F800%2F1%2APPK5SJvQVNmZ1gWpOmeU6A.png "New Folder structure after adding typeDefs and resolvers file")](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fcdn-images-1.medium.com%2Fmax%2F800%2F1%2APPK5SJvQVNmZ1gWpOmeU6A.png)

Now, as I said earlier that `typeDefs` is the way for the client to connect to our backend service and ask for data. So let’s see how we can define.  

```
const {gql} = require('apollo-server');


const typeDefs = gql`
        type Query {
            sayHello: String
        }

`

module.exports = typeDefs
```

Enter fullscreen mode Exit fullscreen mode

Now, in the above example, we have defined a simple `Query` which helps us fetch some data from backend and in our case it is `sayHello` and it returns a type of `String` as defined by the `sayHello` Query itself. Just make sure that you name your query so that they are self-declarative. Here our `Query` name clearly signifies what it’s going to do. Now as we have defined our `typeDefs` we also have to define our `resolver` function against this query which will actually resolve or compute some value and the way graphQl does that is by mapping each `typeDefs` name to each `resolver` function name. So here in our case, we have to define resolver with the same name. So let’s do that too.  

```
const resolvers = {
  Query: {
    sayHello: () => 'hello random person',
  },
};

module.exports = resolvers
```

Enter fullscreen mode Exit fullscreen mode

Here we have defined our `sayHello` function inside our `Query` and it resolves to certain value here in our case `hello random person` . Just make sure the return type of your `resolver` function and `typeDefs` make otherwise your queries will result in returning `null` . Now since we have created both our `typeDefs` and `resolvers` files we just have to make a little change to our `index.js` file and we are good to go. We just have to import our `resolvers` and `typeDefs` file into our index.js file and make use of them.  

```
const {ApolloServer} = require('apollo-server');
const typeDefs = require('./typeDefs')
const resolvers = require('./resolvers')
const server = new ApolloServer({
  typeDefs,
  resolvers,
});

server.listen()
    .then(({url}) => {
      console.log(`Server ready at ${url}`);
      ``
    })
    .catch(err => {console.log(err)})
```

Enter fullscreen mode Exit fullscreen mode

Now, since we are done with our introduction, let’s build a simple TODO list to get into doing CRUD operations using graphQl. Now, here we are not going to use some database, we will have a fake database inside our backend service in the form of a `json` object and we can manipulate that to perform our CRUD operations. So let’s create our fake JSON file.

[![Creating fake\_data.js file](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fcdn-images-1.medium.com%2Fmax%2F800%2F1%2AFADU-h1HZV5jUFYImbqm4g.png "Creating fake_data.js file")](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fcdn-images-1.medium.com%2Fmax%2F800%2F1%2AFADU-h1HZV5jUFYImbqm4g.png)  

```
const DAILY_TASKS = [
  {
    task: "Make Coffee",
    completed: false,
    id: 1
  },
  {
    task: "Learn GraphQl",
    completed: false,
    id: 2
  },
  {
    task: "Learn GoLang",
    completed: false,
    id: 3
  },
  {
    task: "Learn NodeJs",
    completed: false,
    id: 4
  },
  {
    task: "Learn GraphQl",
    completed: false,
    id: 5
  }
];

module.exports = DAILY_TASKS;

```

Enter fullscreen mode Exit fullscreen mode

Now, We are going to have 3 Mutation to update, create and delete data inside our fake JSON file and 1 query for interacting and fetching our data.

Now, let’s create our first `Query` to fetch the data from our backend service. Let’s call it `fetchTasks` .  

```
const { gql } = require("apollo-server");

const typeDefs = gql`
  type Tasks {
    task: String
    id: ID
    completed: Boolean
  }
  type Query {
    fetchTasks: Tasks
  }
`;

module.exports = typeDefs;

```

Enter fullscreen mode Exit fullscreen mode

Here we define our fetch task `Query` and it has a return type of `Tasks` . Now let’s write a resolver function for our newly added query.  

```
const DAILY_TASKS = require("./fake_data");
const resolvers = {
  Query: {
    fetchTasks: () => DAILY_TASKS[0]
  }
};

module.exports = resolvers;

```

Enter fullscreen mode Exit fullscreen mode

Here our query is going to return the first task always. Before updating this behavior let’s run our server first.

[![Running our server](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fcdn-images-1.medium.com%2Fmax%2F800%2F1%2A6KOFqJHGnwr5ooK_NASYhw.png "Running our server")](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fcdn-images-1.medium.com%2Fmax%2F800%2F1%2A6KOFqJHGnwr5ooK_NASYhw.png)

[![Now let’s navigate to  raw \`http://localhost:4000/\` endraw  .](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fcdn-images-1.medium.com%2Fmax%2F800%2F1%2AOZ6GujWDpmMMZpS3uYLMug.png "Now let’s navigate to  raw `http://localhost:4000/` endraw  .")](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fcdn-images-1.medium.com%2Fmax%2F800%2F1%2AOZ6GujWDpmMMZpS3uYLMug.png)

[![http://localhost:4000/](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fcdn-images-1.medium.com%2Fmax%2F800%2F1%2AAR_W-6535PKBzE9mXn1YVw.png "http://localhost:4000/")](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fcdn-images-1.medium.com%2Fmax%2F800%2F1%2AAR_W-6535PKBzE9mXn1YVw.png)

Now, when we navigate to [http://localhost:4000/](http://localhost:4000/) we are greeted with this GUI. This is known as graphql playground and we can run our queries here. Let’s run our first `Query` here.

[![Running our first Query](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fcdn-images-1.medium.com%2Fmax%2F800%2F1%2A93gy2oDWpPPMugPZykpW0A.png "Running our first Query")](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fcdn-images-1.medium.com%2Fmax%2F800%2F1%2A93gy2oDWpPPMugPZykpW0A.png)

Now, after running our first query we see our results it fetches data from our backend which we have in our fake JSON file. Now, let’s add some logic to our functions and accept some data as a filter from our clients.  

```
const { gql } = require("apollo-server");

const typeDefs = gql`
  type Tasks {
    task: String
    id: ID
    completed: Boolean
  }

  input fetchTaskFilter {
    id: ID!
  }

  input addTaskInput {
    name: String!
    completed: Boolean!
  }

  input updateTaskInput {
    id: ID!
    name: String
    completed: Boolean
  }

  type Query {
    fetchTask(filter: fetchTaskFilter): Tasks
    fetchTasks: [Tasks]
  }

  type Mutation {
    addTask(input: addTaskInput): Tasks
    updateTask(input: updateTaskInput): Tasks
  }
`;

module.exports = typeDefs;

```

Enter fullscreen mode Exit fullscreen mode

Now, in the above example, we have defined our mutation and queries to interact with our data. Now, one new thing we see is the `!`mark in front of our data types, now what this means is that this field is compulsory and we cannot execute our queries or mutation on the backend. Now let’s add some logic to our resolvers so we can interact with our data. Every resolver function inside our resolvers file receives 4 function arguments and in some form or another, almost all graphql server receives these 4 function arguments inside resolvers.

*   **_root_** — Result from the previous/parent type.
*   **_args_** — Arguments provided to the field by the client. For example, in our `typeDefs` we have `addTask(input:addTaskInput)` so the args, in this case, would be `{input:{name:"some name",completed:false}}` .
*   **_context_** — a _Mutable_ object that is provided to all resolvers. This basically contains the authentication, authorization state, and anything else that should be taken into account when resolving the query. You get access to your `request` object so you can apply any middlewares and provide that info to your resolvers through context.
*   **_info_** — Field-specific information relevant to the query. This argument is only used in advanced cases, but it contains information about the execution state of the query, including the field name, the path to the field from the root, and more.

Here we will primarily focus on args to get access to our fields sent by our client or playground.  

```
const DAILY_TASKS = require("./fake_data");
const resolvers = {
  Query: {
    fetchTask: (parent, args, context, info) => {
      return DAILY_TASKS[args.input.id];
    },
    fetchTasks: (parent, args, context, info) => {
      return DAILY_TASKS;
    }
  },
  Mutation: {
    addTask: (parent, args, context, info) => {
      const {
        input: { name, completed }
      } = args;
      const nextId = DAILY_TASKS[DAILY_TASKS.length - 1].id + 1;
      const newTask = {
        task: name,
        completed: completed,
        id: nextId
      };
      DAILY_TASKS.push(newTask);
      return newTask;
    },
    updateTask: (parent, args, context, info) => {
      const {
        input: { id, name, completed }
      } = args;
      const updateTask = DAILY_TASKS.filter(task => {
        return task.id == id;
      });
      if (name) {
        updateTask[0].task = task;
      }
      if (completed) {
        updateTask[0].completed = completed;
      }
      DAILY_TASKS.push(updateTask);
      return updateTask[0];
    }
  }
};

module.exports = resolvers;

```

Enter fullscreen mode Exit fullscreen mode

Now, we have just added some simple logic to interact with our fake database. Now let’s see how we can interact through our playground.

[![GraphQl playground](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fcdn-images-1.medium.com%2Fmax%2F800%2F1%2AfUSELRuhRrPvUAV80eUGzQ.png "GraphQl playground")](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fcdn-images-1.medium.com%2Fmax%2F800%2F1%2AfUSELRuhRrPvUAV80eUGzQ.png)

Now, we see all our mutations and queries here. Now let’s run a few mutations and queries and see if it works.

[![Running addTask Query](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fcdn-images-1.medium.com%2Fmax%2F800%2F1%2AjzgY6mNWPO8aHpX0aKqydQ.png "Running addTask Query")](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fcdn-images-1.medium.com%2Fmax%2F800%2F1%2AjzgY6mNWPO8aHpX0aKqydQ.png)

We are done with the building of our server with minimal configurations. In [part two](https://dev.to/thakursachin467/how-to-get-started-with-a-graph-ql-react-apollo-client-and-apollo-server-app-part-2-15id) of this article, we are going to use React and Apollo Client to build our front-end client and make use of the APIs we just built.
