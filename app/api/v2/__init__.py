from flask import Blueprint
from flask_restful import Api
from app.api.v2.views.users import SignUp, Login
from app.api.v2.views.incidents import Incidents, SingleIncident
from app.api.v2.views.incidents import UpdateIncident


v2 = Blueprint('v2', __name__, url_prefix='/api/v2')
api = Api(v2)

api.add_resource(SignUp, '/auth/signup')
api.add_resource(Login, '/auth/login')
api.add_resource(Incidents, '/incidents')
api.add_resource(SingleIncident, '/incidents/<int:id>')
api.add_resource(UpdateIncident, '/user/incidents/<int:id>')
