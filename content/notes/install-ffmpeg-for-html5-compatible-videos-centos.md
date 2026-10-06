---
title: "Install FFMPEG for HTML5 Compatible Videos – MP4, OGG & WebM on CentOS"
date: '2012-07-02T01:38:50-03:00'
category: webclip
summary: 'The page lists the libraries and build steps needed to compile FFMPEG on CentOS for HTML5-compatible output, including WebM, OGG, Vorbis, x264, Theora, FAAD, FAAC, LAME, and AMR support.'
tags: ["ffmpeg", "centos", "html5-video", "video-codecs"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Install FFMPEG for HTML5 Compatible Videos – MP4, OGG & WebM on CentOS"
    url: "http://pitchpublish.com/?p=158"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2012-07/pitchpublish-com--install-ffmpeg-for-html5-compatible-videos-centos.md"
    kind: repo
---

The page says the libraries must be installed manually, with FFMPEG compiled last using the needed enable options. It gives a root-level CentOS setup sequence, then separate build commands for WebM, OGG, Vorbis, x264, Theora, FAAD, FAAC, LAME, and AMR support.

## Reading notes

- Install the required libraries manually, then compile FFMPEG last with the enable options.
- Log in as root and install the basic prerequisites with yum.
- Add /usr/local/lib to /etc/ld.so.conf if grep does not show it, then run ldconfig.
- Build libvpx for WebM.
- Build libogg and libvorbis for OGG support.
- Build x264 with shared support.
- Build libtheora, faad2, faac, lame, and the opencore-amr components.
- Clone ffmpeg from the Videolan git repository.
- Configure FFMPEG with GPL, version3, nonfree, shared, mp3lame, x264, faac, vorbis, opencore-amr, x11grab, vpx, and theora support.
- Build FFMPEG, build qt-faststart, copy it to /usr/local/bin/, and run ldconfig.
- The page points to another post for FFMPEG commands to use the newly installed tools.
