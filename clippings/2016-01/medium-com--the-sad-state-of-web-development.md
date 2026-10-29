---
url: "https://medium.com/@wob/the-sad-state-of-web-development-1603a861d29f#.o7914kcgv"
captured_at: "2016-01-12T19:22:31-03:00"
title: "The Sad State of Web Development — Medium"
domain: "medium-com"
---

# The Sad State of Web Development

#### Random thoughts on web development

#### **Going to shit**

2015 is when web development went to shit. Web development used to be nice. You could fire up a text editor and start creating JS and CSS files. You can absolutely still do this. That has not changed. So yes, everything I’m about to say can be invalidated by saying that.

The web (specifically the Javascript/Node community) has created some of the most complicated, convoluted, over engineered tools ever conceived.

![1*J7Gli_NPO1j-pzk607jsmw.jpeg](medium-com--the-sad-state-of-web-development/1cb9e41f1ec0ec817f819c89d09c59b2.jpeg)

![1*J7Gli_NPO1j-pzk607jsmw.jpeg](medium-com--the-sad-state-of-web-development/f2e3b44446934b343f7d2631a3c943a1.jpeg)

#### Node.js/NPM

At times, I think where web development is at this point is some cruel joke played on us by Ryan Dahl. You see, to get into why web development is so terrible, you have to start at Node.

By definition I was a [magpie developer](http://blog.codinghorror.com/the-magpie-developer/), so undoubtedly I used Node, just as everyone should. At universities they should make every developer write an app with Node.js, deploy it to production, then try to update the dependencies 3 months later. The only downside is we would have zero new developers coming out of computer science programs.

You see the Node.js philosophy is to take the worst fucking language ever designed and put it on the server. Combine that with all the magpies that were using Ruby at the time, and you have the perfect fucking storm. Lets take everything that was great in Ruby and re write it in Javascript, I think was the official motto.

Most of the smart magpies have moved on to Go at this point, but the people who have stayed in the Node community have undoubtedly created the most over engineered eco system that has ever appeared. No one can create a library that does anything. Every project that creeps up is even more ambitious than the next. It all starts with a core module and 400 plugins for this module. No one will build something that actually does anything. I just don’t understand. The only thing I can think, is people are just constantly re writing Node.js apps over and over.

Javascript has zero standard library, so as soon as you npm init a new Node app you better install at least 15 terabytes of modules to get 1/16th the standard lib of something like Ruby or Go. It may seem super cool to have all these small modules until you try to update them. When the developer who created that module doesn’t follow semver, so you’re fucked. Sorry. To the people who say I’m wrong about this; STOP rewriting your micro services for 5 minutes and listen to me. Your shit WILL fucking break on a patch level change. Other dependencies will not play nice.

#### Enter the front end (not like that)

I didn’t really realize how the Node community affected the front end community until developers started writing their tools in Node. Then started publishing front end libraries on NPM. Now we’re really fucked. These people have taken configuration to the extreme and I did Java Server Faces professionally for 4 years. 0\_0

![1*HcuYB8Lr9GRefrmdypw4EA.gif](medium-com--the-sad-state-of-web-development/e4b6dc95b88485a33c3ec7f69791a6c8.gif)

#### Babel

A great project called 6to5, which did what it’s name implied. By installing a simple Browserify transformer you could write ES6 code(well ES7 too, hence the name change) and “compile” it to ES5.

Now it’s some convoluted mess of plugins that tries to do everything everyone ever wanted, while actually doing nothing out of the box. Sebastian seemed like a nice guy, then goes to Facebook and comes out with Babel 6, then to really shove it in my face, he uses that screaming pile of dump called Phabricator to handle issues.

Maybe all the idle Facebook engineers who created Phabricator can get with the idle Uber engineers who created the [branding](http://brand.uber.com/) page, and come up with something that is better.

#### **PostCSS**

People actually use this thing. Can a library actually do shit out of the box anymore? I just want to install something and use it, not decide all the little plugins I want to use. New developer comes onto your team:

> Oh hey, we use PostCSS. Look at the gulp/grunt/broccoli/brunch file and see what plugins I’ve used. When you do that, then look up what each plugin does. After you have wasted the entire day on that, then start writing some css, or PostCSS, whatever the fuck it actually is. I really just wanted SASS but decided to use these 185 plugins instead and you know, because it’s written in Javascript

#### React

I don’t even know where to start with this project. From what I can tell the background of React is: Facebook couldn’t create a notification indicator on Facebook.com, so they create this over engineered dump pile to solve that problem. Now they can tell you how many unread posts you have while downloading 15 terabytes of Javascript. Once they solved that issue they proceeded to write everything in React. They even built a comment system with it, because you know making an Ajax call and a DOM append is really hard.

That’s right. All you guys using React like it’s the only way to solve every problem ever are using it because Facebook couldn’t build a fucking notification icon.

I have the Chrome plugin that shows when a site uses React. I swear every other website I visit uses React, for the stupidest stuff. So many content sites use React. It’s pitiful. It’s like developers just forget that these frameworks come and go with the wind. Just take a step back and think about your front end choices in 2009. Now 2011. Now 2013. Now 2015. Just think about it. Do you really think putting all your eggs into a basket like React is a good idea?

Of course everyone in the tech community has to rewrite all their interfaces in React now. If you love to get off to to tech stacks then you’ll love hearing from Netflix, Yahoo, Airbnb, Vimeo and Imgur. You know who didn’t give a flying fuck about React? Their customers. Good job Yahoo, you rewrote your shitty mail client in React. Your customers didn’t give a shit. They just want it to work. Oh Vimeo, you couldn’t display the view count on the video without bringing in React? I really appreciate that. My cpu does too. Imgur, really appreciate you bringing in React on a page.. to display a fucking image. I mean you can’t even make this up.

Look at this video of Airbnb’s front end. <https://www.youtube.com/watch?v=gMvvb6F8dgk>. I really think it is a satire piece on web development. Now look at this <https://www.airbnb.com/rooms/5029761>. The whole page is static content, yet they literally hit the Rails stack, then hit the Node stack to render the React to a string and then send it back through the Rails stack. They even toyed with the idea of rewriting Airbnb in Node. 0\_0. Front end developers come in to a company like Airbnb, like a parasitic infection of over engineered sloth turd. For what? Masterbaiting about their line code count for displaying fucking text on a page?

Please guys/girls, just take a step back every now and then. How does rewriting your interface in the latest framework get you to the next customer? Or the next 50 customers. Does it actually make your customers happier?

#### Don’t fucking build a SPA

Really all I’m saying is don’t build a SPA. A SPA will lock you into a framework that has the shelf life of a hamster dump. When you think you need a SPA, just stop thinking. Just don’t. Your users just don’t fucking care.

If I see a section on my app that is really hard to with Pjax/Turbolinks and jQuery, I’ll bring in a library/framework like Vue.js, \*cough\* React, Angular. All good choices for doing really complex forms(although I find Angular to be the best at this), with a ton of conditional validation. You know what though, these are the outliers in my experience, not the norm.

Maybe 1 or 2 pages on your app will have really complex UI, but the other 95% of the app does not. So you pay a huge penalty doing a SPA. You’re typically writing all the basic CRUD stuff in a SPA from scratch. The backend framework your using can’t help you in any way. So my advice is to use Rails Django, Play Framework, or Phoenix to develop most of the app, because they help you with most of the boilerplate stuff, and bring in the flavor of the month on a page that needs it. So when the next flavor of the month comes out you’re entire app is not knee deep in the last flavor of the month. You can just re write that one page.

**Hello my name is Drew and I’m a recovering magpie front end developer.**
