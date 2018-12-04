from flask import jsonify, request, make_response, session
from flask_restful import Resource
from app.api.v1.models.users import Users as UserModel

userObject = UserModel()

class Users(Resource):
    """ A class to handle user registration and login methods of a user"""
    def __init__(self):
        self.userObject = UserModel()
     
    def post(self):
        users_data = request.get_json()
        firstname = users_data['firstname']
        lastname = users_data['lastname']
        othernames = users_data['othernames']
        email = users_data['email']
        phoneNumber = users_data['phoneNumber']
        username = users_data['username']
        password = users_data['password']
       
        response = self.userObject.create(firstname, lastname, othernames, email, phoneNumber, username, password)
        return make_response(response)

    def get(self):
        # GET method begins here 
        response = self.userObject.get_all()
        return response

class User_login(Resource):

    def __init__(self):
        self.userObject = UserModel() 
        
    def login(self):
        user_details = request.get_json
        username = user_details['username']
        password = user_details['password']
        response = self.userObject.login(username,password)

        for user in userObject.users_list:
            if user['username'] == username:
                session['id'] = user['id']
                return make_response(jsonify({
                    "status":200,
                    "data":[{
                        "User":response,
                        "message":"login successful"
                    }]
                }))
          