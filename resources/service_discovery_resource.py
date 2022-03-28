from flask import request
from flask_restful import Resource
from werkzeug.exceptions import BadRequest

from data import get_services
from services.location_service import LocationService


class ServiceDiscovery(Resource):
    @classmethod
    def get(cls):
        user_location = request.args.get("q")
        if not user_location or len(user_location.strip()) == 0: raise BadRequest()
        payload = LocationService().search(user_location)
        if len(payload.get('features')):
            city = payload.get('features')[0].get('properties').get('city')
            return get_services(city)
        return {"message": "Couldn't find your location"}
