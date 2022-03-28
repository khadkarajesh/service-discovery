import pytest

from services.location_service import LocationService

base_url = "https://api-adresse.data.gouv.fr"


@pytest.fixture(scope="module")
def location_service():
    return LocationService()


@pytest.fixture(autouse=True)
def env_setup(monkeypatch):
    monkeypatch.setenv('ADDRESS_SERVICE_API_BASE_URL', base_url)
