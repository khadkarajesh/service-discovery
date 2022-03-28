from unittest import mock

from tests.services.test_location_service import success_address, success_address_with_empty_features

service_dict = {"quessant": {"Orange": {"2G": True, "3G": True, "4G": False}}}


@mock.patch("resources.service_discovery_resource.LocationService.search", return_value=success_address)
@mock.patch("resources.service_discovery_resource.get_services", return_value=service_dict)
def test_discover_service_should_return_success_response(mock_get_service_func, mock_search_func, client):
    response = client.get("/discover", query_string={'q': "Vitry-sur-Seine"})
    assert response.status_code == 200
    assert response.json == service_dict


@mock.patch("resources.service_discovery_resource.LocationService.search",
            return_value=success_address_with_empty_features)
def test_discover_should_return_message_for_invalid_address(mock_search_func, client):
    response = client.get("/discover", query_string={'q': "aaaaa"})
    assert response.status_code == 200
    assert response.json == {"message": "Couldn't find your location"}


def test_discover_should_notify_with_bad_request_when_query_params_is_missing(client):
    response = client.get("/discover")
    assert response.status_code == 400


def test_discover_should_notify_with_bad_request_when_query_params_empty(client):
    response = client.get("/discover", query_string={'q': ""})
    assert response.status_code == 400

    response = client.get("/discover", query_string={'q': " "})
    assert response.status_code == 400
