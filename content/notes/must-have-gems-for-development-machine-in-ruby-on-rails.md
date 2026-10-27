---
title: "Must Have Gems for Development Machine in Ruby on Rails"
date: '2013-11-19T17:55:21-03:00'
category: webclip
summary: 'The page lists Ruby on Rails development gems that speed up debugging, profiling, logging, database inspection, mail testing, code analysis, and app boot time, with brief notes on what each gem does.'
tags: ["ruby-on-rails", "development-gems", "debugging", "profiling"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Must have gems for development machine in ruby on rails | CodeBeerStartups"
    url: "http://www.codebeerstartups.com/2013/04/must-have-gems-for-development-machine-in-ruby-on-rails/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2013-11/codebeerstartups-com--must-have-gems-for-development-machine-in-ruby-on-rails.md"
    kind: repo
---

The page gathers a set of Ruby on Rails gems for development work and groups them by the kind of help they provide. The list covers error pages, query and performance checks, console tools, mail testing, code analysis, UML generation, image optimization, and faster app startup.

## Reading notes

- better_errors replaces the standard Rails error page with a more useful one, and binding_of_caller adds advanced inspection features.
- annotate generates schema information at the top of model files.
- bullet watches queries during development and warns about N+1 queries, unnecessary eager loading, and missing counter caches.
- debugger is presented as a debugger for Rails applications.
- flay analyzes structural similarities in code while ignoring literals, names, whitespace, style, and similar differences.
- hirb adds a nicer console view with tables, paging, trees, and menus.
- localtunnel exposes a local web server to the public Internet.
- lol_dba scans models for columns that probably should be indexed and can generate SQL migration scripts.
- mailcatcher runs a simple SMTP server that captures mail and shows it in a web interface.
- meta_request, described as RailsPanel, shows request details in the browser developer tools.
- pry is an IRB alternative and runtime developer console.
- quiet_assets mutes assets pipeline log messages.
- rack-mini-profiler shows a speed badge for each HTML page.
- railroady generates Rails 3 model and controller UML diagrams as SVG or DOT.
- rails-footnotes adds footnotes to Rails pages with application details and editor links.
- rails_best_practices is a code metric tool for Rails projects.
- reek detects code smells in Ruby.
- request-log-analyzer analyzes request log files to produce a performance report.
- smusher reduces image files without loss.
- zeus boots a Rails app in under a second.
