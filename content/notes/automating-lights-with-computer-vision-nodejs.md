---
title: "Automating lights with Computer Vision & NodeJS"
date: '2020-11-02T11:56:08-03:00'
category: webclip
summary: 'The article proposes using office cameras, OpenCV, and Node.js to detect people in frame quadrants and switch off lights where no one is present, reducing wasted power.'
tags: ["computer-vision", "nodejs", "opencv", "energy-saving"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Automating lights with Computer Vision & NodeJS | by Mudassir H | Humanity Required | Medium"
    url: "https://medium.com/softway-blog/automating-lights-with-computer-vision-nodejs-fb9b614b75b2"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2020-11/medium-com--automating-lights-with-computer-vision-nodejs.md"
    kind: repo
---

The article describes a smart lighting setup that uses existing office cameras instead of extra hardware. It reads the video feed, detects people with an OpenCV HAAR frontal face classifier, and decides which quadrant of the room should stay lit.

## Reading notes

- Offices often have lights on in areas with few or no people nearby, which wastes electricity and increases environmental impact.
- Simple signs asking people to turn off lights have limited effect, and relying on human memory is not enough.
- A 10-watt bulb left on when not needed adds measurable cost over time, especially across many office lights.
- Many automation solutions need additional hardware and regular setup, which adds maintenance costs.
- The proposed approach uses cameras already installed in offices to reduce investment.
- The system processes incoming camera frames with Computer Vision.
- Each frame is divided into four quadrants.
- If no people are detected in a quadrant, the lights for that quadrant are turned off.
- The implementation uses opencv4Nodejs, Socket.IO, and Express.
- The article outlines steps such as importing libraries, capturing video, streaming frames to a web app, detecting faces, and mapping detected positions to quadrants.
- The web app simulates lighting changes by changing bulb color for the active quadrant.
- The author says the same socket-based setup could be extended to control physical lights through relays.
