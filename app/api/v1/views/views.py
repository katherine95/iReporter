from flask import jsonify, request
from app.api.v1 import v1
from app.api.v1.models.incidents import Incident

incidentObject = Incident()


@v1.route('/')
def index():
    return jsonify({"message" : "It works"})

@v1.route('/incidents',methods=['GET', 'POST'])
def incidents():
    '''method to create and get incidents'''
    if request.method == 'POST':
        incidents_data = request.get_json()
        incidentType = incidents_data['incidentType']
        comment = incidents_data['comment']
        createdBy = incidents_data['createdBy']
        location = incidents_data['location']

        response = incidentObject.create(incidentType, comment, createdBy, location)
        return response

    # GET method begins here 
    response = incidentObject.get_all()
    return response    