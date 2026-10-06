---
url: "http://adamrenklint.com/guides/getting-started-with-kranium-js-a-brilliant-framework-for-titanium-mobile"
captured_at: "2012-06-09T02:37:33-03:00"
title: "Getting started with Kranium.js – a brilliant framework for Titanium Mobile – Adam Renklint, application developer"
domain: "adamrenklint-com"
---

[FEEDBACK](http://adamrenklint.com/guides/getting-started-with-kranium-js-a-brilliant-framework-for-titanium-mobile#)

## Adam Renklint

## Application developer

- Scroll to top
- Contact me
- Search
- Subscribe to feed

- ### [Guides](http://adamrenklint.com/guides "View all posts in Guides")
- ### October 2011

### Share post

- [Facebook](http://www.facebook.com/sharer.php?s=%20100&amp;p[title]=Getting%20started%20with%20Kranium.js%20%E2%80%93%20a%20brilliant%20framework%20for%20Titanium%20Mobile&amp;p[url]=http://adamrenklint.com/guides/getting-started-with-kranium-js-a-brilliant-framework-for-titanium-mobile&amp;p[summary]=At%20Codestrong,%20the%20first%20official%20conference%20for%20Titanium%20Mobile%20developers%20in%20SF%20a%20few%20weeks%20ago,%20fellow%20swede%20Jacob%20Waller%20presented%20his%20latest%20project%20-%20one%20awesome%20app%20framework%20built%20on%20the%20previous%20success%20of%20Livetanium%20and%20web%20techniques%20like%20Sizzle,%20Backbone.js%20and%20Jasmine.%20Here's%20a%20short%20introduction%20to%20the%20concept%20to%20get%20you%20started.)
- [Twitter](http://twitter.com/home?status=Getting%20started%20with%20Kranium.js%20%E2%80%93%20a%20brilliant%20framework%20for%20Titanium%20Mobile%20-%20http://adamrenklint.com/guides/getting-started-with-kranium-js-a-brilliant-framework-for-titanium-mobile)
- [StumbleUpon](http://www.stumbleupon.com/submit?url=http://adamrenklint.com/guides/getting-started-with-kranium-js-a-brilliant-framework-for-titanium-mobile&amp;title=Getting%20started%20with%20Kranium.js%20%E2%80%93%20a%20brilliant%20framework%20for%20Titanium%20Mobile)

- [Custom action methods in a few simple steps](http://adamrenklint.com/guides/custom-action-methods-in-a-few-simple-steps) May 2011
- [Use custom element types to get more out of the type selector](http://adamrenklint.com/guides/use-custom-element-types-to-get-more-out-of-the-type-selector) May 2011
- [Ideas for Adamantium.js 0.2](http://adamrenklint.com/thoughts/ideas-for-adamantium-js-0-2) May 2011
- [Adamantium.js - chainable mobile app framework with jQuery-like syntax](http://adamrenklint.com/projects/adamantium-js) April 2011
- [Create a basic model with Titanium Mobile](http://adamrenklint.com/guides/create-a-basic-model-with-titanium-mobile) November 2010

# [Getting started with Kranium.js – a brilliant framework for Titanium Mobile](http://adamrenklint.com/guides/getting-started-with-kranium-js-a-brilliant-framework-for-titanium-mobile "Permanent Link to Getting started with Kranium.js – a brilliant framework for Titanium Mobile")

**At Codestrong, the first official conference for Titanium Mobile developers in SF a few weeks ago, fellow swede Jacob Waller presented his latest project – one awesome app framework built on the previous success of Livetanium and web techniques like [Sizzle](http://sizzlejs.com/), [Backbone.js](http://documentcloud.github.com/backbone/) and [Jasmine](http://pivotal.github.com/jasmine). Here’s a short introduction to the concept to get you started.**

## So what is Kranium.js?

> “The result of merging Titanium with web development techniques, creating a cyborg which is greater than just the sum of its parts. It will significantly speed up development and styling, and is useful both for prototyping and production apps.”  
> [From Kranium.js Codestrong intro](http://codestrong.com/sessions/webifying-titanium-development "From Kranium.js Codestrong intro")

> “Kranium has enough brains to let your brain focus on the crucial stuff while developing Titanium Mobile apps. Kranium transfers some well known practices and techniques from web development to Titanium Mobile development. It’s both spiritually and physically the lovechild of [...] great web tech.”  
> [From kraniumjs.com](http://www.kraniumjs.com/)

## Components

Kranium.js tries to simplify UI component creation and promote a clean modular pattern, which works very well for mobile apps.

```
// Vanilla Titanium Mobile example from kraniumjs.com
var tabGroup = Ti.UI.createTabGroup(),
    win1 = Ti.UI.createWindow({
        backgroundColor: '#ccc',
        barColor: '#00a',
        title: 'My window'
    }),
    tab1 = Ti.UI.createTab({
        icon: 'path/to/my/icon',
        title: 'My tab',
        window: win1
    }),
label1 = Ti.UI.createLabel({
    text: 'Hello world!',
    textAlign: 'center',
    color: '#333',
    shadowColor: '#fff',
    shadowOffset: {
        y: -1,
        x: 0
    },
    font: {
        fontSize: 20,
        fontWeight: 'bold'
    }
});
win1.add(label1);
label1.addEventListener('click', function(e){
    alert('You clicked me!');
});
tabGroup.addTab(tab1);
tabGroup.open();
```

Kranium.js cleans this up nicely and provides a very readable structure for creating deep objects.

```
// Example from kraniumjs.com
K({
    type: 'tabgroup',
    tabs: [{
        cls: 'myTab',
        window: {
            cls: 'myWindow',
            children: [{
                text: 'Hello world!',
                cls: 'mylabel',
                click: function(){
                    alert('You clicked me!');
                }
            }]
        }
    }]
}).open();
```

## Extending components

Our re-usable components are stored in a folder kalled **kui** and custom components will be lazily autoloaded when needed. You can easily extend your app with custom components using the CommonJS module pattern and then easily create new instances of this custom component.

When creating components, I would suggest using a strong namespace pattern. I’m a fan of the Cocoa style naming, so my subclass of Label would in this example be called ARLoginStatusLabel – better to have a longer name that actually explains the components purpose.

```
// kui/ARLoginStatusLabel.js
exports.Class = Label.extend({
    init: function(opts) {
        this.events = {
            app: {
                authchange: this.updateStatus.bind(this)
            }
        };
        this.updateStatus();
        this._super.call(this, opts);
    },
    updateStatus: function(e){
        this.text = "Logged " + (e && e.loggedIn ? "in" : "out");
    }
});
// Instantiate in another file
var label = K.create({
    type: "ARLoginStatusLabel"
});
```

## Use CSS to style components

Kranium.js ships with it’s own take on a CSS port for Titanium Mobile, which is actually pretty competent. Using the **kranium init** or **kranium watch** commands in Termninal will start an auto-compiler service for Sass, LESS and CoffeeScript files, with optional live in-app updating through sockets.

```
window {
        background-color: #777;
        barColor: #333;
}
.alert {
        background-color: #f00;
}
```

## Queries with Sizzle

One thing I have worked hard on the past months is Adamantium.js, an idea that came from missing the query selector pattern, coming from web development. Kranium.js uses a modified version of the well-known Sizzle engine and emulates the DOM in a natural way.

```
$("window").bind("open", function (e) {
        alert("A window was opened");
        K.log(e.source);
});
```

It appears that support for pseudo selectors is lacking and all Sizzle filter methods are not yet implemented, but I think that will change over the coming months. I hope to be able to contribute, maybe through another open source library.

## Console and Jasmine testing

As if it wasn’t enough, Kranium.js also comes with a Jasmine BDD integration and a localhost console – these two features will really improve any app development cycle and I hope I get to use this a lot.

## How to install

Okey, so the only thing left now is to install Kranium.js and download the [demo application](https://github.com/krawaller/kranium-demo). If you don’t have NodeJS installed, [download and install it first](https://github.com/joyent/node/wiki/Installation "NodeJS"). Then [install the Kranium.js](http://kraniumjs.com/#h-installation "Kranium.js installation guide") command line tool by running sudo npm install kranium -g in your terminal and use kranium –version to verify installation.

I look forward to testing Kranium.js during the coming weeks, but I have to say that I am so far very impressed. This looks promising and I hope to be able to contribute.

- #### [Kranium.js](http://adamrenklint.com/tag/kraniumjs)
- #### [Titanium Mobile](http://adamrenklint.com/tag/titanium-mobile)

[[anexo ausente]](http://disqus.com/)

[anexo ausente]

[Sharry](http://www.learningtitanium.com/)

6 months ago

[http://www.learningtitanium.co...](http://www.learningtitanium.com/software/frameworks/getting-started-with-kranium-js-framework.html)

[hide 2 replies](http://adamrenklint.com/guides/getting-started-with-kranium-js-a-brilliant-framework-for-titanium-mobile# "Collapse thread") [reply](http://adamrenklint.com/guides/getting-started-with-kranium-js-a-brilliant-framework-for-titanium-mobile#)

[anexo ausente]

Adam Renklint

6 months ago

Nice! One thing though, the Twitter link at the end of the article is wrong.

[hide 1 reply](http://adamrenklint.com/guides/getting-started-with-kranium-js-a-brilliant-framework-for-titanium-mobile# "Collapse thread") [reply](http://adamrenklint.com/guides/getting-started-with-kranium-js-a-brilliant-framework-for-titanium-mobile#)

[anexo ausente]

[Sharry](http://www.learningtitanium.com/)

6 months ago

Thanks.  Updated twitter link, sorry about that.

[reply](http://adamrenklint.com/guides/getting-started-with-kranium-js-a-brilliant-framework-for-titanium-mobile#)

[anexo ausente]

NaneNare Hambardzumyan

6 months ago

Hi Adam   
Please help me  
I want use this but when I include it in app.js my appcelerator geting error in this file.

[hide 1 reply](http://adamrenklint.com/guides/getting-started-with-kranium-js-a-brilliant-framework-for-titanium-mobile# "Collapse thread") [reply](http://adamrenklint.com/guides/getting-started-with-kranium-js-a-brilliant-framework-for-titanium-mobile#)

[anexo ausente]

Adam Renklint

6 months ago

Hi, afraid I can't help you with such a short description of the problem. Could you expand on what is happening and what error message you are receiving?

[reply](http://adamrenklint.com/guides/getting-started-with-kranium-js-a-brilliant-framework-for-titanium-mobile#)

[anexo ausente]

QuentinC

6 months ago

Hi Adam,

I'm exploring existing Titanium frameworks, maybe we'll want to use one someday to simplify all Ti.UI.createStuff boilerplate code

How do you see things going forward ? Do you plan on improving Adamantium or contributing on Kranium ? I haven't had a chance to play with those frameworks so I'm curious about the differences.

Also I see that TiFramework now points to your framework Adamantium, but [http://wiki.appcelerator.org/d...](http://wiki.appcelerator.org/display/guides/Third-party+Tools#Third-partyTools-UtilityLibraries) doesn't mention Adamantium...

Thanks !

[hide 1 reply](http://adamrenklint.com/guides/getting-started-with-kranium-js-a-brilliant-framework-for-titanium-mobile# "Collapse thread") [reply](http://adamrenklint.com/guides/getting-started-with-kranium-js-a-brilliant-framework-for-titanium-mobile#)

[anexo ausente]

Adam Renklint

6 months ago

Hey Quentin,  
thanks for the comment. Right now, I am knee deep in writing a completely new version of Adamantium.js, leveraging parts of Kranium.js but also offering a more stable and fun application framework.  
So, while I hope to contribute to Kranium in whatever capacity I can, my main focus is on creating the full-featured framework that I need myself for mobile development - hopefully it can be of help to anyone else who wants to build awesome apps, really fast, with a syntax and workflow similar to web.  
Before the year has ended, Adamantium.js 1.0 will be released in open beta...  
Cheers from Berlin, Adam

[reply](http://adamrenklint.com/guides/getting-started-with-kranium-js-a-brilliant-framework-for-titanium-mobile#)
