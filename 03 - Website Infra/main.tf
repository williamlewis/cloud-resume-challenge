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

provider "archive" {}

data "archive_file" "zip" {
  type        = "zip"
  source_file = "lambda_update_view_count_in_dynamodb.py"
  output_path = "update_view_count.zip"
}

# --------------------------------------
# ////////       DynamoDB       ////////
# --------------------------------------

# Table
resource "aws_dynamodb_table" "view-count-table" {
  name           = "view-count-table"
  billing_mode   = "PROVISIONED"
  read_capacity  = 20
  write_capacity = 20
  hash_key       = "count_id" # Partition key

  attribute {
    name = "count_id"
    type = "S" # Partition key data type
  }
}


# Table Item
resource "aws_dynamodb_table_item" "total-views" {
  depends_on = [
    aws_dynamodb_table.view-count-table
  ]
  table_name = aws_dynamodb_table.view-count-table.name
  hash_key   = aws_dynamodb_table.view-count-table.hash_key

  item = <<ITEM
{
  "count_id": {"S": "total_views"},
  "current_count": {"N": "1"}
}
ITEM
}


# ------------------------------------
# ////////       Lambda       ////////
# ------------------------------------

# Lambda Execution Role
resource "aws_iam_role" "iam_for_lambda" {
  name = "iam_for_lambda_dynamodb"

  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": "sts:AssumeRole",
      "Principal": {
        "Service": "lambda.amazonaws.com"
      },
      "Effect": "Allow",
      "Sid": ""
    }
  ]
}
EOF
}

# Function
resource "aws_lambda_function" "lambda-tf-test-function" {
  function_name = "lambda-tf-test-function"

  filename         = data.archive_file.zip.output_path #"update_view_count.zip"
  source_code_hash = data.archive_file.zip.output_base64sha256

  role    = aws_iam_role.iam_for_lambda.arn
  handler = "lambda_update_view_count_in_dynamodb.lambda_handler"
  runtime = "python3.9"

  environment {
    variables = {
      TABLE_NAME = aws_dynamodb_table.view-count-table.id # reference name of dynamodb table
    }
  }
}


# # -----------------------------------------
# # ////////       API Gateway       ////////
# # -----------------------------------------

# # REST API
# resource "aws_api_gateway_rest_api" "" {
#     #
# }
