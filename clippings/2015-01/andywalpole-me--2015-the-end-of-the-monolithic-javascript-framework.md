---
url: "https://andywalpole.me/#!/blog/142134/2015-the-end-the-monolithic-javascript-framework"
captured_at: "2015-01-16T09:54:57-03:00"
title: "2015: The End of the Monolithic JavaScript Framework / blog unblock"
domain: "andywalpole-me"
---

# 2015: The End of the Monolithic JavaScript Framework

Andy Walpole / Category: [JavaScript](https://andywalpole.me/#!/category/javascript) / Jan 15, 2015 / words

***tl;dr**: We need to move beyond monolithic frameworks to a component/library-based front-end solution, but there’s too much fragmentation/abstraction to create an industry standard approach. Below are some constructive thoughts aimed at building a more viable and stable alternative.*

Arguably, the front-end layer of the web stack has, in recent years, seen a greater pace of change than any other.

This has been led, primarily, by an aggressively ambitious feature expansion roadmap by the four major competing browsers: Chrome, Safari, Firefox and Internet Explorer.

It is no coincidence that the era of front-end permanent revolution only came about after Internet Explorer’s monopoly was smashed by the arrival of Chrome in 2008.

#### JavaScript

The front-end code troika are CSS, HTML and JavaScript; the latter is most subject to incessant change. For years, JavaScript languished in stasis. During the last decade, the only major development was the adoption of AJAX that uses the XMLHttpRequest object for client–server communication, but this originated in a browser feature first introduced in Internet Explorer 5.

Since then, the pace of JavaScript expansion has increased in two different ways.

In 2009 the overseeing standards body, [Ecma International](https://en.wikipedia.org/wiki/Ecma_International), introduced their first new version, [ECMAScript 5](http://www.ecma-international.org/ecma-262/5.1/), in over ten years. This was quickly followed by ECMAScript 6, currently [partially implemented in the evergreen browsers](https://kangax.github.io/compat-table/es6/) and due to be finalised sometime in 2015. [Public discussion has already begun on ECMAScript 7](https://drive.google.com/file/d/0B4PVbLpUIdzoUjdmSkFtVVozQnM/view).

The second area of expansion comes under the catch-all banner of HTML5. There is now a multitude of new APIs to utilise. I have used, at some point over the last 12 months, the following: [File API](https://developer.mozilla.org/en-US/docs/Using_files_from_web_applications); [FileReader API](https://developer.mozilla.org/en-US/docs/Web/API/FileReader); [Full Screen API](https://developer.mozilla.org/en-US/docs/Web/Guide/API/DOM/Using_full_screen_mode); [Cross-Origin Resource Sharing](https://dev.opera.com/articles/dom-access-control-using-cors/); [Page Visibility](https://developer.mozilla.org/en-US/docs/Web/Guide/User_experience/Using_the_Page_Visibility_API); [Web Workers](https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API/basic_usage) and [Base64 encoding and decoding](https://developer.mozilla.org/en-US/docs/Web/API/WindowBase64.atob). There are dozens more in existence, all with varying degrees of browser support.

#### JavaScript Frameworks

Harnessing the power of contemporary JavaScript has seen arrival of the model–view–controller (MVC) JavaScript framework. The MVC architectural pattern for these frameworks is interpreted far more loosely than server-side MVC frameworks, with all variants commonly abbreviated to MV\*.

The first framework to be widely commercially used was [Backbone.js](http://backbonejs.org/). Created by [Jeremy Ashkenas](https://twitter.com/jashkenas), who also authored [CoffeeScript](http://coffeescript.org/), its initial public release came in the autumn of 2010.

Here are some positive Twitter reactions from the succeeding 12 months:

Backbone.js was the first but its meta-framework approach left space for a newer generation of full-frameworks - the most notable being [Ember.js](http://emberjs.com/) and [AngularJS](https://angularjs.org/) - to gain rapid traction among developers, as these positive tweets testify:

Today, AngularJS’s popularity far exceeds that of any other framework, although Ember.js has a healthy, vibrant community of contributors and users. I suspect, 2015 will witness an increase in Ember’s popularity due to the controversial Angular roadmap.

AngularJS, commonly referred to as just Angular, was originally conceived by [Adam Abrons](https://github.com/abrons?tab=repositories) and [Miško Hevery](http://misko.hevery.com/); the latter continued the project at Google. More programmers were added freely as it grew in both project scope and popularity.

[In this interview from 2011, Miško explains how he views the Angular approach to building single-page applications:](http://jaxenter.com/deep-dive-into-web-architecture-103268.html)

> Angular in a way acts as a polyfill or a shim to give the browser the vocabulary which is useful for building web-applications.

> A lot of what a web-application code must do is DOM manipulation to present the data to the user. DOM manipulation code is around 80% of application code. Angular lets you declare the way the internal state (model) is projected to the DOM, which means that your application code can skip writing the DOM manipulation code, and having to write 80% of code is a huge saving. The result is that an application written with Angular is significantly shorter, and as a result easier to maintain.

Generally speaking, compared to Backbone, far fewer lines of code are written when using Angular; although depending on the complexity of the project, this doesn’t necessarily mean less development time. Although all the main JavaScript (JS) frameworks have many similarities, Angular differs from the rest in its use of dirty checking, an in-depth description of which can be [read in the official documentation](https://docs.angularjs.org/guide/scope).

Angular dates back to 2009 but the vast majority of Angular developers have only been using the framework over the last couple of years. Originally conceived as a means to assist non-web developers with creating applications, its complexity means it is a tool for seasoned developers only.

One noticeable unintentional consequence of the rise of the front-end framework is an influx of server-side programmers to the front-end. These programmers bring with them, I would argue, more hardened approaches to the web build, especially in the areas of test-driven development (TDD) and design patterns (although they do have some annoying habits like insisting on using Twitter Bootstrap).

This isn’t an article detailing Angular’s strengths and weaknesses, but when a giant news publication such as [The Guardian](http://www.theguardian.com/) switches to Angular, it’s clearly a sign of a mature project that is able to scale to the most demanding of commercial environments.

In 2014, the Angular team [went public with their plans for AngularJS 2.0](http://jaxenter.com/angular-2-0-112094.html). This important version will be a complete rewrite of the codebase, with no backwards compatibility to the 1.x line of releases.

With important new browser features like Web Components just around the corner, the Angular team felt that this was the only option open to them. Such a revolutionary roadmap elicited many hostile responses, with the quotes below taken from a [Reddit thread](https://www.reddit.com/r/programming/comments/2kl88s/angular_20_drastically_different/). A lot of the comments are unnecessarily dramatic due to a misunderstanding of the rationale behind the planned changes, but those highlighting a lack of backwards compatibility in a corporate environment are right to be concerned:

> This is a mess. The syntax looks like hot shit, and the huge gap between this and 1.3 means those of us with real jobs where projects live for years and years have to back off. I can’t tell my boss that we’re going to build something incredible, but that we need to plan for a code only, no new features rewrite in 18 months.

> I work for a moderately large company (2,000 people) and were rolling out a new web experience to replace all our old text based systems this weekend. I've backed angular the whole way and its been lovely to work with - the entire UI is written in it. This news is incredibly unfortunate, inconvenient and potentially expensive.

> The old systems have been running for over 15 years without breaking version to version, and even survived a Solaris to Linux migration. Meanwhile I can't even get a year out of an app before it's superseded with no migration path. Unreal.>

Regardless of your opinion of Angular 2.0 (and there are many good reasons why it should be completely rewritten), this episode has highlighted the dangers of investing time and resources into a single monolithic framework with corporate stewardship. Google’s leadership of the project has led to dozens of full-time developers being deployed on the project, but Google is a business with its own unique set of requirements; it would be hard to think of a non-Google-based open software project that considers [Dart](https://www.dartlang.org/) important enough to create a new language, [AtScript](https://docs.google.com/document/d/11YUzC-1d0V1-Q3V0fQ7KSit97HnZoKVygDxpWzEYW0U/mobilebasic?viewopt=127&pli=1), which compiles into both JavaScript and Dart.

This is the fatal point of weakness inherent in the one-stop solution. Facing the prospect of learning - from scratch - a new front-end framework (which is what, according to current plans, Angular 2.0 will be), some voices have openly expressed weariness at the permanent revolution being forced on front-end developers.

In London, companies are dependent on contract labour. In 2013–2014, it was almost impossible to recruit seasoned Angular developers, but the recruitment landscape has become slightly more amenable in recent months.

When Angular 2.0 is finally launched, companies will once again face the strenuous task of recruiting candidates who can work within the new framework.

Jimmy Breck-McKye penned an article, [*The State of JavaScript in 2015*](http://www.breck-mckye.com/blog/2014/12/the-state-of-javascript-in-2015/), in the closing weeks of 2014:

> Innovation is great, but this kind of churn rate seems excessive. It’s just not possible for developers to make large, upfront investments of time in getting to grips with new frameworks and technologies when there’s no guarantee of their longevity. Programmers want to program – they want to build things, and be masters of their craft. But how can we get anything done when we’re spending most of our time learning? How can we feel like craftsmen when we’re scrabbling in the dark with unfamiliar tech?

One solution presented by Jimmy was to “Prefer dedicated libraries to monolithic frameworks” because:

> When you choose a framework, you make a large, long term commitment. You sign up to learn about the framework’s various inner workings and strange behaviours. You also sign up to a period of ineffectiveness whilst you’re getting to grips with things. If the framework turns out to be the wrong bet, you lose a lot. But if you pick and choose from libraries, you can afford to replace one part of your front end stack whilst retaining the rest.

[Cody Lindley](http://www.codylindley.com/), author of [*JavaScript Enlightenment*](http://www.javascriptenlightenment.com/) and [*DOM Enlightenment*](http://www.domenlightenment.com/) among much else, was more curt on this subject in these two tweets:

Joe Gregorio’s well-read article, [*No more JS frameworks*](http://bitworking.org/news/2014/05/zero_framework_manifesto), contributed to the debate on full-framework over reliance. And it is from Joe that I take the phrase ‘zero framework manifesto’.

#### Building a Zero Framework Manifesto

Combining several different non-proprietary software licensed projects mitigates the possibility of reliance on one multi-purpose framework. If a component is discontinued or the direction of the roadmap is radically changed, that project could, with relative ease, be replaced with another similar non-proprietary software project.

There are, though, several dangers to this approach.

The first is of agency/corporate siloing. With so many front-end open source/free projects to choose from, each development house could be building their own tailored framework. To a certain extent, this is favourable, but too much diversity - and in particular, abstraction - will affect the ability to recruit, retain and train staff.

Another issue is maintainability. Rather than code coming from one trusted source, the use of multiple projects would require constant code reviewing with each new release.

If a component-based approach is widely adopted, the industry needs to subscribe to a manifesto of common purpose. Below are some ideas.

**1. Corporations need to give and not just take.**

Today, non-proprietary software is the backbone of every layer of the web stack in the majority of corporate IT departments. One major issue facing all these projects is that corporate users are quick to magpie the software released under a permissive BSD, MIT or Apache License 2.0 licence, and then fail to contribute, in turn, any modified code back, or to even share their gained knowledge through blog posts or talks. Legally, under these licences, that is their entitlement; ethically, they are in the wrong. Permissive legal licences, such as those listed above, allow open source software to be interpreted as “free beer”, damaging the fragile cooperative ecosystem that sustains them.

Either companies need to have a serious ethical rethink or we should abandon permissive legal licences, using the GPL licence to force code-sharing. This is, as far as I understand, the fundamental dividing line that Richard Stallman claims makes free software different from open software.

**2. Avoid over-abstraction.**

Through simplicity comes great power and maintainability. Simplicity, in the framework of this article’s discussion, means adhering to the JavaScript spec as standardised by Ecma International. [This is the draft of version 6](https://people.mozilla.org/~jorendorff/es6-draft.html).

There has been a trend towards creating JavaScript subset languages that transcompile on runtime to browser-friendly JS.

React uses JSX to allow that framework to be accessible to “casual developers such as designers”. Angular 2.0 will use ATScript which transcompiles into both JS and Dart. CoffeeScript offers only syntactic changes - little more than putting lipstick on a pig. The most interesting of them all is TypeScript, which offers features common to other programming languages but that are absent from JavaScript: types, classes and interfaces.

Three of the four listed above were conceived and are maintained by three large web-based corporations, initially for internal use but then released under licence to all developers.

With ES6 just around the corner, the attraction of using JS subsets has become less alluring.

**3. Use [Isomorphic JavaScript](http://isomorphic.net/).**

There needs to be a dual server-side and client-side solution to enable razor-sharp performance. If you are unconvinced that performance doesn’t matter in 2015, then I would encourage you to read [*Slow Pages Damage How Users Perceive Your Content, Design, and Navigation*](http://calendar.perfplanet.com/2013/slow-pages-damage-perception/) by [Tammy Everts](http://www.webperformancetoday.com/).

**4. A clear separation of concerns.**

Having grown used to Angular’s extensive use of logic in the template, it now seems far more natural than initially indicated by my initial shock when first seeing inline JavaScript during my Angular introductory days. Like any platform, one adapts and makes the best use of a feature, but keeping logic out of the view should be a priority.

**5. No dependencies.**

Any choice of third-party libraries must be standalone and not dependent on another library (although there is a difference between “plays nicely with” to “this requires the use of”).

**6. Using an ES6 compiler.**

Personally, I’m uncomfortable with using an ES6 to ES5 compiler like [Traceur](https://github.com/google/traceur-compiler) or [6to5](https://6to5.org/). These are ‘black boxes’ that swallow code in one end and spit a different version out the other; if the aim, however, is to avoid using JS subsets, then writing in standard-compliant ES6, which is then changed to standard-compliant ES5, is in the scope of the manifesto.

I’m waiting for an opportunity to embrace Traceur or 6to5 on a forthcoming project before I can properly evaluate them.

#### Some Library Suggestions

The list below comprises recipe parts pointing towards a fully baked solution; it is the equivalent of me going through the cupboards and fridge and placing the ingredients I like the most onto the table. Subscribing to the maxim of “absolute criticism of all things existing”, I don’t uncritically endorse any single one of these projects, but they are good starting points for initial investigation.

##### Helper Libraries

[**moment.js**](http://momentjs.com/): an invaluable tool for date and time cross-browser standardisation.

[**underscore.js**](http://underscorejs.org/) **/** [**Lo-Dash**](https://lodash.com/): widely used for years, these libraries are considered essential for functional programming in JavaScript. Do we really need a full library anymore? Perhaps it’s better to pick the function polyfills required from the [Mozilla Development Network](https://developer.mozilla.org/en-US/).

##### Routing

[**router.js**](https://github.com/tildeio/router.js/): router.js is the micro-library used in Ember.js.

[**route-recognizer**](https://github.com/tildeio/route-recognizer): recommended as a “recognizer for a more comprehensive router system (such as router.js)”.

[**page.js**](https://github.com/visionmedia/page.js): directly inspired by Node’s well-used Express library.

[**director**](https://github.com/flatiron/director): a comprehensive, isomorphic routing solution. Read through the thorough documentation and code examples.

##### Promises

[**RSVP.js**](https://github.com/tildeio/rsvp.js): an ES6-compliant library with “some extra toys”.

[**ES6-Promise**](https://github.com/jakearchibald/es6-promise): a subset of RSVP.js, but fully compliant with the ES6 spec.

[**q**](https://github.com/kriskowal/q): one of the most popular promises libraries, a stripped-down version of q is used in AngularJS.

[**native-promise-only**](https://github.com/getify/native-promise-only): like ES6-Promise the intention of this project is to be “a polyfill for native ES6 Promises as close as possible (no extensions) to the strict spec definitions”.

##### Client–Server Communication

[**fetch**](https://github.com/github/fetch): a polyfill for window.fetch.

[**qwest**](https://github.com/pyrsmk/qwest): an “Ajax library with XHR2, promises and request limitation”.

[**jQuery**](https://github.com/jquery/jquery): from version 2.0 onwards, it is now possible to build your own jQuery component-based library; this leaves open the possibility of creating a slimmed-down AJAX-centred version.

##### Animation

[**cssanimevent**](https://github.com/magnetikonline/cssanimevent): a “Cross browser compatible library to handle CSS3 animation and transition DOM events with a fallback pattern for unsupported browsers”.

[**Velocity.js**](http://julian.com/research/velocity/): this JS animation library, created by Julian Shapiro, received a lot of attention last year and now has a loyal user-base.

##### Development Assistance

[**LogJS**](https://github.com/bfattori/LogJS): a lightweight JavaScript logging platform.

[**UserTiming.js**](https://github.com/nicjansma/usertiming.js): UserTiming is a polyfill that extends support to all common browsers.

##### Flow Control/Architecture

[**ondomready**](https://github.com/tubalmartin/ondomready): “An AMD compatible module to detect when the DOM is ready”. Based on jQuery’s ready() method.

[**script.js**](https://github.com/ded/script.js]): “Asyncronous JavaScript loader and dependency manager”.

[**async**](https://github.com/caolan/async): a comprehensive set of asynchronous utilities for both the browser and node.js.

[**Virtual DOM**](https://github.com/Matt-Esch/virtual-dom): a viable alternative to react.js. For a full explanation, read the article [*Virtual DOM and diffing algorithm*](https://gist.github.com/Raynos/8414846).

Data-binding/Object.observe(): there was much more enthusiasm for two-way data-binding a year ago, but some criticisms have now surfaced. Object.observe is now supported in Chrome but not, currently, in any other browser.

##### Templating

[**Mustache**](http://mustache.github.io/): quite possibly the most popular “logic-less” templating system in current use.

##### Micro-Frameworks

It may be worth considering using a micro-framework as a starting point:

[**bottlejs**](https://github.com/young-steveo/bottlejs): “BottleJS is a tiny yet powerful dependency injection container. It features lazy loading, middleware hooks, decorators and a clean api inspired by the AngularJS Module API and the simple PHP library Pimple”.

[**Stapes.js**](http://hay.github.io/stapes/#top): a tiny MVC framework. From looking at GitHub submits, it hasn’t received much attention over the past year.

[**soma.js**](http://somajs.github.io/somajs/site/): “soma.js is a set of tools and design patterns to build a long term architecture that are decoupled and easily testable. The tools provided by the framework are dependency injection, observer pattern, mediator pattern, facade pattern, command pattern, OOP utilities and a DOM manipulation template engine as an optional plugin”.

[**knockout**](http://knockoutjs.com/): the most popular, well-maintained of all those in this list, but one that is focused on the UI interface, using the Model View ViewModel architectural pattern.

The above is not an exhaustive list; I haven’t even covered TDD or Web Components.

#### Follow the Way of the Zero Framework Manifesto

It’s not merely enough to collate your own personal preferences into one system; there needs to be an industry-wide approach to an industry-wide problem.

Here are some questions you can ask when choosing a library:

\* How maintainable will this project be? If somebody else inherited your code tomorrow after you were run over by a bus, how quickly could they master your code?  
\* Do any of the individual components adversely affect performance? If so, do they do so unnecessarily? Can this be changed by a pull-request/fork?  
\* Do any of the components adversely affect accessibility? Can these be fixed by pull-requests/forking?  
\* How open are the developer(s) of the components to code contributions? How quick are they to respond to queries in their GitHub connected issues section? Running an open/free software project can be extremely time-consuming, and although many start out with the best of intentions, most quickly become burnt-out and disillusioned.

To recap: write JavaScript, not somebody else’s interpretation of what JavaScript should be; use non-proprietary software, but give back what you take; be very, very suspicious of the “next big thing” receiving publicity on Twitter; aim for simplicity, avoiding unnecessary complexity; keep talking and writing - we need a conversation about this. We are all in it together.
