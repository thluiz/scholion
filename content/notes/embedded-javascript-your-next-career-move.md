---
title: "Embedded JavaScript: Your Next Career Move"
date: '2013-09-05T13:54:41-03:00'
category: webclip
summary: 'The article frames JavaScript as an embedded language used inside web pages, apps, and game engines, and argues that its growing use in native software creates opportunities for developers who can bridge scripting and runtime integration.'
tags: ["javascript", "embedded-systems", "runtime"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "DailyJS: Embedded JavaScript: Your Next Career Move"
    url: "http://dailyjs.com/2013/08/26/embeddedjs/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2013-09/dailyjs-com--embedded-javascript-your-next-career-move.md"
    kind: repo
---

JavaScript is presented as more than a web language. The post treats it as an embedded language that sits inside web pages and can also be used inside native software through bindings, web views, and runtime integrations.

## Reading notes

- JavaScript started in web pages, but it can also be understood as an embedded language connected to native data structures and runtime functions.
- Embedded scripting is useful in large C++, C#, and Objective-C projects because it can reduce rebuild and deployment work when only small changes are needed.
- In game development, Python and Lua are common scripting choices for interfaces, logic, asset loading, and AI, and UnrealScript helped support modding around Unreal engine games.
- Python and Lua are widely adopted and easy to bind to native code; libraries such as Boost.Python and Luabind are cited as examples.
- A web view can be an alternative to low-level binding, with JavaScript handling parts of a UI built in HTML.
- Once UI grows large, the JavaScript layer becomes harder to manage, which is where frameworks like Backbone and AngularJS are used.
- Embedding JavaScript as a runtime is described as uneven across languages and ecosystems.
- In .NET, the article mentions IronJS, ClearScript, and Jurassic as ways to run JavaScript inside applications, with V8 presented as the preferred option.
- In Objective-C, Apple’s WebKit guide and JavaScriptCore are presented as ways to access JavaScript from native code.
- The author says colleagues in Objective-C, C++, C#, and JavaScript all want JavaScript embedded in games, desktop software, and mobile apps.
- The article also notes limits of JavaScript, including its type system, scope rules, and coercion behavior, especially for developers used to C-like languages.
- The final point is that JavaScript has strong momentum across more platforms, so working with scripts for games and apps is becoming a relevant skill.
