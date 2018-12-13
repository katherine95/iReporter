from datetime import date
from flask import g
from app.db_config import conn
cur = conn.cursor()


def serialiser_incident(incident):
    return dict(
        id=incident[0],
        createdOn=incident[1],
        createdBy=incident[2],
        incidentType=incident[3],
        location=incident[4],
        status=incident[5],
        comment=incident[6]
    )


class Incident(object):
    """class that deals with incidents data"""

    def __init__(self, incidentType=None, location=None, comment=None,
                 createdBy=None):
        self.incidentType = incidentType
        self.location = location
        self.comment = comment
        self.createdBy = createdBy

    def save(self):
        conn.commit()

    def create_incident(self):
        """Function to create an incident"""
        createdOn = date.today()
        status = "pending"
        cur.execute(
            """
            INSERT INTO incidents (incidentType, location, comment, status,
            createdOn, createdBy)
            VALUES (%s , %s, %s, %s, %s , %s) RETURNING id;
            """,
            (self.incidentType, self.location, self.comment, status,
             createdOn, self.createdBy))
        id = cur.fetchone()[0]
        self.save()
        return id

    def check_if_comment_exist(self, comment):
        """ check if incident with the same comment already exist """
        cur.execute("SELECT * FROM incidents WHERE comment = %s;", (comment,))
        comment = cur.fetchone()
        if comment:
            return True
        else:
            return False

    def get_all_incidents(self):
        """Function to GET all incidents"""
        cur.execute("SELECT * FROM incidents")
        incidents = cur.fetchall()
        incidents_list = []
        for item in incidents:
            incidents_list.append(serialiser_incident(item))

        return incidents_list

    def get_incident_by_id(self, id):
        """function to GET a single incident by id"""
        cur.execute("SELECT * FROM incidents WHERE id = %s;", (id,))
        incident = cur.fetchone()
        if incident:
            return serialiser_incident(incident)
        return False

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

            else:
                return "valid"
        except Exception as error:
            return "please provide all the fields,\
             missing " + str(error)

    def update_incident_status(self, id, status):
        """function to allow an admin user to update status record"""
        cur.execute("UPDATE incidents SET status=%s WHERE id = %s;",
                    (status, id,))
        self.save()
        return self.get_incident_by_id(id)

    def update_incident_comment(self, id, comment):
        """function to allow a user to update comment of a record"""
        cur.execute("UPDATE incidents SET comment=%s WHERE id = %s;",
                    (comment, id,))
        self.save()
        return self.get_incident_by_id(id)

    def update_incident_location(self, id, location):
        """function to allow a user to update location of a record"""
        cur.execute("UPDATE incidents SET location=%s WHERE id = %s;",
                    (location, id,))
        self.save()
        return self.get_incident_by_id(id)

    def delete_incident_record(self, id):
        """function to allow an admin user to update status record"""
        cur.execute("DELETE FROM incidents WHERE id = %s;",
                    (id,))
        self.save()
        return True
