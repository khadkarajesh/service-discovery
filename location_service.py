import os

import requests as requests

from exceptions import BaseError


class LocationService:
    def __init__(self, user_location):
        self.user_location = user_location
        self.base_url = os.environ.get('ADDRESS_SERVICE_API_BASE_URL')

    def search(self):
        search_url = self.base_url + "/search"
        response = requests.get(search_url, params={'q': self.user_location})
        if response.status_code == 200:
            data = response.json()
            return data
        raise BaseError(message="No Result found", error="GEO_CODE_FAILURE", status_code=400)
