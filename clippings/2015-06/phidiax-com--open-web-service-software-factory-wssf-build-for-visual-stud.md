---
url: "https://www.phidiax.com/blog/post/open-web-service-software-factory-wssf-build-for-visual-studio-2013-and-2015-rc"
captured_at: "2015-06-02T19:53:21-03:00"
title: "Open Web Service Software Factory (WSSF) - Build for Visual Studio 2013"
domain: "phidiax-com"
---

# Open Web Service Software Factory (WSSF)

## Background

The Microsoft Standards and Practices group put out a contract-first development, modeling, and practices based tool starting long ago with Visual Studio 2008, and it was known as the Web Service Software Factory. Unfortunately for the WCF development community, it seems that there have been no updates to bring this tool forward with the latest Visual Studio Environment versions (VS 2013 has come and gone, and we are approaching release of VS 2015, with no recent updates or ports).

Phidiax uses this tool in many of our SOA implementations as it allows for schema development up front which is then used to generate interoperable WSDL contracts using ASMX or WCF, and can be serialized using XML Serializer or Data Contract Serializer. Since I make use of this tool daily in building services to easily generate code from XSDs and maintain the development patterns, and clients are beginning to make the move to VS 2013 and prepare for VS 2015, I thought it would be beneficial to rebuild this tool into these latest environments. Obviously, that benefits those of you who make use of this tool as well!

## How To

To get this moving, I made no changes aside from those necessary to achieve a successful build and installation for VS 2013, so no feature changes have been implemented. Once Visual Studio 2015 is released, I will also begin updating for that environment as well (I attempted for VS 2015 RC, but there are definitely some issues at runtime, so I will wait for final to debug and address). I noticed that there are installation issues (as many in CodePlex discussions commented of the VS 2012 version), but there is a workaround described below. The following steps contain the links to the binaries. Source code is available if needed at <https://github.com/Phidiax/open-wssf-2013>.

If anyone knows how to eliminate the issue causing the main package not to install the member packages, I'd love to get this fixed, but since this workaround isn't that bad, I wanted to get something out there to keep those using this tool coding quality services.
