---
title: "How YOU can learn to extend Gatsby further by authoring Plugins"
date: '2020-07-05T14:10:46+00:00'
category: webclip
summary: 'The article explains how Gatsby plugins extend the build process, then shows how to write a source plugin that fetches SWAPI data and a transformer plugin that turns CSV rows into queryable nodes.'
tags: ["gatsby", "plugins", "source-plugin", "transformer-plugin"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "How YOU can learn to extend Gatsby further by authoring Plugins"
    url: "https://dev.to/azure/how-you-can-learn-to-extend-gatsby-further-by-authoring-plugins-4aik"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/dev-to--how-you-can-learn-to-extend-gatsby-further-by-authoring-plug.md"
    kind: repo
---

The article says Gatsby plugins extend the framework by adding or transforming data during the build process. It separates source plugins, which fetch data and create nodes, from transformer plugins, which convert existing content into nodes that Gatsby can query.

## Reading notes

- Source plugins run early in the build process and add fetched data to Gatsby's in-memory data graph as nodes.
- Transformer plugins act on content already in the graph and convert one content type into another, such as JSON or YAML into nodes.
- A plugin can live inside the project or as a separate Node.js library, but Gatsby must be told about it through `gatsby-config.js`.
- The source plugin demo creates `gatsby-source-swapi` with `gatsby-node.js` and `package.json`.
- That plugin defines `sourceNodes()`, fetches planets from `https://swapi.dev/api/planets`, and creates nodes with `createNodeId()`, `createContentDigest()`, and `actions.createNode()`.
- The plugin is registered in `gatsby-config.js`, then tested with `gatsby develop` and inspected in `http://localhost:8000/___graphql`.
- The transformer demo builds `gatsby-transformer-csv` as a separate Node.js project.
- It uses `gatsby-source-filesystem` to scan `src/csv`, then `onCreateNode()` filters nodes whose media type is `text/csv`.
- The plugin reads file content with `loadNodeContent(node)`, parses CSV rows into objects, creates child nodes, and links them to the file node with `createParentChildLink()`.
- During development, the article recommends `gatsby clean` before rerunning `gatsby develop` so cached data does not hide code changes.
- The final result is that CSV file fields become available in GraphQL queries through Gatsby's node graph.
