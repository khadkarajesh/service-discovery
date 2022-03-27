from flask_restful import Resource

from data.transformer import fetch_city


class CityExtractor(Resource):
    @classmethod
    def get(cls):
        fetch_city()
        return {"success": True}
