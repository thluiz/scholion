---
title: "Writing Custom Yeoman App Generators"
date: '2013-05-05T19:02:18-03:00'
category: webclip
summary: 'The page explains how Yeoman generators scaffold projects, distinguishes boilerplate copiers from app scaffolders, and shows how to build generators with prompts, templates, file writes, hooks, and dependency installs.'
tags: ["yeoman", "generators", "scaffolding", "nodejs"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Yeoman - Modern workflows for modern webapps"
    url: "http://yeoman.io/generators.html?utm_source=javascriptweekly&utm_medium=email"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2013-05/yeoman-io--writing-custom-yeoman-app-generators.md"
    kind: repo
---

The page says Yeoman generators can scaffold a project with chosen boilerplates, frameworks, and dependencies. It separates simple boilerplate copiers from fuller application scaffolders, and shows that community members can write and share generators for different workflows.

## Reading notes

- Yeoman generators can kick off a new project or part of a project without manually writing a boilerplate.
- A generator may only copy an existing boilerplate, or it may add customization prompts, unit tests, and documentation.
- Two generator types are listed: boilerplate copiers and application scaffolders.
- Boilerplate generators write an existing boilerplate project into the application directory when run with yo.
- Application scaffolders can cover build systems, sub-generators, dependency management, and workflow automation.
- Existing official generators can be forked and customized for another workflow.
- A boilerplate generator example shows cloning a generator project, adding a boilerplate under app/templates, editing package.json and README.md, installing dependencies, and running yo awesome.
- A tarball URL can be used instead of submodules to bring a boilerplate into a generator.
- Yo runs app/index.js by default inside a generator directory.
- generator-generator can create a full generator project with editorconfig, package.json, tests, and other defaults.
- The built-in yo generator command can also create a new generator directly from the command line.
- The index.js file is the entry point, and templates is where files for the generator live.
- The example Base class code defines options and a scaffold method that copies a template directory to a target location.
- The generator-bootstrap example uses prompts to ask for Bootstrap format and then installs the matching package with bowerInstall.
- Prompts can collect user input through name, message, default, and warning fields.
- this.copy() and this.template() copy files from the templates directory into the user’s project.
- this.write() writes custom content to files, and this.mkdir() creates directories.
- this.readFileAsString() imports file content as a string.
- A generator can append scripts and files, replace body content in an index file, and prepare default page content.
- Dependencies can be installed at the end with installDependencies.
- Sub-generators can be hooked in with this.hookFor and later called on their own.
- Files can also be pulled remotely with this.remote(), then copied into the project.
- The page points readers to generator internals and suggests studying existing generators such as HTML5 Boilerplate, Mobile Boilerplate, and AngularJS.
- The FAQ mentions Bower dependency installation, unit testing, sub-generators, extending beyond the API with npm packages, and publishing to npm.
