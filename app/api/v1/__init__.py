from flask import Blueprint
from flask_restful import Resource, Api

from app.api.v1.views.views import Incidents, RedFlags, IncidentDetail

v1 = Blueprint('v1', __name__, url_prefix='/api/v1')
api = Api(v1)

api.add_resource(Incidents, '/incidents')
api.add_resource(RedFlags, '/redflags/<id>')
api.add_resource(IncidentDetail, '/redflags/<id>/<attribute>')

