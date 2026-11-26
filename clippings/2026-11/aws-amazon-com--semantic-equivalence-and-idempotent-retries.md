---
url: "https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/"
captured_at: "2026-11-25T16:21:42+00:00"
title: "references-details-empty"
domain: "aws-amazon-com"
---

### Semantic equivalence and support for default retry strategies

An alternative is to deliver a semantically equivalent response in every case for the same unique request identifier for some interval. This means that any subsequent response to a retry request from the same caller with the same unique client request identifier will have the same meaning as the first response returned for the first successful request. This approach has some really useful properties—especially where we want to improve the customer experience by safely and simply retrying operations that experience server-side faults, just as we do with the AWS SDK through default retry policies.

We can see an example of idempotency with semantically equivalent responses and automated retry logic in action when we use the Amazon EC2 RunInstances API operation and the AWS Command Line Interface (CLI). Note that the AWS CLI (like the AWS SDK) [supports a default retry policy](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-retries.html), which we are using here. In this example, we launch an EC2 instance using the following AWS CLI command:

```
$ aws ec2 run-instances --image-id ami-04fcd96153cb57194 --instance-type t2.micro  
```

```
{ 
```

```
    "Instances": [ 
```

```

```

        "Monitoring": { 

            "State": "disabled"

        },

        "StateReason": {

             "Message": "pending",

             "Code": "pending"

        },

        "State": {

              "Code": 0

              "Name": "pending"

         },

        "InstanceId": "i-xxxxxxxxxxxxxxxxx",

        "ImageId": "ami-04fcd96153cb57194",         

        …

        "ClientToken": "eb3c3141-a229-4ca0-b005-eb922e2cabdc",

        …                                                                                                                                                                                                                                       "ClientToken": "eb3c3141-a229-4ca0-b005-eb922e2cabdc",                                                                                                                                                                                                                           …                                                                                                                                                                                                                                                                                    "Instances": \[                                                                                                                                                                                                                                                                       {                                                                                                                                                                                                                                                                                    "Monitoring": {                                                                                                                                                                                                                                                                      "State": "disabled"                                                                                                                                                                                                                                                          },                                                                                                                                                                                                                                                                               "StateReason": {                                                                                                                                                                                                                                                                     "Message": "pending",                                                                                                                                                                                                                                                            "Code": "pending"                                                                                                                                                                                                                                                            },                                                                                                                                                                                                                                                                               "State": {                                                                                                                                                                                                                                                                           "Code": 0,                                                                                                                                                                                                                                                                       "Name": "pending"                                                                                                                                                                                                                                                            },                                                                                                                                                                                                                                                                               "InstanceId": "i-xxxxxxxxxxxxxxxxx",                                                                                                                                                                                                                                             "ImageId": "ami-04fcd96153cb57194",             …                                                                                                                                                                                                                                              "ClientToken": "eb3c3141-a229-4ca0-b005-eb922e2cabdc",                                                                                                                                                                                                                           …

In many AWS API operations, the unique client request identifier is modeled by the ClientToken field. Note that we didn’t provide a unique client request identifier in our request. The ClientToken property in the response is echoed back by the remote service. This is because the AWS CLI will generate a unique ID for the request if an identifier is not provided, which allows retries to happen “under the hood” in the event of a transient upstream service fault. An example of what a retried request/response might look like can be simulated by waiting a few minutes and then making another request using the AWS CLI and the same ClientToken that was returned in the previous request. It’s important to note that the response returned is very similar but not identical to the first response:

$ aws ec2 run-instances --image-id ami-04fcd96153cb57194 --instance-type t2.micro 

```
--client-token eb3c3141-a229-4ca0-b005-eb922e2cabdc 
```

```
{ 
```

```
    "Instances": [ 
```

```
        { 
```

```
            "Monitoring": { 
```

```
                "State": "disabled" 
```

```
            }, 
```

```
            "StateReason": { 
```

```
                "Message": "running",  Now running 
```

```
                "Code": "running"  Now running 
```

```
            }, 
```

```
            "State": { 
```

```
                "Code": 16,  Now running status code 
```

```
                "Name": "running"  Now running 
```

```
        }, 
```

```
        "InstanceId": "i-xxxxxxxxxxxxxxxxx", 
```

```
        "ImageId": "ami-04fcd96153cb57194", 
```

```
        … 
```

```
        "ClientToken": "eb3c3141-a229-4ca0-b005-eb922e2cabdc", 
```

```
        …                                                                                                                                                                                                                                       "ClientToken": "eb3c3141-a229-4ca0-b005-eb922e2cabdc",                                                                                                                                                                                                                           …
```

The AWS SDK and AWS CLI leverage this behavior whenever it’s available to simplify the experience of the customer using these tools. Our SDK and CLI are aware of which operations support an idempotent contract, and they will generate a unique client request identifier and add it to the request if one is not provided by the caller. This generated identifier is then reused in the event of a retry, thus ensuring we meet the “at most once” commitment for the request. Because the response (even on a retry) is semantically equivalent, the calling client code can be completely unaware of any retries that happen within the SDK code and simply deal with the response when it is received.
