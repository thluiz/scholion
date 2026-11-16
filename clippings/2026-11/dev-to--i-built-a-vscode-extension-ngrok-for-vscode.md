---
url: "https://dev.to/philnash/i-built-a-vscode-extension-ngrok-for-vscode-29f7"
captured_at: "2026-11-16T19:39:20+00:00"
title: "I built a VSCode extension: ngrok for VSCode"
domain: "dev-to"
---

[![Cover image for I built a VSCode extension: ngrok for VSCode](https://media2.dev.to/dynamic/image/width=1000,height=420,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fphilna.sh%2Fassets%2Fposts%2Fngrok-for-vscode%2Fnfv-header-df3d9b0d8074f44a8a9af698c36678da177715951ee49697bc8b8347ae9cd15a.png)](https://media2.dev.to/dynamic/image/width=1000,height=420,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fphilna.sh%2Fassets%2Fposts%2Fngrok-for-vscode%2Fnfv-header-df3d9b0d8074f44a8a9af698c36678da177715951ee49697bc8b8347ae9cd15a.png)

[![Phil Nash](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F1359%2F66a50b53-0476-4228-86de-a7cfce832832.jpeg)](https://dev.to/philnash)

Over the Easter weekend, a four day weekend characterised by lockdowns all over the world, I decided to use the extra time I had at home to start a new project and learn a new skill. By the end of the weekend I was proud to release my first VSCode extension: [_ngrok for VSCode_](https://marketplace.visualstudio.com/items?itemName=philnash.ngrok-for-vscode).

## [](#whats-that-now)What’s that now?

[ngrok](https://ngrok.com/) is a command line tool built by [Alan Shreve](https://github.com/inconshreveable) that you can use to expose your localhost server with a publicly available URL. It’s great for sharing access to an application running on your own machine, testing web applications on mobile devices or testing webhook integrations. For example, [I’m a big fan of using ngrok to test my webhooks](https://www.twilio.com/blog/2015/09/6-awesome-reasons-to-use-ngrok-when-testing-webhooks.html) when I am working with Twilio applications.

[VSCode](https://code.visualstudio.com/) is my current favourite text editor, built by Microsoft and based on JavaScript (well, [mostly TypeScript](https://github.com/microsoft/vscode)).

As I was using VSCode last week I wondered if there was an extension that made it easier to use ngrok. I had a search and found [one under development](https://github.com/WassimBenzarti/Ngrok-connect) and one [that started a web server as well as running ngrok](https://github.com/ceyhunkeklik/vscode-ngrok-client). So I decided to build the extension I wanted to see in the marketplace.

## [](#what-does-it-do)What does it do?

With version 1 of the extension you can start an ngrok tunnel with either a port number or by choosing one of your named tunnels from your [ngrok config file](https://ngrok.com/docs#config). There is one available setting, where you can set a custom path to a config file.

Once a tunnel is running you can then open [the ngrok dashboard](https://ngrok.com/docs#getting-started-inspect) or close the tunnel.

All the commands are available from the VSCode command palette.

It’s simple so far, but I wanted to keep the scope small and get it released.

[![An animation showing using the extension from the VSCode command palette.](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fphilna.sh%2Fassets%2Fposts%2Fngrok-for-vscode%2Fstart-7cd45917e640c19e37deb6f24fa97a2a21e4a382631cee3b24014d59eb6da78e.gif)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fphilna.sh%2Fassets%2Fposts%2Fngrok-for-vscode%2Fstart-7cd45917e640c19e37deb6f24fa97a2a21e4a382631cee3b24014d59eb6da78e.gif)

The code is all open source and [you can find it on GitHub](https://github.com/philnash/ngrok-for-vscode).

## [](#whats-next)What’s next?

I would love for you to try the extension out, especially if you are already an ngrok user. If it’s useful then I am looking for feedback, [bug reports and feature requests](https://github.com/philnash/ngrok-for-vscode/issues) so I can continue to improve it.

One idea I have already is to provide a [Status Bar Item](https://code.visualstudio.com/api/references/vscode-api#StatusBarItem) or [Tree View](https://code.visualstudio.com/api/extension-guides/tree-view) that can give more information on and control over currently running ngrok tunnels. I should probably work out how to write tests for the extension too.

## [](#what-do-you-think)What do you think?

I really am after feedback, so [please install _ngrok for VSCode_](https://marketplace.visualstudio.com/items?itemName=philnash.ngrok-for-vscode) and let me know what you think [on Twitter](https://twitter.com/philnash) or via a [review on the VSCode Marketplace](https://marketplace.visualstudio.com/items?itemName=philnash.ngrok-for-vscode&ssr=false#review-details).

[![Strands harness](https://media2.dev.to/dynamic/image/width=775%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Farticles%2Fhw6m8qng9z1njxbtewf9.png)](https://strandsagents.com/?trk=1c097af3-4db9-4f1f-b0c4-4ea3fa25f1c3&sc_channel=display+ads&bb=264932)

## [](#strands-harness-is-a-stateoftheart-fully-assembled-agent-harness)[Strands harness is a state-of-the-art, fully assembled agent harness.](https://strandsagents.com/?trk=1c097af3-4db9-4f1f-b0c4-4ea3fa25f1c3&sc_channel=display+ads&bb=264932)

Strands harness is a complete, production-ready agent the moment you install it. Shell, file, and web tools, plus context management, memory, sessions, and subagents, are tuned and ready. Run it as a library or from the strands CLI, on any model and any cloud. Every default is yours to change through the open-source Harness SDK.

[Get Started with Strands](https://strandsagents.com/?trk=1c097af3-4db9-4f1f-b0c4-4ea3fa25f1c3&sc_channel=display+ads&bb=264932)
