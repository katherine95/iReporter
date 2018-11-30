from flask import jsonify, request, make_response
from datetime import date
import uuid

incidents_list = []
class Incident(object):
   """class that deals with incidents data"""

   def __init__(self):
       self.incidents_list = incidents_list

    # Method to create an incident   
   def create(self, incidentType, comment, createdBy, location):
       incident_details = {}
       incident_details['createdBy'] = createdBy
       incident_details['incidentType'] = incidentType
       incident_details['location'] = location
       incident_details['status'] = "pending"
       incident_details['comment'] = comment
       incident_details['CreatedOn'] = date.today()
       incident_details['id'] = len(incidents_list) + 1

       incidents_list.append(incident_details)
       incidents = len(self.incidents_list)
       print(incidents)
       newIncident = self.incidents_list[incidents - 1]
       return jsonify({
           "status": 201,
           "message": "Created succesfully",
           "data": newIncident
       })

    # method to GET all incidents
   def get_all(self):
        return jsonify({
            "incidents" : self.incidents_list
    })
  
   def getById(self, id):
        for item in incidents_list:
            if item['incidentType'] == 'redflag' and item['id'] == int(id):
                return item
        return "Record not found"

   def checkRecordIfExist(self, id):
        for item in incidents_list:
            if item['incidentType'] == 'redflag' and item['id'] == int(id):
                return True 
        return False

   def editLocation(self, id, attribute):
       if self.checkRecordIfExist(id):
           item = self.getById(id)
           item['location'] = attribute
           return jsonify({
               "status": 201,
               "message": "Patched successfully",
               "data": self.getById(id)
           })
       return jsonify({
            "status": 404,
            "message": "Record with that ID does not exist."
            })
   
   def editComment(self, id, attribute):
       if self.checkRecordIfExist(id):
           item = self.getById(id)
           item['comment'] = attribute
           return jsonify({
               "status": 201,
               "message": "Patched successfully",
               "data": self.getById(id)
           })
       return jsonify({
            "status": 404,
            "message": "Record with that ID does not exist."
            })

   def deleteIncident(self,id):
       if self.checkRecordIfExist(id):
           for item in incidents_list:
               if item['id'] == int(id):
                   incidents_list.pop(incidents_list.index(item))
                   return jsonify({
                       "status": 204,
                       "data": [{
                           "Id": id,
                           "message": "red-flag record has been deleted"
                       }]
                   })
       return jsonify({
            "status": 404,
            "message": "Record with that ID does not exist."
            })     