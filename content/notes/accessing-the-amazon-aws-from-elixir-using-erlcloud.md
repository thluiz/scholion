---
title: "Accessing the Amazon AWS from Elixir (using erlcloud)"
date: '2015-04-30T13:10:11-03:00'
category: webclip
summary: 'The post explains how to use the Erlang library erlcloud from Elixir to reach AWS, configure credentials, and run basic S3 calls such as creating buckets, listing objects, and reading content.'
tags: ["elixir", "aws", "s3", "erlcloud"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Accessing the Amazon AWS from Elixir (using erlcloud)"
    url: "http://blog.jordan-dimov.com/accessing-the-amazon-aws-from-elixir-using-erlcloud/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-04/blog-jordan-dimov-com--accessing-the-amazon-aws-from-elixir-using-erlcloud.md"
    kind: repo
---

The post says Amazon does not yet provide an official Elixir SDK for AWS, but erlcloud already makes a lot possible. It presents a quick guide focused on S3 and notes that the library documentation is thin, so the examples are meant to fill that gap.

## Reading notes

- Add `erlcloud` to `mix.exs`, start the `ssl` and `erlcloud` applications, then run `mix deps.get` and `mix deps.compile`.
- Store AWS credentials in environment variables and pass them to `:erlcloud_s3.configure/2` from Elixir.
- Convert Elixir strings to char lists before passing them to Erlang functions.
- Create an S3 bucket with `:erlcloud_s3.create_bucket/1` and use a unique name because bucket names are shared across accounts.
- List buckets with `:erlcloud_s3.list_buckets/0` and list objects with `:erlcloud_s3.list_objects/1`.
- Store a value with `:erlcloud_s3.put_object/3` and read it back with `:erlcloud_s3.get_object/2`.
- Use an Elixir comprehension over `objects[:contents]` to get a cleaner list of keys.
- The post ends by pointing readers to the `erlcloud` source code for the full set of S3 functions.
