from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


class ServiceDiscovery(Resource):
    @classmethod
    def get(cls):
        return {
            "orange": {"2G": True, "3G": True, "4G": False},
            "SFR": {"2G": True, "3G": True, "4G": True}
        }


api.add_resource(ServiceDiscovery, '/discover')

if __name__ == '__main__':
    app.run()
