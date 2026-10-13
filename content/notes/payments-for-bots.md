---
title: "Payments for Bots"
date: '2017-06-01T15:03:31-03:00'
category: webclip
summary: 'Telegram launches Bot Payments so bots can accept payments through a Pay button, with saved cards and Apple Pay, while payment providers and developers handle the transaction flow.'
tags: ["bot-payments", "telegram-bots", "payments", "bot-framework"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Payments for Bots"
    url: "https://telegram.org/blog/payments"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2017-06/telegram-org--payments-for-bots.md"
    kind: repo
---

Telegram introduces Bot Payments, letting bots sell goods or services through a Pay button in messages. Users enter card and shipping details, can save cards with 2-Step Verification, and may pay with Apple Pay.

## Reading notes

- Bots can now accept payments from users around the world through Telegram 4.0 or newer.
- A bot message can include a Pay button that opens checkout for credit card and shipping information.
- Users with 2-Step Verification can save a card and complete future purchases in two taps.
- Apple Pay is supported for a smoother payment flow.
- Developers can try @ShopBot for a demo and @TelegramDonate for a real payment test.
- Telegram says bot developers can start using the APIs without long approval delays.
- Most payments are handled by Stripe, but the platform is meant to work with different payment providers.
- Telegram says the bot developer can choose among available providers, including one already used by the buyer or the one with the lowest commission.
- Payments were announced for India via Razorpay, several African countries via Flutterwave, and over 190 other countries via Paymentwall.
- Telegram says it does not process payments, store sensitive data, take commission, or handle complaints and cashbacks.
- Disputed payments are the responsibility of bot developers, payment providers, and banks involved in the exchange.
