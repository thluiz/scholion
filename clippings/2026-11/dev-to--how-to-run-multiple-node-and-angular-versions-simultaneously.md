---
url: "https://dev.to/patricepeartree/how-to-run-multiple-node-and-angular-versions-simultaneously-3lfj"
captured_at: "2026-11-16T01:47:37+00:00"
title: "How to run multiple Node and Angular versions simultaneously"
domain: "dev-to"
---

In my line of work as a Web Engineer, I have leaped through a decent amount of projects in a not so big amount of time. Not only that, but all of these projects had at least one [Node](https://nodejs.org/) based component and a big part of them also used [Angular](https://angular.io/) as their Frontend framework. So I eventually came to a point where I needed to actively work on my current project but be able to quickly switch back to any of the other projects.

I must admit that the first time this switch was needed, I naively downgraded both Node and [Angular CLI](https://cli.angular.io/)… Only to then upgrade them again when I went back to working on my current project. Not only is this a time-wasting process, it is susceptible to errors from missing information. An Angular project's CLI version is in the `package.json` file, but what about the Node version? That is a piece of information that must be documented, and as we all know well, documentation is almost always left behind.

> _**Each Angular version is compatible with a range of Node versions**. When downgrading/upgrading Angular CLI, you also need to make sure the Node version being used is compatible. Besides, it's good practice to maintain versions during development, unless explicitly wanting to change them._

It was in that moment that I started to search for a possible **solution to manage different Node and Angular versions** for different projects. I found two concepts that seemed promising to be used together:

*   [nvm](https://github.com/nvm-sh/nvm), a version manager for Node
*   Local Angular CLI

## [](#nvm)nvm

nvm is a Node version manager command line tool. It allows the user to install multiple Node versions on its machine and then use different versions in separate shells simultaneously.

> _If you are not familiar with nvm commands, keep in mind that:_
> 
> *   `nvm run [arguments]` _is equivalent to_ `node [arguments]`
> *   `nvm exec [command] [arguments]` _is equivalent to_ `[command] [arguments]`

A normal nvm usage workflow (and the one we are going to use to manage different projects' Node versions) would be to **install each project's Node version and then execute it in an independent project dedicated shell**. Node can either be or not be natively installed in the machine, it does not make a difference for this use case.

For demonstration purposes, let's suppose we have the following projects:

*   Project XPTO, Node version 8.17.0
*   Project EPIC, Node version 12.16.1

To be able to execute both projects without needing to downgrade/upgrade your Node version, you have to:

* * *

##### [](#1-install-both-node-versions-using-nvm)1\. Install both Node versions using nvm:

```
$ nvm install 8.17.0
$ nvm install 12.16.1
```

Enter fullscreen mode Exit fullscreen mode

##### [](#2-go-to-the-directory-of-project-xpto-and-set-nvm-to-use-the-correct-node-version)2\. Go to the directory of project XPTO and set nvm to use the correct Node version:

```
$ nvm use 8.17.0
# check Node version being used
$ nvm run -v # or just "node -v"
> Running node v8.17.0
> v8.17.0
# start project XPTO
$ nvm exec npm start # or just "npm start"
```

Enter fullscreen mode Exit fullscreen mode

> _By executing_ `nvm use` _you are defining the Node version that nvm is going to run in that shell, not only in the directory where you executed the command._

##### [](#3-open-a-new-shell-go-to-the-directory-of-project-epic-and-do-the-same-for-that-projects-node-version)3\. Open a new shell, go to the directory of project EPIC and do the same for that project's Node version.

* * *

Now there are two different projects being executed by two different Node versions! _What's missing?_ Well, `nvm use` action is **shell session scoped**, which means new shells will start with the default nvm version of Node. So when you come back to work tomorrow and open a shell to start either of your projects, nvm will no longer be pointing to their correct Node version.

Luckily, nvm has the [`.nvmrc`](https://github.com/nvm-sh/nvm#nvmrc) file, which allows the user to specify a **Node version to be used by nvm in a directory** and all its sub-directories. Create this file in the root directory of your projects with the correct Node version:  

```
# in project root directory
$ echo "8.17.0" > .nvmrc
```

Enter fullscreen mode Exit fullscreen mode

Make sure you always use nvm commands to execute Node or npm, given that these are the commands that search for and use the `.nvmrc` file:  

```
# "node server.js" with Node version from .nvmrc
$ nvm run server.js
# "npm start" with Node version from .nvmrc
$ nvm exec npm start
```

Enter fullscreen mode Exit fullscreen mode

Now nvm will always run the correct Node version for your projects!

## [](#local-angular%C2%A0cli)Local Angular CLI

If you are working on an Angular project, besides guaranteeing the correct Node version you also need to make sure you are using the correct Angular CLI version when running your `ng` commands.

When you create an Angular project, the **Angular CLI is added as a development dependency** to your project's `package.json`:  

```
{
  ...
  "devDependencies": {
    "@angular/cli": "9.0.5",
    ...
  }
}
```

Enter fullscreen mode Exit fullscreen mode

This means that independently of the Angular CLI version you have globally installed in your machine, there will be a **locally-installed Angular CLI in `node_modules`** folder after installing your projects' dependencies. What you need to do is make sure you execute this locally-installed version instead of the global one. You can do one of the following:

* * *

##### [](#use-raw-packagejson-endraw-scripts)Use `package.json` scripts

The `npm run-script` command adds the `node_modules/.bin` binaries to the pre-existing shell's PATH that is then provided to the scripts. This means that scripts in `package.json` which execute `ng` will be running the locally-installed Angular CLI. If you also want to directly execute `ng` in the shell using this approach, you can add `"ng": "ng"` as a script in `package.json`.  

```
{
  ...
  "scripts": {
    "ng": "ng",
    "start": "ng serve",
    ...
  }
}
```

Enter fullscreen mode Exit fullscreen mode

```
# serve your application with nvm and local Angular CLI
$ nvm exec npm start
# create an Angular component using local Angular CLI
$ nvm exec npm run ng g component my-cool-component
```

Enter fullscreen mode Exit fullscreen mode

* * *

##### [](#use-raw-nodemodulesbinng-endraw-)Use `node_modules/.bin/ng`

Run the local Angular CLI by directly executing the binaries present in the `node_modules/.bin` folder in a shell.  

```
# create an Angular component using local Angular CLI
$ nvm exec ./node_modules/.bin/ng g component my-cool-component
```

Enter fullscreen mode Exit fullscreen mode

* * *

## [](#conclusion)Conclusion

By taking advantage of both **nvm and local Angular CLI binaries**, it is not only possible to manage different Node and Angular versioned projects, but also to do it in a simple and straightforward way.

With this methodology, it's important to **never forget to use the nvm commands**! It's true that a simple command (e.g. to start a project) turns a bit more verbose, but the trade-off of being able to work on and execute multiple projects seamlessly is a big plus.

_Hope this is helpful for someone out there!_ 💡  
_And of course, thanks for reading._ 🤓  
_If you have any question/suggestion/feedback, feel free to leave a comment._ 📝

_[PatricePeartree](https://twitter.com/PatricePeartree) @ Twitter_
