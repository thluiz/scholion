---
title: "Top 10 tips to a new django developer"
date: '2012-12-19T22:36:38-03:00'
category: webclip
summary: 'The post lists Django habits that improve reuse, portability, and maintainability, from avoiding hardcoded project names and paths to using named URLs, debug tools, and reusable third-party apps.'
tags: ["django", "best-practices", "reusability", "third-party-apps"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Top 10 tips to a new django developer - Move On"
    url: "http://www.ramavadakattu.com/top-10-tips-to-a-new-django-developer"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2012-12/ramavadakattu-com--top-10-tips-to-a-new-django-developer.md"
    kind: repo
---

The post collects practical advice for new Django developers. It argues for reusable app structure, configurable paths and static URLs, moving core logic out of views, and using named URLs and debug tools to keep projects easier to maintain and deploy.

## Reading notes

- Do not include the project name in imports, because it ties an app to one project and makes reuse and renaming harder.
- Avoid hardcoding MEDIA_ROOT and TEMPLATE_DIRS; build them from SITE_ROOT so deployment changes and OS changes are easier to handle.
- Do not hardcode static file paths in templates; use {{ MEDIA_URL }} so changing the media host updates all templates at once.
- Pass useful context variables to templates with RequestContext(request) instead of rewriting template paths by hand.
- Keep core business logic out of views, since putting it there makes the code harder to unit test and reuse.
- Set DEBUG based on the hostname, or use a separate local settings file, so production changes are less likely to be forgotten.
- Load third-party template tags once with template.add_to_builtins so you do not repeat {% load ... %} in every template.
- Split URLs across app-level urls.py files instead of placing everything in project/urls.py, which makes apps easier to reuse.
- Use named URLs with reverse lookups in views, models, and templates instead of hardcoding URL strings.
- Use django-debug-toolbar, Werkzeug debugger, and pdb for debugging.
- Consider Pinax when you want reusable Django components such as openid support, contact import, and notifications.
- The post also points to third-party tools such as django-evolution, South, template-utils, Jinja, django-command-extensions, and sorl-thumbnail.
