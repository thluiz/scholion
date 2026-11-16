---
url: "https://wizardsofsmart.wordpress.com/2020/06/04/custom-site-generation-with-azure-static-web-apps"
captured_at: "2026-11-16T03:49:36+00:00"
title: "Custom Site Generation with Azure Static Web Apps"
domain: "wizardsofsmart-wordpress-com"
---

While fooling around with [Azure Static Web Apps](https://azure.microsoft.com/en-us/services/app-service/static/) — which went into [public preview](https://aka.ms/trystaticwebapps) today — I found a trick to working with any front-end build tool, not just `npm install && npm run build`. In this post, I’ll work through adding a new build step and using a [custom static site generator](https://www.staticgen.com/). To keep things interesting, I’ll use an [F#](https://fsharp.org/) script to generate the site.

Azure Static Web Apps generates and commits the [GitHub Actions](https://github.com/features/actions) configuration for your project when you create your project. After that, it’s just a standard GitHub Actions configuration, and you are able to do anything you want with it. Since it’s already been committed to source control, you can freely try out any additions you want. So long as you don’t `git push -f` and erase the original, you’ll always be able to safely return to a working configuration.

Azure Static Web Apps is intended to build your web app and deploy it, but you can also host a truly static site. Azure Static Web Apps uses a tool called [Oryx](https://github.com/Microsoft/Oryx) to infer the kind of app you are deploying and run the appropriate commands to build the application. If it cannot determine what kind of application you have pushed, it will assume it is already built (or just a plain, static site). This is great news! That means you don’t have to try to bypass anything if you want to run another tool.

To demonstrate how this works, I’ll start with a failed build. It’s the heart of TDD, after all. While setting up my new Azure Static Web App, I specified `/` as my application root. My static files are actually in `/src`. Here’s what Oryx determined:

![](https://wizardsofsmart.wordpress.com/wp-content/uploads/2020/06/image.png?w=1024)

Failed build and deployment

Taking a look at the generated GitHub Actions configuration, you can see that there’s a section explicitly marked off as “safe to edit” with comments beginning with `######` marking the boundaries.

name: Azure Static Web Apps CI/CD

on:

push:

branches:

\- master

pull\_request:

types: \[opened, synchronize, reopened, closed\]

branches:

\- master

jobs:

build\_and\_deploy\_job:

if: github.event\_name == 'push' || (github.event\_name == 'pull\_request' && github.event.action != 'closed')

runs-on: ubuntu-latest

name: Build and Deploy Job

steps:

\- uses: actions/checkout@v1

\- name: Build And Deploy

id: builddeploy

uses: Azure/static-web-apps-deploy@v0.0.1-preview

with:

azure\_static\_web\_apps\_api\_token: ${{ secrets.AZURE\_STATIC\_WEB\_APPS\_API\_TOKEN\_GENTLE\_CLIFF\_06D430810 }}

repo\_token: ${{ secrets.GITHUB\_TOKEN }} # Used for Github integrations (i.e. PR comments)

action: "upload"

\###### Repository/Build Configurations - These values can be configured to match you app requirements. ######

\# For more information regarding Static Web App workflow configurations, please visit: [https://aka.ms/swaworkflowconfig](https://aka.ms/swaworkflowconfig)

app\_location: "/" # App source code path

api\_location: "api" # Api source code path - optional

app\_artifact\_location: "" # Built app content directory - optional

\###### End of Repository/Build Configurations ######

close\_pull\_request\_job:

if: github.event\_name == 'pull\_request' && github.event.action == 'closed'

runs-on: ubuntu-latest

name: Close Pull Request Job

steps:

\- name: Close Pull Request

id: closepullrequest

uses: Azure/static-web-apps-deploy@v0.0.1-preview

with:

azure\_static\_web\_apps\_api\_token: ${{ secrets.AZURE\_STATIC\_WEB\_APPS\_API\_TOKEN\_GENTLE\_CLIFF\_06D430810 }}

action: "close"

If I change `app_location: "/"` to `app_location: "src"`, my build and deploy should succeed.

![](https://wizardsofsmart.wordpress.com/wp-content/uploads/2020/06/image-1.png?w=1024)

Successful static site deployment with no build

The site itself is nothing exciting. It’s a simple event registration form. It has an event drop-down, but it’s currently empty.

![](https://wizardsofsmart.wordpress.com/wp-content/uploads/2020/06/image-2.png?w=1000)

Deployed form with no events

In the same repository, I have a `services.csv` file that we _could_ load with a JavaScript CSV parsing library like [d3](https://d3-wiki.readthedocs.io/zh_CN/master/CSV/) or [PapaParse](https://www.papaparse.com/). However, where is the fun in doing this with JavaScript? We’re building a _static_ site, after all, and as that’s far more bleeding edge than the latest front-end JavaScript library, we’re going to populate the drop-down options with some static site generating magic!

Below is the F# script file I added to the `/src` directory to “build” my static form. It retrieves the data from the CSV and inserts it into the HTML page, writing the modified HTML and other files in the `/src` folder to the `/out` folder. I won’t go into the details in this post. If you are familiar with either F# or JavaScript, you should find this fairly readable.

#r "nuget:AngleSharp"

#r "nuget:Deedle"

open System

open System.IO

open AngleSharp

open AngleSharp.Html.Parser

open Deedle

let src = DirectoryInfo(\_\_SOURCE\_DIRECTORY\_\_)

let root = src.Parent.FullName

let dataDir = Path.Combine(root, "data")

let srcDir = src.FullName

let outDir = Path.Combine(root, "out")

// Load and parse CSV

let csvPath = Path.Combine(dataDir, "services.csv")

let df = Frame.ReadCsv(csvPath)

//df.Print()

let now = DateTime.Today

let lastSunday = now.AddDays(-(float now.DayOfWeek))

let nextSunday = lastSunday.AddDays(7.)

let services =

df.Rows |> Series.filterValues (fun row ->

let date = row.GetAs<DateTime>("Date")

lastSunday < date && date <= nextSunday)

//services.Print()

let svcs =

services |> Series.mapValues (fun row ->

let date = row.GetAs<DateTime>("Date")

let time = row.GetAs<string>("Time").Split(':')

let dt = date.AddHours(float time.\[0\]).AddMinutes(float time.\[1\])

let title = row.GetAs<string>("Title")

let lang = row.GetAs<string>("Language")

sprintf "%s %s (%s)" (dt.ToString("d")) title lang)

//svcs.Print()

// Load and parse HTML

let htmlPath = Path.Combine(srcDir, "index.html")

let context = BrowsingContext.New(Configuration.Default)

let parser = context.GetService<IHtmlParser>()

let doc = using (File.OpenRead htmlPath) parser.ParseDocument

// Set the correct form action

let form : Html.Dom.IHtmlFormElement = downcast doc.GetElementsByTagName("form").\[0\]

form.Action <- "[https://some-function-api.azurewebsites.net/&quot](https://some-function-api.azurewebsites.net/&quot);

// Add the options for the upcoming week.

let frag = doc.CreateDocumentFragment()

for key in svcs.Keys do

let opt : Html.Dom.IHtmlOptionElement = downcast doc.CreateElement("option")

opt.Value <- svcs.\[key\]

opt.TextContent <- svcs.\[key\]

frag.AppendChild(opt) |> ignore

let select = doc.GetElementsByTagName("select").\[0\]

select.AppendChild(frag) |> ignore

// Clean the out directory

if (Directory.Exists outDir) then Directory.Delete(outDir, recursive=true)

Directory.CreateDirectory outDir

// Write the result to the outDir

let outPath = Path.Combine(outDir, "index.html")

// Prettified

using (File.CreateText outPath) (fun writer -> writer.Write(doc.Prettify()))

// Minified

using (File.CreateText outPath) (fun writer -> writer.Write(doc.Minify()))

// Copy style and script

File.Copy(Path.Combine(srcDir, "style.css"), Path.Combine(outDir, "style.css"))

// Write the timestamp

let lastWriteTime = DateTimeOffset(File.GetLastWriteTime(outPath))

using (File.CreateText(Path.Combine(outDir, "timestamp"))) (fun writer -> writer.Write(lastWriteTime.ToUnixTimeMilliseconds()))

Once you add a build script and output folder, you’ll need to modify the GitHub Actions configuration again. The easy bit is specifying the output folder. You just need to change the `app_location` parameter again from `app_location: "src"` to `app_location: "out"`, or whatever you name your output folder. You may wonder whey `app_location` instead of `app_artifact_location`, and the answer is that without a build, Oryx will deploy from the `app_location`. If it detects and runs a build, it will then look in the `app_artifact_location`.

The other easy bit is adding a build step. That’s right. That’s all that’s required to use a custom static site generator. If you’ve used GitHub Actions at all, this should be fairly trivial. I added two steps to run the F# script, between the `-uses: actions/checkout@v1` and the `- name: Build And Deploy` section added by Azure Static Web Apps:

1

2

3

4

5

6

7

8

9

10

`- uses: actions/checkout@v1`

`- name: Setup .NET Core 3.1`

  `id: setupdotnet`

  `uses: actions/setup-dotnet@v1`

  `with:`

    `dotnet-version: 3.1.300`

`- name: Generate`

  `id: generate`

  `run: dotnet fsi --langversion:preview ./src/build.fsx`

`- name: Build And Deploy`

The first piece sets up .NET Core 3.1, and the second runs the F# script with `dotnet fsi --langversion:preview`. The `--langversion:preview` flag enables the use of the NuGet references in the script above, which is really convenient.

![](https://wizardsofsmart.wordpress.com/wp-content/uploads/2020/06/image-3.png?w=1016)

Successful build with F# script

The form now provides a list of events in the drop-down for the user to select.

![](https://wizardsofsmart.wordpress.com/wp-content/uploads/2020/06/image-4.png?w=942)

Form with generated event list

Azure Static Web Apps does not yet support every static site generator and likely never will. However, the platform can certainly be used by any of them, as long as you are willing to make a few tweaks to the GitHub Actions configuration. Trust me when I say that this is still preferable to the alternative of setting up all the pieces separately. (I will likely do a follow-up post on that topic, as well.)

I hope you enjoyed this little jaunt into custom static site generation with Azure Static Web Apps. Feel free to try it for yourself. You can find the source for this post [here](https://github.com/panesofglass/fsharp-site-generator/). Leave a comment if you do try this or find any other interesting tricks to using Azure Static Web Apps. Happy generating!
