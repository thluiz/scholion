---
url: "https://msft.it/6018T5nW0"
captured_at: "2026-11-16T19:42:18+00:00"
title: "Bring your own machine to Visual Studio Online"
domain: "msft-it"
---

Today [Visual Studio Online](https://visualstudio.microsoft.com/services/visual-studio-online/) provides fully-managed, on-demand, ready-to-code development environments in the cloud, but did you know you can also register your _own machines_ and access them remotely from Visual Studio Code or our web editor? This is a great option for developers that want to cloud-connect an already configured work or home machine for anywhere access, or take advantage of the Visual Studio Online developer experience for specialized hardware we don’t currently support. We’ve made several improvements to streamline the self-hosted registration process and expand supported scenarios.

## Register your machine with our CLI (Preview)

Previously, registering your machine required you to be able to launch and interact with Visual Studio Code. If you only had SSH access or didn’t want to install and setup RDP, cloud-connecting your machine with Visual Studio Online was simply impossible. With the [preview release of our CLI](https://aka.ms/vso-cli), we’ve expanded our support to include server and headless OS scenarios across macOS, Linux, and Windows. To help get you started quickly, we’ve published our CLI to Homebrew and APT, with chocolatey coming soon.

On Windows:

Install via `Powershell` by download and executing our [script](https://aka.ms/install-vso-windows).

On macOS:

`brew install microsoft/vsonline/vso`

On Linux:

`apt install vso`

Once you have the CLI installed, run `vso start` to register your machine and select a plan created in your current region.

## Updated Registration Experience in Visual Studio Code

For those of you who prefer using Visual Studio Code to connect your environment, we updated our extension to get you started with just one click! If you don’t have any self-hosted machines, you’ll now find a “**Register self-hosted environment…**” command in the Visual Studio Online viewlet that will walk you through the steps required to register your environment. You can also still access the registration command via the command palette.

GIF of registering a self-hosted environment in Visual Studio Code, image

Register a self-hosted environment in Visual Studio Code

## Try it today!

Find out more about the CLI in our [docs](https://aka.ms/vso-self-hosted) or update your Visual Studio Online extension to try out these improvements today! If you have any feedback or issues, you can always reach us on our [GitHub page](https://aka.ms/vso-issues).

## Author

![Allison Buchholtz-Au](https://devblogs.microsoft.com/visualstudio/wp-content/uploads/sites/4/2019/02/Allison-Buchholtz-Au-150x150.jpg)

Program Manager II

Allison is a Program Manager on the Visual Studio Online team.
