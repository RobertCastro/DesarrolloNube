from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_restful import Api
from flask_restful import Resource
from controllers.video_controller import upload_video

class RootResource(Resource):
    def get(self):
        return {'message': '¡Flask app running in a Docker container! 🐳🐍🚀'}

class UploadVideoResource(Resource):
        def post(self):
            return upload_video()
    
def routes(app):
    api = Api(app)
    api.add_resource(RootResource, '/')
    api.add_resource(UploadVideoResource, '/api/tasks')
