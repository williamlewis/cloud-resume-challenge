import os
os.environ['TABLE_NAME'] = 'view-counter-cloud-resume-challenge'

from lambda_update_view_count_in_dynamodb import lambda_handler
import pytest
import moto
import json


################################
##  SET UP CONTEXT FOR TESTS  ##
################################

# @pytest.fixture
# def mock_env_var_table_name(monkeypatch):
#     monkeypatch.setenv('TABLE_NAME', 'view-counter-cloud-resume-challenge')

@pytest.fixture
def call_1():
    return lambda_handler(None, None)

@pytest.fixture
def call_2():
    return lambda_handler(None, None)






######################
##  TEST FUNCTIONS  ##
######################

# def test_first_attempt():
#     assert lambda_handler(None, None) == None


def test_lambda_response_is_not_empty(call_1):
    assert call_1 != None

def test_lambda_increments_view_count(call_1, call_2):
    count_1 = json.loads(call_1['body'])['total_views']
    count_2 = json.loads(call_2['body'])['total_views']    
        
    assert count_2 > count_1







# TEST ON LAMBDA FUNCTION
# / does function get item from DB?

# / does function write item back to DB?

# / is written item larger than original item?


# # TEST ON API ENDPOINT
# - is returned function response in a JSON format?

# - is returned response a single key/val pair?

# - is val of returned resonse a number formatted as an integer?



