# Lambda function to read current website view count from DynamoDB, increment count, and resave to DynamoDB table

import boto3
import json

dynamodb = boto3.resource('dynamodb')
    
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

return new_count
