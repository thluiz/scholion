---
url: "https://dev.to/albertomontalesi/5-best-gatsby-plugins-for-your-programming-blog-4d6g"
captured_at: "2026-11-16T00:56:30+00:00"
title: "5 Best Gatsby plugins for your programming blog"
domain: "dev-to"
---

> Check out my [blog](https://inspiredwebdev.com/) for more articles or [Github](https://github.com/AlbertoMontalesi/The-complete-guide-to-modern-JavaScript) for my free-to-read JavaScript Ebook that covers all the new features from ES6 to 2019.  
> If you want find a great place for interactive tutorials, i recommend [Educative](https://www.educative.io/explore?aff=BqmB) (Disclaimer: the link it's affiliate) where I'm currently finishing to build my JavaScript course.

## [](#what-is-gatsbyjs)What is GatsbyJS?

GastbyJS is a Static Site Generator that you can use to build super fast blogs and websites.

Together with Hugo and Jekyll is the most popular and it's currently my favorite one due to the fact that it uses React.

Getting started with GatsbyJS is very easy and if you download one of their starter template you can get your blog up and running in literally five minutes, just push your code to Github and deploy to Netlify.

If you want two examples of blogs built with GatsbyJS you can check out my personal blog [inspiredwebdev.com](https://inspiredwebdev.com/) and my girlfriend's vietnamese learning website [elingos.com](https://elingos.com/).

One thing I like about GatsbyJS is the ecosystem of plugins you can use to extend its functionalities and to make your life easier.  
Being built on React means that every React plugin that you love will work on GatsbyJS but in this article i'm going to cover my favorite plugins specifically for GatsbyJS.

These are all plugins that i currently use on my two aforementioned websites.

## [](#gatsbyremarkprismjs)gatsby-remark-prismjs

If you are building a programming blog such as mine, chances are you are going to need syntax highlight for your code blocks.

This plugin will make it very easy to add PrismJS to your website, letting you choose among different choices of syntax highlight which you can preview on the [PrismJS website](https://prismjs.com/).

You can get it [here](https://www.gatsbyjs.org/packages/gatsby-remark-prismjs/)

## [](#gatsbyplugingoogleanalytics)gatsby-plugin-google-analytics

This plugin will let you easily connect your GatsbyJS website to Google Analytics so that you can have a clear idea of how many users you have and their behavior.

What I like about this plugin is the `OutboundLink` component that let's you track clicks on outbound links. I use it to track how many people click on my Amazon link to check out my [book](http://a-fwd.to/5gUojI8).

You can get this plugin [here](https://www.gatsbyjs.org/packages/gatsby-plugin-google-analytics/).

## [](#gatsbypluginmanifest)gatsby-plugin-manifest

Progressive Web Apps are amazing, I love them, and the choice of making your site a PWA should be a no brainer.

This plugin will help you easily set up a manifest for your website so that users can add it to their home screen.  
You can edit the color and the background of the splash page and the plugin also helps you autogenerate icons.

Making your site a PWA can enhance the experience of your followers and make it much easier for them to get back to your site from the home screen of their phones.

You can get this plugin [here](https://www.gatsbyjs.org/packages/gatsby-plugin-manifest/).

## [](#gatsbytransformerjson)gatsby-transformer-json

When you write blog posts on your GatsbyJS you will mostly use Markdown, and for that you will need the plugin `gatsby-transformer-remark` but there are times where you might want to have configuration files and you are probably going to store them as JSON files.

In my case, I have JSON file called products where I store information about different articles, such as title, description, price and image.

Those information are then pulled in the page with the use of this plugin and I dynamically generate cards to display my products. To see what I mean you can check out [this page of one of my sites](http://elingos.com/shop).

Other examples of instances where I would use a JSON file are: a list of team members or a list of testimonials.

You can get this plugin [here](https://www.gatsbyjs.org/packages/gatsby-transformer-json/).

## [](#gatsbypluginreacthelmet)gatsby-plugin-react-helmet

This plugin adds support for React Helmet, a component which lets you control your document head using their React component.

This includes passing metadata such as page title, description and different images for when your page get's shared on social medias.

It's definitely a useful plugin that will make your life (and your SEO) better.

You can get this plugin [here](https://www.gatsbyjs.org/packages/gatsby-plugin-react-helmet/).

This concludes the list of my 5 favorite GatsbyJS plugin. If you know others that can be useful or that you personally love, please leave a comment and share them with everybody.

* * *

Thank you very much for reading. Follow me on [DevTo](https://dev.to/albertomontalesi) or on my blog at [inspiredwebdev](https://inspiredwebdev.com/) for more.

[  
![book banner](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fraw.githubusercontent.com%2FAlbertoMontalesi%2FThe-complete-guide-to-modern-JavaScript%2Fmaster%2Fassets%2Fbanner.jpg)  
](http://a-fwd.to/5gUojI8)  
Get my ebook on [Amazon](http://a-fwd.to/5gUojI8) and [Leanpub](https://leanpub.com/thecompleteguidetomodernjavascript2019)
