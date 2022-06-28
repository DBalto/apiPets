import pytest
import requests
import json
from assertpy.assertpy import assert_that


def test_create_user(app_config):
    pURL = 'user/createWithArray'
    pData = [{
        "id": 13,
        "userName": "Darrny",
        "firstName": "Daniel",
        "lastName": "Baltodano",
        "email": "daniel@mailinator.com",
        "password": "psswrd",
        "phone": "26651313",
        "userStatus": 0
    }]
    response = requests.post(app_config.base_url + pURL,
                             data=json.dumps(pData),
                             headers={"Content-Type": "application/json"})
    assert_that(response.status_code).is_equal_to(requests.codes.ok)

@pytest.mark.skip(reason = 'Not currently working, not sure if XFail')
def test_get_user_byUserName(app_config):
    pURL = 'user/'
    pUserName = 'Darrny'
    response = requests.get(app_config.base_url + pURL + pUserName)
    assert_that(response.status_code).is_equal_to(requests.codes.ok)
