import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'tu_clave_secreta')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'postgresql://admin:admin@localhost/idlr_db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY', 'tu_jwt_clave_secreta')
    UPLOAD_FOLDER = '../uploads'
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB
