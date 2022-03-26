from dotenv import load_dotenv
from flask import Flask, request
from flask_restful import Api, Resource

import logging

from data import get_services
from location_service import LocationService

logging.basicConfig(level=logging.DEBUG)

load_dotenv(".env")
app = Flask(__name__)
api = Api(app)


class ServiceDiscovery(Resource):
    @classmethod
    def get(cls):
        user_location = request.args.get("q")
        location_service = LocationService(user_location)
        payload = location_service.search()
        if len(payload.get('features')):
            city = payload.get('features')[0].get('properties').get('city')
            return get_services(city)
        return {"message": "Couldn't find your location"}


api.add_resource(ServiceDiscovery, '/discover')

if __name__ == '__main__':
    app.run()
