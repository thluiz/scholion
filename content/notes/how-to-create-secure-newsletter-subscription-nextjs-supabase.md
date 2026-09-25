---
title: "How to Create a Secure Newsletter Subscription with NextJS, Supabase, Nodemailer and Arcjet 🔐💯"
date: '2026-09-25T00:33:15+01:00'
category: webclip
summary: 'Tutorial shows how to build a newsletter form with NextJS, Supabase, Nodemailer, and Arcjet, using double opt-in, email validation, rate limiting, and bot protection.'
tags: ["nextjs","supabase","arcjet","nodemailer"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "How to Create a Secure Newsletter Subscription with NextJS, Supabase, Nodemailer and Arcjet 🔐💯"
    url: "https://dev.to/madza/how-to-create-a-secure-newsletter-subscription-with-nextjs-supabase-nodemailer-and-arcjet-3ll7?context=digest"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/dev-to--how-to-create-secure-newsletter-subscription-nextjs-supabase.md"
    kind: repo
---

The guide explains how to build a custom newsletter subscription app from scratch with NextJS, Supabase, Nodemailer, and Arcjet. It focuses on solving spam sign-ups, poor email validation, bot traffic, and other common issues through server-side checks and a double opt-in flow.

It also walks through the app structure, the UI states for landing, pending, error, and confirmation, and the backend routes for submission and confirmation. The setup uses Arcjet for protection rules, Supabase for subscriber storage, and Nodemailer for sending confirmation emails.

## Reading notes

- A newsletter can help engage an audience, generate traffic, and build a loyal community around a brand.
- Free solutions tend to suffer from spam sign-ups, poor email validation, and insufficient bot protection.
- The tutorial proposes creating a subscription app from scratch and addressing these problems with security and validation measures.
- The stack includes interface and API in NextJS, backend in Supabase, confirmation sending with Nodemailer, and protection with Arcjet.
- The final app uses double opt-in to confirm the subscription by email.
- The text presents Arcjet as an integrated security solution as a dependency, without requiring agents or complex infrastructure.
- Arcjet is used for email format validation, rate limiting, bot detection, and protection against common web attacks.
- The interface is divided into four states: landing, pending, error, and confirmation.
- In the initial state, there is an email field and a submit button.
- In the pending state, the user is told that the process is in progress and should check email.
- In the error state, the interface shows that the subscription failed.
- In the confirmation state, the message says that the email was registered.
- The NextJS project is created with `create-next-app`, and the development server is started with `npm run dev`.
- The tutorial asks for five icons, including images for the newsletter states and a GIF for loading.
- The Arcjet configuration file uses shield, bot detection, fixed window of 3 requests in 2 minutes, and email validation rules.
- The Arcjet rules are configured in `LIVE` mode, with a `DRY_RUN` option for testing or debugging.
- Nodemailer is configured with SMTP variables and a `BASE_URL` address.
- The sending function builds the confirmation email with a link to `/api/confirm?token=...`.
- In Supabase, the text creates the `pending_subscriptions` table with `token`, `email`, and `link_sent_at`.
- It also creates the `subscribers` table with `email` and `confirmed_at`.
- The Supabase client is initialized with the project URL and key from the environment file.
- The `/api/submit` route handles GET and POST requests, applies Arcjet protection, and returns errors for suspicion, bot, rate limit, and email issues.
- Before inserting a new sign-up, the server checks whether the email already exists in the `subscribers` table.
- If the email does not already exist, the application generates a UUID, inserts the data into `pending_subscriptions`, and sends the opt-in email.
- The `/api/confirm` route reads the token from the query string, looks up the record in `pending_subscriptions`, inserts the email into `subscribers`, and removes the pending record.
- The main page uses client state to switch between loading, sending, error, and confirmation, and also reads the `approved` parameter in the URL.
- The form sends the email by `fetch` to `/api/submit` and updates the message according to the response.
- The text shows tests for attack protection, bot detection, email validation, request limiting, duplicate checking, and the complete confirmation flow.
