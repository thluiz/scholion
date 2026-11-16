---
url: "https://dev.to/get_hariharan/write-angular-code-10x-faster-gbi"
captured_at: "2026-11-16T00:29:20+00:00"
title: "Write Angular code 10x faster"
domain: "dev-to"
---

[![Hari Haran😎](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F172952%2F310ca08a-c4f8-4f43-a06d-b8d8d16a1736.jpg)](https://dev.to/get_hariharan)

In today's age speed is a thing. Speed is a necessity. In this blog i will tell you a secret to write angular code 10x faster ⏩ ⏩.

## [](#prerequisites-greyquestion)Prerequisites ❔

*   Visual Studio code
*   You should be working in Angular 😝

If you are not having VSCode, you can download it [here](https://code.visualstudio.com/) for free.

## [](#angular-amp-component-sharing-ballotboxwithcheck)Angular & Component sharing ☑️

In angular, we can have multiple reusable components. `Eg:` You can create the below list of components which are commonly used across the application and it enables sharing and faster development.

⬇️ Some of the commonly used components like ⬇️

*   Blade
*   Modal
*   Any common filters used across the application.
*   Shared components that generate Charts/ Graphs etc.

## [](#pray-how-vscode-can-help-checkeredflag)🙏 How VS-Code can help 🏁

When you are starting out on a new project or application, initially we will focus on getting the common components out first. Once we have developed the common components, we can easily keep on re-using it across the entire application.

Let's say we need `blade` on multiple areas of the application. While development instead of typing the entire `snippet`, we can make vscode to automatically insert the whole component HTML code for us.

## [](#how-to-create-snippets-informationsource)How to create snippets? ℹ️

1.  Open Visual Studio Code.
2.  Open the desired project or workspace. `[Optional]`
    
    The second step is optional because some people prefer to create snippets which applies to a particular workspace or specific project.
    
3.  Type `F1` on your keyboard and type `User Snippets`
    
    [![User Snippets](https://res.cloudinary.com/practicaldev/image/fetch/s--gg9IIxtD--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://imgur.com/download/0YfWsi9)](https://res.cloudinary.com/practicaldev/image/fetch/s--gg9IIxtD--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://imgur.com/download/0YfWsi9)
    
4.  Press `Enter` and vs code will prompt for selection of a language. Since we are developing snippets for Angular proceed to choose `HTML`
    
    [![HTML.json](https://res.cloudinary.com/practicaldev/image/fetch/s--fhmadg9R--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://imgur.com/download/pRqpVFd)](https://res.cloudinary.com/practicaldev/image/fetch/s--fhmadg9R--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://imgur.com/download/pRqpVFd)
    
5.  Once you have selected `html.json` it will open a json file, in which we are going to make some changes.
    
6.  The syntax for the `snippet.json` will be something like this  
    
    ```
    {
        "snippetName":{
            "prefix":"your-shortcut-name",
            "body":[
            // Your full HTML content to be inserted
            ]
        }
    }
    ```
    
7.  Using the help of this syntax you can insert whatever you want to inside your HTML in an efficient and fastest way.
    

**NOTE: Each line inside the `body[]` should be enclosed within `""` string notation.**

## [](#my-snippet-shortcuts)My snippet shortcuts

Here are my top snippets for creating something very quickly.

### [](#zap-blade-zap)⚡ Blade ⚡

```
"app-blade": {
        "prefix": "blade",
        "body": [
            "<app-blade>",
            " <div bladeHeader>",
            " </div>",
            " <div bladeContent>",
            " </div>",
            " <div bladeFooter>",
            " </div>",
            "</app-blade>"
        ]
    }
```

### [](#kendo-grid)Kendo Grid

```
{
    "KendoGrid": {
        "prefix": "k-grid",
        "body": [
            "<kendo-grid [data]=\"data\"",
            "            [filterable]=\"true\"",
            "            [pageSize]=\"10\"",
            "            [skip]=\"0\"",
            "            [kendoGridSelectBy]=\"'id'\"",
            "            [selectedKeys]=\"selectedKeysIndexes\"",
            "            [resizable]=\"true\"",
            "            [sortable]=\"true\">",
            "",
            "</kendo-grid>"
        ],
        "description": "KendoGrid"
    }
}
```

I have a much bigger list since I am working on an enterprise application, we have a lot of sharable components that we tend to keep re-using.

I found this highly useful and improves our workflow and the way we write code. My team found it very useful.

If you are reading this, I hope this will definitely help you as well.

Happy coding 💥💥

Thanks for reading. 🙏 🙏  
Stay tuned for more interesting stuffs 🔥🔥🔥🔥
