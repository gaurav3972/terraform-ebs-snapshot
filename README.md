# 🌌 Automated Multi-Region EBS Snapshot Backup Using Lambda & Terraform

## 📘 Project Description:

This project delivers a **robust, scalable, and fully automated solution** for backing up Amazon Elastic Block Store (EBS) volumes across **all available AWS regions**. It leverages the power of **AWS Lambda** (serverless computing), **Amazon EventBridge** (for scheduling), **Amazon SNS** (for notifications), and **Terraform** (for Infrastructure as Code) to achieve seamless, repeatable, and multi-region snapshot automation.

The core functionality is driven by a Python-based Lambda function that dynamically discovers EBS volumes in an "in-use" state across every AWS region, and creates snapshots for each. These snapshots are **tagged with metadata** for easier tracking and organization. The entire workflow is scheduled to run at user-defined intervals using EventBridge rules, and the result of each run is emailed to administrators via Amazon SNS.

This system is ideal for cloud engineers, DevOps teams, and system administrators looking to automate disaster recovery, reduce manual workload, and achieve consistent daily backups for business-critical infrastructure.
![](https://github.com/gaurav3972/terraform-ebs-snapshot/blob/main/IMAGES/1.00.png)
---

## ✅ Key Features:

* 📦 **Fully Automated Snapshot Creation**: Creates EBS snapshots for all "in-use" volumes across all AWS regions.
* ⚙️ **Infrastructure as Code with Terraform**: Easily replicable deployments with a single command.
* ⏱ **EventBridge Rule-Based Scheduling**: Execute Lambda automatically every 24 hours or on a custom schedule.
* 📢 **SNS Integration**: Email notifications to keep stakeholders informed of backup status.
* ☁️ **Serverless Architecture**: No EC2 required; completely Lambda-powered.
* 🔒 **IAM with Least Privilege Access**: Secure execution with fine-grained permissions.
* 🌐 **Multi-Region Awareness**: Ensures no volume is left behind, regardless of AWS region.
* 🏑 **Cost-Efficient & Scalable**: Pay-per-execution with zero idle cost.

---

## 🧱 Use Case Scenarios:

* Organizations needing **cross-region EBS backups** for resilience
* **DevOps teams** enforcing snapshot policies
* **Disaster Recovery** and **Business Continuity Planning**
* Cloud environments requiring **zero-touch** daily backups

---

## 🧰 Project Architecture:

```bash
ebs-snapshot-backup/
├── lambda_function.py          # Python logic for multi-region snapshot creation
└── terraform/
    ├── main.tf                 # Defines Lambda, IAM, SNS, EventBridge
    ├── variables.tf            # Parameterizes region, email, schedule
    ├── outputs.tf              # Outputs like Lambda name, SNS topic ARN
    └── lambda_function.zip     # Zipped Lambda function deployed to AWS
```

---

## 🔧 Technologies Used:

* 🖥️ **AWS Lambda** – Stateless function execution for snapshot logic
* 🌐 **Amazon EventBridge (CloudWatch Events)** – CRON scheduler
* 📧 **Amazon SNS** – Email delivery for job results
* 📁 **Amazon EBS** – Persistent storage to be backed up
* 🔐 **IAM Policies & Roles** – Security and access control
* 📚 **Terraform** – Infrastructure management via code
* 🧙‍♂️ **Python 3.12** – Lambda runtime environment

---

## 📊 Learning Objectives:

* Understand how to build **serverless automation** with AWS Lambda
* Learn to use **Terraform** for provisioning AWS resources
* Implement **event-driven** architecture using **EventBridge**
* Send **automated alerts** using Amazon SNS
* Write Python code to **discover resources dynamically** across AWS regions
* Master **multi-region awareness** and backup strategies

---

## 🚀 Features Recap

* ⚙️ 100% automated deployment and backup lifecycle
* 🌎 Coverage of **all AWS regions** for max redundancy
* ⏰ Snapshot scheduling with **CRON expressions**
* 📧 Email summary after every backup run
* ✅ Clean and tagged snapshots for traceability

---

## 💪 Benefits

* ⚡ Fast deployment using **Terraform scripts**
* 🧠 Set it and forget it — once deployed, no manual intervention
* 🛡️ Strong access control via IAM
* 🚨 Notifications reduce uncertainty in automation
* 💎 Enterprise-ready solution

---

## 🚧 Deployment Guide

### 1. Prerequisites

* Terraform (v1.3+)
* AWS CLI configured with permissions
* Python 3.x
* An active email address (for notifications)

### 2. Prepare Lambda Function

Inside `ebs/`, create your Python snapshot function named `lambda_function.py`. Then zip it:

```bash
zip lambda_function.zip lambda_function.py
mv lambda_function.zip terraform/
```

### 3. Configure Variables

Edit the file `terraform/variables.tf`:

```hcl
variable "aws_region" {
  description = "Primary AWS region"
  default     = "us-east-1"
}

variable "lambda_function_name" {
  default = "ebs_snapshot_backup"
}

variable "notification_email" {
  default = "your-email@example.com"
}

variable "schedule_expression" {
  default = "rate(24 hours)"
}
```

### 4. Deploy via Terraform

```bash
cd terraform
terraform init
terraform plan
terraform apply
```

> Confirm with "yes" when prompted.

### 5. Confirm SNS Subscription

Go to your email and **confirm the SNS subscription** link sent by AWS.

### 6. Validation

* Lambda: Check logs in CloudWatch after execution
* Snapshots: Open EC2 > Snapshots in AWS Console
* Email: Verify backup notification email
* EventBridge: Confirm scheduling rule is active

---

## 📅 Schedule Customization

In `variables.tf`, change `schedule_expression` to:

```hcl
default = "cron(0 3 * * ? *)" # every day at 3 AM UTC
```

---

## 📄 Project Summary

This project offers a **complete, hands-free solution** for **daily multi-region EBS volume backups**, making use of modern, scalable, and cost-effective AWS services.

It’s an excellent blueprint for **serverless architecture** and IaC practices, useful for any production-grade cloud deployment. From **infrastructure provisioning** with Terraform to **Python Lambda automation** to **real-time notifications**, every part of the pipeline is designed with **reliability**, **scalability**, and **security** in mind.

---

## 📈 Future Enhancements

* Integrate snapshot **lifecycle policies**
* Add support for **tag-based volume filtering**
* Export snapshot reports to **S3 or DynamoDB**
* Add **Slack or Teams notifications**

---

## 📑 License

MIT License © 2025 gaurav3972

---

