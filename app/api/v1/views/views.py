from flask import jsonify, request, make_response
from flask_restful import Resource
from app.api.v1.models.incidents import Incident as IncidentModel

class Incidents(Resource):
    def __init__(self):
        self.incidentObject = IncidentModel()
     
    def post(self):
        incidents_data = request.get_json()
        incidentType = incidents_data['incidentType']
        comment = incidents_data['comment']
        createdBy = incidents_data['createdBy']
        location = incidents_data['location']
       
        response = self.incidentObject.create(incidentType, comment, createdBy, location)
        return response
        
    def get(self):
        # GET method begins here 
        response = self.incidentObject.get_all()
        return response 
    
# class RedFlags(Resource):
#     def __init__(self):
#         self.incidentObject = IncidentModel 

#     def get(self, id):
#         response = self.incidentObject.getById(self, id)
#         return make_response(jsonify(response)) 

#     def patchLocation(self):
#         pass

#     def patchComment(self):
#         pass    

#     def delete(self):
#         pass       