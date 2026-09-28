---
title: "How to Create a Lambda Function with Python and CockroachDB Serverless"
date: '2022-03-27T19:10:08-03:00'
category: webclip
summary: 'Tutorial showing how to create an AWS Lambda function in Python, package it with psycopg2, configure AWS access, connect it to a CockroachDB Serverless cluster, deploy it, and verify it by invoking the function.'
tags: ["aws-lambda", "python", "cockroachdb-serverless", "serverless"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "How to Create a Lambda Function with Python and CockroachDB Serverless"
    url: "https://www.cockroachlabs.com/blog/aws-lambda-function-python-cockroachdb-serverless/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2022-03/cockroachlabs-com--how-to-create-a-lambda-function-with-python-and-cockroachdb-.md"
    kind: repo
---

The page walks through building and deploying a Python AWS Lambda function that connects to a CockroachDB Serverless cluster. It assumes some Python and command-line familiarity, then explains how to set up AWS, create an IAM user and execution role, prepare the deployment package, configure environment variables, and invoke the function to create sample account rows in the database.

## Reading notes

- The tutorial is for an AWS Lambda function written in Python that uses CockroachDB Serverless as its database.
- It notes that serverless compute still depends on serverless storage if you want to avoid thinking about servers altogether.
- The sample code includes `create_accounts()` and `lambda_handler()` in `init_db.py`.
- `create_accounts()` connects to CockroachDB Serverless, creates an `accounts` table, and inserts `n` rows.
- The sample data uses UUIDs for `id` and randomized six-digit integers for `balance`.
- `lambda_handler()` creates the connection pool and calls `create_accounts()` with `5` as the number of accounts.
- The tutorial uses AWS account setup, IAM user creation, and the AWS CLI.
- It requires saving the AWS Access Key ID and Secret Access Key for later CLI configuration.
- It instructs creating a CockroachDB Cloud account and a Serverless cluster.
- The connection string from CockroachDB Cloud is copied for later use.
- The sample Python code is cloned from GitHub.
- A deployment package is built with `psycopg2-binary`, `init_db.py`, and `root.crt`.
- AWS is configured with `aws configure` using the IAM user credentials.
- An execution role named `lambda-ex` is created and attached to `AWSLambdaBasicExecutionRole`.
- The function is deployed with `aws lambda create-function`.
- The deployment sets `DATABASE_URL` and `PGSSLROOTCERT` as environment variables.
- The function is invoked from the command line with `aws lambda invoke`.
- The log output shows five accounts being created and the database initialized.
- The page then shows how to confirm the table exists in CockroachDB Cloud.
- It also offers an optional check using the CockroachDB SQL shell and a `SELECT * FROM accounts;` query.
- The closing note says the next likely steps are to make the function more useful and add an automatic Lambda trigger.
