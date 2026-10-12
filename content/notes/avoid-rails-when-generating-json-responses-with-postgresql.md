---
title: "Avoid Rails When Generating JSON responses with PostgreSQL"
date: '2014-06-21T20:51:17-03:00'
category: webclip
summary: 'The article argues that moving JSON generation into PostgreSQL removes expensive Ruby object creation and Rails serialization work, cutting response times and memory use for API payloads.'
tags: ["postgresql", "rails", "json-serialization", "active-model-serializers"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Avoid Rails When Generating JSON responses with PostgreSQL"
    url: "http://reefpoints.dockyard.com/2014/05/27/avoid-rails-when-generating-json-responses-with-postgresql.html"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2014-06/reefpoints-dockyard-com--avoid-rails-when-generating-json-responses-with-postgresql.md"
    kind: repo
---

The article argues that Rails spends most of its time converting database rows into Ruby objects and then back into JSON. By having PostgreSQL generate the JSON response directly, ActiveRecord can receive a single JSON string instead of a set of model instances, which reduces CPU work, memory use, and garbage collection.

It compares this approach with ActiveModel::Serializers and reports large speedups in test cases, including roughly 160X on a large dataset and smaller but still significant gains on a smaller one. It then shows how PostgresExt-Serializers monkey patches AMS so JSON generation can be pushed into PostgreSQL, using CTEs, `array_agg`, `row_to_json`, `array_to_json`, and `coalesce` to assemble notes, tag ids, and tags into one JSON object.

## Reading notes

- Rails typically receives the request, builds a query with ActiveRecord, and then serializes the result into JSON after PostgreSQL has already returned rows.
- Most of the time in that flow is spent creating model objects and serializing them again for the response.
- If PostgreSQL generates the JSON payload, ActiveRecord can deserialize the protocol response as a single string instead of many objects.
- The approach removes two steps from the usual response cycle and lowers memory pressure from short-lived Ruby objects.
- The article reports a test with 1000 notes and 10000 tags where Rails and ActiveModel::Serializers took about 9 seconds.
- The same dataset with PostgreSQL-generated JSON returned in 72 milliseconds on the first request and 54 milliseconds on a repeated request.
- On a smaller dataset of 10 notes and 100 tags, Rails-side JSONification took 187 and 118 milliseconds.
- The PostgreSQL version took 92 and 12 milliseconds on that smaller dataset.
- PostgresExt-Serializers is presented as a gem that monkey patches ActiveModel::Serializers and sends serialization work to PostgreSQL.
- The example uses an Ember app that needs notes, their tag ids, and a side-loaded list of tags.
- The query is built with CTEs to gather note ids, group tag ids by note id, filter note records, build JSON arrays for notes and tags, and combine them into one JSON object.
- `coalesce` is used so notes without tags still return an empty array.
- `LEFT OUTER JOIN` keeps notes even when they have no tags, while `INNER JOIN` would drop them.
- `row_to_json`, `array_agg`, and `array_to_json` are used together to turn rows into JSON objects and then into JSON arrays.
