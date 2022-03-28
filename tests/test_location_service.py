import requests
from _pytest.python_api import raises

from conftest import base_url
from exceptions import BaseError

expected_success_address_response = {
    "type": "FeatureCollection",
    "version": "draft",
    "features": [
        {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [
                    2.290084,
                    49.897443
                ]
            },
            "properties": {
                "label": "8 Boulevard du Port 80000 Amiens",
                "score": 0.49159121588068583,
                "housenumber": "8",
                "id": "80021_6590_00008",
                "type": "housenumber",
                "name": "8 Boulevard du Port",
                "postcode": "80000",
                "citycode": "80021",
                "x": 648952.58,
                "y": 6977867.25,
                "city": "Amiens",
                "context": "80, Somme, Hauts-de-France",
                "importance": 0.6706612694243868,
                "street": "Boulevard du Port"
            }
        }
    ],
    "attribution": "BAN",
    "licence": "ODbL 1.0",
    "query": "8 bd du port",
    "limit": 1
}


def test_search_should_return_address(monkeypatch, location_service):
    class MockResponse(object):
        def __init__(self):
            self.status_code = 200
            self.url = base_url + "/search"

        def json(self):
            return expected_success_address_response

    def mock_get(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr(requests.Session, 'get', mock_get)
    assert expected_success_address_response == location_service.search("8 bd du port")


def test_search_should_raise_exception(monkeypatch, location_service):
    class MockResponse(object):
        def __init__(self):
            self.status_code = 500
            self.url = base_url + "/search"

        def json(self):
            return expected_success_address_response

    def mock_get(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr(requests.Session, 'get', mock_get)
    with raises(BaseError) as e:
        location_service.search("8 bd du port")


def test_reverse_should_return_address(monkeypatch, location_service):
    class MockResponse(object):
        def __init__(self):
            self.status_code = 200
            self.url = base_url + "/reverse"

        def json(self):
            return expected_success_address_response

    def mock_get(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr(requests.Session, 'get', mock_get)
    assert expected_success_address_response == location_service.reverse(latitude=10000, longitude=2000)


def test_reverse_should_return_none(monkeypatch, location_service):
    class MockResponse(object):
        def __init__(self):
            self.status_code = 400
            self.url = base_url + "/reverse"

        def json(self):
            return expected_success_address_response

    def mock_get(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr(requests.Session, 'get', mock_get)
    assert not location_service.reverse(latitude=10000, longitude=2000)
