---
url: "https://fly.io/phoenix-files/setup-vscode-for-elixir-development/"
captured_at: "2022-07-28T09:33:07-03:00"
title: "Setup VSCode for Elixir Dev · Fly"
domain: "fly-io"
---

# Setup VSCode for Elixir Dev

![phoenix-files-default.jpg](fly-io--setup-vscode-for-elixir-dev-fly/1700d4e4ccd9d12746d733d61227ae5b.jpg)

Since [Elixir](https://elixir-lang.org/) and [Phoenix](https://www.phoenixframework.org/) appeared prominently in the [Stack Overflow Survey Results for 2022](https://survey.stackoverflow.co/2022/#technology-most-loved-dreaded-and-wanted), more people have been discovering the joy of Elixir and the power of LiveView. This article introduces developers to getting the popular VS Code editor up and running for productive Elixir development.

## Problem

You want to use [Microsoft's VS Code](https://code.visualstudio.com/) for [Elixir](https://elixir-lang.org/) development but there are [many extension options](https://marketplace.visualstudio.com/search?term=elixir&target=VSCode&category=All%20categories&sortBy=Relevance)! Some extensions conflict, some are old, others new, and some require extra config.

How do we setup VS Code for productive Elixir and Phoenix development?

## Solution

Let's assume you already have [Elixir](https://elixir-lang.org/install.html) and [Phoenix](https://hexdocs.pm/phoenix/installation.html) installed. We are focused on setting up your development environment using VS Code.

There are **many** extension options and some have been replaced by newer, official extensions. We'll start with the "must have" and then cover some great optional ones.

### Must Have Extensions

Let's start with the 2 absolute must-have extensions!

**[ElixirLS: Elixir support and debugger](https://marketplace.visualstudio.com/items?itemName=JakeBecker.elixir-ls)** - Elixir support with debugger, autocomplete, and more. Powered by ElixirLS.

Refer to the extension information for learning what it can do and troubleshooting steps as well. Just note that it runs a project analysis on first run which can take some time. You may hear laptop fans kick up while that's going. Wait for that to finish before expecting code completion and formatting to work.

#### Code Management Tip

ElixirLS creates an `.elixir_ls` directory in your project root. You don't want that checked in with your code so adding the directory to your `.gitignore` file is recommended.

**[Phoenix Framework](https://marketplace.visualstudio.com/items?itemName=phoenixframework.phoenix)** - Syntax highlighting support for Phoenix templates. Supports `.heex` and `~H` embedded templates as well.

View > Command Palette... > "Preferences: Open Settings (JSON)"

The [extension Github project](https://github.com/phoenixframework/vscode-phoenix) recommends the following config change in your `settings.json` file:

```
"emmet.includeLanguages":{"phoenix-heex":"html"},
```

Note: If you don't see the improvements after making the changes, try reloading the window (Command Palette > Developer: Reload Window) or restart VS Code.

### Nice to Have Extensions

With the critical pieces in place, let's add some frosting!

**[Elixir Test](https://marketplace.visualstudio.com/items?itemName=samuel-pordeus.elixir-test)** - An extension with a few commands that helps you with your Elixir tests

Make sure to check out the extension instructions page to see what it can do and especially the keyboard shortcuts for your platform.

### Optional Extensions

If you use [Tailwind CSS](https://tailwindcss.com/) for styling your web application, then you'll want to install the **[Tailwind CSS IntelliSense](https://marketplace.visualstudio.com/items?itemName=bradlc.vscode-tailwindcss)** extension that gives you helpful code completion and documentation lookups.

This config change lets it work well with Phoenix templates and even inside your embedded `~H` function components!

View > Command Palette... > "Preferences: Open Settings (JSON)"

Add the following config to your `settings.json` file:

```
"tailwindCSS.includeLanguages":{"elixir":"html","phoenix-heex":"html"},
```

## Discussion

With your development environment setup, you are ready to productively hack on some Elixir code!

If you are new to VS Code, then it may make sense to check out the official [learning resources](https://code.visualstudio.com/learn) for how to be productive with the tool.

# Fly.io ❤️ Elixir

Need a place to deploy that shiny new Phoenix app? Fly.io is a great place to deploy LiveView applications. You can be running in minutes.

[Deploy your Phoenix app today!  →](https://fly.io/docs/getting-started/elixir/)

![cta-turtle@2x.jpg](fly-io--setup-vscode-for-elixir-dev-fly/e967a8600a6f269ae7ce7dcb6c3ae1b9.jpg)

Last updated
:   Jul 21, 2022
