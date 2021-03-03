"""Test fixtures"""

import json
import os
import pytest
import requests

BASE_API_DOMAIN = 'https://cat-fact.herokuapp.com'


@pytest.fixture
def api_list_data():
    return requests.get(f'{BASE_API_DOMAIN}/facts/').json()


@pytest.fixture
def test_data():
    os.chdir('tests')
    with open('cats_test.json', 'r') as file:
        data = json.load(file)
    return data