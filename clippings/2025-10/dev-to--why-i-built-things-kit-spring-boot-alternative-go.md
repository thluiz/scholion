---
url: "https://dev.to/noxymon/why-i-built-things-kit-a-spring-boot-alternative-for-go-3ip4?"
captured_at: "2025-10-22T11:19:51+01:00"
title: "Why I Built Things-Kit: A Spring Boot Alternative for Go - DEV Community"
domain: "dev-to"
---

---
I built [Things-Kit](https://github.com/things-kit/things-kit), a modular microservice framework for Go that brings Spring Boot's developer experience while staying true to Go's philosophy. It's built on Uber Fx and provides composable modules for common infrastructure concerns.

___

## [](https://dev.to/noxymon/why-i-built-things-kit-a-spring-boot-alternative-for-go-3ip4?#my-journey-with-microservices)My Journey with Microservices

Like many developers, I've built my share of microservices. Started with monoliths, moved to microservices, learned the hard way about distributed systems, and eventually found patterns that work.

But here's the thing: every time I started a new Go microservice, I found myself in the same frustrating cycle.

___

## [](https://dev.to/noxymon/why-i-built-things-kit-a-spring-boot-alternative-for-go-3ip4?#the-groundhog-day-problem)The Groundhog Day Problem

Picture this: It's Monday morning. You're starting a new microservice. You know exactly what you need to build, but first...

**You need to set up the HTTP server:**  

```
<span>router</span> <span>:=</span> <span>gin</span><span>.</span><span>Default</span><span>()</span>
<span>router</span><span>.</span><span>Use</span><span>(</span><span>middleware</span><span>.</span><span>Recovery</span><span>())</span>
<span>router</span><span>.</span><span>Use</span><span>(</span><span>middleware</span><span>.</span><span>Logger</span><span>())</span>
<span>// ... 20 more lines of setup</span>
```

**Then wire up dependencies:**  

```
<span>logger</span> <span>:=</span> <span>zap</span><span>.</span><span>NewProduction</span><span>()</span>
<span>defer</span> <span>logger</span><span>.</span><span>Sync</span><span>()</span>

<span>db</span><span>,</span> <span>err</span> <span>:=</span> <span>sql</span><span>.</span><span>Open</span><span>(</span><span>"postgres"</span><span>,</span> <span>connectionString</span><span>)</span>
<span>if</span> <span>err</span> <span>!=</span> <span>nil</span> <span>{</span>
    <span>logger</span><span>.</span><span>Fatal</span><span>(</span><span>"failed to connect"</span><span>,</span> <span>zap</span><span>.</span><span>Error</span><span>(</span><span>err</span><span>))</span>
<span>}</span>
<span>defer</span> <span>db</span><span>.</span><span>Close</span><span>()</span>

<span>cache</span> <span>:=</span> <span>redis</span><span>.</span><span>NewClient</span><span>(</span><span>&amp;</span><span>redis</span><span>.</span><span>Options</span><span>{</span>
    <span>Addr</span><span>:</span> <span>config</span><span>.</span><span>RedisAddr</span><span>,</span>
<span>})</span>
<span>defer</span> <span>cache</span><span>.</span><span>Close</span><span>()</span>

<span>// Create services</span>
<span>userService</span> <span>:=</span> <span>service</span><span>.</span><span>NewUserService</span><span>(</span><span>logger</span><span>,</span> <span>db</span><span>,</span> <span>cache</span><span>)</span>
<span>orderService</span> <span>:=</span> <span>service</span><span>.</span><span>NewOrderService</span><span>(</span><span>logger</span><span>,</span> <span>db</span><span>,</span> <span>cache</span><span>)</span>

<span>// Create handlers</span>
<span>userHandler</span> <span>:=</span> <span>handler</span><span>.</span><span>NewUserHandler</span><span>(</span><span>userService</span><span>)</span>
<span>orderHandler</span> <span>:=</span> <span>handler</span><span>.</span><span>NewOrderHandler</span><span>(</span><span>orderService</span><span>)</span>

<span>// Register routes</span>
<span>router</span><span>.</span><span>GET</span><span>(</span><span>"/users/:id"</span><span>,</span> <span>userHandler</span><span>.</span><span>GetUser</span><span>)</span>
<span>router</span><span>.</span><span>POST</span><span>(</span><span>"/orders"</span><span>,</span> <span>orderHandler</span><span>.</span><span>CreateOrder</span><span>)</span>
<span>// ... more routes</span>
```

**Don't forget configuration:**  

```
<span>viper</span><span>.</span><span>SetConfigName</span><span>(</span><span>"config"</span><span>)</span>
<span>viper</span><span>.</span><span>AddConfigPath</span><span>(</span><span>"."</span><span>)</span>
<span>if</span> <span>err</span> <span>:=</span> <span>viper</span><span>.</span><span>ReadInConfig</span><span>();</span> <span>err</span> <span>!=</span> <span>nil</span> <span>{</span>
    <span>log</span><span>.</span><span>Fatal</span><span>(</span><span>err</span><span>)</span>
<span>}</span>

<span>type</span> <span>Config</span> <span>struct</span> <span>{</span>
    <span>HTTPPort</span>  <span>int</span>
    <span>DBHost</span>    <span>string</span>
    <span>DBPort</span>    <span>int</span>
    <span>RedisAddr</span> <span>string</span>
    <span>LogLevel</span>  <span>string</span>
    <span>// ... 20 more fields</span>
<span>}</span>

<span>var</span> <span>config</span> <span>Config</span>
<span>if</span> <span>err</span> <span>:=</span> <span>viper</span><span>.</span><span>Unmarshal</span><span>(</span><span>&amp;</span><span>config</span><span>);</span> <span>err</span> <span>!=</span> <span>nil</span> <span>{</span>
    <span>log</span><span>.</span><span>Fatal</span><span>(</span><span>err</span><span>)</span>
<span>}</span>
```

**And of course, graceful shutdown:**  

```
<span>srv</span> <span>:=</span> <span>&amp;</span><span>http</span><span>.</span><span>Server</span><span>{</span>
    <span>Addr</span><span>:</span>    <span>fmt</span><span>.</span><span>Sprintf</span><span>(</span><span>":%d"</span><span>,</span> <span>config</span><span>.</span><span>HTTPPort</span><span>),</span>
    <span>Handler</span><span>:</span> <span>router</span><span>,</span>
<span>}</span>

<span>quit</span> <span>:=</span> <span>make</span><span>(</span><span>chan</span> <span>os</span><span>.</span><span>Signal</span><span>,</span> <span>1</span><span>)</span>
<span>signal</span><span>.</span><span>Notify</span><span>(</span><span>quit</span><span>,</span> <span>syscall</span><span>.</span><span>SIGINT</span><span>,</span> <span>syscall</span><span>.</span><span>SIGTERM</span><span>)</span>

<span>go</span> <span>func</span><span>()</span> <span>{</span>
    <span>if</span> <span>err</span> <span>:=</span> <span>srv</span><span>.</span><span>ListenAndServe</span><span>();</span> <span>err</span> <span>!=</span> <span>nil</span> <span>&amp;&amp;</span> <span>err</span> <span>!=</span> <span>http</span><span>.</span><span>ErrServerClosed</span> <span>{</span>
        <span>logger</span><span>.</span><span>Fatal</span><span>(</span><span>"server failed"</span><span>,</span> <span>zap</span><span>.</span><span>Error</span><span>(</span><span>err</span><span>))</span>
    <span>}</span>
<span>}()</span>

<span>&lt;-</span><span>quit</span>
<span>logger</span><span>.</span><span>Info</span><span>(</span><span>"shutting down server..."</span><span>)</span>

<span>ctx</span><span>,</span> <span>cancel</span> <span>:=</span> <span>context</span><span>.</span><span>WithTimeout</span><span>(</span><span>context</span><span>.</span><span>Background</span><span>(),</span> <span>5</span><span>*</span><span>time</span><span>.</span><span>Second</span><span>)</span>
<span>defer</span> <span>cancel</span><span>()</span>

<span>if</span> <span>err</span> <span>:=</span> <span>srv</span><span>.</span><span>Shutdown</span><span>(</span><span>ctx</span><span>);</span> <span>err</span> <span>!=</span> <span>nil</span> <span>{</span>
    <span>logger</span><span>.</span><span>Fatal</span><span>(</span><span>"server forced to shutdown"</span><span>,</span> <span>zap</span><span>.</span><span>Error</span><span>(</span><span>err</span><span>))</span>
<span>}</span>

<span>logger</span><span>.</span><span>Info</span><span>(</span><span>"server exited"</span><span>)</span>
```

**By now, you've written 100+ lines of code** and you haven't even started on your actual business logic!

Sound familiar? 😅

___

## [](https://dev.to/noxymon/why-i-built-things-kit-a-spring-boot-alternative-for-go-3ip4?#the-copypaste-trap)The Copy-Paste Trap

My first solution? "I'll just copy from my last project!"

But then:

-   Different projects used different patterns
-   Some had better error handling
-   Others had better testing setups
-   Configuration structures diverged
-   Updates to one project didn't propagate

I was maintaining the same infrastructure code in 15+ microservices, each slightly different. When I found a bug or wanted to improve something, I had to update it everywhere.

There had to be a better way.

___

## [](https://dev.to/noxymon/why-i-built-things-kit-a-spring-boot-alternative-for-go-3ip4?#learning-from-spring-boot)Learning from Spring Boot

I come from a Java background (yes, I said it on a Go blog 😄). One thing Spring Boot does brilliantly is this:  

```
<span>@SpringBootApplication</span>
<span>public</span> <span>class</span> <span>Application</span> <span>{</span>
    <span>public</span> <span>static</span> <span>void</span> <span>main</span><span>(</span><span>String</span><span>[]</span> <span>args</span><span>)</span> <span>{</span>
        <span>SpringApplication</span><span>.</span><span>run</span><span>(</span><span>Application</span><span>.</span><span>class</span><span>,</span> <span>args</span><span>);</span>
    <span>}</span>
<span>}</span>
```

That's it. HTTP server? Check. Dependency injection? Check. Configuration? Check. Database connections? Check. Logging? Check.

**But here's what I loved most:** It wasn't magic. It was conventions over configuration with escape hatches everywhere. Need custom behavior? Implement an interface. Want a different database? Swap the dependency.

Could we bring this experience to Go without sacrificing Go's simplicity?

___

## [](https://dev.to/noxymon/why-i-built-things-kit-a-spring-boot-alternative-for-go-3ip4?#the-go-challenge)The Go Challenge

Go isn't Java. And that's great! Go's philosophy is different:

-   Simplicity over cleverness
-   Explicit over implicit
-   Composition over inheritance
-   Small, focused standard library

Any solution had to respect these principles. No magic. No reflection-heavy frameworks. No "enterprise" complexity.

But I still wanted:

-   ✅ Minimal boilerplate
-   ✅ Clear dependency injection
-   ✅ Testable code
-   ✅ Swappable components
-   ✅ Graceful lifecycle management

___

## [](https://dev.to/noxymon/why-i-built-things-kit-a-spring-boot-alternative-for-go-3ip4?#enter-uber-fx)Enter Uber Fx

Then I discovered [Uber Fx](https://uber-go.github.io/fx/).

Fx is a dependency injection framework from Uber (yes, the ride-sharing company uses this in production). It's not magic - it's just a clever use of Go's type system and reflection to wire dependencies.  

```
<span>func</span> <span>main</span><span>()</span> <span>{</span>
    <span>fx</span><span>.</span><span>New</span><span>(</span>
        <span>fx</span><span>.</span><span>Provide</span><span>(</span><span>NewLogger</span><span>),</span>
        <span>fx</span><span>.</span><span>Provide</span><span>(</span><span>NewDatabase</span><span>),</span>
        <span>fx</span><span>.</span><span>Provide</span><span>(</span><span>NewUserService</span><span>),</span>
        <span>fx</span><span>.</span><span>Invoke</span><span>(</span><span>RunServer</span><span>),</span>
    <span>)</span><span>.</span><span>Run</span><span>()</span>
<span>}</span>
```

This felt right! But you still had to:

-   Write all the `New*` functions
-   Handle lifecycle hooks manually
-   Set up configuration loading
-   Manage graceful shutdown
-   Create server instances

Every. Single. Time.

___

## [](https://dev.to/noxymon/why-i-built-things-kit-a-spring-boot-alternative-for-go-3ip4?#the-solution-thingskit)The Solution: Things-Kit

What if we could package these common patterns into reusable modules?

Here's what the same microservice looks like with Things-Kit:  

```
<span>package</span> <span>main</span>

<span>import</span> <span>(</span>
    <span>"github.com/things-kit/app"</span>
    <span>"github.com/things-kit/module/httpgin"</span>
    <span>"github.com/things-kit/module/logging"</span>
    <span>"github.com/things-kit/module/sqlc"</span>
    <span>"github.com/things-kit/module/viperconfig"</span>
    <span>"myapp/internal/user"</span>
<span>)</span>

<span>func</span> <span>main</span><span>()</span> <span>{</span>
    <span>app</span><span>.</span><span>New</span><span>(</span>
        <span>viperconfig</span><span>.</span><span>Module</span><span>,</span>  <span>// Configuration</span>
        <span>logging</span><span>.</span><span>Module</span><span>,</span>      <span>// Logging</span>
        <span>sqlc</span><span>.</span><span>Module</span><span>,</span>         <span>// Database</span>
        <span>httpgin</span><span>.</span><span>Module</span><span>,</span>      <span>// HTTP server</span>
        <span>user</span><span>.</span><span>Module</span><span>,</span>         <span>// Your business logic</span>
    <span>)</span><span>.</span><span>Run</span><span>()</span>
<span>}</span>
```

**That's it.**

No HTTP server setup. No manual wiring. No graceful shutdown code. No configuration loading boilerplate.

But unlike magic frameworks, you can see exactly what's happening. Each module is just an Fx module providing certain types:  

```
<span>// Inside the logging module</span>
<span>var</span> <span>Module</span> <span>=</span> <span>fx</span><span>.</span><span>Module</span><span>(</span><span>"logging"</span><span>,</span>
    <span>fx</span><span>.</span><span>Provide</span><span>(</span><span>NewLogger</span><span>),</span>
<span>)</span>

<span>func</span> <span>NewLogger</span><span>(</span><span>config</span> <span>Config</span><span>)</span> <span>(</span><span>log</span><span>.</span><span>Logger</span><span>,</span> <span>error</span><span>)</span> <span>{</span>
    <span>// Standard Zap logger setup</span>
    <span>return</span> <span>zap</span><span>.</span><span>NewProduction</span><span>()</span>
<span>}</span>
```

___

## [](https://dev.to/noxymon/why-i-built-things-kit-a-spring-boot-alternative-for-go-3ip4?#core-principles)Core Principles

Building Things-Kit, I stuck to five principles:

### [](https://dev.to/noxymon/why-i-built-things-kit-a-spring-boot-alternative-for-go-3ip4?#1-modularity-first)1\. **Modularity First**

Every component is an independent Go module. Need just logging? Import just logging. Your binary only includes what you actually use.  

```
<span>import</span> <span>"github.com/things-kit/module/logging"</span>
```

Each module is versioned independently. No monolithic framework version hell.

### [](https://dev.to/noxymon/why-i-built-things-kit-a-spring-boot-alternative-for-go-3ip4?#2-program-to-interfaces)2\. **Program to Interfaces**

Your code depends on interfaces, not concrete implementations:  

```
<span>type</span> <span>UserHandler</span> <span>struct</span> <span>{</span>
    <span>logger</span> <span>log</span><span>.</span><span>Logger</span>      <span>// Not *zap.Logger</span>
    <span>db</span>     <span>*</span><span>sql</span><span>.</span><span>DB</span>         <span>// Standard library</span>
    <span>cache</span>  <span>cache</span><span>.</span><span>Cache</span>     <span>// Not *redis.Client</span>
<span>}</span>
```

Want to swap Zap for Zerolog? Implement the `log.Logger` interface. Want to use Valkey instead of Redis? Implement the `cache.Cache` interface.

### [](https://dev.to/noxymon/why-i-built-things-kit-a-spring-boot-alternative-for-go-3ip4?#3-convention-over-configuration)3\. **Convention over Configuration**

Everything works out of the box with sensible defaults:  

```
<span># config.yaml</span>
<span>http</span><span>:</span>
  <span>port</span><span>:</span> <span>8080</span>  <span># That's it for basic HTTP</span>

<span>logging</span><span>:</span>
  <span>level</span><span>:</span> <span>info</span>  <span># Sensible default</span>
```

But every value is overridable when you need it.

### [](https://dev.to/noxymon/why-i-built-things-kit-a-spring-boot-alternative-for-go-3ip4?#4-no-magic)4\. **No Magic**

Every module is just regular Go code using Fx. You can read the source and understand exactly what's happening. No code generation. No build tags. No reflection tricks.  

```
<span>// You can always access the underlying types</span>
<span>fx</span><span>.</span><span>Invoke</span><span>(</span><span>func</span><span>(</span><span>logger</span> <span>log</span><span>.</span><span>Logger</span><span>)</span> <span>{</span>
    <span>// This is the actual *zap.Logger if you need it</span>
    <span>if</span> <span>zapLogger</span><span>,</span> <span>ok</span> <span>:=</span> <span>logger</span><span>.</span><span>(</span><span>*</span><span>zap</span><span>.</span><span>Logger</span><span>);</span> <span>ok</span> <span>{</span>
        <span>// Use Zap-specific features</span>
    <span>}</span>
<span>})</span>
```

### [](https://dev.to/noxymon/why-i-built-things-kit-a-spring-boot-alternative-for-go-3ip4?#5-lifecycle-aware)5\. **Lifecycle Aware**

All modules hook into Fx's lifecycle for graceful startup and shutdown:  

```
<span>fx</span><span>.</span><span>Invoke</span><span>(</span><span>func</span><span>(</span><span>lc</span> <span>fx</span><span>.</span><span>Lifecycle</span><span>,</span> <span>server</span> <span>Server</span><span>)</span> <span>{</span>
    <span>lc</span><span>.</span><span>Append</span><span>(</span><span>fx</span><span>.</span><span>Hook</span><span>{</span>
        <span>OnStart</span><span>:</span> <span>func</span><span>(</span><span>ctx</span> <span>context</span><span>.</span><span>Context</span><span>)</span> <span>error</span> <span>{</span>
            <span>// Start server</span>
        <span>},</span>
        <span>OnStop</span><span>:</span> <span>func</span><span>(</span><span>ctx</span> <span>context</span><span>.</span><span>Context</span><span>)</span> <span>error</span> <span>{</span>
            <span>// Graceful shutdown</span>
        <span>},</span>
    <span>})</span>
<span>})</span>
```

No signal handling. No goroutine management. It just works.

___

## [](https://dev.to/noxymon/why-i-built-things-kit-a-spring-boot-alternative-for-go-3ip4?#show-me-real-code)Show Me Real Code

Let's build a user service with Things-Kit:

**1\. Your Business Logic** (`internal/user/service.go`):  

```
<span>package</span> <span>user</span>

<span>import</span> <span>"github.com/things-kit/module/log"</span>

<span>type</span> <span>Service</span> <span>struct</span> <span>{</span>
    <span>logger</span> <span>log</span><span>.</span><span>Logger</span>
    <span>repo</span>   <span>*</span><span>Repository</span>
<span>}</span>

<span>func</span> <span>NewService</span><span>(</span><span>logger</span> <span>log</span><span>.</span><span>Logger</span><span>,</span> <span>repo</span> <span>*</span><span>Repository</span><span>)</span> <span>*</span><span>Service</span> <span>{</span>
    <span>return</span> <span>&amp;</span><span>Service</span><span>{</span><span>logger</span><span>:</span> <span>logger</span><span>,</span> <span>repo</span><span>:</span> <span>repo</span><span>}</span>
<span>}</span>

<span>func</span> <span>(</span><span>s</span> <span>*</span><span>Service</span><span>)</span> <span>GetUser</span><span>(</span><span>ctx</span> <span>context</span><span>.</span><span>Context</span><span>,</span> <span>id</span> <span>string</span><span>)</span> <span>(</span><span>*</span><span>User</span><span>,</span> <span>error</span><span>)</span> <span>{</span>
    <span>s</span><span>.</span><span>logger</span><span>.</span><span>InfoC</span><span>(</span><span>ctx</span><span>,</span> <span>"fetching user"</span><span>,</span> <span>log</span><span>.</span><span>Field</span><span>{</span><span>Key</span><span>:</span> <span>"id"</span><span>,</span> <span>Value</span><span>:</span> <span>id</span><span>})</span>
    <span>return</span> <span>s</span><span>.</span><span>repo</span><span>.</span><span>FindByID</span><span>(</span><span>ctx</span><span>,</span> <span>id</span><span>)</span>
<span>}</span>
```

**2\. Your HTTP Handler** (`internal/user/handler.go`):  

```
<span>package</span> <span>user</span>

<span>import</span> <span>(</span>
    <span>"github.com/gin-gonic/gin"</span>
    <span>"github.com/things-kit/module/http"</span>
<span>)</span>

<span>type</span> <span>Handler</span> <span>struct</span> <span>{</span>
    <span>service</span> <span>*</span><span>Service</span>
<span>}</span>

<span>func</span> <span>NewHandler</span><span>(</span><span>service</span> <span>*</span><span>Service</span><span>)</span> <span>*</span><span>Handler</span> <span>{</span>
    <span>return</span> <span>&amp;</span><span>Handler</span><span>{</span><span>service</span><span>:</span> <span>service</span><span>}</span>
<span>}</span>

<span>func</span> <span>(</span><span>h</span> <span>*</span><span>Handler</span><span>)</span> <span>GetUser</span><span>(</span><span>c</span> <span>*</span><span>gin</span><span>.</span><span>Context</span><span>)</span> <span>{</span>
    <span>user</span><span>,</span> <span>err</span> <span>:=</span> <span>h</span><span>.</span><span>service</span><span>.</span><span>GetUser</span><span>(</span><span>c</span><span>.</span><span>Request</span><span>.</span><span>Context</span><span>(),</span> <span>c</span><span>.</span><span>Param</span><span>(</span><span>"id"</span><span>))</span>
    <span>if</span> <span>err</span> <span>!=</span> <span>nil</span> <span>{</span>
        <span>c</span><span>.</span><span>JSON</span><span>(</span><span>500</span><span>,</span> <span>gin</span><span>.</span><span>H</span><span>{</span><span>"error"</span><span>:</span> <span>err</span><span>.</span><span>Error</span><span>()})</span>
        <span>return</span>
    <span>}</span>
    <span>c</span><span>.</span><span>JSON</span><span>(</span><span>200</span><span>,</span> <span>user</span><span>)</span>
<span>}</span>

<span>// Register routes</span>
<span>func</span> <span>(</span><span>h</span> <span>*</span><span>Handler</span><span>)</span> <span>RegisterRoutes</span><span>(</span><span>router</span> <span>gin</span><span>.</span><span>IRouter</span><span>)</span> <span>{</span>
    <span>router</span><span>.</span><span>GET</span><span>(</span><span>"/users/:id"</span><span>,</span> <span>h</span><span>.</span><span>GetUser</span><span>)</span>
<span>}</span>
```

**3\. Wire It Together** (`internal/user/module.go`):  

```
<span>package</span> <span>user</span>

<span>import</span> <span>(</span>
    <span>"go.uber.org/fx"</span>
    <span>"github.com/things-kit/module/httpgin"</span>
<span>)</span>

<span>var</span> <span>Module</span> <span>=</span> <span>fx</span><span>.</span><span>Module</span><span>(</span><span>"user"</span><span>,</span>
    <span>fx</span><span>.</span><span>Provide</span><span>(</span><span>NewRepository</span><span>),</span>
    <span>fx</span><span>.</span><span>Provide</span><span>(</span><span>NewService</span><span>),</span>
    <span>fx</span><span>.</span><span>Provide</span><span>(</span><span>NewHandler</span><span>),</span>
    <span>fx</span><span>.</span><span>Invoke</span><span>(</span><span>httpgin</span><span>.</span><span>AsHandler</span><span>((</span><span>*</span><span>Handler</span><span>)</span><span>.</span><span>RegisterRoutes</span><span>)),</span>
<span>)</span>
```

**4\. Main** (`cmd/server/main.go`):  

```
<span>package</span> <span>main</span>

<span>import</span> <span>(</span>
    <span>"github.com/things-kit/app"</span>
    <span>"github.com/things-kit/module/httpgin"</span>
    <span>"github.com/things-kit/module/logging"</span>
    <span>"github.com/things-kit/module/sqlc"</span>
    <span>"github.com/things-kit/module/viperconfig"</span>
    <span>"myapp/internal/user"</span>
<span>)</span>

<span>func</span> <span>main</span><span>()</span> <span>{</span>
    <span>app</span><span>.</span><span>New</span><span>(</span>
        <span>viperconfig</span><span>.</span><span>Module</span><span>,</span>
        <span>logging</span><span>.</span><span>Module</span><span>,</span>
        <span>sqlc</span><span>.</span><span>Module</span><span>,</span>
        <span>httpgin</span><span>.</span><span>Module</span><span>,</span>
        <span>user</span><span>.</span><span>Module</span><span>,</span>
    <span>)</span><span>.</span><span>Run</span><span>()</span>
<span>}</span>
```

That's a complete, production-ready microservice!

___

## [](https://dev.to/noxymon/why-i-built-things-kit-a-spring-boot-alternative-for-go-3ip4?#whats-different)What's Different?

### [](https://dev.to/noxymon/why-i-built-things-kit-a-spring-boot-alternative-for-go-3ip4?#before-thingskit)Before Things-Kit:

-   ❌ 150+ lines of infrastructure code
-   ❌ Manual dependency wiring
-   ❌ Custom graceful shutdown
-   ❌ Configuration boilerplate
-   ❌ Repeated across every service

### [](https://dev.to/noxymon/why-i-built-things-kit-a-spring-boot-alternative-for-go-3ip4?#after-thingskit)After Things-Kit:

-   ✅ 10 lines in main
-   ✅ Automatic dependency injection
-   ✅ Built-in lifecycle management
-   ✅ Convention-based configuration
-   ✅ Reusable across all services

___

## [](https://dev.to/noxymon/why-i-built-things-kit-a-spring-boot-alternative-for-go-3ip4?#current-status)Current Status

Things-Kit is **feature-complete** for the initial release:

-   ✅ Core app runner
-   ✅ Configuration (Viper)
-   ✅ Logging (Zap)
-   ✅ HTTP server (Gin)
-   ✅ gRPC server
-   ✅ Database (sqlc/PostgreSQL)
-   ✅ Cache (Redis)
-   ✅ Messaging (Kafka)
-   ✅ Testing utilities

I've built [two complete examples](https://github.com/things-kit):

1.  Basic HTTP service
2.  Full CRUD API with PostgreSQL + integration tests

Both are running in production-like environments.

___

## [](https://dev.to/noxymon/why-i-built-things-kit-a-spring-boot-alternative-for-go-3ip4?#whats-next)What's Next?

In this series, I'll dive deep into:

1.  **This Post:** Why I built it (you are here! 👋)
2.  **Next:** How dependency injection works in Go with Uber Fx
3.  **Tutorial:** Building your first microservice step-by-step
4.  **Deep Dive:** The interface abstraction pattern
5.  **Production:** Taking it from example to production

___

## [](https://dev.to/noxymon/why-i-built-things-kit-a-spring-boot-alternative-for-go-3ip4?#try-it-yourself)Try It Yourself

Want to see it in action?  

```
git clone https://github.com/things-kit/things-kit-example.git
<span>cd </span>things-kit-example
<span>cp </span>config.example.yaml config.yaml
go run ./cmd/server

<span># In another terminal:</span>
curl http://localhost:8080/health
curl http://localhost:8080/greet/DevTo
```

___

## [](https://dev.to/noxymon/why-i-built-things-kit-a-spring-boot-alternative-for-go-3ip4?#i-want-your-feedback)I Want Your Feedback! 🙏

Before I release v1.0, I'm actively seeking feedback:

**Questions for you:**

1.  Does this approach resonate? Is it useful or overengineering?
2.  What modules would you want to see next?
3.  Any concerns with the interface abstraction pattern?
4.  How do you currently handle DI in your Go projects?

**Links:**

-   📦 [Main Repository](https://github.com/things-kit/things-kit)
-   📚 [Example (Basic)](https://github.com/things-kit/things-kit-example)
-   🗄️ [Example (Database)](https://github.com/things-kit/things-kit-example-db)

Drop a comment below! I read and respond to everything.

And if you found this interesting, ⭐ star the repo and follow along. Next week, I'll explain exactly how the dependency injection magic works under the hood.

___

## [](https://dev.to/noxymon/why-i-built-things-kit-a-spring-boot-alternative-for-go-3ip4?#thank-you)Thank You! 🙌

Thanks for reading this far! Building Things-Kit has been a journey of learning about Go, microservices, and developer experience.

What's your biggest pain point when building Go microservices? Let me know in the comments!

___

**Follow the series:**

-   Part 1: Why I Built This (this post)
-   Part 2: Understanding Dependency Injection in Go (coming next week)
-   Part 3: Building Your First Microservice (tutorial)
-   Part 4: The Interface Abstraction Pattern
-   Part 5: From Example to Production

See you in Part 2! 👋

___

_Built with ❤️ for the Go community_

## [](https://dev.to/noxymon/why-i-built-things-kit-a-spring-boot-alternative-for-go-3ip4?#go-golang-microservices-opensource-webdev-programming-tutorial-showdev)go #golang #microservices #opensource #webdev #programming #tutorial #showdev
