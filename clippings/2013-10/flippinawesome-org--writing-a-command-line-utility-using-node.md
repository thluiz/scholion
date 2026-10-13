---
url: "http://flippinawesome.org/2013/07/29/writing-a-command-line-utility-using-node/?utm_source=javascriptweekly&utm_medium=email"
captured_at: "2013-10-09T01:05:55-03:00"
title: "Writing a Command Line Utility using Node | Flippin' Awesome"
domain: "flippinawesome-org"
---

# **W**riting a Command Line Utility using Node

![75cc2a567cb8640e57fb1f15272690dd.jpg](flippinawesome-org--writing-a-command-line-utility-using-node/75cc2a567cb8640e57fb1f15272690dd.jpg)

*By [Jonathan Fielding](http://flippinawesome.org/authors/jonathan-fielding)*

Recently I started writing my own command line utility using Node**.** In doing some research, I found a few tutorials including a great one over at [Javascript Playground](http://javascriptplayground.com/blog/2012/08/writing-a-command-line-node-tool/) , however many were out of date or left out some key details**.** In this article I plan to walk you through all the steps needed to create your first Node-based command-line utility by showing how to build a simple command line calculator which takes two values and adds them together**.** While the example is simple, the goal is to show the underlying concepts that you can expand into a more complete and complex utility**.**

## Prerequisites

Before we get started there are a few prerequisites that we need**.**

- [NodeJS](http://nodejs.org/)  installed (current version is 0**.**10.13)
- NPM installed (this is typically packaged with Node)
- [Grunt-cli](http://gruntjs.com/)  installed (if not run `npm install -g grunt-cli`)
- [Grunt-Init](http://gruntjs.com/)  installed (if not run `npm install -g grunt-init`)
- [Node template for Grunt-Init](https://github.com/gruntjs/grunt-init-node)  (`git clone git@github.com:gruntjs/grunt-init-node.git ~/.grunt-init/node`)

## Getting Going

Assuming all the prerequisites installed properly, we can get started writing our command line tool using Node**.**

First, create a directory for the new project and use the Terminal to navigate to it**.** Next, we will initialize our project using the following command:

```
grunt-init node
```

When run, grunt-init will ask us some questions about the project before generating the scaffolding**.** Below are my answers, obviously you should customize the responses to suit your needs**.**

```
[?] Project name (calc) calc
[?] Description (The best project ever.) Simple command line calculator
[?] Version (0.1.0)
[?] Project git repository (git://github.com/jonathanfielding/calc.git) git@github.com:jonathan-fielding/CalcCLI.git
[?] Project homepage (https://github.com/jonathan-fielding/CalcCLI)
[?] Project issues tracker (https://github.com/jonathan-fielding/CalcCLI/issues)
[?] Licenses (MIT) 
[?] Author name (Jonathan Fielding) 
[?] Author email (j.fielding@me.com) 
[?] Author url (none) http://www.jonathanfielding.com
[?] What versions of node does it run on? (>= 0.8.0)
[?] Main module/entry point (lib/calc) 
[?] Npm test command (grunt nodeunit)
[?] Will this project be tested with Travis CI? (Y/n) n
[?] Do you need to make any changes to the above before continuing? (y/N) n
```

I should note that if you are on Windows, you might want to choose a name other than “calc” that doesn’t conflict with pre-existing commands**.**

Once our project scaffolding is created, let’s take a quick look in our directory to see what grunt-init has generated**.**

```
Gruntfile.js
README.md
package.json
LICENSE-MIT
lib/calc.js
test/calc_test.js
```

If we load up the package.json in our editor is should look like this:

```
{
  "name": "calc",
  "description": "Simple command line calculator",
  "version": "0.1.0",
  "homepage": "https://github.com/jonathan-fielding/CalcCLI",
  "author": {
    "name": "Jonathan Fielding",
    "email": "j.fielding@me.com",
    "url": "http://www.jonathanfielding.com"
  },
  "repository": {
    "type": "git",
    "url": "git@github.com:jonathan-fielding/CalcCLI.git"
  },
  "bugs": {
    "url": "https://github.com/jonathan-fielding/CalcCLI/issues"
  },
  "licenses": [
    {
      "type": "MIT",
      "url": "https://github.com/jonathan-fielding/CalcCLI/blob/master/LICENSE-MIT"
    }
  ],
  "main": "lib/calc",
  "engines": {
    "node": ">= 0.8.0"
  },
  "scripts": {
    "test": "grunt nodeunit"
  },
  "devDependencies": {
    "grunt-contrib-jshint": "~0.6.0",
    "grunt-contrib-nodeunit": "~0.2.0",
    "grunt-contrib-watch": "~0.4.0",
    "grunt": "~0.4.1"
  },
  "keywords": []
}
```

We need to tell our package that it should be installed globally if possible, this can be achieved through adding the `preferGlobalproperty`**.** We also want to define the command that we will use on the command line, we can do this by adding a bin object**.** This object needs to list any commands the user may want to enter, for this example we will add one command `calc`**.** We will need to point this to our main JavaScript file for the utility which is lib/calc**.**js.

```
"preferGlobal": "true",
"bin": {
    "calc" : "lib/calc.js"
}
```

We have told our package.json that whenever the user of our utility enter `calc`, it should run lib/calc**.**js. However, what we haven’t yet done is tell our script how it should be executed**.** We do this by opening up lib/calc.js and adding this line at the top:

```
#! /usr/bin/env node
```

This tells the script it needs to be executed using Node**.** At the moment if we type `calc` into our Terminal, we will receive the error**.**

```
-bash: calc: command not found
```

This is because we have not installed our package yet so we are unable to test it**.** To install our package locally we simply need to run `npm link` which will give us access to the `calc` command in Terminal**.**

You will probably notice that when you run this command, npm will download some files**.** This is npm downloading all the dependencies required by your tool that were specified in the package.json**.**

At the moment when we test our `calc` command nothing will happen; this is as expected**.**

When looking in the main plugin file (in this case lib/calc**.**js) we will see that grunt-init has generated this code:

```
exports.awesome = function() {
  return 'awesome';
};
```

As you might expect, `exports` is how we export methods and variables from a script**.** These exports can then be used in other scripts. In the case of our calculator script, this isn’t needed as it is unlikely our script will be used as part of other scripts**.** We can delete this.

## Passing Arguments

We expect the users of our tool to enter the name of our tool then for the arguments, which in this case are the numbers to add**.** The command might look something like this.

```
calc 10 10
```

To achieve this, we need to get the to get the arguments**.** The parameters passed are stored in an array `process.argv`**.** We can output the contents of this array:

```
console.log(process.argv);
```

If you run `calc 10 10` in your terminal you should see a result similar to the following:

```
[ 'node', '/usr/local/bin/calc', '10' , '10' ]
```

The first two items in the array relate to how the script is executed and where the executable is**.** The third item is the first user defined argument. To get only the user supplied arguments we can simply slice the array at index two**.**

```
var userArgs = process.argv.slice(2);
```

With our `userArgs` stored, we can simply reference the arguments passed as `userArgs[0]` and `userArgs[1]`**.** However, to make this easier to read we can simply store these in variables**.** Because the original array stored these as strings, we will need to use `parseInt` to convert them to an integer**.**

```
var value1 = parseInt(userArgs[0]);
var value2 = parseInt(userArgs[1]);
```

We now need to calculate the result of the arguments passed by the user**.** For this example we will simply add the two values together**.**

```
var answer = value1 + value2;
```

Finally, we need to output this answer to the user**.** We will simply use `console.log` to output the answer**.**

```
console.log(answer);
```

Now go back to the Terminal and run the command:

```
calc 10 10
```

The utility will reply with the answer:

```
20
```

At this point we have a very simple calculator for the command line which allows us to add two values together**.**

## Publishing to npm

We already have a working command line utility, but now we want to publish the utility as a npm module**.** First we need to authenticate ourselves or signup with npm**.** To do this, we run:

```
npm adduser
```

This will ask us to supply a username, password and email address**.** Once we are authenticated we need to ensure our project is in a git repository**.** We should also check the following:

- We have added node\_modules/ to our .gitignore, (grunt-init should have included a .gitignore file as part of the original template to make this easy for us)
- We also need to ensure that our repository has a valid package.json (running `npm link` will verify this)**.**
- Push your repository to GitHub (or elsewhere, BitBucket offers a good alternative) and make sure your package.json has a repository object that looks like this:

  ```
  "repository": {
     "type": "git",
     "url": "git://github.com/jonathanfielding/calc.git"
   }
  ```

Once you have verified these tasks and you are happy with everything, simply run `npm publish`**.** This will publish your module and users can install through `npm install modulename`**.**

## Commanding your Node CLI arguments with Commander**.**js

One of the most useful features of a command line utility is the ability for it to accept arguments from the user**.** These can vary significantly from the most simple utility that accepts one argument to a more complex utility which accepts lot of arguments**.**

Above, we achieved this through reading the `process.argv` array**.** Our original code being:

```
var userArgs = process.argv.slice(2);
var value1 = parseInt(userArgs[0]);
var value2 = parseInt(userArgs[1]);
```

This is fine for a small little utility that adds two numbers together However, this could potentially get quite messy for more complicated command line utilities**.** That’s where [Commander.js](https://github.com/visionmedia/commander.js/) comes in**.**

Our first step to use Commander.js with our project is to install it using npm:

```
npm install commander --save-dev
```

After we have installed commander, we now need to use Require to include it in our project**.**

```
var program = require('commander');
```

With commander in place we can now replace:

```
var userArgs = process.argv.slice(2);
```

…with:

```
program
  .version('0.1.0')
  .option('--number1 ', 'specify the first number to add together',Number)
  .option('--number2 ', 'specify the second number to add together',Number)
  .parse(process.argv);
```

To retrieve our arguments we can now access them using `program.number1` and `program.number2`**.** This means we will need to update the values we reference to reference these new values**.**

```
var answer = program.number1 + program.number2;
```

Now if we test our utility we now need to reference the option we want to pass a value to so the command now becomes:

```
calc --number1 20 --number2 20
```

…which should result in:

```
40
```

As an added bonus, our users will now be able to use `calc --help` to see all the arguments that our utility accepts**.**

This is just skimming on the surface of what commander**.**js is able to offer, to find out more information visit the [commander**.**js website](http://visionmedia.github.io/commander.js/) .

## Underscore.js, the utility belt for your Node CLI

Underscore**.**js is a utility belt library which can be used on both the frontend and with Node**.**

Currently, if the user enters a string instead of a number our simple calculator example the result is `NaN` (not a number)**.** To fix this we can use Underscore.js to help us to validate whether the result is in fact a number and if it isn’t we will let the user know they need to enter numbers**.**

The first step is for us to install Underscore**.**js into our project

```
npm install underscore --save-dev
```

Once done we will then need to get Underscore**.**js by using Require. Add this directly after the line where we have included commander**.**js.

```
var _ = require('underscore');
```

Then replace the existing `console.log(answer)` with the following calculation logic:

```
if(_.isUndefined(program.number1) || _.isUndefined(program.number2)){
	console.log('Please check your arguments, check --help for details');
}
else{
	if(_.isNaN(program.number1) || _.isNaN(program.number2)){
		console.log('Please only enter numbers');
	}
	else{
		answer = program.number1 + program.number2;
		console.log(answer);
	}
}
```

The first portion of this uses Underscore to check if either of the values is undefined and, if one is, an error message is displayed to the user**.** The next step is to check if the numbers entered are in fact numbers and, if they are not, another error message will be displayed**.** Finally, when the two numbers have been entered a result has been calculated, show it to the user**.**

This is of course a very simple example of how Underscore**.**js can be used.

## Help your users to help themselves use your CLI

If you are familiar with the command line on Mac/\*nix, you will likely know of the `man` command which allows you to view manuals for different command line utilities**.** For example if you enter `man ls` it will load the manual for the `ls` command**.**

We can do this with Node command line utilities as well by creating a man file and adding it to our package.json file**.**

### Getting started with man

For our manual we will use our existing README**.**md file, to enable this to work as a manual using the man command we will need to convert the README**.**md file into the correct format. For this we will use a tool called [marked-man](https://github.com/kapouer/marked-man)  which will take our README**.**md file and give us a lovely manual (if you’re on Windows, you can check out the [Groff tool](http://www.gnu.org/software/groff/groff.html)  which adds similar functionality)

Our first step is to install marked-man**.**

```
npm install marked-man -g
```

Once this is installed we can simply run the following command to generate our manual (please note that a subfolder named “doc” will need to exist otherwise you will get an error):

```
marked-man README.md > doc/calc.1
```

With our manual prepared we can now add it to our package.json file**.** This is done by adding an extra item to the JSON object called “man” with the value set to an array of files that make up your manual**.**

```
"man" :[ "./doc/calc.1" ]
```

With this added we now need to update the npm link to our plugin by running**.**

```
npm link
```

We should now be able to view our new manual in the command line using:

```
man calc
```

## Where to Go From Here

While it’s unlikely you will use this simple utility on a day to day basis, hopefully it has allowed you to learn about how to write a command line utility using Node**.** There are a lot of modules available which will help you to enhance both the features and the usability of your command line utilities**.** The [NPM registry](https://npmjs.org/)  is a fantastic resource for finding modules that you can use**.** Through using NPM modules we can not only save time but we can also be more consistent with how other command line utilities have been developed**.**

## Credits

Thanks to [Jack Franklin](https://twitter.com/Jack_Franklin)  for his original post, I based this article on what I learnt from his original post on creating a command line tool using Node**.**

I based portions of this post partially on some comments on a Reddit post of the original article**.** In particular [ISV\_Damocles](http://www.reddit.com/user/ISV_Damocles)  offered some good suggestions which I then researched to put this piece together**.**

*This post is a combination of articles originally posted at <http://www.jonathanfielding.com/writing-a-command-line-utility-using-node/> and <http://www.jonathanfielding.com/ive-written-a-node-cli-so-now-what/>*
