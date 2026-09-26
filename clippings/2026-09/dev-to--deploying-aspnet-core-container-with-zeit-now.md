---
url: "https://dev.to/schwamster/deploying-a-aspnet-core-container-with-zeit-now"
captured_at: "2026-09-27T00:29:11+01:00"
title: "Deploying a asp.net core container with Zeit \"now\""
domain: "dev-to"
---

I just listened to a podcast [hanleminutes](https://dev.to/hanselminutes/deployment-made-easy-with-zeit) about "now" from Zeit. The promise is, that you create new folder with an node.js app, a static website or any app that you can containerize with docker. You then just type "now" in the shell and your app gets deployed.

You can find the related code in this [repo](https://github.com/schwamster/aspnetcore-docker-now). If you would like to find out more about Asp.Net Core and docker check this [tutorial](https://dev.to/schwamster/docker-tutorial-with-for-aspnet-core) out.

This sounds nice. So I gave it a try. Here is a short write up of what I did.

## [](#what-you-will-need)What you will need

*   [dotnet core cli](https://www.microsoft.com/net/core)
*   [node.js](https://nodejs.org/)

## [](#creating-the-project)Creating the project

In the commandline of your choice run the following:

```
mkdir aspnetcore-now
cd ./aspnetcore-now
dotnet new webapi
dotnet restore
```

We now have a sample web api. We can test if everything works locally by running:

```
dotnet run
```

Now point a browser to [http://localhost:5000/api/values](http://localhost:5000/api/values) and you should see a sample response like this:

```
["value1","value2"]
```

## [](#add-a-dockerfile)Add a Dockerfile

```
FROM microsoft/aspnetcore-build
ENV ASPNETCORE_URLS=http://+:80
EXPOSE 80
COPY . /opt/app
WORKDIR /opt/app
RUN dotnet restore
CMD dotnet run
```

Also add a .dockerignore file to your project, so bin and obj are not part of your build context:

```
bin
obj
```

This is a pretty straight forward dockerfile. We copy our sources to the container, expose port 80, run dotnet restore to fetch the dependencies and finally set the default command to dotnet run to execute our application.  
Yes, we are using aspnetcore-build as an image and not an optimized runtime image. The deployment will take longer, but firstly it is easier for the purpose of this article and secondly it helps work around some restrictions with the free OSS plan of now. I wanted everybody to be able to give this a try without having to use their credit card. But one of the restrictions that I quite frankly don't really understand, is that an individual file that is part of your container build context ( in this case only the very small source files), cannot be larger than 1 MB if you run in the free plan. If you build/publish your dotnet core project on your local machine or you use the build image to compile your app you will see that some files in the output are larger than 1 MB. So copying the compiled app into the runtime image (microsoft/aspnetcore) will not work, since now will then complain with the following errors:

[![](https://res.cloudinary.com/practicaldev/image/fetch/s--JB5HYVE3--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://thepracticaldev.s3.amazonaws.com/i/ln0uxvo4u6ei4dj83d51.png)](https://res.cloudinary.com/practicaldev/image/fetch/s--JB5HYVE3--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://thepracticaldev.s3.amazonaws.com/i/ln0uxvo4u6ei4dj83d51.png)

There are 3 ways to work around the problem (maybe more):

### [](#use-the-build-image)Use the build image

Use the build image instead like we do it in the article. This is creating a much lager image though. I cannot really see the benefit for Zeit forcing me to do this. A maximum total image size or a maximum total build context would have made more sense in my eyes. Every tech stack is different, in some there are fewer larger in others there is a insane amount of very small files. Zeit should not drive away devs of stacks they did not have on their radar... Of course I also might be misunderstanding something and this restriction makes perfect sense.

### [](#remove-the-large-files)Remove the large files

The offending files (refs/Microsoft.CodeAnalysis\*) are actually not needed at runtime for this project - add the following to your csproj

[![](https://res.cloudinary.com/practicaldev/image/fetch/s--dKxwn9Lk--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://thepracticaldev.s3.amazonaws.com/i/slefly8fj56xpl54r4yy.png)](https://res.cloudinary.com/practicaldev/image/fetch/s--dKxwn9Lk--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://thepracticaldev.s3.amazonaws.com/i/slefly8fj56xpl54r4yy.png)

### [](#use-a-registry)Use a registry

Another way to work around this would be to build the image however you like, push it to e.g. hub.docker.com and then just "now" a simplified dockerfile:

```
FROM myusername/myapp
ENV ASPNETCORE_URLS=http://+:80
EXPOSE 80
CMD ["dotnet", "myapp.dll"]
```

This works fine but it kind of takes the fun away. The thing I really like about "now" is, that i don't have to worry about a build pipeline.

Back to the original plan. We just use the build-image, that includes runtime and sdk as stated in the first dockerfile above.

## [](#install-now)Install now

There are different ways to install now as described [https://zeit.co/docs/getting-started/installing-now](https://dev.to/schwamster/here).

Here is how you can do it with npm:

```
npm install -g now
```

## [](#deploy)Deploy

We are now ready to deploy our application. All you need to do is run:

```
now
```

Follow the instructions. If this is the first time you run now, you will have to register with your email address.

[![](https://res.cloudinary.com/practicaldev/image/fetch/s--XffWQXuX--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://thepracticaldev.s3.amazonaws.com/i/41hpuiydiiifwmopy393.png)](https://res.cloudinary.com/practicaldev/image/fetch/s--XffWQXuX--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://thepracticaldev.s3.amazonaws.com/i/41hpuiydiiifwmopy393.png)

In the beginning of the output you will find a url now creates for you.  
Open that address in your browser and append /api/values. The result should be the same as running it locally.

[![](https://res.cloudinary.com/practicaldev/image/fetch/s--saKLQfVQ--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://thepracticaldev.s3.amazonaws.com/i/2qe9gozyapw0xad8cqqh.png)](https://res.cloudinary.com/practicaldev/image/fetch/s--saKLQfVQ--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://thepracticaldev.s3.amazonaws.com/i/2qe9gozyapw0xad8cqqh.png)

## [](#creating-aliases)Creating aliases

Every time we run now, we will create a new deployment with a new url. What is really helpful is to create aliases with more memorable and lasting urls or even custom domains. In this way, a new version can always be deployed side by side with the old one. Once happy with the result you can point the alias to the new deployment. Have a look at the [docs](https://zeit.co/docs) to find out more.

## [](#whats-next)Whats next?

Check out the cli to find out more about the nice features of now. Scale, Logs, Alias, DNS, Domains, Certs...

## [](#summary)Summary

Except for the file size limitation that kind of sucks I can highly recommend "now". This is just a first impression though. I will try this for one of my pet projects and see how it goes. I am especially interested in finding out how the whole "we only offer cpu fronted by web apps" limitation will hinder me, since I am kind of used to have certain parts of the application hidden away inside the cloud providers eco system, inside private subnets, protected by policies...
