---
url: "https://dev.to/shayy/i-automated-my-entire-dev-workflow-with-ai-you-wont-believe-how-easy-it-is-45n0?context=digest"
captured_at: "2025-08-04T17:06:21+01:00"
title: "I Automated My Entire Dev Workflow with AI (You Won't Believe How Easy It Is) - DEV Community"
domain: "dev-to"
---

---
As a solo developer building [UserJot](https://userjot.com/?utm_source=devto&utm_medium=post&utm_campaign=mcp-automation-workflow), I was spending too much time on repetitive tasks. Between analyzing user feedback, doing keyword research, checking support tickets, and actually writing code, I barely had time to write code.

Then I discovered MCP (Model Context Protocol) and automated most of these tasks. Here's how you can do it too.

## [](https://dev.to/shayy/i-automated-my-entire-dev-workflow-with-ai-you-wont-believe-how-easy-it-is-45n0?context=digest#what-is-mcp)What is MCP?

MCP lets AI assistants like Claude interact with external tools and services. Instead of just chatting, Claude can:

-   Read and write files on your computer
-   Call APIs and web services
-   Run terminal commands
-   Access databases
-   Basically run any code you write for it

Think of it as building custom functions that Claude can call when needed.

## [](https://dev.to/shayy/i-automated-my-entire-dev-workflow-with-ai-you-wont-believe-how-easy-it-is-45n0?context=digest#fastmcp-makes-it-simple)FastMCP Makes It Simple

While MCP is useful, setting up servers from scratch involves boilerplate code. [FastMCP](https://github.com/punkpeye/fastmcp) simplifies this process.

Here's a basic example:  

```
<span>import</span> <span>{</span> <span>FastMCP</span> <span>}</span> <span>from</span> <span>"</span><span>fastmcp</span><span>"</span><span>;</span>
<span>import</span> <span>{</span> <span>z</span> <span>}</span> <span>from</span> <span>"</span><span>zod</span><span>"</span><span>;</span>

<span>const</span> <span>server</span> <span>=</span> <span>new</span> <span>FastMCP</span><span>({</span>
  <span>name</span><span>:</span> <span>"</span><span>My Automation Server</span><span>"</span><span>,</span>
  <span>version</span><span>:</span> <span>"</span><span>1.0.0</span><span>"</span><span>,</span>
<span>});</span>

<span>server</span><span>.</span><span>addTool</span><span>({</span>
  <span>name</span><span>:</span> <span>"</span><span>check_todos</span><span>"</span><span>,</span>
  <span>description</span><span>:</span> <span>"</span><span>Get my current todo list</span><span>"</span><span>,</span>
  <span>parameters</span><span>:</span> <span>z</span><span>.</span><span>object</span><span>({</span>
    <span>status</span><span>:</span> <span>z</span><span>.</span><span>enum</span><span>([</span><span>"</span><span>pending</span><span>"</span><span>,</span> <span>"</span><span>completed</span><span>"</span><span>,</span> <span>"</span><span>all</span><span>"</span><span>]).</span><span>default</span><span>(</span><span>"</span><span>pending</span><span>"</span><span>),</span>
  <span>}),</span>
  <span>execute</span><span>:</span> <span>async </span><span>(</span><span>args</span><span>)</span> <span>=&gt;</span> <span>{</span>
    <span>// Your logic here to fetch todos</span>
    <span>const</span> <span>todos</span> <span>=</span> <span>await</span> <span>fetchTodosFromNotion</span><span>(</span><span>args</span><span>.</span><span>status</span><span>);</span>
    <span>return</span> <span>todos</span><span>.</span><span>map</span><span>(</span><span>t</span> <span>=&gt;</span> <span>`- </span><span>${</span><span>t</span><span>.</span><span>title</span><span>}</span><span>`</span><span>).</span><span>join</span><span>(</span><span>'</span><span>\n</span><span>'</span><span>);</span>
  <span>},</span>
<span>});</span>

<span>server</span><span>.</span><span>start</span><span>({</span> <span>transportType</span><span>:</span> <span>"</span><span>stdio</span><span>"</span> <span>});</span>
```

Now Claude can check your todos when you ask it to.

## [](https://dev.to/shayy/i-automated-my-entire-dev-workflow-with-ai-you-wont-believe-how-easy-it-is-45n0?context=digest#tools-i-built)Tools I Built

Here are the MCP tools that actually saved me time:

### [](https://dev.to/shayy/i-automated-my-entire-dev-workflow-with-ai-you-wont-believe-how-easy-it-is-45n0?context=digest#1-keyword-research)1\. Keyword Research

Instead of manually checking search volumes, I created a tool that pulls data from SEO APIs:  

```
<span>server</span><span>.</span><span>addTool</span><span>({</span>
  <span>name</span><span>:</span> <span>"</span><span>keyword_research</span><span>"</span><span>,</span>
  <span>description</span><span>:</span> <span>"</span><span>Research keywords for blog topics</span><span>"</span><span>,</span>
  <span>parameters</span><span>:</span> <span>z</span><span>.</span><span>object</span><span>({</span>
    <span>topic</span><span>:</span> <span>z</span><span>.</span><span>string</span><span>(),</span>
    <span>intent</span><span>:</span> <span>z</span><span>.</span><span>enum</span><span>([</span><span>"</span><span>informational</span><span>"</span><span>,</span> <span>"</span><span>commercial</span><span>"</span><span>,</span> <span>"</span><span>transactional</span><span>"</span><span>]),</span>
  <span>}),</span>
  <span>execute</span><span>:</span> <span>async </span><span>(</span><span>args</span><span>)</span> <span>=&gt;</span> <span>{</span>
    <span>// Calls SEO APIs to get search volume, difficulty, related keywords</span>
    <span>const</span> <span>data</span> <span>=</span> <span>await</span> <span>analyzeKeywords</span><span>(</span><span>args</span><span>.</span><span>topic</span><span>,</span> <span>args</span><span>.</span><span>intent</span><span>);</span>
    <span>return</span> <span>formatKeywordReport</span><span>(</span><span>data</span><span>);</span>
  <span>},</span>
<span>});</span>
```

Now I can ask: "Claude, research keywords for 'user feedback tools'" and get data in seconds instead of 15 minutes.

### [](https://dev.to/shayy/i-automated-my-entire-dev-workflow-with-ai-you-wont-believe-how-easy-it-is-45n0?context=digest#2-support-ticket-summary)2\. Support Ticket Summary

I used to spend 30 minutes each morning going through support emails. Now I have a tool that summarizes them:  

```
<span>server</span><span>.</span><span>addTool</span><span>({</span>
  <span>name</span><span>:</span> <span>"</span><span>analyze_support</span><span>"</span><span>,</span>
  <span>description</span><span>:</span> <span>"</span><span>Analyze recent support tickets</span><span>"</span><span>,</span>
  <span>parameters</span><span>:</span> <span>z</span><span>.</span><span>object</span><span>({</span>
    <span>days</span><span>:</span> <span>z</span><span>.</span><span>number</span><span>().</span><span>default</span><span>(</span><span>7</span><span>),</span>
    <span>urgentOnly</span><span>:</span> <span>z</span><span>.</span><span>boolean</span><span>().</span><span>default</span><span>(</span><span>false</span><span>),</span>
  <span>}),</span>
  <span>execute</span><span>:</span> <span>async </span><span>(</span><span>args</span><span>)</span> <span>=&gt;</span> <span>{</span>
    <span>const</span> <span>tickets</span> <span>=</span> <span>await</span> <span>fetchSupportTickets</span><span>(</span><span>args</span><span>);</span>
    <span>return</span> <span>categorizeAndPrioritize</span><span>(</span><span>tickets</span><span>);</span>
  <span>},</span>
<span>});</span>
```

### [](https://dev.to/shayy/i-automated-my-entire-dev-workflow-with-ai-you-wont-believe-how-easy-it-is-45n0?context=digest#3-task-prioritization)3\. Task Prioritization

A simple tool that helps me figure out what to work on next:  

```
<span>server</span><span>.</span><span>addTool</span><span>({</span>
  <span>name</span><span>:</span> <span>"</span><span>smart_todos</span><span>"</span><span>,</span>
  <span>description</span><span>:</span> <span>"</span><span>Manage and prioritize my development tasks</span><span>"</span><span>,</span>
  <span>parameters</span><span>:</span> <span>z</span><span>.</span><span>object</span><span>({</span>
    <span>action</span><span>:</span> <span>z</span><span>.</span><span>enum</span><span>([</span><span>"</span><span>list</span><span>"</span><span>,</span> <span>"</span><span>add</span><span>"</span><span>,</span> <span>"</span><span>complete</span><span>"</span><span>,</span> <span>"</span><span>prioritize</span><span>"</span><span>]),</span>
    <span>task</span><span>:</span> <span>z</span><span>.</span><span>string</span><span>().</span><span>optional</span><span>(),</span>
    <span>category</span><span>:</span> <span>z</span><span>.</span><span>enum</span><span>([</span><span>"</span><span>feature</span><span>"</span><span>,</span> <span>"</span><span>bug</span><span>"</span><span>,</span> <span>"</span><span>refactor</span><span>"</span><span>,</span> <span>"</span><span>content</span><span>"</span><span>]).</span><span>optional</span><span>(),</span>
  <span>}),</span>
  <span>execute</span><span>:</span> <span>async </span><span>(</span><span>args</span><span>)</span> <span>=&gt;</span> <span>{</span>
    <span>if </span><span>(</span><span>args</span><span>.</span><span>action</span> <span>===</span> <span>"</span><span>prioritize</span><span>"</span><span>)</span> <span>{</span>
      <span>// Sorts tasks based on impact and urgency</span>
      <span>return</span> <span>await</span> <span>prioritizeTasks</span><span>();</span>
    <span>}</span>
    <span>// Handle other actions...</span>
  <span>},</span>
<span>});</span>
```

### [](https://dev.to/shayy/i-automated-my-entire-dev-workflow-with-ai-you-wont-believe-how-easy-it-is-45n0?context=digest#4-user-feedback-reader)4\. User Feedback Reader

This one connects to UserJot's API to pull feature requests:  

```
<span>server</span><span>.</span><span>addTool</span><span>({</span>
  <span>name</span><span>:</span> <span>"</span><span>top_feature_requests</span><span>"</span><span>,</span>
  <span>description</span><span>:</span> <span>"</span><span>Get the most requested features from UserJot</span><span>"</span><span>,</span>
  <span>parameters</span><span>:</span> <span>z</span><span>.</span><span>object</span><span>({</span>
    <span>limit</span><span>:</span> <span>z</span><span>.</span><span>number</span><span>().</span><span>default</span><span>(</span><span>10</span><span>),</span>
    <span>minVotes</span><span>:</span> <span>z</span><span>.</span><span>number</span><span>().</span><span>default</span><span>(</span><span>5</span><span>),</span>
  <span>}),</span>
  <span>execute</span><span>:</span> <span>async </span><span>(</span><span>args</span><span>)</span> <span>=&gt;</span> <span>{</span>
    <span>const</span> <span>feedback</span> <span>=</span> <span>await</span> <span>userJotAPI</span><span>.</span><span>getFeatureRequests</span><span>({</span>
      <span>sortBy</span><span>:</span> <span>"</span><span>votes</span><span>"</span><span>,</span>
      <span>limit</span><span>:</span> <span>args</span><span>.</span><span>limit</span><span>,</span>
      <span>threshold</span><span>:</span> <span>args</span><span>.</span><span>minVotes</span><span>,</span>
    <span>});</span>

    <span>return</span> <span>feedback</span><span>.</span><span>map</span><span>(</span><span>f</span> <span>=&gt;</span> 
      <span>`</span><span>${</span><span>f</span><span>.</span><span>title</span><span>}</span><span> (</span><span>${</span><span>f</span><span>.</span><span>votes</span><span>}</span><span> votes)\n</span><span>${</span><span>f</span><span>.</span><span>description</span><span>}</span><span>`</span>
    <span>).</span><span>join</span><span>(</span><span>'</span><span>\n\n</span><span>'</span><span>);</span>
  <span>},</span>
<span>});</span>
```

## [](https://dev.to/shayy/i-automated-my-entire-dev-workflow-with-ai-you-wont-believe-how-easy-it-is-45n0?context=digest#how-i-use-userjot-with-mcp)How I Use UserJot with MCP

[UserJot](https://userjot.com/?utm_source=devto&utm_medium=post&utm_campaign=mcp-automation-workflow) is where I collect user feedback. Here's my current workflow:

1.  Users submit feedback on my UserJot board
2.  Other users vote on what's important
3.  My MCP tool reads the top requests
4.  I use this data to decide what to build next

[![UserJot Dashboard](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fsxzr88187iq734kawa4l.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fsxzr88187iq734kawa4l.png)

We're working on native MCP support in UserJot. The goal is to make it easier to:

-   Pull feature requests directly into your coding workflow
-   Generate implementation plans based on user descriptions
-   Track which feedback has been addressed

For example, you'll be able to ask Claude: "What's the top requested feature?" and have it automatically check UserJot, then help you implement it.

## [](https://dev.to/shayy/i-automated-my-entire-dev-workflow-with-ai-you-wont-believe-how-easy-it-is-45n0?context=digest#setting-it-up)Setting It Up

1.  **Install the dependencies:**

1.  **Create your server file** (e.g., `my-automation.ts`)
    
2.  **Add it to Claude Desktop:**  
    

```
<span>   </span><span>{</span><span>
     </span><span>"mcpServers"</span><span>:</span><span> </span><span>{</span><span>
       </span><span>"my-automation"</span><span>:</span><span> </span><span>{</span><span>
         </span><span>"command"</span><span>:</span><span> </span><span>"npx"</span><span>,</span><span>
         </span><span>"args"</span><span>:</span><span> </span><span>[</span><span>"tsx"</span><span>,</span><span> </span><span>"/path/to/my-automation.ts"</span><span>]</span><span>
       </span><span>}</span><span>
     </span><span>}</span><span>
   </span><span>}</span><span>
</span>
```

1.  **Start using it**

## [](https://dev.to/shayy/i-automated-my-entire-dev-workflow-with-ai-you-wont-believe-how-easy-it-is-45n0?context=digest#actual-results)Actual Results

Since implementing these tools:

-   I save about 2 hours daily on repetitive tasks
-   I ship features faster because I spend less time on admin work
-   I respond to support tickets quicker
-   I make better decisions about what to build (based on real user data)

Each tool took about 30 minutes to build and test.

## [](https://dev.to/shayy/i-automated-my-entire-dev-workflow-with-ai-you-wont-believe-how-easy-it-is-45n0?context=digest#getting-started)Getting Started

Pick one repetitive task that annoys you. Maybe it's:

-   Checking multiple dashboards every morning
-   Formatting data for reports
-   Running the same API tests
-   Categorizing emails or tickets

Build a simple MCP tool for it. The pattern is straightforward:

1.  Find the API for the service you want to automate
2.  Wrap it in a FastMCP server
3.  Connect it to Claude
4.  Use it instead of doing the task manually

Most services you already use have APIs: Notion, Linear, Slack, GitHub, etc. Each can become an MCP tool.

## [](https://dev.to/shayy/i-automated-my-entire-dev-workflow-with-ai-you-wont-believe-how-easy-it-is-45n0?context=digest#whats-next)What's Next

The combination of AI assistants and programmable tools is changing how we work. Instead of context switching between a dozen apps, you can have Claude coordinate everything through MCP.

If you want to try this yourself, start with [FastMCP](https://github.com/punkpeye/fastmcp). And if you're looking for a better way to collect and act on user feedback, check out [UserJot](https://userjot.com/?utm_source=devto&utm_medium=post&utm_campaign=mcp-automation-workflow) - we're building tools to make the feedback-to-feature cycle much shorter.

The point isn't to replace developers. It's to spend less time on boring tasks and more time building things people actually want.
