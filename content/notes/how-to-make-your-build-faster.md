---
title: "How to make your build faster"
date: '2012-06-04T12:53:41-03:00'
category: webclip
summary: 'The post argues that build speed can be improved without buying SSDs by using smarter project structures, parallel builds in Visual Studio/MSBuild, and Mighty Moose’s incremental build information.'
tags: ["build-times", "visual-studio", "msbuild", "mighty-moose"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "How to make your build faster | Greg Young"
    url: "http://codebetter.com/gregyoung/2012/03/26/how-to-make-your-build-faster/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2012-06/codebetter-com--how-to-make-your-build-faster.md"
    kind: repo
---

The post argues that slow build feedback disrupts work, and says build times can be improved in several ways without buying SSDs. It focuses on smarter project layouts, parallel builds in Visual Studio and MSBuild, and the faster incremental builds available through Mighty Moose.

## Reading notes

- The author says long feedback cycles break concentration and make it hard to stay on task.
- Smarter project layouts can help, and larger well-factored projects may build faster than many smaller ones.
- Visual Studio and MSBuild already support parallel builds, and maxcpucount lets multiple projects build concurrently when dependencies allow it.
- Parallel builds can improve times in some cases, but the author says the average gain is often only around 20–25%.
- Mighty Moose uses more information than MSBuild because it knows what is changing and how that affects the dependency graph.
- The author says static analysis can help decide whether public contracts changed and what tests need to run.
- In the example given, Mighty Moose reduces an incremental build plus test discovery and test execution from about 4.5 seconds in MSBuild to about 2.5–3 seconds.
- The feature is opt-in because compatibility with existing Visual Studio projects is the main concern.
