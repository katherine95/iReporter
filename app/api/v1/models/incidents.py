from datetime import date

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
        return incident_details

    def validate_data(self, data):
        """validate user details"""
        try:
            # check if incidentType has letters only
            if not data['incidentType'].strip().isalpha():
                return "incidentType can only contain letters only"
            # check if the incidentType is more than 7 characters
            elif len(data['incidentType'].strip()) < 7:
                return "incidentType must be more than 7 characters"
            # check if the comment is more than 15 characters
            elif len(data['comment'].strip()) < 15:
                return "comment must be more than 15 characters"
            # check if the location is more than 3 characters
            elif len(data['location'].strip()) < 3:
                return "location must be more than 3 characters"
            # check if id is an integer
            elif not isinstance(data['createdBy'], int):
                return "createdby must be an integer"
            else:
                return "valid"
        except Exception as error:
            return "please provide all the fields, missing " + str(error)   

    def validate_patch_data(self, data, attribute):
        """validate patch data"""
        if attribute == 'location':
            if len(data['location'].strip()) < 3:
                return "Location should be more than 3 characters"
        elif attribute == 'comment':
            if len(data['comment'].strip()) < 15:
                return "Comment should be more than 15 characters"
        return "valid"

    def get_all_incidents(self):
        """Function to GET all incidents"""
        if len(incidents_list) < 1:
            return "You have no incidents created"
        return self.incidents_list

    def get_incident_by_id(self, id):
        """function to GET a single incident by id"""
        item = [item for item in incidents_list if item['id'] == id]
        if len(item) > 0:
            return item
        return False

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

    def delete_single_incident(self, id):
        """function to delete a specific incident"""
        if self.check_if_record_exist(id):
            for item in incidents_list:
                if item['id'] == int(id):
                    incidents_list.pop(incidents_list.index(item))
                    return "The record has been deleted"
        return "Record with that ID does not exist."
