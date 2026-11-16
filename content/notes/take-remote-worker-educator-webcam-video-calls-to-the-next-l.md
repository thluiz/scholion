---
title: "Take Remote Worker/Educator Webcam Video Calls to the Next Level with OBS, NDI Tools, and Elgato Stream Deck"
date: '2020-04-20T21:22:36+00:00'
category: webclip
summary: 'The post shows how to route webcams, desktop capture, and other sources through OBS, send the result as a virtual webcam, and switch scenes instantly in video calls with NDI tools or OBS virtual camera.'
tags: ["obs", "ndi", "stream-deck", "virtual-webcam"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Take Remote Worker/Educator webcam video calls to the next level with OBS, NDI Tools, and Elgato Stream Deck"
    url: "https://hanselman.com/blog/TakeRemoteWorkerEducatorWebcamVideoCallsToTheNextLevelWithOBSNDIToolsAndElgatoStreamDeck.aspx"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/hanselman-com--take-remote-worker-educator-webcam-video-calls-to-the-next-l.md"
    kind: repo
---

The post describes a low-cost way to turn OBS into a software video compositor for remote calls. You can combine multiple webcams, desktop capture, and other sources into scenes, then output them as a virtual webcam for Teams, Skype, or Zoom. Scene changes can be triggered with a Stream Deck, a hotkey, or Stream Deck Mobile.

## Reading notes

- Use OBS as the compositor for webcams, desktop capture, and other scene sources.
- Send OBS output through NDI Tools and NDI Virtual Input, or use OBS-VirtualCam as an alternate plugin.
- Create separate scenes for each camera angle and for desktop views with picture-in-picture.
- Switch scenes dynamically during calls instead of changing camera inputs inside the video app.
- Use a Stream Deck, Stream Deck Mobile, or Touch Portal to change scenes.
- Select the virtual camera, labeled NewTek NDI Video in the post, in Teams, Skype, or Zoom.
