from flask import jsonify, request, make_response
from datetime import date
import uuid
from passlib.hash import sha256_crypt

users_list = []

class Users(object):
   """class that deals with users information"""

   def __init__(self):
       self.users_list = users_list

    # Method to register   
   def create(self, firstname, lastname, othernames, email, phoneNumber, username, password):
       hash_pass = self.hash_password(password)

       user_details = {}
       user_details['firstname'] = firstname
       user_details['lastname'] = lastname
       user_details['othernames'] = othernames
       user_details['email'] = email
       user_details['phoneNumber'] = phoneNumber
       user_details['username'] = username
       user_details['isAdmin'] = False
       user_details['registered'] = date.today()
       user_details['password'] = hash_pass
       user_details['id'] = len(users_list) + 1


       users_list.append(user_details)
       users = len(self.users_list)
       print(users)
       newUser = self.users_list[users - 1]
       return jsonify({
           "status": 201,
           "message": "User registered succesfully",
           "data": newUser
       })

   def hash_password(self, password):
       """Hash Password """
       h_pass = sha256_crypt.encrypt(password)
       return h_pass

   # method to GET all users
   def get_all(self):
       if len(users_list) == 0:
           return jsonify({
               "status": 200,
               "message": "There are no registered users" 
               })
       return jsonify({
            "users" : self.users_list
       })    

   def login(self, username, password):
       for user in users_list:
           if username == user['username']:
               if password == user['password']:
                   return "user successfully logged in"
               else:
                   return "wrong password or username"
       return "user does not exist" 

   def get_user_by_id(self, id):
       for user in users_list:
           if user['id'] == id:
               return user