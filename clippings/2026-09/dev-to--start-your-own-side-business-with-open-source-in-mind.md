---
url: "https://dev.to/developuls/start-your-own-side-business-with-open-source-in-mind-2noe?ref=dailydev"
captured_at: "2026-09-24T23:56:40+01:00"
title: "Start your own (side) business with open-source in mind"
domain: "dev-to"
---

This month I started my own DevRel advisory business and it's super fun tbh. Such an experience already, and it's not yet even properly launched.

It _literally_ takes less than 2 days to set _EVERYTHING_ up for static parts of your website.

This is the URL of my website: [developuls.com](https://developuls.com/).  
It's quite a simple one, but it will grow over time.  
Here is a quick walkthrough on how can you build your own  
_(or expand your presence from any of the platforms you are relying on to your own website)_.

[![A coder building a website](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fsming3vpgksyu08awow3.jpg)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fsming3vpgksyu08awow3.jpg)

## [](#website-components)Website components

### [](#cicd)CI/CD

[Vercel](https://vercel.com/) is an open-source platform for hosting and deploying web applications and websites.

You can seamlessly use it as a part of your CI-CD pipeline. This is also where you'll connect your domain and never have to worry about it again.

Create a Vercel hobby (read: free) account (make sure to check if it works for you [here](https://vercel.com/docs/accounts/plans/hobby)).

Click the `Add new...` button on the right-hand side of your dashboard, then select `Project`.

[![Create vercel project](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F27rqfsq2vccrf8ur3v8k.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F27rqfsq2vccrf8ur3v8k.png)

If you already have your website code, just connect the Git repository with your Vercel account.

[![Project creation in vercel](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fq5x42t0sjglbyjaajxcs.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fq5x42t0sjglbyjaajxcs.png)

Otherwise, either start coding it or _do what I did_ and check some of the many templates available and pick what best suits you.

After you're done with your site (or a part of it), and you want to deploy it just go to your project (on the dashboard), click the `...`, and select `Create deployment` option.

[![Vercel deployment](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fmhgexii4l0vh1w4ligtf.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fmhgexii4l0vh1w4ligtf.png)

### [](#website-framework)Website Framework

As I mentioned in the intro, my website is fairly simple.

I built my website relying on the [Astro](https://astro.build/) and their template available on Vercel.  
Astro is an open-source framework designed for content-driven websites.

[![Astro framework website](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fffokxejzykf4ad0jdi16.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fffokxejzykf4ad0jdi16.png)  
Luckily, the framework itself was super easy to play with and to adjust the template to my specific needs.

I did struggle _a little bit_ with in-project image rendering as it relies on `Sharp` whose `v0.33.0` release doesn’t really play the best, but it was an easy workaround with simply storing my images on the cloud instead of the website repository.

Other than that it was joyful to use it, and I iterated super fast.

### [](#contact-form)Contact form

As with any business, you want to be able to communicate with your (potential) clients.

I chose another open-source tool to hook up my business email address with my website's contact form.  
[Web3forms](https://web3forms.com/) is an open-source solution (and completely free one) that sends HTML contact form submissions directly to your email inbox using their contact form api service _without any server or backend code_.

And you don’t even have to log in. Just go to their website and click the `Create your Access Key` button.

[![Web3forms create access key](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fce4n9i8aabd3mks9ptlt.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fce4n9i8aabd3mks9ptlt.png)

Then insert your email address.

[![Web3forms insert your email address](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F1osito0t9sznsxp5yqp7.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F1osito0t9sznsxp5yqp7.png)

Then copy the HTML form (which you can adjust per your needs).  
[![Copy the HTML form](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F69ad5uyz4k48b1vfc2d4.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F69ad5uyz4k48b1vfc2d4.png) and paste it wherever on your website you want your clients to contact you that way.

Finally, go to the inbox of the email you inserted above, copy the access key sent to you by `notify@web3forms.com`, and paste it instead of the `YOUR_ACCESS_KEY_HERE` placeholder of the contact form you previously placed.

## [](#calendar-integration)Calendar integration

While I appreciate people reaching out via email, I find it much easier to understand their needs and pains while chatting with them.

Being a techie, I used another open-source solution here: Cal.com.

[Cal.com](https://cal.com/) is an open-source event-juggling scheduler for everyone, and is free for individuals.

You just create an account, connect it with your email calendar, and start getting calls scheduled.

The coolest part of it is it comes with a couple of embeddable templates you can simply add to your website. I chose the floating widget at the bottom right corner of my website so people can book a call with me to discuss a potential partnership.

Here is what it looks like on my website (see the bottom right):  
[![Cal.com embed on developuls](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fwyj1k91bcdag2gosol3q.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fwyj1k91bcdag2gosol3q.png)

It works with Google, Outlook, Apple, Notion, and plenty of other calendars, and you can schedule calls in any of the +20 options.

[![Cal.com website embed](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fbqv2u2gw46xefjckqbq1.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fbqv2u2gw46xefjckqbq1.png)

## [](#realtime-communication-platform)Real-time communication platform

If you're an open-source lover such as myself, you might go and connect Cal.com with the Mirotalk.

[Mirotalk](https://dev.tourl/) is an open-source, free, browser-based Real-time communication (video) solution, that you can use to replace Google Meet or any other commercial alternative you might've been using beforehand.

[![Mirotalk RTC website](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F5s0w17yfb1h2xcpv9mvf.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F5s0w17yfb1h2xcpv9mvf.png)

## [](#wrap-up)Wrap Up

Nowadays is super easy to get started with an online presence of a business. And most of the things we can think of exist in the form of open-source solutions.

How crazily good is that?!?

In my endeavor, I used a bunch of open-source solutions because it:  
1) saves me some time from reinventing the wheel  
2) is free  
3) usually has a healthy community of contributors and people willing to help in case you get stuck anywhere.

Let's support some these open source tools on GitHub:

*   Vercel - [\[ Star on GitHub \]](https://github.com/vercel/vercel)
*   Astro - [\[ Star on GitHub \]](https://github.com/withastro/astro)
*   Web3Forms - [\[ Star on GitHub \]](https://github.com/web3forms/web3forms-react)
*   Cal.com - [\[ Star on GitHub \]](https://github.com/calcom/cal.com)
*   Mirotalk - [\[ Star on GitHub \]](https://github.com/miroslavpejic85/mirotalksfu)

What open-source projects helped you bring your project to the top level?
