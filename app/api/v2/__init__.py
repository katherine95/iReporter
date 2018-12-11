from flask import Blueprint
from flask_restful import Api
from app.api.v2.views.users import Users, Login

v2 = Blueprint('v2', __name__, url_prefix='/api/v2')
api = Api(v2)

api.add_resource(Users, '/auth/signup')
api.add_resource(Login, '/auth/login')
