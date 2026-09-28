---
title: "Building Microservices With Security in Mind"
date: '2022-05-30T09:39:32-03:00'
category: webclip
summary: 'The article says microservices, open architecture, DevSecOps, and observability help banks and fintech teams ship faster while keeping security checks, testing, and monitoring inside the delivery flow.'
tags: ["microservices", "cybersecurity", "devsecops", "fintech"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Building Microservices With Security in Mind - Codemotion Magazine"
    url: "https://www.codemotion.com/magazine/backend-dev/microservices/microservices-security/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2022-05/codemotion-com--building-microservices-with-security-in-mind.md"
    kind: repo
---

The article links fintech-led banking change to open architecture and microservices. It says banks can offer in-house and third-party services in one place, detect threats earlier, and use OpenID for decentralized authentication. It also uses Credemtel as an example of open architecture for SME customers and billing-data-based reconciliation and financial analysis.

## Reading notes

- Microservices are presented as a way to develop, test, deploy, and scale specific parts of a fintech application more easily.
- The article says security checks should be delegated to the API gateway, with authentication and authorization handled there.
- dotNet 6 is described as a fast full-stack web framework with minimal APIs, cloud-based configurations, and cross-platform support.
- DevSecOps is framed as an extension of DevOps that adds automation, feedback loops, agility, and cross-functional collaboration.
- Security testing should run throughout the CI/CD pipeline and the software development lifecycle, not only at the end.
- TDD can be automated with NUnit, and TestDriven.net is mentioned for better integration with Visual Studio.
- Sonarqube is used for code analysis, quality reports, code smells, and common security vulnerabilities.
- RedGate is mentioned for dataops, to speed up database changes and reduce deployment failures.
- Azure DevOps pipelines are described as tools that automatically build and test code projects.
- Angular is recommended for the UI layer in open architecture apps.
- RabbitMQ and MassTransit are presented as tools for decoupled message-based applications.
- OpenID is described as a decentralized authentication protocol that speeds up signup and stores user details for reuse.
- Observability is presented as useful for understanding the internal state of distributed microservices systems.
- Correlation IDs support distributed tracing, while Prometheus and Grafana are used for monitoring and visualization.
