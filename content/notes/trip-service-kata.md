---
title: "TripService kata"
date: '2020-07-05T14:11:19+00:00'
category: webclip
summary: 'A legacy-code exercise where the goal is to write tests for TripService, reach full coverage, and then refactor the code so it clearly expresses the business rules.'
tags: ["legacy-code", "testing", "refactoring"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "GitHub - sandromancuso/trip-service-kata: Kata for a legacy code hands-on session. The objective is to write tests and refactor the given legacy code."
    url: "https://github.com/sandromancuso/trip-service-kata"
    kind: repo
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/github-com--trip-service-kata.md"
    kind: repo
---

Kata for a legacy code hands-on session. The goal is to test the legacy TripService class, reach 100% coverage, and then refactor the code so both tests and production code clearly express the business rules.

The exercise describes a social networking site for travellers. Users must be logged in to see content, must be friends to see another user's trips, and the code throws an exception when the user is not logged in. Unit tests for TripService must avoid the real UserSession and TripDAO because they depend on resources such as HTTP session and database.

## Reading notes

- Write tests for TripService until coverage reaches 100%
- Refactor only after the class is covered by tests
- Keep the public interface of TripService unchanged
- Do not introduce state in TripService
- The final code should make the business rules explicit
- Unit tests should not call the real UserSession or TripDAO
- The exercise focuses on TripService itself, not on external resources
