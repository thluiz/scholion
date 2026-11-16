---
url: "https://dev.to/azure/use-blazor-and-c-to-host-a-static-website-in-azure-storage-b1d"
captured_at: "2026-11-16T00:29:33+00:00"
title: "Use Blazor and C# to host a static website in Azure Storage"
domain: "dev-to"
---

#### [](#creating-the-blazor-app)Creating the Blazor app

We will first create the Blazor application. I'm going to use Visual Studio 2019 to do that, but you can use Visual Studio Code, etc. To follow along with this tutorial, go ahead and download the following:

*   [Visual Studio 2019](https://visualstudio.microsoft.com/vs/?WT.mc_id=microsoft-azuredevtips-micrum) with the ASP.NET and web development workload selected as well as the Azure Development workload.
*   An Azure subscription (If you don't have an Azure subscription, create a [free account](https://azure.microsoft.com/free/?WT.mc_id=azure-azuredevtips-micrum) before you begin)

For Visual Studio Code, make sure you have the following installed:

*   [.NET Core 3.1 SDK (latest version)](https://dotnet.microsoft.com/download/dotnet-core/3.1?WT.mc_id=microsoft-azuredevtips-micrum)
*   Get the Blazor templates by executing the following command on the command line:

```
  dotnet new -i Microsoft.AspNetCore.Blazor.Templates
```

Enter fullscreen mode Exit fullscreen mode

Let's create the Blazor app:

1.  Open Visual Studio 2019
    
2.  Create a **new project**
    
    1.  Choose **Blazor App**
    2.  Give it a **name**
    3.  Choose the Blazor WebAssembly App template.
    4.  Press create

[![Alt Text](https://res.cloudinary.com/practicaldev/image/fetch/s--jp1ACdZM--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/m4d60fe5j5caxdbv4fyb.png)](https://res.cloudinary.com/practicaldev/image/fetch/s--jp1ACdZM--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/m4d60fe5j5caxdbv4fyb.png)  
(Create a new Blazor app in Visual Studio)

You should now have a Blazor application. Take a look at it in the solution explorer. It will look like this:

[![Alt Text](https://res.cloudinary.com/practicaldev/image/fetch/s--TNz2-yh---/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/zubv7zi3vg9zyg1pwvow.png)](https://res.cloudinary.com/practicaldev/image/fetch/s--TNz2-yh---/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/zubv7zi3vg9zyg1pwvow.png)  
(The folder structure of a default Blazor app)

If you open the page **Counter.razor** in the **Pages** folder, you'll see an example of how you can use Blazor to work with the UI. Cool right? You can have the UI trigger C# methods and do whatever you want, like increment an int.  

```
@page "/counter"

<h1>Counter</h1>

<p>Current count: @currentCount</p>

<button class="btn btn-primary" onclick="@IncrementCount">Click me</button>

@functions {
    int currentCount = 0;

    void IncrementCount()
    {
        currentCount++;
    }
}
```

Enter fullscreen mode Exit fullscreen mode

Run the application locally by **pressing \*\*F5**\*\*. You can also debug the C# code by putting a breakpoint in it as you are used to with ASP.NET.

#### [](#publish-the-blazor-app)Publish the Blazor app

To be able to host the Blazor app, we need to publish the files that we need to run it. That's easy in Visual Studio.

1.  **Right-click** the Blazor project and click **Publish**
2.  Choose **Folder** as the publish target
3.  Click **Publish** to publish the files
4.  Navigate to the published files. Navigate to the **dist** folder. We need the contents of that folder to run the website. It should look like this:

```
C:\Users\mbcrump\source\repos\BlazorApp3\BlazorApp3\bin\Release\netstandard2.1\publish\BlazorApp3\dist>tree
Folder PATH listing
Volume serial number is E6B7-F4E5
C:.
├───css
│   ├───bootstrap
│   └───open-iconic
│       └───font
│           ├───css
│           └───fonts
├───sample-data
└───_framework
    ├───wasm
    └───_bin
```

Enter fullscreen mode Exit fullscreen mode

(The result of publishing a client-side Blazor app)

#### [](#create-an-azure-storage-account-and-enable-the-static-website-feature)Create an Azure Storage Account and enable the Static website feature

Now that we have a working static web app, we can run it in Azure. We are going to run it as a [static website](https://docs.microsoft.com/azure/storage/blobs/storage-blob-static-website?WT.mc_id=docs-azuredevtips-micrum) in [Azure Storage](https://azure.microsoft.com/services/storage/?WT.mc_id=azure-azuredevtips-micrum). Running the app in there is very inexpensive, reliable and performant.

Let's start by creating a new Azure Storage account.

1.  Go to the [Azure portal](https://portal.azure.com/?WT.mc_id=azure-azuredevtips-micrum)
    
2.  Click the **Create a resource** button (the plus sign in the top left corner)
    
3.  Search for or select **Storage account**. This will open the **Create storage account** blade
    
    1.  Select an **Azure subscription**
    2.  Select or create a **Resource group**
    3.  Fill in a **name**
    4.  Make sure that the account is a **StorageV2 account**
    5.  Click **Review + create**
    6.  Click **Create**

[![Alt Text](https://res.cloudinary.com/practicaldev/image/fetch/s--U-Pjwp9q--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/iy7vhzntu94srzfmkyk2.png)](https://res.cloudinary.com/practicaldev/image/fetch/s--U-Pjwp9q--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/iy7vhzntu94srzfmkyk2.png)  
(Create a new Azure Storage account)

When the storage account is created, we can enable its **static website** feature.

1.  Go to the Azure storage account in the Azure portal
2.  Click on the **static website** menu-item
3.  Click **enable**
4.  Fill in **index.html** as the **index document name**. This will be the default file that is used when we navigate to the website
5.  Click **Save** to enable the setting

[![Alt Text](https://res.cloudinary.com/practicaldev/image/fetch/s--BBYDMHa1--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/ukuwzcm6oogzapyhq9g4.png)](https://res.cloudinary.com/practicaldev/image/fetch/s--BBYDMHa1--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/ukuwzcm6oogzapyhq9g4.png)  
(The static website feature in Azure Storage)

This Azure Storage Account can now host a static website. Notice the **Primary endpoint URL** and **copy it**. That is the URL that we use to reach the website.

#### [](#copy-the-blazor-app-into-azure-storage-and-test-the-website)Copy the Blazor app into Azure Storage and test the website

There is only one more thing to do: copy the files of the Blazor application into the Azure Storage Account. We will do that using the [Azure Storage Explorer](https://azure.microsoft.com/features/storage-explorer/?WT.mc_id=azure-azuredevtips-micrum), which is a free tool that you can use to manage Azure Storage.

1.  Open the Azure Storage Explorer and make sure that you are signed in to your Azure account
2.  Navigate to the Azure storage account that we've created
3.  Drill down into **Blob Storage**
4.  The static website feature looks for files in the **\\$web** container that is created. Click on the **\\$web** container
5.  Now open an explorer window to the **dist folder** of the published Blazor app. Select the contents of the dist folder and drag that onto the storage explorer. It will automatically upload the files into the \\$web container

[![Alt Text](https://res.cloudinary.com/practicaldev/image/fetch/s--wsuOSlvw--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/68xy5y3zyil9czmggbeq.png)](https://res.cloudinary.com/practicaldev/image/fetch/s--wsuOSlvw--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/68xy5y3zyil9czmggbeq.png)  
(Azure Storage Explorer)

That's it!

Now go to a browser and paste in the **Primary endpoint URL** of the Azure Storage static website. Here we go. A static Blazor website running in Azure!

[![Alt Text](https://res.cloudinary.com/practicaldev/image/fetch/s--GfqSB-VS--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/22cigurqo82ol1417yzu.png)](https://res.cloudinary.com/practicaldev/image/fetch/s--GfqSB-VS--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/22cigurqo82ol1417yzu.png)  
(Blazor app running in Azure Storage as a static website)

We've just deployed the app manually, but you can also automate this process by using [DevOps Pipelines](https://azure.microsoft.com/services/devops/pipelines?WT.mc_id=azure-azuredevtips-micrum). This is easy to set up and eliminates errors that we might introduce by copying things manually. You can learn how to get started with DevOps Pipelines [here](https://docs.microsoft.com/azure/devops/pipelines/create-first-pipeline?WT.mc_id=docs-azuredevtips-micrum).

#### [](#conclusion)Conclusion

Blazor is a very cool feature of ASP.NET Core that allows you to use C# instead of JavaScript, to create web UIs. Many .NET developers have dreamed about that for a long time, and now it is finally here.

And when you've created a website with Blazor, there is nothing simpler than running it as a static website in Azure Storage. It is extremely simple to use and it is inexpensive. It is also very reliable, as Azure Storage is highly available by default and makes sure that you never lose data. On top of that, your website will be very fast, because Azure Storage is very fast and Blazor is very fast. You can learn more about Blazor [here](https://dotnet.microsoft.com/apps/aspnet/web-apps/client?WT.mc_id=microsoft-azuredevtips-micrum). Thanks!

Stay connected with me on various social platforms for daily software development news.

*   [Twitter](https://twitter.com/intent/follow?screen_name=mbcrump) | [Twitch](https://twitch.tv/mbcrump) | [Instagram](https://instagram.com/mbcrump) | [YouTube](https://youtube.com/mbcrump) | [GitHub](https://github.com/mbcrump) | [Website](https://www.michaelcrump.net/)
