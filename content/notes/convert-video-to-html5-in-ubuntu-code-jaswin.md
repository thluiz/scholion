---
title: "Convert Video to HTML5 in Ubuntu"
date: '2012-03-01T13:10:29-03:00'
category: webclip
summary: 'The post shows how to install ffmpeg and related tools on Ubuntu, then run a bash script that converts a video to ogv, webm, and mp4, creates a poster image, and writes the HTML5 video markup.'
tags: ["ubuntu", "ffmpeg", "html5-video", "bash"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Convert Video to HTML5 in Ubuntu – Code – Jaswin"
    url: "http://jaswin.net/code/convert-video-to-html5-in-ubuntu/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2012-03/jaswin-net--convert-video-to-html5-in-ubuntu-code-jaswin.md"
    kind: repo
---

The post explains a workflow for converting videos to HTML5 formats on Ubuntu. It says the setup takes time, but once ffmpeg and its dependencies are installed, the script can process many videos, keep the original file intact, generate a screenshot for the poster attribute, and write the HTML code.

## Reading notes

- The installation section removes older ffmpeg, x264, libx264-dev, and yasm packages first.
- It then installs build tools and libraries needed for ffmpeg, x264, lame, and libvpx.
- The author notes that ffmpeg takes the longest to build.
- The script accepts one video file as input.
- It creates a thumbnail by picking a random point in the video and using ffmpeg to capture one frame.
- It converts the video to ogv, webm, and mp4.
- It writes a separate HTML file with plain video markup and three source elements.
- The original video file is left unchanged.
