---
title: "Django tips: Template context processors"
date: '2012-12-20T09:02:59-03:00'
category: webclip
summary: 'Explains how Django’s RequestContext and context processors add the same variables to every template, avoiding repeated template tags. The example adds MEDIA_URL through a small custom processor.'
tags: ["django", "template-context-processors", "requestcontext"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Django tips: Template context processors"
    url: "http://www.b-list.org/weblog/2006/jun/14/django-tips-template-context-processors/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2012-12/b-list-org--django-tips-template-context-processors.md"
    kind: repo
---

Django provides RequestContext as a way to make variables available in every template. Instead of calling a template tag in each template, you can define a context processor that returns a dictionary and let RequestContext add those values automatically.

The post uses MEDIA_URL as the example. It shows a small media_url(request) function, adding it to TEMPLATE_CONTEXT_PROCESSORS, and switching view code from Context to RequestContext. It also notes that generic views use RequestContext by default.

## Reading notes

- A template tag is often the best choice for pulling content out of the database, but a shared variable belongs in the template context.
- RequestContext is a Context subclass that reads TEMPLATE_CONTEXT_PROCESSORS from settings.
- Each context processor is a callable that returns a dictionary, and its key/value pairs become template variables.
- Built-in processors can add the requesting user, debug information, i18n data, and the current HttpRequest object.
- A custom processor for MEDIA_URL can live in a context_processors.py file inside the application.
- Adding the processor to TEMPLATE_CONTEXT_PROCESSORS overrides the default set, so the built-in processors must be added back manually if they are still needed.
- Views can use RequestContext(request, context_dictionary) instead of Context(context_dictionary).
- render_to_response can receive RequestContext(request) through the context_instance argument.
- Generic views already use RequestContext by default.
