import json
from unittest import mock

import requests

from services.city_extractor_service import map_code_to_name, get_city
from tests.conftest import base_url
from tests.services.test_location_service import success_address, \
    success_address_with_empty_features


@mock.patch("services.city_extractor_service.lamber93_to_gps", return_value=(1000, 200))
def test_get_city_should_return_text_with_city_included(lamb_to_gps, monkeypatch, network_file):
    class MockResponse(object):
        def __init__(self):
            self.status_code = 200
            self.url = base_url + "/reverse"

        def json(self):
            return success_address

    def mock_get(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr(requests.Session, 'get', mock_get)
    assert network_file.read_text() + ";Amiens\n" == get_city(network_file.read_text())


@mock.patch("services.city_extractor_service.lamber93_to_gps", return_value=(1000, 200))
def test_get_city_should_return_empty_text_if_address_does_not_exist(lamb_to_gps, monkeypatch, network_file):
    class MockResponse(object):
        def __init__(self):
            self.status_code = 200
            self.url = base_url + "/reverse"

        def json(self):
            return success_address_with_empty_features

    def mock_get(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr(requests.Session, 'get', mock_get)
    assert '' == get_city(network_file.read_text())


def test_map_code_to_name_should_return_name_of_network_provider():
    file_content = json.dumps({"20001": "SFR"})
    with mock.patch('builtins.open', mock.mock_open(read_data=file_content)):
        assert "SFR" == map_code_to_name("20001")


def test_map_code_to_name_should_return_unknown_when_network_provider_is_not_available():
    file_content = json.dumps({"20001": "SFR"})
    with mock.patch('builtins.open', mock.mock_open(read_data=file_content)):
        assert "unknown" == map_code_to_name("200012")
