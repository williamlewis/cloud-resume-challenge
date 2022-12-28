# Lambda function invoked by API Gateway POST request
# Reads current website view count from DynamoDB, increments count, then updates value in DynamoDB table before returning JSON response to API Gateway

import boto3
import json

dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):

    table_name = 'view-counter-cloud-resume-challenge'
    table = dynamodb.Table(table_name)

    # get current view count value from DB
    resp = table.get_item(
        Key={
            'count_id': 'total_views'
        }
    )

    # increment count value up for current view
    previous_count = resp['Item']['current_count']
    new_count = previous_count + 1

    # update DB with new view count value
    table.put_item(
        Item={
            'count_id': 'total_views',
            'current_count': new_count
        }
    )

    # build JSON response to return to API
    api_response = {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps({'total_views': str(new_count)})
    }
    
    return api_response
