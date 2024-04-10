from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_restful import Api
from flask_restful import Resource

class RootResource(Resource):
    def get(self):
        return {'message': '¡Flask app running in a Docker container! 🐳🐍🚀'}
    
def routes(app):
    api = Api(app)
    api.add_resource(RootResource, '/')
