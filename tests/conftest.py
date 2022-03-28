import pytest

from services.location_service import LocationService

base_url = "https://api-adresse.data.gouv.fr"


@pytest.fixture
def network_file(tmp_path):
    directory = tmp_path / 'data'
    directory.mkdir()
    file = directory / "networks.csv"
    file.write_text("20801;102980;6847973;1;1;0")
    return file


@pytest.fixture(scope="module")
def location_service():
    return LocationService()


@pytest.fixture(autouse=True)
def env_setup(monkeypatch):
    monkeypatch.setenv('ADDRESS_SERVICE_API_BASE_URL', base_url)
