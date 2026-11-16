---
url: "https://hanselman.com/blog/TakeRemoteWorkerEducatorWebcamVideoCallsToTheNextLevelWithOBSNDIToolsAndElgatoStreamDeck.aspx"
captured_at: "2026-11-16T04:26:22+00:00"
title: "Take Remote Worker/Educator webcam video calls to the next level with OBS, NDI Tools, and Elgato Stream Deck"
domain: "hanselman-com"
---

![Changing cameras dyamically with OBS](https://images.hanselman.com/blog/OBS.gif "Changing cameras dyamically with OBS")Over the years I've collected a few webcams, some quality and some not. If you're interested in [creating the ultimate remote worker webcam setup on a budget](https://www.hanselman.com/blog/GoodBetterBestCreatingTheUltimateRemoteWorkerWebcamSetupOnABudget.aspx), I've written a blog post on the topic.

However, now that we are a remote workers - my entire company has everyone working remotely until further notice - I've found that an extra webcam or two can really be helpful if I want to point a camera at something on my desk, or get a wider view, look at a whiteboard, etc.

Of course, you **can** always change video inputs in any application but there's that...pause...that...hang...that moment. You have to switch into your apps Device Settings, do the dropdown, switch, wait, and then you've changed the camera.

What if you could change cameras - scenes - like you were a movie director. But, you have minimal budget. What can you do for nothing or next to nothing? A lot.

### What's the goal?

**With minimal setup, you can feed all your webcams, your desktop itself, and really anything you can express as a 'scene' into a software video compositor and then output them as a virtual webcam.**

**Then you select and use that Virtual Webcam in your remote video conferencing tool of choice! The results are amazing.**

### Setup

First, get OBS and NDI Tools, specifically NDI Virtual Input.

*   [OBS (Open Broadcaster Software)](https://obsproject.com/) is free and open source software for video recording and live streaming.
    *   You have likely heard of this software package when you read about Twitch Streamers. [Jeff Fritz](https://jeffreyfritz.com/) uses this for [his Live Streaming Setup](https://jeffreyfritz.com/2019/01/live-streaming-setup-2019-edition/). [https://obsproject.com/](https://obsproject.com/)
*   [NDI Tools](https://ndi.tv/tools/) and NDI Virtual Input.

*   This is a software package that creates a virtual camera input.
*   [NDI Plug for OBS : obs-ndi](https://github.com/Palakis/obs-ndi/releases?WT.mc_id=-blog-scottha) - This allows the OBS software to send its output to NDI, the virtual camera.

*   **ALTERNATE:**

*   You can avoid using NDI Tools (which is an extra hop) and use [OBS-VirtualCam](https://obsproject.com/forum/resources/obs-virtualcam.539/) as plugin instead. It will create a Virtual Camera locally and directly send 1080p video to a Virtual Cam called OBS-VirtualCam.

*   **OPTIONAL:** [Elgato Stream Deck](https://amzn.to/2xj2ios) and the Stream Deck Software
    *   They've got 6- and 15-key decks. The have full color LCD keys and you can make the icons look however you want. Ya, it's a portable hotkey button machine, but it's amazing. Note in the upper right corner of my Stream Deck I have three OBS buttons, one for each scene and the active one lights up. I've also made buttons to change my primary monitor's resolution. More on that in a future blog post. I've also got [Elgato Stream Deck buttons to change my audio inputs an outputs as well, with a how-to](https://www.hanselman.com/blog/ProgrammaticallyChangeYourSystemsMicAndSpeakersWithNirCmdAndElgatoStreamDeck.aspx).  
        [![My Elgato Stream Deck](https://images.hanselman.com/blog/Windows-Live-Writer/38a9f81fd510_148BE/IMG_2874_94503105-c994-4096-aee7-84dc955ab0ce.jpg "My Elgato Stream Deck")](https://amzn.to/2xj2ios)
    *   Don't want to buy a physical device? Use your phone as a [Stream Deck with Stream Deck Mobile](https://www.elgato.com/en/gaming/stream-deck-mobile)
    *   You could also buy [Touch Portal](https://www.touch-portal.com/) for about $12 and use any old Android phone you have laying around as a remote control for this purpose!

Install these three things and run OBS. When you run OBS after installing the NDI plugin, you'll need to go to Tools, NDI Output Settings and select Main Output. Leave OBS running.

![NDI Output Settings in OBS](https://images.hanselman.com/blog/Windows-Live-Writer/38a9f81fd510_148BE/image_8518b929-983a-488e-b35c-9026ef5a6577.png "NDI Output Settings in OBS")

Then run Virtual Input and right click on it in your tray (near the clock) and set it's output to your computer name | OBS. Mine is IRONHEART in the picture below. If you see None, you likely don't have OBS running.

![Taking output from OBS and feeding it into Virtual Input](https://images.hanselman.com/blog/Windows-Live-Writer/38a9f81fd510_148BE/image_00c41c38-80d8-42d2-8549-e33d54dd5515.png "Taking output from OBS and feeding it into Virtual Input")

Define your Scenes. Scenes are a collection of sources.

Add and name a scene, then add a Video Capture Device for your camera. I also like to set the Resolution manually.

![BRIO 1080p in OBS](https://images.hanselman.com/blog/Windows-Live-Writer/38a9f81fd510_148BE/image_5732941e-2d81-48c5-a897-1a41883990f7.png "BRIO 1080p in OBS")

I made one Fullscreen Scene per webcam, and one for my desktop that also includes my camera in PIP in the corner.

> **NOTE:** If you're a teacher, perhaps you share just your lesson plans or browser window and yourself in video another way. You can be split screen, pip, or whatever makes you happy! Your scenes can be as complex as you'd like and include lesson plans, links, resources, and more!

![PIP inside OBS](https://images.hanselman.com/blog/Windows-Live-Writer/38a9f81fd510_148BE/image_840ff45f-86bc-44d8-b2b2-00a827e18734.png "PIP inside OBS")

To review:

*   OBS is a compositor that feeds into
*   NDI Virtual Input
*   And Scenes can be changed dynamically (see animation at top of this post) by a Stream Deck, hotkey, or Stream Deck Mobile
*   Select "NewTek NDI Video" as your webcam in Teams or Skype or Zoom!

At this point you can change camera angles and select scenes when you're on a call! The transitions will be be instant and smooth for your viewers. This also works great for workshops and teachers teaching classes!

![image](https://images.hanselman.com/blog/Windows-Live-Writer/38a9f81fd510_148BE/image_b9e996b4-39df-46f9-bc4e-71e55e2f8453.png "image")

Thanks Jeff Fritz for your help with this! Do you have any OBS teams, dear reader?

* * *

**Sponsor**: Couchbase gives developers the power of SQL with the flexibility of JSON. [Start using it today for free](https://hnsl.mn/3bRG10z) with technologies including Kubernetes, Java, .NET, JavaScript, Go, and Python.

#### About Scott

Scott Hanselman is a former professor, former Chief Architect in finance, now speaker, consultant, father, diabetic, and Microsoft employee. He is a failed stand-up comic, a cornrower, and a book author.

[![facebook](https://images.hanselman.com/main/icon-fb.png)](https://facebook.com/shanselman) [![bluesky](https://images.hanselman.com/main/icon-bluesky.png)](https://bsky.app/profile/scott.hanselman.com) [![subscribe](https://images.hanselman.com/main/icon-rss.png)](http://feeds.hanselman.com/ScottHanselman)  
[About](http://hanselman.com/about)   [Newsletter](http://www.hanselman.com/newsletter)

**Hosting By**  
[![Hosted on Linux using .NET in an Azure App Service](https://images.hanselman.com/main/azure-250x250.png)](https://azure.microsoft.com/free?WT.mc_id=-blog-scottha)
