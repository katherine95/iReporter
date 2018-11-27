from flask import Flask

def create_app(config_name):
    app = Flask(__name__)
    
    from app.api.v1 import v1 as version_one
    app.register_blueprint(version_one, url_prefix='/api/v1')
    return app

