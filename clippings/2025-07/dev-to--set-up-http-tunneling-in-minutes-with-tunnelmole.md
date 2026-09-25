---
url: "https://dev.to/robbiecahill/set-up-http-tunneling-in-minutes-with-tunnelmole-56n4?context=digest"
captured_at: "2025-07-17T13:34:15+01:00"
title: "Set up HTTP Tunneling in minutes with Tunnelmole - DEV Community"
domain: "dev-to"
---

---
## [](https://dev.to/robbiecahill/set-up-http-tunneling-in-minutes-with-tunnelmole-56n4?context=digest#set-up-http-tunneling-in-minutes-with-tunnelmole)Set up HTTP Tunneling in minutes with Tunnelmole

As a developer, you often run web applications, APIs, or websites on your local machine. But what happens when you need to expose that local service to the public internet? Whether it's for testing webhooks, sharing a demo with a client, or debugging a mobile application, you need a way to make your `localhost` accessible from anywhere. This is where HTTP tunneling comes in.

This guide will demystify HTTP tunneling. We'll explore what it is, its most common applications for developers, and how it works under the hood. Most importantly, we'll walk you through a step-by-step process to set up your own HTTP tunnel in just a few minutes using Tunnelmole, a simple and powerful open-source tunneling tool.

## [](https://dev.to/robbiecahill/set-up-http-tunneling-in-minutes-with-tunnelmole-56n4?context=digest#what-is-http-tunneling)What is HTTP Tunneling?

HTTP tunneling is a technique that encapsulates HTTP (Hypertext Transfer Protocol) traffic within another protocol. Essentially, it creates a "tunnel" through which your HTTP requests and responses can travel, bypassing network restrictions like firewalls or NATs (Network Address Translators) that typically prevent direct access to a local machine from the public internet.

When you run a web server on your computer, it's usually only accessible via `localhost` or `127.0.0.1`. This address is internal to your machine. HTTP tunneling provides a publicly accessible URL (e.g., `https://random-name.tunnelmole.net`) and forwards all traffic from that public URL to your local server.

### [](https://dev.to/robbiecahill/set-up-http-tunneling-in-minutes-with-tunnelmole-56n4?context=digest#https-tunneling-vs-http-tunneling)HTTPS Tunneling vs. HTTP Tunneling

While closely related, there's a crucial difference:

-   **HTTP Tunneling**: Creates a tunnel for standard HTTP traffic - which is not secure, so don't serve up any sensitive information using this method.
-   **HTTPS Tunneling**: Does the same but for HTTPS traffic, which is secure and encrypted.

For modern web development, using an HTTPS tunnel is the standard and recommended practice. It protects data in transit and is required for many modern browser features and third-party integrations (like webhooks) that mandate secure endpoints. Tunnelmole provides free HTTPS URLs by default, ensuring your tunnels are secure right out of the box.

## [](https://dev.to/robbiecahill/set-up-http-tunneling-in-minutes-with-tunnelmole-56n4?context=digest#how-http-tunneling-works)How HTTP Tunneling Works

Understanding the flow of data makes the concept of tunneling much clearer. When you use a tool like Tunnelmole, a few key components work together to create the magic.

Heres how it all fits together:  
[![How Tunnelmole Works](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F435q80fnypa8ga1amyq2.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F435q80fnypa8ga1amyq2.png)

Let's break down the steps in the diagram:

1.  **The Request**: An internet user (or a service like a webhook provider) sends an HTTPS request to a public URL provided by the Tunnelmole service.
2.  **The Public Service**: The Tunnelmole public server receives this request. Its job is to act as the public gateway.
3.  **The Secure Tunnel**: The Tunnelmole service sends the request data through a persistent, secure connection (a tunnel) it maintains with the Tunnelmole client software running on your local machine.
4.  **The Tunnelmole Client**: The client software on your computer receives the request from the tunnel.
5.  **Forwarding to `localhost`**: The client then forwards this request to your local web application, which is listening on a specific port (e.g., `localhost:3000`).
6.  **The Local Response**: Your local application processes the request and generates a response.
7.  **The Return Journey**: The response travels back through the exact same path in reverse—from your app to the Tunnelmole client, through the secure tunnel to the Tunnelmole service, and finally back to the original internet user.

This entire process happens almost instantaneously, creating a seamless connection between the public internet and your private development environment.

## [](https://dev.to/robbiecahill/set-up-http-tunneling-in-minutes-with-tunnelmole-56n4?context=digest#common-use-cases-for-http-tunneling)Common Use Cases for HTTP Tunneling

So, why would a developer need to set up an HTTP tunnel? The applications are incredibly practical and solve many common development and testing bottlenecks.

#### [](https://dev.to/robbiecahill/set-up-http-tunneling-in-minutes-with-tunnelmole-56n4?context=digest#1-testing-and-debugging-webhooks)1\. Testing and Debugging Webhooks

This is perhaps the most popular use case. Services like Stripe, Shopify, Slack, GitHub, and Zapier use webhooks to send real-time notifications to your application. To develop and test these integrations, you need to provide a public HTTPS URL where the service can send its webhook payloads. An HTTP tunnel lets you direct these webhooks straight to your local machine, allowing you to set breakpoints in your code and debug the entire flow live, without deploying your code or relying on mock requests.

#### [](https://dev.to/robbiecahill/set-up-http-tunneling-in-minutes-with-tunnelmole-56n4?context=digest#2-sharing-workinprogress-with-stakeholders)2\. Sharing Work-in-Progress with Stakeholders

Have you ever wanted to show a new feature to a project manager, designer, or client without going through the hassle of a full deployment? With an HTTP tunnel, you can generate a public URL for your local development server and share it. They can access your work-in-progress directly from their browser, providing immediate feedback.

#### [](https://dev.to/robbiecahill/set-up-http-tunneling-in-minutes-with-tunnelmole-56n4?context=digest#3-realdevice-mobile-and-crossbrowser-testing)3\. Real-Device Mobile and Cross-Browser Testing

Browser dev tools are great for emulating mobile devices, but they are not a substitute for testing on a real device. An HTTP tunnel gives your local development server a public URL that you can access from your phone, tablet, or any other device on the internet. This allows for accurate testing of responsive designs, touch interactions, and performance on actual hardware.

#### [](https://dev.to/robbiecahill/set-up-http-tunneling-in-minutes-with-tunnelmole-56n4?context=digest#4-developing-apis-for-frontend-applications)4\. Developing APIs for Frontend Applications

When building a backend API and a separate frontend application (like a React or Vue SPA), the frontend needs to make requests to the API. During development, you can run the API locally and use an HTTP tunnel to give it a public URL. The frontend developer can then point their application to this public URL, enabling seamless, independent development and live integration testing.

#### [](https://dev.to/robbiecahill/set-up-http-tunneling-in-minutes-with-tunnelmole-56n4?context=digest#5-bypassing-network-restrictions)5\. Bypassing Network Restrictions

If you are on a restrictive corporate network or behind a Carrier-Grade NAT (CGNAT) that blocks incoming connections, setting up traditional port forwarding can be difficult or impossible. A HTTP tunnel works by establishing an _outbound_ connection from your machine to the tunnel service, which is almost never blocked. This effectively bypasses the network restrictions and makes your local service reachable.

## [](https://dev.to/robbiecahill/set-up-http-tunneling-in-minutes-with-tunnelmole-56n4?context=digest#how-to-set-up-an-http-tunnel-with-tunnelmole)How to Set Up an HTTP Tunnel with Tunnelmole

Now for the practical part. Let's set up a tunnel in just a few steps using Tunnelmole.

### [](https://dev.to/robbiecahill/set-up-http-tunneling-in-minutes-with-tunnelmole-56n4?context=digest#step-1-install-tunnelmole)Step 1: Install Tunnelmole

Tunnelmole is a lightweight, open-source tool built with Node.js. There are two primary ways to install it.

**Option A: Install with `npm` (if you have Node.js)**  
If you have Node.js (version 16.10 or later) installed, you can install Tunnelmole globally with a single command:  

```
<span>sudo </span>npm <span>install</span> <span>-g</span> tunnelmole
```

**Option B: Install a Pre-compiled Binary (No Node.js needed)**  
For Linux, macOS, or Windows Subsystem for Linux (WSL), you can install a standalone binary that includes everything needed to run.  

```
curl <span>-O</span> https://install.tunnelmole.com/xD345/install <span>&amp;&amp;</span> <span>sudo </span>bash <span>install</span>
```

For Windows, you can [download `tmole.exe`](https://tunnelmole.com/downloads/tmole.exe) and add it to your system's PATH.

### [](https://dev.to/robbiecahill/set-up-http-tunneling-in-minutes-with-tunnelmole-56n4?context=digest#step-2-start-your-local-web-service)Step 2: Start Your Local Web Service

Before creating a tunnel, you need a web service running locally. For this example, let's create a minimal Express.js server in Node.js.

If you don't have a project, create one:  

```
<span>mkdir </span>my-test-app
<span>cd </span>my-test-app
npm init <span>-y</span>
npm <span>install </span>express
```

Create a file named `app.js` and add the following code:  

```
<span>const</span> <span>express</span> <span>=</span> <span>require</span><span>(</span><span>'</span><span>express</span><span>'</span><span>);</span>
<span>const</span> <span>app</span> <span>=</span> <span>express</span><span>();</span>
<span>const</span> <span>port</span> <span>=</span> <span>3000</span><span>;</span>

<span>app</span><span>.</span><span>get</span><span>(</span><span>'</span><span>/</span><span>'</span><span>,</span> <span>(</span><span>req</span><span>,</span> <span>res</span><span>)</span> <span>=&gt;</span> <span>{</span>
  <span>res</span><span>.</span><span>send</span><span>(</span><span>'</span><span>Hello from my local server via Tunnelmole!</span><span>'</span><span>);</span>
<span>});</span>

<span>app</span><span>.</span><span>listen</span><span>(</span><span>port</span><span>,</span> <span>()</span> <span>=&gt;</span> <span>{</span>
  <span>console</span><span>.</span><span>log</span><span>(</span><span>`Example app listening at http://localhost:</span><span>${</span><span>port</span><span>}</span><span>`</span><span>);</span>
<span>});</span>
```

This simple server listens on port `3000` and responds with a message. Run it:  

You should see "Example app listening at [http://localhost:3000](http://localhost:3000/)" in your terminal.

### [](https://dev.to/robbiecahill/set-up-http-tunneling-in-minutes-with-tunnelmole-56n4?context=digest#step-3-run-tunnelmole-to-get-a-public-url)Step 3: Run Tunnelmole to Get a Public URL

With your local server running, open a **new terminal window** and run Tunnelmole, pointing it to the port your server is using (in this case, `3000`).  

Tunnelmole will start and display output similar to this:  

```
Your Tunnelmole Public URLs are below and are accessible internet wide. Always use HTTPs for the best security

https://cqcu2t-ip-49-185-26-79.tunnelmole.net ⟶ http://localhost:3000
http://cqcu2t-ip-49-185-26-79.tunnelmole.net ⟶ http://localhost:3000
```

That's it! You now have a public HTTPS URL. Anyone who visits `https://cqcu2t-ip-49-185-26-79.tunnelmole.net` (your URL will be different) will see the "Hello from my local server..." message served directly from your machine.

## [](https://dev.to/robbiecahill/set-up-http-tunneling-in-minutes-with-tunnelmole-56n4?context=digest#programmatic-usage-integrating-tunnelmole-with-nodejs)Programmatic Usage: Integrating Tunnelmole with Node.js

For more advanced workflows, you can integrate Tunnelmole directly into your Node.js projects. This is useful for automating your development environment.

First, install Tunnelmole as a local dependency:  

```
npm <span>install</span> <span>--save</span> tunnelmole
```

Next, you can import and run it from within your application code.

**ES Module `import` syntax:**  

```
<span>import</span> <span>{</span> <span>tunnelmole</span> <span>}</span> <span>from</span> <span>'</span><span>tunnelmole</span><span>'</span><span>;</span>

<span>(</span><span>async </span><span>()</span> <span>=&gt;</span> <span>{</span>
    <span>// Start Tunnelmole and get the public URL</span>
    <span>const</span> <span>url</span> <span>=</span> <span>await</span> <span>tunnelmole</span><span>({</span>
        <span>port</span><span>:</span> <span>3000</span>
    <span>});</span>
    <span>// The url will be something like: https://cqcu2t-ip-49-185-26-79.tunnelmole.net</span>
    <span>console</span><span>.</span><span>log</span><span>(</span><span>`Public URL: </span><span>${</span><span>url</span><span>}</span><span>`</span><span>);</span>
<span>})();</span>
```

**CommonJS `require` syntax:**  

```
<span>const</span> <span>{</span> <span>tunnelmole</span> <span>}</span> <span>=</span> <span>require</span><span>(</span><span>'</span><span>tunnelmole/cjs</span><span>'</span><span>);</span>

<span>(</span><span>async </span><span>()</span> <span>=&gt;</span> <span>{</span>
    <span>const</span> <span>url</span> <span>=</span> <span>await</span> <span>tunnelmole</span><span>({</span>
        <span>port</span><span>:</span> <span>3000</span>
    <span>});</span>
    <span>console</span><span>.</span><span>log</span><span>(</span><span>`Public URL: </span><span>${</span><span>url</span><span>}</span><span>`</span><span>);</span>
<span>})();</span>
```

This approach allows you to automatically start a tunnel every time you start your development server, streamlining your workflow even further.

## [](https://dev.to/robbiecahill/set-up-http-tunneling-in-minutes-with-tunnelmole-56n4?context=digest#conclusion)Conclusion

HTTP tunneling is an indispensable technique for the modern web developer. It bridges the gap between your local development environment and the public internet, solving a host of common problems related to testing, collaboration, and debugging.

With open-source tools like Tunnelmole, setting up a secure HTTPS tunnel is no longer a complex task. With a single command, you can get a stable, public URL and focus on what really matters: building great applications. Whether you're wrangling webhooks, demoing a new feature, or testing on a real phone, HTTP tunneling is a skill that will dramatically boost your productivity.
