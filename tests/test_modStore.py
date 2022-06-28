import requests
import json
from assertpy.assertpy import assert_that


def test_create_newOrder(app_config):
    pURL = 'store/order'
    pData = {
        "id": 13,
        "petId": 13,
        "quantity": 0,
        "shipDate": '2022-03-07T15:00:00.000Z',
        "status": 'placed',
        "complete": True
    }
    response = requests.post(app_config.base_url + pURL,
                             data=json.dumps(pData),
                             headers={"Content-Type": "application/json"})
    assert_that(response.status_code).is_equal_to(requests.codes.ok)

def test_get_order_byID(app_config):
    pURL = 'store/order/'
    pOrder = '13'
    response = requests.get(app_config.base_url + pURL + pOrder)
    assert_that(response.status_code).is_equal_to(requests.codes.ok)

def test_delete_order_byID(app_config):
    pURL = 'store/order/'
    pOrder = '13'
    response = requests.delete(app_config.base_url + pURL + pOrder)
    assert_that(response.status_code).is_equal_to(requests.codes.ok)

def test_get_order_byID_notFound(app_config):
    pURL = 'store/order/'
    pOrder = '13'
    response = requests.get(app_config.base_url + pURL + pOrder)
    assert_that(response.status_code).is_equal_to(requests.codes.not_found)

def test_get_inventory(app_config):
    pURL = 'store/inventory'
    response = requests.get(app_config.base_url + pURL)
    assert_that(response.json()).is_not_equal_to('')
    assert_that(response.status_code).is_equal_to(requests.codes.ok)