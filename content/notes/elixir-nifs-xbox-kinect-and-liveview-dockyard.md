---
title: "Elixir, NIFs, Xbox Kinect, and LiveView"
date: '2026-11-16T19:58:00+00:00'
category: webclip
summary: 'The post traces how Kinext was built to connect an Xbox Kinect to Elixir through Erlang NIFs, then expose it in a simple Phoenix LiveView demo app.'
tags: ["elixir", "nifs", "phoenix-liveview", "kinect"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Elixir, NIFs, Xbox Kinect, and LiveView - DockYard"
    url: "https://dockyard.com/blog/2020/05/11/elixir-nifs-xbox-kinect-and-liveview"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/dockyard-com--elixir-nifs-xbox-kinect-and-liveview-dockyard.md"
    kind: repo
---

The post follows the path from a borrowed Xbox Kinect to a working Elixir integration. It explains why NIFs were needed to reach `libfreenect`, how opaque C pointers were handled with resources, and why Phoenix LiveView was used for a quick demo UI.

## Reading notes

- The author first became interested in Kinect by seeing what people did with it connected to computers, but did not buy one at the time.
- Years later, a borrowed Kinect led to a project that touches Elixir, NIFs, Kinect, and Phoenix LiveView.
- The post is a journey report, not an in-depth guide to NIFs or Phoenix LiveView.
- OpenKinect’s `libfreenect` gives direct C access to Kinect hardware features such as tilt motors, LED, audio, video, and depth sensors.
- Elixir cannot call C bindings directly, so Erlang NIFs are used to bridge Elixir and `libfreenect`.
- NIFs let native code run inside the Erlang VM, but they also carry the risk of crashing the VM.
- Phoenix LiveView was chosen because it was the simplest way to build a small interactive demo app.
- The author validated the Kinect connection by installing `libfreenect` and using `freenect-glview`.
- The first NIF work centered on `freenect_init`, which creates a context for the `libfreenect` environment.
- Because `context` and `device` are opaque pointers, the project used NIF resources so Elixir could carry them as references and pass them back into later NIF calls.
- The Elixir module defines NIF functions that are replaced at load time by the native implementations.
- Video handling uses a callback: `libfreenect` sends one frame each time events are processed.
- The callback stores the Elixir process PID and sends the frame to that PID.
- Raw RGB data is converted to PNG with `svpng`, placed in an Erlang binary, and sent with `enif_send`.
- On the Elixir side, a listener GenServer receives frames and stores the latest one.
- The demo app uses LiveView buttons and `handle_event` functions to call Kinext and update assigns.
- Frames are embedded in the page as Data URLs by base64-encoding the PNG stored in assigns.
- The author notes that this image approach is inefficient for video, but felt responsive on a local machine.
- The project is intended as a library for the community, and the author invites others to build on it.
