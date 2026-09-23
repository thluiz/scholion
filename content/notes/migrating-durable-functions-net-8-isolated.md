---
title: "Migrating Durable Functions to .NET 8 Isolated"
date: "2026-09-23T17:40:34+01:00"
category: webclip
has_commentary: false
summary: "A field guide to migrating Azure Durable Functions from .NET 6 in-process to .NET 8 isolated: project file changes, NuGet package renames, and API replacements across activities, entities, orchestrators, and clients."
tags:
  - dotnet
  - azure-functions
  - durable-functions
  - migration
sources:
  - title: "From .NET 6 to .NET 8, my migration experience: Migrating Durable Functions .NET 8 isolated"
    url: "https://anthonygiretti.com/2024/12/05/from-net-6-to-net-8-my-migration-experience-migrating-durable-functions-net-8-isolated/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/anthonygiretti-com--migrating-durable-functions-net-8-isolated.md"
    kind: repo
---

Anthony Giretti documents the migration of Azure Durable Functions from .NET 6 in-process to .NET 8 isolated, based on a real migration project. Non-Durable Functions moved easily; Durable Functions did not, and the post walks through every API that changed shape: the project file, the NuGet packages, and the four building blocks of the Durable Functions programming model (activities, entities, orchestrators, clients).

The core pattern across all four blocks is the same: WebJobs-namespaced packages and interfaces (`IDurableOrchestrationContext`, `IDurableEntityContext`, `IDurableOrchestrationClient`) give way to Worker-namespaced replacements (`TaskOrchestrationContext`, `TaskEntityDispatcher`, `DurableTaskClient`), and the generic `GetInput<T>()` call disappears in favor of typing the input directly as a function parameter.

## Fichamento

- The `.csproj` needs `TargetFramework` set to `net8.0`, `AzureFunctionsVersion` to `v4`, and `OutputType` to `Exe` for isolated mode to run at all.
- A "Function already exists" crash is fixed by adding `<FunctionsEnableWorkerIndexing>False</FunctionsEnableWorkerIndexing>` to the csproj.
- Every NuGet package under `Microsoft.Azure.WebJobs.*` gets replaced by its `Microsoft.Azure.Functions.Worker.*` equivalent; `Microsoft.Azure.Functions.Worker.Sdk`, `.Extensions`, and `.Worker` itself are required additions for isolated mode.
- `local.settings.json` needs `FUNCTIONS_WORKER_RUNTIME` changed from `dotnet` to `dotnet-isolated`.
- `Startup.cs` is replaced by a `Program.cs` built around `HostBuilder`, with Application Insights wired through `AddApplicationInsightsTelemetryWorkerService()` and `ConfigureFunctionsApplicationInsights()`; a specific logging-rule removal is needed at the end of the chain to avoid a known custom-logging issue (linked to an open Azure SDK GitHub issue).
- Activity functions: `[FunctionName]` becomes `[Function]`, `IDurableActivityContext` and its `GetInput<T>()` call disappear, and the typed input becomes the method parameter directly. An activity with no input takes a `FunctionContext` parameter instead.
- Entity functions: `IDurableEntityContext` is replaced by `TaskEntityDispatcher`, keeping the same `DispatchAsync<T>()` call.
- Orchestrator functions see the widest set of changes: `IDurableOrchestrationContext` becomes `TaskOrchestrationContext`; `context.LockAsync()` becomes `await using (await context.Entities.LockEntitiesAsync())`; `CallActivityWithRetryAsync` is replaced by a single `CallActivityAsync` overload that takes retry options via `TaskOptions.FromRetryPolicy(new RetryPolicy(...))`, with parameters and options in reversed order from the old signature; and `context.SetOutput()` is gone, replaced by changing the method's return type to `Task<string>` and returning the value directly.
- Durable clients: `IDurableOrchestrationClient` becomes `DurableTaskClient`, and `StartNewAsync()` becomes `ScheduleNewOrchestrationInstanceAsync()`.
