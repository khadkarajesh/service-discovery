import logging.config

from dotenv import load_dotenv
from flask import Flask
from flask_restful import Api

from core.logger import config
from data.transformer import fetch_city
from resources.city_extractor_resource import CityExtractor
from resources.service_discovery_resource import ServiceDiscovery

logging.config.dictConfig(config)

load_dotenv(".env")
app = Flask(__name__)
api = Api(app)

api.add_resource(ServiceDiscovery, '/discover')
api.add_resource(CityExtractor, '/extract')

if __name__ == '__main__':
    app.run()
    fetch_city()
