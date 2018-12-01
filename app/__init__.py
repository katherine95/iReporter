import os
from flask import Flask, Blueprint

from app.api.v1 import v1 as version_one

# config_name = os.getenv('FLASK_ENV') # config_name = "development"
# from instance.config import app_config

# config_name = os.getenv('app_settings') # config_name = "development"
# app = create_app(app_config[config_name])

def create_app():
    app = Flask(__name__)
    
    app.register_blueprint(version_one)
    return app

