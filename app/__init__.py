from flask import Flask, Blueprint

from app.api.v1 import v1 as version_one

def create_app(config_name='development'):
    app = Flask(__name__)
    
    app.register_blueprint(version_one)
    return app

