---
url: "http://blog.yodersolutions.com/why-i-recommend-emberjs-over-angularjs/"
captured_at: "2015-03-11T15:24:33-03:00"
title: "Why I recommend EmberJS over AngularJS | Paul Yoder's Blog"
domain: "blog-yodersolutions-com"
---

# Why I recommend EmberJS over AngularJS

*tldr: scroll down and read the headlines and bold words to get a quick overview.*

For the past couple years I have absolutely loved developing web applications with AngularJS. Angular has made it so easy to provide the advance user experience that people are coming to expect. And as a developer I have enjoyed how easy Angular has made two way databinding and unit testing the JavaScript code with its built in dependency injection.

Everything was awesome!

**But then the Angular team announced their plans for Angular 2.0 and everything was no longer awesome.**

When the Angular team announced version 2.0 would be a complete rewrite with no upgrade path, I felt like a good friend had just abandoned me.

To be sure, the Angular team says they will work on an upgrade path from 1.x to 2.0, but I don’t believe it. And until they prove otherwise, it’s going to basically look something like this:

1. Extract as much business logic as you can out to Plain Old Java Script (POJO) objects
2. Rewrite all your Angular controllers, directives, etc. to use the new syntax and reuse your business logic that you extracted into the POJO objects.

I’m sorry, but this really isn’t a legitimate upgrade path. The same upgrade path could be used to completely move off Angular altogether and onto another JavaScript framework. **It shouldn’t take as much work to upgrade your app from version 1.x to version 2.0 as it does to migrate off the framework altogether.** (they might as well no longer keep the Angular name and just say it’s a completely new framework.)

*3/10/2015 Update: It was announced at NgConf last week that it will be possible to incrementally upgrade parts of an Angular 1.x app to 2.0. It won’t have to be done in one big bang migration. I’m happy that the Angular team has worked hard to make this happen and has proven me wrong [anexo ausente] This hasn’t changed my reasons for recommending Ember, but it is encouraging to hear.*

As you can tell, I was upset. So I started looking at other JavaScript frameworks. **If moving to Angular 2.0 requires completely rewriting my Angular 1.x apps, then I at least wanted to make sure there wasn’t another framework out there that was competitive with Angular.**

And that’s when **I found the EmberJS framework.**

Ember has been out for a couple years now, and I have been hearing a little bit about it here and there from other JavaScript developers online, but I had never spent any time looking into it. I saw that CodeSchool had a course on it, so I signed up for the course and starting going through it.

#### Learning Ember

As I was learning Ember, I realized right away that Ember was not Angular, and it had its own way to structure a JavaScript application. Unlike Angular, Ember is a very opinionated framework which forces you to structure your app the way it wants you to. And if you don’t follow its guidelines, then you’ll quickly find yourself fighting against the framework.

Honestly, **I was kind of annoyed with how opinionated Ember was, but then something happened that completely changed my mind on the matter.** Let me share.

About six hours into learning Ember, I decided to take a break from the course and take a look at the source code for a production app that was using Ember. I knew the [Discourse forum software](https://github.com/discourse/discourse) was open source and built with Ember. So I found its Github page and started browsing its Ember code.

I opened a template file and looked through it. I saw that it was displaying a value from a property, so I opened the controller file associated with the template. I saw the property was actually a computed property based upon the controller’s model. Next, I browsed to the controller’s associated route and saw how the controller’s model was be retrieved. I then went back to the template file and saw that a view helper was being used, so I opened the view helper file to see what it was doing.

And then I distinctly remember pausing and thinking something didn’t feel right. Something was off, but I couldn’t put my finger on it. **And then it hit me: I was actually understanding the code base for a project I had never looked at before.**

For a project the size of Discourse, it typically takes a few hours to a few days to just begin to understand its code base. But **Ember’s strong opinions and conventions allowed me to open a project I had never seen before and understand what was going on in only a few minutes.**

And that’s when my opinion about Ember changed. Up until that point I had been hesitant about Ember and didn’t think it was better than Angular. But that experience browsing the source code of a production Ember app helped me begin to understand Ember’s benefits over Angular.

I then I began learning all I could about Ember. And the more I learned about Ember and its community, the more I appreciated Ember. And now I fully recommend Ember over Angular. Let me share my reasons why.

## Why I Recommend Ember over Angular

My reasons for recommending Ember over Angular are not the typical reasons given by developers when they’re recommending a framework. But once you read my explanation for each reason, I hope you’ll also see the benefits Ember has.

But before I share my reasons for Ember, I want to share some reasons that did not affect my decision.

### Reasons that did not affect my decision

#### It doesn’t have new functionality

Anything you can do in Angular, you can do in Ember. And anything you can do in Ember, you can do in Angular. Both frameworks can provide the same functionality to the end user.

To be sure, how you implement a feature (like a modal, or sorting a table) is different in Ember versus Angular, but the end result would be the same. The user would notice no difference if the website was built with Ember or Angular. So difference in functionality is not a reason for my Ember recommendation.

#### It’s not the next shiny new toy

It could be argued that I have the *Shiny New Toy Syndrome* because every couple of years I’m advocating for a new JavaScript framework. It started with Backbone, then a couple of years later I started advocating for Angular, and now it’s Ember.

I would argue I don’t have the shiny new toy syndrome, though, because each framework I have advocated for had benefits over the previous framework of choice.

The reason I have changed my recommended JavaScript frameworks so much is because the JavaScript framework ecosystem itself is still in its infancy and has not matured yet. It seems every week there is a new JavaScript framework created.

It’s not cool to change frameworks just because there is a new framework out. There must be a business reason to change. And as you’ll read below, I would argue there are some very good business reasons to move to Ember.

### Reasons that did affect my decision

#### The Core Team

When deciding between frameworks, the members of the core team usually doesn’t affect my decision making process. But this time it did affect my decision to choose Ember over Angular. And actually, it was one of the main deciding factors for me.

Here’s why: **every member on Ember’s core team is actively working on one or more production apps that use Ember**. On the flip side, no one on Angular’s 2.0 core team can say the same thing. That’s because Angular 2.0 won’t even be out for another year.

Let me explain why this is so important to me.

When everyone on the core team has their own production apps using the framework, then **the core team is forced to experience all the joys and pains of using the framework, just like every other developer does. And this means the core team will naturally look out for the good of all developers using the framework.**

On the flip side, when the core team members don’t use the framework on production apps, then “the sky is the limit!” It’s easy to forget about the developers using the framework as they dream up new features. Framework designers don’t feel pain in brainstorming meetings.

Angular 2.0 is a perfect case in point for this situation. One reason they are going forward with a complete rewrite of the framework is because none of the core team members will experience the pain of rewriting an app to migrate from version 1.x to 2.0. But you can be sure the Ember team won’t do the same thing because they also would have to rewrite their apps.

Another example of what happens when the core team dogfoods their own framework is Ember CLI. The main reason the core team is developing Ember CLI is because they not only see its benefit but also experience its benefit. I’ll go into more detail on Ember CLI below.

Like I mentioned, I haven’t heard many others look at the members of the framework’s core team, and use them as a reason for choosing one framework over another. But to me, it’s one of the most significant reasons for my decision.

#### Guidance is set by those with the most experience

So here’s a question: **Who do you want to set the guidance and best practices for using a framework? Developers with some experience using the framework or developers that actually created the framework?**

That’s the difference between Angular and Ember.

**Angular doesn’t provide much guidance on how to use the framework**, so it becomes the wild west when a company first adopts Angular. Every team uses the framework however they see fit. But eventually it does come to a head when the company realizes a developer can no longer easily switch teams because the framework is used so differently between teams. Then a few developers from different teams get together and come up with the company’s official guidance and best practices for using the framework.

But then that guidance only applies to apps created going forward. The apps that are already using the framework are grandfathered in because it would take too much time to refactor them. So it’s still difficult for developers to switch teams because there’s still legacy apps. And the developers that created the guidance only went off their own experience and features they had to create. They didn’t experience all the edge cases, so the guidance is in constant flux as new scenarios are coming up.

Here’s a case in point: there are four development teams currently using Angular at my work place, and every team has structured their Angular app differently. There is no consistency even though we’re all using the same framework. And we have literally spent multiple days worth of time discussing and debating how our apps should be structured. And they are still not structured the same way.

**Ember, on the other hand, has its guidance and best practices set by its core developers.** And these guidances and best practices are baked directly into the framework, so it’s easy to follow.

Because Ember specifically defines how an application should be structured, the **developers do not waste hours upon hours debating how the app should be structured.** Instead they can spend that time actually developing the app and providing value to the business.

It also means **new team members that already know Ember can become productive in any Ember app within minutes** because they know how the app is structured and where to go to add a new feature or fix a bug. Like I shared above, after only spending a few hours learning Ember, I was able to browse and understand the structure of a large Ember application. That can’t be said for most developers learning Angular.

#### Use 2.0 features in the 1.x version series

Many new features are being added for Ember version 2.0, yet when version 2.0 is finally released, it won’t contain any new features. I know, it doesn’t make sense. It didn’t make sense to me at first either. But after I understood Ember’s versioning process it finally did make sense to me. And it turns out Ember’s versioning process is pretty cool.

The reason no new features will be introduced when Ember 2.0 is released is because **all the 2.0 features will have already been introduced in the 1.x version releases**.

The Ember team has a lot of new features they want to add to Ember 2.0, but they’re not waiting for 2.0 to implement them. **They’re introducing the 2.0 features in version 1.x as they complete them**. For example, that means Ember apps can take advantage of using the react style virtual DOM for increased speed, whereas Angular developers have to wait until Angular 2.0 comes out.

Another cool feature being added to Ember is Fast Boot. This allows an Ember app to be ran on the server with Node.js, and it gives the ability for an Ember app to serve up populated HTML when the browser first comes to a page instead of a barebones skeleton HTML that requires the user to wait for all the JavaScript to be parsed and ajax data downloaded before they can see any data on the page.

So if nothing new is being introduced when Ember 2.0 is releaseed, what actually changes when it’s released? Basically the deprecation warnings in 1.x go away and if you had any deprecation warnings, then that code no longer works.

#### Ember CLI

Ember CLI is a game changer for Ember. And it will make all other JavaScript frameworks absolutely jealous. It not only streamlines developing Ember apps, but also makes it super easy to share common code among different Ember apps. And all this results in making Ember developers more productive.

**Ember CLI takes care of all the grunt work that’s involved in adding new third party libraries and code to the app.**

For example, let’s say you want to add a date picker to your Ember app. With Ember CLI, all you have to do is execute the following command and you can immediately use the datepicker addon:

1. `ember install:addon ember-cli-datepicker`

Now compare that with the typical set of steps required to install an addon without using Ember CLI:

1. Download the addon (typically with bower or npm)
2. Update the build config to include the addon’s javascript
3. Update the build config to include the addon’s css
4. Update the app’s dependencies to include the addon

As you can see, Ember CLI combines these four steps into a single command. And sure, these four steps only take a minute or two to perform manually, but that time quickly adds up over the lifetime of developing an application.

Another major feature in Ember CLI is blueprints. These are snippet generators that automatically add the scaffolding code required when creating new features in your Ember app.

Here’s an example of using Ember CLI to create a new route named `foo`:

```
ember generate route foo

installing
  create app/routes/foo.js
  create app/templates/foo.hbs
installing
  create tests/unit/routes/foo-test.js
```

So with one command, not only are all the necessary files created, but each file is stubbed out with the necessary scaffolding code and ready for you to actually write your application specific logic.

For example, here is the contents for the `test/unit/routes/foo-test.js` file that was generated:

```
import {
  moduleFor,
  test
} from 'ember-qunit';

moduleFor('route:foo', 'FooRoute', {
  // Specify the other units that are required for this test.
  // needs: ['controller:foo']
});

('it exists', function() {
   route  .subject();
  (route);
});
```

And now you can focus on writing your tests instead of spending a minute or two writing the plumbing code required before you can start testing.

No other JavaScript framework I know of has a command line utility like Ember CLI. So while developers on other JavaScript frameworks spend time writing plumbing code and updating their builds when adding third party libraries, Ember developers have that much more time to actually write their apps.

## Conclusion

Don’t get me wrong, I believe Angular 2.0 will be great, and I have enjoyed writing web applications in Angular 1.x. The complete rewrite for Angular 2.0 has really turned me off from the framework, though, and it made me realize there’s another framework out there that looks out for the developer more than Angular.

And it also made me ask the question: **since the Angular team is doing a complete rewrite for version 2.0, what’s to keep them from doing another complete rewrite for version 3.0 in the future?** After all, the pace of change in the JavaScript ecosystem is only speeding up, and shortly after Angular 2.0 is published, there will only continue to be new JavaScript features and enhancements.

I don’t want to use a framework that abandons its developers. I want to use a framework that looks out for its developers, and that’s why I like Ember.
