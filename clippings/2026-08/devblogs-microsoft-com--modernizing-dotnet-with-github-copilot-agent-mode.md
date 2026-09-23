---
url: "https://devblogs.microsoft.com/dotnet/modernizing-dotnet-with-github-copilot-agent-mode/"
captured_at: "2026-08-03T17:42:44+01:00"
title: "A step-by-step guide to modernizing .NET applications with GitHub Copilot agent mode - .NET Blog"
domain: "devblogs-microsoft-com"
---

> This blog post has been updated to reflect changes in the 18.1 release.

Upgrading an old .NET app doesn't have to mean chasing broken builds and cryptic errors. Yet for many developers, a simple version bump turns into hours of dependency conflicts and manual fixes.

Modernization isn't just about staying current. Older frameworks can introduce security risks, slow performance, and block cloud adoption. Upgrading unlocks modern APIs, better tooling, and cloud-native features like automated scaling and secure identity management.

That's where GitHub Copilot app modernization comes in. Think of it as your modernization assistant, guiding you through every step, automating the heavy lifting, and helping you move from "this might take weeks" to "done in hours."

## What you'll learn

By the end of this guide, you'll know how to:

- Analyze your .NET projects and generate a clear upgrade plan
- Apply changes automatically with GitHub Copilot
- Fix build issues and validate tests in real time
- Review a detailed summary report
- Prepare your app for Azure migration and deployment

## Before you begin

To follow along, make sure you have:

- Visual Studio 2026 (or Visual Studio 2022 version 17.14.17 and newer)
- A GitHub Copilot license
- .NET desktop development workload with GitHub Copilot and GitHub Copilot app modernization enabled

## Upgrade your .NET app

### Step 1: Open your project or solution

Start by launching Visual Studio and opening your .NET project or solution.

### Step 2: Start an agent session

You can begin in two ways:

- Right-click your project or solution in Solution Explorer and select Modernize
- Or open GitHub Copilot Chat and type @modernize followed by your request

### Step 3: Choose your path

Next, decide what you want to do:

- Upgrade to a newer .NET version for better performance and security
- Migrate to Azure to unlock cloud-native capabilities
- Explore more modernization options if you have additional goals

### Step 4: Assess and plan

Copilot evaluates your code, dependencies, and project structure, then creates an assessment.md report that includes:

- Outdated NuGet packages and recommended target versions
- Project count and upgrade complexity
- API analysis and potential breaking changes

After the assessment finishes, Copilot creates a plan.md file based on your project's current state. The plan outlines the recommended upgrade steps and is fully editable, giving you control over how the upgrade proceeds.

You can edit the plan to add context, reorder steps, or exclude specific projects before approving.

### Step 5: Apply changes and resolve errors

Once you approve the plan, Copilot begins applying the recommended upgrade steps. This stage is tracked in a tasks.md file that records each task as it runs.

Copilot will:

- Upgrade files, adjust imports, and fix syntax issues automatically
- Handle build errors in a fix-and-test loop to ensure stability
- Keep the tasks.md file updated as progress continues
- Commit major changes to Git for easy rollback if needed

If Copilot encounters a problem it can't fix automatically, it pauses and asks for your input, keeping you in control.

### Step 6: Review the results

When the upgrade is complete, Copilot provides a final summary that includes:

- A detailed report with Git commit hashes for traceability
- A Next Steps section for post-upgrade actions like updating CI/CD pipelines or running integration tests

## Make your app cloud ready

Modernization doesn't stop at upgrading your code. Making your app cloud-ready unlocks scalability, security, and operational efficiency. Here's how Copilot helps:

### Step 1: Run a cloud readiness assessment

Start by selecting Migrate to Azure from the GitHub Copilot app modernization UI.

Copilot will:

- Scan your project for framework compatibility and configuration gaps
- Identify authentication and identity issues for cloud environments
- Highlight dependency vulnerabilities that need attention

When the assessment finishes, you'll see a detailed report along with:

- A list of migration tasks in the chat window
- Criticality ratings
- Recommended actions

### Step 2: Approve and execute the migration plan

Similar to the upgrade process, Copilot creates a migration plan that will:

- Highlight dependency updates for Azure compatibility
- List configuration changes for cloud services to ensure smooth deployment
- Include security enhancements for compliance

Once you approve the plan, Copilot will:

- Update your configuration and code
- Add required Azure SDKs and authentication adapters

### Step 3: Validate and secure

After code remediation, Copilot will:

- Run automated CVE scans on all updated dependencies
- Propose safe version replacements if vulnerabilities are found
- Confirm all tests pass and build integrity is maintained

### Step 4: Deploy to Azure

Finally, deployment is fully automated. Copilot handles:

- Provisioning resources without manual scripting
- Configuring monitoring and logging for observability
- Securing identities for safe access

From code to cloud in minutes, without writing infrastructure scripts.

## Try GitHub Copilot app modernization today

Ready to modernize your .NET apps faster? Whether you're upgrading frameworks or planning a cloud migration, GitHub Copilot app modernization helps you analyze large codebases, automate fixes, and save hours of manual work.

## Author

Mika Dumont is a Product Manager on the .NET and GitHub Copilot developer experience.
