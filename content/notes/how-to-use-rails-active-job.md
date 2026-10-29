---
title: "How to use Rails Active Job"
date: '2015-08-27T09:03:46-03:00'
category: webclip
summary: 'The article explains how Rails Active Job standardizes queue adapters and shows when to move work off the request cycle for faster responses, steadier load, and background processing.'
tags: ["rails", "active-job", "background-jobs", "queues"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "How to use Rails Active Job"
    url: "http://blog.codeship.com/how-to-use-rails-active-job/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-08/blog-codeship-com--how-to-use-rails-active-job.md"
    kind: repo
---

Active Job standardizes access to queue backends in Rails, including Sidekiq, Resque, and Delayed Job. It can also run jobs immediately with the Inline adapter, and the article shows the basic flow for generating jobs, enqueuing them, and choosing a queue backend in app configuration.

## Reading notes

- Active Job was added in Rails 4.2 to standardize the interface to existing queueing options.
- It works through a single interface with multiple backends, including Sidekiq, Resque, and Delayed Job.
- The Inline backend executes enqueued jobs immediately.
- The `rails g job` generator creates both the job class and a test stub.
- `perform_later` adds a job to the queue as soon as a worker is available.
- Some backends accept time parameters so a job can run later.
- The job class defines `perform`, which receives the arguments passed when the job was enqueued.
- Sidekiq and Resque use Redis to store queued items.
- The queue adapter is set in the application config, such as `config.active_job.queue_adapter = :sidekiq`.
- Sidekiq and Resque both provide web interfaces for checking workers and queued jobs.
- The article treats email delivery as a common background task and recommends changing `deliver_now` to `deliver_later`.
- It says images can be processed in the background with tools like Delayed Paperclip and CarrierWave Backgrounder.
- For uploaded files, the workflow is to accept the file, upload it to storage, enqueue processing, show the user a success page, and let a worker process it.
- Large reports can also be generated in the queue and then delivered through a link or email.
- External APIs should be called in the background when possible because they can be slow and affect response time.
- The example job receives an IP address, adjusts it for localhost testing, and passes it to a class that performs the API call.
- The article shows a job that notifies users after a tweet is created.
- GlobalID lets Rails pass the full object to the worker instead of passing only an ID and reloading the record.
