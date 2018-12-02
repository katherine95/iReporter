from flask import Flask
from flask import Blueprint
from flask_restful import Resource, Api

from app.api.v1.views.incidents import Incidents, Incident, UpdateIncident
from app.api.v1.views.users import Users

v1 = Blueprint('v1', __name__, url_prefix='/api/v1')
api = Api(v1)

api.add_resource(Incidents, '/incidents')
api.add_resource(Incident, '/incident/<id>')
api.add_resource(UpdateIncident, '/incident/<id>/<attribute>')
api.add_resource(Users, '/users')
