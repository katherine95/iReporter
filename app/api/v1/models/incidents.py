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

        incidents_list.append(incident_details)
        incidents = len(self.incidents_list)
        newIncident = self.incidents_list[incidents - 1]
        return newIncident

    def get_all_incidents(self):
        """Function to GET all incidents"""
        if len(incidents_list) == 0:
            return "You have no incidents created"
        return self.incidents_list
    
    def get_incident_by_id(self, id):
        """function to GET a single incident by id"""
        for item in incidents_list:
            item = [item for item in incidents_list if item['id'] == id]
            if len(item) > 0:
                return item
            return  "Record with that ID does not exist."
                
    def check_if_record_exist(self, id):
        """function to check if a record exist by id"""
        for item in incidents_list:
            if item['id'] == id:
                return True 
        return False

    def patch_incident(self, id, patch_data, attribute):
        """function to edit an incident's location"""
        if self.check_if_record_exist(id):
            item = self.get_incident_by_id(id)
            if attribute == 'location':
                item[0]['location'] = patch_data['location']
                return self.get_incident_by_id(id)
            item[0]['comment'] = patch_data['comment']
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