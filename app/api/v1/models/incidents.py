from flask import jsonify
from datetime import date
import uuid

class Incident(object):
   """class that deals with incidents data"""

   def __init__(self):
       self.incidents_list = []

    # Method to create an incident   
   def create(self, incidentType, comment, createdBy, location):
       incident_details = {}
       incident_details['createdBy'] = createdBy
       incident_details['incidentType'] = incidentType
       incident_details['location'] = location
       incident_details['status'] = "pending"
       incident_details['comment'] = comment
       incident_details['CreatedOn'] = date.today()

       incident_details['id'] = uuid.uuid1()
       self.incidents_list.append(incident_details)
       incidents = self.incidents_list
       return jsonify({
           "message" : "Created successfully",
           "data" : incidents
       }), 201

    # method to GET all incidents
   def get_all(self):
        return jsonify({
            "incidents" : self.incidents_list
    })
  
