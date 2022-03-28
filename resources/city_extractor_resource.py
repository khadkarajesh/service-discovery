from flask_restful import Resource

from jobs import get_city_for_networks


class CityExtractor(Resource):
    @classmethod
    def get(cls):
        _ = get_city_for_networks.queue()
        return {"message": "job initiated to fetch city for networks"}
