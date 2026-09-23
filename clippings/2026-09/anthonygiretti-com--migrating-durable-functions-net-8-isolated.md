---
url: "https://anthonygiretti.com/2024/12/05/from-net-6-to-net-8-my-migration-experience-migrating-durable-functions-net-8-isolated/"
captured_at: "2026-09-23T17:40:34+01:00"
title: "From .NET 6 to .NET 8, my migration experience: Migrating Durable Functions .NET 8 isolated – Anthony Giretti's .NET blog"
domain: "anthonygiretti-com"
---

.NET
Azure
C#
From .NET 6 to .NET 8, my migration experience: Migrating Durable Functions .NET 8 isolated
2024-12-05 by anthonygiretti
Introduction

We recently started migrating our applications from .NET 6 to .NET 8. The migration was quite simple for all Functions that were not Durable. Durable Functions on .NET 8 isolated were often difficult. In this post I will show you all the scenarios we encountered in our Functions. If I can save you from having headaches during your migration project in 2025 I will be very happy! In this post I will show you step by step how to migrate your function!

Common changes

Before going into the details of Durable Functions we will start with the generalities associated with Azure Functions. We will see in this section the changes to be made to your NuGet packages, csproj file, your Program.cs startup file.

CsProj file

In your CsProj file, ensure that you are turning your function to .NET 8, in the v4 version and with that output type set to "Exe", which are mandatory to run to Function to .NET 8 isolated (you can set it to .NET 9 as well).

Your PropertyGroup section should look like this:

	<PropertyGroup>
	  <TargetFramework>net8.0</TargetFramework>
	  <AzureFunctionsVersion>v4</AzureFunctionsVersion>
	   <OutputType>Exe</OutputType>
	</PropertyGroup>
view raw
csproj hosted with ❤ by GitHub

If your functions is crashing and says "Function already exists":

You must add in your csproj the following tag in your csproj to remove that error:

<FunctionsEnableWorkerIndexing>False</FunctionsEnableWorkerIndexing>

Nuget packages

Your project will need a ton of changes as follows:

1- Whatever the type of the function, any Nuget packages that contain "WebJobs" must be replaced as follow: From Microsoft.Azure.WebJobs.{Feature} To Microsoft.Azure.Functions.Worker.{Feature}, example:

Microsoft.Azure.WebJobs.Extensions.EventGrid becomes Microsoft.Azure.Functions.Worker.Extensions.EventGrid

2- Whatever the type of the function the following packages must be added with the Isolated mode:

Microsoft.Azure.Functions.Worker.Sdk
Microsoft.Azure.Functions.Extensions
Microsoft.Azure.Functions.Worker

You can now remove this following package which was necessary with the in-process model. It's been replaced by the Microsoft.Azure.Functions.Worker.Sdk package for isolated model.

3- If you are using Application Insights you'll need both packages:

Microsoft.ApplicationInsights.WorkerService
Microsoft.Azure.Functions.Worker.ApplicationInsights

4- I strongly suggest you to enable the ASP.NET Core Integration with the following package:

Microsoft.Azure.Functions.Worker.Extensions.Http.AspNetCore

If you want more explanations about it, you can check my previous post: ASP.NET Core: Using the ASP.NET Core integration on Azure functions – Anthony Giretti's .NET blog

local.settings.json file

To run Isolated functions on Visual Studio, you'll need to turn the FUNCTIONS_WORKER_RUNTIME from dotnet to dotnet-isolated as follows:

	{
	  "IsEncrypted": false,
	  "Values": {
	    "AzureWebJobsStorage": "UseDevelopmentStorage=true",
	    "FUNCTIONS_WORKER_RUNTIME": "dotnet-isolated",
	  }
	}
view raw
local.appsettings.json hosted with ❤ by GitHub

Once you deploy it on Azure, don't forget to update the environment variable as follows:

Program.cs file

If you ahven't done it already, you can remove your Sartup.cs file and place everything in the new Program.cs file. The following code snippets enable the ASP.NET Core Integration and Application insights. At the end of the pipeline, you'll have to configure logging. The later has an issue with custom logging especially with custom LogInformation and the code snippet below shows you how to overcome that:

	using Microsoft.Azure.Functions.Worker;
	using Microsoft.Extensions.DependencyInjection;
	using Microsoft.Extensions.Hosting;
	using Microsoft.Extensions.Logging;
	

	var host = new HostBuilder()
	        .ConfigureServices((context, services) =>
	        {
	            services.AddApplicationInsightsTelemetryWorkerService();
	            services.ConfigureFunctionsApplicationInsights();
	        })
	        .ConfigureFunctionsWebApplication(app =>
	        {
	        })
	        // Must be set at the end of the chain
	        .ConfigureLogging(logging =>
	        {
	            logging.Services.Configure<LoggerFilterOptions>(options =>
	            {
	                LoggerFilterRule defaultRule = options.Rules.FirstOrDefault(rule => rule.ProviderName
	                    == "Microsoft.Extensions.Logging.ApplicationInsights.ApplicationInsightsLoggerProvider");
	                if (defaultRule is not null)
	                {
	                    options.Rules.Remove(defaultRule);
	                }
	            });
	        })
	        .Build();
	host.Run();
view raw
Program.cs hosted with ❤ by GitHub

Here is the explanation of the issue encountered with some logs: https://github.com/Azure/azure-functions-dotnet-worker/issues/2059

If you are using AppConfiguration, you can follows the steps on my previous post here: From .NET 6 to .NET 8+,my migration experience:Using Azure AppConfiguration in Azure Functions on .NET8+ isolated – Anthony Giretti's .NET blog

Changes on ActivityTrigger

Activities undergo some changes. First, like all functions, the key name FunctionName changes to Function. Then the parameter of type IDurableActivityContext disappears in favour of the input of type that you will have specified with the function GetInput<T>(). This function is no longer necessary because the type T is, as I told you, passed as a parameter. The ActivityTrigger attribute remains unchanged. Namespaces must be adjusted, by removing all that contains "WebJob" and by adding Microsoft.Azure.Functions.Worker instead. The code below shows the code in .NET 6 in-process:

	[FunctionName(nameof(EntityInformationEmailActivity))]
	public async Task Run([ActivityTrigger] IDurableActivityContext context)
	{
	    var entitynotification = context.GetInput<EntityInformationRequestNotification>();
	    // ...
	}
view raw
EntityInformationEmailActivity.cs hosted with ❤ by GitHub

On .NET 8+ isolated the same activity gives the following:

	using Microsoft.Azure.Functions.Worker;
	

	// ... Constructor, functions...
	

	[Function(nameof(EntityInformationEmailActivity))]
	public async Task Run([ActivityTrigger] EntityInformationRequestNotification entitynotification)
	{
	    // ...
	}
view raw
EntityInformationEmailActivity.cs hosted with ❤ by GitHub

If you activity does not use any input, you have to pass, as a parameter, the FunctionContext object instead as follows:

	using Microsoft.Azure.Functions.Worker;
	

	// ... Constructor, functions...
	

	[Function(nameof(EntityInformationEmailActivity))]
	public async Task Run([ActivityTrigger] FunctionContext context)
	{
	    // ...
	}
view raw
EntityInformationEmailActivity.cs hosted with ❤ by GitHub
Changes on EntityTrigger

Here again, there are some changes. Namespaces must be adjusted by removing all containing "WebJob" and adding Microsoft.Azure.Functions.Worker instead. The EntityTrigger attribute remains unchanged while the IDurableEntityContext parameter is being replaced by TaskEntityDispatcher. The code below shows the code in .NET 6 in-process:

	[FunctionName(nameof(EntityInformationExportProcessState))]
	public static Task Run([EntityTrigger] IDurableEntityContext context)
	{
	    return context.DispatchAsync<EntityInformationExportProcessState>();
	}
view raw
EntityInformationExportProcessState.cs hosted with ❤ by GitHub

It gives the following on .NET 8+ isolated:

	using Microsoft.Azure.Functions.Worker;
	 
	[Function(nameof(EntityInformationExportProcessState))]
	public static Task Run([EntityTrigger] TaskEntityDispatcher dispatcher)
	{
	    return dispatcher.DispatchAsync<EntityInformationExportProcessState>();
	}
view raw
EntityInformationExportProcessState.cs hosted with ❤ by GitHub
Changes on OrchestrationTrigger

OrchestrationTrigger are the most challenging part of the migration. I'll show you an example of OrchestionTrigger I had to migrate. Many aspects have changed there, such as Entity locking, Activity invocations and its Retry Policy and finally, the function Output.

The example below shows an OrchestrationTrigger with .NET 6 in-process, I'm voluntarily missing some business logic in order to focus only on the changes required on .NET 8+ isolated:

	[FunctionName(nameof(ExportOrchestrator))]
	public async Task RunOrchestrator([OrchestrationTrigger] IDurableOrchestrationContext context, ILogger log)
	{
	    try
	    {
	        // Handling business logic
	        // ...
	        
	        var message = context.GetInput<ExportRequestMessage>();   
	        var entityId = new EntityId(nameof(ExportProcessState), message.EntityKey);
	

	        // Handling business logic
	        // ...
	            
	        using (await context.LockAsync(entityId))
	        {
	            // Define activity retry policy            
	            var retryConfig = new retryConfig(); // Gettign default config
	            var retryOptions = new RetryOptions(
	                firstRetryInterval: retryConfig.FirstRetryInterval,
	                maxNumberOfAttempts: retryConfig.MaxNumberOfAttempts)
	            {
	                BackoffCoefficient = retryConfig.BackoffCoefficient,
	                MaxRetryInterval = retryConfig.MaxRetryInterval,
	                RetryTimeout = retryConfig.RetryTimeout
	            };
	            
	            var report = await context.CallActivityWithRetryAsync<ReportParameters>(nameof(StorageActivity), retryOptions, new Parameters());
	            
	            // Handling business logic
	            // ...
	        
	        }
	        context.SetOutput("Task Completed}");
	    }
	    catch (Exception ex)
	    {
	        Error handling
	        // ...
	

	        context.SetCustomStatus($"Exception details: {ex.Message}");
	        context.SetOutput($"Failure");
	    }
	}
view raw
ExportOrchextrator.cs hosted with ❤ by GitHub

The .NET 8+ isolated gives the following:

	[Function(nameof(ExportOrchestrator))]
	public async Task<string> RunOrchestrator([OrchestrationTrigger] TaskOrchestrationContext context)
	{
	    try
	    {
	        // Handling business logic
	        // ...
	        
	        var entityId = new EntityInstanceId(nameof(ExportProcessState), entityKey);
	

	        // Handling business logic
	        // ...
	            
	        await using (await context.Entities.LockEntitiesAsync(entityId))
	        {
	            // Define activity retry policy            
	            var retryConfig = new retryConfig(); // Getting default config
	            var taskOptions = TaskOptions.FromRetryPolicy(
	                  new RetryPolicy(
	                    retryConfig.MaxNumberOfAttempts,
	                    retryConfig.FirstRetryInterval,
	                    retryConfig.BackoffCoefficient,
	                    retryConfig.MaxRetryInterval,
	                    retryConfig.RetryTimeout
	                  ));
	            
	            var report = await context.CallActivityAsync<ReportParameters>(nameof(StorageActivity), new Parameters(), taskOptions);
	            
	            // Handling business logic
	            // ...
	        
	        }
	        return "Task Completed";
	    }
	    catch (Exception ex)
	    {
	        Error handling
	        // ...
	

	        context.SetCustomStatus($"Exception details: {ex.Message}");
	        return "Failure";
	    }
	}
view raw
ExportOrchestrator.cs hosted with ❤ by GitHub

Let's discuss it:

First, The interface IDurableOrchestrationContext parameters disappear, and the TaskOrchestrationContext class takes place instead. Like ActivityTrigger, the GetInput<T>() method is removed, and the T class is set as a parameter of the Orchestrator. using (await context.LockAsync(entityId)) is replaced by the await using (await context.Entities.LockEntitiesAsync(entityId)) function. The CallActivityWithRetryAsync function is removed, and the CallActivityAsync takes place instead. It will always be CallActivityAsync event if you are adding a Retry Policy or not. Note that this function is reversing the parameters (new Parameters()) and the options (taskOptions parameter). Note that the RetryOptions class is replaced by the static function TaskOptions.FromRetryPolicy() takes a RetryPolicy object as a parameter. Finally, the SetOutput function disappears and gets replaced by a string, which forces you to change the return type of the Orchestrator function from a Task to Task<string>.

Changes on DurableClient

Lastly, I'd like to show you the changes on the DurableClient. Essentially, in my experience , I only had to make two little changes. The first is IDurableOrchestrationClient parameter that is being replaced by the DurableTaskClient parameter. Then the StartNewAsync function is being replaced by the ScheduleNewOrchestrationInstanceAsync function. Here is an example of a .NET 6 in-process DurableClient:

	[FunctionName("FlowCleanupOrchestratorTimeTrigger")]
	public async Task Run([TimerTrigger("%FlowCleanupTimeTrigger%", RunOnStartup = true)] TimerInfo myTimer,
	    [DurableClient] IDurableOrchestrationClient client)
	{
	    var instanceId = Guid.NewGuid().ToString();
	

	    try
	    {
	        _logger.LogInformation($"FlowCleanupOrchestratorTimeTrigger Timer trigger function activated for instanceId: {instanceId}");
	

	        await client.StartNewAsync(nameof(FlowCleanupOrchestrator), instanceId);
	    }
	    catch (Exception ex)
	    {
	        _logger.LogError(ex, $"FlowCleanupOrchestratorTimeTrigger: queue trigger function exception for instanceId: {instanceId}. Details: {ex.Message}");
	    }
	 }
view raw
FlowCleanupTimeTrigger.cs hosted with ❤ by GitHub

Here the .NET 8+ isolated version of it:

	        [Function("FlowCleanupOrchestratorTimeTrigger")]
	        public async Task Run([TimerTrigger("%FlowCleanupTimeTrigger%", RunOnStartup = true)] TimerInfo myTimer,
	            [DurableClient] DurableTaskClient client)
	        {
	            var instanceId = Guid.NewGuid().ToString();
	

	            try
	            {
	                _logger.LogInformation($"FlowCleanupOrchestratorTimeTrigger Timer trigger function activated for instanceId: {instanceId}");
	

	                await client.ScheduleNewOrchestrationInstanceAsync(nameof(FlowCleanupOrchestrator), new StartOrchestrationOptions(InstanceId: instanceId));
	            }
	            catch (Exception ex)
	            {
	                _logger.LogError(ex, $"FlowCleanupOrchestratorTimeTrigger: queue trigger function exception for instanceId: {instanceId}. Details: {ex.Message}");
	            }
	        }
view raw
FlowCleanupOrchestrator.cs hosted with ❤ by GitHub
Conclusion

This migration gave me a little more work than the other Azure functions to be honest. I wanted to share my migration experience with you because I had a hard time gathering all the Microsoft documentation, the latter being succinct, I had to rack my brains. I hope that, thanks to this tutorial you will be able to start 2025 without a nervous breakdown or hair pulling!
Finally, I wish you a happy and joyful end of year!

Like this:
Loading...
Related posts

From .NET 6 to .NET 8+,my migration experience:Using Azure AppConfiguration in Azure Functions on .NET8+ isolated

From .NET 6 to .NET 8,my migration experience:Fixing missing x-forwarded headers in .NET 8 isolated Azure Functions

From .NET 6 to .NET 8, my migration experience: Using OpenApi on Azure Function on .NET 8 isolated
