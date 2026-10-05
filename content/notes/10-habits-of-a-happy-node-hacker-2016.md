---
title: "10 Habits of a Happy Node Hacker (2016)"
date: '2015-12-23T15:00:43-03:00'
category: webclip
summary: 'Heroku lists ten habits for app developers using Node.js: start with npm init, lock dependencies, use ES6, keep filenames lowercase, cluster apps, rely on environment variables, manage garbage collection, hook npm scripts, ignore generated files, and simplify builds and code.'
tags: ["nodejs", "npm", "javascript", "deployment"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Heroku | 10 Habits of a Happy Node Hacker (2016)"
    url: "https://blog.heroku.com/archives/2015/11/10/node-habits-2016"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-12/blog-heroku-com--10-habits-of-a-happy-node-hacker-2016.md"
    kind: repo
---

Heroku presents ten practices for Node.js app developers aimed at keeping projects healthy as the JavaScript ecosystem grows more crowded. The list focuses on setup, dependency control, platform portability, process management, environment configuration, memory behavior, build automation, version control hygiene, and reducing complexity.

## Reading notes

- Start new projects with `npm init`, then add an `engines` field that specifies the current Node version.
- Use `.npmrc` or `--save-exact` so dependencies are recorded in `package.json` with exact versions, and consider shrinkwrap when production needs fixed nested versions.
- Take advantage of ES6 features in Node 4+, such as arrow functions, template strings, and `let`.
- Keep filenames lowercase so `require` statements stay portable across Linux, OS X, and Windows.
- Use Cluster to take advantage of multiple cores and more than about 1.5 GB of memory, and set concurrency from the environment when possible.
- Prefer environment variables over multiple environment-specific config files, and use a Procfile plus node-foreman for local process setup.
- Be aware that V8’s garbage collector can wait before reclaiming memory, and adjust V8 flags in the Procfile when memory limits are tight.
- Use npm lifecycle scripts such as `preinstall` and `postinstall` for automation, and move longer scripts into files when they grow.
- Keep generated files like `node_modules`, `bower_components`, build outputs, and npm debug logs out of git.
- Simplify architecture, build systems, and code, including by favoring static frontends with a Node API, avoiding unnecessary build tools, and using async-await through Babel when needed.
