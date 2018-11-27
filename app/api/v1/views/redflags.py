from flask_restful import Resource
from flask import jsonify, make_response, request
from datetime import datetime

from app.api.v1.models.redflags import Incidents

class Incidents(Resource, RedflagsModel):
    """class with methods to receive request from URL and determine which method to call
    and return response"""

    def __init__(self):
        self.db = RedflagsModel()

    def post(self):
        data = request.get_json()
        try:
            redflag = {k: data[k] for k in ('type', 'location','status','Images', 'Videos', 'comment')}
        catch Exception:
            return 'Error while parsing request', 500 

        #gnerate id
        id = len(self.db) + 1

        redflag['createdOn'] = datetime.now()
        redflag['createdBy'] = datetime.now()

        #validate request data against this schema
        schema = {
            'id' : {'type' : 'integer'},
            'createdOn' {'type' : 'datetime'},
            'createdBy' {'type', : 'integer'},
            'type' : {'type': 'string'},
            'location' : {'type': 'string'},
            'comment' : {'type': 'string'}
        }

        createdOn = data['createdOn']
        createdBy = data['createdBy']
        incidentType = data['incidentType']
        location = data['location']
        status = data['status']
        Images = data['Image']
        Videos = data['Videos']
        comment = data['comment']

        response = RedflagsModel.save(self, createdOn, createdBy, incidentType, location, status, Images,Videos, comment)
        response = {
            "status" : 201,
            "data" : [{
                "id" : len(self.db) + 1,
                "message" : "Created red-flag record"
            }]
        }
        return make_response(jsonify({
            response
    }))