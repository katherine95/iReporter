from flask import Blueprint
from flask_restful import Api

v2 = Blueprint('v2', __name__, url_prefix='/api/v2')
api = Api(v2)
