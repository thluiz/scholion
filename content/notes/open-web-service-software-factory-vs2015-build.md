---
title: "Open Web Service Software Factory (WSSF) - Build for Visual Studio 2015"
date: '2015-08-11T23:43:02-03:00'
category: webclip
summary: 'Author rebuilds Microsoft’s Web Service Software Factory for Visual Studio 2015, preserving existing features and offering binaries plus a workaround for installation issues.'
tags: ["wcf", "visual-studio-2015", "soa", "code-generation"]
has_commentary: false
generated_by: "openai/gpt-5.1"
sources:
  - title: "Open Web Service Software Factory (WSSF) - Build for Visual Studio 2015"
    url: "https://www.phidiax.com/blog/post/open-web-service-software-factory-wssf-build-for-visual-studio-2015"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-08/phidiax-com--open-web-service-software-factory-vs2015-build.md"
    kind: repo
---

The text describes how Microsoft’s Web Service Software Factory (WSSF), a contract‑first, modeling‑based tool originally released for Visual Studio 2008, has not been updated for newer Visual Studio versions. The author explains that Phidiax relies on WSSF for SOA implementations, using it to design schemas first and then generate interoperable WSDL contracts for ASMX or WCF, serializable with XML Serializer or Data Contract Serializer. Because the tool is used daily and clients are moving to Visual Studio 2015, the author rebuilt WSSF for VS 2015 with only the changes required to compile and install, keeping features unchanged. Binaries and source are made available, and the author notes known installation problems with a workaround and invites help fixing the issue where the main package fails to install member packages.

## Reading notes

- Microsoft’s Standards and Practices group released the Web Service Software Factory as a contract‑first development, modeling, and practices tool starting with Visual Studio 2008.
- The WCF development community has not received updates to move WSSF forward to the latest Visual Studio versions.
- Phidiax uses WSSF in many SOA implementations because it supports schema‑first development that drives WSDL contract generation.
- The tool can generate interoperable WSDL contracts using either ASMX or WCF.
- Generated services can be serialized using XML Serializer or Data Contract Serializer.
- The author uses WSSF daily to build services from XSDs and to maintain consistent development patterns.
- As clients begin adopting Visual Studio 2015, the author decided it would be useful to rebuild WSSF for the VS 2015 environment.
- The rebuild only includes changes necessary to achieve a successful build and installation for Visual Studio 2015, without introducing new features.
- The author observed installation issues similar to those reported for the VS 2012 version in CodePlex discussions.
- A workaround for these installation problems is provided in the steps referenced in the text.
- Binaries for the VS 2015 build are made available, and the source code can be obtained from the GitHub repository at https://github.com/Phidiax/open-wssf-2015.
- There is a known issue where the main package does not install the member packages, and the author asks for help resolving this.
- Despite this problem, the author chose to release the build with the workaround so that existing users can continue developing services with WSSF on Visual Studio 2015.
