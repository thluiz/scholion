---
url: "https://awstip.com/lets-go-serverless-b56da97b8bb6"
captured_at: "2022-07-22T16:50:44-03:00"
title: "Let’s go Serverless.. Opting for a serverless architecture… | by Asna Siji | Jun, 2022 | AWS Tip"
domain: "awstip-com"
---

# Let’s go Serverless.

Opting for a serverless architecture, minimizes lot of management and administration overhead. Does Serverless imply no servers? Nope. It simply means that the servers are managed by some one else for you.

Serverless is a cloud native execution model in which the cloud provider dynamically allocates the resources needed to execute a particular piece of code. This offers automatic scaling, built-in high availability and cost optimization with pay-per-use billing.

Let’s build a simple serverless architecture with API Gateway, Lambda functions, Dynamo DB and S3.Do more with less, let’s go serverless.

Use Case:

A URL is exposed for submitting small text documents. The payload will be scanned to get information about the document (ex:- document number and shipper details).These details will be extracted and saved in a NoSQL database. The entire message will be logged in an Object Store for later reference. A response is returned back to intimate the status of the operation. There should be provision to handle any failures during processing.

The sample architecture looks like this.

![1*aHmL21O6QyX7E0Bd9oEHGw.png](awstip-com--lets-go-serverless-aws-tip/1f54a2e633b0e6fefc0ab6ce80a44fe5.png)

1. User will be invoking URL endpoint exposed by API Gateway. Protocol is REST over HTTPS.
2. Gateway invokes a lambda function.
3. Lambda function scans the message, extracts the details and saves in Dynamo DB. Lambda logs the received message in S3 as well.
4. Exceptions during processing are pushed to an SNS topic which has a SQS queue as a subscriber. Further integrations can be added here to process the error details, notify support team etc.

Come. Let’s build.

**Step 1:**Create a DynamoDB table say DocumentTable with 2 columns, DocumentNumber and PartyDetails.

![1*LRV9xWzLG51uJlahQ9tlvw.png](awstip-com--lets-go-serverless-aws-tip/10b7f87efe9c1e3b7a777bfdfa631cca.png)

Keep all other settings as default and create the table.

**Step 2**

Create an S3 bucket to save the received message content.

![1*4trIWCL7WTNMHkzwiUVNKA.png](awstip-com--lets-go-serverless-aws-tip/2722abfac4cb4ef98e7dde9bf95136e4.png)

Create the bucket with default settings. Optionally versioning can be enabled if you wish to see multiple versions of the request with same document number.

**Step 3**

Create a service role to be assigned to the lambda function as its execution role which permits lambda to access S3, DynamoDB, CloudWatch and SNS.

Navigate to IAM -> Roles-> Create Role.

![1*34g-J6W727vurdRRRul9MQ.png](awstip-com--lets-go-serverless-aws-tip/644150a246296a9b486f804b8286381d.png)

Select Trusted entity type as ‘AWS Service’ and Common Use Case as ‘Lambda’. Click Next and in Add Permissions section, search and select the preconfigured policies provided by AWS as shown.

![1*ytrmFdVMmnfvgrvjXfWX8g.png](awstip-com--lets-go-serverless-aws-tip/f8e7adfc196c1d877c2ebb240ae724db.png)

For the purpose of this case study, let’s assign pre configured permissions which gives full access to all the required resources. But always the principle of least privilege to be maintained during actual implementation.

Lambda needs Cloud Watch permissions to upload the logs of the execution. SNS permission is needed later for handling the exception scenarios.

**Step 4**

Create an SNS Topic with default values for Exception Flows so that lambda will publish a message in case of any failures.

![1*l99LDU27np4vpIcEBYn6zw.png](awstip-com--lets-go-serverless-aws-tip/6cae34e245ef5accff24669798510dc3.png)

**Step 5**

Create a SQS queue as a subscriber to the above topic so that error messages can be polled for taking any action later.

![1*RDxeYQDNDErju_RxQX1tfg.png](awstip-com--lets-go-serverless-aws-tip/7d38f5d711aaf985859e3f4ec1ee1be0.png)

After creating the queue, subscribe to the previously created topic by clicking the highlighted button.

![1*5KcAsZsuGqlP_eUwOy2ftw.png](awstip-com--lets-go-serverless-aws-tip/18e13d9868bab58323397f007223b882.png)

Navigate to the Access Policy tab and you can now see that a policy is added which permits the SNS Topic to send the message to queue.

Under the Subscriptions section of the SNS topic, the SQS queue will be listed. Ensure that Raw message delivery is turned on to see the message as is. When you enable raw message delivery for SQS, any Amazon SNS metadata is stripped from the published message and the message is sent as is.

![1*u021oTr1oTTzugz1QXYXAg.png](awstip-com--lets-go-serverless-aws-tip/a9712ce9e23bcc443bff01abd003ff7c.png)

Create the lambda function. Navigate to the Lambda console and create the function with Node.js as runtime.

![1*n_LaXfRxHdw5Ru9GPopldw.png](awstip-com--lets-go-serverless-aws-tip/576aac8956189ea4e5ee155a4faaa50c.png)

*Change default execution role to the existing role and select the previously created role in Step 3.*

![1*hjeIO8PAfOZowj53vZv2mA.png](awstip-com--lets-go-serverless-aws-tip/dc1e116b2cbde2d532f29345798a8934.png)

Under the ‘Code’ tab, replace the contents of the index.js file with the index.js file from GitHub repo after making necessary modifications. <https://github.com/asnakhader/aws-serverless>

Points to Note:

1. All the initialization and reusable components can be kept before the handler function. For ex:-Database Configuration and connection settings. Reason: Any variable outside the handler function will be frozen in between Lambda invocations and possibly reused. So all the variables can be placed inside the handler.

*var dynamoDB = new AWS.DynamoDB();*

*const tableName = “DocumentTable”;*

2. Environment Variables  
An environment variable is a pair of strings that is stored in a function’s configuration. You can use environment variables to adjust your function’s behavior without updating code. The Lambda runtime makes environment variables available to your code.  
Lets keep the code to be extracted from the text message as an environment variable. Navigate to Configuration -> Environment Variables and click ‘Edit’.

![1*xTX3C7LPS1RdO-zNmm5Png.png](awstip-com--lets-go-serverless-aws-tip/0f8ef8075fbd7574c05d48bbe9674ac9.png)

The function logic will scan for the occurrence of this parameters and extract it and save in DynamoDB.

*//extraction parameters   
 let param1 = process.env.PARAM1;  
 let param2 = process.env.PARAM2;*

If the parameters are not found in the received message, an error response will be sent back. Also, the function supports HTTP Post method. Invocation with any other request type will result in error.

3. Exception Flows

Lambda supports adding Destinations to handle success / failure scenarios for asynchronous invocation. Since we are using API Gateway to invoke lambda, this can not be used. However, we can programmatically push to SNS topic on failures.

3. Test the function

Under the ‘Test’ tab, create a test event. A sample payload with message body and request method is provided below.

We have configured parameters as ‘DocNum’ and ‘Shipper’. Run the test and details of the execution are listed.

![1*Js60ylBy98yAByOTw2GldA.png](awstip-com--lets-go-serverless-aws-tip/e4d5aa62e1c26ddb9cf2db7130e3cd6e.png)

**Step 8**

Create a Trigger for Lambda and select API Gateway . Choose API Type as REST and Security as ‘Open’.

![1*ejJRzP5fs1K02WD0p_TG3Q.png](awstip-com--lets-go-serverless-aws-tip/0e92ddaa3deaea5f7742f7e6bbcb9f48.png)

**Step 9**

Test the setup. You can use any software / plugin of your choice. I have installed Talend API tester which is a light weight Chrome plugin.

![1*vFS88Zf7Qx0usJaU_RK6oA.png](awstip-com--lets-go-serverless-aws-tip/8303bbe22e00beca5bc3eeb2434b8f53.png)

API gateway provides a URL invocation point. Copy the URL and configure the request parameters.

![1*LRDwZ5nl-NYDdrptWfizLg.png](awstip-com--lets-go-serverless-aws-tip/659fff0df0da5f2060ee13774cb32b23.png)

Sample payload given below.

You may notice slight difference in the test data used directly to test the function and below payload. This is because the tool will add the necessary tags like ‘header’ / ‘body’ etc.

Yay! Results are displayed and invocation is success.

![1*q9FEbqOW21mSkSEwi8sY_w.png](awstip-com--lets-go-serverless-aws-tip/f2d5d2dbc71b19100f5e27262b871210.png)

Navigate to S3 bucket to see the message logged.

![1*q3O2c9vQUshOaAfP0JktLQ.png](awstip-com--lets-go-serverless-aws-tip/03db723061916dd38614cc1c76d2fdb6.png)

Navigate to DynamoDB and record is created.

![1*rixl_MtWtx4JTG7Y8vmHdg.png](awstip-com--lets-go-serverless-aws-tip/06fd136d9d6a278922662bc473ce258d.png)

We can see that lambda invocation details are logged in CloudWatch as well.

Note : Using the same payload again will rewrite the data as DocumentNumber is used as the key in DynamoDB and S3.

Lets test the function for a failure. Invoke the function with ‘PUT’ method. Error response is returned. We are expecting the function to push a message to SNS.

![1*JKC1lVzq4zBR41UrJrmpqA.png](awstip-com--lets-go-serverless-aws-tip/76e088f939267e1aece662b0f696512d.png)

Navigate to SQS and poll for messages. The status of the polling is displayed and messages are getting listed.

![1*uiVhtuUUW9eEkb4O0LMGIg.png](awstip-com--lets-go-serverless-aws-tip/bda0616a15fe4332cd7541267f3d8f27.png)

Click on the latest message to view the details of the error.

![1*p8s7ntLcV-lApeUHczo_wg.png](awstip-com--lets-go-serverless-aws-tip/613688b2aa9b227196a8609f18a312ba.png)

This can be used for further integrations like executing another lambda function / notifying support etc.

We have successfully completed a simple serverless architecture with persistence and exception layers in very less time. That’s cool.

Do more with less. Let’s go Serverless!!
