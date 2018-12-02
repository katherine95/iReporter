import os
from flask import Flask, Blueprint
from instance.config import app_config


from app.api.v1 import v1 as version_one

config_name = os.getenv('APP_SETTINGS') # config_name = "development"

def create_app(config_name=config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    
    app.register_blueprint(version_one)
    return app    
    