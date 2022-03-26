import os

import requests
from _pytest.python_api import raises

from exceptions import BaseError
from location_service import LocationService

response = {
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
base_url = "https://api-adresse.data.gouv.fr"


def test_search_should_return_address(monkeypatch):
    monkeypatch.setenv('ADDRESS_SERVICE_API_BASE_URL', base_url)
    location_service = LocationService("anything")

    class MockResponse(object):
        def __init__(self):
            self.status_code = 200
            self.url = base_url

        def json(self):
            return response

    def mock_get(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr(requests, 'get', mock_get)
    assert response == location_service.search()


def test_search_should_raise_exception(monkeypatch):
    monkeypatch.setenv("ADDRESS_SERVICE_API_BASE_URL", base_url)
    location_service = LocationService("anything")
    assert location_service.base_url == base_url

    class MockResponse(object):
        def __init__(self):
            self.status_code = 400
            self.url = base_url

        def json(self):
            return response

    def mock_get(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr(requests, 'get', mock_get)
    with raises(BaseError) as e:
        location_service.search()
