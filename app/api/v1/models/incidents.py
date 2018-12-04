from flask import jsonify, request, make_response
from datetime import date
import uuid
incidents_list = []
class Incident(object):
    """class that deals with incidents data"""

    def __init__(self):
        self.incidents_list = incidents_list

    def create_incident(self, incidentType, comment, createdBy, location):
        """Function to create an incident"""
        incident_details = {}
        incident_details['createdBy'] = createdBy
        incident_details['incidentType'] = incidentType
        incident_details['location'] = location
        incident_details['status'] = "pending"
        incident_details['comment'] = comment
        incident_details['CreatedOn'] = date.today()
        incident_details['id'] = len(incidents_list) + 1

        self.incidents_list.append(incident_details)
        return incidents_list

    def get_all_incidents(self):
        """Function to GET all incidents"""
        if len(incidents_list) == 0:
            return "You have no incidents created"
        return self.incidents_list
    
    def get_incident_by_id(self, id):
        """function to GET a single incident by id"""
        for item in incidents_list:
            if item['id'] == int(id):
                return item
            else:
                return  "Record with that ID does not exist."
                
    def check_if_record_exist(self, id):
        """function to check if a record exist by id"""
        for item in incidents_list:
            if item['id'] == int(id):
                return True 
        return False

    def edit_incident_location(self, id, attribute):
        """function to edit an incident's location"""
        if self.check_if_record_exist(id):
            item = self.get_incident_by_id(id)
            item['location'] = attribute
            return self.get_incident_by_id(id)
        return "Record with that ID does not exist."
    
    def edit_incident_comment(self, id, attribute):
        """function to edit an incident's comment"""
        if self.check_if_record_exist(id):
            item = self.get_incident_by_id(id)
            item['comment'] = attribute
            return self.get_incident_by_id(id)
        return "Record with that ID does not exist."

    def delete_single_incident(self,id):
        """function to delete a specific incident"""
        if self.check_if_record_exist(id):
            for item in incidents_list:
                if item['id'] == int(id):
                    incidents_list.pop(incidents_list.index(item))
                    return "The record has been deleted"
        return "Record with that ID does not exist."