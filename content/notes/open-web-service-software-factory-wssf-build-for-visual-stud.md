---
title: "Open Web Service Software Factory (WSSF) - Build for Visual Studio 2013"
date: '2015-06-02T19:53:21-03:00'
category: webclip
summary: 'The post explains that WSSF was not updated for newer Visual Studio versions, so Phidiax rebuilt it for VS 2013 without feature changes and notes a workaround for installation issues.'
tags: ["wssf", "visual-studio-2013", "wcf", "soa"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Open Web Service Software Factory (WSSF) - Build for Visual Studio 2013"
    url: "https://www.phidiax.com/blog/post/open-web-service-software-factory-wssf-build-for-visual-studio-2013-and-2015-rc"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-06/phidiax-com--open-web-service-software-factory-wssf-build-for-visual-stud.md"
    kind: repo
---

The post says the Open Web Service Software Factory was originally released with Visual Studio 2008 and had not been updated for later Visual Studio versions. Phidiax rebuilt it for Visual Studio 2013 because it uses the tool in SOA implementations and wanted it to keep working for code generation from XSDs and contract-first service development.

## Reading notes

- The Web Service Software Factory was a Microsoft Standards and Practices tool for contract-first development, modeling, and practices.
- The author says there had been no updates to move the tool forward to newer Visual Studio versions.
- Phidiax uses the tool in SOA implementations to develop schemas first and generate interoperable WSDL contracts with ASMX or WCF.
- The tool can be serialized with XML Serializer or Data Contract Serializer.
- The rebuild for VS 2013 did not include feature changes, only the changes needed for a successful build and installation.
- The author plans to update it again for Visual Studio 2015 after the final release.
- Installation issues remain, and the post mentions a workaround.
- Source code is available on GitHub.
