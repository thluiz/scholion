---
title: "Phoenix: Templates Are Just Functions"
date: '2015-09-18T17:58:06-03:00'
category: webclip
summary: 'The post explains that Phoenix templates are compiled into render functions injected into views, which made the author understand how `@conn` and pattern matching work during rendering.'
tags: ["phoenix", "elixir", "templates", "views"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Phoenix: Templates Are Just Functions"
    url: "http://www.jeramysingleton.com/phoenix-templates-are-just-functions/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-09/jeramysingleton-com--phoenix-templates-are-just-functions.md"
    kind: repo
---

The author describes confusion about why Phoenix separates views and templates, especially after seeing a template call a function from the view and pass `@conn` into it. Chris McCord explains that templates are compiled into functions injected into the view module at compile time.

After testing a custom `render/2` function, the author sees that a view can render without a template and that different templates can be selected by pattern matching. This makes the request flow easier to picture and removes part of the sense that Phoenix rendering is magical.

## Reading notes

- The author read the Phoenix Guides expecting a more familiar view-template setup and became confused at the Views and Templates guides.
- In the example, `handler_info/1` lives in the view, and the template calls it with `@conn`.
- Chris McCord explains that templates are compiled down to functions and injected into the view at compile time.
- A custom `render("foo.html", _assigns)` function in `HelloPhoenix.PageView` returns `"Foo!"` without a template file.
- The author confirms that `render/2` can call `handler_info(assigns.conn)` directly from the view.
- The same `render/2` function can pattern match on the template name and return different output for `"foo.html"` and `"foobar.html"`.
- The author concludes that understanding templates as injected render functions makes Phoenix rendering feel less like magic and easier to reason about.
