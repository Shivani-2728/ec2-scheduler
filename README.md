# EC2 Start/Stop Scheduler

Automated EC2 instance scheduler using AWS Lambda and EventBridge that starts and stops instances automatically based on a schedule.

## What This Does

Instead of manually starting and stopping EC2 instances every day, this project automates it completely. Instances stop automatically at 6PM IST every evening and start again at 9AM IST every morning without any manual intervention.

## Why I Built This

Shutting down unused EC2 instances during non-business hours is one of the most common cost optimization practices in cloud operations. This project automates that process entirely through code.

## Architecture

EventBridge Schedule → Lambda Function → EC2 Instance

## Tools Used

- AWS Lambda
- Amazon EventBridge
- AWS IAM
- Amazon CloudWatch
- Python 3.14
- boto3
- Git and GitHub

## How It Works

Stop Schedule runs at 6PM IST every day and triggers the stop Lambda function which finds all running EC2 instances tagged with Environment=Learning and stops them automatically.

Start Schedule runs at 9AM IST every day and triggers the start Lambda function which finds all stopped EC2 instances tagged with Environment=Learning and starts them automatically.

## Skills Demonstrated

AWS Lambda · EventBridge
