import os
from flask import Flask, jsonify, make_response
from instance.config import app_config
from flask_jwt_extended import JWTManager

from app.api.v1 import v1 as version_one
from app.api.v2 import v2 as version_two
# from app.api.v2.models.users import RevokedTokenModel


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(app_config[os.getenv('APP_SETTINGS')])

    app.config['JWT_SECRET_KEY'] = 'secret-key'
    app.config['PROPAGATE_EXCEPTIONS'] = True
    # app.config['JWT_BLACKLIST_ENABLED'] = True
    # app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access']
    jwt = JWTManager(app)

    # @jwt.token_in_blacklist_loader
    # def check_if_token_in_blacklist(decrypted_token):
    #     jwtObj = RevokedTokenModel()
    #     jti = decrypted_token['jti']
    #     print(jti)
    #     return jwtObj.is_jti_blacklisted(jti)

    app.register_blueprint(version_one)
    app.register_blueprint(version_two)

    @app.errorhandler(403)
    def forbidden(error):
        return make_response(jsonify({
            "status": 403,
            "message": "You do not have sufficient permissions"
            "to access this resource."
        }), 403)

    @app.errorhandler(404)
    def page_not_found(error):
        return make_response(jsonify({
            "status": 404,
            "message": "The request you are looking for does not exist"
            }), 404)

    @app.errorhandler(500)
    def internal_server_error(error):
        return make_response(jsonify({
            "status": 500,
            "message": "The server encountered an internal error."
        }), 500)
    return app
