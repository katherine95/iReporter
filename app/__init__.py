import os
from flask import Flask, Blueprint

from instance.config import app_config

from app.api.v1 import v1 as version_one

# config_name = os.getenv('FLASK_ENV') # config_name = "development"


# config_name = os.getenv('app_settings') # config_name = "development"
# app = create_app(app_config[config_name])

def create_app(config):
    app = Flask(__name__,instance_relative_config=True)
    app.config.from_object(app_config[config])
    app_config[config].init_app(app)
    
    app.register_blueprint(version_one)
    return app

