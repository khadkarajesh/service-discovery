import logging.config

from dotenv import load_dotenv
from flask import Flask
from flask_restful import Api

from core.logger import config
from resources.city_extractor_resource import CityExtractor
from resources.service_discovery_resource import ServiceDiscovery

logging.config.dictConfig(config)

load_dotenv(".env")


def create_app():
    flask_app = Flask(__name__)
    api = Api(flask_app)
    api.add_resource(ServiceDiscovery, '/discover')
    api.add_resource(CityExtractor, '/extract')
    return flask_app


if __name__ == '__main__':
    app = create_app()
    app.run()
