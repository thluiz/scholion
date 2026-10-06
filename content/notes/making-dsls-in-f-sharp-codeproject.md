---
title: "Making DSLs in F#"
date: '2012-06-12T16:02:14-03:00'
category: webclip
summary: 'The article shows how F# can be used to build a simple DSL for software estimation, with project, resource, group, task, and prepare statements that generate a Microsoft Project plan.'
tags: ["f-sharp", "dsl", "software-estimation", "microsoft-project"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Making DSLs in F# - CodeProject"
    url: "http://www.codeproject.com/Articles/39031/Making-DSLs-in-F"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2012-06/codeproject-com--making-dsls-in-f-sharp-codeproject.md"
    kind: repo
---

The article presents a simple F# DSL for software estimation and project planning. It uses English-like statements to define a project, add resources, group tasks, assign durations, and then generate a Microsoft Project plan.

## Reading notes

- The article defines a DSL as a way to express domain-specific logic in English instead of a programming language.
- The example domain is software estimation, with a real-world version already used at the author’s company.
- The attached code is a single .fs file and requires Project 2007 to run.
- The problem described is estimating software work from an RFP by breaking a project into tasks, durations, resources, and milestones.
- The DSL is meant to save time compared with drawing and rearranging a Gantt chart in Microsoft Project.
- It also lets business logic and validation rules be embedded in the planning procedure.
- The target users are project managers who may not know programming but can work with a DSL.
- The article presents F# as a good choice because it is a first-class .NET language and can be used to build the needed infrastructure.
- The first statement shown defines a project name and start date, and it maps to a `Project` type with mutable fields.
- The DSL keeps one project in a global variable called `my_project`.
- A `project` function initializes the project name, empty resource and group lists, and parses the start date.
- Resources are modeled with a `Resource` type containing name, position, and rate.
- A `resource` statement creates a resource and prepends it to the project’s resource list.
- The article notes that list items end up in reverse order and are later reversed when needed.
- A `group` statement links a task group to a named resource using string lookup over the project’s resource list.
- Tasks are modeled with a `Task` type containing name and duration.
- Time units are represented by constants such as hours, days, weeks, and months so that `task ... takes ...` reads fluently.
- The `task` function formats duration values for Project and adds each task to the current group.
- The current task is found as the head of the list because new tasks are prepended.
- The `prepare` function creates a Project application, adds the project, copies resources, creates group tasks, and links task predecessors.
- The article ends with a complete sample script that defines resources, groups, tasks, and finishes with `prepare my_project`.
