from flask import Flask, Blueprint, jsonify, make_response
from instance.config import DevelopmentConfig

from app.api.v1 import v1 as version_one

def create_app(config_name=DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config_name)
    
    app.register_blueprint(version_one)

    @app.errorhandler(403)
    def forbidden(error):
        return make_response(jsonify({
            "status":403,
            "error": "You do not have sufficient permissions to access this resources."
        }), 403)

    @app.errorhandler(404)
    def page_not_found(error):
        return make_response(jsonify({
            "status": 404,
            "error": "The record you are looking for does not exist" 
        }), 404)

    @app.errorhandler(500)
    def internal_server_error(error):
        return make_response(jsonify({
            "status": 500,
            "error": "The server encountered an internal error."
        }), 500)
    return app    

