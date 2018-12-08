from flask_restful import Resource
from flask import jsonify, request, make_response
from app.api.v1.models.incidents import Incident as IncidentModel

incidentObject = IncidentModel()


class Incidents(Resource):
    """class that deals with incidents request functions"""

    def __init__(self):
        self.incidentObject = IncidentModel()

    def post(self):
        """POST an incident request function"""
        incidents_data = request.get_json()
        res = self.incidentObject.validate_data(incidents_data)
        if res == "valid":
            comment = incidents_data['comment']
            incidentType = incidents_data['incidentType']
            createdBy = incidents_data['createdBy']
            location = incidents_data['location']
            response = self.incidentObject.create_incident(
                incidentType, comment, createdBy, location)
            return make_response(jsonify({
                "status": 201,
                "data": [response],
                "message": "Incident created successfully."
            }), 201)
        return make_response(jsonify({
            "status": 400,
            "message": res
        }), 400)

    def get(self):
        """GET all incidents request function"""
        response = self.incidentObject.get_all_incidents()
        return make_response(jsonify({
            "status": 200,
            "data": response,
            "message": "All incidents fetched successfully."
        }), 200)


class SingleIncident(Resource):
    """class that deals with a single incident request functions"""

    def __init__(self):
        self.incidentObject = IncidentModel

    def get(self, id):
        """function to edit an incident's location"""
        response = self.incidentObject.get_incident_by_id(self, id)
        if not response:
            return make_response(jsonify({
                "status": 404,
                "message": "Record with that ID does not exist."
            }), 404)
        return make_response(jsonify({
            "status": 200,
            "data": response,
            "message": "Incident created successfully"
        }), 200)

    def delete(self, id):
        """function to edit an incident's location"""
        response = incidentObject.delete_single_incident(id)
        return make_response(jsonify({
            "status": 200,
            "message": response
        }), 200)


class UpdateIncident(Resource):
    def __init__(self):
        self.incidentObject = IncidentModel

    def patch(self, id, attribute):
        """function to edit an incident's comment and location details"""
        patch_attributes = ['comment', 'location']
        patch_data = request.get_json()
        if attribute in patch_attributes:
            if attribute in patch_data and attribute == "location" or attribute == "comment":
                res = incidentObject.validate_patch_data(patch_data, attribute)
                if res == 'valid':
                    response = incidentObject.patch_incident(
                        id, patch_data, attribute)
                    return make_response(jsonify({
                        "status": 202,
                        "data": response,
                        "message": "Attribute patched successfully"
                    }), 202)
                return make_response(jsonify({
                    "status": 400,
                    "data": [{
                        "error": res
                    }]
                }), 400)
            return make_response(jsonify({
                "Status": 400,
                "message": "Please provide " + attribute
            }), 400)
        return make_response(jsonify({
            "Status": 404,
            "message": "You can only patch location or comment."
        }), 404)
