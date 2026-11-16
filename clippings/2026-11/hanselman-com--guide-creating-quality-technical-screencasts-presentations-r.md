---
url: "https://www.hanselman.com/blog/The2020GuideToCreatingQualityTechnicalScreencastsPresentationsAndRemoteMeetings.aspx"
captured_at: "2026-11-16T19:48:03+00:00"
title: "The 2020 Guide to Creating Quality Technical Screencasts, Presentations, and Remote Meetings"
domain: "hanselman-com"
---

[![Being effective when presenting remotely](https://images.hanselman.com/blog/Windows-Live-Writer/The-2020-Guide-to-Creating-Quality-Techn_8637/image_9d3c1489-32a2-42cb-99ae-2dc8626fdde3.png "Being effective when presenting remotely")](https://www.youtube.com/watch?v=x_lHk9Lf-ow&list=PL0M0zPgJ3HSdmN9tQ2xqco8Yz5whLMrj2)I've had a lot of people ask me to write up a guide to creating great technical screencasts. This is an [update to my 2011 post on the same topic](https://www.hanselman.com/blog/TheGuideToCreatingQualityTechnicalScreencasts.aspx).

### What are you doing? STOP and reassert your assumptions

Hang on. You're doing a screencast or sharing your screen in some way for a meeting, presentation, or YouTube. What does that mean and why did I suggest you stop.

This isn't a stage presentation or even a talk in a conference room. Screencasts and remote meetings have an intimacy to them. You're in someone's ear, in their headphones, you're 18 inches from their face. Consider how you want to be seen, how you want to be heard, and what is on your screen.

Try to apply a level of intentionality and _deliberate practice._ I'm not saying to micromanage, but I am saying don't just "share your screen." Put your empathy hat on and consider your audience and how it'll look and feel for them.

### Initial setup and tools

You can use any number of tools for screen capture. They are largely the same. My preferred tool is Camtasia. Other valid tools are CamStudio (a free and open source tool) and Expression Encoder Screen Capture. You can also use [OBS to record](https://www.hanselman.com/blog/TakeRemoteWorkerEducatorWebcamVideoCallsToTheNextLevelWithOBSNDIToolsAndElgatoStreamDeck.aspx) your screen and webcam.

When you're using Skype/Zoom/Teams to record live, you're already set as those tools will share for you as well as record.

### Windows Look and Feel

At the risk of sounding uptight, how you setup Windows and your environment is the difference between a professional and an amateurish screencast. It's shocking how many folks will start recording a screencast without changing a thing, then wonder why their 1600x1200 screencast looks bad on YouTube at 360p or low bandwidth on a phone. If you find yourself doing screencasts a lot, considering making a custom user (maybe named Screencast?) on your machine with these settings already applied. That way you can login as Screencast and your settings will stick.

### Resolution and Aspect

First, decide on your aspect ratio. Your laptop may have a ratio of width to height that is 3:2 or 4:3 but MOST people have a 16:9 Widescreen system? A VERY safe resolution in 2020 is 1280x720 (also known as 720p). That means that you'll be visible on everything from a low-end Android, any tablet, up to a desktop.

That said, statistics show that many folks now have 1920x1080 (1080p) capable systems. But again, consider your audience. If I was presenting to a rural school district, I'd use 720 or a lower resolution. It will be smoother and use less bandwidth and you'll never have issue with things being too small. If I was presenting in a professional environment I'd use 1080p. I don't present at 4k, especially if the audience is overseas from where I am. You're pushing millions of pixels that aren't needed, slowing your message and adding no additional value.

On Windows, consider your scale factor. At 1080p, 125% DPI is reasonable. At 720p (or 1366x768, using 100% scaling is reasonable).

### Background Wallpaper and Icons

Choose a standard looking background photo. I prefer to use one from [http://unsplash.com](http://unsplash.com/) or the defaults that come with Windows 10 or your Mac. Avoid complex backgrounds as they don't compress well during encoding. Avoid using pictures of your kids or family unless it feeds your spirit and you don't mind mixing the professional and personal. Again - be **intentional**. I am neither for nor against - just be conscious and decide. Don't just accept the defaults.

Hide your desktop icons. Right click your desktop and hit View | Show Desktop Items. Also consider whether we need to see your desktop at all. If it doesn’t add value, don’t show it on the screencast.

### Fonts

Try to use standard fonts and themes. While your preferred font and colors/themes offer personality, they can be distracting. Consider the message you want to present.

If you're using Visual Studio or Visual Studio Code, remember that your audience likely hasn't changed their defaults, and if you show them something fancy, they'll be thinking about how they get that fancy widget rather than your content. In Visual Studio proper, go to Tools | Options | Environment | Fonts and Colors and click "Use Defaults."

In all your text editors, consider change your fonts to Consolas Size 15. It may seem counter-intuitive to have such large fonts but in fact this will make your code viewable even on an iPhone or Tablet. 

Remember, most video sites, including YouTube, restrict the embedded video player size to a maximum of around 560p height, unless you go full-screen or use a pop-out. Use the font size recommended here, and use Camtasia’s zoom and highlight features during editing to call out key bits of code.

Don’t highlight code in the editor by selecting it with the mouse UNLESS you've deliberately change the selection background color. Defaults are typically hard to read editor selections in video. Instead, zoom and highlight in post production, or use ZoomIt and _practice_ zooming and emphasizing on screen elements.

### Browser Setup

Unless your screencast is about using different browsers, pick a browser and stick to it. Hide your toolbars, clear your cache, history, and your autocomplete history. You'd be surprised how many inappropriate sites and autocomplete suggestions are published on the web forever and not noticed until it's too late. Don't view pr0n on your screencast machine. Be aware.

### Toolbars

Your browser shouldn't show any, and this is a good time to uninstall or hide whatever coupon-offering nonsense or McAffee pixel waster that you've stopped being able to see after all these years. Remember, default is the word of the day. Disable any Browser Extensions that aren't adding value.

If you are using Visual Studio or an IDE (Eclipse, Photoshop, etc) be aware of your toolbars. If you have made extensive customizations to your toolbars and you use them in the screencast, you are doing a great disservice to your audience. Put things to the default. If you use hotkeys, tell the audience, and use them for a reason.

### Toast

You've got mail! Yay. Yes, but not during your screencast. Turn off Outlook Gmail, GChat, Twitter, Messenger, Skype, and _anything_ else that can "pop toast" during your screencast.

### Clock and Notifications

Go to Start on Windows 10, and search for System Icons and turn off the Clock temporarily. Why? You can't easily edit a screencast if there's a convenient time code in the corner that jumps around during your edits. Also, no one needs to know you're doing your work at 3am.

Clean out your taskbar and notification area. Anything that visually distracts, or just hide the taskbar.

### Audio and Voice

Use a decent microphone. I use a Samson C01U. You can also use a USB headset-style microphone but be aware that breathing and "cotton mouth" really shows up on these. Test it! Listen to yourself! Try moving the microphone _above your nose_ so you aren't exhaling onto it directly. Use a pop filter to help eliminate 'plosives (p's and t's). You can get them cheap at a music store.

Be aware of your keyboard clicks. Some folks feel strongly about whether or not your keyboard can be heard during a screencast. Ultimately it's your choice, but you have to be aware of it first, then make a conscious decision. Don't just let whatever happens happen. Think about your keyboard sound, your typing style and your microphone, and listen to it a few times and see if you like how it comes together.

Avoid prolonged silence. There should be ebb and flow of "I'm saying this, I'm doing that" but not 10 seconds of "watch my mouse." Speak in an upbeat but authentic tone. Be real.

Also be calm and quiet. Remember you are a foot from them and you're their ear. It's a conversation with a friend, not a presentation to thousands (even if it is).

Don’t apologize or make excuses for mistakes – either work them in as something to learn from, or remove them completely.

If you are editing the presentation - _If you make a mistake when speaking or demonstrating, clap your hands or cough loudly into the mic and wait a second before starting that portion over._ When editing, the mistakes will show up as loud audio spikes, making it easy to find them.

Camtasia has decent automatic noise reduction. Use it. You’ll be surprised how much background noise your room has that you, but not your audience, will easily tune out.

If you must overdub a portion of the audio, sit in the same position you did while recording the original, and have the mic in the same spot. You want your voice to blend in seamlessly.

### Preferred Video Output for Prerecords

Your screen capture tool should be produced at the highest _reasonable_ quality as it will be compressed later when it's uploaded. Think of it like producing JPEGs. You can make a 5 megabyte JPG, but often a 500k one will do. You can make a 10 gig screen capture if you use uncompressed AVI encoding, but often a high bit rate MP4 will do.

The trick is to remember that your compressed screencast will be recompressed (copies of copies) when it is run through the encoding process.

Edit your screencast, if you do, in its recorded native resolution which hopefully is what you'll publish to as well. That means, record at 1080p, edit at 1080p, and publish at 1080p. Let YouTube or your final destination do the squishing to smaller resolutions.

Personally, I like to know what's going on in my production process so I always select things like "Custom production settings" in Camtasia rather than presets. Ultimately you'll need to try and find what works for you. Use an H.264 encoder with a high bitrate for the video and 44.1kHz/441000Hz 16 bit mono for the audio. Basically make a decently sized MP4 and it should work everywhere.

### Do you have enough bandwidth?

In my opinion, if you are doing a live call with Video and Screensharing and you want it to be high definition, you'll need 4 Mbps upstream from your connection. You can check this at [http://speedtest.net](http://speedtest.net/). If you have 5-6 Mbps you've got a little more headroom. However, if someone in the house decides to get on Netflix, you could have an issue. Know your bandwidth limitations ahead of time. If it's an important stream, can you dedicate your bandwidth to just your one machine? Check out QoS (quality of service) on your router, or better yet, take your kids' iPads away! ;)

### Conclusion

Take some time. I put about an hour of work into a 15 min screencast. Your mileage may vary. Watch your video! Listen to it, and have your friends listen to it. Does it look smooth? Sound smooth? Is it viewable on a small device AND a big screen? Does it FEEL good?

* * *

**Sponsor:** Have you tried [developing in Rider](https://hnsl.mn/2VPP4rV) yet? This fast and feature-rich cross-platform IDE improves your code for .NET, ASP.NET, .NET Core, Xamarin, and Unity applications on Windows, Mac, and Linux.

#### About Scott

Scott Hanselman is a former professor, former Chief Architect in finance, now speaker, consultant, father, diabetic, and Microsoft employee. He is a failed stand-up comic, a cornrower, and a book author.

[![facebook](https://images.hanselman.com/main/icon-fb.png)](https://facebook.com/shanselman) [![bluesky](https://images.hanselman.com/main/icon-bluesky.png)](https://bsky.app/profile/scott.hanselman.com) [![subscribe](https://images.hanselman.com/main/icon-rss.png)](http://feeds.hanselman.com/ScottHanselman)  
[About](http://hanselman.com/about)   [Newsletter](http://www.hanselman.com/newsletter)

**Hosting By**  
[![Hosted on Linux using .NET in an Azure App Service](https://images.hanselman.com/main/azure-250x250.png)](https://azure.microsoft.com/free?WT.mc_id=-blog-scottha)
