---
title: "Input fields in rake task"
date: '2015-07-10T12:40:14-03:00'
category: webclip
summary: 'The post shows how to make a Rake task ask for a customer name and email at runtime by reading from STDIN and using chomp before saving the data to a YAML file.'
tags: ["rake", "ruby", "stdin", "yaml"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Input fields in rake task - aross.se"
    url: "http://aross.se/2014/09/21/input-fields-in-rake-task.html"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-07/aross-se--input-fields-in-rake-task.md"
    kind: repo
---

The post starts from a Rake task that adds a new customer to a YAML file, then shows how to make the task interactive instead of hardcoding name and email values. It uses Ruby’s STDIN so the task can ask for input while it runs.

## Reading notes

- The task writes new customer data to a YAML file, but the name and email are fixed until the file is changed manually.
- Ruby’s STDIN can be used to read user input during execution.
- STDIN includes a trailing newline, so chomp is used to remove it.
- The Rake task is updated to prompt for the customer name and email before saving.
- The same approach can be used in other Ruby scripts, not only in Rake tasks.
