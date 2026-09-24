---
url: "https://dev.to/k1r0s/how-to-handle-exceptions-with-aspect-programming-and-blame-covfefe"
captured_at: "2026-09-25T00:21:09+01:00"
title: "How To Handle Exceptions With Aspect Programming And Blame Covfefe"
domain: "dev-to"
---

Today I'm going to show you a brief, yet useful example of Aspect Oriented Programming.  

```
import * as React from "react";

import Sidebar from "../Sidebar/Sidebar.main";
import Content from "../Content/Content.main";

import { Advices } from "../../advices/Advices"
import { onException, afterMethod } from "kaop-ts"

export default class Root extends React.Component<null, null> {

    someProp: any

    @onException(Advices.blameCovfefe)
    @afterMethod(Advices.throwOnError)
    render(){
        return (
            <div className="mainContainer">
                <Sidebar />
                <Content />
                {this.someProp.nil}
            </div>
        )
    }
}
```

Enter fullscreen mode Exit fullscreen mode

This is what we get on execution:

> Uncaught TypeError: Cannot read property 'nil' of undefined despite the constant negative press covfefe

Here is the implementation of `Advices`  

```
import { AdvicePool, adviceMetadata, IMetadata } from 'kaop-ts'

export class Advices extends AdvicePool {
  static blameCovfefe (@adviceMetadata meta: IMetadata) {
    meta.exception.message += " despite the constant negative press covfefe"
  }

  static throwOnError (@adviceMetadata meta: IMetadata) {
    if(meta.exception) {
      throw meta.exception
    }
  }
}

```

Enter fullscreen mode Exit fullscreen mode

Maybe this is not a good example, but if you know Twitter's API it might be useful to distract several taxpayers..

But if you think previous example was funny somehow.. Instead of throwing an exception, it would be nice render an error component each time our app fails:  

```
import { AdvicePool, adviceMetadata, IMetadata } from 'kaop-ts'
import { Covfefe } from './covfefe-components'

export class Advices extends AdvicePool {
  static blameRussia (@adviceMetadata meta: IMetadata) {
    if(meta.exception) {
      meta.result = <Covfefe/>
    }
  }
}

```

Enter fullscreen mode Exit fullscreen mode

### [](#okay)Okay

Welp. The idea about Aspect Oriented Programming (aka AOP) is to manage common problems in one place and still access to the needed context.

In this article we're going to use [**kaop-ts**](https://github.com/k1r0s/kaop-ts/)

In the previous example we need to capture exceptions when they occur somehow but we don't want to mess our code pasting same blocks of code everywhere. We simply want to tell our application to apply encapsulated patterns in several life cycle hooks in OOP paradigm (aka: 'Join Points').

AOP is an extension of OOP. It helps us to encourage abstraction and modularity. It is a strong tool against repetition.

You probably remember situations where you've had to paste some blocks of code only replacing one variable or reference in order to replicate some behavior. Think about logs, yeah.

But there are many other cases, most of them are fairly covered by frameworks. In NodeJS environments, for example, Express deals with lots of "common problems" that almost nobody has to deal with, like receiving payload from a HTTP request.

AOP is everywhere, but most frameworks don't provide you tools to extend this technique, by providing access to Join Points. AngularJS, for example, brought a bunch of nice solutions to common problems when JQuery or EJS/Underscore templates were the only way to deal with DOM manipulation.

Modern frameworks that include DOM manipulation like Vue or Angular, and many others encourage declarative programming, which includes implicit instructions to be executed to achieve its purpose (DOM manipulation) my removing the side effects. React is more explicit, the idea of JSX with the virtualDOM was simply awesome.

kaop-ts is nice for building big things from the bottom with a powerful layer of abstraction and architecture assets. But it also enhances your code by providing access to Join Points (aka: 'apply encapsulated patterns in several life cycle hooks in OOP paradigm by accessing dynamic contexts').

Nowadays it includes access to: `AfterInstance, BeforeInstance, AfterMethod, BeforeMethod, OnException` where you can retrieve:  

```
export class Registry extends AdvicePool {
  static log (@adviceMetadata meta: IMetadata) {
    meta.args // Arguments to be received by decorated method
    meta.propertyKey // Name of the decorated method as string
    meta.scope // Instance or the context of the call stack
    meta.rawMethod // Original method (contains metadata)
    meta.target // Class definition
    meta.result // The returned value by the method
  }
}
```

Enter fullscreen mode Exit fullscreen mode

You may read and write these references and, of course, perform async request without messing the call-stack. In other words, you can access service layer within Advices (aka: 'functions that are executed within Join Points') and perform async requests to retrieve data and inject to decorated methods.

Read this piece of code carefully:  

```
// view.ts
import { beforeMethod } from 'kaop-ts'
import { PersistanceAdvices } from './persistance-advices'
import { FlowAdvices } from './flow-advices'
import { OrderModel } from './order-model'

class View {
  @beforeMethod(PersistanceAdvices.read, OrderModel)
  @beforeMethod(FlowAdvices.validate)
  update (data?) { ... }
}


// persistance-advices.ts
import { AdvicePool, adviceMetadata, adviceParam, IMetadata } from 'kaop-ts'
import { Service } from './somewhere'
import { ICommonModel } from './somewhere'

export class PersistanceAdvices extends AdvicePool {
  static read (@adviceMetadata meta: IMetadata, @adviceParam(0) model: ICommonModel) {
    Service.get(model.url)
    .then(data => meta.args.push(data))
    .then(this.next) 
  }
}
```

Enter fullscreen mode Exit fullscreen mode

`this.next` is a tool to explicitly tell kaop-ts that the current operation needs time to finish, so following operations will wait until fulfilled

Note that `View class` has a method called `update`, if we instantiate `View` and call `update()` on it we re going to trigger a composed call-stack, but the implementation is clean, declarative and is out of side effects.

Our `viewInstance` will receive request data as an argument in update method and **it will be executed as if we provided explicitly as an argument**.

So, thanks for reading. Hope you enjoy it. [Checkout the repo](https://github.com/k1r0s/kaop-ts/) and feel free to contribute :) happy codding!

Hail covfefe.
