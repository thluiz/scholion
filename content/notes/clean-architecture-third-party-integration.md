---
title: "Clean Architecture: Third-Party System Integration"
date: '2026-11-16T20:20:22+00:00'
category: webclip
summary: 'Explains how integrating with third‑party systems requires strict validation and clear contracts, and how clean architecture layers help enforce constraints on outgoing and incoming data.'
tags: ["clean-architecture", "third-party-integration", "validation", "software-design"]
has_commentary: false
generated_by: "openai/gpt-5.1"
sources:
  - title: "Clean Architecture: Third-Party System Integration"
    url: "https://journal.optivem.com/p/clean-architecture-third-party-system"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/journal-optivem-com--clean-architecture-third-party-integration.md"
    kind: repo
---

The text discusses integrating enterprise applications with third-party systems such as ERPs, couriers, sensors, or databases, using mechanisms like REST, SOAP, FTP, and SQL. It emphasizes that systems must validate data both when sending to and receiving from external systems, covering types, ranges, formats, and units, and that this responsibility fits naturally into a clean architecture through validations in use cases and domain invariants in entities and value objects.

## Reading notes

- Enterprise systems often integrate with external systems like ERPs, courier services, or industrial sensors.
- Common integration mechanisms include REST APIs, SOAP, FTP, SQL, and other similar technologies.
- A central challenge is ensuring that data sent to a third-party system respects that system’s constraints.
- Example of outgoing constraints: an ERP might only accept order numbers up to 10 characters, positive prices, and monetary amounts with exactly two decimal places.
- Applications must validate these constraints before sending data to avoid third-party errors caused by invalid requests.
- Incoming data from third-party systems must also be checked against constraints defined on the consuming side.
- For incoming data, the system should verify type compatibility, such as ensuring a first_name is a string and an amount is a positive decimal.
- Data from external sources should not be trusted by default; the system should handle it conservatively.
- Additional constraints can apply to lengths and formats, such as strings having length within a specific range.
- The system may require specific formats for fields like email or social security numbers.
- Values can be limited to particular sets, such as colors restricted to red, green, or blue.
- Numeric values may be constrained to defined ranges, like integers between lower and upper bounds, with choices about inclusivity.
- Date fields might need to be restricted to past or future values depending on the business rule.
- Integrations must explicitly clarify units whenever quantities are exchanged between teams or systems.
- Differences between metric and imperial units must be documented in the API contract.
- Adapters are needed to handle conversion between different measurement units across integrated systems.
- Beyond basic validation, sanity checks can be added to detect sensor errors or improbable values.
- Example sanity check: an aircraft nose angle might only be considered valid within two specific degree ranges, with values outside treated as potential sensor faults.
- Another example: a height sensor could accept values only within a researched global human height range, extended slightly with buffers, treating anything outside as possible sensor error.
- The text mentions a Boeing-related incident where a single sensor provided bad data to MCAS and lacked input restrictions, suggesting that validation and sensor redundancy might have prevented the issue.
- When sensors are involved, having multiple sensors and comparing their readings can help detect inconsistent or erroneous data.
- Validation is presented as crucial for preventing third-party systems from returning errors due to invalid outgoing data.
- Validation is also crucial for ensuring that incoming data from external systems satisfies internal constraints.
- In a clean architecture, some validation occurs in the use case layer before reaching the infrastructure layer.
- Domain invariants in the domain layer help guarantee the validity of data represented by domain entities and value objects.
- By the time data reaches the infrastructure layer to be sent externally, it should already be in a valid state because of use case and domain validations.
- On the receiving side, infrastructure components read data from third-party systems and construct domain entities and value objects from it.
- The domain invariants enforced by these entities and value objects help ensure that incoming external data respects the required domain rules.
