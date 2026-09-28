---
url: "https://dzone.com/articles/create-a-minimal-web-api-with-aspnet-core-and-publ"
captured_at: "2022-07-27T12:23:14-03:00"
title: "ASP.NET, Visual Studio: Create a Minimal Web API - DZone Web Dev"
domain: "dzone-com"
---

# Create a Minimal Web API With ASP.NET Core and Publish To Azure API Management With Visual Studio

### Follow this tutorial to learn how to create a minimal Web API with .NET CLI and Visual Studio 2022 to publish it on Azure Web App and API management.

by

[Hamida Rebai](https://dzone.com/users/3106850/didourebai.html)

·

Jul. 25, 22
·
[Web Dev Zone](https://dzone.com/web-development-programming-tutorials-tools-news)
·
Tutorial

Like
[(2)](https://dzone.com/articles/create-a-minimal-web-api-with-aspnet-core-and-publ#)

Save

[Tweet](https://dzone.com/articles/create-a-minimal-web-api-with-aspnet-core-and-publ)

Join the DZone community and get the full member experience.

[Join For Free](https://dzone.com/static/registration.html)

Minimal Web API is a new approach for building APIs without all the complex structures of MVC, so, in accordance with the name "minimal," it includes the essential components needed to build HTTP APIs. All that you need is only a CSPROJ and a Program.cs.

## Benefits of Using Minimal Web API

- Less complex than before
- Easy to learn and use
- Don’t need an MVC structure: no controllers!
- Minimal code to build and compile the application, which means the application runs much faster (better performance)
- Latest improvements and functionalities of .NET 6 and C#10

## Prerequisites

- .NET 6 SDK
- Visual Studio 2022 or Visual Studio Code (we will use both of them)

We will use two methods to create our Minimal Web API.

## Method 1: Using .NET CLI

1. We will open PowerShell and check the .NET version as below.

```
dotnet --version
```

The result should be 6. In our case, we have 6.0.101:

![16073497-dotnet-version.jpg](dzone-com--create-minimal-web-api-aspnet-core-azure-api-management/8752cd9c9503fd61d40dbe07f5fb666d.jpg)

2. We will create our application:

```
dotnet new webapi -minimal -o sampleAPI
```

![16073501-create-our-application.jpg](dzone-com--create-minimal-web-api-aspnet-core-azure-api-management/89dcc0d37ce9fc8e1d8af1ff62d9d962.jpg)

3.  Open the created folder on Visual Studio Code. We will see the file structure. The folder content is smaller than the Web APIs project as before: no more startup class or controller folders. All we have is a Program.cs.

![16073507-programcs.jpg](dzone-com--create-minimal-web-api-aspnet-core-azure-api-management/da84d7e7ed480d00007c60a3c228563c.jpg)

4.  Build and run the solution inside our terminal. If you don’t have a terminal, open a new one. To do that, click on the **Terminal** Menu and then select the **New Terminal** option as shown in the below image.

![16073511-open-a-new-terminal.jpg](dzone-com--create-minimal-web-api-aspnet-core-azure-api-management/9bc46819fe9756474d0156668a7de730.jpg)

![16073514-open-editors-progamcs.jpg](dzone-com--create-minimal-web-api-aspnet-core-azure-api-management/7602b4e931ade3dfd794d0e8dbb02085.jpg)

*Build ASP.NET Core Web API Project Using Visual Studio Code Terminal*

![16073518-run-the-aspnet-core-web-api-project-using-net-core.jpg](dzone-com--create-minimal-web-api-aspnet-core-azure-api-management/6b77135077dccb31a8094c6319764b39.jpg)

*Run the ASP.NET Core Web API project using .NET Core CLI*

As you can see in the next image, our Web API Application is running on two different ports. They are as follows: https://localhost:7025 and http://localhost:5272. But if we follow the link, we get a 404 error because we have to add Swagger to the link.

![16073519-web-api-application-is-running-on-two-different-po.jpg](dzone-com--create-minimal-web-api-aspnet-core-azure-api-management/6e96ead9194f4a77fc650fe2180f4f49.jpg)

![16073520-sampleapi.jpg](dzone-com--create-minimal-web-api-aspnet-core-azure-api-management/177caa7a5f2804afc51fcc6023998413.jpg)

## Method 2: Using Visual Studio

1. We will open Visual Studio 2022, and click on "Create a new project."

![16073522-visual-studio-2022.jpg](dzone-com--create-minimal-web-api-aspnet-core-azure-api-management/08fe9860187990b04cbb1bbd5993ec86.jpg)

*Visual Studio 2022*

2. You can search for the template using "API" as a keyword at the top of the window as below and select C# as a language to more easily find the template of Web API.

![16073525-create-a-new-project.jpg](dzone-com--create-minimal-web-api-aspnet-core-azure-api-management/8ab3dbab6b1ed532a033a601f586e955.jpg)

*ASP.NET Core Web API template*

3. It is time to configure our project. We have to add the project name and the location, and we can modify the solution name.

![16073526-configure-your-new-project.jpg](dzone-com--create-minimal-web-api-aspnet-core-azure-api-management/b790018c105f94ca455bc7f26bb082b7.jpg)

4. In the next window, we have additional information. Select the new framework (.NET 6 in our case) and the authentication type, if needed. We will keep "None." We can configure HTTPs if we want to add security to our web application. If we enable Docker to use containers, we will select Docker OS (Linux or Windows). In our case, we will not enable Docker, and we need to uncheck "Use Controller." To use minimal APIs, we can enable OpenAPI support to use Swagger. I will disable it.

![16073527-use-controllers.jpg](dzone-com--create-minimal-web-api-aspnet-core-azure-api-management/1b7bb17a512d2ca06211cd69f162a3c1.jpg)

*Minimal APIs*

5. Let’s check the project structure:

![16073532-sample2api.jpg](dzone-com--create-minimal-web-api-aspnet-core-azure-api-management/a663aa127511fba999a8d56d78d84363.jpg)

6. Let us now Open Program.cs and clear everything from it so we can build a very simple API with less than 4 lines of code!

![16073537-open-programcs-and-clear-everything-from-it.jpg](dzone-com--create-minimal-web-api-aspnet-core-azure-api-management/9851564162c4338d4aee0672ce1343bf.jpg)

7. Let’s run our sample:

![16073542-run-sample.jpg](dzone-com--create-minimal-web-api-aspnet-core-azure-api-management/15d3fbceb2f585a24cd312304a3d324a.jpg)

![16073545-localhost5162.jpg](dzone-com--create-minimal-web-api-aspnet-core-azure-api-management/091b3e8a0cdea612c06aa95b3004f282.jpg)

Let’s compare this project to another using controller!

### Project Structure

![16073548-sample2api-controllers.jpg](dzone-com--create-minimal-web-api-aspnet-core-azure-api-management/3f714bf4128d4fa33c8ede183e597e35.jpg)

#### **Program.cs**

![16073552-add-services-to-the-container.jpg](dzone-com--create-minimal-web-api-aspnet-core-azure-api-management/8beb24a21eb7ebe54161b2a1893c5757.jpg)

![16073553-controller.jpg](dzone-com--create-minimal-web-api-aspnet-core-azure-api-management/1e387089daee955a7d8cbab906b56beb.jpg)

As you can see, Minimal APIs are more simple with less code!

## Publish Minimal APIs to Azure API Management with Visual Studio

1. Open the Azure portal and create a new API Management. Fill all information needed to create an API Management.

![16073554-create-api-management.jpg](dzone-com--create-minimal-web-api-aspnet-core-azure-api-management/c9d283e0cf785a369016e7f8fb71e13b.jpg)

![16073555-sample-minimial-api.jpg](dzone-com--create-minimal-web-api-aspnet-core-azure-api-management/11ee55005ef97b6701df8f40060e9d33.jpg)

*API management in Azure Portal*

2. We go back to Visual Studio 2022 to publish our web API app. Give a right-click on our Solution Explorer. After right-clicking the project, select "Publish:"

![16073556-publish.jpg](dzone-com--create-minimal-web-api-aspnet-core-azure-api-management/47b81f24622a196ce7d13c879c71e45c.jpg)

3. We will publish the API app to Azure App Service first:

- We will select "Azure" in the **Publish** window and we will click on the "Next" button:

![16073558-publish-next.jpg](dzone-com--create-minimal-web-api-aspnet-core-azure-api-management/2003f511ee2d50532ea09fdb86cc2286.jpg)

- We will select "Azure App Service (Linux)" and we will click on the "Next" button:

![16073561-publish-azure-app-service-linux.jpg](dzone-com--create-minimal-web-api-aspnet-core-azure-api-management/148d8027f9c2a5a1948aaef72bd21288.jpg)

- We will click on the "**+"** button to create a new Azure App Service, or you can select an existing Azure App Service if you have already created it before on Azure Portal or using Azure CLI. For example:

![16073564-app-service.jpg](dzone-com--create-minimal-web-api-aspnet-core-azure-api-management/70892325a93f061e334a39240ec9ca6f.jpg)

- When the **Create App Service** dialog appears, we will fill in all information needed to create a new App Service like the App Name, Resource Group, and App Service Plan entry fields. You can keep these names or change them.

![16073568-create-app-servince-linux-fields.jpg](dzone-com--create-minimal-web-api-aspnet-core-azure-api-management/e652eb9753cad05b090bd2cda583dfdf.jpg)

- We will click on "Finish" and after the creation is completed, we will click on "Publish."

![16073569-publish-app-service.jpg](dzone-com--create-minimal-web-api-aspnet-core-azure-api-management/329d8e197cf646432d06e2ee4473f13b.jpg)

If you don’t have any API Management already created, skip the next step, and click on "Finish" to publish the application.

![16073572-ready-to-publish.jpg](dzone-com--create-minimal-web-api-aspnet-core-azure-api-management/3bfe75a385e00c174f1cf1224d858152.jpg)

4. We will add our API to Azure API Management.

- Let’s open the API management Service instance created previously, and we will click on "APIs" that is on the left of the window:

![16073577-sampleminimalapi-apis.jpg](dzone-com--create-minimal-web-api-aspnet-core-azure-api-management/37e0c3b2fb6cd530888f2ebb9429a16a.jpg)

- We will delete Echo API and we will add a new API:

![16073578-all-apis-delete.jpg](dzone-com--create-minimal-web-api-aspnet-core-azure-api-management/b9c651b5ac3b9d5d63f9a520a8e75081.jpg)

![16073579-define-a-new-api.jpg](dzone-com--create-minimal-web-api-aspnet-core-azure-api-management/b9dffa18b265a5e03a980da0e49f3f4d.jpg)

- Enter the following values in the "Create an HTTP API" dialog that appears:
  - Display Name: *WeatherForecasts*
  - Name: *weatherforecasts*
  - API Url suffix: *v1*
  - Leave the web service URL field empty.

![16073580-create-an-http-api.jpg](dzone-com--create-minimal-web-api-aspnet-core-azure-api-management/ff4abe7e53b0d7f3c6dd2b6907a6a239.jpg)

This will result in no operation in our API because we have to publish the previous API to the Azure API Management.

![16073581-revision-1.jpg](dzone-com--create-minimal-web-api-aspnet-core-azure-api-management/f08d220c606c21e5b62a2cff18a02f22.jpg)

5. Publish our previous web API to Azure API Management.

- We switch back to Visual Studio to the "Publish" window, and we will select the previous published Azure App Service:

![16073582-publish-api-management.jpg](dzone-com--create-minimal-web-api-aspnet-core-azure-api-management/6b1749226920baf645264426f55a685d.jpg)

![16073583-api-management-search.jpg](dzone-com--create-minimal-web-api-aspnet-core-azure-api-management/b09752c38de81d3d73e7985a6e653985.jpg)

- Let’s switch back to API Management to check our API.

![16073584-sampleminimalapi.jpg](dzone-com--create-minimal-web-api-aspnet-core-azure-api-management/20b9cba965977550ccb10e18372c7c44.jpg)

![16073585-all-operations.jpg](dzone-com--create-minimal-web-api-aspnet-core-azure-api-management/64bd279d742dc21e54f0361869f51cb4.jpg)
