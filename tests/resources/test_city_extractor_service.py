from unittest import mock


@mock.patch("resources.city_extractor_resource.get_city_for_networks")
def test_extractor_resource_should_return_job_initiated_message(mock_get_city_for_network, client):
    response = client.get("/extract")
    assert response.status_code == 200
    assert response.json == {"message": "job initiated to fetch city for networks"}
