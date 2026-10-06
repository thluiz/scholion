---
title: "Bringing Node.js to Windows 10 IoT Core"
date: '2015-05-14T17:12:32-03:00'
category: webclip
summary: 'Microsoft says Node.js support for Windows 10 IoT Core will use Chakra to fill the Windows on ARM gap, reduce disk footprint, and add UWP access, debugging, and device support.'
tags: ["node-js", "windows-10-iot-core", "chakra", "uwp"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Bringing Node.js to Windows 10 IoT Core"
    url: "http://blogs.windows.com/buildingapps/2015/05/12/bringing-node-js-to-windows-10-iot-core/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-05/blogs-windows-com--bringing-node-js-to-windows-10-iot-core.md"
    kind: repo
---

Microsoft says it is bringing Node.js to Windows 10 IoT Core by using the built-in Chakra engine instead of V8. The goal is to make Node.js work on Windows on ARM devices, reduce disk footprint, and give Node.js apps first-class UWP support.

## Reading notes

- Microsoft frames the work as part of its investment in IoT and says Windows 10 IoT will run connected devices such as gateways, point-of-sale systems, robotics, and medical devices.
- The project addresses a gap where developers cannot use Node.js on Windows on ARM devices.
- The chosen path is a wrapper between Chakra JSRT hosting APIs and the V8 hosting APIs used by Node.js v0.12.
- The public code is available on GitHub.
- The changes are intended to let Node.js run as a classic Windows application on Windows 10 devices.
- The changes also let Node.js run inside a Universal Windows application and access UWP APIs.
- Visual Studio debugging for Node.js apps on Windows 10 is part of the support.
- The post says the work is still in early development and that a pull request to Node.js will come after the code is stabilized.
- For getting started, the post points to a Classic Windows app sample that displays system memory usage through a native addon.
- The post also describes a Universal Windows app template from NTVS IoT Extension Beta, which installs the Chakra-based Node.js build and the uwp package.
- The uwp module is used with require and uwp.projectNamespace to access UWP namespaces from Node.js.
- A sample shows toggling an LED by writing to a GPIO pin from a Node.js app.
- Remote debugging is described as working through Visual Studio with the device IP configured in the project settings.
- The post closes by noting known issues, including incomplete support for VM module and packages such as serialport and firmata, and asks for community feedback.
