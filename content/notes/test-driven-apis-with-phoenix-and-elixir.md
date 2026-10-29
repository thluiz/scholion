---
title: "Test-Driven APIs with Phoenix and Elixir"
date: '2016-01-25T08:48:07-03:00'
category: webclip
summary: 'The tutorial uses TDD to build a Phoenix API for listing movies, adding dependencies, routes, a controller, a view, and a model while showing how each test failure guides the next change.'
tags: ["tdd", "phoenix", "elixir", "api"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Test-Driven APIs with Phoenix and Elixir"
    url: "https://semaphoreci.com/community/tutorials/test-driven-apis-with-phoenix-and-elixir"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2016-01/semaphoreci-com--test-driven-apis-with-phoenix-and-elixir.md"
    kind: repo
---

The tutorial builds an API by starting with a failing integration test and changing the code only when the test points to what is missing. It shows how that process helps the author understand Phoenix and Elixir components while adding the movies endpoint.

## Reading notes

- Start a new Phoenix project without HTML and Brunch because the goal is an API, not pages or stylesheets.
- Create the first integration test for a GET request to /movies and use the failures to discover what needs to be added next.
- Add Plug.Test, a router call, a route for /movies, a controller, and a view until the endpoint returns a response.
- Add a Movie model with name and rating, then use the generator and migrations to make the struct available in the test.
- Encode the movie and the controller output with Poison so the response becomes valid JSON instead of a raw struct.
- Update the integration test to compare the response with the encoded movie list.
- Fix the error view tests so JSON error rendering matches the expected map shape.
- The article closes by saying that TDD gives fast feedback and helps move forward more confidently when learning new tools.
