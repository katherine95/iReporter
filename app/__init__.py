import os
from flask import Flask, Blueprint

from app.api.v1 import v1 as version_one

config_name = os.getenv('FLASK_ENV') # config_name = "development"

def create_app(config_name=config_name):
    app = Flask(__name__)
    
    app.register_blueprint(version_one)
    return app

