---
url: "https://dev.to/lampewebdev/nestjs-adding-a-frontend-to-the-monorepo-11g6"
captured_at: "2026-11-16T01:46:10+00:00"
title: "NestJS - Adding a frontend to the monorepo"
domain: "dev-to"
---

In the last two blog posts, we created a Monorepo and integrated Redis. You can find them here:

*   [Monorepo and Microservice setup in Nest.js](https://dev.to/lampewebdev/monorepo-and-microservice-setup-in-nest-js-41n4)
*   [NestJS - Microservices with Redis](https://dev.to/lampewebdev/nestjs-microservices-with-redis-996)

In this blog post, we will add Vue as our frontend and make it work within our Monorepo.

### [](#installing-the-dependencies)Installing the dependencies

Let's first get install our dependencies:  

```
yarn add vue
```

And now our developer dependencies  

```
yarn add -D babel-loader css-loader file-loader html-webpack-plugin node-sass sass-loader url-loader vue-loader vue-template-compiler webpack webpack-bundle-analyzer webpack-cli webpack-dev-server vue-eslint-parser
```

As you can see, we need to install way more dependencies for development. Most of them are dependencies to make Webpack build and serve our frontend.  
Webpack will handle HTML, vue, css, sass and files.

### [](#creating-the-frontend)Creating the frontend

First, we need to create a folder named 'frontend'  

```
mkdir frontend
```

In that folder, we will have all of our 'frontends'. For this example, we want to create our frontend for our 'blog' backend.  

```
cd frontend
mkdir blog
```

Now we need to create an `index.html` file. This will be the entry file to the blog frontend.  

```
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width,initial-scale=1.0" />
    <title>My Vue app with webpack 4</title>
  </head>

  <body>
    <div id="app"></div>
  </body>
</html>
```

The most important line here is the `div` with the `id="app"`. VueJS needs this `div` as an entry point.

The next file we need is a `webpack.config.js`  

```
/* eslint-disable @typescript-eslint/no-var-requires */
const path = require('path');
const VueLoaderPlugin = require('vue-loader/lib/plugin');
const BundleAnalyzerPlugin = require('webpack-bundle-analyzer').BundleAnalyzerPlugin;
const HtmlPlugin = require('html-webpack-plugin');

const config = {
  context: __dirname,
  entry: './src/index.ts',
  output: {
    path: path.resolve(process.cwd(), 'dist/frontend'),
    filename: '[name].[contenthash].js'
  },
  target: 'web',
  module: {
    rules: [
      {
        test: /\.vue$/,
        loader: 'vue-loader'
      },
      {
        test: /\.css$/,
        use: [
          'vue-style-loader',
          'css-loader'
        ]
      },
      {
        test: /\.ts$/,
        loader: "ts-loader",
        options: { appendTsSuffixTo: [/\.vue$/] },
        exclude: /node_modules/
      },
      {
        test: /\.scss$/,
        use: [
          'vue-style-loader',
          'css-loader',
          'sass-loader'
        ]
      },
      {
        test: /\.svg$/,
        use: 'file-loader'
      },
      {
        test: /\.png$/,
        use: [
          {
            loader: 'url-loader',
            options: {
              mimetype: 'image/png'
            }
          }
        ]
      }
    ]
  },
  resolve: {
    extensions: [
      '.js',
      '.vue',
      '.tsx',
      '.ts'
    ]
  },
  plugins: [
    new HtmlPlugin({
      template: 'index.html',
      chunksSortMode: 'dependency'
    }),
    new BundleAnalyzerPlugin({
      analyzerMode: 'static',
      openAnalyzer: false,
    }),
    new VueLoaderPlugin(),
  ],
  optimization: {
    runtimeChunk: 'single',
    splitChunks: {
      cacheGroups: {
        vendor: {
          test: /[\\/]node_modules[\\/]/,
          name: 'vendors',
          chunks: 'all'
        }
      }
    }
  },
  devServer: {
    contentBase: path.join(__dirname, 'public'),
    compress: true,
    port: 9000
  }
};

module.exports = config;
```

Webpack configs are fun! Let's start from the bottom. The `devServer` will run on port `9000` and will look for files in the `public`. For that to work, we need to set the `context` option to `__dirname`. `__dirname` will resolve to the path that the directory is currently in, in our case, the blog frontend folder. `entry` is the file that bootstraps and we will create it next. In the `output` we need to specify the path. `process.cwd()` will resolve to the main project folder, and we are adding `dist/frontend`. This means you can find there our frontend files. The rest is configuration to get Vue running with typescript, to load CSS, SCSS, SVG and png files.

Typescript also needs a config.  

```
{
  "compilerOptions": {
    "outDir": "./dist/",
    "sourceMap": true,
    "strict": true,
    "noImplicitReturns": true,
    "noImplicitAny": true,
    "module": "es6",
    "moduleResolution": "node",
    "target": "es5",
    "allowJs": true
  },
  "include": [
    "./blog/src/**/*"
  ]
}
```

This is a pretty standard ts config. We need to include our `blog/src` folder. Without this, you will get a typescript error.

Now let us create our `src/index.ts` file, `src/App.vue` file and `src/vue-shim.d.ts`.

`index.ts`:  

```
import Vue from 'vue';
import App from './App.vue';

new Vue({
  el: '#app',
  render: h => h(App),
});
```

This is the default VueJS setup.

`App.vue`  

```
<template>
  <h1>lampeweb dev blog</h1>
</template>

<script lang="ts">
import Vue from 'vue';

export default Vue.extend({
  data: function() {
    return {
      name: 'Hello World!',
    };
  },
});
</script>
```

Thanks to our Webpack config we can already use typescript in our Vue components. This file is a simple Vue component which just will display a header with the text `lampeweb dev blog`.

`vue-shim.d.ts`:  

```
declare module '*.vue' {
  import Vue from 'vue';
  export default Vue;
}
```

This will make typescript and your editor happy :). Do you want to know more about how `declare module` works? Leave a comment!

We need now to define our npm scripts next.  

```
{
  "scripts": {
    "f:blog:dev:watch": "webpack-dev-server -d --mode development --config ./frontend/blog/webpack.config.js",
    "f:blog:build": "webpack -p --mode production  --config ./frontend/blog/webpack.config.js"
  }
}
```

We can now test if everything worked with:  

```
yarn run f:blog:dev:watch
```

After Webpack has built our frontend, you should see the following:  
[![Alt Text](https://res.cloudinary.com/practicaldev/image/fetch/s--kxCA-47J--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/tpevds94qq14kxrvulg6.png)](https://res.cloudinary.com/practicaldev/image/fetch/s--kxCA-47J--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/tpevds94qq14kxrvulg6.png)

I hope you liked that post! If you want a follow-up, please comment, like, and share. So I can know that you are interested in content like that!

**👋Say Hello!** [Instagram](https://www.instagram.com/lampewebdev/) | [Twitter](https://twitter.com/lampewebdev) | [LinkedIn](https://www.linkedin.com/in/michael-lazarski-25725a87) | [Medium](https://medium.com/@lampewebdevelopment) | [Twitch](https://dev.to/twitch_live_streams/lampewebdev) | [YouTube](https://www.youtube.com/channel/UCYCe4Cnracnq91J0CgoyKAQ)
