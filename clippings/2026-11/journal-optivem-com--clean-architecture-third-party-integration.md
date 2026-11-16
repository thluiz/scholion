---
url: "https://journal.optivem.com/p/clean-architecture-third-party-system"
captured_at: "2026-11-16T20:20:22+00:00"
title: "Clean Architecture: Third-Party System Integration"
domain: "journal-optivem-com"
---

In enterprise applications, we often need to integrate with third-party systems. For example, if we have an ordering system, we may need to integrate it with an ERP and courier systems. We may need to integrate with sensors if we're working in industrial automation.

Some possibilities for integrating with third-party systems include the following:

*   REST API
    
*   SOAP
    
*   FTP
    
*   SQL
    
*   etc.
    

[

![](https://substackcdn.com/image/fetch/$s_!gXr_!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Feca4b78d-9595-4b35-9d09-d2d26b9dc285_900x1110.jpeg)

](https://substackcdn.com/image/fetch/$s_!gXr_!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Feca4b78d-9595-4b35-9d09-d2d26b9dc285_900x1110.jpeg)

One challenge arises: when sending data to the third-party system, we need to ensure that it's valid. We must respect constraints set by the third-party system to prevent us from sending bad data to the third-party system.

_So, to give one example, when we send some order to an ERP system, perhaps the order number that we assign must be a maximum of 10 characters because that's the only thing the ERP can accept. The order price needs to be in decimals, exactly to a 2 decimal point precision, and it needs to be positive. This means that we need to do validations for those constraints before we send data to the external system._

Conversely, we also need to check that the data coming from the third-party system is valid and satisfies any constraints we specified.

_For example, when we're reading data from the third-party system, we also need to check type compatibility; for example, the first\_name field must be a string, the amount field must be a decimal, it must be positive, and the product must be set as active._

Furthermore, we can have certain limitations regarding ranges and formats.

_For example, a string must be of length between 3 and 10; the email or social security number must be in a certain format, a value must be in some kind of range (e.g., color must be either red, green or blue, no other string is accepted), and an integer must be between 2 and 100 (inclusive or non-inclusive for lower and upper bounds). We may check that some dates must be in the past or future._

So the general principle is we need to hold the responsibility of sending valid data to external systems. Still, on the other hand, we also have to be very conservative when we're reading data from external systems - we should not trust data from external sources.

The other issue with third-party systems is that whenever any units are involved, we have to be very explicit with the other teams we integrate with - what units are used?

For example, suppose that one team deals with metric and another deals with imperial units. These differences need to be documented as part of the API contract and have adequate adapters to handle the unit conversion.

Aside from these standard, simple, relatively simple validations, we can have additional validation that could be used for sanity checking.

*   Example 1: Suppose that for an aircraft, the angle of the nose must be between 0 and 90 degrees or between 270 and 360 degrees. Any value outside of that range is interpreted as a possible sensor error.
    
*   Example 2: We have a sensor for measuring the height of people. Let’s say we research heights for people worldwide and see that the shortest person is 50 cm and the tallest person is 240 cm. Adding buffers to the min and max, we then say that our senior should accept values between 40 cm and 250 cm as valid, but anything beyond that we interpret as a possible sensor error.
    

_This particular issue occurred with Boeing, where for example, there was just one sensor, and it was taking in bad data, and as was commented, there was no input restriction to MCAS, so this means that it was giving bad input; maybe the input was out of range or something, that is currently not known to us at the time of writing. But that kind of scenario could have been prevented with validation. In the case of sensors, it would be good to have redundancy, i.e. multiple sensors that we connect with, which are able to detect data differences between the sensors._

Validation is a very important topic when dealing with third-party system integration. We need to validate the data we send to third-party systems to avoid the third-party system returning errors because we sent bad data. Still, on the other hand, we also need to validate data coming in from third-party systems to ensure that it satisfies our constraints.

If we're using clean architecture, we would already have certain levels of validation at the use case layer. We would also have domain invariants in the domain layer, and then by the time we get to sending data to external systems via our infrastructure; it would already be in a valid state. That's one side; that's the sending side.

The other side, the receiving side, is in our infrastructure when we read data from third-party systems. Again, we are constructing domain entities and value objects from that data since they have domain invariants that would ensure that certain domain invariants are respected.
