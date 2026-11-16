---
url: "https://signalvnoise.com/posts?n=1987"
captured_at: "2026-11-16T04:17:49+00:00"
title: "Signal v. Noise by Basecamp"
domain: "signalvnoise-com"
---

## [Ta-da List on Rails 2.2, Passenger And EC2](https://signalvnoise.com/posts/1433-ta-da-list-on-rails-22-passenger-and-ec2)

Ta-da List just moved to three exciting platforms: Rails 2.2, Phusion Passenger, Amazon EC2.

This is an important milestone for 37signals. As proponents of simplicity, we really felt the difference the latter two technologies made for server provisioning and deployment. As we grow more comfortable with these services, we’ll be moving other applications this way and writing more about the results.

## Phusion Passenger

After we comissioned Phusion to [add global queueing to Passenger](http://blog.phusion.nl/2008/10/29/phusion-passenger-now-with-global-queuing/), we felt it was time to give it a try. Since we were already on Apache, it proved a simple transition. We’re really impressed with the ease of deployment and stability under Passenger. The app now requires less than 10 lines of configuration to launch and deploy. Passenger handles its own process spawning: done. Its command line tools for monitoring requests and memory usage complete the package for easy integration into monitoring tools.

## Amazon EC2

This has been my ongoing project at 37signals. Avoiding the extra layer of low-level setup involved with our current Xen-based virtualization system brought me closer to the core concerns of our environment – how to best automate support for the applications from the systems side. More often than not, a traditional server deployment consists of a range or organically provisioned services and environments. Ours is no exception, due to the rapidly-changing requirements of each application. EC2’s lack of persistence forces you to think about automating this from the start. This turns out to be a blessing in disguise. Setting up a full environment consisting of dedicated instances for mail, Nagios/remote logging, application serving, a master and a slave now takes about 5 minutes.

In future posts we’ll detail how we used combination of image bundling and a custom EC2 deployment tool to build the Ta-da List environment.

If you haven’t documented your server deployment process in code or experimented with these technologies, now is the time.

## [Good Experience: It's the little things](https://signalvnoise.com/posts/1432-good-experience-its-the-little-things)

![](http://www.37signals.com/svn/images/153-freeshowtime.png) I have the usual gripes with cable/satellite/telecom company customer service like most people. However, I recently had an experience with DirecTV that left me feeling good about doing business with them.

Upon checking my latest bill, I was greeted with a message on my Account page: 3 months of Showtime for free. Score! OK, what’s there not to like about free premium programming right? But it wasn’t the free Showtime that made the experience great. Above that there was a line that read: **Loyal viewer since 2004**. I didn’t realize I had been a customer for so long. I appreciated that DirecTV was keeping track of that stat.

There was a feedback form next to the free Showtime graphic. I decided to send a “Thank you” note for the free Showtime, that I was enjoying my HD DVR, and a plea to not increase the monthly programming fees. I thought that this would just disappear into the Customer Service inbox ether. Needless to say, I started looking up Showtime programs that I could record. A few hours later I received this reply from DirecTV Customer Service:

> Thanks for writing. I see that you have been part of the DIRECTV family since 2004. I’m happy to hear that you appreciate the free SHOWTIME UNLIMITED for 3 months that we’ve added to your account as a free gift. I would like to personally assure you that your suggestion about not increasing the monthly fee is very important to us. We value your opinions about our service, so I have forwarded your request to DIRECTV management, who review every suggestion, inquiry and complaint for trends from our most important customers to determine what changes should be considered. Sincerely, Jhaney S. Employee ID# 100102919 DIRECTV Customer Service

I love how they not only responded to my note, but that they also reiterated that I have been “part of the DIRECTV family since 2004”. There is something “mom and pop shop” about that. That recognition of how long I’ve been a customer made me feel important. It’s such a simple little thing to do.

## ["Mixed content warning", how I loathe thee!](https://signalvnoise.com/posts/1431-mixed-content-warning-how-i-loathe-thee)

Browsers try their best to protect users from the evils of the internet, but some times their eager kills good use cases all the same. The “mixed content warning” that IE and Firefox throws when you reference a non-SSL asset from an SSL page is one of those cases.

The problem is that browsers don’t like caching SSL content. So when you have an image or a style sheet on SSL, it’ll generally only be kept in memory and may even be scrubbed from there if the user is low on RAM (though you can [kinda get around that](http://blog.pluron.com/2008/07/why-you-should.html)).

Even when you do your best to limit the number of style sheets and javascript files and gzip them for delivery, it’s still mighty inefficient and slow to serve them over SSL every single time the user comes back to your site. Even when nothing changed. HTTP caching was supposed to help you with that, but over SSL it’s almost all for naught.

Now I understand why SSL content is not kept on a disk cache. You don’t want the financial-results-2008.png lying around on a public computer that you thought was safe to use because of SSL.

This is why it would be ever so wonderful if you could refer to a non-SSL asset from an SSL page. That way you could say “this stuff is private, don’t share it” when serving over SSL and at the same time take advantage of HTTP caching for things that pose no security risk, like drag\_handle.gif.

But oh no. If you try to do that with IE, you’ll get a “mixed content warning” that’ll scare the bejesus out of your users, so that won’t go. On Firefox, you’ll often (depending on settings) get the same warning if you try to serve JavaScript or style sheets like that.

Only Safari stands out as the hero with no mention of “mixed content warning”. So please, IE and Firefox, can you learn from Safari and kill it too? Then we wouldn’t have to [adjust our asset rules](http://gist.github.com/29752) depending on the user agent and everyone would be able to enjoy the extra speed of properly caching assets.

Note: There’s a reasonable argument for warning on JavaScript includes as man-in-the-middle attacks can do nasty things, but that’s not true for CSS (on anything but IE) or images

## [Hire managers of one](https://signalvnoise.com/posts/1430-hire-managers-of-one)

When you’re hiring, seek out people who are managers of one.

What’s that mean? A manager of one is someone who comes up with their own goals and executes them. They don’t need heavy direction. They don’t need daily check-ins. They do what a manager would do — set the tone, assign items, determine what needs to get done, etc. — but they do it by themselves and for themselves.

These people free you from oversight. They set their own direction. When you leave them alone, they surprise you with how much they’ve gotten done. They don’t need a lot of handholding or supervision.

How can you spot these people? Look at their history. Have they been self-sufficient at previous jobs? Have they defined their own role before? Have they started their own site/company before? Or done their own thing in some other way? Find someone with initiative and a budding entrepreneurial spirit. And then nurture it.

You want someone who’s capable of building something from scratch and seeing it through. When you find these people, it frees up the rest of your team to _work_ more and manage less.

![master\_sheet\_v3.jpg](https://37assets.37signals.com/svn/thumb-master_sheet_v3-67267d6e575a58716ad155f8ba0478bb.jpg)

[The Art of the Title Sequence](http://www.artofthetitle.com/): a great site for opening credits aficionados.

## ["37signals is the (Lotus, iPhone, Disney) of software"](https://signalvnoise.com/posts/1427-37signals-is-the-lotus-iphone-disney-of-software)

Recently we asked commenters here [how they would describe 37signals to average civilians in 20 seconds or less](http://www.37signals.com/svn/posts/1371-describe-37signals-in-20-seconds-or-less). A quick recap below:

A lot of people turned to analogy. Some things 37signals is like…

> “Just like you can use Gmail for email without installing Outlook on your computer, you can use our stuff to run your small business without installing anything on your computer.”
> 
> “If Steve Jobs was in the online apps market, his company would be 37signals.”
> 
> “A giant filofax in the sky.”
> 
> “The Lotus (cars) of business software. We build lean, compact solutions to business needs. Just like a Lotus, we’re great with everything you need, and we jettison away all the crap you don’t.”
> 
> “We do web based stuff like google, amazon or ebay. Except we focus on tools to manage projects, todo’s, sharing documents and contacts and working together – simple stuff that most people and businesses need. At 37 Signals – the BIG DEAL is simplicity. Up, running and effective in minutes.”
> 
> “You know the iPhone? It’s gotten all this attention for being so elegant, practical, and kind of fun to use. Imagine if the software you used at work were like that. You know, your project management and organization tools. Fewer menus, more results, kind of fun to use. We make software for the web that’s like that.”
> 
> “We are the Disney of software.”

A chunk of people thought we should get salty:

> “We are doing anti-management kickass software.”
> 
> “37signals – we help people get their $#!+ together.”
> 
> “We take the sh out of IT.”
> 
> “37Signals makes products that take the bullshit out of communication so you can communicate.”
> 
> “P-roject management done right  
> I-ntranets for anyone  
> M-essaging that works  
> P-eople tracking on a whole n’uther level  
> S-implified for real”

[Continued…](https://signalvnoise.com/posts/1427-37signals-is-the-lotus-iphone-disney-of-software#extended)

## [Backpack: Some things you may not have known](https://signalvnoise.com/posts/1426-backpack-some-things-you-may-not-have-known)

We recently conducted a survey of our [Backpack](http://www.backpackit.com/?source=svn_post) customers. We got some great feedback — including that 97% of our customers would recommend Backpack to a colleague, friend, or family member. Thank you!!

We also included some open ended questions and comment boxes. I recently finished reviewing every response and noticed some suggestions about things that Backpack already offers. I thought I’d pull out some of the more common suggestions and show you where you can find these features in Backpack.

## SSL on Solo

A few people mentioned that they didn’t have SSL on their Solo Plan. The Solo plan _does_ include SSL, but it’s possible that it’s turned off. To check, click the Settings link in the top right corner. Then you’ll see this option:

![](http://www.37signals.com/svn/images/backpack-ssl-setting.png)

## Difficult to upload multiple files (or a folder) at once

A good way to handle multiple file upload (or uploading an entire folder) is to zip or compress the files or folder into a single archive. Then you can upload that single file instead of trying to upload all the separate files separately. Both the Mac and PC have zip/archiving/compression tools that allow you to do this. On the Mac OS X 10.5, for example, you can select multiple files or a folder, right-click, and select “Compress items”. I believe 10.4 said “Archive items”.

[Continued…](https://signalvnoise.com/posts/1426-backpack-some-things-you-may-not-have-known#extended)

## [When hi-tech is too-much-tech](https://signalvnoise.com/posts/1425-when-hi-tech-is-too-much-tech)

Is anyone else annoyed by the “just speak your choice” automation in so many telephone menus? I feel like an idiot mumbling “YES!” or “CHECK BALANCE!” into my phone. Maybe it’s the misanthrope in me coming to the front, but I’d much rather push buttons than talk to a pretend person.

What problem does the “speak your choice” technology solve? Is it just to work around the limitation of rotary phones not working with the other menus? (Does anyone even use rotary phones anymore?) It feels, to me, like an example of “we do it, because we can” syndrome. Sometimes, lower-tech really is sufficient-tech.

## [Jason Polan explains with a sharpie](https://signalvnoise.com/posts/1422-jason-polan-explains-with-a-sharpie)

The new [Criterion Collection](http://www.criterion.com/) website features a cool introductory video in the upper-right corner. A pair of anonymous hands draw on white paper with a sharpie as a narrator introduces the site.

[![](http://www.37signals.com/svn/images/152-criterion.png)](http://criterion.com/)

Turns out the hands and voice belong to artist [Jason Polan](http://www.jasonpolan.com/). A Google video search revealed he’s done [more of these sharpie videos](http://video.google.com/videosearch?q=%22jason+polan%22&emb=0&aq=f#). He also sells a couple on his site, like [How to Draw a Giraffe](http://www.jasonpolan.com/art/giraffe.html) and [How to Draw an Apatosaurus](http://www.jasonpolan.com/art/apatosaurus.html). Too bad those last two don’t have preview clips.

Check out this video he did for the State Bar of Texas:

Love this stuff.

![open\_table.png](https://37assets.37signals.com/svn/thumb-open_table-a3f0c1cb5abc4cfe0d6d53af68c9ea08.png)

Make a reservation at [OpenTable](http://www.opentable.com/) and the confirmation screen smartly offers to send a custom invite to your other dinner guests.
