---
title: "How can I reduce my Ruby/Rails memory usage when running Redmine?"
date: '2013-05-20T01:33:33-03:00'
category: webclip
summary: 'A wrapper script can reduce Redmine’s Ruby memory usage by setting Ruby heap and GC variables, then having nginx call that script instead of the Ruby executable. The setup may save about 20 MB.'
tags: ["ruby", "rails", "redmine", "memory-usage"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "How can I reduce my Ruby/Rails memory usage when running Redmine? - WebFaction Community"
    url: "http://community.webfaction.com/questions/2476/how-can-i-reduce-my-rubyrails-memory-usage-when-running-redmine"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2013-05/community-webfaction-com--how-can-i-reduce-ruby-rails-memory-usage-running-redmine.md"
    kind: repo
---

A wrapper script is suggested to lower the memory usage of a Redmine project by setting Ruby heap and garbage-collection environment variables before calling Ruby. The setup is meant to be used by nginx in place of the normal Ruby executable, and one reply says it reduced memory use by about 20 MB.

## Reading notes

- Use a shell wrapper that exports RUBY_HEAP_MIN_SLOTS, RUBY_HEAP_SLOTS_INCREMENT, RUBY_HEAP_SLOTS_GROWTH_FACTOR, RUBY_GC_MALLOC_LIMIT, and RUBY_HEAP_FREE_MIN before executing Ruby.
- Point nginx to the wrapper script instead of the Ruby binary.
- Put the script in a file such as ruby.sh or ruby_small.
- Update the passenger_ruby line in nginx.conf to the wrapper’s full path.
- Make the wrapper executable with chmod 755.
- One user reports needing to change the last exec line to call Ruby by full path.
