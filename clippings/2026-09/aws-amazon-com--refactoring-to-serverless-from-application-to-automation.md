---
url: "https://aws.amazon.com/pt/blogs/devops/refactoring-to-serverless-from-application-to-automation/?ref=dailydev"
captured_at: "2026-09-23T18:15:35+01:00"
title: "Refactoring to Serverless: From Application to Automation | AWS DevOps & Developer Productivity Blog"
domain: "aws.amazon.com"
---
Refactoring to Serverless: From Application to Automation
by Sindhu Pillai and Gregor Hohpe on 03 JUL 2024 in Architecture, AWS Cloud Development Kit, AWS Lambda, AWS Step Functions, Best Practices, Featured, Serverless Permalink  Share

Serverless technologies not only minimize the time that builders spend managing infrastructure, they also help builders reduce the amount of application code they need to write. Replacing application code with fully managed cloud services improves both the operational characteristics and the maintainability of your applications thanks to a cleaner separation between business logic and application topology. This blog post shows you how.

Serverless isn't a runtime; it's an architecture

Since the launch of AWS Lambda in 2014, serverless has evolved to be more than just a cloud runtime. The ability to easily deploy and scale individual functions, coupled with per-millisecond billing, has led to the evolution of modern application architectures from monoliths towards loosely-coupled applications. Functions typically communicate through events, an interaction model that's supported by a combination of serverless integration services, such as Amazon EventBridge and Amazon SNS, and Lambda's asynchronous invocation model.

Modern distributed architectures with independent runtime elements (like Lambda functions or containers) have a distinct topology graph that represents which elements talk to others. In the diagram below, Amazon API Gateway, Lambda, EventBridge, and Amazon SQS interact to process an order in a typical Order Processing System. The topology has a major influence on the application's runtime characteristics like latency, throughput, or resilience.

The role of cloud automation evolves

Cloud automation languages, commonly referred to as IaC (Infrastructure as Code), date back to 2011 with the launch of CloudFormation, which allowed users to declare a set of cloud resources in configuration files instead of issuing a series of API calls or CLI commands. Initial document-oriented automation languages like AWS CloudFormation and Terraform were soon complemented by frameworks like AWS Cloud Development Kit (CDK), CDK for Terraform, and Pulumi that introduced the ability to write cloud automation code in popular general-purpose languages like TypeScript, Python, or Java.

The role of cloud automation evolved alongside serverless application architectures. Because serverless technologies free builders from having to manage infrastructure, there really isn't any "I" in serverless IaC anymore. Instead, serverless cloud automation primarily defines the application's topology by connecting Lambda functions with event sources or targets, which can be other Lambda functions. This approach more closely resembles "AaC" – Architecture as Code – as the automation now defines the application's architecture instead of provisioning infrastructure elements.

Improving serverless applications with automation code

By utilizing AWS serverless runtime features, automation code can frequently achieve the same functionality as your application code.

For example, the Lambda function below, written in TypeScript, sends a message to EventBridge:

export const handler = async (event: APIGatewayProxyEvent): Promise<APIGatewayProxyResult> => { 
    const result = // some logic
    const eventParam = new PutEventsCommand({
        Entries: [
            {
              Detail: JSON.stringify(result),
              DetailType: 'OrderCreated',
              EventBusName: process.env.EVENTBUS_NAME,
            }
          ]
    });
    await eventBridgeClient.send(eventParam);     return {
       statusCode: 200,
       body: JSON.stringify({ message: 'Order created', result }),
    };
};
TypeScript

You can achieve the same behavior using AWS Lambda Destinations, which instructs the Lambda runtime to publish an event after the completion of the function. You can configure Lambda destinations via below AWS CDK code, also written in TypeScript:

import {EventBridgeDestination} from "aws-cdk-lib/aws-lambda-destinations"

const createOrderLambda = new Function(this,'createOrderLambda', {
    functionName: `OrderService`,
    runtime: Runtime.NODEJS_20_X,
    code: Code.fromAsset('lambda-fns/send-message-using-destination'),
    handler: 'OrderService.handler',
 onSuccess: new EventBridgeDestination(eventBus)
});
TypeScript

With the AWS CDK, you can use the same programming languages for both application and automation code, allowing you to switch easily between the two.

The Lambda function can now focus on the business logic and doesn't contain any reference to message sending or EventBridge. This separation of concerns is a best practice because changes to the business logic do not run the risk of breaking the architecture and vice versa.

export const handler = async (event: APIGatewayProxyEvent): Promise<APIGatewayProxyResult> => {
    const result = //some logic
    return {
        statusCode: 200,
        body: JSON.stringify({ message: 'Order created', result }),
     };
};
TypeScript

Instructing the serverless Lambda runtime to send the event has several advantages over hand-coding it inside the application code

It decouples application logic from topology. The message destination, consisting of the type of the service (e.g., EventBridge vs. another Lambda Function) and the destination's ARN, define the application's architecture (or topology). Embedding message sending in the application code mixes architecture with business logic. Handling the sending of the message in the runtime separates concerns and avoids having to touch the application code for a topology change.
It makes the composition explicit. If application code sends a message, it will likely read the destination from an environment variable, which is passed to the Lambda function. The name of the variable that is used for this purpose is buried in the application code, forcing you to rely on naming conventions. Defining all dependencies between service instances in automation code keeps them in a central location, and allows you to use code analysis and refactoring tools to reason about your architecture or make changes to it.
It avoids simple mistakes. Redundant code can lead to mistakes. For example, debugging a Lambda function that accidentally swapped day and month in the message's date field took hours. Letting the runtime send messages avoids such errors.
Higher-level constructs simplify permission grants. Cloud automation libraries like CDK allow the creation of higher-level constructs, which can combine multiple resources and include necessary IAM permissions. You'll write less code and avoid debugging cycles.
The runtime is more robust. Delegating message sending to the serverless runtime takes care of any required retries, ensuring the message to be sent and freeing builders from having to write extra code for such undifferentiated heavy lifting.

In summary, letting the managed service handle message passing makes your serverless application cleaner and more robust. We also like to say that it becomes "serverless-native" because it fully utilizes the native services available to the application.

Refactoring to serverless-native

Shifting code from application to automation is what we call "Refactoring to Serverless". Refactoring is a term popularized by Martin Fowler in the late 90s to describe the restructuring of source code to alter its structure without changing its external behavior. Code refactoring can be as simple as extracting code into a separate method or more sophisticated like replacing conditional expressions with polymorphism.

Developers refactor their code to improve its readability and maintainability. A common approach in Test-Driven Development (TDD) is the so-called red-green-refactor cycle: write a test, which will be red because the functionality isn't implemented, then write the code to make the test green, and finally refactor to counteract the growing entropy in the codebase.

Serverless refactoring takes inspiration from this concept but augments it to the context of serverless automation:

Serverless refactoring: A controlled technique for improving the design of serverless applications by replacing application code with equivalent automation code.

Let's explore how serverless refactoring can enhance the design and runtime characteristics of a serverless application. The diagram below shows an AWS Step Functions workflow that performs a quality check through image recognition. An early implementation, shown on the left, would use an intermediate AWS Lambda function to call the Amazon Rekognition service. Thanks to the launch of Step Functions' AWS SDK service integrations in 2021, you can refactor the workflow to directly call the Rekognition API. This refactored design, seen on the right, eliminates the Lambda function (assuming it didn't perform any additional tasks), thereby reducing costs and runtime complexity.

See the AWS CDK implementation for this refactoring, in TypeScript, on GitHub.

Refactoring Limitations

The initial example of replacing application code to send a message to SQS via Lambda Destinations reveals that refactoring from application to automation code isn't 100% behavior-preserving.

First, Lambda Destinations are only triggered when the function is invoked asynchronously. For synchronous invocations, the function passes the results back to the caller, and does not invoke the destination. Second, the serverless runtime wraps the data returned from the function inside a message envelope, affecting how the message recipient parses the JSON object. The message data is placed inside the responsePayload field if sending to another Lambda function or the detail field if sending to an EventBridge destination. Last, Lambda Destinations sends a message after the function completes, whereas application code could send the message at any point during the execution.

The last change in behavior will be transparent to well-architected asynchronous applications because they won't depend on the timing of message delivery. If a Lambda function continues processing after sending a message (for example, to EventBridge), that code can't assume that the message has been processed because delivery is asynchronous. A rare exception could be a loop waiting for the results from the downstream message processing, but such loops violate the principles of asynchronous integration and also waste compute resources (Amazon Step Functions is a great choice for asynchronous callbacks). If such behavior is required, it can be achieved by splitting the Lambda function into two parts.

Can Serverless Refactoring be Automated?

Traditional code refactoring like "Extract Method" is automated thanks to built-in support by many code editors. Serverless refactoring isn't (yet) a fully automatic, 100%-equivalent code transformation because it translates application code into automation code (or vice versa). While AI-powered tools like Amazon Q Developer are getting us closer to that vision, we consider serverless refactoring primarily as a design technique for developers to better utilize the AWS runtime. Improved code design and runtime characteristics outweigh behavior differences, especially if your application includes automated tests.

Incorporating refactoring into your team structures

If a single team owns both the application and the automation code, refactoring takes place inside the team. However, serverless refactoring can cross team boundaries when separate teams develop business logic versus managing the underlying infrastructure, configuration, and deployment.

In such a model, AWS recommends that the development team be responsible for both the application code and the application-specific automation, such as the CDK code to configure Lambda Destinations, Step Functions workflows, or EventBridge routing. Splitting application and application-specific automation across teams would make the development team dependent on the platform team for each refactoring and introduce unnecessary friction.

If both teams use the same Infrastructure-as-Code (IaC) tool, say AWS CDK, the platform team can build reusable templates and constructs that encapsulate organizational requirements and guardrails, such as CDK constructs for S3 buckets with encryption enabled. Development teams can easily consume those resources across CDK stacks.

However, teams could use different IaC tools, for example, the infrastructure team prefers CloudFormation but the development team prefers AWS CDK. In this setup, development teams can build their automation on top of the CFN Modules provided by the infrastructure team. However, they won't benefit from the same high-level programming abstractions as they do with CDK.

Continuous Refactoring

Just like traditional code refactoring, refactoring to serverless isn't a one-time activity but an essential aspect of your software delivery. Because adding functionality increases your application's complexity, regular refactoring can help keep complexity at bay and maintain your development velocity. Like with Continuous Delivery, you can improve your software delivery with Continuous Refactoring.

Teams who encounter difficulties with serverless refactoring might be lacking automated test coverage or cloud automation. So, refactoring can become a useful forcing function for teams to exercise software delivery hygiene, for example by implementing automated tests.

Getting Started

The refactoring samples discussed here are a subset of an extensive catalog of open source code examples, which you can find along with AWS CDK implementation examples at refactoringserverless.com. You can also dive deeper into how serverless refactoring can make your application architecture more loosely coupled in a separate blog post.

Use the examples to accelerate your own refactoring effort. Now Go Refactor!

TAGS: AWS CDK, AWS Lambda, Best practices, Serverless
