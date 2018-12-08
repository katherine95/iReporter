from flask_restful import Resource
from app.api.v1.models.users import Users as UserModel

userObject = UserModel()


class Users(Resource):
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
        """function to get all users"""
        response = self.userObject.get_all()
        return response
