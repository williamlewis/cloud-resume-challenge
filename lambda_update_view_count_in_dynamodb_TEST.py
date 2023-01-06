import os
table_name = 'example-table-for-testing'
os.environ['TABLE_NAME'] = table_name

import boto3
import pytest
import json
from moto import mock_dynamodb


@pytest.fixture
def use_moto():
    @mock_dynamodb
    def dynamodb_resource():
        # from lambda_update_view_count_in_dynamodb import lambda_handler
        dynamodb_mocked = boto3.resource('dynamodb')
        
        #table_name = os.environ['TABLE_NAME']
        table = dynamodb_mocked.create_table(
            TableName = table_name,
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
                },
                # {
                #     'AttributeName': 'current_count',
                #     'AttributeType': 'N'
                # }
            ],
            BillingMode='PAY_PER_REQUEST'
        )
        return dynamodb_mocked # return the full mocked resource, with a mocked table within
    return dynamodb_resource

@pytest.fixture
def use_sample_data():
    # Sample data reflects fields of actual DynamoDB table
    sample_data = {
        'count_id': 'total_views',
        'current_count': 1
    }
    return sample_data


'''
@mock_dynamodb
def test_write_into_table(use_moto, use_sample_data):
    use_moto()

    table = boto3.resource('dynamodb', region_name='us-east-1').Table(table_name)

    table.put_item(Item=use_sample_data)

    resp = table.get_item(Key={'count_id': 'total_views'})
    actual_output = resp['Item']

    print('\n')
    print(use_sample_data)
    print('----')
    print(actual_output)
    assert actual_output == use_sample_data
@mock_dynamodb
def test_total_count_can_be_incremented(use_moto, use_sample_data):
    use_moto()

    table = boto3.resource('dynamodb', region_name='us-east-1').Table(table_name)

    table.put_item(Item=use_sample_data)

    resp = table.get_item(Key={'count_id': 'total_views'})
    old_count = resp['Item']['current_count']
    new_count = old_count + 1

    print('\n')
    print(old_count)
    print('----')
    print(new_count)
    assert new_count > old_count
@mock_dynamodb
def test_lambda_func_can_increment_on_mock_db(use_moto, use_sample_data):
    use_moto()
    table = boto3.resource('dynamodb', region_name='us-east-1').Table(table_name)
    table.put_item(Item=use_sample_data)

    from lambda_update_view_count_in_dynamodb import lambda_handler
    response = lambda_handler(None, None)

    assert response != None
'''



@mock_dynamodb
def test_lambda_response_is_not_empty(use_moto, use_sample_data):
    use_moto()
    table = boto3.resource('dynamodb', region_name='us-east-1').Table(table_name)
    table.put_item(Item=use_sample_data)

    from lambda_update_view_count_in_dynamodb import lambda_handler
    response = lambda_handler(None, None)

    assert response != None

@mock_dynamodb
def test_lambda_response_body_is_JSON_format(use_moto, use_sample_data):
    use_moto()
    table = boto3.resource('dynamodb', region_name='us-east-1').Table(table_name)
    table.put_item(Item=use_sample_data)

    from lambda_update_view_count_in_dynamodb import lambda_handler
    response = lambda_handler(None, None)    
    
    # body = response['body']
    
    # print('\n')
    # print(response)
    # print('--------')
    # print(body)
    # #print(json.dumps(body))
    # print(json.loads(body))
    # assert json.loads(body)
    assert json.loads(response['body'])

@mock_dynamodb
def test_lambda_response_is_single_key_val_pair(use_moto, use_sample_data):
    use_moto()
    table = boto3.resource('dynamodb', region_name='us-east-1').Table(table_name)
    table.put_item(Item=use_sample_data)

    from lambda_update_view_count_in_dynamodb import lambda_handler
    response = lambda_handler(None, None)
    body = json.loads(response['body'])

    assert type(body) == dict # body is a key/value pair
    assert len(body) == 1 # body only contains one key/value pair
    assert 'total_views' in body # body includes expected 'count_id' key
    assert type(body['total_views']) == str # value is receivced as string format
    assert int(body['total_views']) # value is a number (i.e. can be converted to integer successfully)

@mock_dynamodb
def test_lambda_increments_value_and_saves_to_db(use_moto, use_sample_data):
    use_moto()
    table = boto3.resource('dynamodb', region_name='us-east-1').Table(table_name)
    table.put_item(Item=use_sample_data)

    from lambda_update_view_count_in_dynamodb import lambda_handler
    response_1 = lambda_handler(None, None)
    count_1 = int(json.loads(response_1['body'])['total_views'])

    response_2 = lambda_handler(None, None)
    count_2 = int(json.loads(response_2['body'])['total_views'])

    assert count_2 > count_1 # lambda function increments count & successfully saves back to table (since received on second call)
    assert (count_2 - count_1) == 1 # lambda function increments count by one




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




# TEST ON LAMBDA FUNCTION
# / does function get item from DB?

# / does function write item back to DB?

# / is written item larger than original item?


# # TEST ON API ENDPOINT
# - is returned function response in a JSON format?

# - is returned response a single key/val pair?

# - is val of returned resonse a number formatted as an integer?

