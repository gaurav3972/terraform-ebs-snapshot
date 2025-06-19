# EBS-Backup-Automation-via-Terraform
# Automated Multi-Region EBS Snapshot Backup Using Lambda & Terraform
## 📘 Project Description:

This project provides a **fully automated solution** to create EBS volume snapshots **across all AWS regions**, using a **Python-based Lambda function**, **Terraform** for infrastructure provisioning, and **SNS + EventBridge** for notifications and scheduling. It improves disaster recovery, reduces manual effort, and ensures daily backups of active volumes.

---

## ✅ Key Features:

* 📦 **Automated Daily Snapshots** of all “in-use” EBS volumes across **all AWS regions**.
* ⚙️ **Infrastructure as Code** using **Terraform** – fast and repeatable deployments.
* 🔁 **EventBridge Scheduler** triggers Lambda every 24 hours (or custom CRON).
* 🔔 **SNS Integration** sends email notifications when the snapshot process runs.
* ☁️ **Serverless & Scalable**: No EC2 used; runs via AWS Lambda.
* 🔒 **IAM Role Management** with least privilege access policies.
* 🌐 **Multi-Region Support** for complete AWS volume coverage.

---

## 🧱 Project Architecture:

```bash
ebs-snapshot-backup/
├── lambda_function.py          # Python code to create snapshots
└── terraform/
    ├── main.tf                 # Terraform resources: Lambda, IAM, SNS, EventBridge
    ├── variables.tf            # All customizable variables
    ├── outputs.tf              # Output important values like Lambda name, SNS ARN
    └── lambda_function.zip     # Zipped Lambda code for deployment
```

---

## 🔧 Technologies Used:

* 🖥️ **AWS Lambda** – Runs the snapshot automation logic
* 🌍 **AWS CloudWatch EventBridge** – Triggers Lambda daily
* 📩 **AWS SNS** – Sends email notifications
* 🛢️ **Amazon EBS** – Volumes whose snapshots are taken
* 🔐 **IAM Roles & Policies** – For secure Lambda execution
* 🧪 **Python 3.12** – For Lambda function
* 🛠️ **Terraform** – For end-to-end infrastructure automation
---

## 📈 Learning Objectives:

* How to deploy **serverless automation** on AWS
* Use **Terraform** to provision Lambda, IAM, SNS, and EventBridge
* Create **CRON-based automation** using EventBridge rules
* Work with **multi-region AWS service discovery and iteration**

## ✅ Features

- ⚙️ **Fully automated** via Terraform IaC
- 🌍 **Multi-region** snapshot across ALL AWS regions
- 📅 **Scheduled daily** backups using EventBridge
- 📧 **Email alerts** via SNS after every run
- 🛡️ **Tagged snapshots** for easy management
---

## 🚀 Deployment Guide

## 1. Prerequisites

- **Terraform** v1.3+ installed
- **AWS CLI** configured (`aws configure`)
- **Python 3.x** installed
- **Email address** for SNS notifications

---

## 2. Create and Zip Lambda Code

In `ebs/` directory, create `lambda_function.py` with snapshot logic, then run:

```bash
zip lambda_function.zip lambda_function.py
````

Move the ZIP into the Terraform module:

```bash
mv lambda_function.zip terraform/
```

---

## 3. Configure Terraform Variables

Edit `terraform/variables.tf`:

```hcl
variable "aws_region" {
  description = "Primary AWS region"
  default     = "us-east-1"
}

variable "lambda_function_name" {
  default = "ebs_snapshot_backup"
}

variable "notification_email" {
  default = "you@example.com"  # <-- Replace with your email
}

variable "schedule_expression" {
  default = "rate(24 hours)"
}
```

---

## 4. Deploy Infrastructure

```bash
cd terraform
terraform init
terraform plan    # validate changes
terraform apply   # type "yes" to confirm
```

---

## 5. Confirm Email Subscription

AWS will send a confirmation to your email—click the link to complete SNS subscription.

---

## 6. Verify Operation

* ✅ **Lambda**: Check your AWS Console → Lambda
* ✔ **EventBridge**: Confirm rule is scheduled
* 📂 **EC2 Snapshots**: Look for new backups in all regions
* 📧 **Email Alerts**: Watch for summary after snapshot runs
---

## 📄 **Project Summary**

The **Automated Multi-Region EBS Snapshot Backup** project is a **fully serverless AWS backup solution** that uses **AWS Lambda**, **Terraform**, **EventBridge**, and **SNS** to automatically create snapshots of all "in-use" EBS volumes across **every AWS region**.

The project is written in **Python** and deployed entirely using **Terraform**, ensuring repeatable, reliable, and hands-free infrastructure setup. Snapshots are created daily, and **email notifications** are sent to keep administrators informed.

This project enhances **disaster recovery**, simplifies backup operations, and requires **no EC2 instances or manual intervention**.

---

