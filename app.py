import logging.config
import rq_dashboard

from dotenv import load_dotenv
from flask import Flask
from flask_restful import Api

from core import rq
from core.logger import config
from resources.city_extractor_resource import CityExtractor
from resources.service_discovery_resource import ServiceDiscovery

logging.config.dictConfig(config)

load_dotenv(".env")


def create_app():
    flask_app = Flask(__name__)
    rq.init_app(flask_app)
    return flask_app


app = create_app()
api = Api(app)
api.add_resource(ServiceDiscovery, '/discover')
api.add_resource(CityExtractor, '/extract')
app.config.from_object(rq_dashboard.default_settings)
app.register_blueprint(rq_dashboard.blueprint, url_prefix="/rq")

if __name__ == '__main__':
    app.run()
