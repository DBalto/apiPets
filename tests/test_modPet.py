import pytest
import requests
import json
from assertpy.assertpy import assert_that


def test_create_newPet(app_config):
    petMod = 'pet/'
    pData = {
        "id": 13,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "BaltoWolf",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    }
    response = requests.post(app_config.base_url + petMod,
                             data=json.dumps(pData),
                             headers={"Content-Type": "application/json"})
    assert_that(response.status_code).is_equal_to(requests.codes.ok)

def test_get_pet_statusAvailable(app_config):
    petMod = 'pet/findByStatus?status='
    status = 'availabe'
    req = app_config.base_url + petMod + status
    response = requests.get(req)
    assert_that(response.status_code).is_equal_to(requests.codes.ok)

def test_get_pet_statusPending(app_config):
    petMod = 'pet/findByStatus?status='
    status = 'pending'
    req = app_config.base_url + petMod + status
    response = requests.get(req)
    assert_that(response.status_code).is_equal_to(requests.codes.ok)

def test_get_pet_statusSold(app_config):
    petMod = 'pet/findByStatus?status='
    status = 'sold'
    req = app_config.base_url + petMod + status
    response = requests.get(req)
    assert_that(response.status_code).is_equal_to(requests.codes.ok)

@pytest.mark.xfail(reason = 'Known Break')
def test_get_pet_invalidStatus(app_config):
    petMod = 'pet/findByStatus?status='
    status = 'invalid'
    req = app_config.base_url + petMod + status
    response = requests.get(req)
    assert_that(response.status_code).is_equal_to(requests.codes.bad)

def test_get_pet_byID(app_config):
    petMod = 'pet/'
    id = '13'
    req = app_config.base_url + petMod + id
    response = requests.get(req)
    assert_that(response.status_code).is_equal_to(requests.codes.ok)

def test_delete_pet_byID(app_config):
    petMod = 'pet/'
    id = '13'
    req = app_config.base_url + petMod + id
    response = requests.delete(req)
    assert_that(response.status_code).is_equal_to(requests.codes.ok)