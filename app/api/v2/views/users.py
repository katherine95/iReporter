from flask_restful import Resource
from app.api.v2.models.users import SignUp as UserModel
from flask import jsonify, request, make_response


class Users(Resource):
    """class that deals with users request functions"""
    def __init__(self,):
        self.userObject = UserModel()

    def post(self):
        """function to create a new user"""
        users_data = request.get_json()
        res = self.userObject.validate_data(users_data)
        if res == "valid":
            firstname = users_data['firstname']
            lastname = users_data['lastname']
            othernames = users_data['othernames']
            email = users_data['email']
            phonenumber = users_data['phonenumber']
            username = users_data['username']
            password = users_data['password']
            user = UserModel(
                firstname, lastname, othernames, email, phonenumber, username,
                password)
            response = user.register_user()
            if response == "success":
                return make_response(jsonify({
                    "status": 201,
                    "message": "User registered succesfully",
                    "data": self.userObject.get_by_username(username)
                }), 201)
            return make_response(jsonify({
                    "status": 409,
                    "message": response
                }), 409)
        return make_response(jsonify({
                "status": 405,
                "message": res
            }), 405)

    def get(self):
        resp = self.userObject.get_all_users()
        return make_response(jsonify({
            "status": 200,
            "data": resp,
            "message": "all users fetched successfully"
        }))


class Login(Resource):
    """class that deals with a single user request functions"""
    def __init__(self):
        self.userObject = UserModel()

    def post(self):
        """function to get a single user by username"""
        res = self.userObject.login_user()
        if res is False:
            return make_response(jsonify({
                "status": 404,
                "message": "Username and password dont match"
            }), 404)
        return make_response(jsonify({
            "status": 200,
            "data": res,
            "message": "User fetched successfully"
        }), 200)
