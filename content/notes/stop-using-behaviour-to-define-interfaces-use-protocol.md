---
title: "Stop using Behaviour to define interfaces, use Protocol!"
date: '2021-07-22T14:48:07-03:00'
category: webclip
summary: 'The post argues that Behaviour fits impure interfaces with shared logic, while Protocol is the right tool for pure interfaces. It also proposes growing pure interfaces into richer ones and introduces Objext.'
tags: ["elixir", "protocol", "behaviour", "interfaces"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Stop using Behaviour to define interfaces, use Protocol! - Yiming Chen"
    url: "https://yiming.dev/blog/2021/07/18/stop-using-behaviour-to-define-interfaces-use-protocol/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2021-07/yiming-dev--stop-using-behaviour-to-define-interfaces-use-protocol.md"
    kind: repo
---

The post says Elixir developers often use Behaviour to model common interfaces, but that this feels awkward when the goal is only dynamic dispatch. It points to naming confusion, module injection, Mox’s global-state mocks, and delegation patterns as signs that Behaviour is being used for pure interfaces.

It argues that Protocols are better for pure interfaces because they define an API without extra shared logic, while Behaviours are meant for impure interfaces where the interface module carries reusable logic, as with GenServer. The author recommends using Protocol for pure interfaces, Behaviour for impure interfaces, and growing pure interfaces into richer ones when needed.

## Reading notes

- Elixir developers often use Behaviour to define common interfaces, but the author finds that awkward for simple polymorphism.
- The author lists several problems with that pattern: confusing terminology, passing modules around, Mox mocks with global state, and common delegation from a behaviour module to callback modules.
- Behaviour is presented as a better fit for impure interfaces, where the interface module adds shared logic around the call.
- GenServer is used as the main example of an impure interface, because it wraps common async logic in shared functions like GenServer.call and GenServer.cast.
- Protocol is presented as the right tool for pure interfaces, with the official docs quoted as saying that a protocol specifies an API that implementations define.
- The author suggests that common logic should be extracted into the behaviour module so callback modules stay simple.
- The post introduces Objext as a library for defining interfaces in Elixir, alongside Promox for easier Protocol mocks.
- The final takeaway is to choose the interface type deliberately: Protocol for pure interfaces, Behaviour for impure interfaces, and to grow pure interfaces into impure ones when possible.
