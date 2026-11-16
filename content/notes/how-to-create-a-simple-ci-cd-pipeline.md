---
title: "How to Create a Simple CI/CD Pipeline"
date: '2026-11-16T01:19:20+00:00'
category: webclip
summary: 'The page explains how CI/CD pipelines automate builds, tests, and deployments, and shows how Microtica uses a declarative YAML file to define build steps, create Docker images, and track pipeline health.'
tags: ["ci-cd", "microtica", "declarative-pipeline", "docker"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "How to Create a Simple CI/CD Pipeline"
    url: "https://dev.to/saramiteva/how-to-create-a-simple-ci-cd-pipeline-420"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/dev-to--how-to-create-a-simple-ci-cd-pipeline.md"
    kind: repo
---

The page presents CI/CD pipelines as a way to automate software delivery steps such as builds, tests, and deployments. It contrasts scripted and declarative syntaxes and favors the declarative approach for simpler pipelines because it gives a clear structure and supports pipeline as code.

## Reading notes

- CI/CD pipelines automate the steps of the software delivery process, including code builds, automated tests, and deployment to testing or production environments.
- Scripted pipeline syntax is based on Groovy DSL, is less restrictive, and can become hard to read and write.
- Declarative syntax is more restrictive, has a well-defined structure, and fits simpler CI/CD pipelines.
- Declarative syntax supports pipeline as code, so the pipeline definition can be stored in version control.
- In Microtica, each component or microservice has a microtica.yaml file at the root of its source code.
- Microtica extracts the build specification from the code and creates a state machine to run the process.
- Build pipeline changes are taken only from the YAML file, not from the UI, so the source code remains the single source of truth.
- The example pipeline uses Pipeline, StartAt, States, Type, Resource, Parameters, commands, sourceLocation, artifacts, and End.
- The commands section can contain bash commands for build, test, and code quality checks.
- Microtica supports bash commands for the execution action and plans to allow custom actions in the future.
- An extended example adds environment variables, creates an ECR repository if needed, builds a Docker image, tags it, and pushes it to the repository.
- After the microtica.yaml file is defined, build automation can be enabled through a webhook that triggers builds when new code is pushed.
- The Docker image becomes an artifact that can be deployed to a Kubernetes cluster.
- The platform shows build events in real time, marks failed builds in red, and exposes logs for debugging.
- The Pipelines overview page lets users track pipeline status, inspect build history, and see whether a pipeline is marked unhealthy after repeated failures.
- The page says automated pipelines reduce manual errors, improve productivity, and reduce stress around releases.
