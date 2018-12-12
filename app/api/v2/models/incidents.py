from datetime import date
from flask import g
from app.db_config import conn
cur = conn.cursor()


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
        return incidents

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
