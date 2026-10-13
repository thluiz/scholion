---
title: "Fix for Skype Mic volume increasing when Sc2 launches."
date: '2014-01-09T18:13:34-03:00'
category: webclip
summary: 'The post gives a temporary fix for a Skype microphone volume jump when StarCraft II launches by changing Windows, Skype, and SC2 voice settings so the mic stays at the same level.'
tags: ["skype", "starcraft-ii", "microphone", "voice-settings"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Fix for Skype Mic volume increasing when Sc2 launches. - Forums - StarCraft II"
    url: "http://eu.battle.net/sc2/en/forum/topic/3686610847"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2014-01/eu-battle-net--fix-for-skype-mic-volume-increasing-when-sc2-launches.md"
    kind: repo
---

The post describes a temporary workaround for a problem where launching StarCraft II makes Skype microphone volume jump to 100%. It says the fix is to change microphone access and auto-adjust settings in Windows and Skype, then match SC2 voice settings to Skype and switch the voice provider to FMod.

## Reading notes

- In Windows, open Recording devices from the volume control, open the microphone properties, and uncheck “Allow applications to take exclusive control of this device.”
- In Skype, remove anything listed under Manage other Program's Access to Skype, save the changes, and uncheck Automatically Adjust in Audio Settings.
- In StarCraft II, enable voice, set microphone volume to match Skype, untick Automatic next to microphone volume, and change the voice provider to FMod.
- If you do not want other players to hear you in SC2, mute the microphone next to the portrait.
