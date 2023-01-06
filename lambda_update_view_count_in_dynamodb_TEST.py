import os
table_name = 'example-table-for-testing'
os.environ['TABLE_NAME'] = table_name

import boto3
import pytest
import json
from moto import mock_dynamodb

'''
# Set up mock table as a fixture, to use in tests
@pytest.fixture
def use_mock_db():
    @mock_dynamodb
    def dynamodb_resource():
        dynamodb_resource = boto3.resource('dynamodb', region_name='us-east-1')

        # Create a table
        dynamodb_resource.create_table(
            TableName=table_name,
            KeySchema=[
                {
                    'AttributeName': 'RecordId',
                    'KeyType': 'HASH'
                },
                {
                    'AttributeName': 'RecordType',
                    'KeyType': 'RANGE'
                },
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'RecordId',
                    'AttributeType': 'S'
                },
                {
                    'AttributeName': 'RecordType',
                    'AttributeType': 'S'
                },
            ],
            BillingMode='PAY_PER_REQUEST'
        )
        return dynamodb_resource
    return dynamodb_resource

# Create test, using fixture argument to operate off of mock db
@mock_dynamodb
def test_something():
    return 'something'
'''







@mock_dynamodb
def test_write_into_table():
    # from lambda_update_view_count_in_dynamodb import lambda_handler
    dynamodb_mocked = boto3.resource('dynamodb')
    
    
    table_name = os.environ['TABLE_NAME']
    table = dynamodb_mocked.create_table(
        TableName = table_name,
        KeySchema = [
            {
                'AttributeName': 'date',
                'KeyType': 'HASH'
            }
        ],
        AttributeDefinitions = [
            {
                'AttributeName': 'date',
                'AttributeType': 'S'
            }
        ],
        BillingMode='PAY_PER_REQUEST'
    )

    data = {
        'date': '06-Nov-2020',
        'field2': 'value2',
        'field3': 'value3'
    }

    table.put_item(Item=data)

    resp = table.get_item(Key={'date': '06-Nov-2020'})
    actual_output = resp['Item']


    print(data)
    print('----')
    print(actual_output)
    assert actual_output == data











'''
# Define in environmental variable for DynamoDB table name before importing other modules 
import os
os.environ['TABLE_NAME'] = 'example-table-for-testing'

# # Test actual lambda function from locally cloned repo (in same directory as testing file)
# from lambda_update_view_count_in_dynamodb import lambda_handler
# from lambda_update_view_count_in_dynamodb import dynamodb

import boto3
# Use moto to set up mock cloud resources for majority of function testing, to reduce number of API calls and lambda invocations
from moto import mock_dynamodb2
import pytest
import json



################################
##  SET UP CONTEXT FOR TESTS  ##
################################

# @pytest.fixture
# def call_1():
#     return lambda_handler(None, None)

# @pytest.fixture
# def call_2():
#     return lambda_handler(None, None)



######################
##  TEST FUNCTIONS  ##
######################


# def test_lambda_response_is_not_empty(call_1):
#     assert call_1 != None

# def test_lambda_increments_view_count(call_1, call_2):
#     count_1 = json.loads(call_1['body'])['total_views']
#     count_2 = json.loads(call_2['body'])['total_views']    
        
#     assert count_2 > count_1


@mock_dynamodb2
def test_write_into_table():
    from lambda_update_view_count_in_dynamodb import lambda_handler
    dynamodb_mocked = boto3.resource('dynamodb')

    # from moto.core import patch_client, patch_resource
    # patch_client(dynamodb)
    # patch_resource(dynamodb_mocked)
    
    
    
    
    
    
    table_name = os.environ['TABLE_NAME']
    table = dynamodb_mocked.create_table(
        TableName = table_name,
        KeySchema = [{
            'AttributeName': 'date',
            'KeyType': 'HASH'
        }],
        AttributeDefinitions = [{
            'AttributeName': 'date',
            'AttributeType': 'S'
        }]
    )

    data = {
        'date': '06-Nov-2020',
        'field2': 'value2',
        'field3': 'value3'
    }

    table.put_item(Item=data)

    resp = table.get_item(Key={'date': '06-Nov-2020'})
    actual_output = resp['Item']


    print(data)
    print('----')
    print(actual_output)
    assert actual_output == data















# TEST ON LAMBDA FUNCTION
# / does function get item from DB?

# / does function write item back to DB?

# / is written item larger than original item?


# # TEST ON API ENDPOINT
# - is returned function response in a JSON format?

# - is returned response a single key/val pair?

# - is val of returned resonse a number formatted as an integer?

'''

