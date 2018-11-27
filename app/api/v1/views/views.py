from flask import jsonify, request
from app.api.v1 import v1 

@v1.route('/')
def index():
    return jsonify({"message" : "It works"})

