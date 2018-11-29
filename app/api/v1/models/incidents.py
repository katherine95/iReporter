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

   def editAttribute(self, id, attribute, change):
       change = request.get_json()['change']
       allowed = ['comment', 'location']

       if self.getById(id):
           if attribute in allowed:
               self.editAttribute(id,attribute,change)
               return make_response(jsonify({
                   "status":200,
                   "data" :[{
                       "id":id,
                       "message": "Record is updated "
                   }]
               }), 200)
           else:
               return make_response(jsonify({
                   "status": 404,
                   "error":"Attribute cannot be edited"
                   }), 404)
       else:
           return make_response(jsonify({
               "status":404,
               "error":"record not found"
               }), 404)     

   def deleteIncident(self,id):
       for item in incidents_list:
           if item.get('id') == int(id):
               del item
           return {"status": 204, "incidents" : incidents_list ,"message":"Incident successfully deleted"}

    #    [item for item in incidents_list if item.get('id') == int(id)]
    #    return {"status": 204, "incidents" : incidents_list ,"message":"Incident successfully deleted"}

    #    for item in incidents_list:
    #        if item['id'] == int(id):
    #            item.remove(incidents_list[0])

           
       
                    