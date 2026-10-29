---
title: "How to build stable systems"
date: '2016-04-11T14:04:27-03:00'
category: webclip
summary: 'The guide argues that stable systems stay under developer control, ship in small reversible steps, and favor limited scope, reproducible builds, strong testing, and operational safety.'
tags: ["stable-systems", "software-architecture", "devops", "reliability"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "How to build stable systems — Medium"
    url: "https://medium.com/@jlouis666/how-to-build-stable-systems-6fe9dcf32fc4"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2016-04/medium-com--how-to-build-stable-systems.md"
    kind: repo
---

The guide says stable systems are built for production from the start and kept under developer control. It favors small projects, limited scope, gradual transitions, reproducible artifacts, and operational habits that make rollback and recovery routine.

## Reading notes

- Developers should control the software, not managers or product owners.
- Work should be split into small units that can be controlled and shipped.
- A project should be small, self-contained, short, and have a clear win condition.
- Each project should begin with a short seed that tests the feasibility of the system.
- Projects should include only one major gamble, with the rest kept stable.
- Scope should be limited by explicitly listing what will not be solved yet.
- The system should be designed with its place in the infrastructure and test needs in mind.
- Experiments should be done as small analyses before the real project starts.
- Existing code and data quality should be checked before depending on them.
- New systems on top of old ones need a gradual transition plan.
- The system should be built for production use, with limited external dependencies.
- Modules should be loosely coupled, independent, and connected through protocols.
- Deep dependency chains, monster modules, and unnecessary intermediaries should be avoided.
- Communication should keep endpoints intelligent and intermediaries simple.
- The system should have supervision and restart strategies.
- Idempotence and ratcheting behavior should be preferred for retries and distributed delivery.
- The system should catch up to a point in time instead of maintaining separate online and offline paths.
- Each tool should do one thing well.
- Capacity should be defined up front.
- Continuous integration should produce a reproducible artifact that is the same in staging and production.
- Dependencies should be locked to specific versions and builds should be reproducible.
- Deployments should be fast and should include a shared default library for debugging, tracing, metrics, and chat integration.
- Correctness, elegance, and code quality should come before speed.
- Optimization should happen only after measurement.
- The system should collect and export metrics about itself.
- Testing, property-based checks, type systems, static analysis, and profiling should all be used when useful.
- The software should run on multiple environments, preferably UNIX.
- Code formatting debates are treated as low value once a standard exists.
- The error kernel should be identified and isolated.
- Load should be regulated at the border, and circuit breakers should stop cascading failure.
- PostgreSQL is the default database unless the dataset is above 10 terabytes.
- PostgreSQL should serve as authoritative storage, with other stores fed from it.
- New databases should be treated cautiously because of consistency and performance limits.
- Complex transactional behavior should be kept narrow when possible.
- Erlang is presented as the language that best supports robustness.
- The text warns against monoculture in programming languages.
- Deployment tooling should exist before a language is adopted.
- make(1) should be the common build tool across projects.
- Configuration should come from the environment, with default configuration in the artifact.
- Persistent data should live outside the artifact path, and logs should be bounded and rotated.
- Production and staging should use different credentials and isolated networks.
- Operations should optimize for sleep, graceful degradation, safe restarts, and easy rollback.
- Developers should usually work from staging and rely on shipped logs and metrics instead of production access.
- Production changes should happen by redeploying, not by editing hosts in place.
- Docker is described as immature at the time of writing and not ready for production.
