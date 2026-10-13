---
url: "http://davidwalsh.name/13-factors-choosing-javascript-charting-library"
captured_at: "2015-03-29T20:36:13-03:00"
title: "13 Factors to Consider While Choosing a JavaScript Charting Library"
domain: "davidwalsh-name"
---

# 13 Factors to Consider While Choosing a JavaScript Charting Library

By
[Vikas Lalwani](http://lalwanivikas.github.io/) on
March 24, 2015

Before starting your search for a charting library, you need to know that creating good data visualization (dataviz) is a huge time investment if you are planning to build a serious application. Having clear answers to questions like what exactly your dataviz is going to achieve, on which devices will it be used, how much time you have to build the application etc. will help you make the best use of guidelines mentioned below.

## Cross Browser Compatibility

Whether you need a charting library that’s compatible with all browsers or just modern browsers depends on your target audience. If you are building for government or for enterprise clients, there’s a very good chance that they are still using older versions of IE. So charting libraries that only work with modern browsers might not be a good choice.

It’s a pain to handle cross-browser compatibility issues, and I believe the library you choose should do it for you.

## Cross Device Compatibility

Will your application be used primarily on desktop or are you targeting mobile users as well? If it’s just for large screen viewing, most of the charting libraries will work for your dataviz component, but if you want to ensure a consistent experience across hand-held devices as well, the charting library you choose should be responsive. This is becoming increasingly important because of changing user habits in recent times.

## Input Data Format

Although JSON (JavaScript Object Notation) is gradually becoming the standard format especially when it comes to charting libraries, there are still many cases where you’ll have to deal with XML. If you need XML data for your dataviz, it will be good to know whether your charting library supports it.

## Customizability

This, for me at least, is the biggest decision factor. Is the charting library flexible enough so that I can make it do what I want, or will it just look good on defaults and you are on your own if you try to customize it?

There are hundreds of things that I like to play around with like adding custom shapes, configuring legends, attaching events (click, hover, key press), leveraging drill-down of data, and applying themes etc. If you want to create a beautiful design, it’ll be good to have a library that is easily customizable so that you can mold it according the design of your application.

## Range of Available Charts

This one is a no brainer. Whatever dataviz you want to create should be part of the library. But it’s not so easy as various charting libraries have collective packages in which similar charts are grouped like maps, widgets and stock charts. So depending on the use case you might want to go for a particular chart type only, or you can get a complete bundle.

If you want to compare different charting libraries based on range of available charts, you’ll find [this resource](http://www.fusioncharts.com/javascript-charting-comparison/) very helpful.

## Learning Curve

Some data visualization libraries like D3.js have a steep learning curve. No doubt D3.js is very powerful, but if you are running on a tight deadline or using a charting library for the first time, I would not recommend that.

On the other hand, if you are getting started in dataviz and have lots of time on your hands for experimentation, you should by all means try libraries that are beautiful but require some time investment.

## Compatibility With Other Parts of Code

Imagine you are a PHP or ASP.NET ninja and are not familiar with JavaScript very much. Wouldn’t it be great if you can build charts without writing any JavaScript code? Some libraries have free plugins and wrappers that generate the required JavaScript and HTML code for you, which is then used to render charts on a browser page. Examples [here](http://www.fusioncharts.com/extensions/) and [here](http://www.highcharts.com/component/content/article/14-articles/2-third-party-implementation/).

## Performance

Performance is dependent on many factors like size of library, memory usage while rendering, garbage collection and number of [browser repaint cycles](http://paulirish.com/2011/viewing-chromes-paint-cycle/). I value performance very highly, but optimizing only for performance is not always the best idea. This might sound contradictory so let me explain my point with an example.

Let’s assume you are building a dashboard which will be used on local intranet. Do you think using the library with smallest package size makes sense here? In this case I’ll choose a library that comes out best based on other factors discussed here. Saving on library size will be the least of my concerns.

## Exporting

This point is not applicable for every use case, but only for cases like reports and dashboards. If you are building a dashboard for business audience, your users might want to export charts to PDF or images. It will be better that the charting library you choose support export feature out of the box. Common export formats to look for are JPEG, PNG, PDF and SVG.

## Design and Interactivity

Design is more than just look and feel of a chart. It should not only look good (themes, color scheme), but it should have meaningful interactivity. For example, if you are building a pie-chart, clicking a pie should pull it out (or add border on circumference) by default. Custom code should not be required for that. Clicking a legend icon in multi-series line chart should toggle the visibility of related data plot.

## Pricing and Licensing Terms

Most of the libraries now give away their source code when you buy a licence, but that doesn’t mean you are free to do whatever you want. It’s important to know what all permissions you’ll need for your project and buy a relevant license. Terms and pricing varies depending on factors like number of users, type of application (SaaS, intranet, web) and number of servers.

## Support

If you are building an application, dataviz might not be your core strength. So when you face a problem, you might need some external support to solve it. Support can come in many forms like personal, forum or community sites like StackOverflow. If you are on a tight schedule you would not want to wait for an answer on StackOverflow. Personal support or dedicated forum would be very useful in this case.

In case of popular libraries, most of the answers to general questions are easily available. But I’ve faced dead ends couple of times while testing edge cases. If you think you might need dedicated support, I would recommend buying a charting component instead of using an open source solution (given it meets all other requirements).

## Open Source

I love open-source, but I believe it’s not the right solution for everything. Especially when it comes to charting solutions, there are tons of tiny open open-source libraries available on GitHub. But be careful before you try to implement one of those in your project.

A friend of mine once used a small open-source library in his commercial project because he liked few of its features. After one year he got stuck when he attempted to implement some advanced features. When he tried to contact the creator, he came to know that the project was long abandoned. I am sure that’s not going to happen with huge open-source projects like D3.js, Google Charts or morris.js, but it’s better to consider the possibility rather than repenting later.

Here’s a very good article that answers when a [commercial library makes sense over an open-source one](http://www.codeproject.com/Articles/581146/8-reasons-to-choose-commercial-library-instead-of).

These are all the factors that I think are important to know in order to make an informed choice. If you think I missed some factors, mention them in the comments.

![28f3c3faabcb35931cd9c9595bdf5e65.jpg](davidwalsh-name--13-factors-to-consider-while-choosing-a-javascript-charting-/28f3c3faabcb35931cd9c9595bdf5e65.jpg)

### About Vikas Lalwani

Vikas is a budding programmer who likes to have fun with front-end technologies. You can see some of his tiny experiments on his website. He works at FusionCharts and always available for a quick chat.

[lalwanivikas.github.io](http://lalwanivikas.github.io/)[lalwanivikas](http://twitter.com/lalwanivikas)[Posts](http://davidwalsh.name/author/vikaslalwani)
