import json

import pytest

from app import create_app
from data.transformers.name_transformer import NameTransformer
from data.transformers.service_transformer import ServiceTransformer
from services.location_service import LocationService

base_url = "https://api-adresse.data.gouv.fr"


@pytest.fixture
def name_transformer():
    return NameTransformer("input_file", "output_file")


@pytest.fixture
def service_transformer():
    return ServiceTransformer("input_file", "output_file")


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


@pytest.fixture(scope="package")
def city_map_content():
    return json.dumps({"quessant": {"Orange": {"2G": True, "3G": True, "4G": False}}})


@pytest.fixture()
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })
    yield app


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()
