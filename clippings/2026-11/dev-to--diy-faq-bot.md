---
url: "https://dev.to/twilio/diy-faq-bot-o61"
captured_at: "2026-11-16T18:54:41+00:00"
title: "DIY FAQ Bot"
domain: "dev-to"
---

_The following blog post will walk you through how to use Microsoft Azure [Bot Services](https://azure.microsoft.com/en-us/services/bot-service/?WT.mc_id=devto-blog-chcondon) to create a simple chatbot using minimal programming, [Twilio](https://www.twilio.com/referral/xBBj30), and a Word Doc._

_If you’re looking for a quick summary and overview on the [Azure Bot Service](https://azure.microsoft.com/en-us/services/bot-service/?WT.mc_id=devto-blog-chcondon), I recommend starting here with our [documentation](https://azure.microsoft.com/en-us/services/bot-service/?WT.mc_id=devto-blog-chcondon), or taking an hour or two to complete a step-by-step [Learning Path](https://docs.microsoft.com/en-us/learn/paths/create-bots-with-the-azure-bot-service/?WT.mc_id=devto-blog-chcondon), so you have some context on the various bot options available with Azure._

_This post is part 1 of a series of posts on how to create various bots that can be built using Azure, with varying difficulty (this post being the easiest)._

_Happy botting! 🤖_

_\-Chloe_

![](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fsy4x64nas0rly846pp9u.gif)

I’m a **big** fan of using technology to solve problems and common sources of anxiety in my life. If you’ve followed any of my content in the past, you may be familiar with [my fake boyfriend app](https://dev.to/azure/an-ambivert-s-guide-to-azure-functions-27b8) that I used to save me from awkward social situations, as well as [my ADHD medication reminder](https://dev.to/azure/building-a-diy-adhd-medication-reminder-with-azure-functions-o70). Lately, I’ve been dealing with a lot of stress and anxiety around my DMs. Specifically the **amount** of inbound I get on Twitter, Instagram, Facebook Messenger, etc. Often times I drop the ball because I read a message on the go, promise to respond later, and well… apologies to anyone I’ve ghosted 😬👻. The truth is, as a [Cloud Advocate](https://developer.microsoft.com/en-us/advocates/), my role is incredibly social. My DMs are often full of attempted coffee meeting plans, memes from friends, speaking inquiries, bootcamp grads seeking career advice, and the occasional unwelcome “hey” from a random dude I’ve never met 😑.

[![DMs gif](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fv5fb4qbltzsosnmtozbr.gif)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fv5fb4qbltzsosnmtozbr.gif)

Unfortunately, due to the volume of inbound I get, I often get overwhelmed by all the noise. Not only do constant messages and notifications make it difficult to focus (especially while programming), but I also feel terrible when I drop the ball on folks. So, I started playing around with Azure Bot Service to see if there was some way to build a bot that would help me manage and automate my communication with folks.

After some quick brainstorming, I figured out that my DMs typically fall into the following categories:

*   Azure related questions 👩🏼‍💻
*   Bootcamp grads seeking career advice 🙋‍♀️
*   Speaking inquires 🎤
*   Ongoing conversations with close friends 👯‍♀️
*   Creepy folks (bots?) I’ve never met just saying “hey” 🙅🏼‍♀️
*   Miscellaneous opportunities (podcasts, interviews, specific Furby hacking questions, etc). 🎧🎙🎭❓

I knew that I wanted to build a bot, but I didn’t want it to respond to _every_ inbound message. For example, if I had a way to automate responding to commonly asked questions from bootcamp grads, I could save a considerable amount of time. Whereas a message from an Azure user would require a personal/detailed response from me. Additionally, I brainstormed the idea of training my bot to help me schedule and organize speaking opportunities, as well as flag or delegate important inquires/messages. However, I had never built a bot... but thanks to [Microsoft Learn](https://docs.microsoft.com/en-us/learn/modules/build-a-faq-chat-bot-with-qna-maker-and-azure-bot-service/?WT.mc_id=devto-blog-chcondon)\- I was able to get up and running with my 1st bot in under under an hour!

And so, I built my first bot using [QnA Maker](https://docs.microsoft.com/en-us/azure/cognitive-services/qnamaker/?WT.mc_id=devto-blog-chcondon). If you’re unfamiliar, [QnA Maker](https://docs.microsoft.com/en-us/azure/cognitive-services/qnamaker/overview/overview/?WT.mc_id=devto-blog-chcondon) allows you to create a bot using a simple FAQ list. Below I’ll walk through how you can build your own QnA bot to help delegate inbound messages for yourself. If you’re a small business owner, CEO, teenage girl, or anxious-tech-worker-afraid-of-dropping-the-ball-on-DMs like myself, building your own bot is shockingly easy (_seriously, it feels like witchcraft_ ✨😳).

[![witchcraft if](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fkq0zewraowg6mk7qy2js.gif)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fkq0zewraowg6mk7qy2js.gif)

Let's review what we're doing real quick...

**The Problem:** Noisy DMs + Constant Anxiety from Unanswered DMs  
**The Solution:** Build a bot to help respond and automate common messages I receive online  
**The Technology:** QnA bot

Below is a visual of how we’ll build our QnA bot from the [docs](https://docs.microsoft.com/en-us/learn/modules/build-a-faq-chat-bot-with-qna-maker-and-azure-bot-service/1-introduction)

[![diagram](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F5izeykmxdbc234ek80o5.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F5izeykmxdbc234ek80o5.png)

## [](#lets-create-a-knowledge-base-amp-qna-service)Let's Create a Knowledge Base & QnA Service

First, head to the QnA Portal ([https://www.qnamaker.ai/](https://www.qnamaker.ai/)) and sign-in in the right corner with your Azure credentials. Click over to to Create a Knowledge Base ([https://www.qnamaker.ai/Create](https://www.qnamaker.ai/Create)).

The knowledge base for our bot will be a collection of searchable questions and answers. It will be hosted in a QnA service in Azure. Click on Create a QnA service (button highlighted in pink below).

[![](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fejw4p8hr8z8gscqoloq0.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fejw4p8hr8z8gscqoloq0.png)

## [](#lets-provide-qna-maker-service-details)Let's Provide QnA Maker Service Details

Next, we’ll need to provide some details for the QnA Maker, including a unique name, Azure subscription, location, etc. Pictured below are my inputs. You’ll notice I’ve selected F0 for pricing (free tier) and have chosen West Coast (closest to my current location) for all locations. I’ve also created a new resource group called ChloBots (you can name yours whatever you’d like). For pricing tier, I’ve selected F (three indexes) which is the free tier for the search pricing tier. I have also disabled App Insights for this demo, but enabling is also an option if you'd like to have monitoring data (you can learn more about that [here](https://docs.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview#how-do-i-use-application-insights/?WT.mc_id=devto-blog-chcondon)).

[![](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F6cyrnvvs0ij0tpvpo3x9.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F6cyrnvvs0ij0tpvpo3x9.png)

Click **Create** at the bottom of the page, and in a minute or so you’ll have a resource created for the service.

## [](#lets-connect-our-qna-maker-service-to-the-knowledge-base)Let's Connect Our QnA Maker Service to the Knowledge Base

Head back to the [QnA Maker web portal](https://www.qnamaker.ai/Create). If you refresh the page, dropdown menus showing your account info will show up under Step 2. Select the Directory ID, subscription name, and QnA service (the ones we just selected/created in the Azure portal).

Scroll down to Step 3 and provide a unique name for your Knowledge Base. I'm naming mine 'BootcampBotFAQs'.

## [](#populate-knowledge-base)Populate Knowledge Base

Download [this Word doc](https://github.com/ChloeCodesThings/BootcampBot/raw/master/ChloeHackbrightFAQ.docx) of FAQs I've created (obviously, you can create your own set of FAQs or edit this file to customize it for your own bot). Under step 4, add the file in [QnAMaker](https://www.qnamaker.ai/Create).

Under Step 4, you can also choose the type of "Chit-chat" your bot will have. This will determine the personality of your bot. Options provided range from 'professional' to 'enthusiastic', or none at all. I'm going to go with 'friendly', since I want to make sure my bot is overwhelmingly welcoming and kind to everyone it encounters. 😁

If everything looks good on this page, go ahead and click **Create your KB**. After a short wait, we'll have a Knowledge Base and the **Edit** page will load.

### [](#lets-test-it-out)Let's Test it Out!

Believe it or not, our bot is already ready to test (told ya it was witchcraft 🔮)! In the top right corner, click **Test** and you can go ahead and test out your bot! Go ahead and ask it some commonly asked questions, and see its responses.

[![](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fi6gu1cwplf42wxco6gep.gif)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fi6gu1cwplf42wxco6gep.gif)

### [](#lets-publish-our-knowledge-base)Let's Publish Our Knowledge Base!

Once you've tested out your bot and you are confident in it's answers, we can go ahead and publish our knowledge base!

Head to the QnA Maker Knowledge page (the same one we've been testing in) and click **Publish** located at the top of the page. You'll be taken to a page letting you know that your Knowledge Base will no longer be in test mode, and it will become an endpoint you'll be able to use. If all goes smoothly to this point, you'll see a **Success!** page containing a URL.

### [](#lets-integrate)Let's Integrate!

In the [Azure portal](https://azure.microsoft.com/?WT.mc_id=devto-blog-chcondon), click on _Create a Resource_ on the lefthand side of the page. In the search bar enter "bot", and find **Web App Bot**. We'll now create a web site for our bot, and we'll also get it registered with [Azure Bot Service](https://docs.microsoft.com/en-us/azure/bot-service/?view=azure-bot-service-4.0/?WT.mc_id=devto-blog-chcondon). This looks similar to the QnA Maker Service we created earlier, but with a few minor adjustments. Provide a name (this must be unique!) for your bot (I'm naming mine "chloeslinebot"), and select your subscription and the resource group you used/created previously. Use S1 pricing tier, and under **Bot Template** select **SDK v3** and **C#** for language as well as **Question and Answer** for the template. We'll turn off Application Insights as well.

Once **Create** is clicked, it'll be ready in a few minutes!

When you get the notification that your deployment has been successful, navigate to the left hand navigation of your recently created **Configuration** section to view your **Application Settings**.

[![](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F3hb70jacozvhvwukjsn4.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F3hb70jacozvhvwukjsn4.png)

### [](#lets-connect-our-bot-to-our-qna-service)Let's Connect Our Bot to Our QnA Service!

Here's the part where we connect it all together 🤖 If you don't already have it open, create a new tab to sign into your [QnA Maker](https://www.qnamaker.ai/) account and find the details for your QnA Maker service that was published. In the Postman sample, find the GUID (this represents the knowledge base ID) and copy it. We'll paste that GUID and select the **Hidden Value** for **QnAKnowledgebaseId** in our **Application Settings**.

[![](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fxejpu57q1xbd62z1fdyq.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fxejpu57q1xbd62z1fdyq.png)

Do the same for the **QnAEndpointHostName** and **QnAAuthKey** in **Application Settings**. Save these settings, and find **Test in Web Chat** under the **Bot Management** section in the left side navigation. Our bot is now connected to our QnA Maker Service! 🎉 Test out the bot by asking it a question or two, and your bot should be up and running and at your service.

Congrats- you did it! You now have published a QnA Maker service that has been published on Azure. Your web chatbot has been integrated with QnA Maker and allows folks to chat in a interactive way with your bot. OK, that was a lot... let's take a look at that diagram again, shall we?

[![diagram](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F5izeykmxdbc234ek80o5.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F5izeykmxdbc234ek80o5.png)

### [](#lets-connect-it-to-twilio)Let's Connect it to Twilio!

Now we'll need to connect it to the proper Channel. I've decided to use [Twilio](https://www.twilio.com/referral/xBBj30) for this, since I'm familiar with their API. If you're unfamiliar, Twilio allows software developers to programmatically make and receive phone calls, send and receive text messages, and perform other communication functions using its web service APIs. Head over to Twilio, and set-up an account if you don't have one already (🙋‍♀️ FYI you can use code CHLOE20 for some free credits and sign up [here](https://www.twilio.com/referral/xBBj30)). You can use Twilio in all kinds of ways ([fake boyfriend apps](https://dev.to/azure/an-ambivert-s-guide-to-azure-functions-27b8) and [ADHD reminders](https://dev.to/azure/building-a-diy-adhd-medication-reminder-with-azure-functions-o70) to name a few 🤳)!

Once you've created a Twilio account, create a new project. We'll need a couple things to get our bot connected to Twilio:

*   A Twilio phone number
*   A Twilio Account Sid _(acts as a username for our Twilio app)_
*   A Twilio Auth Token _(acts as a password)_

Give your project a unique name (I named mine "BootcampBot"), and you'll be taken to your dashboard. In the left-hand side navigation, click on the **Phone Numbers** section (labeled as **"#"**\-- can't find it? it may be hiding behind the _"..."_ icon that you need to expand!). Click on **Buy a Number** and hit the **Search** button. Once you find a number that suits your needs (the area code doesn't matter, but it **will** need texting capabilities!), click **Buy** (note: phone numbers typically cost about $1-$2 monthly).

### [](#lets-create-a-twiml-app)Let's Create a TwiML App!

Now we need to [create a TwiML app](https://docs.microsoft.com/en-us/azure/bot-service/bot-service-channel-connect-twilio/?WT.mc_id=devto-blog-chcondon) so we can give it a Request URL (in this case, _[https://sms.botframework.com/api/sms](https://sms.botframework.com/api/sms)_) for messaging with Twilio. In the [Twilio console](https://www.twilio.com/console) click through to Programmable **Messaging > Tools > TwiML Apps**. Click the red ➕ sign icon, or **Create new TwiML App**.

Fill out the TwiML App form with a friendly name, and under **Messaging** add **[https://sms.botframework.com/api/sms](https://sms.botframework.com/api/sms)** as the **Messaging Request URL** (HTTP POST).

Lastly, navigate back to the Azure portal, select **Channels** (under **Bot Management** and add your Twilio credentials to your Azure Web App Bot like so:

[![](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F2d8td00ot1pjyss5ax2x.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F2d8td00ot1pjyss5ax2x.png)

**NOTE**: _Make sure you keep your Twilio SID + Auth Token private and secure!_

To test that all is working smoothly with your bot, text a question to your Twilio phone number, and enjoy! You've successfully built a QnA Bot with Azure, and hooked it up to Twilio- **SUCCESS!** 🎉

Here's a video of my bot in action (I've added the bot to my contacts as "🤖 Bootcamp Bot 🤖".

YES! Our bot is alive!

[![](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Flul7a0p2lnndcqqx8f17.gif)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Flul7a0p2lnndcqqx8f17.gif)

If you've made it this far, congrats on making your first basic bot. As you can see, [QnA Maker](https://www.qnamaker.ai/) is an incredibly simple way to create a basic bot to manage commonly asked questions for customers, friends, family members, or bootcamp-curious folks. Do you have an FAQ page on your site? Then you can build a bot for it!

As always, here to answer any questions, tackle any bugs, or help you build your own. Comment below, or reach out on Twitter if you get stuck! I'm here to help. 🤖💖 -Chloe
