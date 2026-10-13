---
url: "http://discursive.com/2013/02/19/rails-you-have-turned-into-java-congratulations/"
captured_at: "2013-02-21T15:28:09-03:00"
title: "Rails, You Have Turned into Java. Congratulations! « Discursive"
domain: "discursive-com"
---

# **R**ails, You Have Turned into Java. Congratulations!

Rails isn’t the easy framework it once was, age has brought along a good deal of complexity both in the way Rails applications are deployed and in the number of technologies you need to assemble together to get anything meaningful done**.**

***Update (2/20/13):** Hello all, one additional note**.**   I’m surprised to be saying this, but I think the key difference between Rails and Java is that the Java “ecosystem” has this imperfect, somewhat ad-hoc standards group called the JCP**.**  This means that Hibernate and MyBatis or Spring and Oracle aren’t just pulling another framework out of thin air, they have to agree on standards and APIs**.**   This slows things down a bit, but, in the long run, this makes things more interchangeable**.**   It’s odd for me to write this because I’ve railed against the JCP for years, but I do think that Rails is a picture of what happens to “frameworks” in the absence of standards**.**   Call me old for saying it, but I did.  So there**.***

**Frameworks atop Frameworks atop Opaque Hosting Platforms**

Sure, Rails itself is straightforward, but the frameworks you slap on top of it can quickly become burdensome abstractions:  RefineryCMS, Devise, Omniauth, Carrierwave, Unicorn, Rack Rewrite, Fog, New Relic, Foreman, AMQP, and Honeybadger, not to mention the extra magic that Heroku gems throw into the mix (backups and other fun)**.**

> Why is the site slow today**?**  I don’t know maybe AWS is having problems?  Nope.  Ok, maybe the Unicorn configuration is screwy?  No**.**   Alright, everything works except Refinery take a look at New Relic**.**   That didn’t help**.**   Ok, let’s restart the application.   Great, that fixed it**.**  Why?  Not sure**.**  Was it a worker thread that was stuck?  Who knows, and who cares the site works now…

Maybe I’m reacting more to Heroku’s recent unpredictably and mysterious performance issues**.**   Maybe, I’m not fully dissatisfied with Rails or Ruby, but I can’t help but notice that Rails has become heavier these days**.**

Is it the complexity that Refinery brings to the table**?**  Maybe.  Refinery does what it does, but it is something of a beast**.**   If you follow the rules closely, you’ll end up developing a Rails application with an excessive number of Engines, which is really just another way of saying that you’ll be fumbling through a messy file explosion**.**  (What view is that engine in**?**   Hold on, let me click through five levels of folders…**.**)    There are those of you who will shout “Sinatra, you should use Sinatra**?**”  But that’s really not what I came to Rails for.

I know I have unrealistic expectations**.**  I want it all, and I want it to be easy: I want straightforward defaults, but I also want customizations to be things I can understand**.**    Take the intersection of Devise, Refinery, and Omniauth as an example**.**  All three of these frameworks are first-class, don’t get me wrong**.**   (I lied, Devise and Omniauth are first-class, and Refinery is an awful mess**.**) Making them work seamlessly together is an obtuse nightmare  - a documentation desert littered with wreckage**.**

**Frameworks that Eat Frameworks don’t like it when you Customize the Frameworks they Eat**

The problem is really that once you start making use of Rails and all of the frameworks built atop of Rails you end up creating an opaque mess of customization**.**   One framework, say Refinery depends on something like Devise**.**   Customize anything and good luck upgrading.

> Who really knows what happens during the login process**?**  Oh, I know, we’ll use RubyMine to step through this unpredictable mess**.**     I need to make a simple change to how routes work… oh look Routes have become incomprehensible because you now have 12 difference Refinery engines**.**

You’ll find yourself staring at incomprehensible mega-frameworks maintained by developers who are unapologetic about how little they care for writing documentation**.**     You’ll also end up with the most common pattern from Hell: the single Rails application that runs an entire business**.**

I’m starting to think that Rails has turned into the new Java, and that it is time to return to Java and ask it a simple question…

**…Java, have you learned to “easy” yet**?****

### Share this:

### Like this:

Like Loading..**.**
