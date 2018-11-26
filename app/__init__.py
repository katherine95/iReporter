from flask import Flask
from flask_restful import Resource, Api

# local import
from instance.config import app_config

# initialize database


def create_app(app_config):
    app = Flask(__name__)
    api = Api(app)
    app.config.from_object(app_config)
    return app

    