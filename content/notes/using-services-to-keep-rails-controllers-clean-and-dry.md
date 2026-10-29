---
title: "Using Services to Keep Your Rails Controllers Clean and DRY"
date: '2015-01-28T09:30:54-03:00'
category: webclip
summary: 'The article argues for moving controller-adjacent work into service objects, keeping Rails controllers thin while models stay focused on business objects and external integrations stay isolated.'
tags: ["rails", "service-objects", "controllers", "testing"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Using Services to Keep Your Rails Controllers Clean and DRY"
    url: "https://blog.engineyard.com/2014/keeping-your-rails-controllers-dry-with-services"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-01/blog-engineyard-com--using-services-to-keep-rails-controllers-clean-and-dry.md"
    kind: repo
---

The article argues that Rails controllers get crowded when they absorb logic for mailers, Stripe, and other APIs. It suggests creating more folders than Rails provides by default, with actions, decorators, policies, support, and a services folder reserved for external systems.

## Reading notes

- Controller code grows when it has to coordinate mailers, Stripe, and other external APIs.
- The article prefers not to push all of that logic into models, since models should stay close to business objects.
- It recommends creating additional folders in app instead of limiting the project to Rails’ default structure.
- It uses actions for things like creating invoices and services for objects that talk to external systems such as Stripe, AWS, or geolocation services.
- The example service object is a plain Ruby object that wraps Stripe calls behind methods like charge! and create_customer!.
- The service accepts charge amount, card token, and email through dependency injection.
- The controller calls the service and keeps registration logic private.
- The service is tested with a test/services folder and mocked Stripe expectations.
- The article closes by saying that skinny controllers and DRY code come from choosing the right place for each piece of logic.
