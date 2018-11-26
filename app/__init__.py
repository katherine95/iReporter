<<<<<<< HEAD
#from flask_restful import Api, Resource
#from flask import Blueprints
#from api.v1 import version_one as v1

#def create_app():
    #app = Flask()
    #app.register_blueprint(v1)
    #return app
=======
from flask import Flask
from flask_restful import Resource, Api

# local import
from instance.config import app_config

# initialize database


def create_app(app_config):
    app = Flask(__name__)
    api = Api(app)
    app.config.from_object(app_config)
    return app

    
>>>>>>> 2fdd1bd054df05ed34868cfe47204d359e3ae422
