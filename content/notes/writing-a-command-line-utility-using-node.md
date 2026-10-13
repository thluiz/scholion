---
title: "Writing a Command Line Utility using Node"
date: '2013-10-09T01:05:55-03:00'
category: webclip
summary: 'The article walks through creating a simple Node-based CLI calculator, from Grunt-init scaffolding and argument parsing to npm publishing, Commander.js, Underscore.js, and man-page support.'
tags: ["node", "command-line", "npm", "commander-js"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Writing a Command Line Utility using Node | Flippin' Awesome"
    url: "http://flippinawesome.org/2013/07/29/writing-a-command-line-utility-using-node/?utm_source=javascriptweekly&utm_medium=email"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2013-10/flippinawesome-org--writing-a-command-line-utility-using-node.md"
    kind: repo
---

The article shows how to build a small command-line calculator with Node. It starts from a Grunt-init scaffold, adds a shebang line, links the package locally with `npm link`, and reads user input from `process.argv` before adding two values and printing the result.

It then extends the tool with `package.json` configuration for global installation, npm publishing steps, Commander.js for named options, Underscore.js for input checks, and a man page generated from `README.md` so users can run `man calc`.

## Reading notes

- Create the project with `grunt-init node` and review the generated files.
- Add `preferGlobal` and a `bin` entry in `package.json` so `calc` maps to `lib/calc.js`.
- Put `#! /usr/bin/env node` at the top of the script so Node executes it.
- Use `npm link` to install the package locally and test the command.
- Read arguments from `process.argv.slice(2)` and convert the values with `parseInt`.
- Add the two numbers and print the answer with `console.log`.
- Before publishing, authenticate with `npm adduser`, verify the repository settings, and run `npm publish`.
- Use `commander` to define named options like `--number1` and `--number2`, then read them from `program.number1` and `program.number2`.
- Use `underscore` to detect missing or invalid numeric values and print an error message when needed.
- Generate a manual with `marked-man`, add it to the `man` field in `package.json`, and view it with `man calc`.
