---
url: "https://dev.to/horusgoul/using-html-css-and-javascript-to-create-obs-plugins-for-your-live-streaming-sessions-45ij"
captured_at: "2026-11-16T19:38:55+00:00"
title: "Using HTML, CSS, and JavaScript to Create OBS Plugins for Your Live Streaming Sessions"
domain: "dev-to"
---

[![Horus Lugo](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F210860%2Fa7422269-8da7-4bb8-9d87-e7deb7eb1dca.jpeg)](https://dev.to/horusgoul)

A few days ago, I decided to give a try to live coding on Twitch. I developed a bot for one of the forums I visit regularly and it was a great experience, a lot of people visited the streaming and the big majority stayed for a while.

Because of that, I have been looking for ways to improve the experience of my live coding sessions and then I thought that one of these ways could be creating my own plugins for OBS (Open Broadcaster Software).

I found out that OBS plugins can be written in C++, but that's overkill! Then I thought that maybe there's another way using web technologies (HTML, CSS, and JS), that's when I discovered the `Browser` source.

[![Browser Source](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2Fnt242vt70j7e4sonz54s.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2Fnt242vt70j7e4sonz54s.png)

This type of source allows you to use an internal browser that supports modern web capabilities, just point it to an URL or a local HTML file and start building a dynamic experience for your viewers!

[![Browser Source Properties](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2F2b2yyj2ag6n58l1z3s7t.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2F2b2yyj2ag6n58l1z3s7t.png)

Once I got to know about this, I decided to use [Preact](https://preactjs.com/) with [HTM](https://github.com/developit/htm) and plain CSS as the stack to build my plugins. I believe that this stack rocks for this use case because it doesn't require a build step, just go ahead and use the platform!

Here's a GIF of my first OBS plugin, which loads the latest posts of my dev.to profile in case someone wants to read one of my publications after the stream finishes:

[![Plugin that retrieves my latest dev.to publications](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2Fjy2zusgwrplz81yk3rey.gif)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2Fjy2zusgwrplz81yk3rey.gif)

After building my first plugin and seeing that this stack rocks, I have created a repository that you can use as a template to develop obs plugins with this stack: [HorusGoul/preact-obs-plugin](https://github.com/HorusGoul/preact-obs-plugin).

## Preact OBS Plugin

This is a template that can be used to build OBS plugins (or webapps!)

$ git clone https://github.com/HorusGoul/preact-obs-plugin hello-world-obs-plugin

Enter fullscreen mode Exit fullscreen mode

The dependencies are downloaded from CDNs, just launch a web server with `npx serve` and use the local URL in your `Browser` source on OBS.

I recommend you to use `npx live-server` to develop, it will reload your website whenever you change one of the files.

  
  

  

* * *

_Follow me on [Twitter](https://twitter.com/HorusGoul) if you want to know about my future articles, projects or whatever I come up with!_

[![Strands harness](https://media2.dev.to/dynamic/image/width=775%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Farticles%2Fm2mvywz0h8vpa1igwwvy.png)](https://strandsagents.com/?trk=1c097af3-4db9-4f1f-b0c4-4ea3fa25f1c3&sc_channel=display+ads&bb=264933)

## [](#strands-harness-is-a-stateoftheart-fully-assembled-agent-harness)[Strands harness is a state-of-the-art, fully assembled agent harness.](https://strandsagents.com/?trk=1c097af3-4db9-4f1f-b0c4-4ea3fa25f1c3&sc_channel=display+ads&bb=264933)

Strands harness is a complete, production-ready agent the moment you install it. Shell, file, and web tools, plus context management, memory, sessions, and subagents, are tuned and ready. Run it as a library or from the strands CLI, on any model and any cloud. Every default is yours to change through the open-source Harness SDK.

[Get Started with Strands](https://strandsagents.com/?trk=1c097af3-4db9-4f1f-b0c4-4ea3fa25f1c3&sc_channel=display+ads&bb=264933)
