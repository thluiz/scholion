---
url: "https://dockyard.com/blog/2020/05/11/elixir-nifs-xbox-kinect-and-liveview"
captured_at: "2026-11-16T19:58:00+00:00"
title: "Elixir, NIFs, Xbox Kinect, and LiveView - DockYard"
domain: "dockyard-com"
---

![Out of focus lights](https://assets.dockyard.com/images/287b22d9-29c7-40ca-9fca-f454134a26ca-large.webp)

![Mike Binns](https://s3.amazonaws.com/dockyard-com-production/images/team-monster-03.png)

When the Xbox Kinect first came out about 10 years ago, I was fascinated by the technology and the interesting things people were doing by connecting the Kinect to their computers. But, I had just recently become a father for the second time and -- with my limited free time -- couldn't justify the $150 price point, so I never picked one up.

Fast forward almost 10 years, and I came across a Kinect that had been sitting in a box for the past five years and an owner who had no issues letting me borrow it. I enjoyed numerous hours playing Kinect Star Wars with my boys, but then I remembered my original draw to the Kinect: connecting to it and controlling it via a computer. This led me on a journey that touches on Elixir, NIFs, Kinect, and Phoenix LiveView. The Kinext library and the Kinext LiveView demo app were the result of that journey.

This blog post follows that journey, but is not an in-depth guide for NIFs or Phoenix LiveView.

## The Technology

### OpenKinect

From the [OpenKinect website](https://openkinect.org/wiki/Main_Page):

> OpenKinect is an open community of people interested in making use of the amazing Xbox Kinect hardware with our PCs and other devices. We are working on free, open source libraries that will enable the Kinect to be used with Windows, Linux, and Mac. The OpenKinect library (`libfreenect`) provides the ability to interact with the Kinect directly via the C language. It grants access to the tilt motors, LED, audio, video, and depth sensors. `libfreenect` has been around for many years, and wrappers for the library exist for a number of programming languages, but (prior to this journey) not Elixir.

### Elixir and Erlang NIFs

Elixir cannot directly call C bindings, so to access `libfreenect` from Elixir, we need to bridge the gap using Erlang's Natively Implemented Function (NIF) feature. NIFs are powerful because they enable you to write C code and load it into the Erlang Virtual Machine, allowing any native action to be performed from Erlang/Elixir; however, they also bring all the dangers of C with them including the ability to crash the entire Erlang Virtual Machine.

### Phoenix LiveView

The [Phoenix Framework](https://www.phoenixframework.org/) allows you to "build rich, interactive web applications quickly, with less code and fewer moving parts." When it came time to create a simple app to demo the functionality of Kinext, Phoenix LiveView was the obvious choice. It took ~45 minutes from running `mix phx.new --live` to having all the functionality on display in a simple interactive web page.

## The Journey

### libfreenect

The first step in the Kinext journey was to explore the [OpenKinect library](https://openkinect.org/wiki/Main_Page) and make sure it was actually feasible to use it for this project. I had to pick up [a USB adapter](https://www.amazon.com/IDS-Xbox-Kinect-Sensor-Adapter/dp/B073GY3C7Z) to connect the Kinect to my laptop. After running `brew install libfreenect` and `brew cask install quartz` I was able to validate the connection to my Kinect via the `freenect-glview` utility.

### Erlang NIFs

With the connection from my computer to the Kinect validated, the next step was to figure out how to talk to the `libfreenect` library from Elixir via Erlang NIFs. I created an Elixir project named Kinext, and after reading a number of guides online, I implemented the skeleton of the NIF process for the first function I would need: `freenect_init`, which creates a context that I could use to reference the `libfreenect` environment.

The actual function in C shows some of the things you need to do a bit different when interacting with NIFs ([Github link](https://github.com/TheFirstAvenger/kinext/blob/v0.2.0/native/nifs/kinext.c#L94-L113)):

![kinext\_freenect\_init](https://i.imgur.com/oEpFa9n.png)

As seen above, calls into a NIF are given two different arguments:

1.  **The current Erlang NIF Environment as a pointer.** You can think of this as a reference to the process the NIF is called from. The environment can later be used in `enif_*` function calls to manipulate terms, send messages, and more.
    
2.  **A list of arguments as an array.** These are just terms -- the arguments to the NIF function.
    

When passing things back to Erlang/Elixir from a NIF, one would normally encode the data into a normal Erlang term. This works great in a lot of cases, and enables you to keep working with the data from the NIF in the Erlang/Elixir program.

There is, however, a problem with doing that in this case.

The `libfreenect` library exposes several things as pointers to opaque objects (e.g. `context` and `device`). In the libfreenext library, these contain any data the library needs to communicate with the hardware itself. Because they are opaque to us, there is no way we can encode them into a normal Erlang term.

Luckily, the NIF API has a feature designed for exposing things like these to Erlang/Elixir, called Resources. Resources can be encoded into a term inside a NIF function, returned to Erlang/Elixir (where it just looks like a normal `Reference`), and later decoded into the original data in another NIF. This enables us to return these opaque objects from the `libfreenect` library safely, then use them later in other NIFs we pass them to.

Resources are useful because they do not require you to encode and decode the underlying data structure when passing to Elixir -- they are just a pointer. In this case, we call `freenect_init` to initialize the context, then copy that into a resource allocated via `enif_alloc_resource`, and created via `enif_make_resource`. We can then return that resource, and the NIF will hand it back as a Reference to Elixir. We see the NIF defined from the Elixir side of things here ([Github Link](https://github.com/TheFirstAvenger/kinext/blob/v0.2.0/lib/kinext/native.ex#L18-L21)):

![Elixir freenect\_init](https://i.imgur.com/bxL13L8.png)

You notice that its spec matches the returns from the C function: either the reference or the integer error code.

As you can see, the actual function body in Elixir throws an error by default. When the file is compiled, the NIFs are loaded and (if successful) replace the error throwing version of the function body with the call to the NIF. This magic is outlined at the top of the Elixir module [Github Link](https://github.com/TheFirstAvenger/kinext/blob/master/lib/kinext/native.ex#L1-L16):

![on\_load load\_nifs](https://i.imgur.com/k3JcIqs.png)

and the Elixir function name is mapped to the C function name at the bottom of the C file ([Github Link](https://github.com/TheFirstAvenger/kinext/blob/v0.2.0/native/nifs/kinext.c#L259-L272)):

![nif\_funcs](https://i.imgur.com/I9bAWp5.png)

We can now take that Reference, representing a `libfreenect` Context, and pass it back into the "freenect\_open\_device" function ([Github Link](https://github.com/TheFirstAvenger/kinext/blob/v0.2.0/lib/kinext/native.ex#L33-L36)):

![freenect\_open\_device](https://i.imgur.com/ORP91Nb.png)

One interesting feature to implement was the video handling. To handle video in `libfreenect`, you first need to call into `libfreenect` to initialize video. This call includes giving `libfreenect` a video callback function that will be called asynchronously when a video frame is returned. Once initialized, you need to make a separate call into `libfreenect` to "process events," which will trigger a picture to be taken and sent to the previously defined video callback function. Each time you call "process events," a single frame is sent to the video callback.

The way I decided to handle this was to have the initialization function take and store an Elixir Process PID, and have the video callback function send a message to that PID with the video frame when called. Side note: this is currently implemented with a global variable in the C code, so you can currently only run one video context at a time.

In the `send_data_to_pid` function, which is called by the video callback, we take the raw RGB data and convert it to PNG via the `svpng` function (huge thanks to fellow DockYarder Jason Goldberger for helping me fumble through C for the first time since that one college class on OpenGL almost 20 years ago). We store the PNG in an Erlang binary via `enif_make_new_binary`, then send it to the video callback pid via `enif_send`. ([Github Link](https://github.com/TheFirstAvenger/kinext/blob/v0.2.0/native/nifs/kinext.c#L198-L225)):

![Video Callback send\_data\_to\_pid](https://i.imgur.com/4VFCHVx.png)

And on the Elixir side of things, we spin up a simple listener GenServer when the video context is created, passing its pid to the `kinext_start_video` NIF. When we want to get a frame, we call the `freenect_process_events` NIF, which triggers a frame to be sent to, and stored in, the listener GenServer, and then we get the last frame from the listener ([Github Link](https://github.com/TheFirstAvenger/kinext/blob/v0.2.0/lib/kinext/video.ex#L27-L56)):

![Video processing](https://i.imgur.com/mwZocNO.png)

And the simple Listener GenServer ([Github Link](https://github.com/TheFirstAvenger/kinext/blob/v0.2.0/lib/kinext/video/listener.ex#L8-L33)):

![Listener GenServer](https://i.imgur.com/tB8bQin.png)

## The Demo App in Phoenix LiveView

At this point, I finally had everything working, but only from the command line via IEX. As I mentioned above, my interest was in getting Elixir connected to the Kinect -- I have no current plans to build something interesting on top of the library. I am hoping someone else in the Elixir community might take that challenge on! I did, however, want to have a demo app that did more than simple command line interactions. In thinking of the options I had before me, Phoenix LiveView came to mind as the simplest and fastest way to put a UI on Kinext. This proved true, because about 45 minutes after running `mix phx.new kinext_live_view --live`, [the full demo](https://github.com/TheFirstAvenger/kinext_live_view) app was running:

![Kinext LiveView](https://i.imgur.com/kRX4zEh.png)

As you can see from [the LiveView template](https://github.com/TheFirstAvenger/kinext_live_view/blob/v0.1.0/lib/kinext_liveview_web/live/page_live.html.leex) and [the LiveView controller](https://github.com/TheFirstAvenger/kinext_live_view/blob/v0.1.0/lib/kinext_liveview_web/live/page_live.ex), the code to implement the demo app in Phoenix LiveView is incredibly simple. For each function in Kinext we just add a button to the template and a corresponding handle\_event function. That function simply calls the Kinext function and then updates the assign with the new information. The template displays the information stored in the assigns.

The picture frames are displayed using the html "Data URL" functionality, which allows you to embed an image directly in the `src` field of an `img` tag. Since we have the frame already as a PNG in the assigns, we simply `Base.encode64` the frame and use that encoded data as the `src` field of the `img` tag ([Github Link](https://github.com/TheFirstAvenger/kinext_live_view/blob/v0.1.0/lib/kinext_liveview_web/live/page_live.html.leex#L36-L38)):

![Encoding image data in LiveView template](https://i.imgur.com/vULxn7T.png)

Given that the images are about a megabyte each, this is an incredibly inefficient way of handling "video", not something you would do in production. That being said, the responsiveness of the "video" on my local machine was really good, almost on par with what I would expect in a regular video chat.

## Where to go from here

As mentioned above, my intention with Kinext is to provide and support a library for the community to use. Where the project goes from here is up to the community, but I will continue to support it. If you are interested in developing for the Kinect in Elixir, pick up a [Kinect Sensor](https://www.amazon.com/Xbox-Kinect-Sensor-Packaging-Renewed-one/dp/B08124R4SN) and a [USB Adapter](https://www.amazon.com/IDS-Xbox-Kinect-Sensor-Adapter/dp/B073GY3C7Z) and go for it. Please let me know how it goes via [Github Issues](https://github.com/TheFirstAvenger/kinext/issues) (for the bad) or [Twitter](https://twitter.com/1stAvenger) (for the good).

_[DockYard](https://dockyard.com/) is a digital product agency offering custom software, mobile, and web application development consulting. We provide exceptional professional services in strategy, user experience, design, and full stack engineering using Ember.js, React.js, Ruby, and Elixir. With a nationwide staff, we've got consultants in key markets across the United States, including San Francisco, Los Angeles, Denver, Chicago, Austin, New York, and Boston._

### Stay in the Know

Get the latest news and insights on Elixir, Phoenix, machine learning, product strategy, and more—delivered straight to your inbox.

![Narwin holding a press release sheet while opening the DockYard brand kit box](https://assets.dockyard.com/images/narwin-press-release-og-v2.svg)
