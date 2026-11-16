---
url: "https://dev.to/azure/how-you-can-learn-to-extend-gatsby-further-by-authoring-plugins-4aik"
captured_at: "2026-11-16T01:39:51+00:00"
title: "How YOU can learn to extend Gatsby further by authoring Plugins"
domain: "dev-to"
---

TLDR; this article will teach you how to build two types of plugins for Gatsby and thereby extend Gatsby's capabilities.

This article is part of a series. If you are completely new to Gatsby I suggest you start with the first article on top:

*   Part I, Gatsby introduction

Plugins are one of the best parts of Gatsby. With the help of Plugins, you can fetch data and also transform data to make it all usable by Gatsby. Being able to extend Gatsby's capacity with plugins is, in my opinion, one of the most powerful things about Gatsby.

## [](#references)References

*   [Plugins library](https://www.gatsbyjs.org/plugins/)
*   [First article on Gatsby](https://dev.to/azure/how-you-can-use-gatsby-react-and-graphql-to-author-blazingly-fast-static-apps-p08)
*   [Create a source plugin](https://www.gatsbyjs.org/docs/creating-a-source-plugin/)
*   [Creating a transform plugin](https://www.gatsbyjs.org/docs/creating-a-transformer-plugin/)
*   [Gatsby CLI tool I built](https://github.com/softchris/gatsby-cli) This CLI tool helps you scaffold, components, pages, and plugins.

Here are some more links if you want to take your Gatsby app to the Cloud

*   [Docs: Azure Static Web Apps, overview page](https://docs.microsoft.com/en-gb/azure/static-web-apps?WT.mc_id=staticwebapps-github-chnoring)
*   [Docs: Azure Static Web Apps, add Serverless API](https://docs.microsoft.com/en-us/azure/static-apps/apis?WT.mc_id=staticwebapps-github-chnoring)
*   [Docs: Azure Static Web Apps, setup Custom domain](https://docs.microsoft.com/en-us/azure/static-apps/custom-domain?WT.mc_id=staticwebapps-github-chnoring)
*   [LEARN module: Gatsby and Azure Static Web Apps](https://docs.microsoft.com/learn/modules/create-deploy-static-webapp-gatsby-app-service?WT.mc_id=staticwebapps-github-chnoring)
*   [LEARN module: SPA applications + Serverless API and Azure Static Web Apps](https://docs.microsoft.com/learn/modules/publish-app-service-static-web-app-api?WT.mc_id=staticwebapps-github-chnoring)
*   [Docs: Azure Static Web Apps, Routing](https://docs.microsoft.com/en-us/azure/static-web-apps/routes?WT.mc_id=staticwebapps-github-chnoring)
*   [Docs: Azure Static Web Apps, Authentication & Authorization](https://docs.microsoft.com/en-us/azure/static-web-apps/authentication-authorization?WT.mc_id=staticwebapps-github-chnoring)
*   [Quickstart: Azure Static Web Apps + Gatsby](https://docs.microsoft.com/en-us/azure/static-apps/publish-gatsby?WT.mc_id=staticwebapps-github-chnoring)

## [](#plugins)Plugins

Gatsby's plugins work to augment, to give Gatsby functionality it didn't have before. Plugins operate during a _build process_ in which it's able to run the plugins before the page components are being built. Why does the order matters? Well, the plugins are supposed to add data to the in-memory data graph or change what's already there and make it something that's easy to render in a page component. We, therefore, differ between two different types of plugins:

*   **Source plugins**  
    Source plugins _source_ content. _Sourcing_ means it fetches content from somewhere and then adds it to the in-memory data graph as Nodes.
    
*   **Transformer plugins**  
    Transformer plugins are transforming a certain content type from one type to another. Just like source plugins a transformer plugin ends up changing the data graph and its Nodes. Examples of things a Transformer plugin could do is to take the content of JSON or YAML files and convert that into Nodes the user can query for.
    

### [](#where-to-create-them)Where to create them

Plugins can be created in one of two ways:

*   **In your project**, you can create a plugin directly in your project. This plugin is now tied to this project.
*   **As a Node.js library**, you can also create a plugin as a separate Node.js library and install it like you would any Node module.

### [](#how-to-configure)How to configure

Regardless of whether you create a plugin directly in the library or download them as a Node module you need to tell the Gatsby project they exist. There's a `gatsby-config.js` that we can instruct to say here's a plugin please run it during the build process.

### [](#plugin-anatomy)Plugin anatomy

All a plugin need is a `gatsby-node.js` file and a `package.json` file, like this:  

```
--| gatsby-node.js
--| package.json
```

## [](#demo-author-source-plugin)DEMO author source plugin

What you are about to do next is implement the Gatsby Node API. In the context of a source plugin that means that you will export a JavaScript module that implements the method `sourceNodes()`. The method `sourceNodes()` will be invoked early in the build process and expects us to fetch data from somewhere and turn that data into Nodes.

To create and run your plugin we will need to do the following:

1.  Create the files `gatsby-node.js` and `package.json`
2.  Place the files under the `plugins` directory or in a directory of your choosing
3.  Implement the `sourceNodes()` method
4.  Configure the plugin for use
5.  Run the build process and see the plugin working

### [](#create-the-needed-files)Create the needed files

1.  Create the file `gatsby-node.js`, give it the following content:

```
  exports.sourceNodes = async({ actions, createNodeId, createContentDigest }) => {  

  });
```

You will implement this shortly.

1.  Create the file `package.json`, give it the following content:  
    
    ```
    {
      "name": "gatsby-source-swapi",
      "version": "1.0.0",
      "description": "",
      "main": "gatsby-node.js",
      "scripts": {
        "test": "echo \"Error: no test specified\" && exit 1"
      },
      "keywords": [],
      "author": "",
      "license": "MIT"
    }
    ```
    
    Note how the `name` property has the name `gatsby-source-swapi`. The two first parts is a name convention. The convention looks like this `<gatsby>-<what source or transform>-<from where>`. Given the name you therefore state that you will create a `source` plugin reading its data from `swapi`. What is swapi? The Star Wars API of course, located at `https://swapi.dev/`.
    

### [](#plugin-placement)Plugin placement

You will create a `plugins` directory under `src/` directory. Additionally, you will create a directory with the same name as the name you gave the plugin in the `package.json` file. You should now have a structure looking like this:  

```
--| src/
----| plugins/
------| gatsby-source-swapi
--------| gatsby-node.js
--------| package.json
```

It is possible to still create plugins within your project but not place them in the `plugins/` directory. You do need to point out to Gatsby where to find your plugin. Let's come back to this one in the configure section.

### [](#implement)Implement

Open up your `gatsby-node.js` file. The data your plugin is about to query is located at `https://swapi.dev`. To fetch the data you will need a library capable of fetching data over HTTP. Ensure you are at the root of the Gatsby project before typing the following command:  

```
npm install node-fetch
```

The above will install the `node-fetch` library which will help us do `fetch()` requests like we are used to from the Browser.

Add the following code to `gatsby-node.js`:  

```
async function getSwapiData() {
  const res = await fetch("https://swapi.dev/api/planets");
  const json = await res.json();
  return json.results;
}
```

The code above fetches data from `https://swapi.dev` and converts it to JSON. Next locate the part in the code that says `export.sourceNodes` and replace it with this:  

```
exports.sourceNodes = async({ actions, createNodeId, createContentDigest }) => {  
  const planets = await getSwapiData();

  planets.forEach(planet => {
    const newNode = {
      ...planet,
      id: createNodeId(planet.name),
      internal: {
        type: "SwapiNode",
        contentDigest: createContentDigest(planet),
      },
    };
    // creating nodes from SWAPI data
    actions.createNode(newNode);
  });

};
```

Above you are invoking the method `getSwapiData()` that fetches the data you need from the outside. Next, you are iterating through the data. For every iteration, you are creating a Node that will be inserted into the built-in data graph. Let's break down the methods being invoked:

*   `createNodeId()`, this method will generate a unique ID for your Node.
*   `createContentDigest()`, this is a hash of the content, a summary being encoded as a so-called MD5 hash. This is used for caching.
*   `createNode()`, this is what is actually creating the Node and inserts it into the Graph.

Note also how we set the `internal.type` to `SwapiNode`. Let's revisit this when we later run Gatsby.

### [](#configure-plugin)Configure plugin

Now that you have authored your plugin it's time to tell Gatsby about your plugin so it can _source_ the data so you can use that data as part of your Gatsby app. Locate the file `gatsby-config.js`, open it, and add the following entry:  

```
`gatsby-source-swapi`
```

## [](#run-the-plugin)Run the plugin

To test out the plugin type the following command:  

```
gatsby develop
```

Above you are starting Gatsby's development server but you could also have tested the plugin out by typing `gatsby build`. The reason for going with `gatsby develop` is that you want to see the built-in graph and how your Nodes have been added to it. Navigate to URL `http://localhost:8000/___graphql` in your browser.

[![](https://res.cloudinary.com/practicaldev/image/fetch/s--Mv0kesgt--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/gatsby-swapi-graphql.png)](https://res.cloudinary.com/practicaldev/image/fetch/s--Mv0kesgt--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/gatsby-swapi-graphql.png)

Above you see the Nodes `allSwapiNode` and `swapiNode` have been created. Let's try to query for the data as well by drilling down and selecting Nodes in the explorer section:

[![](https://res.cloudinary.com/practicaldev/image/fetch/s--SGPWP0FM--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/gatsby-swapi-graphql-query.png)](https://res.cloudinary.com/practicaldev/image/fetch/s--SGPWP0FM--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/gatsby-swapi-graphql-query.png)

## [](#demo-author-transformer-plugin)DEMO author transformer plugin

Let's look at how to author a transformer plugin next. This time you will develop this plugin as a stand-alone Node.js project. This is how you would author a plugin that you mean to redistribute. The point of this plugin is to be able to read and transform content inside of CSV files that is placed in the Gatsby project.

### [](#the-plan)The plan

The overall plan is to come in at a later stage than a sourcing plugin would. This later stage is when a node has just been created. As you have seen in the previous demo a Node is created as part of a sourcing process. Gatsby has a built-in source plugin `gatsby-source-filesystem` that scans the project directory and creates a Node from every file. You will use that fact and filter out Nodes that are the result of scanning `.csv` files. What you want is for each and every node representing a CSV file, read out the content from the said file, and create a child node from it. That way you will be able to query for contents within the files and not just the file nodes themselves.

You will need to do the following:

1.  Create CSV data in the Gatsby project
2.  Scaffold a new Node.js project and create the files `package.json` and `gatsby-node.js`
3.  Implement the method `onCreateNode()`
4.  Configure the plugin for use
5.  Run the plugin

### [](#create-csv-data)Create CSV data

In your Gatsby project create a directory `csv` under the `src` directory and inside of it create the file `orders.csv`. Give the file the following content:  

```
id       name       created
1        order1     2011-01-01
2        order2     2011-02-12
```

Your project structure should look something like this:  

```
--| src/
----| csv/
------| orders.csv
```

### [](#scaffold-a-new-nodejs-project)Scaffold a new Node.js project

Place yourself in a new directory apart from the Gatsby project. In the terminal run the command:  

```
npm init -y
```

This will create a `package.json` file with some Node.js defaults. Locate the `name` property and change it to the following:  

```
"name": "gatsby-transformer-csv"
```

This follows the convention that was mentioned before for the source plugin, namely that it's a gatsby plugin of type _transform_ that operates on CSV files.

Create the file `gatsby-node.js` and give it the following content:  

```
exports.onCreateNode({
  node,
  actions,
  loadNodeContent,
  createNodeId,
  createContentDigest,
}) {}
```

Your plugin project structure should look like this:  

```
--| package.json
--| gatsby-node.js
```

### [](#implement)Implement

Create the file `parseContent.js` and give it the following content:  

```
function parseContent(content) {
  const [headerRow, ...rest] = content.split("\n");
  const headers = headerRow.match(/\w+/g);
  const data = [];
  rest.forEach((row) => {
    const columns = row.match(/[a-z0-9-]+/g);
    let obj = headers.reduce((acc, curr, index) => {
      acc = { ...acc, [curr]: columns[index] };
      return acc;
    }, {});
    data.push(obj);
  });
  return data;
}

module.exports = parseContent;
```

What the above does is to take the CSV content and transform it from it's CSV format, with headers as the first row and content on the remaining rows to a list with objects on this format:  

```
[{
  'column1': 'first row value, first column',
  'column2': 'first row value, second column',
  'column3': 'first row value, third column'
},
{
  'column1': 'second row value, first column',
  'column2': 'second row value, second column',
  'column3': 'second row value, third column'
}]
```

Open up `gatsby-node.js`, and replace its content with the following:  

```
const parseContent = require('./parseContent')

async function onCreateNode({
  node,
  actions,
  loadNodeContent,
  createNodeId,
  createContentDigest,
}) {
  function transformObject(obj, id, type) {
    const csvNode = {
      ...obj,
      id,
      children: [],
      parent: node.id,
      internal: {
        contentDigest: createContentDigest(obj),
        type,
      },
    };
    createNode(csvNode);
    createParentChildLink({ parent: node, child: csvNode });
  }

  const { createNode, createParentChildLink } = actions;

  if (node.internal.mediaType !== `text/csv`) {
    return;
  }

  const content = await loadNodeContent(node);
  const parsedContent = parseContent(content);
  parsedContent.forEach(row => {
    transformObject(row, createNodeId(row.id), 'CSV')
  })
}
exports.onCreateNode = onCreateNode
```

There is a lot of interesting things going on here. Let's list it from the top:

1.  `transformObject()`, this is an inner function that will help you create a CSV node. What it does is create a child node using the `createNode()` function and the input data you give it. Then it connects itself to a parent, an instance called `node` via the method `createParentChildLink()`.
2.  **filter nodes**, you are only interested in file nodes from CSV files so the following line of code filter out all other nodes:

```
   if (node.internal.mediaType !== `text/csv`) {
     return;
   }
```

1.  **load content**, Here we are using a built-in method to read out the CSV content from the Node so we can parse it from CSV to an object format that we can use when creating the child node:

```
   const content = await loadNodeContent(node);
```

1.  **parse content** here you are parsing the content from CSV to an object format

```
   const parsedContent = parseContent(content);
```

1.  **create child nodes for each row**, here you are iterating the list you got back from parsing and invoke the `transformObject()` method that will create a child node for each row.

```
   parsedContent.forEach(row => {
     transformObject(row, createNodeId(row.id), 'CSV')
   })
```

### [](#configure-the-plugin)Configure the plugin

To use this plugin we need to do the following:

1.  **Link plugin project with Gatsby project**, because you are developing a Node.js plugin project locally you need to _emulate_ that you have installed it via `npm install`. A way to do that is to invoke the `npm link` command. You will do so in two steps:

*   at the root of the plugin project type the following command in the terminal:

```
   npm link
```

this will create a so called `symlink`

*   at the root of the Gatsby project type the following:

```
   npm link gatsby-transformer-csv
```

this will link in the content of your plugin project `node_modules/gatsby-transformer-csv` in the Gatsby project. Any changes you do to your plugin project will be reflected as it's a link.

1.  Open up `gatsby-config.js` and add an entry `gatsby-transformer-csv` to the `plugins` array
2.  Additionally add the following entry to scan for the CSV files:

```
   {
     resolve: `gatsby-source-filesystem`,
     options: {
       name: `csv`,
       path: `./src/csv`,
     },
   }
```

### [](#run-it)Run it

Gatsby is very efficient in caching data. While developing plugins it's a good idea to run the following command to clear that cache every time you change the code and want to try it out:  

```
gatsby clean
```

Run your Gatsby project with the following command:  

```
gatsby develop
```

Open up a browser and navigate to the following URL `http://localhost:8000/___graphql`.

Drill down into the following nodes in the explorer section and you should see the following columns available:

[![](https://res.cloudinary.com/practicaldev/image/fetch/s---SDjgTyM--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/gatsby-transform-graphql.png)](https://res.cloudinary.com/practicaldev/image/fetch/s---SDjgTyM--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/gatsby-transform-graphql.png)

Above you can see how the node has the fields `id` and `name` on it and when queried we are to get a response. That response is data that resided inside of the CSV file.

## [](#summary)Summary

You were taught an advanced topic today, plugins. Being able to extend Gatsby with plugins is a great feature. You were taught how to create _source_ plugins that enabled you to fetch external data and make that part of Gatsby's build process. Additionally, you were shown how to process content within files residing inside of your project when building _transform_ plugins. Hopefully, you feel empowered by now that you can extend your Gatsby app in any direction you see fit. If there is no plugin already that you can download you now know how to build one, or maybe two? :)
