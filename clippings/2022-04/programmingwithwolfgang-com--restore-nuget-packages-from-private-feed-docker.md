---
url: "https://www.programmingwithwolfgang.com/restore-nuget-inside-docker/"
captured_at: "2022-04-05T18:36:34-03:00"
title: "Restore NuGet Packages from a Private Feed when building Docker Containers"
domain: "programmingwithwolfgang-com"
---

[In my last posts](https://www.programmingwithwolfgang.com/publish-internal-nuget-feed), I created a private NuGet feed and automatically uploaded a NuGet package with my Azure DevOps pipeline. Using Visual Studio to restore the NuGet package from the private feed works fine because my user has access to the feed. When I try to restore the package when building a Docker image, it will crash with a 401 Unauthorized error.

[![The Docker build failed](https://www.programmingwithwolfgang.com/assets/img/posts/2021/01/The-Docker-build-failed.jpg)](https://www.programmingwithwolfgang.com/assets/img/posts/2021/01/The-Docker-build-failed.jpg)

The Docker build failed

Today, I will show you how to create an access token for your private Azure DevOps NuGet feed and how to pass it to your Dockerfile to build Docker images.

This post is part of [“Microservice Series - From Zero to Hero”](https://www.programmingwithwolfgang.com/microservice-series-from-zero-to-hero).

## Create a Personal Access Token (PAT) in Azure DevOps[](#create-a-personal-access-token-pat-in-azure-devops)

To create a personal access token in Azure DevOps, click on user settings, and select Personal access tokens.

[![Create a Personal access tokens](https://www.programmingwithwolfgang.com/assets/img/posts/2021/01/Create-a-Personal-access-tokens.jpg)](https://www.programmingwithwolfgang.com/assets/img/posts/2021/01/Create-a-Personal-access-tokens.jpg)

Create a Personal access tokens

This opens a new flyout window. There you can enter a name, your organization, and the expiration date. If you select Custom defined as the expiration date, you can create a PAT which is valid for one year. Select custom defined scope and then select Read in the Packaging section. This allows the PAT to read the NuGet packages from the feed.

[![Configure the PAT](https://www.programmingwithwolfgang.com/assets/img/posts/2021/01/Configure-the-PAT.jpg)](https://www.programmingwithwolfgang.com/assets/img/posts/2021/01/Configure-the-PAT.jpg)

Configure the PAT

After you click Create, the new PAT is displayed. Make sure to copy it because you won’t be able to see it again after you closed the window.

[![The PAT got created](https://www.programmingwithwolfgang.com/assets/img/posts/2021/01/The-PAT-got-created.jpg)](https://www.programmingwithwolfgang.com/assets/img/posts/2021/01/The-PAT-got-created.jpg)

The PAT got created

## Pass the PAT to build the Dockerfile locally[](#pass-the-pat-to-build-the-dockerfile-locally)

You can find the code of the demo on [GitHub](https://github.com/WolfgangOfner/MicroserviceDemo).

### Add a nuget.config file[](#add-a-nugetconfig-file)

The first step to restoring the NuGet package from the private feed is to add a nuget.config file to the root folder of the CustomerApi project. This file contains the URLs for the nuget.org and private feed. Since this file gets committed to source control, I don’t add the PAT there because I want to keep it private. The file looks as follows:

<?xml version\="1.0" encoding\="utf-8"?>

<configuration\>

<packageSources\>

<clear />

<add key\="nuget.org" value\="https://api.nuget.org/v3/index.json" />

<add key\="MicroserviceDemoNugets" value\="https://wolfgangofner.pkgs.visualstudio.com/\_packaging/MicroserviceDemoNugets/nuget/v3/index.json" />

</packageSources\>

<activePackageSource\>

<add key\="All" value\="(Aggregate source)" />

</activePackageSource\>

</configuration\>

### Use the PAT in the Dockerfile[](#use-the-pat-in-the-dockerfile)

Docker supports build arguments which I will use to pass the PAT inside the Dockerfile in the CI pipeline. Locally, I don’t pass a PAT but I can set a default value. Additionally, I have to add the PAT and a username to the nuget.config to be able to access the private NuGet feed. the code looks as follows:

ARG PAT=localhost

RUN sed -i "s|</configuration>|<packageSourceCredentials><MicroserviceDemoNugets><add key=\\"Username\\" value=\\"PAT\\" /><add key=\\"ClearTextPassword\\" value=\\"${PAT}\\" /></MicroserviceDemoNugets></packageSourceCredentials></configuration>|" nuget.config

Instead of localhost, use the previously created PAT. Make sure to not commit it to your source control though. Additionally, you have to copy the previously nuget.config file inside the Docker image. You can do this with the following code:

COPY \["CustomerApi/nuget.config", ""\]

To use the nuget.config file during the restore, use the –configfile flag and provide the path to the nuget.config file.

RUN dotnet restore "CustomerApi/CustomerApi.csproj" --configfile "./nuget.config"

RUN dotnet restore "Tests/CustomerApi.Test/CustomerApi.Test.csproj" --configfile "./nuget.config"

RUN dotnet restore "Tests/CustomerApi.Service.Test/CustomerApi.Service.Test.csproj" --configfile "./nuget.config"

RUN dotnet restore "Tests/CustomerApi.Data.Test/CustomerApi.Data.Test.csproj" --configfile "./nuget.config"

You can find the finished Dockerfile on [GitHub](https://github.com/WolfgangOfner/MicroserviceDemo/blob/master/CustomerApi/CustomerApi/Dockerfile).

Run the docker build again and it will finish successfully this time.

## Pass the PAT in the Azure DevOps Pipeline[](#pass-the-pat-in-the-azure-devops-pipeline)

In the Azure DevOps pipeline, create a new secret variable for the PAT. To do that, open the pipeline and then click on Variables on the right top. Click on the + symbol and then provide a name for the variable and the value of the PAT. Make sure to enable Keep this value secret to hide the actual value from users.

[![Create a secret variable for the PAT](https://www.programmingwithwolfgang.com/assets/img/posts/2021/01/Create-a-secret-variable-for-the-PAT.jpg)](https://www.programmingwithwolfgang.com/assets/img/posts/2021/01/Create-a-secret-variable-for-the-PAT.jpg)

Create a secret variable for the PAT

Next, add the build-arg parameter to the docker build task and provide the previously created variable as PAT. The whole task looks as follows:

\- task: Docker@1

inputs:

containerregistrytype: 'Container Registry'

dockerRegistryEndpoint: 'Docker Hub'

command: 'Build an image'

dockerFile: '\*\*/CustomerApi/CustomerApi/Dockerfile'

arguments: '\--build-arg BuildId=$(Build.BuildId) --build-arg PAT=$(PatMicroserviceDemoNugetsFeed)'

imageName: '$(ImageName)'

useDefaultContext: false

buildContext: 'CustomerApi'

displayName: 'Build the Docker image'

That’s already all to restore the NuGet package from a private feed. Run the pipeline it will finish successfully.

## Conclusion[](#conclusion)

You can create a private access token (PAT) to access NuGet packages of a private NuGet feed in Azure DevOps. This token can be passed to the Dockerfile as a build argument and then inside the Dockerfile be added to the nuget.config file. This allows you to restore private NuGet packages locally and in your Azure DevOps pipeline without committing your secret PAT to source control.

Note: If you run this demo, it will work without my private feed because I uploaded the NuGet package to nuget.org.

You can find the code of the demo on [GitHub](https://github.com/WolfgangOfner/MicroserviceDemo).

This post is part of [“Microservice Series - From Zero to Hero”](https://www.programmingwithwolfgang.com/microservice-series-from-zero-to-hero).
