from flask import jsonify, request
from datetime import date
from app.db_config import conn
from passlib.hash import sha256_crypt
import re
cur = conn.cursor()


class Users(object):
    """class that deals with users information"""

    def __init__(self, firstname=None, lastname=None, othernames=None,
                 email=None, phonenumber=None, username=None, password=None):
        self.firstname = firstname
        self.lastname = lastname
        self.othernames = othernames
        self.email = email
        self.phonenumber = phonenumber
        self.username = username
        self.password = password
        self.isAdmin = False

    def save(self):
        conn.commit()

    def register_user(self):
        if self.check_if_username_exist(self.username) is False:
            hash_pass = self.hash_password(self.password)
            cur.execute(
                """
                INSERT INTO users (firstname, lastname, othernames,
                 email, phonenumber, username, password, isAdmin)
                VALUES (%s , %s, %s, %s, %s , %s, %s, %s) RETURNING user_id;
                """,
                (self.firstname, self.lastname, self.othernames,
                 self.email, self.phonenumber, self.username,
                 hash_pass, self.isAdmin))
            self.save()

            return True
        return False

    def serialiser_user(self, user):
        return dict(
            user_id=user[0],
            username=user[4],
            email=user[5],
            isAdmin=user[10],
            firstname=user[1],
            lastname=user[2],
            othernames=user[3],
            phonenumber=user[6],
            createdOn=user[7]
        )

    def get_all_users(self):
        """ fetch all registered users """
        cur.execute("SELECT * FROM users")
        users = cur.fetchall()
        users_list = []
        for user in users:
            users_list.append(self.serialiser_user(user))
        return users_list

    def check_if_username_exist(self, username):
        """ check if user with the same username already exist """
        cur.execute("SELECT * FROM users WHERE username = %s;", (username,))
        user = cur.fetchone()
        if user:
            return True
        else:
            return False

    def get_by_username(self, username):
        """ Get user by username """
        cur.execute("SELECT * FROM users WHERE username = %s", (username,))
        user = cur.fetchone()
        if user:
            return self.serialiser_user(user)
        return False

    def get_admin_access_rights(self, isAdmin):
        """ check if user is an admin """
        cur.execute("SELECT * FROM users WHERE isAdmin = %s;", (True,))
        admin = cur.fetchone()
        print(admin)
        if admin:
            return True
        else:
            return False

    def get_user_by_id(self, id):
        """ Get user by username """
        cur.execute("SELECT * FROM users WHERE user_id = %s", (id,))
        user = cur.fetchone()
        if user:
            return self.serialiser_user(user)
        return False

    def update_user_admin_status(self, username, isAdmin):
        """function to allow an admin user create a new admin"""
        cur.execute("UPDATE users SET isAdmin=%s WHERE username = %s;",
                    (isAdmin, username,))
        self.save()
        return self.get_by_username(username)

    def hash_password(self, password):
        """Hash Password """
        h_pass = sha256_crypt.hash(password)
        return h_pass

    def login_user(self):
        """validate user log's in with valid username and password"""
        user_details = request.get_json()
        if self.check_if_username_exist(user_details['username']):
            cur.execute("SELECT password FROM users WHERE username = %s",
                        (user_details['username'],))
            reg_password = cur.fetchone()
            if sha256_crypt.verify(user_details['password'], reg_password[0]):
                return True
            return False
        return False

    def validate_data(self, data):
        """validate user details"""
        try:
            # check if email is valid
            if not re.match("^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+[a-zA-Z0-9-.]+$",
                            data['email'].strip()):
                return "provide a valid email"

            # check if firstname has atleast 3 characters
            elif len(data['firstname'].strip()) < 3:
                return "firstname must have more than 3 characters"

            # check if lastname has atleast 3 characters
            elif len(data['lastname'].strip()) < 3:
                return "lastname must have more than 3 characters"

            # check if username has atleast 5 characters
            elif len(data['username'].strip()) < 5:
                return "username must have more than 3 characters"

            # check if username starts with letters and contains only
            # underscore as special character
            elif not re.match("[a-zA-Z]{3,}_*[0-9_]*[a-zA-Z]*_*",
                              data['username'].strip()):
                return "username must start with letters before number or\
                        underscore"

            # check if password has more than 6 characters
            elif len(data['password'].strip()) < 6:
                return "password must have atleast 6 characters"

            # check if phone number has 10 characters
            elif not len(data['phonenumber'].strip()) == 10:
                return "phone number must have 10 characters"

            # check if id is an integer
            elif not re.match("[0-9]",
                              data['phonenumber'].strip()):
                return "phonenumber must contain only numbers"

            else:
                return "valid"
        except Exception as error:
            return "please provide all the fields, missing " + str(error)
