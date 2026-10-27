---
title: "Writing Web Audio API code that works in every browser"
date: '2013-09-27T15:54:25-03:00'
category: webclip
summary: 'The post explains how to write Web Audio API code that works across browsers by using AudioContext-MonkeyPatch, updating old method names, and avoiding nodes and parameters not yet supported in Firefox.'
tags: ["web-audio-api", "browser-compatibility", "firefox"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Writing Web Audio API code that works in every browser ✩ Mozilla Hacks – the Web developer blog"
    url: "https://hacks.mozilla.org/2013/08/writing-web-audio-api-code-that-works-in-every-browser/?utm_source=javascriptweekly&utm_medium=email"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2013-09/hacks-mozilla-org--writing-web-audio-api-code-that-works-in-every-browser.md"
    kind: repo
---

The post says developers can target the newer, standards-based Web Audio API while still supporting browsers that use prefixed names or older method names. It recommends using AudioContext-MonkeyPatch to alias prefixed APIs to unprefixed ones, then checking old names in the spec and updating code where needed.

## Reading notes

- AudioContext-MonkeyPatch normalizes the interface so code can use the modern Web Audio API style across Chrome, Opera, Safari, and Firefox.
- The library aliases newer method names such as `start` and `stop` to older browser-specific names when needed.
- Old code may still fail if it relies on methods that the library does not alias, such as `createGainNode` instead of `createGain`.
- The post points readers to the spec section on old names and to a Mozilla article about porting `webkitAudioContext` code.
- Firefox still lacks some node types mentioned in the post, including `MediaStreamAudioSourceNode`, `MediaElementAudioSourceNode`, and `OscillatorNode`.
- It suggests using `ScriptProcessorNode` as a possible workaround when `OscillatorNode` is not available.
- Parameters must also be checked for Firefox support, and the post gives `PannerNode` with the default HRTF panning model as an example.
- While support for that case had landed in Nightly, the post advises setting `panningModel` to `'equalpower'` in the meantime.
- To follow progress, the post recommends the Web Audio mailing list, the umbrella bug for Firefox implementation, and example projects that show compatibility choices.
