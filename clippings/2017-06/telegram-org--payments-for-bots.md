---
url: "https://telegram.org/blog/payments"
captured_at: "2017-06-01T15:03:31-03:00"
title: "Payments for Bots"
domain: "telegram-org"
---

# Payments for Bots

![3c5b8d2945aa66354907d96c749b777f.png](telegram-org--payments-for-bots/3c5b8d2945aa66354907d96c749b777f.png)

> Note: Today’s update includes two other major features in addition to payments. Don't miss [**Video Messages + Telescope**](https://telegram.org/blog/video-messages-and-telescope) and the [**Instant View Platform**](https://telegram.org/blog/instant-view-contest-200K)!

[![deb035e8a54ed594230a1a7a9408b387.png](telegram-org--payments-for-bots/deb035e8a54ed594230a1a7a9408b387.png)](https://telegram.org/file/811140819/2/35lGXQhh0BE.186683/c2d4dcc9207478f815)

Imagine a world where you can order pizza, pay for a pair of shoes, hire a cab, or refill your subway pass — all in a few button taps on Telegram.

To make this world possible, we are launching [**Bot Payments**](https://core.telegram.org/bots/payments) today. Bot developers can now **accept payments** from their users around the world, just like that:

[📎 YYY](telegram-org--payments-for-bots/d2a9582603d498c128a61ccd5d7e7bb2.bin)

If you have Telegram 4.0 (or newer) installed, you can order goods or services from bots that offer them. These bots may now add a **Pay button** to their messages. When you tap **Pay**, you'll be asked to fill in your credit card and shipping information and confirm the payment. Then you get what you paid for. Voila!

If your account is protected by [2-Step Verification](https://telegram.org/blog/sessions-and-2-step-verification#two-step-verification), you can **save** your card for future purchases. If you do that, ordering stuff from bots will only take two taps. Bot Payments also support Apple Pay for a completely frictionless experience.

### Check It Out Now

Try our demo [**@ShopBot**](https://t.me/shopbot) to get a taste of what‘s coming. (Note: Our demo bot thinks it sells time machines, but they’re **not** a part of what‘s coming. Sadly.) If you’re looking to test a real payment with actual money, stop by our [**@TelegramDonate**](https://t.me/telegramdonate) bot.

Telegram is an open platform, so bot developers can implement the necessary APIs and accept payments from users starting right now, without lengthy approval dramas. If you’re a **bot developer**, check out [the docs](https://core.telegram.org/bots/payments) immediately!

### Behind the Scenes

[![e14e0ca1ea714c3136af2570ef9f0d42.png](telegram-org--payments-for-bots/e14e0ca1ea714c3136af2570ef9f0d42.png)](https://telegram.org/file/811140227/2/ZTXUngAbELM.193805/ba6aa233d1d4206207)

Currently, most of the payments are handled by [**Stripe**](https://stripe.com/), but Telegram Bot Payments are a **platform for payment providers** all over the world. When accepting a payment from a user, the bot developer can choose between all available payment providers, selecting the one already used by the buyer or the one with the lowest commission.

[Stripe](https://stripe.com/) is just the beginning. In the next few days, payments will become available to developers in India via [Razorpay](http://razorpay.com/), in Nigeria, Kenya, Ghana, South Africa, and Uganda via [Flutterwave](https://www.flutterwave.com/), and in over **190** other countries via [Paymentwall](https://www.paymentwall.com/).

[Yandex.Money](https://money.yandex.ru/new) and [Qiwi](https://qiwi.ru/) for Russia and [Payme](https://payme.uz/) for Uzbekistan will be joining the club a little later. Follow our [**@BotNews**](https://t.me/botnews) channel to be the first to know about new providers joining.

If you’re a payment provider (especially in a developing country), [click here](https://core.telegram.org/bots/payments#how-do-i-join-as-a-payment-provider) to learn how to get on board.

### Just Passing Through

Telegram acts as a messenger (pun intended) between the paying user, the bot developer, and their chosen payment system. The user sends their credit card details directly to the payment system. Then the payment system's response and the shipping details entered by the user are passed to the bot developer so that they can process the order.

Due to this structure, it is impossible for Telegram to handle complaints or cashbacks – any disputed payments are the responsibility of the bot developers, payment providers, and banks that participated in the exchange.

Since Telegram doesn‘t process the payments, we don’t store and can‘t access any sensitive data. We also don’t take any commission from payments and don't profit from these transactions.

Instead, we just do what every sheriff has to do with strangers passing through their turf: shoot the bad bots and award the good ones with a badge. We’re sure there’ll be plenty of good ones.

### If You Are…

- **…one of our lovely users**, wait and see what wonders Telegram bot developers will soon bring your way using this new platform. Meanwhile, try our demo [@ShopBot](https://t.me/shopbot) to get an idea of what's coming or try spending some real money via [@TelegramDonate](https://t.me/telegramdonate).
- **…a bot developer**, check out our [Introduction to Payments](https://core.telegram.org/bots/payments) and [Payments API](https://core.telegram.org/bots/api#payments) to see what you can build.
- **…a payments provider**, [learn how to get on board](https://core.telegram.org/bots/payments#how-do-i-join-as-a-payment-provider).

And if you're none of the above for some weird reason, **be a user**, [do the right thing](https://telegram.org/apps). Happy shopping, everyone!

*May 18, 2017  
The Telegram Team*
