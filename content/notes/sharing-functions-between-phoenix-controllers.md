---
title: "Sharing Functions Between Phoenix Controllers"
date: '2016-01-07T16:47:27-03:00'
category: webclip
summary: 'The post explains how Phoenix controllers share imports through web/web.ex, how use MyApp.Web, :controller expands __using__/3, and how adding an import there makes helper functions available to all controllers.'
tags: ["phoenix", "elixir", "controllers", "imports"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Sharing Functions Between Phoenix Controllers — Medium"
    url: "https://medium.com/@cjbell_/sharing-methods-between-phoenix-controllers-358ab6d36e22#.53ajwxyfo"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2016-01/medium-com--sharing-functions-between-phoenix-controllers.md"
    kind: repo
---

The post says Phoenix applications often need shared controller functions to avoid duplicating code. It places helper functions in a helpers.ex file under web/controllers and shows that, instead of importing them in each controller, the shared import can be added in web/web.ex.

## Reading notes

- Phoenix controllers often need shared functions to keep code DRY.
- Helper functions can live in a helpers.ex file inside web/controllers.
- Importing helpers in each controller works, but repeats the same line.
- The shared controller definitions are in web/web.ex.
- use MyApp.Web, :controller calls the controller/0 function in web/web.ex.
- The use call triggers the __using__ macro on MyApp.Web with :controller.
- __using__ calls apply/3, which expands the quoted code from controller/0 into the controller.
- Adding another import line to controller/0 makes the helper module available in all controllers.
- The same technique can extend functionality to views, channels, router, and models.
