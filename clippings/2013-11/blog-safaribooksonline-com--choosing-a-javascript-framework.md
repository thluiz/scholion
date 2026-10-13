---
url: "http://blog.safaribooksonline.com/2013/10/16/choosing-a-javascript-framework/?utm_source=javascriptweekly&utm_medium=email"
captured_at: "2013-11-10T22:28:23-03:00"
title: "Choosing a JavaScript Framework | Safari Books Online's Official Blog"
domain: "blog-safaribooksonline-com"
---

# **C**hoosing a JavaScript Framework

Posted on [October 16, 2013](http://blog.safaribooksonline.com/2013/10/16/choosing-a-javascript-framework/ "10:38 am")  by [Safari Books Online](http://blog.safaribooksonline.com/author/safaribooksonline/ "View all posts by Safari Books Online")

> *A guest post by Pam Selle, a web developer based in Philadelphia, PA**.** She speaks publicly anywhere from local user groups to international conferences on development topics including HTML/CSS, Ruby, Python, and JavaScript, and she also teaches web development and JavaScript, and can be reached via her blog at [thewebivore.com](http://www.thewebivore.com)  or on Twitter [@pamasaur](https://www.twitter.com/pamasaur) **.***

One of my favorite sayings these days is [Brendan Eich’s](https://brendaneich.com/)  “Always bet on JS**.**” So it’s not surprising that when people are starting new projects these days, they’re placing their bets on client-side development, rather than on server-side frameworks**.** The problem is, how do you choose? You can whittle it down to a few key factors**.**

## Always Consider What You Need First

It might seem obvious, but sitting down and creating a bulleted list of exactly what you need will help you narrow down your list of frameworks – chiefly because anything in a framework that you don’t need is cruft**.** Does it include a UI kit when you plan on writing your own front-end components**?** On a dependency side, don’t want to include jQuery**?** If your framework uses it as a dependency, guess you’re getting it anyway**.** If you haven’t seen it yet, read Pam’s [13 Criteria for Evaluating Web Frameworks](http://blog.safaribooksonline.com/2013/10/14/13-criteria-for-evaluating-web-frameworks/)  post before reading on**.**

Some frameworks are designed in a modular fashion so that you can choose what you need (the “only pay for what you get” concept)**.** That’s ideal, but not the case with all frameworks**.**

## Look For Backup

In a framework, you need to consider its maturity, documentation, and support**.** Who’s thrown money behind it (ex. when enterprise organizations started adopting Rails)**?** Are people patching it when vulnerabilities arise?

With JavaScript frameworks in particular, you should also weigh how much you’ll need to rely on support — for smaller frameworks/libraries, if it does what you need, then it’s something to consider**.**

Take for example the Twitter Flight library – it does one thing very well, that is, map behavior to DOM nodes (sounds like something pretty common, right**?**). It’s not a very widely adopted framework, however, it does have backing (Twitter), and it feels lightweight enough that if you had to you would likely be able to maintain it yourself**.** However, it does have jQuery and ES5-shim as dependencies, so be ready for that**.**

Writing Twitter Flight components is very simple, and part of its dependency on jQuery is that the binding will look quite familiar if you already know jQuery, and the library authors encourage using AMD to efficiently load library components when you need them (yay, modular**!**).

Here’s a sample component definition using Flight:

```
define(function (require) {
  // load component definition portion of the Flight library
  var defineComponent = require('flight/lib/component');

  // define the component
  return defineComponent(feed);

  function feed() {
    // define custom functions here
    this.doSomething = function() {
      //...
    }

    // now initialize the component
    this.after('initialize', function() {
      this.on('click', this.doSomething); // Very jQuery!
    });
  }
});
```

It’s not too large, and it’s definitely not difficult to understand**.** Read [The Twitter Flight Edge](http://my.safaribooksonline.com/9781939902030?iid=2013-10-blog-frameworks-book-9781939902030-SBOBlog&promocode=blog1999_1308)  for more on developing with Flight**.**

## What’s Your Team’s Background**?**

A major factor when choosing a framework will be how fast your team can get up to speed with something new to them**.** Let’s look at how we implement routes in Ember and Backbone:

### Ember

```
App.Router.map(function() {
  this.route("about", { path: "/about" });
  this.route("inbox", { path: "/inbox" });
});
```

The `map` reminds me of Ruby, and if you make the router a little more complicated, you’ll be using “`this.resource(...)`,” which is very Rails-esque.

### Backbone

```
var AppRouter = Backbone.Router.extend({
  routes: {
      "posts/:id": "getPost",
      "*actions": "defaultRoute"
  }
});
var app_router = new AppRouter;
```

Meanwhile, Backbone reminds me more of a standard JavaScript object; you define it and you need to make a “`new`” one when you’re ready to use it**.**

While Backbone is arguably less of a framework than Ember (Backbone is, after all, meant to form the “backbone” of a more fleshed out application, so many don’t count it among frameworks), the patterns in both will be very familiar to developers coming from a Ruby on Rails background**.**

Backbone, however, looks more like pure JavaScript, so purely RoR folks looking for a front-end framework are migrating towards Ember for a reason**.** The Ember router actually gives you some routes “for free” (i**.**e., they’re happening, but there’s no documentation of them in your code) for the root (/) level**.** That kind of style would be very familiar to someone coming from Rails (magic**!**), but possibly very annoying to someone coming from say, Python**.**

If your team can get up to speed very quickly, that’ll impact your decision**.** One framework known well for bucking traditional patterns is AngularJS**.** The best resource nowadays for AngularJS tutorials is [egghead**.**io](http://egghead.io/) , but there are [AngularJS](http://techbus.safaribooksonline.com/search?q=angularjs)  books in Safari Books Online**.**

AngularJS challenges the assumptions of other frameworks by creating bindings in the page — you can even invent new elements with specified behaviors (however, your CSS developers might not like that so much)**.** Angular is a great, fast, innovative, (and importantly) well-funded framework, but it has new patterns that are challenging to pick up on if you or your team can’t update your way of thinking**.**

## Conclusion

Choosing a framework is no simple matter – but if you want to focus during the process I definitely recommend focusing on these three factors: what you need, its backing, and how the framework does with your existing (or theoretical) team**.**

Be sure to look at resources on frameworks that you can find in Safari Books Online**.**

Not a subscriber? Sign up for a [free trial](https://ssl.safaribooksonline.com/trial?iid=2012-10-01-freetrial-SBOBlog&promocode=blog1999_1307) .

## Safari Books Online has the content you need

|  |  |
| --- | --- |
| [c290ff5c63bf722af62be7b0595bd2bb.jpg](http://my.safaribooksonline.com/9781449355852?iid=2013-10-blog-frameworks-book-9781449355852-SBOBlog&promocode=blog1999_1308) | [AngularJS](http://my.safaribooksonline.com/9781449355852?iid=2013-10-blog-frameworks-book-9781449355852-SBOBlog&promocode=blog1999_1308)  is a hands-on guide that introduces you to AngularJS, the open source JavaScript framework that uses Model–view–controller (MVC) architecture, data binding, client-side templates, and dependency injection to create a much-needed structure for building web apps**.** |
| [d8fd6b6f133cd8d4c58d7b49dd85f0a8.jpg](http://my.safaribooksonline.com/9781939902009?iid=2013-10-blog-frameworks-book-9781939902009-SBOBlog&promocode=blog1999_1308) | [Developing an AngularJS Edge](http://my.safaribooksonline.com/9781939902009?iid=2013-10-blog-frameworks-book-9781939902009-SBOBlog&promocode=blog1999_1308)  is intended for intermediate JavaScript programmers**.** No attempt has been made to explain the JavaScript syntax used (except in the cases where AngularJS may introduce a peculiarity), nor do we explain concepts such as closures, function chaining, callbacks, or other common patterns**.** What we do explain are basic AngularJS concepts, components, and their applications**.** We provide examples along the way, answer questions, and correct common misconceptions**.** Together, we’ll build a working single-page weblog application using AngularJS, which will help you become proficient with using AngularJS to go out and create your own applications**.** |
| [64560302adc7489e2b65e3ef83ed90a0.jpg](http://my.safaribooksonline.com/9781449328535?iid=2013-10-blog-frameworks-book-9781449328535-SBOBlog&promocode=blog1999_1308) | [Developing Backbone**.**js Applications](http://my.safaribooksonline.com/9781449328535?iid=2013-10-blog-frameworks-book-9781449328535-SBOBlog&promocode=blog1999_1308)  shows you how to get the job done with Backbone**.**js**.** You’ll learn how to create structured JavaScript applications, using Backbone’s own flavor of model-view-controller (MVC) architecture**.** |
| [df8ab700f759385e7c9641ce7b29c5fe.jpg](http://my.safaribooksonline.com/9781939902047?iid=2013-10-blog-frameworks-book-9781939902047-SBOBlog&promocode=blog1999_1308) | [Developing an Ember**.**js Edge](http://my.safaribooksonline.com/9781939902047?iid=2013-10-blog-frameworks-book-9781939902047-SBOBlog&promocode=blog1999_1308)  takes you from a casual interest in Ember**.**js through to building a complete application**.** Along the way we’ll cover the current state of client-side web development, the history and evolution of Ember, and the projects and challenges that have informed its design**.** Then we’ll dig deep into each of Ember’s constituent component libraries, demonstrating how each operates on its own and how they work together harmoniously as a framework**.** |

### About the author

|  |  |
| --- | --- |
|  | Pam Selle is a web developer based in Philadelphia, PA**.** She speaks publicly anywhere from local user groups to international conferences on development topics including HTML/CSS, Ruby, Python, and JavaScript**.** She also teaches web development and JavaScript in Philadelphia where she co-organizes a JavaScript user group**.** Contact her via her blog at [thewebivore.com](http://thewebivore.com)  or on Twitter [@pamasaur](https://twitter.com/pamasaur) **.** |

This entry was posted in [Content - Highlights and Reviews](http://blog.safaribooksonline.com/category/content-highlights-and-reviews/ "View all posts in Content - Highlights and Reviews") , [Programming & Development](http://blog.safaribooksonline.com/category/programming-development/ "View all posts in Programming & Development")  and tagged [AngularJS](http://blog.safaribooksonline.com/tag/angularjs/) , [Backbone**.**js](http://blog.safaribooksonline.com/tag/backbone-js/) , [Ember**.**js](http://blog.safaribooksonline.com/tag/ember-js/) , [Frameworks](http://blog.safaribooksonline.com/tag/frameworks/) , [Javascript](http://blog.safaribooksonline.com/tag/javascript/) , [Python](http://blog.safaribooksonline.com/tag/python/) , [RoR](http://blog.safaribooksonline.com/tag/ror/) , [Ruby on Rails](http://blog.safaribooksonline.com/tag/ruby-on-rails/) , [Twitter Flight](http://blog.safaribooksonline.com/tag/twitter-flight/) **.** Bookmark the [permalink](http://blog.safaribooksonline.com/2013/10/16/choosing-a-javascript-framework/ "Permalink to Choosing a JavaScript Framework") **.**

[← Celebrating Women in Science and Technology](http://blog.safaribooksonline.com/2013/10/15/celebrating-women-in-science-and-technology/)  |
[Updating to iOS 7: Getting Your Views Back →](http://blog.safaribooksonline.com/2013/10/17/updating-to-ios-7-getting-your-views-back/) 

### One Response to Choosing a JavaScript Framework

1. ![f2003d115880a99113698744d397ef47.jpg](blog-safaribooksonline-com--choosing-a-javascript-framework/f2003d115880a99113698744d397ef47.jpg) Lukas Bünger says:

   [October 19, 2013 at 6:15 am](http://blog.safaribooksonline.com/2013/10/16/choosing-a-javascript-framework/#comment-186801)

   Nice read**!**  
   However, the assumption that “One framework known well for bucking traditional patterns is AngularJS” is a bit misleading**.** If your refer to traditional in terms of established Javascript techniques it is valid to a certain extent**.** Otherwise, AngularJS comes with loads of features that I’d definitely expect from a mature framework, no matter what language or context it addresses**.** IMHO for example dependency injection is a critical must for anything that claims to be even halfway decent and the fact that none of the other (mentioned) solutions comes with DI makes them the bucks IMHO**.**  
   But again, very good introduction to the problem domain**.**

   Regards!

   [Reply](http://blog.safaribooksonline.com/2013/10/16/choosing-a-javascript-framework/?utm_source=javascriptweekly&utm_medium=email&replytocom=186801#respond)

### Leave a Reply [Cancel reply](http://blog.safaribooksonline.com/2013/10/16/choosing-a-javascript-framework/?utm_source=javascriptweekly&utm_medium=email#respond)

Your email address will not be published**.** Required fields are marked \*

Name \*

Email \*

Website

Comment

You may use these HTML tags and attributes: `<a href="" title=""> <abbr title=""> <acronym title=""> <b> <blockquote cite=""> <cite> <code> <del datetime=""> <em> <i> <q cite=""> <strike> <strong>`

Notify me of follow-up comments by email**.**

Notify me of new posts by email**.**
