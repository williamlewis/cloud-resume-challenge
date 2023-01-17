# Lambda function invoked by POST request to API Gateway URL endpoint via Javascript script
# Reads current website view count from DynamoDB, increments count, then updates value in DynamoDB table before returning JSON response to API Gateway

import boto3
import json
import os

dynamodb = boto3.resource('dynamodb')

# Table name is stored as an environmental variable to differentiate during production vs. testing
table_name = os.environ['TABLE_NAME']

def lambda_handler(event, context):

    table = dynamodb.Table(table_name)

    # Get current view count value from DB
    try:
        resp = table.get_item(
            Key={
                'count_id': 'total_views'
            }
        )
    # If no table item found in DB, set to 1
    except:
        resp = {
            'Item': {
                'count_id': 'total_views',
                'current_count': 1
            }
        }

    # Increment count value up for current view
    previous_count = resp['Item']['current_count']
    new_count = previous_count + 1

    # Update DB with new view count value
    table.put_item(
        Item={
            'count_id': 'total_views',
            'current_count': new_count
        }
    )

    # Build JSON response to return to API
    api_response = {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps({'total_views': str(new_count)})
    }
    
    return api_response
