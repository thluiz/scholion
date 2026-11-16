---
url: "https://dev.to/n_tepluhina/three-awesome-tools-for-graphql-developer-experience-28e7"
captured_at: "2026-11-16T19:30:56+00:00"
title: "Three awesome tools for GraphQL developer experience"
domain: "dev-to"
---

The thing I really like about GraphQL and Apollo Client is a developer experience they provide for me as a frontend engineer. In this article, we will take a look at some useful tools that make your everyday work easier!

> Please note this article assumes you already have some experience with GraphQL

## [](#graphql-explorerplayground)GraphQL explorer/playground

Usually, when we start working with the new API, the first thing we do is reading API documentation. In the days of good old REST API, I was really happy if I had descriptive documentation for every endpoint so things like [Swagger](https://swagger.io/tools/swagger-ui/) were a real blessing. How things are going on the GraphQL side?

Let's check the documentation for [Rick and Morty APIs](https://rickandmortyapi.com/documentation/#introduction)

As you can see, the GraphQL part is documented very briefly comparing to REST... but there is a link to the playground there!

[![GraphQL Playground](https://res.cloudinary.com/practicaldev/image/fetch/s--f57d1rLC--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.imgur.com/M43GQIf.png)](https://rickandmortyapi.com/graphql/)

So, what is this? Basically, it's a playground where you can run GraphQL queries and mutations and check the result. Try to paste this query on the left side of the explorer and click the `Run` button:  

```
query Characters {
  characters {
    results {
      id
      name
    }
  }
}
```

![Before](https://res.cloudinary.com/practicaldev/image/fetch/s--W3NqNarG--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.imgur.com/S3aoIN7.png)

![After](https://res.cloudinary.com/practicaldev/image/fetch/s--SGxfRMZe--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.imgur.com/du1gQeV.png)

If you wonder about other queries this particular GraphQL endpoint has, please don't hesitate to click on the `Docs` tab on the right side! There you can find all the information about what parameters query expects, what fields you can specify to have in the response etc.

[![GraphQL docs](https://res.cloudinary.com/practicaldev/image/fetch/s--GpgBx97L--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.imgur.com/dCXku8T.png)](https://res.cloudinary.com/practicaldev/image/fetch/s--GpgBx97L--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.imgur.com/dCXku8T.png)

Also, if you try to write a different query, you'll notice that the playground also has a linting and autocompletion:

[![Playground linting](https://res.cloudinary.com/practicaldev/image/fetch/s--DLTifayS--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.imgur.com/P7tOqqO.png)](https://res.cloudinary.com/practicaldev/image/fetch/s--DLTifayS--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.imgur.com/P7tOqqO.png)

[![Playground autocomplete](https://res.cloudinary.com/practicaldev/image/fetch/s--ixcST_Pt--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.imgur.com/QPMODMc.png)](https://res.cloudinary.com/practicaldev/image/fetch/s--ixcST_Pt--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.imgur.com/QPMODMc.png)

> A playground shown on these screenshots is [Prisma Playground](https://github.com/prisma-labs/graphql-playground). Other popular option is [GraphiQL](https://github.com/graphql/graphiql) - for example, we're using it at GitLab as our [GraphQL Explorer](https://gitlab.com/-/graphql-explorer)

## [](#linting-and-autocomplete-with-ide-plugin)Linting and autocomplete with IDE plugin

It's really nice to have a playground with all the bells and whistles but we still write the code in our IDEs/editors. Are there any tools to help us with this? Let's take a look at two popular IDEs: VS Code and WebStorm to see how they work with GraphQL.

### [](#vs-code)VS Code

If your IDE of choice is VS Code, you would be probably interested in [Apollo GraphQL extension](https://marketplace.visualstudio.com/items?itemName=apollographql.vscode-apollo) by Apollo. It provides a lot of goodness: syntax highlighting, linting, autocomplete, navigating to fragments, etc.

After installing a plugin, you need to configure it properly. To do so, create an `apollo.config.js` file in your project root. Projects are configured through a top-level `client` key in this file:  

```
// apollo.config.js

module.exports = {
  client: { ... },
};
```

Now we need to provide a schema for the plugin to operate. In the case of Rick and Morty API, we deal with the _remote_ schema so we need to set the correct schema URL in the `service` property of the `client`:  

```
// apollo.config.js

module.exports = {
  client: {
    service: {
      name: 'Rick and Morty',
      url: 'https://rickandmortyapi.com/graphql',
    },
  },
};
```

We can check how does it work for linting and autocompletion. Let's create a JS file and write a query using `graphql-tag`  

```
import gql from 'graphql-tag';

const charactersQuery = gql`
  query CharactersQuery {
    characters {
      results {
        id
        name
      }
    }
  }
`;
```

When we start adding a new field, we can see how autocompletion works:

[![VSCode Autocomplete](https://res.cloudinary.com/practicaldev/image/fetch/s--bbaBul7O--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.imgur.com/dMGnczi.png)](https://res.cloudinary.com/practicaldev/image/fetch/s--bbaBul7O--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.imgur.com/dMGnczi.png)

Also, if we add a non-existent field, it will be highlighted as an error:

[![VSCode error](https://res.cloudinary.com/practicaldev/image/fetch/s--8TQfdJbD--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.imgur.com/u6E4zae.png)](https://res.cloudinary.com/practicaldev/image/fetch/s--8TQfdJbD--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.imgur.com/u6E4zae.png)

The same features will work for `.graphql` or `.gql` files placed under the `/src` folder. If you want to include files outside of it, you should [set up your client correctly](https://www.apollographql.com/docs/devtools/apollo-config/#clientincludes)

If you want to define some GraphQL types [locally to use for Apollo state management](https://dev.to/n_tepluhina/apollo-state-management-in-vue-application-8k0), a plugin will automatically stitch the local schema with the remote one - so your local queries and mutations will be validated properly!

### [](#webstorm)WebStorm

For WebStorm IDE, we can use a [JS GraphQL](https://plugins.jetbrains.com/plugin/8097-js-graphql) plugin by Jim Kynde Meyer. After the installation, we should configure it by defining the way to your GraphQL schema. To do so, right-click on your project base folder and choose `New` -> `GraphQL Configuration File`.

This will result in creating a `.graphqlconfig` file in the root of your project with the following content  

```
// .graphqlconfig
{
  "name": "Untitled GraphQL Schema",
  "schemaPath": "schema.graphql",
  "extensions": {
    "endpoints": {
      "Default GraphQL Endpoint": {
        "url": "http://localhost:8080/graphql",
        "headers": {
          "user-agent": "JS GraphQL"
        },
        "introspect": false
      }
    }
  }
}
```

Let's give our schema some name like `"Remote Rick-n-Morty Schema"`. `pathName` option will define a name for the file where schema will be stored, we won't change it. For Rick and Morty API, we need to download the schema from the endpoint. For the `Default GraphQL endpoint`, we change a link from `localhost` to `https://rickandmortyapi.com/graphql`. We don't need any headers for this endpoint so we can safely remove this section.

Also, it would be nice to update the local GraphQL schema every single time we open the project! To achieve this, let's set `introspect` to `true`.

Now your config file should look like this  

```
// .graphqlconfig

{
  "name": "Remote Rick-n-Morty Schema",
  "schemaPath": "schema.graphql",
  "extensions": {
    "endpoints": {
      "Default GraphQL Endpoint": {
        "url": "https://rickandmortyapi.com/graphql",
        "introspect": true
      }
    }
  }
}
```

Click on the `GraphQL` tab on the bottom of the IDE. You will see the information about our GraphQL schema...but so far the schema is empty!

[![Empty schema](https://res.cloudinary.com/practicaldev/image/fetch/s--QJqxLRYg--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.imgur.com/4zWEGHL.png)](https://res.cloudinary.com/practicaldev/image/fetch/s--QJqxLRYg--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.imgur.com/4zWEGHL.png)

Double-click on the `Default GraphQL Endpoint` and select `Get GraphQL Schema from Endpoint (introspection)`.

[![Getting a schema](https://res.cloudinary.com/practicaldev/image/fetch/s--MO_cITX8--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.imgur.com/MtLIly5.png)](https://res.cloudinary.com/practicaldev/image/fetch/s--MO_cITX8--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.imgur.com/MtLIly5.png)

Now, after the schema is fetched, we can check how does it work for linting and autocompletion. Let's create a JS file and write a query using `graphql-tag`  

```
import gql from 'graphql-tag';

const charactersQuery = gql`
  query CharactersQuery {
    characters {
      results {
        id
        name
      }
    }
  }
`;
```

If we try to add a new field to the query, the plugin will give us a list of suggestions:

[![Suggestion](https://res.cloudinary.com/practicaldev/image/fetch/s--3_igvATA--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.imgur.com/RMCdw2l.png)](https://res.cloudinary.com/practicaldev/image/fetch/s--3_igvATA--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.imgur.com/RMCdw2l.png)

And if we type it wrong, we'll have an error highlighted:

[![Error](https://res.cloudinary.com/practicaldev/image/fetch/s--YfMpMpYQ--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.imgur.com/zD0zMBd.png)](https://res.cloudinary.com/practicaldev/image/fetch/s--YfMpMpYQ--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.imgur.com/zD0zMBd.png)

These features also work for `.graphql` files. Unfortunately, the plugin is not able to recognize files with a `.gql` extension like VS Code plugin does. Also, unlike VS Code plugin, Webstorm one is not stitching local GraphQL schema with the remote one.

## [](#apollo-devtools)Apollo DevTools

We just learned about how to improve our developer experience when dealing with API endpoint itself and when writing GraphQL-related code in the editor. But what about debugging a GraphQL API interaction in the browser?

If you use the [Apollo Client](https://www.apollographql.com/docs/react/) as your GraphQL client, you will be able to leverage their awesome [Apollo DevTools](https://github.com/apollographql/apollo-client-devtools) extension for Chrome or Firefox browsers.

What could you do with this extension? Let's take a glance on how does it look in the browser:

[![Apollo Devtools](https://res.cloudinary.com/practicaldev/image/fetch/s--7-xLi6E5--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.imgur.com/SBfdfhD.png)](https://res.cloudinary.com/practicaldev/image/fetch/s--7-xLi6E5--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.imgur.com/SBfdfhD.png)

*   `GraphQL` tab: this is actually a local GraphQL playground, similar to what we've described in the first part of the article. You can read schema docs here, write and run queries, just like on Prisma or GraphiQL:

[![Apollo DevTools query](https://res.cloudinary.com/practicaldev/image/fetch/s--ty2sd20G--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.imgur.com/6806RNi.png)](https://res.cloudinary.com/practicaldev/image/fetch/s--ty2sd20G--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.imgur.com/6806RNi.png)

*   `Queries`: here you can see all queries your application has called at this moment, inspect them and run them on the playground if necessary

[![Apollo DevTools Queries](https://res.cloudinary.com/practicaldev/image/fetch/s--XbtYhNL4--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.imgur.com/ModNmXI.png)](https://res.cloudinary.com/practicaldev/image/fetch/s--XbtYhNL4--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.imgur.com/ModNmXI.png)

*   `Mutations`: same as the previous tab but for GraphQL mutations
    
*   `Cache`: in my opinion, this one is the most useful. Here you can always check what do you have right now in the Apollo Client cache as a result of all the previous queries and mutations. It really saved my life when I had complex update logic in mutations and was completely lost about how they affect my cache.
    

[![Apollo Cache](https://res.cloudinary.com/practicaldev/image/fetch/s--La_Tvke9--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.imgur.com/bLDchBj.png)](https://res.cloudinary.com/practicaldev/image/fetch/s--La_Tvke9--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.imgur.com/bLDchBj.png)

I hope all the mentioned tools will make your life a bit easier when working with GraphQL! Please let me know in comments if you have any questions about them
