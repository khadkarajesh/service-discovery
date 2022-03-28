import os

import requests

from exceptions import BaseError

errors = {
    "GEO_CODE_FAILURE": "No Result found",
    "GEO_CODE_REVERSE_FAILURE": "Couldn't reverse geo-code"
}


class LocationService:
    def __init__(self):
        self.base_url = os.environ.get('ADDRESS_SERVICE_API_BASE_URL', 'https://api-adresse.data.gouv.fr')
        self.session = requests.Session()

    def search(self, location):
        search_url = self.base_url + "/search"
        response = self.session.get(search_url, params={'q': location})
        if response.status_code == 200:
            return response.json()
        raise BaseError(message=errors.get("GEO_CODE_FAILURE"))

    def reverse(self, longitude, latitude):
        reverse_geocode_url = self.base_url + "/reverse"
        response = self.session.get(reverse_geocode_url, params={"lat": latitude, "lon": longitude})
        if response.status_code == 200:
            return response.json()
