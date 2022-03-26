import pytest


@pytest.fixture
def base_url(monkeypatch):
    monkeypatch.setenv('ADDRESS_SERVICE_API_BASE_URL', 'https://api-adresse.data.gouv.fr')
