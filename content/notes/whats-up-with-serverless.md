---
title: "What’s Up With Serverless?"
date: '2023-06-26T18:08:20+00:00'
category: webclip
summary: 'The page argues that new software should start serverless to cut operational costs, improve reliability, and let teams focus on product work while cloud services handle scaling and infrastructure.'
tags: ["serverless", "nextjs", "vercel", "cloud-services"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "What’s Up With Serverless? - JavaScript Scene - Medium"
    url: "https://medium.com/javascript-scene/whats-up-with-serverless-1b9bfa80f21f"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2023-06/medium-com--whats-up-with-serverless.md"
    kind: repo
---

The page argues that serverless should be the default for new products because it reduces the cost and burden of operations, scales with demand, and lets teams move faster while they search for product-market fit. It frames serverless as a practical way to avoid managing always-on servers for most applications.

## Reading notes

- The author says Adobe Creative Cloud needed expensive ongoing server operations when it was rebuilt with Node, including uptime checks, autoscaling, release trains, logging, database scaling, and load testing.
- The argument is that a similar product built today could run on a fraction of that budget and still get scalability automatically.
- Serverless is defined as building with third-party backend services and APIs instead of traditional server infrastructure and maintenance.
- The page lists reduced operational costs, higher developer productivity, and increased reliability as the main benefits.
- It says serverless does not mean there are no servers, only that the provider manages them and the app uses functions and queries instead of always-on web servers.
- It notes that always-on or long-running workloads, such as some game servers or custom-hardware optimization, may still need servers.
- For application framework and deployment, the page recommends Vercel and Next.js.
- It describes Next.js as serverless-native and mentions serverless functions, edge functions, SSR, static edge deployment, incremental static regeneration, image optimization, bundle splitting, cache management, and page-load optimization.
- The author says Next.js on Vercel produced strong performance without special optimization work in one of his own projects.
- For authentication, the page says passwords are obsolete and unsafe, and it advises never to build authentication yourself.
- It recommends Magic for authentication and says Google social auth or Firebase social auth are also acceptable, while username/password flows should be avoided.
- For databases, the page prefers Fauna for GraphQL support, event streaming, scalability, low-latency reads and writes, and reliability.
- For content management, it recommends Notion with its API, combined with Next.js incremental static generation and on-demand revalidation.
- For commerce, it recommends Stripe for subscriptions and payments, Shopify or BigCommerce for more complex commerce, and Magic Connect for crypto fiat onramps.
- For media and storage, it recommends Next.js image optimization for owned content, Cloudinary for user-generated media, and NFT.storage for permanent immutable NFT storage.
