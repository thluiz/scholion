---
title: "What are some of the things about Ruby on Rails that most developers don't know?"
date: '2015-08-09T17:43:18-03:00'
category: webclip
summary: 'The page points out two Rails details: ActiveRecord::Relation#to_sql exposes the SQL behind a query, and association conditions can reuse a model''s own where_values_hash instead of hard-coding schema details.'
tags: ["ruby-on-rails", "activerecord", "associations"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "(1) What are some of the things about Ruby on Rails that most developers don't know? - Quora"
    url: "http://www.quora.com/What-are-some-of-the-things-about-Ruby-on-Rails-that-most-developers-dont-know"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-08/quora-com--what-are-some-of-the-things-about-ruby-on-rails-that-most-de.md"
    kind: repo
---

The page highlights two Rails details that many developers may miss. One is that an ActiveRecord relation can be turned into its underlying SQL with `ActiveRecord::Relation#to_sql`. The other is a way to define filtered associations without hard-coding a model's schema details, while still keeping association-specific behavior available.

## Reading notes

- `ActiveRecord::Relation#to_sql` returns the SQL for a relation, as shown with `User.where(:first_name => 'Jim').order(:created_at).to_sql`.
- For a `User#published_posts` association, the page compares a direct filtering approach with an association declaration that uses `:where => published.where_values_hash`.
- The point of that approach is to avoid repeating `:published => true` and to keep the class from hard-coding the other class's schema.
- The example also says this preserves association-specific features such as eager loading.
- The page frames the second point as keeping the Law of Demeter intact.
