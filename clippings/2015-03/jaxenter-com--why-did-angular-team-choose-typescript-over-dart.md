---
url: "http://jaxenter.com/angular-typescript-dart-115426.html"
captured_at: "2015-03-13T09:56:20-03:00"
title: "Why did the Angular team choose TypeScript over Dart? - JAXenter"
domain: "jaxenter-com"
---

# Why did the Angular team choose TypeScript over Dart?

Natali Vlatko

![4623eebcca8411810955ca71862b21a9.jpg](jaxenter-com--why-did-angular-team-choose-typescript-over-dart/4623eebcca8411810955ca71862b21a9.jpg)

[Post-its](http://www.shutterstock.com/pic-224142373/stock-photo-two-notes-stuck-on-message-cork-board-with-smiley-and-sad-cartoon-face-expression-in-happiness.html?src=Yt6hd3wPurUyZENxqVcWtg-1-7) image via Shutterstock

What has TypeScript got going for it that won the Angular team over? Aren’t Google using Dart internally anyway? What’s the deal with the comparisons? We try our luck at dissecting the issue of Angular’s recent TypeScript coalition.

When you’re looking at JavaScript alternatives, TypeScript and Dart often spring to mind. With the recent [hoopla](http://jaxenter.com/angular-2-0-announcement-backfires-112127.html) over Angular 2.0 making the rounds, the decision to go with TypeScript over Dart has been met with much contention and debate.

The question has [already been posted](http://www.reddit.com/r/dartlang/comments/2y4ady/why_typescript_and_not_dart_for_angular_2/) on Reddit, and some users on Hacker News are now looking to move on from Angular altogether as a result of their TypeScript alliance. So what are the reasons behind the Angular and TypeScript pairing?

### Microsoft and Google are now buddies

The [recently announced](http://jaxenter.com/google-announces-new-approach-angular-2-0-115228.html) collaboration between Microsoft and Google marked the end of AtScript, the short-lived ‘syntax sugar’ that Angular 2.0 was wanting to introduce. Instead, the Angular team will be incorporating TypeScript, which S. Somasegar, the Corporate Vice President of the Developer Division Microsoft, [reported on](http://blogs.msdn.com/b/somasegar/archive/2015/03/05/typescript-lt-3-angular.aspx) earlier in the month.

The partnership is a big deal to both sides, with Microsoft able to work on bettering TypeScript and allowing wider use, while Google are able to satisfy their own userbase who are (for the most part) firmly entrenched in JavaScript already. As Redditor [the\_hoser](http://www.reddit.com/user/the_hoser) states:

> As nice as Dart is, TypeScript wins because, at the end of the day, they both have to appeal to existing web developers. These developers, nearly without exception, use JavaScript. Their skills do not cleanly translate to Dart like they do to TypeScript. By virtue of not simply being a better JavaScript, Dart lost.

Many users have also commented on Dart’s goal, saying that is should not be to replace JavaScript, but to exist alongside it.

### Is Dart unmanageable for big and complex stuff?

Jeff Walker recently [blogged](http://www.walkercoderanger.com/blog/2014/03/dart-isnt-the-answer/) about Dart’s problems, highlighting the special interop library that exposes wrapped versions of any JavaScript objects you access. While it enables Dart to “safely sandbox JavaScript away and prevent its problems from leaking into a Dart application”, Walker believes this tends to ‘silo’ you into the specific platform that you’re working with:

> Currently, many new and exciting JavaScript libraries are being released and the Dart platform is immature and hasn’t had time to fill out with all the options a developer might want. Being siloed into the Dart platform will be a very high price to pay to avoid the JavaScript minefield.

Redditor [zoechi](http://www.reddit.com/user/zoechi) also had something to say about Dart’s manageability:

> Would they build Angular in Dart it wouldn’t be possible to use it in JavaScript applications. Dart builds to JavaScript but the entire app needs to be built to JavaScript at once for now (that may change in the future). There is no way to build Angular.js from Angular.dart to be used in JS applications.

Dart doesn’t generate consumable JavaScript at present. This problem doesn’t exist with TypeScript for the most part, which again plays nice with Angular’s current userbase, despite Dart being used actively at Google.

### A language of its own vs. a JavaScript superset

At the end of the day, Google’s development of Dart was intended to be the creation of a new web programming language. TypeScript follows a less radical approach than Dart – it’s a typed superset of JavaScript and existing JavaScript projects can be converted to TypeScript simply by renaming the source files from*\*.js* to *\*.ts*.

Rather than trying to replace JavaScript, Dart could aim to exist alongside it and compile to readable, yet fast JavaScript. The special interop library is also a feature that could be looked at, in order for developers to use the hundreds of thousands of JavaScript libraries already out there.

For those not familiar with TypeScript, user [peferron](https://news.ycombinator.com/item?id=9151993) over on Hacker News puts it nicely: “It feels just like writing JavaScript, but with a thin layer of type annotations that bring you the familiar advantages of static typing”.
