---
title: "To Serialize or Not to Serialize: ActiveModel Serializers"
date: '2015-06-26T12:34:33-03:00'
category: webclip
summary: 'The post explains why a Rails API response should be serialized for a JavaScript front end, then shows how ActiveModel Serializers lets you whitelist fields, shape associations, and customize JSON output.'
tags: ["rails", "ruby", "json", "active-model-serializers"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "To Serialize or Not to Serialize: ActiveModel Serializers - Words and Code"
    url: "http://vaidehijoshi.github.io/blog/2015/06/23/to-serialize-or-not-to-serialize-activemodel-serializers"
    kind: repo
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-06/vaidehijoshi-github-io--to-serialize-or-not-to-serialize-activemodel-serializers.md"
    kind: repo
---

The post argues that raw Rails JSON is often too verbose for an Ember front end, especially when it includes fields like timestamps, full user objects, and full book records. ActiveModel Serializers is presented as the way to shape that response into the structure the client actually needs.

## Reading notes

- The example starts with a Rails app that returns a user's wish lists as JSON for an Ember front end.
- The initial JSON includes more data than needed, such as created and updated timestamps, full user data, and full book data.
- The post says the front end only needs selected fields, such as `user_id` and `book_ids`.
- `active_model_serializers` is added to the Gemfile and installed with Bundler.
- A serializer is generated for `WishList`, along with an `application_serializer`.
- The generated `WishListSerializer` whitelists attributes and recognizes `has_many` and `belongs_to` associations.
- The first serialized response is grouped under a `wish_lists` key.
- The serializer is then adjusted to replace `belongs_to :user` with a `user_id` attribute.
- A `BookSerializer` is generated so books can be customized separately.
- The post shows a private `books` method in `WishListSerializer` that instantiates `BookSerializer` for each associated book.
- Changing `BookSerializer` changes the book data returned through the wish list serializer.
- The controller action does not need to change; Rails finds and uses the serializer automatically.
- The post notes that different serializers can be used for the same object type, including a more detailed book serializer when needed.
- It ends by pointing to documentation and related posts about serializers and caching.
