from flask import jsonify, request, make_response
from flask_restful import Resource
from app.api.v1.models.incidents import Incident as IncidentModel

incidentObject = IncidentModel()

class Incidents(Resource):
    def __init__(self):
        self.incidentObject = IncidentModel()
     
    def post(self):
        incidents_data = request.get_json()
        comment = incidents_data['comment']
        incidentType = incidents_data['incidentType']
        createdBy = incidents_data['createdBy']
        location = incidents_data['location']
       
        response = self.incidentObject.create(incidentType, comment, createdBy, location)
        return make_response(response)
        
    def get(self):
        # GET method begins here 
        response = self.incidentObject.get_all()
        return response 
    

class Incident(Resource):
    def __init__(self):
        self.incidentObject = IncidentModel 

    def get(self, id):
        response = self.incidentObject.getById(self, id)
        return make_response(jsonify(response))

    def delete(self, id):
        response = incidentObject.deleteIncident(id)
        return make_response(response)


class UpdateIncident(Resource):
    def __init__(self):
        self.incidentObject =IncidentModel       

    def patch(self, id, attribute):
        patch_attributes = ['comment', 'location']
        print(attribute)
        if attribute in patch_attributes:
            patch_data = request.get_json()
            if attribute in patch_data:
                if attribute == "location":
                    res = incidentObject.editLocation(id, patch_data['location'])
                    return make_response(res)
                res = incidentObject.editComment(id, patch_data['comment'])
                return make_response(res)
            return make_response(jsonify({
            "Status": 400, 
            "message": "Please provide " + attribute  
            }), 400)
        return make_response(jsonify({
            "Status": 400,
            "message": "You can only patch location or comment."
        }), 400)