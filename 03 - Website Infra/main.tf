terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "4.49.0"
    }
  }
}

provider "aws" {
    region = "us-east-1"
}

# --------------------------------
# ////////       S3       ////////
# --------------------------------

# Bucket
resource "aws_s3_bucket" "tf-crc-bucket" {
    bucket = "wlewis-tf-cloud-resume-challenge"
}

# Bucket Policy
resource "aws_s3_bucket_policy" "tf-crc-bucket-policy" {
    # S3 Bucket Policy?
    bucket = aws_s3_bucket.tf-crc-bucket.id
    policy = data.aws_iam_policy_document.tf-crc-bucket-policy-text.json
}

# Bucket Policy (JSON Data)
data "aws_iam_policy_document" "tf-crc-bucket-policy-text" {
#   statement {
#     principals {
#       type        = "AWS"
#       identifiers = ["123456789012"]
#     }

#     actions = [
#       "s3:GetObject",
#       "s3:ListBucket",
#     ]

#     resources = [
#       aws_s3_bucket.example.arn,
#       "${aws_s3_bucket.example.arn}/*",
#     ]
#   }
}


# ----------------------------------------
# ////////       CloudFront       ////////
# ----------------------------------------

# Distribution
resource "aws_cloudfront_distribution" "" {
    #
}


# --------------------------------------
# ////////       Route 53       ////////
# --------------------------------------

# Hosted Zone
resource "aws_route53_zone" "" {
    #
}

# DNS Record(s)
resource "aws_route53_record" "" {
    #
}


# -------------------------------------------------
# ////////       Certificate Manager       ////////
# -------------------------------------------------

# SSL Certificate
resource "aws_acm_certificate" "" {
    #
}

# Issued SSL Certificate
data "aws_acm_certificate" "" {
    #
}


# ------------------------------------
# ////////       DynamoDB       ////////
# ------------------------------------

# Table
resource "aws_dynamodb_table" "" {
    #
}

# Table Item
resource "aws_dynamodb_table_item" "" {
    #
}


# ------------------------------------
# ////////       Lambda       ////////
# ------------------------------------

# Function
resource "aws_lambda_function" "" {
    #
}

# IAM Role for Lambda?
resource "aws_iam_role" "" {
    #
}


# -----------------------------------------
# ////////       API Gateway       ////////
# -----------------------------------------

# REST API
resource "aws_api_gateway_rest_api" "" {
    #
}
