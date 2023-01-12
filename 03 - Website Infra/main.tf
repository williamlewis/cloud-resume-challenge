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


# # Table Item
# resource "aws_dynamodb_table_item" "" {
#     #
# }


# # ------------------------------------
# # ////////       Lambda       ////////
# # ------------------------------------

# # Function
# resource "aws_lambda_function" "" {
#     #
# }

# # IAM Role for Lambda?
# resource "aws_iam_role" "" {
#     #
# }


# # -----------------------------------------
# # ////////       API Gateway       ////////
# # -----------------------------------------

# # REST API
# resource "aws_api_gateway_rest_api" "" {
#     #
# }
