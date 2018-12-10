from flask import jsonify
from datetime import date
from app.db_config import conn
from passlib.hash import sha256_crypt
cur = conn.cursor()


class SignUp(object):
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

            return "success"
        return "Username Is already taken"

    def serialiser_user(self, user):
        return dict(
            id=user[0],
            username=user[4],
            email=user[5],
            isAdmin=user[10],
            password=user[8],
            firstname=user[1],
            lastname=user[2],
            othernames=user[3],
            phonenumber=user[6],
            createdOn=user[7]
        )

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
        cur.execute("SELECT * FROM users WHERE username = %s;", (username,))
        user = cur.fetchone()
        if user:
            return self.serialiser_user(user)
        return "Username doesnt exist"

    def hash_password(self, password):
        """Hash Password """
        h_pass = sha256_crypt.hash(password)
        return h_pass
