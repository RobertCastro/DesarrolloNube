from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from routes import routes
from flask_sqlalchemy import SQLAlchemy


import logging
logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

db = SQLAlchemy()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://admin:admin@localhost/idlr_db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = 'super-secreto'

    db.init_app(app)
    CORS(app)
    jwt.init_app(app)
    routes(app)
    
    return app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)