from flask_restful import Resource
from flask import jsonify, request, make_response
from app.api.v2.models.incidents import Incident as IncidentModel
from app.api.v2.models.users import SignUp
from flask_jwt_extended import (create_access_token, create_refresh_token,
                                jwt_required, jwt_refresh_token_required,
                                get_jwt_identity, get_raw_jwt)

incidentObject = IncidentModel()
userObject = SignUp()


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


class SingleIncident(Resource):
    """class that deals with a single incident request functions"""

    def __init__(self):
        self.incidentObject = IncidentModel

    @jwt_required
    def get(self, id):
        """function to get a single incident"""
        response = self.incidentObject.get_incident_by_id(self, id)
        if not response:
            return make_response(jsonify({
                "status": 404,
                "message": "Record with that ID does not exist."
            }), 404)
        return make_response(jsonify({
            "status": 200,
            "data": response,
            "message": "Incident fetched successfully"
        }), 200)

    @jwt_required
    def patch(self, id):
        current_user = get_jwt_identity()
        user = userObject.get_user_by_id(current_user)
        if user['isAdmin']:
            if incidentObject.get_incident_by_id(id):
                data = request.get_json()
                if 'status' in data:
                    status = data['status']
                    resp = incidentObject.update_incident_status(id, status)
                    return make_response(jsonify({
                        "status": 200,
                        "data": resp,
                        "message": "Incident patched successfully"
                    }), 200)
                return make_response(jsonify({
                    "status": 400,
                    "message": "Please provide 'status'"
                }), 400)
            return make_response(jsonify({
                "status": 404,
                "message": "Incident with that ID doesnt exist"
            }), 404)
        return make_response(jsonify({
            "status": 405,
            "message": "you dont have access rights"
        }), 405)

    @jwt_required
    def delete(self, id):
        """function to delete a posted incident"""
        current_user = get_jwt_identity()
        user = userObject.get_user_by_id(current_user)
        if incidentObject.get_incident_by_id(id):
            response = incidentObject.delete_incident_record(id)
            return make_response(jsonify({
                "status": 200,
                "data": [{
                    "id": id,
                    "message": "Incident deleted successfully"
                }]
            }), 200)
        return make_response(jsonify({
            "status": 404,
            "message": "Incident with that ID doesnt exist"
        }), 404)


class UpdateIncident(Resource):
    """class that deals with updating a single request functions"""

    def __init__(self):
        self.incidentObject = IncidentModel

    @jwt_required
    def patch(self, id):
        current_user = get_jwt_identity()
        user = userObject.get_user_by_id(current_user)
        if incidentObject.get_incident_by_id(id):
            data = request.get_json()
            if 'comment' in data:
                comment = data['comment']
                resp = incidentObject.update_incident_comment(id, comment)
                return make_response(jsonify({
                    "status": 200,
                    "data": resp,
                    "message": "Comment patched successfully"
                }), 200)
            elif 'location' in data:
                location = data['location']
                resp = incidentObject.update_incident_location(id, location)
                return make_response(jsonify({
                    "status": 200,
                    "data": resp,
                    "message": "Comment patched successfully"
                }), 200)
            return make_response(jsonify({
                "status": 400,
                "message": "Please provide 'comment' or 'location'"
            }), 400)
        return make_response(jsonify({
            "status": 404,
            "message": "Incident with that ID doesnt exist"
        }), 404)
