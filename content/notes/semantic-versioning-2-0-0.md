---
title: "Semantic Versioning 2.0.0"
date: '2014-05-05T08:46:27-03:00'
category: webclip
summary: 'Defines version numbers as MAJOR.MINOR.PATCH, with rules for public APIs, compatibility, pre-release labels, build metadata, and precedence in dependency management.'
tags: ["semantic-versioning", "versioning", "api-compatibility", "dependency-management"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Semantic Versioning 2.0.0"
    url: "http://semver.org/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2014-05/semver-org--semantic-versioning-2-0-0.md"
    kind: repo
---

Semantic Versioning 2.0.0 defines how software version numbers should communicate changes to a public API. It says to bump MAJOR for incompatible API changes, MINOR for backwards-compatible additions or deprecations, and PATCH for backwards-compatible bug fixes. It also defines pre-release labels, build metadata, and how version precedence is determined.

## Reading notes

- Software using Semantic Versioning must declare a public API, and that API should be precise and comprehensive.
- A normal version number must use the form X.Y.Z, with non-negative integers and no leading zeroes.
- A released version must not be modified after release; any change must go out as a new version.
- Version 0.y.z is for initial development, and the public API should not be considered stable.
- Version 1.0.0 defines the public API.
- Patch version Z increases for backwards-compatible bug fixes only.
- Minor version Y increases for new backwards-compatible public API functionality, and also for deprecating public API functionality.
- Major version X increases for backwards-incompatible public API changes.
- Pre-release versions are marked with a hyphen and dot-separated identifiers after the patch version.
- Build metadata is marked with a plus sign and dot-separated identifiers after the patch or pre-release version, and it should be ignored for precedence.
- Version precedence is determined by comparing major, minor, patch, and then pre-release identifiers from left to right.
- The document argues that semantic versioning makes dependency management clearer and helps avoid dependency hell.
- It recommends declaring that a project uses Semantic Versioning and linking to the specification from the README.
- For initial development in 0.y.z, the simplest approach is to start at 0.1.0 and increment the minor version for each release.
- If a backwards-incompatible change is accidentally released as a minor version, the recommendation is to fix it and release a new minor version that restores compatibility.
- Deprecating functionality should be documented and released in a minor version before removal in a later major release.
