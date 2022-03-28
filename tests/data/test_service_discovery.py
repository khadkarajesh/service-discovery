import json
from unittest import mock

from data import get_services


def test_get_services_should_return_available_networks(city_map_content):
    with mock.patch('builtins.open', mock.mock_open(read_data=city_map_content)):
        assert get_services("quessant").get("quessant") != {}


def test_get_services_should_return_empty_if_data_does_not_exist(city_map_content):
    with mock.patch('builtins.open', mock.mock_open(read_data=city_map_content)):
        assert get_services("paris") == {}
