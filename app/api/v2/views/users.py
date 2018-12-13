from flask_restful import Resource
from app.api.v2.models.users import Users as UserModel
from flask import jsonify, request, make_response, g
from flask_jwt_extended import (create_access_token, create_refresh_token,
                                jwt_required, jwt_refresh_token_required,
                                get_jwt_identity, get_raw_jwt)


class SignUp(Resource):
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
                username = request.get_json()['username']
                user = self.userObject.get_by_username(username)
                user_id = user['user_id']
                access_token = create_access_token(identity=user_id)
                return make_response(jsonify({
                    "status": 201,
                    "message": "User registered succesfully",
                    "data": [{
                        "user": self.userObject.get_by_username(username),
                        "token": access_token
                    }]
                }), 201)
            return make_response(jsonify({
                    "status": 409,
                    "message": response
                }), 409)
        return make_response(jsonify({
                "status": 405,
                "message": res
            }), 405)

    @jwt_required
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
        username = request.get_json()['username']
        user = self.userObject.get_by_username(username)
        user_id = user['user_id']
        access_token = create_access_token(identity=user_id)

        return make_response(jsonify({
            "status": 200,
            "data": [{
                "token": access_token,
                "user": self.userObject.get_by_username(username)
            }],
            "message": "User successfully logged in"
        }), 200)

    @jwt_required
    def get(self):
        pass
