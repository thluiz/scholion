---
url: "https://blog.bytebytego.com/p/ep130-design-a-system-like-youtube?ref=dailydev"
captured_at: "2026-09-23T18:49:10+01:00"
title: "EP130: Design a System Like YouTube - ByteByteGo Newsletter"
domain: "blog.bytebytego.com"
---

Discover more from ByteByteGo Newsletter
Explain complex systems with simple terms, from the authors of the best-selling system design book series. Join over 1,000,000 friendly readers.
Subscribe
By subscribing, you agree Substack's Terms of Use, and acknowledge its Information Collection Notice and Privacy Policy.
Already have an account? Sign in
EP130: Design a System Like YouTube
BYTEBYTEGO
SEP 21, 2024
237
2
16
Share
✂️Cut your QA cycles down to minutes with QA Wolf (Sponsored)

If slow QA processes bottleneck you or your software engineering team and you're releasing slower because of it — you need to check out QA Wolf.

Their AI-native approach gets engineering teams to 80% automated end-to-end test coverage and helps them ship 2x faster by reducing QA cycles from hours to minutes.

QA Wolf takes testing off your plate. They can get you:

Unlimited parallel test runs

24-hour maintenance and on-demand test creation

Human-verified bug reports sent directly to your team

Zero flakes guaranteed

The benefit? No more manual E2E testing. No more slow QA cycles. No more bugs reaching production.

With QA Wolf, Drata's team of 80+ engineers achieved 4x more test cases and 86% faster QA cycles.

Schedule a demo to learn more

This week's system design refresher:

Introduction to Generative AI (Youtube video)

Iterative, Agile, Waterfall... What are the differences between these Software Development Life Cycle models?

How to Design a System Like YouTube?

SPONSOR US

Introduction to Generative AI
Iterative, Agile, Waterfall... What are the differences between these Software Development Life Cycle models?

The Software Development Life Cycle (SDLC) is a framework that outlines the process of developing software in a systematic way. Here are some of the most common ones:

Waterfall Model:
- A linear and sequential approach.
- Divides the project into distinct phases: Requirements, Design, Implementation, Verification, and Maintenance.


Agile Model:
- Development is done in small, manageable increments called sprints.
- Common Agile methodologies include Scrum, Kanban, and Extreme Programming (XP).


V-Model (Validation and Verification Model):
- An extension of the Waterfall model.
- Each development phase is associated with a testing phase, forming a V shape.


Iterative Model:
- Focuses on building a system incrementally.
- Each iteration builds upon the previous one until the final product is achieved.


Spiral Model:
- Combines iterative development with systematic aspects of the Waterfall model.
- Each cycle involves planning, risk analysis, engineering, and evaluation.


Big Bang Model:
- All coding is done with minimal planning, and the entire software is integrated and tested at once.


RAD Model (Rapid Application Development):
- Emphasizes rapid prototyping and quick feedback.
- Focuses on quick development and delivery.


Incremental Model:
- The product is designed, implemented, and tested incrementally until the product is finished.


Each of these models has its advantages and disadvantages, and the choice of which to use often depends on the specific requirements and constraints of the project at hand.

Latest articles

If you're not a paid subscriber, here's what you missed.

The Saga Pattern

Infrastructure as Code

A Crash Course on Scaling the Data Layer

A Crash Course on Load Balancers for Scaling

A Crash Course on Scaling the API Layer

To receive all the full articles and support ByteByteGo, consider subscribing:

Subscribe
How to Design a System Like YouTube?

Here's a 9-step process:

The user creates a video upload request and provides the video files along with the details about the video.

The raw video files are uploaded to an Object Storage (such as S3).

Also, the metadata is saved in a database as well as a cache for faster retrieval when needed.

The raw video files are sent for transcoding to a special transcoding server. Transcoding is the process of encoding the videos into compatible bitrates and formats for streaming.

The transcoded video is uploaded to another object storage.

The notification for transcoding completion is sent to a special service via a message queue.

The Transcoding Status Handler updates the metadata DB and cache with the latest details of the video.

The user raises a video streaming request that goes to a Content Delivery Network (CDN).

The CDN fetches the video from the object storage for streaming. It also caches the video locally for subsequent streaming requests.

Over to you: What else would you add to make the YouTube-like system?

SPONSOR US

Get your product in front of more than 1,000,000 tech professionals.

Our newsletter puts your products and services directly in front of an audience that matters - hundreds of thousands of engineering leaders and senior engineers - who have influence over significant tech decisions and big purchases.

Space Fills Up Fast - Reserve Today

Ad spots typically sell out about 4 weeks in advance. To ensure your ad reaches this influential audience, reserve your space now by emailing sponsorship@bytebytego.com

Subscribe to ByteByteGo Newsletter
Explain complex systems with simple terms, from the authors of the best-selling system design book series. Join over 1,000,000 friendly readers.
Subscribe
By subscribing, you agree Substack's Terms of Use, and acknowledge its Information Collection Notice and Privacy Policy.
237 Likes
∙
16 Restacks
237
2
16
Share
