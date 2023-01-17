# Test actual API endpoint URL to validate live response and status

import pytest
import json
import requests

@pytest.fixture
def api_endpoint():
    endpoint_url = 'https://sm82gzbtzk.execute-api.us-east-1.amazonaws.com/prod/count'
    
    return endpoint_url

def test_api_response_not_empty_and_correct_status_code(api_endpoint):
    response = requests.post(api_endpoint)
    
    assert response != None # response is not empty
    assert response.status_code == 200 # status code is 200
    assert len(json.loads(response.text)) == 1 # response is JSON format & only contains one key/value pair
    assert 'total_views' in json.loads(response.text) # response contains expected key/value pair
    assert type(json.loads(response.text)['total_views']) == str # returned value is a string format
    assert int(json.loads(response.text)['total_views']) # returned string value is a number (i.e. can be converted to an integer successfully)
