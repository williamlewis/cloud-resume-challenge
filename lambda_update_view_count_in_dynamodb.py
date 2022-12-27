# Lambda function to read current website view count from DynamoDB, increment count, and resave to DynamoDB table

import boto3
import json

dynamodb_resource = boto3.resource('dynamodb')

def lambda_handler(event, context):
    
    table_name = 'view-counter-cloud-resume-challenge'
    table = dynamodb_resource.Table(table_name)

    count_item = event    
    
    try:
        table.put_item(
                Item=count_item
            )
    except Exception as e:
        print(f'Error:  not able to add item {count_item} to DyanmoDB table {table_name}.')
    
    return None

    # SAMPLE VALUE CONFIGURED IN TEST EVENT
    # count_item = {
    #     'count_id': '0',
    #     'view_count': 1
    # }