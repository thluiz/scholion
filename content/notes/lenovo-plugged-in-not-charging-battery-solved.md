---
title: "Lenovo plugged in, not charging battery--SOLVED!"
date: '2015-12-09T16:05:27-03:00'
category: webclip
summary: 'The post says a Lenovo that would not charge was fixed by removing the Microsoft ACPI Compliant Control Method Battery entries in Windows 7 Device Manager, then restarting with the battery and power supply reinstalled.'
tags: ["lenovo", "windows-7", "battery", "device-manager"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Way Off the Wall (Life in Xiamen Fujian China): Lenovo plugged in, not charging battery--SOLVED!"
    url: "http://offthewallchina.blogspot.com/2012/07/lenovo-plugged-in-not-charging-battery.html"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-12/offthewallchina-blogspot-com--lenovo-plugged-in-not-charging-battery-solved.md"
    kind: repo
---

The post describes a Lenovo laptop that stopped charging even though the battery and charger were fine. The problem is presented as a Windows 7 issue rather than a Lenovo hardware issue, and the writer says the fix came from Jeffrey Palermo’s blog.

## Reading notes

- The battery was at 9%, but the PC still reported good battery health.
- The writer attributes the problem to a Windows 7 bug that had existed for at least two years.
- The fix begins by disconnecting the A/C power supply, shutting down the computer, and removing the battery.
- After reconnecting the A/C power supply and starting the computer, the Battery section is found in Control Panel, then System, then Device Driver, then Battery.
- All entries called Microsoft ACPI Compliant Control Method Battery are uninstalled.
- The computer is shut down again, then the battery and A/C power supply are reinserted, and the computer is started.
- The post says the charging problem should then be fixed.
