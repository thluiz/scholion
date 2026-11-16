---
url: "https://antondevtips.com/blog/how-to-start-a-new-dotnet-project-in-2026"
captured_at: "2026-11-16T04:50:39+00:00"
title: "How to Start a New .NET Project in 2026"
domain: "antondevtips-com"
---

Starting a new .NET project is exciting, but it can also be overwhelming. There are so many decisions to make, and the choices you make in the first few days will affect your project for months or even years.

I have created dozens of .NET projects over the years, and today I want to share my experience with you.

In this post, we will explore the following essential steps to start a new .NET project:

1.  Set Project-Wide Standards
2.  Add Static Code Analysis Packages
3.  Enforce Coding Standards
4.  Centralize Package Management
5.  Simplify Local Development with Aspire
6.  Setup OpenTelemetry
7.  Automate Build and Testing with GitHub Actions
8.  Project Template to Start With

Let's dive in.

[Sponsor my newsletter to reach 28,000+ readers](https://antondevtips.com/sponsorship)

[Copied](#1-directorybuildprops-set-projectwide-standards)

## 1\. Directory.Build.props - Set Project-Wide Standards

Every .NET solution should start with a `Directory.Build.props` file. This file defines project-wide settings that apply to all projects in your solution.

Without this file, you end up duplicating the same configuration across multiple `.csproj` files. When you want to change a setting, you have to update every project file manually. This leads to inconsistencies and wasted time.

`Directory.Build.props` solves this problem by centralizing configuration in one place. You create this file in the same directory as your `.sln` file, and MSBuild automatically applies it to all projects in the solution.

Here is the configuration I use for every new project:

xml

`<Project>     <PropertyGroup>        <Nullable>enable</Nullable>        <ImplicitUsings>enable</ImplicitUsings>        <AnalysisLevel>latest</AnalysisLevel>        <AnalysisMode>All</AnalysisMode>        <TreatWarningsAsErrors>true</TreatWarningsAsErrors>        <CodeAnalysisTreatWarningsAsErrors>true</CodeAnalysisTreatWarningsAsErrors>        <EnforceCodeStyleInBuild>true</EnforceCodeStyleInBuild>    </PropertyGroup> </Project>`

If needed, you can also put `Directory.Build.props` on any directory level in your project hierarchy and override settings there.

**Here is what each setting does:**

**Nullable:** Enables nullable reference types, which help prevent null reference exceptions. The compiler warns you when you might be using a null value incorrectly.

**ImplicitUsings:** Automatically includes common namespace imports in every file. You do not need to write `using System;` or `using System.Linq;` anymore.

**AnalysisLevel:** Sets the code analysis level to the latest version. You get the most recent code quality checks from Microsoft.

**AnalysisMode:** Enables all code analysis rules. This gives you the most comprehensive feedback on code quality.

**TreatWarningsAsErrors:** Prevents compilation if there are any warnings. This forces you to fix issues immediately rather than letting them accumulate.

**CodeAnalysisTreatWarningsAsErrors:** Applies the same strict treatment to code analysis warnings.

**EnforceCodeStyleInBuild:** Runs code style checks during build, not just in the IDE. Your CI/CD pipeline will catch style violations.

These settings create a strong foundation for code quality. They catch issues early and enforce consistency across your entire solution.

[Copied](#2-add-static-code-analysis-packages)

## 2\. Add Static Code Analysis Packages

Code quality is something you need to care about from day 1. It's easier to follow the best coding practices than to fix them later.

For this, we can use static code analysis.

Static code analyzers examine your code without running it. They catch common mistakes, enforce coding standards, and identify potential bugs before they reach production.

The analyzers run during compilation, so you get immediate feedback in your IDE and in your CI/CD pipeline.

Add these analyzer packages to your `Directory.Build.props` file:

xml

`<Project>   <PropertyGroup>    <Nullable>enable</Nullable>    <ImplicitUsings>enable</ImplicitUsings>    <AnalysisLevel>latest</AnalysisLevel>    <AnalysisMode>All</AnalysisMode>    <TreatWarningsAsErrors>true</TreatWarningsAsErrors>    <CodeAnalysisTreatWarningsAsErrors>true</CodeAnalysisTreatWarningsAsErrors>    <EnforceCodeStyleInBuild>true</EnforceCodeStyleInBuild>  </PropertyGroup>   <ItemGroup>    <PackageReference Include="Meziantou.Analyzer" Version="2.0.257">      <IncludeAssets>runtime; build; native; contentfiles; analyzers; buildtransitive</IncludeAssets>    </PackageReference>    <PackageReference Include="SonarAnalyzer.CSharp" Version="10.16.0.128591">      <IncludeAssets>runtime; build; native; contentfiles; analyzers; buildtransitive</IncludeAssets>    </PackageReference>    <PackageReference Include="Roslynator.Analyzers" Version="4.14.1">      <IncludeAssets>runtime; build; native; contentfiles; analyzers; buildtransitive</IncludeAssets>    </PackageReference>    <PackageReference Include="xunit.analyzers" Version="1.26.0">      <IncludeAssets>runtime; build; native; contentfiles; analyzers; buildtransitive</IncludeAssets>    </PackageReference>  </ItemGroup> </Project>`

**Here is what each analyzer provides:**

**SonarAnalyzer.CSharp:** Focuses on code quality, security vulnerabilities, and code smells. It identifies complex methods, duplicated code, and potential bugs.

**Meziantou.Analyzer:** Catches performance issues, security vulnerabilities, and incorrect API usage. It has hundreds of rules covering async/await patterns, LINQ usage, string handling, and more.

**Roslynator.Analyzers:** Provides code analysis and refactoring suggestions. It helps you write cleaner, more idiomatic C# code.

**xunit.analyzers:** Ensures you write tests correctly. It catches common testing mistakes, such as missing assertions or incorrect test attributes.

The `IncludeAssets` configuration ensures that these analyzers run during compilation but do not get included in your published application.

With `TreatWarningsAsErrors` enabled, your build will fail if any analyzer finds an issue. This might seem strict, but it prevents technical debt from accumulating.

You should always strive to have zero warnings in your project. Many developers ignore warnings, but warnings often indicate real problems that will cause bugs later.

For more information about code quality best practices, check out this [article](https://antondevtips.com/blog/best-practices-for-increasing-code-quality-in-dotnet-projects).

[Copied](#3-enforce-coding-standards)

## 3\. Enforce Coding Standards

Analyzers identify issues, but you also need to configure which rules matter for your team and how strict they should be.

The `.editorconfig` file defines coding standards and specifies the severity level for each analyzer rule. You can mark rules as errors, warnings, suggestions, or turn them off completely.

Place this file in the same directory as your `.sln` file. Every developer on your team will automatically follow the same rules, regardless of which IDE they use.

Here is a basic `.editorconfig` file to get started:

ini

`root = true [*] charset = utf-8 indent_style = space indent_size = 4 insert_final_newline = true trim_trailing_whitespace = true [*.cs] # Nullable reference types dotnet_diagnostic.CS8600.severity = error dotnet_diagnostic.CS8601.severity = error dotnet_diagnostic.CS8602.severity = error dotnet_diagnostic.CS8603.severity = error dotnet_diagnostic.CS8604.severity = error # Code style rules dotnet_style_qualification_for_field = false:warning dotnet_style_qualification_for_property = false:warning dotnet_style_qualification_for_method = false:warning dotnet_style_qualification_for_event = false:warning # Naming conventions dotnet_naming_rule.interface_should_begin_with_i.severity = error dotnet_naming_rule.interface_should_begin_with_i.symbols = interface dotnet_naming_rule.interface_should_begin_with_i.style = begins_with_i dotnet_naming_symbols.interface.applicable_kinds = interface dotnet_naming_style.begins_with_i.required_prefix = I dotnet_naming_style.begins_with_i.capitalization = pascal_case # Async methods should end with Async dotnet_naming_rule.async_methods_end_in_async.severity = error dotnet_naming_rule.async_methods_end_in_async.symbols = any_async_methods dotnet_naming_rule.async_methods_end_in_async.style = end_in_async dotnet_naming_symbols.any_async_methods.applicable_kinds = method dotnet_naming_symbols.any_async_methods.applicable_accessibilities = * dotnet_naming_symbols.any_async_methods.required_modifiers = async dotnet_naming_style.end_in_async.required_suffix = Async dotnet_naming_style.end_in_async.capitalization = pascal_case`

> You can download the complete `.editorconfig` file from [my article](https://antondevtips.com/blog/best-practices-for-increasing-code-quality-in-dotnet-projects).

You can customize this file to match your team's preferences. The key is to agree on standards early and enforce them automatically.

With `.editorconfig`, code reviews become faster because developers do not need to argue about formatting or naming conventions. The tooling enforces these rules automatically.

[Copied](#4-centralize-package-management)

## 4\. Centralize Package Management

As your solution grows, managing NuGet package versions across multiple projects becomes challenging. Different projects end up using different versions of the same package, which can cause compatibility issues and make updates harder.

Central Package Management (CPM) solves this problem by managing all package versions in one place.

You need to create a `Directory.Packages.props` file that defines all package versions for your solution. Place this file in the same directory as your `.sln` file:

xml

`<Project>   <PropertyGroup>    <ManagePackageVersionsCentrally>true</ManagePackageVersionsCentrally>  </PropertyGroup>   <ItemGroup>    <!-- Web -->    <PackageVersion Include="Microsoft.AspNetCore.OpenApi" Version="10.0.0" />     <!-- Database -->    <PackageVersion Include="Microsoft.EntityFrameworkCore" Version="10.0.0" />    <PackageVersion Include="Microsoft.EntityFrameworkCore.Design" Version="10.0.0" />    <PackageVersion Include="Npgsql.EntityFrameworkCore.PostgreSQL" Version="10.0.0" />     <!-- Testing -->    <PackageVersion Include="xunit" Version="2.9.3" />    <PackageVersion Include="xunit.runner.visualstudio" Version="3.1.5" />    <PackageVersion Include="Microsoft.NET.Test.Sdk" Version="18.0.1" />     <!-- Code Analysis -->    <PackageVersion Include="Meziantou.Analyzer" Version="2.0.257" />    <PackageVersion Include="SonarAnalyzer.CSharp" Version="10.16.0.128591" />    <PackageVersion Include="Roslynator.Analyzers" Version="4.14.1" />    <PackageVersion Include="xunit.analyzers" Version="1.26.0" />  </ItemGroup> </Project>`

You need to add the `ManagePackageVersionsCentrally` property in this file to enable CPM.

With CPM enabled, your project files reference packages without specifying versions:

xml

`<ItemGroup>   <PackageReference Include="Microsoft.EntityFrameworkCore" />  <PackageReference Include="Npgsql.EntityFrameworkCore.PostgreSQL" /> </ItemGroup>`

If needed, you can override package versions in individual projects:

xml

`<ItemGroup>   <PackageReference Include="Npgsql.EntityFrameworkCore.PostgreSQL" Version="10.0.1" /> </ItemGroup>`

[Copied](#5-simplify-local-development-with-aspire)

## 5\. Simplify Local Development with Aspire

Setting up local development environments is often frustrating. Developers spend hours installing databases, configuring connection strings, and getting dependencies to work together.

Even with Docker, you still have a lot of manual setup, including volumes and configuration for each container.

.NET Aspire solves this problem by providing a consistent way to manage your application's dependencies, configuration, and deployment.

Aspire is an application framework for building observable, production-ready, cloud-native applications with .NET. It handles service discovery, configuration, health checks, and telemetry out of the box.

Starting from [version 13](https://aspire.dev/whats-new/aspire-13/), .NET Aspire was rebranded to [Aspire](https://aspire.dev/) and is now a multi-language application platform.

Aspire introduces two new project types to your solution:

*   **AppHost:** The orchestrator that defines your application's architecture and dependencies.
*   **ServiceDefaults:** Shared configuration and observability setup applied to all services.

Here is how to add Aspire to your new project:

**Step 1:** Install the Aspire project templates:

bash

`dotnet new install Aspire.ProjectTemplates`

**Step 2:** Install the Aspire CLI:

bash

`dotnet tool install --global aspire.cli`

**Step 3:** Add Aspire support to your solution through Visual Studio or Rider, or use the CLI to create a new Aspire project.

**Step 4:** Configure your dependencies in the AppHost project:

csharp

`var builder = DistributedApplication.CreateBuilder(args); var cache = builder.AddRedis("cache"); var postgres = builder.AddPostgres("postgres"); builder     .AddProject<Projects.Products_Api>("products-api");    .WithReference(cache)    .WithReference(postgres); builder.Build().Run();`

**Step 5:** Reference the connection strings in your API project:

csharp

`var postgresConnection = configuration.GetConnectionString("postgres"); var redisConnection = configuration.GetConnectionString("cache");`

Aspire automatically injects connection strings through environment variables. You do not need to configure them manually in `appsettings.json`.

With Docker integration, Aspire starts all your dependencies automatically when you run the AppHost project. PostgreSQL, Redis, and any other services run in containers, and Aspire manages their lifecycle.

The Aspire dashboard opens in your browser and shows all running services, their health status, logs, and distributed traces.

![Screenshot\_5](https://antondevtips.com/media/code_screenshots/dotnet/aspire-13/img_2.png)

**Here are the key benefits of using Aspire:**

*   **Simplified local development:** Run all your services, databases, and dependencies with a single command.
*   **Built-in observability:** OpenTelemetry integration for logs, metrics, and traces comes preconfigured.
*   **Service discovery:** Services automatically discover each other without hardcoded URLs.
*   **Configuration management:** Centralized configuration that works locally and in the cloud.
*   **Easy deployment to Docker Compose and Cloud:** Deploy your entire application stack to Docker, Azure or AWS with minimal setup.
*   **Consistent developer experience:** New team members can get the entire application running in minutes.

For a complete guide on deploying .NET applications with Aspire, read this [article](https://antondevtips.com/blog/getting-started-with-dotnet-aspire-13-building-and-deploying-an-app).

[Copied](#6-setup-opentelemetry)

## 6\. Setup OpenTelemetry

Understanding what happens inside your application is essential. OpenTelemetry provides a standardized way to collect and analyze telemetry data from your applications, giving you visibility into their behavior.

Every application has external dependencies such as databases, caches, APIs, and other services. Monitoring these dependencies is essential for understanding how your application performs and interacts with the rest of the system.

OpenTelemetry collects logs, metrics, and traces from your applications:

*   **Logs** explain what happened.
*   **Traces** reveal where and how long operations took.
*   **Metrics** show how often events occur.

When you use Aspire, OpenTelemetry is already configured for you. The ServiceDefaults project contains the observability setup:

csharp

`public static TBuilder ConfigureOpenTelemetry<TBuilder>(this TBuilder builder)     where TBuilder : IHostApplicationBuilder {     builder.Logging.AddOpenTelemetry(logging =>    {        logging.IncludeFormattedMessage = true;        logging.IncludeScopes = true;    });     builder.Services.AddOpenTelemetry()        .WithMetrics(metrics =>        {            metrics.AddAspNetCoreInstrumentation()                .AddHttpClientInstrumentation()                .AddRuntimeInstrumentation();        })        .WithTracing(tracing =>        {            tracing.AddSource(builder.Environment.ApplicationName)                .AddAspNetCoreInstrumentation()                .AddHttpClientInstrumentation();        });     builder.AddOpenTelemetryExporters();     return builder; }`

Aspire automatically configures OpenTelemetry to send logs, metrics, and traces to the Aspire dashboard. However, Aspire does not persist OpenTelemetry and Dashboard data.

In production, you need a more robust solution for storing and analyzing telemetry data. You can configure additional exporters to send data to Jaeger, Seq, Grafana, or other observability tools.

By default, OpenTelemetry instruments ASP.NET Core and HttpClient. For additional dependencies like PostgreSQL or Redis, install the instrumentation packages:

bash

`dotnet add package Npgsql.OpenTelemetry dotnet add package OpenTelemetry.Instrumentation.StackExchangeRedis`

Then register them in your ServiceDefaults:

csharp

`tracing.AddSource(builder.Environment.ApplicationName)     .AddAspNetCoreInstrumentation()    .AddHttpClientInstrumentation()    .AddNpgsql()    .AddRedisInstrumentation();`

The Aspire dashboard shows distributed traces across all your services. You can see exactly which database queries ran, how long they took, and where bottlenecks exist.

![Screenshot\_13](https://antondevtips.com/media/code_screenshots/dotnet/aspire-13/img_8.png)

Starting with observability from day one helps you understand performance characteristics early. You can identify slow queries, optimize API calls, and troubleshoot issues before they reach production.

![Screenshot\_4](https://antondevtips.com/media/code_screenshots/dotnet/opentelemetry/img_4.png)

For more information on OpenTelemetry, read this [article](https://antondevtips.com/blog/getting-started-with-open-telemetry-in-dotnet-with-jaeger-and-seq).

[Copied](#7-automate-build-and-testing-with-github-actions)

## 7\. Automate Build and Testing with GitHub Actions

Modern software development requires automated pipelines. You cannot afford to deploy manually or skip automated tests.

A good CI/CD pipeline ensures that every code change is built, tested, and deployed consistently. It catches bugs before they reach production and accelerates your delivery speed.

Without proper CI/CD pipelines, you waste time on manual tasks and increase the risk of human error.

For .NET developers using GitHub, GitHub Actions is the natural choice. It integrates seamlessly with your repository and provides everything you need to build and test .NET applications.

Create a `.github/workflows/ci.yml` file in your repository:

yaml

`name: BUILD_AND_TEST on:   push:    branches: [ "main" ]  pull_request:    branches: [ "main" ] jobs:   build:    runs-on: ubuntu-latest     strategy:      matrix:        dotnet-version: [ '10.0.x' ]     steps:      - uses: actions/checkout@v3       - name: Setup .NET        uses: actions/setup-dotnet@v3        with:          dotnet-version: ${{ matrix.dotnet-version }}       - name: Restore dependencies        run: dotnet restore       - name: Build        run: dotnet build --no-restore       - name: Test        run: dotnet test --no-build --no-restore --verbosity normal       - name: Build Docker image with Aspire        if: ${{ success() }}        run: |          dotnet tool install --global aspire.cli          aspire publish -o docker-compose-artifacts          docker compose -f docker-compose-artifacts/docker-compose.yaml build`

This pipeline runs on every push to the main branch and on every pull request. It restores dependencies, builds the solution, runs tests, and builds a Docker image using Aspire.

The Aspire CLI generates a Docker Compose file that includes all your services and their dependencies. The pipeline then builds the Docker images for deployment.

**Follow these best practices for CI/CD pipelines:**

*   **Keep pipelines fast:** Aim for under 10 minutes for CI builds.
*   **Run tests on every pull request:** Catch issues before they merge into the main branch.
*   **Store secrets securely:** Use GitHub Secrets for sensitive data like API keys and connection strings. Never commit secrets to your repository.
*   **Fail fast:** If tests fail, stop the pipeline immediately. Do not waste time building Docker images for broken code.
*   **Use caching:** Cache NuGet packages and build artifacts to speed up subsequent runs.

[Copied](#8-project-template-to-start-with)

## 8\. Project Template to Start With

Setting up a new .NET project following the above steps is not hard.

However, you need many more things to set up in your project, like:

*   Code Structure: Clean Architecture / Vertical Slices / N-Layered
*   WebApi endpoint structure
*   Authentication and Authorization.
*   ASP .NET Core Identity
*   JWT Claims and Refresh tokens
*   Logging
*   Jaeger and Seq integration
*   Result Pattern
*   Architecture Tests
*   Unit and Integration Tests

You can download my free [.NET Backend Project Template](https://antondevtips.com/templates/modular-monolith) and save weeks of development time. It is built as a Modular Monolith using industry-best practices and patterns, including Vertical Slice Architecture and Clean Architecture.

Skip all the boilerplate — start with a fully configured Modular Monolith .NET template so you can focus on delivering business value from day one. The project is ready to run in Docker with a one-click setup, including a fully configured database and external dependencies.

[Copied](#summary)

## Summary

Starting a new .NET project with the right foundation saves time and prevents technical debt.

Here are the seven essential steps for every new .NET project in 2026:

**1\. Directory.Build.props:** Set project-wide standards for nullable reference types, implicit usings, code analysis, and strict warning treatment.

**2\. Static Code Analysis Packages:** Add Meziantou.Analyzer, SonarAnalyzer.CSharp, Roslynator.Analyzers, and xunit.analyzers to catch issues during compilation.

**3\. .editorconfig:** Enforce coding standards and configure severity levels for analyzer rules.

**4\. Directory.Packages.props:** Centralize NuGet package version management across all projects in your solution.

**5\. Aspire + Docker:** Simplify local development with automatic service orchestration, configuration management, and Docker integration.

**6\. OpenTelemetry:** Get built-in observability with logs, metrics, and traces configured automatically through Aspire.

**7\. GitHub Actions:** Automate build, test, and Docker image creation with a CI/CD pipeline.

These practices will pay off quickly throughout the project's lifetime. The best time to establish quality standards is at the beginning. Start your next .NET project with these seven steps, and you will build better software faster.

Hope you find this newsletter useful. See you next time.
