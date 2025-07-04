# AWS Automated Threat Detection & Response

This project uses **AWS CloudTrail**, **EventBridge (CloudWatch Events)**, **Lambda**, and **SNS** to detect suspicious activity—specifically **root account console logins**—and automatically send alerts.

## What It Does

Monitoring root login activity is critical in any secure AWS environment. This project showcases how to automate that process and demonstrates:

- AWS-native threat detection (EventBridge + CloudTrail)
- Real-time alerting (SNS)
- Lambda-based automation

---

## Architecture

Root Console Login > CloudTrail logs event > EventBridge > Lambda Function triggered > SNS sends alert email

## Tech Stack

- AWS CloudTrail
- AWS EventBridge (CloudWatch Events)
- AWS Lambda (Python 3.12)
- AWS SNS
- IAM Roles

## Setup Instructions

1. Enable CloudTrail with logging to CloudWatch Logs.
2. Create an SNS topic and confirm email subscription.
3. Create Lambda function:
   - Paste code from `lambda_function.py`
   - Set `SNS_TOPIC_ARN` environment variable
4. Create EventBridge rule:
   - Use pattern from `event_pattern.json`
   - Set Lambda as the target

## Screenshots

### 1. SNS Email

Shows the email alert sent to my inbox

![SNS Email](Screenshots/sns-email.png)

---

### 2. Lambda Logs

Shows the Lambda Logs in AWS Console

![Lambda Logs](Screenshots/lambda-logs.png)

---

### 3. CloudTrail Event

Shows the CloudTrail Event

![CloudTrail Event](Screenshots/cloudtrail-event.png)

## Further Automation

A .yaml script is included in this repo that can be run from AWS CLI to automatically recreate all aspects of this project.