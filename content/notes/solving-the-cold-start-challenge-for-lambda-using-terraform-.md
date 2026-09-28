---
title: "Solving the Cold Start Challenge for Lambda Function Using Terraform Cloud"
date: '2022-06-12T08:47:17-03:00'
category: webclip
summary: 'The post shows a Terraform setup for an AWS Lambda function with an S3 deployment artifact, reserved concurrency, and provisioned concurrency through an alias to reduce cold starts.'
tags: ["aws", "lambda", "terraform", "cold-start"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Solving the Cold Start Challenge for Lambda Function Using Terraform Cloud - DEV Community"
    url: "https://dev.to/pedramha/solving-the-cold-start-challenge-for-lambda-function-using-terraform-cloud-1o2m?s=09"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2022-06/dev-to--solving-the-cold-start-challenge-for-lambda-using-terraform-.md"
    kind: repo
---

The post walks through a Terraform setup for an AWS Lambda function and focuses on reducing cold starts. It uses an S3 bucket for the deployment artifact, sets reserved concurrency, and adds provisioned concurrency through an alias. The author also notes that provisioned concurrency has a cost because AWS keeps a warm instance available.

## Reading notes

- Start from an empty directory with main.tf, variables.tf, output.tf, and terraform.auto.tfvars.
- Configure the AWS provider for eu-central-1 and avoid placing credentials in the file.
- Use random_pet to create a unique private S3 bucket for the Lambda package.
- Use archive_file to zip the source code before uploading it to S3.
- Create an aws_s3_bucket_object for the deployment artifact and point the Lambda to that object.
- Set reserved_concurrent_executions on the Lambda to keep concurrency predictable.
- Add an aws_lambda_alias and an aws_lambda_provisioned_concurrency_config to use provisioned concurrency.
- Define a basic IAM role that lets Lambda assume the execution role.
- Put function name, paths, runtime, handler, concurrency values, and version in variables.tf.
- Set src_path and target_path in terraform.auto.tfvars.
- Provide a simple Node.js handler that returns a date and the message Terraform is awesome!.
- Deploy with terraform apply -auto-approve or use Terraform Cloud for GitOps.
- The post links to a GitHub repository and a Terraform Cloud guide for GitHub-based workflows.
