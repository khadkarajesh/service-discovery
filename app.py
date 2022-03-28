import logging.config

import rq_dashboard
from dotenv import load_dotenv
from flask import Flask, jsonify
from flask_restful import Api
from werkzeug.exceptions import HTTPException

from core import rq
from core.logger import config
from exceptions import BaseError
from resources.city_extractor_resource import CityExtractor
from resources.service_discovery_resource import ServiceDiscovery

logging.config.dictConfig(config)

load_dotenv(".env")


def create_app():
    flask_app = Flask(__name__)
    flask_app.config['PROPAGATE_EXCEPTIONS'] = True
    rq.init_app(flask_app)

    api = Api(flask_app)
    api.add_resource(ServiceDiscovery, '/discover')
    api.add_resource(CityExtractor, '/extract')
    flask_app.config.from_object(rq_dashboard.default_settings)
    flask_app.register_blueprint(rq_dashboard.blueprint, url_prefix="/rq")

    return flask_app


app = create_app()


@app.errorhandler(Exception)
def handle_error(e):
    code = 500
    if isinstance(e, HTTPException):
        code = e.code
    return jsonify(error=str(e)), code


@app.errorhandler(BaseError)
def handle_base_exception(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


if __name__ == '__main__':
    app.run()
