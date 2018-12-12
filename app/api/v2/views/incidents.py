from flask_restful import Resource
from flask import jsonify, request, make_response
from app.api.v2.models.incidents import Incident as IncidentModel
from flask_jwt_extended import (create_access_token, create_refresh_token,
                                jwt_required, jwt_refresh_token_required,
                                get_jwt_identity, get_raw_jwt)

incidentObject = IncidentModel()


class Incidents(Resource):
    """class that deals with incidents request functions"""

    def __init__(self):
        self.incidentObject = IncidentModel()

    @jwt_required
    def post(self):
        """POST an incident request function"""
        incidents_data = request.get_json()
        res = self.incidentObject.validate_data(incidents_data)
        if res == "valid":
            comment = incidents_data['comment']
            incidentType = incidents_data['incidentType']
            location = incidents_data['location']
            createdBy = get_jwt_identity()
            if not self.incidentObject.check_if_comment_exist(comment):
                incident = IncidentModel(
                    incidentType, location, comment, createdBy)
                response = incident.create_incident()
                return make_response(jsonify({
                    "status": 201,
                    "data": [{
                        "id": response,
                        "message": "Incident created successfully."
                    }]
                }), 201)
            return make_response(jsonify({
                    "status": 409,
                    "message": "Incident with this comment exist."
                }), 409)
        return make_response(jsonify({
            "status": 400,
            "message": res
        }), 400)

    @jwt_required
    def get(self):
        """GET all incidents request function"""
        response = IncidentModel.get_all_incidents(self)
        return make_response(jsonify({
            "status": 200,
            "data": response,
            "message": "All incidents fetched successfully."
        }), 200)
