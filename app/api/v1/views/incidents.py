from flask import jsonify, request, make_response
from flask_restful import Resource
from app.api.v1.models.incidents import Incident as IncidentModel

incidentObject = IncidentModel()

class Incidents(Resource):
    """class that deals with incidents request functions"""

    def __init__(self):
        self.incidentObject = IncidentModel()
        
    def post(self):
        """POST an incident request function"""
        incidents_data = request.get_json()
        comment = incidents_data['comment']
        incidentType = incidents_data['incidentType']
        createdBy = incidents_data['createdBy']
        location = incidents_data['location']
        
        response = self.incidentObject.create_incident(incidentType, comment, createdBy, location)
        return make_response(jsonify({
            "status": 201,
            "data": [{
                "Incident": response
            }]
        }))
        
    def get(self):
        """GET all incidents request function"""
        response = self.incidentObject.get_all_incidents()
        return make_response(jsonify({
            "status": 200,
            "data":[{
                "Incidents": response
            }]
        })) 
    

class SingleIncident(Resource):
    """class that deals with a single incident request functions"""

    def __init__(self):
        self.incidentObject = IncidentModel 

    def get(self, id):
        """function to edit an incident's location"""
        response = self.incidentObject.get_incident_by_id(self, id)
        return make_response(jsonify({
            "status": 200,
            "data": [{
                "Incident": response
            }]
        }))

    def delete(self, id):
        """function to edit an incident's location"""
        response = incidentObject.delete_single_incident(id)
        return make_response(jsonify({
            "status": 204,
            "data": [{
                "message": response
            }]
        }))


class UpdateIncident(Resource):
    def __init__(self):
        self.incidentObject =IncidentModel       

    def patch(self, id, attribute):
        """function to edit an incident's comment and location details"""
        patch_attributes = ['comment', 'location']
        if attribute in patch_attributes:
            patch_data = request.get_json()
            if attribute in patch_data:
                if attribute == "location":
                    response = incidentObject.edit_incident_location(id, patch_data['location'])
                    return make_response(jsonify({
                        "status":202,
                        "data": [{
                            "Incident": response
                        }]
                    }))
                response = incidentObject.edit_incident_comment(id, patch_data['comment'])
                return make_response(jsonify({
                    "status": 202,
                    "data":[{
                        "Incident": response
                    }]
                }))
            return make_response(jsonify({
            "Status": 400, 
            "error": "Please provide " + attribute  
            }))
        return make_response(jsonify({
            "Status": 404,
            "error": "You can only patch location or comment."
        }))