import os
from flask import Flask, Blueprint
from instance.config import DevelopmentConfig


from app.api.v1 import v1 as version_one
from app.api.v2 import v2 as version_two

def create_app(config_name=DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config_name)
    
    app.register_blueprint(version_one)
    app.register_blueprint(version_two)
    return app    
    