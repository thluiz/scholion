---
title: "Semantic equivalence and support for default retry strategies"
date: '2026-11-25T16:21:42+00:00'
category: webclip
summary: 'Explains how AWS uses client request identifiers and semantically equivalent responses to make retries idempotent and invisible when using the SDK and CLI.'
tags: ["idempotency", "aws-sdk", "retry-strategies"]
has_commentary: false
generated_by: "openai/gpt-5.1"
sources:
  - title: "references-details-empty"
    url: "https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/aws-amazon-com--semantic-equivalence-and-idempotent-retries.md"
    kind: repo
---

The text describes an approach where a service returns a semantically equivalent response for every request that uses the same unique client request identifier within some interval. This allows safe retries with default policies, as used in the AWS SDK, because any retried call with the same identifier has the same meaning as the original successful call. The example given is the Amazon EC2 RunInstances API invoked from the AWS CLI, where a ClientToken acts as the unique request identifier and enables idempotent behavior.

## Reading notes

- A strategy for safe retries is to ensure that, for a given unique request identifier, any subsequent response within a time window carries the same meaning as the first successful response.
- With this strategy, a caller that retries the same operation using the same unique client request identifier receives a response that is semantically equivalent to the original one.
- This behavior is particularly useful for improving customer experience when applying automatic retries to operations that encounter server-side faults, similar to the default retry policies in the AWS SDK.
- The Amazon EC2 RunInstances API with the AWS CLI illustrates idempotency using semantically equivalent responses combined with automated retry logic.
- In the example, the user runs `aws ec2 run-instances` without explicitly providing a client request identifier, yet the response includes a ClientToken field.
- Many AWS API operations represent the unique client request identifier using the ClientToken field.
- When a caller does not provide a unique identifier, the AWS CLI generates one and the remote service echoes this value back in the ClientToken field of the response.
- The generated ClientToken allows retries to occur transparently in the presence of transient upstream service faults.
- A follow-up request made later with the same ClientToken produces a response that is similar to the first one, though some fields reflect the updated instance state.
- In the retried RunInstances example, the instance state fields change from "pending" to "running", including updated status code and message values.
- Although individual fields differ between the initial and retried responses, both responses represent the same underlying effect of having a running instance associated with that request identifier.
- The AWS SDK and AWS CLI use this idempotent behavior when it is available to streamline the user experience.
- These tools track which operations support an idempotent contract and automatically generate a unique client request identifier if the caller does not include one.
- The same generated identifier is reused on retries so that the service can recognize repeated attempts for the same logical request.
- By reusing the client request identifier, the system upholds an "at most once" commitment for the operation associated with that identifier.
- Because retried responses are semantically equivalent to the original, client code using the SDK or CLI does not need to manage retry logic explicitly and can simply consume the final response it receives.
