variable "lambda_function_name" {
  description = "Name of the Lambda function"
  default     = "ebs_snapshot_backup"
}

variable "notification_email" {
  description = "Email address to receive SNS alerts"
  default     = "your-email@example.com"  # ✅ Replace this with your real email!
}

variable "schedule_expression" {
  description = "Cron-style schedule for EventBridge trigger"
  default     = "rate(24 hours)"
}