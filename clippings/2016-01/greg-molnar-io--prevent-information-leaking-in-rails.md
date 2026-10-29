---
url: "https://greg.molnar.io/tech/2015/10/28/prevent-rails-information-leaking.html"
captured_at: "2016-01-02T14:08:45-03:00"
title: "Greg Molnar | Prevent information leaking in Rails"
domain: "greg-molnar-io"
---

# Prevent information leaking in Rails

#### **28 Oct 2015** . tech . [Comments](https://greg.molnar.io/tech/2015/10/28/prevent-rails-information-leaking.html#disqus_thread) [#rails](https://greg.molnar.io/tags/rails.html) [#information leaking](https://greg.molnar.io/tags/information%20leaking.html) [#ruby on rails](https://greg.molnar.io/tags/ruby%20on%20rails.html) [#caching](https://greg.molnar.io/tags/caching.html)

By default Rails sets the `Cache-Control` HTTP Header to `max-age=0, private, must-revalidate`, which means the browser needs to revalidate the page on each request, BUT the browser still stores the cached version of the page. The problem with this, if a user clicks the back button of the browser, it won't revalidate the page, it will just simply load the page from it's cache. This can lead to serious information leaking, if you a user logs out from an application and someone else sits to that computer and navigates back in history. A more advanced attacker can even decrypt the browser's cache files and access sensitive information.

To address this issue, you can explicitly set the `Cache-Control` header in your app with a before filter:

```
  before_filter :set_as_private

  protected

   set_as_private
    responseheaders'Cache-Control'  'no-cache, no-store'
```

You can call this filter in each controller where you display sensitive information(usually every controller behind authentication).
Alternatively, you can ask you users at sign in, whether they are on a public or private computer and set the cache header based on their choice.
