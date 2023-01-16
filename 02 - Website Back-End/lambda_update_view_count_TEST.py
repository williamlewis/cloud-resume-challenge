import os
import boto3
import pytest
import json
from moto import mock_dynamodb

mock_table_name = 'mocked_table'


@pytest.fixture # Initial data to store in mock table
def sample_data():
    sample_data = {
        'count_id': 'total_views',
        'current_count': 1
    }
    return sample_data

@pytest.fixture # Mock DynamoDB table with initial data
def use_moto():
    @mock_dynamodb
    def mock_dynamodb_resource(sample_data):
        # Set up DynamoDB resource
        dynamodb_mocked = boto3.resource('dynamodb')
        # Create table within DB resource
        mock_table = dynamodb_mocked.create_table(
            TableName = mock_table_name,
            KeySchema = [
                {
                    'AttributeName': 'count_id',
                    'KeyType': 'HASH'
                }
            ],
            AttributeDefinitions = [
                {
                    'AttributeName': 'count_id',
                    'AttributeType': 'S'
                }
            ],
            BillingMode = 'PAY_PER_REQUEST'
        )

        mock_table.put_item(Item=sample_data)

        # Return full resource including mocked table within
        return dynamodb_mocked
    return mock_dynamodb_resource

os.environ['TABLE_NAME'] = mock_table_name # Set table name env var for all tests within session (instead of repeating within each test function)

@mock_dynamodb
def test_lambda_function_response_is_not_empty(use_moto, sample_data):
    use_moto(sample_data)
    from lambda_update_view_count import lambda_handler
    response = lambda_handler(None, None)

    assert response != None # Response is not empty

@mock_dynamodb
def test_lambda_response_body_is_JSON_format(use_moto, sample_data):
    use_moto(sample_data)
    from lambda_update_view_count import lambda_handler
    response = lambda_handler(None, None)

    assert json.loads(response['body']) # Response body is JSON if .loads method can be called on it

@mock_dynamodb
def test_lambda_response_is_single_key_value_pair(use_moto, sample_data):
    use_moto(sample_data)
    from lambda_update_view_count import lambda_handler
    response = lambda_handler(None, None)

    body = json.loads(response['body'])
    
    assert type(body) == dict # Body is a key/value pair
    assert len(body) == 1 # Body only contains one key/value pair
    assert 'total_views' in body # Body includes expected 'count_id' key
    assert type(body['total_views']) == str # Value is receivced as string format
    assert int(body['total_views']) # Value is a number (i.e. can be converted to integer successfully)

@mock_dynamodb
def test_lambda_increments_value_and_saves_back_to_db(use_moto, sample_data):
    use_moto(sample_data)
    from lambda_update_view_count import lambda_handler
    response_1 = lambda_handler(None, None)
    count_1 = int(json.loads(response_1['body'])['total_views'])

    response_2 = lambda_handler(None, None)
    count_2 = int(json.loads(response_2['body'])['total_views'])

    assert count_2 > count_1 # Lambda function increments count & successfully saves it back to DB table
    assert (count_2 - count_1) == 1 # Lambda function increments count by one
