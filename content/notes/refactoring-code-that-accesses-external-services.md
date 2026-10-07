---
title: "Refactoring code that accesses external services"
date: '2015-02-19T22:25:53-03:00'
category: webclip
summary: 'The article shows how to refactor code that mixes YouTube access, data translation, and domain logic into separate connection, gateway, domain, and coordinator objects, using small behavior-preserving steps and tests.'
tags: ["refactoring", "external-services", "gateway", "domain-objects"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Refactoring code that accesses external services"
    url: "http://martinfowler.com/articles/refactoring-external-service.html"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-02/martinfowler-com--refactoring-code-that-accesses-external-services.md"
    kind: repo
---

The article argues that code which collaborates with external services should separate access code from domain logic. Using a Ruby example that reads local video data, calls YouTube, and computes monthly views, it shows how small refactorings move responsibilities into distinct objects so the coordinator stays focused on orchestration.

## Reading notes

- External service access is separated because it mixes different concerns with domain logic.
- The first refactoring extracts the YouTube interaction into its own method so it can be stubbed.
- A test double is introduced to make the YouTube response deterministic.
- Date.today is also stubbed so the test does not depend on time.
- The remote call is then moved into a YoutubeConnection object.
- The connection object is treated as a humble object, with parsing moved to the caller.
- A YoutubeGateway translates YouTube data into the structure the application wants.
- The gateway hides where view counts and published dates live in the YouTube response.
- A Video domain object is introduced to hold local video data.
- The monthly view calculation is moved into Video with an enrich_with_youtube method.
- The service method is simplified to coordinate Video objects and gateway items.
- The final arrangement is coordinator, domain object, gateway, and connection.
- The article notes that different systems may move responsibilities differently.
- It suggests keeping naming conventions consistent for object roles.
- Existing tests may remain enough after the refactoring, with new tests added only when new behavior appears.
- The article stresses that refactoring means many small behavior-preserving steps, not arbitrary restructuring.
